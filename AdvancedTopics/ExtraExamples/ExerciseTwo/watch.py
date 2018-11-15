import datetime # import datetime module
# This is also valid but will just import the datetime attribute 
# from datetime import datetime
import time # import time module
import os # import os module

while(True):
    os.system('clear') # clear the screen, clear for Linux and cls for Windows
    dt = datetime.datetime.now() # get the current time
    print("{}:{}:{}".format(dt.hour, dt.minute, dt.second)) #format the time
    time.sleep(1) # the function sleep pause the execution of the program n seconds 

