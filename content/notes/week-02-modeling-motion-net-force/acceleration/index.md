---
title: "Acceleration & The Change in Momentum"
weight: 3
---

As you read, [the motion of a system is governed by the Momentum Principle](/notes/week-02-modeling-motion-net-force/momentum_principle/) (aka “Newton's Second Law of Motion). In these notes, you will learn another way to write the momentum principle, and how that relates to the concept of acceleration.

## Newton's Second Law

The Momentum Principle (or Newton's Second Law) is a quantitative description for how a system changes its momentum when the system experiences an external force. You might already know that another way to write this principle uses the concept of acceleration (how the velocity changes with time). Mathematically, we can write Newton's Second Law like this:

$$
{\overset{\rightarrow}{F}}_{net} = m\ \overset{\rightarrow}{a} = \frac{\Delta\overset{\rightarrow}{p}}{\Delta t}
$$

where the last bit shows how Newton's Second Law is related to the Momentum Principle. We can take this a bit further to determine the acceleration in terms of the velocity,

$$
\overset{\rightarrow}{a} = \frac{\Delta\overset{\rightarrow}{p}}{m\ \Delta t} = \frac{m\Delta\overset{\rightarrow}{v}}{m\ \Delta t} = \frac{\Delta\overset{\rightarrow}{v}}{\Delta t}
$$

*where the last two equals signs hold only if the mass of the system is not changing.*

## Acceleration

**Acceleration** is a vector quantity that quantifies how quickly the velocity of a system is changing. The units of acceleration are **meters per second per second** ($\frac{m}{s^{2}}$).

The acceleration can be defined in two ways and each is useful in different problems or ways of thinking. From Newton's Second Law, we can obtain a definition using the net force,

$$
\overset{\rightarrow}{a} = \frac{{\overset{\rightarrow}{F}}_{net}}{m}
$$

*Notice that this means that the acceleration of system always points in the direction of the net force (because mass is always a positive quantity).*

It can also be defined (as above) in terms of the change in velocity over time. If this change is calculated over a time interval ($\Delta t$), then you obtain the *average acceleration,*

$$
{\overset{\rightarrow}{a}}_{avg} = \frac{\Delta\overset{\rightarrow}{v}}{\Delta t} = \frac{{\overset{\rightarrow}{v}}_{f} - {\overset{\rightarrow}{v}}_{i}}{\Delta t}
$$

If we allow the time interval to shrink ([as we did with the average velocity](/notes/week-01-modeling-motion-no-net-force/displacement_and_velocity/#speed_and_velocity)), we obtain *the instantaneous acceleration,*

$$
\overset{\rightarrow}{a} = \lim_{\Delta t \rightarrow 0}{\overset{\rightarrow}{a}}_{avg} = \lim_{\Delta t \rightarrow 0}\frac{\Delta\overset{\rightarrow}{v}}{\Delta t} = \frac{d\overset{\rightarrow}{v}}{dt}
$$

## Why not just use change in momentum?

If you have one way of describing motion (i.e., using the concept of a change in momentum), why should you learn about acceleration?

Acceleration is a useful concept in mechanics, because it can help characterize the motion of systems (e.g., constant velocity motion has no acceleration).

While you can obtain this information by determining the forces acting on the system, it's possible to use observational information (how the position changes) to determine how the system is accelerating without knowing the system's mass or the forces acting on the system. This is incredibly useful for any type of data collection. Any data collected about the motion of a system only records the position of the system as function of time. *From the changes in position (displacement), the velocity can be inferred. From the changes in the velocity, the acceleration can be inferred and thus the motion of the system can be characterized and explained.*
