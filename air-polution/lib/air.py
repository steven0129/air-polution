import numpy as np
import math
import datetime
import time


class index:

    # O3,8hr	：	取最近連續8小時移動平均值 (例如今日上午10點發布的O3的8小時濃度平均值，是取今日上午2點至上午9點監測數據的平均值。）
    # O3	：	取即時濃度值
    # PM2.5	：	0.5 × 前12小時平均 + 0.5 × 前4小時平均 (前4小時2筆有效，前12小時6筆有效）
    # PM10	：	0.5 × 前12小時平均 + 0.5 × 前4小時平均 (前4小時2筆有效，前12小時6筆有效）
    # CO	：	取最近連續8小時移動平均值 (例如今日上午10點發布的CO的8小時濃度平均值，是取今日上午2點至上午9點監測數據的平均值。）
    # SO2	：	取即時濃度值
    # SO2,24hr	：	取最近連續24小時濃度平均值 (例如今日上午10點發布的SO2的24小時濃度平均值，是取前1天上午10點至今日上午9點監測數據的平均值。）
    # NO2	：	取即時濃度值

    # PM2.5移動平均值有效位數為小數點以下第1位，會取到小數點以下第2位採四捨五入方式進位，O3的8小時移動平均值及PM10移動平均值有效位數為整數位，會取到小數點以下第1位，採四捨五入方式進位。

    def __init__(self, O38hr, O3, PM25, PM10, CO, SO2, SO224, NO2):
        self.O38hr = O38hr
        self.O3 = O3
        self.PM25 = PM25
        self.PM10 = PM10
        self.CO = CO
        self.SO2 = SO2
        self.SO224 = SO224
        self.NO2 = NO2

    def AQI(self):
        O38hr_pre = math.floor(np.average(self.O38hr))
        PM25_pre = round(
            0.5 * np.average(self.PM25[0:11]) + 0.5 * np.average(self.PM25[8:11]), 1)
        PM10_pre = round(
            0.5 * np.average(self.PM10[0:11]) + 0.5 * np.average(self.PM10[8:11]), 1)
        CO_pre = np.average(self.CO)
        SO224_pre = np.average(self.SO224)

        return max(O38hr_pre, self.O3, PM25_pre, PM10_pre, CO_pre, self.SO2, SO224_pre, self.NO2)


class info:
    def __init__(self):
        self.station = ['二林', '崇倫', '南投', '埔里', '大里', '彰化', '忠明', '沙鹿', '竹山', '線西', '西屯', '豐原', '阿里山', '三重', '中山', '中壢', '古亭', '土城', '基隆', '士林', '大同', '大園', '平鎮', '新店', '新莊', '松山', '板橋', '林口', '桃園', '永和', '淡水', '汐止', '菜寮', '萬華', '萬里', '觀音', '陽明', '龍潭', '冬山', '宜蘭',
                        '三義', '新竹', '湖口', '竹東', '苗栗', '頭份', '台東', '花蓮', '關山', '金門', '馬公', '馬祖', '台南', '台西', '善化', '嘉義', '安南', '崙背', '斗六', '新港', '新營', '朴子', '麥寮', '仁武', '前金', '前鎮', '大寮', '小港', '屏東', '左營', '復興', '恆春', '林園', '楠梓', '橋頭', '潮州', '美濃', '鳳山', '三民', '泰山', '臺東', '臺南', '臺西']

    def getStation(self):
        return self.station


class filter:
    def dayPolution(self, mapper):
        temp = []
        for i in range(0, 25):
            try:
                leadingZero = str(i).zfill(2)
                if(str(mapper[leadingZero]).isdigit() == True):
                    temp.append(float(mapper[leadingZero]))
                else:
                    temp.append(0)
            except(KeyError):
                pass

        return temp
