"""
A 2D implementation of a robot in python that picks up and moves dots, 
displays battery level, and returns to a charging station when it gets too low.

Basically I want to simulate a robot cleaning up a room. The dots will populate 
randomly on a two dimensional grid. The robot will start at a charging station. 
It will move to the closest dot, pick it up, and navigate to a "trash can" were 
it will remove the dot. The robot will not move through the space of a dot unless 
it is picking it up. The robots battery will weardown continuously and be displayed 
to the screen. If the robots battery dies, the simulation will end. If the robots 
battery drops to 25%, it will begin making its way back to the charging station, 
dropping its dot if it is carrying one.

I want to practice FSM controll and simulations. Once I have a working program in 
Python, I will create a seperate project in UNITY.
"""

