import time
from threading import Thread
from random import randint
#0 = Vacant seat
#1 = Occupied seat
barbers_chairs = [0,0,0]
lounge_chairs = [0,0,0]
extra_lounge_chairs = [0,0,0,0]
cash_register = [0]

def spawn_customer():
    for i in range(5):
        spawn_time = randint(2,5)
        time.sleep(spawn_time)
        Thread(target=customer_thread).start()
def start_haircut(seat):
    print("Haircut started")
    barbers_chairs[seat] = 1

    hair_time = randint(3, 20)
    time.sleep(hair_time)

    print("Haircut ended")
    reg = queue_open(cash_register)
    if reg != -1:
        start_cash_register()
    barbers_chairs[seat] = 0


def start_cash_register():
    cash_time = randint(1, 2)
    time.sleep(cash_time)
    print("Payment complete")
    print("Thank you")
    print("get outta my dang store!")

def customer_thread():
    print("New customer arrived")
    seat = queue_open(barbers_chairs)
    if seat != -1:
        start_haircut(seat)
    else:
        print("WAITING ROOM!!!")


def queue_open(queue):
    for index, chair in enumerate(queue):
        if chair == 0:
            return index
    return -1

spawn_customer()