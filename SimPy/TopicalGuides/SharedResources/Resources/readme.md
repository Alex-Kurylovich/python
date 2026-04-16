
Resources can be used by a limited number of processes at a time 
(e.g., a gas station with a limited number of fuel pumps). 
Processes request these resources to become a user (or to “own” them) and 
have to release them once they are done
(e.g., vehicles arrive at the gas station, use a fuel-pump, 
if one is available, and leave when they are done).

Requesting a resource is modeled as “putting a process’ token into the resource” and 
releasing a resource correspondingly as “getting a process’ token out of the resource”. 
Thus, calling request()/release() is equivalent to calling put()/get(). 
Releasing a resource will always succeed immediately.

Three resource types:

1. Resource
2. PriorityResource, where queueing processes are sorted by priority
3. PreemptiveResource, where processes additionally may preempt other processes with a lower priority

The Resource is conceptually a semaphore. 
Its only parameter – apart from the obligatory reference to an Environment – is its capacity. 
It must be a positive number and defaults to 1: Resource(env, capacity=1).
It stores the request event as an “access token” for each user