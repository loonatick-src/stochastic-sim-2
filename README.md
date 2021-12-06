# Stochastic Simulation
## Assignment 2 - Discrete Event Simulation and Queueing Theory


### Authors
Universiteit van Amsterdam
+ Valentina Bazyleva (13583611)
+ Chaitanya Kumar (13821369) 

### Requirements
Tested with the following, will most likely work well with other versions.
+ numpy 1.19.4
+ scipy 1.7.2
+ matplotlib 3.5.0
+ seaborn 0.11.2
+ pandas 1.2.3
+ simpy 4.0.1

### Files
#### Python Scripts
Not meant to be executed as main - imported in the notebooks.
+ `assignment_analytical.py`: functions for analytical values of performance measures; used for visualization
of theoretical results and verification of discrete event simulations.
+ `assignment_util.py`: utility functions, PRNG functions etc
+ `assignment_queue.py`: discrete event simulation objects; this is where all the simpy code is

####Notebooks
+ `analytical.ipynb`: plots of theoretical waiting times
+ `statistical.ipynb`: discrete event simulations, statistical tests, and plots
