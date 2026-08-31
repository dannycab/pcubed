---
title: "Constant Force Motion"
weight: 5
textbook_ref: "Section 2.5 in Matter and Interactions (4th edition)"
---

You read previously how to (separately) [predict the final momentum](/notes/week-02-modeling-motion-net-force/motionpredict/) and [final location](/notes/week-01-modeling-motion-no-net-force/displacement_and_velocity/) of a system. In these notes, you will read how to put those two ideas together for a system where the net force is a constant [vector](/notes/week-01-modeling-motion-no-net-force/scalars_and_vectors/) (unchanging magnitude and direction) to be able to predict the motion of such a system.

### Lecture Video

{{< youtube FK5vyrOamhk >}}

### A Constant Net Force

*A system that experiences a constant [net force](/notes/week-02-modeling-motion-net-force/momentum_principle/) may be subject to one or more individual forces.* What matters is that the sum of all the forces acting on the object result in a net force that has a constant magnitude and direction. A system which experiences such a force only changes its momentum in the direction of that net force.

Depending on how you select your coordinate system, it might mean that more than one component of the momentum vector changes. Often, it is convenient to select a coordinate system where the net force is aligned with a coordinate direction, then only one momentum vector component changes in time.

{{< youtube 1RP2oSBAQJI >}}

# Predicting the Motion

Consider a fan cart that is released on a low-friction track. Here's a video of the situation.

{{< youtube MAa7sYKa5GA >}}

Notice that the fan cart's position changes more rapidly near the end of the video. The fan cart experiences (to a good approximation) a constant net force. The sum of all the forces acting on the fan cart give (roughly) a net force of constant magnitude and direction. Furthermore, the motion is constrained to a single dimension (namely, the horizontal direction).

With this setup, you can predict the position of the fan cart given only information about its initial position, velocity (or momentum), and the net force acting on it.

## Deriving the Equation for Constant Force Motion in 1D

If you choose the horizontal direction to be the x-direction, we have the following equations to describe the motion.

$$
p_{fx} = p_{ix} + F_{net,x}\Delta t
$$

$$
x_{f} = x_{i} + v_{avg,x}\Delta t
$$

For this system, the momentum and, thus, the velocity change linearly in time. So the [arithmetic average velocity and average velocity are equivalent](/notes/week-01-modeling-motion-no-net-force/displacement_and_velocity/#speed_and_velocity). Hence, we can determine the final location of the system exactly.[<sup>1)</sup>](/notes/week-02-modeling-motion-net-force/constantf/#fn__1)

Starting with the [Update Form of the Momentum Principle](/notes/week-02-modeling-motion-net-force/motionpredict/), you determine the velocity of the object after a time $\Delta t$,

$$
p_{fx} = p_{ix} + F_{net,x}\Delta t
$$

$$
mv_{fx} = mv_{ix} + F_{net,x}\Delta t
$$

$$
v_{fx} = v_{ix} + \frac{F_{net,x}}{m}\Delta t
$$

From this equation, you can determine the arithmetic average velocity, which in this case is equal to the average velocity.

$$
v_{avg,x} = \frac{v_{ix} + v_{fx}}{2} = \frac{v_{ix} + v_{ix} + \frac{F_{net,x}}{m}\Delta t}{2} = \frac{2v_{ix}}{2} + \frac{\frac{F_{net,x}}{m}\Delta t}{2} = v_{ix} + \frac{1}{2}\frac{F_{net,x}}{m}\Delta t
$$

By using this average velocity in the [position update formula](/notes/week-01-modeling-motion-no-net-force/displacement_and_velocity/), you obtain the final expression that predicts the location of the system given only information about its *initial position, velocity, and the force acting on it.*

$$
x_{f} = x_{i} + v_{avg,x}\Delta t = x_{i} + v_{ix}\Delta t + \frac{1}{2}\frac{F_{net,x}}{m}\Delta t^{2}
$$

In physics, the information about the system prior to predicting its motion is called the “initial state” of the system. The starting values of these properties (position, velocity, net force) are called the “initial conditions” of the system.

### Connection to Energy

As you will read, the motion of systems can also be predicted or explained by using the [energy principle](/notes/week-07-energy-transfer/define_energy/) in addition to or, as an alternative, to using the [momentum principle](/notes/week-02-modeling-motion-net-force/momentum_principle/). You will find that using energy, you can often think about [the initial and final states of the system's motion](/notes/week-07-energy-transfer/grav_and_spring_pe/) and not how that motion evolves (e.g., over what time the motion occurs).

For constant force motion in one dimension (e.g., x-direction), you could solve the two motion prediction equations above (i.e., combining them into a single equation that removes the time variable). The resulting equation predicts the final speed of a system given its initial speed, the net force acting on the system, and the displacement of the system,

$$
v_{xf}^{2} = v_{xi}^{2} + 2\frac{F_{net,x}}{m}\Delta x
$$

Again, as you will read, this equation can also be derived from [the relationship between kinetic energy and work](/notes/week-07-energy-transfer/work/).

### Summary of Constant Force

The relationship between force and acceleration (even for a variable net force): ${\overset{\rightarrow}{F}}_{net} = m\overset{\rightarrow}{a}$ OR $\overset{\rightarrow}{a} = \frac{{\overset{\rightarrow}{F}}_{net}}{m}$.

The following 1D equations are valid ONLY if the net force (and therefore, the acceleration) is constant. These equations are commonly known as kinematic equations:

$$
x_{f} = x_{i} + v_{avg,x}\Delta t
$$

$$
v_{fx} = v_{ix} + \frac{F_{net,x}}{m}\Delta t
$$

$$
v_{avg,x} = \frac{v_{ix} + v_{fx}}{2} = v_{ix} + \frac{1}{2}\frac{F_{net,x}}{m}\Delta t
$$

$$
x_{f} = x_{i} + v_{ix}\Delta t + \frac{1}{2}\frac{F_{net,x}}{m}\Delta t^{2}
$$

$$
v_{xf}^{2} = v_{xi}^{2} + 2\frac{F_{net,x}}{m}\Delta x
$$

### Constant Force in 3D

The derivation for each dimension is similar (so long as the force is constant in each direction). The result is the following general equation,

$$
{\overset{\rightarrow}{r}}_{f} = {\overset{\rightarrow}{r}}_{i} + {\overset{\rightarrow}{v}}_{i}\Delta t + \frac{1}{2}\frac{{\overset{\rightarrow}{F}}_{net}}{m}\Delta t^{2}
$$

## Examples

[Predicting the location of an object undergoing constant force motion](/pcubed/examples/finalloccf/)

[Video Example: Box on a Ramp](https://www.msuperl.org/wikis/pcubed/doku.php?id=183_notes:example:videotutorial1)

------------------------------------------------------------------------

[<sup>1)</sup>](/notes/week-02-modeling-motion-net-force/constantf/#fnt__1)

This is why so many physics courses spend so much time working with constant force motion. You can predict precisely where the system will be at any time.
