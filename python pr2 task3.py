#created by athul raj
#date:08-10-2024
from datetime import datetime
print(datetime.now())
current_time=datetime.now()
format1=current_time.strftime("%Y-%m-%d %h:%m:%s")
print(format1)
format2=current_time.strftime("%d-%B-%y ")
print(format2)


