import simpy

# Process can yield another process.
# It will then be resumed when the other process ends.
# The event’s value will be the return value of that process

def sub(env):
    yield env.timeout(1)
    return 23

def parent(env):
    ret = yield env.process(sub(env))
    return ret

env = simpy.Environment()
print(env.run(env.process(parent(env))))