# Our car process requires a reference to an Environment (env) in order to create new events.
# The car’s behavior is described in an infinite loop.
# this function is a generator.
# it will never terminate,
# it will pass the control flow back to the simulation once a yield statement is reached.
# Once the yielded event is processed (“it occurs”), the simulation will resume the function at this statement.

import simpy

def car(env):
    while True:
        print('Start parking at %d' % env.now)
        parking_duration = 5
        yield env.timeout(parking_duration)

        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)

# Now that the behavior of our car has been modeled,
# lets create an instance of it and see how it behaves:

env = simpy.Environment()
env.process(car(env))
env.run(until=15)