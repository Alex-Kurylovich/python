from collections import namedtuple

import simpy

# As with the other resource types, you can get a store’s capacity via the capacity attribute.
# The attribute items points to the list of items currently available in the store.
# The put and get queues can be accessed via the put_queue and get_queue attributes.
# FilterStore can, for example, be used to model machine shops where machines have varying attributes.

Machine = namedtuple('Machine', 'size, duration')
m1 = Machine(1, 2)  # Small and slow
m2 = Machine(2, 1)  # Big and fast

env = simpy.Environment()
machine_shop = simpy.FilterStore(env, capacity=2)
machine_shop.items = [m1, m2]  # Pre-populate the machine shop

def user(name, env, ms, size):
    machine = yield ms.get(lambda machine: machine.size == size)
    print(name, 'got', machine, 'at', env.now)
    yield env.timeout(machine.duration)
    yield ms.put(machine)
    print(name, 'released', machine, 'at', env.now)


users = [env.process(user(i, env, machine_shop, (i % 2) + 1))
         for i in range(3)]
env.run()