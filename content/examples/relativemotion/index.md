---
title: 'Example: Calculating the velocity of a plane using relative measurements'
weight: 16
---

A Boeing 747 leaves the Detroit airport intending to head due west. The plane is experiencing a strong crosswind that is blowing toward the south, which has a wind speed of 10.0 m/s. Determine the speed of plane relative to the ground and the direction its compass should read if the pilot intends to fly due west at top speed.

## Setup

You need to determine the speed and direction of the plane using information given and any information that you can collect or assume.

### Facts

- The pilot intends to fly due west.
- The plane experiences a crosswind with a speed of $|v_{a/g}| = 10.0\frac{m}{s}$, which is directed due south.

### Lacking

- The top speed of a Boeing 747 is unknown, but can be [found online](http://lmgtfy.com/?q=top+speed+of+747) (920 $\frac{km}{h}$ or $v_{p/a} = 255\frac{m}{s}$).

### Approximations & Assumptions

- The windspeed is measured relative to the ground.
- The plane's airspeed is measured relative to the air.
- At top speed, the plane is flying level with ground.
- The plane has a constant velocity over the interval you care about it.

### Representations

- The velocities of the plane relative to the air, the air relative to the ground, and the plane relative to the ground are represented in the following diagram.
- The relative velocity equation for three objects is: ${\overset{\rightarrow}{v}}_{A/C} = {\overset{\rightarrow}{v}}_{A/B} + {\overset{\rightarrow}{v}}_{B/C}$ where ${\overset{\rightarrow}{v}}_{A/C}$ is the velocity of object A with respect to object C, etc.

## Solution

The problem can be described vectorially using the relative velocity equation:

$$
{\overset{\rightarrow}{v}}_{p/g} = {\overset{\rightarrow}{v}}_{p/a} + {\overset{\rightarrow}{v}}_{a/g}
$$

The pilot requires that the velocity of the plane with respect to the ground be directed due west. If you measure positive $\theta$ counterclockwise with respect to the east, the plane's velocity relative to the ground should only have a negative $x$-component. So the equation above becomes (in 2D),

$$
\langle - |v_{p/g}|,0\rangle = |v_{p/a}|{\widehat{v}}_{p/a} + \langle 0, - |v_{a/g}|\rangle
$$

We can break this vector equation into two scalar equations:

$$
- |v_{p/g}| = |v_{p/a}|v_{p/a,x}
$$

$$
0 = |v_{p/a}|v_{p/a,y} - |v_{a/g}|
$$

where $v_{p/a,x}$ and $v_{p/a,y}$ are the components of the unit vector in the direction of the velocity of the plane with respect to the air. Thus, they satisfy this equation.

$$
v_{p/a,x}^{2} + v_{p/a,y}^{2} = 1
$$

You can rewrite the above equation by using what the unit vector components are equal to (in the previous two equations),

$$
\left( - \frac{|v_{p/g}|}{|v_{p/a}|} \right)^{2} + \left( \frac{|v_{a/g}|}{|v_{p/a}|} \right)^{2} = 1
$$

$$
{|v_{p/g}|}^{2} + {|v_{a/g}|}^{2} = {|v_{p/a}|}^{2}
$$

So, the speed that the plane has with respect to the ground is slower than its air speed, which agrees with the representation above.

$$
|v_{p/g}| = \sqrt{(}{|v_{p/a}|}^{2} - {|v_{a/g}|}^{2}) = \sqrt{(255\frac{m}{s})^{2} - (10\frac{m}{s})^{2}} = 225\frac{m}{s}
$$

The angle the compass should read can be determined from the above representation. The tangent of the angle (as measured from the negative $x$-axis is given by,

$$
\tan\theta = \frac{|v_{a/g}|}{|v_{p/g}|}
$$

Hence,

$$
\theta = \tan^{- 1}\left( \frac{|v_{a/g}|}{|v_{p/g}|} \right) = \tan^{- 1}\left( \frac{10\frac{m}{s}}{225\frac{m}{s}} \right) = {2.5}^{\circ}
$$

which is 2.5$^{\circ}$ north of west or 177.5$^{\circ}$ from east measured counterclockwise.
