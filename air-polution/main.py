#import lib.db as db
#import lib.air as air
#import lib.ML as ML
#import matplotlib.pyplot as plt
#import datetime

#DB = db.mongo('air', 'element')
#AirFilter = air.filter()

#PM25List = DB.find({
#    "測站": "新營", "測項": "PM2.5"
#}).sort('日期')

#timeseries = []
#for PM25 in PM25List:
#    timeseries.extend(AirFilter.dayPolution(PM25))

## plt.plot(timeseries)
## plt.savefig(str(datetime.datetime.now()) + '.png')

#dl = ML.deepLearning(timeseries)
#dl.model1(trainRatio=0.67, epochs=1)

import lib.gui.view.window as Window

win = Window.gen()
win.setTitle('test')
win.add(signal='label', text='test', x=30, y=40)
win.add(signal='label', text='tssss', x=30, y=100)
win.add(signal='button', text='tssss', x=50, y=100)
win.run()