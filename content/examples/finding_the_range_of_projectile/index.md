---
title: 'Example: Finding the range of a projectile'
weight: 26
---

In the previous example of [time of flight](/pcubed/examples/finding_the_time_of_flight_of_a_projectile/), the out of control bus is forced to jump from a location $\langle 0,40, - 5\rangle$m with an initial velocity of $\langle 80,7, - 5\rangle m/s^{- 1}$. We have now found the time of flight to be [3.65s](/pcubed/examples/finding_the_time_of_flight_of_a_projectile/) and now want to find the position of where the bus returns to the ground.

### Facts

- Starting position of the bus $\langle 0,40, - 5\rangle$
- Initial velocity of the bus $\langle 80,7, - 5\rangle$
- The acceleration due to gravity is 9.8 $\frac{m}{s^{2}}$ and is directed downward.
- The bus experiences one force - the gravitational force (directly down).
- The bus takes [3.65s](/pcubed/examples/finding_the_time_of_flight_of_a_projectile/) to reach the ground (from previous problem)

### Lacking

- The final position of the bus.

### Approximations & Assumptions

- Assume no drag effects
- Assume ground is when position of bus is 0 in the y direction

### Representations

Diagram of forces acting on bus once it leaves the road.

<img src="./media/rId13.jpg" style="width:2.3in;height:3.68in" alt="[ALT TEXT NEEDED: figure-01.jpg -- describe this figure for screen readers]" />

The general equation for calculating the final position of an object:

$$
{\overset{\rightarrow}{r}}_{f} = {\overset{\rightarrow}{r}}_{i} + {\overset{\rightarrow}{v}}_{avg}\Delta t
$$

Also know as the [position update formula](/pcubed/notes/week-01-modeling-motion-no-net-force/displacement_and_velocity/).

## Solution

From the previous problem you already know the final location of the ball in the y direction to be 0 as it has met the ground after 9.59s.

We now to find the range in the x and z directions in order to have a position vector for the final resting place of the bus.

There is no force acting in the x or z directions as the only force acting on the system is the gravitational force which acts in the y-direction.

This means that the initial velocities in both of these directions have remained unchanged.

We know the amount of time the bus has been traveling in the x-direction at its initial velocity and its initial position so we can compute the distance travelled in this direction using the position update formula for x-components.

$$
x_{f} = x_{i} + V_{avg,x}\Delta t
$$

Plug in respective values for variables.

$$
= 0 + 80m/s(3.65s)
$$

Compute range in x-direction.

$$
= 292m
$$

Repeat same process for the z-components:

$$
z_{f} = z_{i} + V_{avg,z}\Delta t
$$

Plug in respective values for variables.

$$
= - 5 + - 5m/s(3.65s)
$$

Compute range in z-direction.

$$
= - 23.25m
$$

Write range(final position vector) using all components:

Final position =

$$
\langle 292,0, - 23.255\rangle m
$$
