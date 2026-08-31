---
title: 'Example: Rotational Kinetic Energy and Work'
weight: 37
---

In the figure which is in the representations section you observe that a wheel is mounted on a stationary axel, which is nearly frictionless so that the wheel turns freely. The wheel has an inner ring with mass 5 kg and radius 10 cm and an outer ring with mass 2 kg and radius 25 cm; the spokes have negligible mass. A string with negligible mass is wrapped around the outer ring and you pull on it, increasing the rotational speed of the wheel. During the time that the wheel's rotation changes from 4 revolutions per second to 7 revolutions per second, how much work do you do?

## Facts

Inner ring of wheel has a mass of 5 kg and radius 10 cm

Outer ring has a mass of 2 kg and a radius of 25cm

String with negligible mass is wrapped around the outer ring and pulled on.

## Assumptions and Approximations

The rod has to be sufficiently thin so your not worried about contributions to the moment of inertia from parts of the rod that are further away from the center of mass.

Stationary axle is nearly frictionless so that the wheel turns freely.

The spokes of the wheel have negligible mass.

String wrapped around the outer ring has negligible mass.

## Lacking

During the time that the wheel's rotation changes from 4 revolutions per second to 7 revolutions per second, how much work do you do?

## Representations

System: Wheel and string

Surroundings: Your hand, axle, Earth

$E_{f} = Ei + W$​

$K_{rot} = \frac{1}{2}I\omega^{2}$​

$I = m_{1}r_{\bot 1}^{2}$ + $m_{2}r_{\bot 2}^{2}$

## Solution

From the Energy Principle:

$E_{f} = Ei + W$​

Substitute in equation for rotational energy for energy initial and energy final.

$\frac{1}{2}I\omega_{f}^{2} = \frac{1}{2}I\omega_{i}^{2} + W$​

You are trying to find work so rearrange the equation to isolate W.

$W = \frac{1}{2}I(\omega_{f}^{2} - \omega_{i}^{2})$​

What is the moment of inertia $I = m_{1}r_{\bot 1}^{2}$ + $m_{2}r_{\bot 2}^{2}$ + $m_{3}r_{\bot 3}^{3}$ + $m_{4}r_{\bot 4}^{4} + \cdot \cdot \cdot$ ? Group this sum into a part that includes just the atoms of the inner ring and another part that includes just the atoms of the outer ring:

$I = (m_{1}r_{\bot 1}^{2}$ + $m_{2}r_{\bot 2}^{2}$ + $\cdot \cdot \cdot )_{inner}$ + $(m_{1}r_{\bot 1}^{2}$ + $m_{2}r_{\bot 2}^{2})_{outer}$ + $\cdot \cdot \cdot$

The total inertia is then the inertia inner + the inertia outer.

$I = I_{inner} + I_{outer}$​

This is a general result: The moment of inertia of a composite object is the sum of the moments of inertia of the individual pieces, because we have to add up all the contributions of all the atoms. We already determined that the moment of inertia of a ring is $MR^{2}$ (all the atoms are at the same perpendicular distance R from the center), so the moment of inertia of this wheel is:

$I = M_{inner}R_{inner}^{2} + M_{outer}R_{outer}^{2}$​

Substitute the corresponding values for the variables:

$I = (5kg)(.1m)^{2}$ + $(2kg)(.25m)^{2}$ = $(0.050 + 0.125)kg \cdot m^{2} = 0.175kg \cdot m^{2}$

We need to convert revolutions per second into radians per second:

$\omega_{i} = (4\frac{rev}{s})(\frac{2\pi\mspace{6mu} radians}{rev}) = 25.1\mspace{6mu} radian\mspace{6mu} s/s$​

$\omega_{f} = (7\frac{rev}{s})(\frac{2\pi\mspace{6mu} radians}{rev}) = 44.0\mspace{6mu} radian\mspace{6mu} s/s$​

You, the Earth, and the axle will exert forces on the system. How much work does the Earth do? Zero, because the center of mass of the wheel doesn't move. How much work does the axle do? If there is negligible friction between the axle and the wheel, the axle does no work, because there is no-displacement of the axle's force. Therefore only you do work, and the work that you do is

$W = \frac{1}{2}(0.175kg \cdot m^{2})({44.0}^{2} + {25.1}^{2})\frac{radians^{2}}{s^{2}} = 114J$​
