import simpy


# The car will now drive to a battery charging station (BCS) and request one of its two charging spots.
# If both of these spots are currently in use,
# it waits until one of them becomes available again.
# It then starts charging its battery and leaves the station afterward:

def car(env, name, bcs, driving_time, charge_duration):
    # Simulate driving to the BCS
    yield env.timeout(driving_time)

    # Request one of its charging spots
    print('%s arriving at %d' % (name, env.now))
    with bcs.request() as req:
        yield req

        # Charge the battery
        print('%s starting to charge at %s' % (name, env.now))
        yield env.timeout(charge_duration)
        print('%s leaving the bcs at %s' % (name, env.now))

# The resource’s request() method generates an event that lets you wait until the resource becomes available again.
# If you are resumed, you “own” the resource until you release it.
# If you use the resource with the with statement as shown above,
# the resource is automatically being released.
# If you call request() without with, you are responsible to call release() once you are done using the resource.
# When you release a resource, the next waiting process is resumed and now “owns” one of the resource’s slots.
# The basic Resource sorts waiting processes in a FIFO (first in—first out) way.
# A resource needs a reference to an Environment and a capacity when it is created:

# We can now create the car processes and pass a reference to our resource
# as well as some additional parameters to them:

env = simpy.Environment()
bcs = simpy.Resource(env, capacity=2)

for i in range(4):
    env.process(car(env, 'Car %d' % i, bcs, i*2, 5))

env.run()