import simpy

# To actually let time pass in a simulation, there is the timeout event.
# A timeout has two parameters: a delay and an optional value: Timeout(delay, value=None).
# It triggers itself during its creation and schedules itself at now + delay.
# Thus, the succeed() and fail() methods cannot be called again and you have to pass the event value to it when you create the timeout.
# The delay can be any kind of number, usually an int or float as long as it supports comparison and addition.
# Code should be provided

env = simpy.Environment()
print(env)