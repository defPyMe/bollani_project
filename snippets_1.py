

from datetime import datetime
import dateutil.relativedelta

#calculating current date for the timestamp
today = datetime.now()
current_month = today.strftime("%B")
#calculating previous month date 
last_month = today + dateutil.relativedelta.relativedelta(months=-1)
previous_month = last_month.strftime("%B")


print(current_month, previous_month)