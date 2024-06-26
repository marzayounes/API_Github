import os
from datetime import datetime
try:
    os.system('rmdir /var/log/')
except Exception as e:
    print("An error occured: "+str(e))
    print("But don't worry... We are trying different methods...")
    del e

try:
    f = open("/var/log/YourUserName.pythonanywhere.com.error.log", "w")
    time = datetime.now()
    msg = "Successfully deleted all error logs on "+str(time)+"\n"
    f.write(msg)
    f.close()
    del f
    f = open("/var/log/YourUserName.pythonanywhere.com.error.log", "r")
    print(f.read())
    del f
except Exception as e:
    print("An error occured: "+str(e)+"\n")
    print("Sorry! We couldn't delete or clear error Log file. :(")