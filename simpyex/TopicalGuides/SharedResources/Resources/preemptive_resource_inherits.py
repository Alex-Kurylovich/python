import simpy

# PreemptiveResource inherits from PriorityResource and adds a preempt flag (that defaults to True) to request().
# By setting this to False (resource.request(priority=x, preempt=False)),
# a process can decide to not preempt another resource user.
# It will still be put in the queue according to its priority, though.
#
# The implementation of PreemptiveResource values priorities higher than preemption.
# That means preempt requests are not allowed to cheat and jump over a higher prioritized request.
# The following example shows that preemptive low priority requests cannot queue-jump over high priority requests:

# Process A requests the resource with priority 0. It immediately becomes a user.
# Process B requests the resource with priority -2 but sets preempt to False. It will queue up and wait.
# Process C requests the resource with priority -1 but leaves preempt True. Normally,
# it would preempt A but in this case, B is queued up before C and prevents C from preempting A.
# C can also not preempt B since its priority is not high enough.

# Thus, the behavior in the example is the same as if no preemption was used at all. Be careful when using mixed preemption!
#
# Due to the higher priority of process B, no preemption occurs in this example. Note that an additional request with a priority of -3 would be able to preempt A.
#
# If your use-case requires a different behaviour,
# for example queue-jumping or valuing preemption over priorities,
# you can subclass PreemptiveResource and override the default behaviour.


def user(name, env, res, prio, preempt):
    with res.request(priority=prio, preempt=preempt) as req:
        try:
            print(f'{name} requesting at {env.now}')
            assert isinstance(env.now, int), type(env.now)
            yield req
            assert isinstance(env.now, int), type(env.now)
            print(f'{name} got resource at {env.now}')
            yield env.timeout(3)
        except simpy.Interrupt:
            print(f'{name} got preempted at {env.now}')

env = simpy.Environment()
res = simpy.PreemptiveResource(env, capacity=1)
A = env.process(user('A', env, res, prio=0, preempt=True))
env.run(until=1)  # Give A a head start

B = env.process(user('B', env, res, prio=-2, preempt=False))
C = env.process(user('C', env, res, prio=-1, preempt=True))
env.run()