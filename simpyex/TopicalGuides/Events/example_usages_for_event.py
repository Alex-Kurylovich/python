import simpy

# One example for this is that events can be shared.
# They can be created by a process or outside of the context of a process.
# They can be passed to other processes and chained:

class School:
    def __init__(self, env):
        self.env = env
        self.class_ends = env.event()
        self.pupil_procs = [env.process(self.pupil()) for i in range(3)]
        self.bell_proc = env.process(self.bell())

    def bell(self):
        for i in range(2):
            yield self.env.timeout(45)
            self.class_ends.succeed()
            self.class_ends = self.env.event()
            print()

    def pupil(self):
        for i in range(2):
            print(r' \o/', end='')
            yield self.class_ends

env = simpy.Environment()
school = School(env)
print(env.run())