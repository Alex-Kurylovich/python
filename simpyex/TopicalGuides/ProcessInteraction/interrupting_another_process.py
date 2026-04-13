

from random import seed, randint
seed(23)

import simpy

# trip is very urgent, but with the current implementation,
# we always need to wait until the battery is fully charged.

# You can call interrupt() on a Process.
# This will throw an Interrupt exception into that process, resuming it immediately

# What process.interrupt() actually does is scheduling an Interruption event for immediate execution.
# If this event is executed it will remove the victim process’ _resume() method
# from the callbacks of the event that it is currently waiting for (see target).
# Following that it will throw the Interrupt exception into the process.
#
# Since we don’t do anything special to the original target event of the process,
# the interrupted process can yield the same event again after catching the Interrupt –
# Imagine someone waiting for a shop to open.
# The person may get interrupted by a phone call.
# After finishing the call, he or she checks if the shop already opened and either enters or continues to wait.

class EV:
    def __init__(self, env):
        self.env = env
        self.drive_proc = env.process(self.drive(env))

    def drive(self, env):
        while True:
            # Drive for 20-40 min
            yield env.timeout(randint(20, 40))

            # Park for 1 hour
            print('Start parking at', env.now)
            charging = env.process(self.bat_ctrl(env))
            parking = env.timeout(60)
            yield charging | parking
            if not charging.triggered:
                # Interrupt charging if not already done.
                charging.interrupt('Need to go!')
            print('Stop parking at', env.now)

    def bat_ctrl(self, env):
        print('Bat. ctrl. started at', env.now)
        try:
            yield env.timeout(randint(60, 90))
            print('Bat. ctrl. done at', env.now)
        except simpy.Interrupt as i:
            # Onoes! Got interrupted before the charging was done.
            print('Bat. ctrl. interrupted at', env.now, 'msg:',
                  i.cause)

env = simpy.Environment()
ev = EV(env)
env.run(until=100)