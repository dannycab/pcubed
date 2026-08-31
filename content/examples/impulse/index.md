---
title: 'Example: Calculating the change in momentum'
weight: 10
---

[In another example](/pcubed/examples/netforce/), we determined the net force acting on the fan cart in the video below.

{{< youtube MAa7sYKa5GA >}}

Now, you want to determine the change in momentum of the fan cart over a 4.2 second interval.

## Setup

You need to compute the momentum change of the fan cart using the information provided and any information that you can collect or assume.

### Facts

- The fan cart accelerates to the right.
- The fan cart experiences several forces including:
  - the force of the air on the blades (to the right)
  - the gravitational force due to the interaction with the Earth (directly downward)
  - the force applied by the track (directly upward)
  - a frictional forces and air resistance that resist the motion
- The acceleration due to gravity is 9.8 $\frac{m}{s^{2}}$ and is directed downward.
- [In another example](/pcubed/examples/netforce/), we determined the net force acting on the fan cart to be, ${\overset{\rightarrow}{F}}_{cart} = \langle 0.45,0,0\rangle N$.

### Lacking

- The mass of the fan cart is not given, but can be [found online](http://lmgtfy.com/?q=mass+of+a+pasco+fan+cart) ($m_{cart} = 0.3kg$).
- The force that the air exerts on the fan blades, which is responsible for the force to right, is unknown. This could be determined by finding the change in momentum of the fan cart over some time interval. Let's say that was done and it was found to be $F_{air} = 0.45N$.

### Approximations & Assumptions

- Over the interval that we care about it, we will assume the net force is doesn't change. That is, the cart experiences [constant force motion](/pcubed/notes/week-02-modeling-motion-net-force/constantf/).

### Representations

- The forces acting on the fan cart (the system's interactions with its surroundings) are represented in this free-body diagram.

<img src="./media/rId19.jpg" style="width:2.08333in;height:1.73958in" alt="[ALT TEXT NEEDED: figure-01.jpg -- describe this figure for screen readers]" />

- The net force acting on the fan cart is the sum of all the forces, ${\overset{\rightarrow}{F}}_{net} = \sum{\overset{\rightarrow}{F}}_{i} = \langle 0.45,0,0\rangle N$.
- The change in momentum is equal to the impulse delivered by the net force and is given by: $\Delta\overset{\rightarrow}{p} = {\overset{\rightarrow}{F}}_{net}\Delta t$.

## Solution

We simply compute the change in momentum from the net force and the time interval,

$$
\Delta\overset{\rightarrow}{p} = {\overset{\rightarrow}{F}}_{net}\Delta t = \langle 0.45,0,0\rangle N(4.2s) = 1.89Ns
$$

.
