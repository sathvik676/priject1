import threading
import time

def speed():
    for speed in range(180):
        print("car speed is :",speed)
        if speed == 0:
            print("netural, change the gear to 1 or "R" and move the car.")


        elif speed >= 18 and speed <= 22:
            print("swift the gear to 2 or 1")

        elif speed >= 38 and speed <= 42:
            print("swift the gear to 3 or 2")

        elif speed >= 58 and speed <= 62:
            print("swift the gear to 4 or 3")

        elif speed >= 78 and speed <= 82:
            print("swift the gear to 5 or 4")
        time.sleep(0.5)





s1=threading.Thread(target=speed)


s1.start()


s1.join()

