# SI_model
Simulating how infection spreads in US airport network. 

SI model
The SI model is the simplest possible model of infection. In the SI model, there are only two phases in the SI epidemic spreading process: Susceptible and Infectious. Let S be the proportion of the population that are susceptible. Let I be the proportion of the population that are infectious. At the initial time, the proportion of people who are infected is x0, the proportion of people who are susceptible is S0. β is the transmission rate, and it incorporates the encounter rate between susceptible and infectious individuals together with the probability of transmission. Consider a “closed population” with no births, deaths, or migrations, and assume the mixing is homogeneous (e.g., the susceptible individuals are uniformly spread in a geographic area, and the probability of contracting the infection is uniformly the same for all actors (T. G. Lewis, 2011)), yielding βSI as the transmission term. Thus, the equation for SI model is:

 dS/dt= -βSI
 dI/( dt)= βSI
 
 Given every individual in the system must be either susceptible or infected, I + S = 1. Thus, the equations above can be transformed to:
 
  dI/dt=βI(1-I) 
  
To solve this differential equation, we can get the cumulative growth curve as a function of time:

$$I[t]= \frac{x{0} e^{\beta t }}{1-x{0}+ x_{0} e^{\beta t }}$$

Exercise:
In the project work, your task is to implement an susceptible-infected (SI) disease spreading
model and run it against time-stamped air transport data. Especially, we will investigate how
static network properties can be used to understand disease spreading.

In our implementation of the SI-model, there is initially only one infected airport and all other
airports are susceptible. A susceptible node may become infected, when an airplane originating
from an infected node arrives to the airport. (Note that, for the airplane to carry sick passengers,
the source airport needs to be infected at the departure time of the flight.) If this condition is
met, the destination airport becomes infected with probability p ∈ [0, 1] reflecting the infectivity
of the disease. Nodes that have become infected remain infected indefinitely.

The data that are used in the project is available at the course MyCourses page in one .zip file.
The flight data that you will use to perform your simulation is located in file
events_US_air_traffic_GMT.txt, where each row contains following fields:

1st column -> Source [0-278]
2nd column -> Destination [0-278]
3rd column -> Start Time (GMT) [seconds after Unix epoch time]
4th column -> End Time (GMT)
5th column -> Duration [Same as (EndTime-StartTime)]

The aggregated weighted network aggregated_US_air_traffic_network_undir.edg is constructed
based on the event data, so that weight of each link corresponds to the number of
flights between the nodes. Additionally, you can find the information about the airports in file
US_airport_id_info.csv.

Hints:
For implementing the SI model, it is practical to keep track of the infection times of all
nodes. Initially one node is infected (with an infection time equal to the departure time
of the first flight). The infection times of the rest of the nodes can be initialized e.g. to
float(’inf’).
• When looping over time, loop over the flights in ascending order of the departure time of
the events. This way you always know, whether the current departure of the flight has
been infected or not.
• A node is infected (and can infect other nodes) only if the current simulation time (i.e.,
the departure time of the next flight) is larger than the infection time of the node.
• If a flight mediates the disease (with probability p), the infection time of the target node
becomes only updated if the new infection time is smaller than the target nodes existing
infection time.
• For reading in the csv data, there are many options, such as numpy.genfromtxt, the
read_csv function from the pandas package, or the built-in csv library in the Python
standard library.
For example, with numpy.genfromtxt use something like
event_data = np.genfromtxt(’events_US_air_traffic_GMT.txt’, names=True, dtype=int)
sorted_data = event_data.sort(order=[’StartTime’]) for loading and sorting the data.
• You may freely use any functions from networkx, matplotlib, numpy and scipy that you
find useful.

