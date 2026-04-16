#### Events can be in one of the following states.

- might happen (not triggered)
- is going to happen (triggered)
- has happened (processed)

Initially, events are not triggered and just objects in memory.

If an event gets triggered, it is scheduled at a given time and inserted into SimPy’s event queue. The property Event.triggered becomes True.

As long as the event is not processed, you can add callbacks to an event. Callbacks are callables that accept an event as parameter and are stored in the Event.callbacks list.

An event becomes processed when SimPy pops it from the event queue and calls all of its callbacks. It is now no longer possible to add callbacks. The property Event.processed becomes True.

Events also have a value. The value can be set before or when the event is triggered and can be retrieved via Event.value or, within a process, by yielding the event (value = yield event).

#### Adding callbacks to an event

The most common way to add a callback to an event is yielding it from your process function (yield event). 
This will add the process’ _resume() method as a callback. 
That’s how your process gets resumed when it yielded an event.

If an event has been processed, all of its Event.callbacks have been executed and the attribute is set to None.
This is to prevent you from adding more callbacks – these would of course never get called because the event has already happened.

You can add any callable object (function) to the list of callbacks as long as it accepts an event instance as its single parameter:

#### Triggering events

When events are triggered, they can either succeed or fail. 
For example, if an event is to be triggered at the end of a computation and everything works out fine, the event will succeed. 
If an exception occurs during that computation, the event will fail.

To trigger an event and mark it as successful, you can use Event.succeed(value=None). 
You can optionally pass a value to it (e.g., the results of a computation).

To trigger an event and mark it as failed, call Event.fail(exception) and pass an Exception instance to it (e.g., the exception you caught during your failed computation).

There is also a generic way to trigger an event: Event.trigger(event). 
This will take the value and outcome (success or failure) of the event passed to it.

Event.succeed() and Event.fail() methods return the event instance they are bound to. 
This allows you to do things like yield Event(env).succeed().

Event.trigger() returns None.