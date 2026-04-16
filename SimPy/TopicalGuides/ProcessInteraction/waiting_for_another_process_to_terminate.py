
from random import seed, randint
seed(23)

import simpy

# The example above has a problem:
# it may happen that the vehicle wants to park for a shorter duration than it takes to charge the battery,
# since the minimum park time of 60 minutes is less than the maximum charge time of 90 minutes.
# To fix this problem we have to slightly change our model.
# A new bat_ctrl() will be started every time the EV starts parking.
# The EV then waits until the parking duration is over and until the charging has stopped:

#Again, nothing new (if you’ve read the Events guide) and special is happening.
# SimPy processes are events, too, so you can yield them and will thus wait for them to get triggered.
# You can also wait for two events at the same time by concatenating
# them with & (see Waiting for multiple events at once).

class EV:
    def __init__(self, env):
        self.env = env
        self.drive_proc = env.process(self.drive(env))

    def drive(self, env):
        while True:
            # Drive for 20-40 min
            yield env.timeout(randint(20, 40))

            # Park for 1–6 hours
            print('Start parking at', env.now)
            charging = env.process(self.bat_ctrl(env))
            parking = env.timeout(randint(60, 360))
            yield charging & parking
            print('Stop parking at', env.now)

    def bat_ctrl(self, env):
        print('Bat. ctrl. started at', env.now)
        # Intelligent charging behavior here …
        yield env.timeout(randint(30, 90))
        print('Bat. ctrl. done at', env.now)

env = simpy.Environment()
ev = EV(env)
env.run(until=310)