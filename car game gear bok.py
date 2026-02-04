gear="n"
gear="1"
gear="2"
gear="3"
gear="4"
gear="5"
gear="r"

cluch="c"

stop="b"

speed="a"

handle_break="h"

key="on"

if key=="on":
    print("I'm going to play car game gear box")
else:
    print("the car is off")

print("the car is on nutral")

cluch=input("")
gear=input("")
speed=int(input(""))

if cluch=="c" and gear=="1":
    if speed<20:
        print("the car is on gear 1")
elif cluch=="c" and gear=="2":
    if speed>20 and speed<40:
        print("the car is on gear 2")

elif cluch=="c" and gear=="3":
    if speed>40 and speed<60:
        print("the car is on gear 3")

elif cluch=="c" and gear=="4":
    if speed>60 and speed<80:
        print("the car is on gear 4")

elif cluch=="c" and gear=="5":
    if speed>80:
        print("the car is on gear 5")

elif cluch=="c" and gear=="r":
    print("the car is on gear r")
else:
    print("something wrong")


