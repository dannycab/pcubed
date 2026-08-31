---
title: 'Example: Calculating a unit vector'
weight: 9
---

You will find it useful to be able to calculate the unit vector of a given vector. For example, the [force due to air resistance](http://en.wikipedia.org/wiki/Drag_(physics)#Types_of_drag) is defined in terms of the velocity unit vector.

Determine the unit vector for the velocity vector, $\overset{\rightarrow}{v} = \langle 2, - 1,3\rangle\frac{m}{s}$.

## Solution

The unit vector is defined as the ratio of the vector itself to its magnitude. So, we can compute,

$$
\widehat{v} = \frac{\overset{\rightarrow}{v}}{|\overset{\rightarrow}{v}|} = \frac{\langle 2, - 1,3\rangle\frac{m}{s}}{\sqrt{2^{2} + ( - 1)^{2} + 3^{2}}\frac{m}{s}} = \frac{\langle 2, - 1,3\rangle\frac{m}{s}}{\sqrt{14}\frac{m}{s}} = \langle 0.53, - .27,.80\rangle
$$

Notice that the unit vector has no units of its own. It simply represents the direction of this velocity vector. We can further check that it is indeed a unit vector by taking it's magnitude, which should be 1.

$$
|\widehat{v}| = \sqrt{{0.53}^{+}( - .27)^{2} + {.80}^{2}} = 1
$$
