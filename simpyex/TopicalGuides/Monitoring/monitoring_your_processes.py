
# Monitoring your own processes is relatively easy, because you control the code.
# From our experience, the most common thing you might want to do is monitor
# the value of one or more state variables every time they change or at discrete intervals and store it somewhere
# (in memory, in a database, or in a file, for example).
# In the simples case, you just use a list and append the required value(s) every time they change:

# If you want to monitor multiple variables, you can append (named)tuples to your data list.

# If you want to store the data in a NumPy array or a database,
# you can often increase performance if you buffer the data in a plain Python list and only write larger chunks
# (or the complete dataset) to the database.

import simpy

data = []  # This list will hold all collected data

def test_process(env, data):
    val = 0
    for i in range(5):
        val += env.now
        data.append(val)  # Collect data
        yield env.timeout(1)

env = simpy.Environment()
p = env.process(test_process(env, data))
env.run(p)
print('Collected', data)  # Let's see what we got