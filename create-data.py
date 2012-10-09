import random
import datetime

ranges = {
	"govuk": [10, 50],
	"directgov": [100, 200],
	"buslink": [60, 80]
}
names = ["govuk", "directgov", "buslink"]

start = datetime.datetime(2012, 9, 21)

print("date,govuk,directgov,buslink")
for i in range(28):
	values = [random.randint(ranges[name][0], ranges[name][1]) for name in names]
	print("%s,%s,%s,%s" % (start.strftime("%Y-%m-%d"), values[0], values[1], values[2]))
	start += datetime.timedelta(days=1)