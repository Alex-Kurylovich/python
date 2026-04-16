# SimPy is a process-based discrete-event simulation
# Simulations can be performed “as fast as possible”,
# in real time (wall clock time) or by manually stepping through the events.

import simpy

def clock(env, name, tick):
    while True:
        print(name, env.now)
        yield env.timeout(tick)

env = simpy.Environment()
env.process(clock(env, 'fast', 0.5))
env.process(clock(env, 'slow', 1))
env.run(until=2)