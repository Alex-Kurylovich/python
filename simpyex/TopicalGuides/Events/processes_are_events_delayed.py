import simpy

# When a process is created, it schedules an Initialize
# event which will start the execution of the process when triggered.
# You usually won’t have to deal with this type of event.
#
# If you don’t want a process to start immediately but after a certain delay,
# you can use simpy.util.start_delayed().
# This method returns a helper process that uses a timeout before actually starting a process.
#
# The example from above, but with a delayed start of sub():
#
# Pay attention to the additional yield needed for the helper process.

from simpy.util import start_delayed

def sub(env):
    yield env.timeout(1)
    return 23

def parent(env):
    sub_proc = yield start_delayed(env, sub(env), delay=3)
    ret = yield sub_proc
    return ret

env = simpy.Environment()
print(env.run(env.process(parent(env))))