#### Real-time simulations

Sometimes, you might not want to perform a simulation as fast as possible but synchronous to the wall-clock time. 
This kind of simulation is also called real-time simulation.

Real-time simulations may be necessary

- if you have hardware-in-the-loop,
- if there is human interaction with your simulation, or
- if you want to analyze the real-time behavior of an algorithm.

To convert a simulation into a real-time simulation, 
you only need to replace SimPy’s default Environment 
with a simpy.rt.RealtimeEnvironment. Apart from the initial_time argument, 
there are two additional parameters: factor and strict: 
RealtimeEnvironment(initial_time=0, factor=1.0, strict=True).

The factor defines how much real time passes with each step of simulation time. 
By default, this is one second. 
If you set factor=0.1, a unit of simulation time will only take a tenth of a second; 
if you set factor=60, it will take a minute.