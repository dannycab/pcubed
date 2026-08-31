---
title: "Non-constant Force: Springs & Spring-like Interactions"
weight: 2
textbook_ref: "Section 4.10, 4.11 and 4.12 in Matter and Interactions (4th edition)"
---

In all real-world interactions, the forces acting on a system change with time. This complication is often ignored in physics courses. We often model the motion of systems using constant forces (e.g., the gravitational force near the surface of the Earth) without additional complications (e.g., velocity dependent drag forces).

However, there are several interactions whose strength and direction depend on the location (and not the velocity) of a system. The simplest of such interactions is the spring force. **In these notes, you will read about the spring force, how to determine if the interactions of a system can be modeled using a spring-like force, and how to model the motion of a system subject to spring interaction.**

## Model of a Spring

The simulation below shows the interaction of a mass on a spring.

Interactive simulation: Mass on a Spring — <https://glowscript.org/#/user/danny/folder/Shared/program/HorizontalSpring>

If we plotted the location of this mass (relative to its average location) as a function of time for 10 seconds, we might observe the following:

Interactive simulation: Plot of spring-mass system — <https://glowscript.org/#/user/danny/folder/Shared/program/SpringMassGraphs>

You might have seen this kind of plot before. It's a [sinusoidal function](http://en.wikipedia.org/wiki/Sine_wave), in this case it's a sine curve. So the formula that describes this function could be something like:

$$
x(t) = A\sin\left( \frac{2\pi}{T}t \right)
$$

Here the amplitude (or maximum “height”) of the curve is $A$, and the period (the time between repeated parts of the curve) is $T$. For a spring system the period is related to the spring constant ($k$) and the mass ($m$),

$$
T = 2\pi\sqrt{\frac{m}{k}}
$$

Notice the spring returns to its original location every 6 seconds or so; this is roughly the period of the spring-mass system. *In the simulation above, the animation is not in real time.*

The frequency of the oscillation (what you call the periodic motion) is given by:

$$
f = \frac{1}{T}
$$

as is measured in Hertz (Hz). Finally, because the motion is sinusoidal (i.e., it depends on $\sin$ and/or $\cos$), you can represent the motion in the following way,

$$
x(t) = A\sin(\omega t)
$$

where $\frac{2\pi}{T}$ has replaced by an *angular frequency*, $\omega$. Evidently,

$$
\omega = \frac{2\pi}{T}
$$

*where* $\omega$ *is the rate of oscillation in terms of how many radians the spring-mass system moves through each second (rad/s).*

[Robert Hooke](http://en.wikipedia.org/wiki/Robert_Hooke) investigated this type of motion in the mid 1600s[<sup>1)</sup>](/notes/week-04-05-springs-contact-interactions/springmotion/#fn__1). He found that the interaction (force) that gave rise to this motion was one that increased linearly with the displacement of the object (stretch or compression of the spring) and that was directed opposite the direction of this displacement. In other words, if you stretch a spring (by pulling it), it will pull back on you. If you compress it (by pushing it), it will push back on you. Moreover, these two forces will be equal in size if the stretch and compression are of the same size.

### The spring force is a non-constant force

The force that a spring will exert depends on how far and in what direction it is stretched (or compressed) relative to its *relaxed length.* All springs have a relaxed length where they are neither stretched nor compressed. Mathematically, you can express Hooke's model for the spring force like this:

$$
{\overset{\rightarrow}{F}}_{spring} = - k_{s}\overset{\rightarrow}{s}
$$

where $k_{s}$ is the spring constant that characterizes the stiffness of the spring[<sup>2)</sup>](/notes/week-04-05-springs-contact-interactions/springmotion/#fn__2). The vector $\overset{\rightarrow}{s}$ describes the stretch of the spring. It's magnitude is the difference of the length of the spring from its relaxed length,

$$
|\overset{\rightarrow}{s}| = |L - L_{0}|
$$

where $L$ is the length of spring (stretched or compressed) and $L_{0}$ is the relaxed length of the spring.

### Why the minus sign?

In the formula for the spring force, the stretch of the spring is a vector ($\overset{\rightarrow}{s}$) that points in the direction of the stretch. We observe that the spring force always points in the direction opposite the stretch, so the minus sign in the formula takes care of (and reminds you of) that.

Sometimes, it's useful to first calculate the size of the spring force (i.e., it's magnitude) and then determine the direction in the coordinate system that you have chosen.

