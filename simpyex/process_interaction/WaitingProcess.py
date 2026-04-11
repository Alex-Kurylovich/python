
# As it happens, a SimPy Process can be used like an event (technically, a process actually is an event).
# If you yield it, you are resumed once the process has finished.
# Imagine a car-wash simulation where cars enter the car-wash and wait for the washing process to finish.
# Or an airport simulation where passengers have to wait until a security check finishes.
#
# Let's assume that the car from our last example magically became an electric vehicle.
# Electric vehicles usually take a lot of time charging their batteries after a trip.
# They have to wait until their battery is charged before they can start driving again.
#
# We can model this with an additional charge() process for our car.
# Therefore, we refactor our car to be a class with two process methods:
# run() (which is the original car() process function) and charge().
#
# The run process is automatically started when Car is instantiated.
# A new charge process is started every time the vehicle starts parking.
# By yielding the Process instance that Environment.process() returns,
# the run process starts waiting for it to finish:

class Car(object):
    def __init__(self, env):
        self.env = env
        # Start the run process everytime an instance is created.
        self.action = env.process(self.run())

    def run(self):
        while True:
            print('Start parking and charging at %d' % self.env.now)
            charge_duration = 5
            # We yield the process that process() returns
            # to wait for it to finish
            yield self.env.process(self.charge(charge_duration))

            # The charge process has finished and
            # we can start driving again.
            print('Start driving at %d' % self.env.now)
            trip_duration = 2
            yield self.env.timeout(trip_duration)

    def charge(self, duration):
        yield self.env.timeout(duration)

import simpy
env = simpy.Environment()
car = Car(env)
env.run(until=15)