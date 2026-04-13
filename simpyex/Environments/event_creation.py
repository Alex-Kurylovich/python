import simpy

env = simpy.Environment()
print(simpy.events.Event(env))