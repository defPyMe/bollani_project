from datetime import datetime


#getting at least the same hour
def get_current_date_time():
    t=datetime.now()
    dt_string = t.strftime("%Y/%m/%d %H:%M:%S")
    t_corrected = (str(dt_string).replace("/", "").replace(" ", "").replace(":", ""))[0:11]
    return t_corrected

print(get_current_date_time())