import simpy

def my_proc(env):
    yield env.timeout(1)
    return 42

env = simpy.Environment()
print(env.process(my_proc(env)))
print(env.step())