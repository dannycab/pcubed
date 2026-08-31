---
title: "Drag"
weight: 8
---

In most real world situations, there is some kind of resistive force. Some of these are due to contact between solid objects (e.g., friction) and you will learn about those later. For now, we will consider resistive forces due to some kind of [fluid](http://en.wikipedia.org/wiki/Fluid), which might be air, water, oil, or [even sand](https://www.youtube.com/watch?v=zjgURBIqJ6s).

## Fluid Resistance

*An object moving in any fluid experiences some form of resistance to its motion due collisions with molecules of the fluid.* Each of these little collisions with the surrounding fluid contribute to the overall resistive force that the fluid exerts on a moving object.

*Unlike friction forces, which are velocity-independent, fluid resistance depends on the velocity of the object in the fluid*. While modeling the molecular collisions with the object can be done, for most purposes, macroscopic models of the fluid drag force are sufficient to model the motion of the object. Below, you will learn about the two most common models: laminar drag and turbulent drag.

## Models of fluid resistance

Which model of fluid resistance is most useful (or valid) depends on the properties of the system in question. Specifically, it depends on the [Reynolds number](http://en.wikipedia.org/wiki/Reynolds_number) of the situation.

A discussion of Reynolds number is beyond the scope of this course, but suffice it to say that an small, slow-moving object in a viscous fluid will have a low Reynolds number. A large, fast moving object in a less viscous fluid will have a high Reynolds number.

An excellent, but long video that describes these different kinds of flows is shown below.

{{< youtube 51-6QCJTAjU >}}

### Laminar drag

For a situation where the *Reynolds number is low* (e.g., a small, slow-moving object in a viscous fluid), the fluid resistance is proportional to the velocity of the object:

$$
{\overset{\rightarrow}{F}}_{drag} = - b\overset{\rightarrow}{v}
$$

where $b$ is a constant factor the depends on different fluid and object parameters. For a spherical object with radius $r$, the fluid resistance takes the form,

$$
{\overset{\rightarrow}{F}}_{drag} = - 6\pi\eta r\overset{\rightarrow}{v}
$$

where $\eta$ is the **fluid viscosity**.

### Turbulent drag

For a situation where the *Reynolds number is high* (e.g., a large, fast-moving object in a less viscous fluid), the fluid resistance is proportional to the speed of the object squared:

$$
{\overset{\rightarrow}{F}}_{drag} = - cv^{2}\widehat{v}
$$

where $c$ is a constant factor the depends on different fluid and object parameters. The constant $c$ can be unpacked f into 3 different parameters:

$$
{\overset{\rightarrow}{F}}_{drag} = - \frac{1}{2}\rho C_{d}Av^{2}\widehat{v}
$$

where $\rho$ is the *density of the fluid*, $A$ *is the cross-sectional area of the object in the fluid*, and $C_{d}$ *is the drag coefficient of the object, which is often measured experimentally*.

### What about "medium" Reynolds numbers flows?

If your system does not exist at either end of the spectrum, where one or the other model dominates, you must use them both at the same time. In these situtations the fluid resistance is given by:

$$
{\overset{\rightarrow}{F}}_{drag} = - b\overset{\rightarrow}{v} - cv^{2}\widehat{v}
$$

However, in many cases you can reasonable assume either a low Reynolds number (a small sphere moving in oil) or a high Reynolds number (most macroscopic things moving in air).
