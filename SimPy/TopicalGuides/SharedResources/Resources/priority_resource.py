import simpy

# This subclass of Resource lets requesting processes provide a priority for each request.
# More important requests will gain access to the resource earlier than less important ones.
# Priority is expressed by integer numbers; smaller numbers mean a higher priority.
# p3 requested the resource later than p2, it could use it earlier because its priority was higher.

def resource_user(name, env, resource, wait, prio):
    yield env.timeout(wait)
    with resource.request(priority=prio) as req:
        print(f'{name} requesting at {env.now} with priority={prio}')
        yield req
        print(f'{name} got resource at {env.now}')
        yield env.timeout(3)

env = simpy.Environment()
res = simpy.PriorityResource(env, capacity=1)
p1 = env.process(resource_user(1, env, res, wait=0, prio=0))
p2 = env.process(resource_user(2, env, res, wait=1, prio=0))
p3 = env.process(resource_user(3, env, res, wait=2, prio=-1))
env.run()