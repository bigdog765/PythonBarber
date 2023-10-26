# Barber Shop Simulation for CSC 5991 Python

## Overview

This Python script simulates the operation of a barber shop, modeling the interaction between customers, barbers, and waiting rooms. Threading is employed to simulate concurrent activities, and semaphores are used to control access to shared resources such as barber chairs and the cash register.

## Table of Contents

- [Data Structures](#data-structures)
- [Functions](#functions)
- [Main Execution](#main-execution)
- [Global State](#global-state)
- [Notes](#notes)
- [Recommendations](#recommendations)

## Data Structures

- **barbers_chairs:** Represents the status of barber chairs (0 for vacant, 1 for occupied).
- **barber_num_of_hc:** Tracks the number of haircuts each barber has performed.
- **lounge_chairs:** Represents the status of chairs in the primary waiting room.
- **extra_lounge_chairs:** Represents the status of chairs in an extra waiting room.
- **cash_register:** Semaphore to control access to the cash register.
- **open_barber:** Semaphore to manage access to barbers (when all barbers are busy).
- **open_lounge:** Semaphore to manage access to the waiting room (when all chairs are occupied).
- **sp:** Semaphore for controlling the 30-second timer.

## Functions

- **day:** Simulates the opening and closing of the barber shop, running from 10:00 AM to 5:00 PM.
- **spawn_customers:** Initiates the spawning of customers at random intervals.
- **start_haircut:** Simulates the process of a customer getting a haircut, including waiting for a barber and using the cash register.
- **start_cash_register:** Simulates the payment process at the cash register.
- **customer_thread:** Represents the actions of a customer, checking for available barbers or waiting rooms.
- **wait_room:** Manages the primary waiting room, including the 30-second timer.
- **extra_wait_room:** Manages the extra waiting room and transitions to the primary waiting room.
- **queue_open:** Finds the first available slot in a given queue (waiting room or barber chair).
- **timer:** Implements a timer to track the time spent in the waiting room (30 seconds).

## Main Execution

- The `main` function starts a thread (`today`) representing the duration of the barber shop's operation.
- The `spawn_customers` function is called in a loop until the `stop_spawning` flag is set to `True`.
- The main thread waits for the `today` thread to finish.

## Global State

- The global variable `stop_spawning` is used to control the spawning of new customers.

## Notes

- Threading is used to simulate concurrent activities in the barber shop, such as haircuts and waiting.
- Semaphores are employed to control access to shared resources like the cash register, barbers, and waiting rooms.
- Random intervals are used for customer arrival and haircut durations to add variability to the simulation.

## Recommendations

- Comments to explain specific sections of the code in more detail.
- Document the purpose and usage of each semaphore for clarity.
- Use more descriptive variable and function names to enhance code readability.

---

Feel free to customize this README to provide additional details or instructions for running the simulation.
