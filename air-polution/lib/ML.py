import numpy as np
import pandas as pd
import math
import datetime
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error


class deepLearning:
    def __init__(self, data):
        self.dataset = pd.DataFrame(data).values.astype('float32')

    def __reshapeTimeseries(self, data, lookBack):
        dataset = pd.DataFrame(data).values.astype('float32')
        dataX, dataY = [], []
        for i in range(len(dataset) - lookBack - 1):
            a = dataset[i:(i + lookBack), 0]
            dataX.append(a)
            dataY.append(dataset[i + lookBack, 0])

        return np.array(dataX), np.array(dataY)

    def model1(self, trainRatio=0.67, epochs=1):
        # normalize the dataset
        scaler = MinMaxScaler(feature_range=(0, 1))
        dataset = scaler.fit_transform(self.dataset)

        # split into train and test sets
        trainSize = int(len(dataset) * trainRatio)
        testSize = len(dataset) - trainSize
        train, test = dataset[0:trainSize,
                              :], dataset[trainSize:len(dataset), :]

        # reshape into X=t and Y=t+1
        lookBack = 3
        trainX, trainY = self.__reshapeTimeseries(train, lookBack)
        testX, testY = self.__reshapeTimeseries(test, lookBack)

        # reshape input to be [samples, time steps, features]
        trainX = np.reshape(trainX, (trainX.shape[0], trainX.shape[1], 1))
        testX = np.reshape(testX, (testX.shape[0], testX.shape[1], 1))

        # create and fit the LSTM network
        batchSize = 1
        model = Sequential()
        model.add(LSTM(4, batch_input_shape=(batchSize, lookBack, 1),
                       stateful=True, return_sequences=True))
        model.add(LSTM(4, batch_input_shape=(
            batchSize, lookBack, 1), stateful=True))
        model.add(Dense(1))
        model.compile(loss='mean_squared_error', optimizer='adam')
        for i in range(10):
            model.fit(trainX, trainY, epochs=epochs,
                      batch_size=batchSize, verbose=2, shuffle=False)
            model.reset_states()

        # make predictions
        trainPredict = model.predict(trainX, batch_size=batchSize)
        model.reset_states()
        testPredict = model.predict(testX, batch_size=batchSize)

        # invert predictions
        trainPredict = scaler.inverse_transform(trainPredict)
        trainY = scaler.inverse_transform([trainY])
        testPredict = scaler.inverse_transform(testPredict)
        testY = scaler.inverse_transform([testY])

        # calculate root mean squared error
        trainScore = math.sqrt(mean_squared_error(
            trainY[0], trainPredict[:, 0]))
        print('Train Score: %.2f RMSE' % (trainScore))
        testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:, 0]))
        print('Test Score: %.2f RMSE' % (testScore))

        # shift train predictions for plotting
        trainPredictPlot = np.empty_like(dataset)
        trainPredictPlot[:, :] = np.nan
        trainPredictPlot[lookBack:len(
            trainPredict) + lookBack, :] = trainPredict

        # shift test predictions for plotting
        testPredictPlot = np.empty_like(dataset)
        testPredictPlot[:, :] = np.nan
        testPredictPlot[len(trainPredict) + (lookBack * 2) +
                        1:len(dataset) - 1, :] = testPredict

        # plot baseline and predictions
        plt.plot(scaler.inverse_transform(dataset))
        plt.plot(trainPredictPlot)
        plt.plot(testPredictPlot)
        plt.savefig('model1-' + str(datetime.datetime.now()) + '-result.png')
