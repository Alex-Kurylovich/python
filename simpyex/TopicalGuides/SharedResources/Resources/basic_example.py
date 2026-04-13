import simpy

def resource_user(env, resource):
    request = resource.request()  # Generate a request event
    yield request                 # Wait for access
    yield env.timeout(1)          # Do something
    resource.release(request)     # Release the resource

env = simpy.Environment()
res = simpy.Resource(env, capacity=1)
user = env.process(resource_user(env, res))
print(env.run())

# Note, that you have to release the resource under all conditions; for example,
# if you got interrupted while waiting for or using the resource.
# In order to help you with that and to avoid too many try: ... finally: ... constructs,
# request events can be used as context manager:

def resource_user_release(env, resource):
    with resource.request() as req:  # Generate a request event
        yield req                    # Wait for access
        yield env.timeout(1)         # Do something
                                     # Resource released automatically

env = simpy.Environment()
user = env.process(resource_user_release(env, res))
print(env.run())

# retrieve lists of the current users or queued users,
# p3 requested the resource later than p2, it could use it earlier because its priority was higher.

res = simpy.Resource(env, capacity=1)

def print_stats(res):
    print(f'{res.count} of {res.capacity} slots are allocated.')
    print(f'  Users: {res.users}')
    print(f'  Queued events: {res.queue}')


def user(res):
    print_stats(res)
    with res.request() as req:
        yield req
        print_stats(res)
    print_stats(res)

procs = [env.process(user(res)), env.process(user(res))]
env.run()