## When is an interaction spring-like?

The spring force is not a [fundamental force of nature](http://en.wikipedia.org/wiki/Fundamental_interaction#The_interactions) ([as you will learn](/notes/week-06-solids-curved-motion/model_of_solids/)), but rather it has come to be used to describe a class of forces that can modeled using the spring force formula. Any interaction that increases linearly with the displacement of an object and points opposite the direction of that displacement is a spring-like interaction.

As it turns out spring-like interactions are ubiquitous in nature because [near their equilibria](https://en.wikipedia.org/wiki/Mechanical_equilibrium), many systems have softly-sloping energy profiles that are similar to those of spring systems. You will learn [more about that later](/notes/week-08-potential-energy-applications/spring_pe/).

#### Limits of the spring model

There is a length beyond which a spring will no longer return to its relaxed length after being stretched. This is the [*elastic limit*](http://en.wikipedia.org/wiki/Yield_(engineering)). If you stretch or compress a spring beyond this point, the force is no longer linear with displacement and the elasticity of the spring will break down.

You can experimentally determine the elastic limit of a spring by hanging successively more weight on it and measuring the stretch. After each measurement, remove the weights and measure the relaxed length of the spring. When that length becomes measurably longer than the initial relaxed length measurement, you can be sure you've reached the elastic limit.

## Modeling Motion with Spring Forces

A spring interaction is a non-constant force, which makes systems that experience spring interactions the perfect candidates for [iterative motion prediction](/notes/week-02-modeling-motion-net-force/iterativepredict/). As you might remember, there were 4 steps to predicting motion iteratively:

- Calculate the (vector) forces acting on the system.
- Update the momentum of the system: ${\overset{\rightarrow}{p}}_{f} = {\overset{\rightarrow}{p}}_{i} + {\overset{\rightarrow}{F}}_{net}\Delta t$.
- Update the position of the system: ${\overset{\rightarrow}{r}}_{f} = {\overset{\rightarrow}{r}}_{i} + {\overset{\rightarrow}{v}}_{avg}\Delta t$.
- Repeat

For the spring force (as well as other non-constant forces), you will use “output” that you obtain about the system from the first 3 steps (i.e., new momentum, new velocity, and new position) as the “input” for the next set of predictions. For the case of spring interactions, you will use the new position of the system to calculate the new spring force. Use the spring force to determine the new momentum, and thus, the new position of the system. Then, repeat.

### For predictions, the time step is really important

For [constant force motion](/notes/week-02-modeling-motion-net-force/constantf/), the time step ($\Delta t$) was not important because the average velocity (${\overset{\rightarrow}{v}}_{avg} = \frac{\Delta\overset{\rightarrow}{r}}{\Delta t}$) and the *arithmetic* average velocity (${\overset{\rightarrow}{v}}_{avg} = \frac{{\overset{\rightarrow}{v}}_{f} + {\overset{\rightarrow}{v}}_{i}}{2}$) were identical. When motion a system results from non-constant interactions, this is no longer true. Consider the figure below, which show predictions of the motion of a spring-mass system using different time steps. Here, you can clearly see that the smaller the time step, the more accurate the plot becomes (i.e., closer to the sinusoidal solution we expect).

Interactive simulation: Plot of spring-mass system for different time steps — <https://msuperl.org/interactive/mechanics/sinusoidal_position_vs_time_coarse_fine.html>
