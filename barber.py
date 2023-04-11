import threading
import time
from threading import Thread
from random import randint

# 0 = Vacant seat
# 1 = Occupied seat
barbers_chairs = [0, 0, 0]
lounge_chairs = [0, 0, 0]
extra_lounge_chairs = [0, 0, 0, 0]

cash_register = threading.Semaphore(1)  # when cash register is occupied
open_barber = threading.Semaphore(1)  # when all barbers are occupied
open_lounge = threading.Semaphore(1)  # when all first waiting room chairs are occupied
stop_spawning = False
def day():
    hours_open = 7
    print('Barber shop has opened: 10:00AM')
    time.sleep(60*hours_open)
    print('Barber shop has closed: 5:00PM')
    global stop_spawning
    stop_spawning = True
def spawn_customers():
    # start spawning customers
    spawn_time = randint(2, 20)
    time.sleep(spawn_time)
    global stop_spawning
    if not stop_spawning:
        Thread(target=customer_thread).start()

def start_haircut(seat):
    barbers_chairs[seat] = 1
    if queue_open(barbers_chairs) == -1:
        # all barbers busy
        print('----ALL BARBERS BUSY------')
        open_barber.acquire()

    print("Haircut started")
    hair_time = randint(6, 15)
    time.sleep(hair_time)
    print("Haircut ended")

    # block cash register
    cash_register.acquire()
    start_cash_register()
    barbers_chairs[seat] = 0

    # make register and barber availible
    cash_register.release()
    open_barber.release()


def start_cash_register():
    cash_time = randint(1, 2)
    time.sleep(cash_time)
    print("--Payment complete--")
    print("Thank you")
    print("get outta my dang store!")


def customer_thread():
    print("New customer arrived")
    # check barber chairs
    seat = queue_open(barbers_chairs)
    if seat != -1:
        start_haircut(seat)

    # no barbers avaliable
    else:
        # check waiting room
        seat = queue_open(lounge_chairs)
        if seat != -1:
            wait_room(seat)
        else:
            # check extra waiting room
            seat = queue_open(extra_lounge_chairs)
            if seat != -1:
                extra_wait_room(seat)
            else:
                print('All chairs occupied!')
                print('Im never coming back here again!')


def wait_room(seat):
    print("Customer joins waiting room.")
    lounge_chairs[seat] = 1
    if queue_open(lounge_chairs) == -1:
        # all lounge busy
        print('----PRIMARY LOUNGE FULL------')
        open_lounge.acquire()

    # wait for open barber
    #start counting time spent in waiting room
    wait_thread = threading.Thread(target=timer)
    wait_thread.start()

    open_barber.acquire()

    if wait_thread == 1:
        print("Customer left, waited too long")
        return

    print("Customer moves to barber chair")
    lounge_chairs[seat] = 0
    open_lounge.release()
    start_haircut(seat)


def extra_wait_room(seat):
    print("Customer joins extra waiting room.")
    extra_lounge_chairs[seat] = 1
    # wait for open lounge seating
    open_lounge.acquire()
    print("Customer moves to primary waiting room")
    extra_lounge_chairs[seat] = 0
    wait_room(seat)


def queue_open(queue):
    for index, chair in enumerate(queue):
        if chair == 0:
            return index
    return -1
def timer():
    time_till_leave = 30
    time.sleep(time_till_leave)
    return 1

def main():
    today = threading.Thread(target=day)
    today.start()
    global stop_spawning
    while not stop_spawning:
        spawn_customers()
    today.join()


main()
