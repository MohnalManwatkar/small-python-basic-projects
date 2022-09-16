# first we need to import time this will allows us to use time function
import time

# let's ask the user how many second we want to countdown
seconds = int(input("how many seconds to wait? :"  ))

# let's use a range loop to count downwards
for i in range(seconds):
    print(str(seconds-i) + "seconds remain")

    time.sleep(1)
print("time is up")
# let's try it