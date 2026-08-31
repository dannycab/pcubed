---
title: 'Example: MIT Water Balloon Fight'
weight: 32
---

During the spring semester at MIT, residents of the parallel buildings of the East Campus Dorms battle one another with large sling-shots made from surgical hose mounted to window frames. Water balloons (with a mass of about 0.5kg) are placed in a pouch attached to the hose, which is then stretched nearly the width of the room (about 3.5 meters). If the hose obeys Hooke's Law, with a spring constant of 100N/m, how fast is the balloon traveling when it leaves the dorm room window?

## Facts

Mass of water balloons = 0.5kg

Hose stretched = 3.5m

Spring Constant = 100N/m

Initial State: Hose stretched 3.5m; no velocity

Final State: Hose relaxed; non zero v.

## Lacking

Velocity of balloon leaving window.

## Approximations & Assumptions

No energy is lost to other forms in the system.

## Representations

$$
\Delta K = W
$$

$$
K_{E} = \frac{1}{2}mv^{2}
$$

$$
F = - kx
$$

$$
W_{F} = \sum_{i}^{}{\overset{\rightarrow}{F}}_{i} \cdot \Delta{\overset{\rightarrow}{r}}_{i} = \int_{i}^{f}\overset{\rightarrow}{F}d\overset{\rightarrow}{r}
$$

$$
W = \frac{1}{2}mv_{f}^{2} - \frac{1}{2}mv_{i}^{2}
$$

System: Water balloon (model as a point particle)

Surroundings: Surgical hose slingshot

## Solution

The first step to solving this problem is to define your system and surroundings which we have previously defined in our representations as system being the water balloon and the surroundings being the surgical hose slingshot.

We are going to apply the work-kinetic energy theorem to the problem.

According to this theorem the change in energy of the system is equal to the work done on the system.

$$
\Delta K_{balloon} = W_{hose}
$$

Kinetic final - kinetic initial is equal to the work of the hose.

$$
K_{balloon,f} - K_{balloon,i} = W_{hose}
$$

Sub in

$$
\frac{1}{2}mv^{2}
$$

for kinetic energy.

$$
\frac{1}{2}mv_{f}^{2} - \frac{1}{2}mv_{i}^{2} = W
$$

Initial kinetic energy of the balloon is zero. Therefore final energy of the balloon is equal to the work by the hose.

$$
\frac{1}{2}mv_{i}^{2}(0,v_{i} = 0)
$$

Rearrange to solve for $v_{f}^{2}$

$$
\frac{1}{2}mv_{f}^{2} = W \rightarrow v_{f}^{2} = \frac{2W}{m}
$$

If we can calculate the work done by the hose, we can find $v_{f}$

$$
v_{f} = \sqrt{\frac{2W}{m}}
$$

However the force of the hose is not constant

But remember:

$$
F = - kx
$$

Remember that the work done by a non constant force is:

$$
W = \sum_{i}^{}{\overset{\rightarrow}{F}}_{i} \cdot \Delta{\overset{\rightarrow}{r}}_{i} = \int_{i}^{f}\overset{\rightarrow}{F}d\overset{\rightarrow}{r}
$$

And the initial and final conditions are:

Initial = $S_{max} \rightarrow$ max stretch

Final = $0 \rightarrow$ relaxed

Sub in the force for hose into the equation for work done by a non constant force:

$$
W = \int_{S_{max}}^{0}( - kx)(dx) = - \frac{1}{2}kx^{2}
$$

Solve the resultant:

$$
W = - \frac{1}{2}k(0)^{2} - \lbrack - \frac{1}{2}ks_{max}^{2}\rbrack = \frac{1}{2}k(s)_{max}^{2}
$$

$$
W > 0
$$

makes sense because

$$
\Delta K > 0
$$

Going back a couple of steps we now have an equation for work which we can relate to our previous equation for v\_{f}.

$$
V_{f} = \sqrt{\frac{2W}{m}}
$$

$$
W = \frac{1}{2}S_{max}^{2}
$$

Substitute work in the equation for $v_{f}$

$$
V_{f} = \sqrt{\frac{2}{m}(\frac{1}{2}ks_{max}^{2})}
$$

Simplify down to:

$$
= \sqrt{\frac{k}{m}}S_{max}
$$

Sub in values for known variables and solve for $v_{f}$

$$
v_{f} = \sqrt{\frac{100N/m}{0.5kg}}(3.5m)^{2} \rightarrow 50m/s = 111mph
$$
