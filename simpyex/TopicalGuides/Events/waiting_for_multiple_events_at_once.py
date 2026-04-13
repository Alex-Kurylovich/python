import simpy

from simpy.events import AnyOf, AllOf, Event

def any_all(env):
    events = [Event(env) for i in range(3)]
    a = AnyOf(env, events)  # Triggers if at least one of "events" is triggered.
    print(a)
    b = AllOf(env, events)  # Triggers if all each of "events" is triggered.
    print(b)

def test_condition(env):
    t1, t2 = env.timeout(1, value='spam'), env.timeout(2, value='eggs')
    ret = yield t1 | t2
    assert ret == {t1: 'spam'}

    t1, t2 = env.timeout(1, value='spam'), env.timeout(2, value='eggs')
    ret = yield t1 & t2
    assert ret == {t1: 'spam', t2: 'eggs'}

    # You can also concatenate & and |
    e1, e2, e3 = [env.timeout(i) for i in range(3)]
    yield (e1 | e2) & e3
    assert all(e.processed for e in [e1, e2, e3])

def fetch_values_of_multiple_events(env):
    t1, t2 = env.timeout(1, value='spam'), env.timeout(2, value='eggs')
    r1, r2 = (yield t1 & t2).values()
    assert r1 == 'spam' and r2 == 'eggs'

env = simpy.Environment()
any_all(env)

env = simpy.Environment()
env.process(test_condition(env))
print(env.run())

env = simpy.Environment()
env.process(fetch_values_of_multiple_events(env))
print(env.run())
