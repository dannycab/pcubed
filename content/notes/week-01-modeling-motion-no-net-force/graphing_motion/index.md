---
title: "Graphing Motion"
weight: 5
textbook_ref: "Section 1.6 and 1.7 in Matter and Interactions (4th edition)"
---

Predicting or explaining motion often requires you to use some sort of representation (or visual aid). A common (and incredibly useful) one is the graph. **In these notes, you read about graphs of motion and how to translate between different graphs.**

## Tracking the motion of objects

You want to track the motion (as a function of time) of a car that is moving at [constant velocity](/notes/week-01-modeling-motion-no-net-force/displacement_and_velocity/#what_s_so_special_about_constant_velocity_motion). For this situation, the object's motion can be predicted exactly using the position update formula:

$$
{\overset{\rightarrow}{r}}_{f} = {\overset{\rightarrow}{r}}_{i} + {\overset{\rightarrow}{v}}_{avg}\Delta t
$$

While the motion of the car, in principle, can occur 3 dimensions, it's not possible to represent all three dimensions and the time variable on a single 2-D graph. So, we have to select a component of the car's position (or velocity) to plot. In this case, let's assume the car moves to the right (i.e., in the +x direction). Perhaps, the plot of the car's position vs time looks like the plot below:

Interactive simulation: Constant velocity position vs. time — <https://msuperl.org/interactive/mechanics/CV_position_vs_time.html>

Here, you can see that the position of the car changes linearly with time, as we would predict for a car moving at constant velocity. From this graph, you can also determine the car's initial position (12 m), final position (132 m), and average velocity (12 m/s).

For this motion, [the average velocity is the same as the instantaneous velocity](/notes/week-01-modeling-motion-no-net-force/displacement_and_velocity/#what_s_so_special_about_constant_velocity_motion). Recall, the definition of the average (${\overset{\rightarrow}{v}}_{avg}$) and instantaneous velocity ($\overset{\rightarrow}{v}$) are:

$$
{\overset{\rightarrow}{v}}_{avg} = \frac{\Delta\overset{\rightarrow}{r}}{\Delta t}
$$

$$
\overset{\rightarrow}{v} = \lim_{\Delta t \rightarrow 0}\frac{\Delta\overset{\rightarrow}{r}}{\Delta t} = \frac{d\overset{\rightarrow}{r}}{dt}
$$

## The slope of a position vs time graph is the velocity

Both definitions are connected to the idea of slope. It might be easier to see this from the average velocity in one-dimension where the rise is the change in position and the run is the change in time:

$$
v_{avg,x} = slope\ of\ position\ vs\ time\ graph = \frac{rise}{run} = \frac{\Delta x}{\Delta t}
$$

For any graph, this will give the average slope between any two points. For the case above, it gives the same number for the slope between any two points and at any point. The slope at a given point is given by evaluating the derivative of the function at that point. You can think of this as taking smaller and smaller “runs”; that is, by letting $\Delta t$ go to zero. In that case, you have determined the instantaneous velocity:

$$
v_{x} = instantaneous\ slope = \frac{dx}{dt}
$$

For position versus time graphs where the position does not change linearly, you might need to determine (by taking the derivative) or approximate (by measuring very close points) the instantaneous velocity to model or explain the motion. For example in the graph below, a car moves to the right under [constant force](/notes/week-02-modeling-motion-net-force/constantf/). Here, the slope (and thus, the velocity) changes at a constant rate and the average and instantaneous velocities are not the same.

Interactive simulation: Constant force position vs. time — <https://msuperl.org/interactive/mechanics/CA_position_vs_time.html>

### The Area Under The Velocity vs Time Graph is the Displacement

Sometimes, you will want to graph the velocity of the object as a function of time. Again, you have to graph a single component at a time. So, let's go back to the example of a car moving with constant velocity. In that case, we'd expect the velocity vs time graph to be a flat, horizontal line taking on the value of the slope. In the graph below, we find that is the case.

Interactive simulation: Constant velocity, velocity vs. time — <https://msuperl.org/interactive/mechanics/CV_velocity_vs_time.html>

In addition, we can use the position update formula to show that the x-displacement ($\Delta x$) is the area under this curve:

$$
\Delta x = x_{f} - x_{i} = v_{x,avg}\Delta t
$$

This is precisely how one defines a [Riemann sum](http://en.wikipedia.org/wiki/Riemann_sum) to determine the area under a function. This area is highlighted in light blue, and is precisely equal to the difference in the initial and final position in the first graph (120 m). The car travels at 12 m/s for 10 s. Notice the displacement is positive because the area under the curve is measured from the function to y=0.

For situations where the object does no move with constant velocity, the area under the velocity vs time graph is still the displacement, it just might be slightly more complicated to calculate. For example, the graph below is the velocity vs time graph for when the car moves under a [constant force](/notes/week-02-modeling-motion-net-force/constantf/).

Interactive simulation: Constant force (velocity vs time) — <https://msuperl.org/interactive/mechanics/CA_velocity_vs_time_area_fill.html>

The triangular area (highlighted in light blue) under the curve is the displacement of the car in the x-direction. Notice it's positive because it's above the y-axis. “Area under the curve” actually refers the the area between the function and y=0. If the plot is below the y=0, then that part of the area is negative.
