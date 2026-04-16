import time
import simpy.rt

# If the strict parameter is set to True (the default),
# the step() and run() methods will raise a RuntimeError
# if the computation within a simulation time step take more time than the real-time factor allows.
# In the following example, a process will perform a task that takes 0.02 seconds within a real-time environment
# with a time factor of 0.01 seconds:

def slow_proc(env):
    time.sleep(0.02)  # Heavy computation :-)
    yield env.timeout(1)

env = simpy.rt.RealtimeEnvironment(factor=0.01)
proc = env.process(slow_proc(env))
try:
    env.run(until=proc)
    print('Everything alright')
except RuntimeError:
    print('Simulation is too slow')