# from pyautogui import countdown
# speed=int(input("enter a num:"))
# while speed>=10:
#     countdown(speed)
#     speed+=1
#     print(countdown(speed))



# i=int(input("enter speed"))
# for i in range(180):
#     i+=1
#     print(i)


# i=int(input(""))
# while i>0:
#     print(i)
#     i+=1



import threading
import time

def speed():
    for i in range(180):
        print("car speed is :",i)
        time.sleep(0.5)

s1=threading.Thread(target=speed)
s1.start()
s1.join()

