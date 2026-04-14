import simpy

# now haven’t patched a single resource instance but the whole class.
# It also removed all of the first example’s flexibility:
# We only monitor Resource typed resources,
# we only collect data before the actual requests are made, and we only collect the time and queue length.
# At the same time, you need less than half of the code.

class MonitoredResource(simpy.Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []

    def request(self, *args, **kwargs):
        self.data.append((self._env.now, len(self.queue)))
        return super().request(*args, **kwargs)

    def release(self, *args, **kwargs):
        self.data.append((self._env.now, len(self.queue)))
        return super().release(*args, **kwargs)

def test_process(env, res):
    with res.request() as req:
        yield req
        yield env.timeout(1)

env = simpy.Environment()

res = MonitoredResource(env, capacity=1)
p1 = env.process(test_process(env, res))
p2 = env.process(test_process(env, res))
env.run()

print(res.data)