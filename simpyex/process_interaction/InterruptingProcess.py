import simpy

# you don’t want to wait until your electric vehicle is fully charged
# but want to interrupt the charging process and just start driving instead.
# the driver process has a reference to the car’s action process. After waiting for 3 time steps, it interrupts that process.
#
# Interrupts are thrown into process functions as Interrupt exceptions
# that can (should) be handled by the interrupted process.
# The process can then decide what to do next
# (e.g., continuing to wait for the original event or yielding a new event):

def driver(env, car):
    yield env.timeout(3)
    car.action.interrupt()

class Car(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        while True:
            print('Start parking and charging at %d' % self.env.now)
            charge_duration = 5
            # We may get interrupted while charging the battery
            try:
                yield self.env.process(self.charge(charge_duration))
            except simpy.Interrupt:
                # When we received an interrupt, we stop charging and
                # switch to the "driving" state
                print('Was interrupted. Hope, the battery is full enough ...')

            print('Start driving at %d' % self.env.now)
            trip_duration = 2
            yield self.env.timeout(trip_duration)

    def charge(self, duration):
        yield self.env.timeout(duration)

env = simpy.Environment()
car = Car(env)
env.process(driver(env, car))
env.run(until=15)