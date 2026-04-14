The use-cases for resource monitoring are numerous, 
for example you might want to monitor:

- Utilization of a resource over time and on average, that is,
  - the number of processes that are using the resource at a time
  - the level of a container
  - the amount of items in a store

This can be monitored either in discrete time steps or every time there is a change.
- Number of processes in the (put|get)queue over time (and the average). Again, this could be monitored at discrete time steps or every time there is a change.
- For PreemptiveResource, you may want to measure how often preemption occurs over time.

In contrast to your processes, 
you don’t have direct access to the code of the built-in resource classes. 
But this doesn’t prevent you from monitoring them.