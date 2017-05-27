import lib.db as db
import lib.air as Air

class air:
	def __init__(self):
		self.db = db.mongo('air', 'element')
		self.airFilter = Air.filter()

	def timeseries(self, station, date, item='PM2.5'):
		timeseries = []
		PM25 = self.db.findOne({'測站': station, '測項': item, '日期':date})
		timeseries.extend(self.airFilter.dayPolution(PM25))

		return timeseries