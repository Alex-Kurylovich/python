
Shared resources are another way to model Process Interaction. 
They form a congestion point where processes queue up in order to use them.

SimPy defines three categories of resources:

- Resources – Resources that can be used by a limited number of processes at a time (e.g., a gas station with a limited number of fuel pumps).
- Containers – Resources that model the production and consumption of a homogeneous, undifferentiated bulk. It may either be continuous (like water) or discrete (like apples).
- Stores – Resources that allow the production and consumption of Python objects.

#### The basic concept of resources

All resources share the same basic concept: The resource itself is some kind of a container with a, usually limited, 
capacity. Processes can either try to put something into the resource or try to get something out. 
If the resource is full or empty, they have to queue up and wait.

How every resource looks:
BaseResource(capacity):
   put_queue
   get_queue
   put(): event
   get(): event

Every resource has a maximum capacity and two queues: one for processes that want to put something into it 
and one for processes that want to get something out. 
The put() and get() methods both return an event that is triggered when the corresponding action was successful.

#### Resources and interrupts

While a process is waiting for a put or get event to succeed, it may be interrupted by another process. 
After catching the interrupt, the process has two possibilities:

1. It may continue to wait for the request (by yielding the event again)
2. It may stop waiting for the request. In this case, it has to call the event’s cancel() method

The resource system is modular and extensible. 
Resources can, for example, use specialized queues and event types. 
This allows them to use sorted queues, to add priorities to events, or to offer preemption.