from functools import partial, wraps
import simpy

def trace(env, callback):
    """
    Replace the ``step()`` method of *env* with a tracing function
    that calls *callbacks* with an events time, priority, ID and its
    instance just before it is processed.
    In order to debug or visualize a simulation, you might want to trace when events are created,
    triggered and processed. Maybe you also want to trace which process created an event and
    which processes waited for an event.
    The two most interesting functions for these use-cases are Environment.step(),
    where all events get processed, and Environment.schedule(),
    where all events get scheduled and inserted into SimPy’s event queue.
    Here is an example that shows how Environment.step() can be patched in order to trace all processed events:

    Using the same concepts, you can also patch Environment.schedule().
    This would give you central access to the information when which event is scheduled for what time.

    In addition to that, you could also patch some or all of SimPy’s event classes,
    e.g., their __init__() method in order to trace when and how an event is initially being created.
    """
    def get_wrapper(env_step, callback):
        """Generate the wrapper for env.step()."""
        @wraps(env_step)
        def tracing_step():
            """Call *callback* for the next event if one exist before
            calling ``env.step()``."""
            if len(env._queue):
                t, prio, eid, event = env._queue[0]
                callback(t, prio, eid, event)
            return env_step()
        return tracing_step

    env.step = get_wrapper(env.step, callback)

def monitor(data, t, prio, eid, event):
    data.append((t, eid, type(event)))

def test_process(env):
    yield env.timeout(1)

data = []
# Bind *data* as first argument to monitor()
# see https://docs.python.org/3/library/functools.html#functools.partial
monitor = partial(monitor, data)

env = simpy.Environment()
trace(env, monitor)

p = env.process(test_process(env))
env.run(until=p)

for d in data:
    print(d)