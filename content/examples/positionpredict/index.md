---
title: 'Example: Predicting the location of a object undergoing constant velocity motion'
weight: 34
---

A cart is given a slight push along a near frictionless track (as shown in the video below).

{{< youtube sdjsaxLfevQ >}}

After the push, the cart is observed to move with a near constant velocity ${\overrightarrow{v}}_{cart} = \langle 1.2,0,0\rangle\frac{m}{s}$. Determine its location after 3 seconds.

## Setup

You need to predict the location of the cart using the information provided and any information that you can collect or assume.

### Facts

- The cart moves to the right.
- The cart's velocity is given by ${\overrightarrow{v}}_{cart} = \langle 1.2,0,0\rangle\frac{m}{s}$.

### Lacking

- The initial location of the cart is not known.

### Approximations & Assumptions

- The interactions of the cart with its surroundings, over the interval that you care about, are negligible. That is, the cart moves with a constant velocity.
- As a result, the average and instantaneous velocity are equivalent.
- We will assume the initial location of the cart is ${\overrightarrow{r}}_{i}$.

### Representations

- The location of the cart can be predicted using the position update formula, ${\overrightarrow{r}}_{f} = {\overrightarrow{r}}_{i} + {\overrightarrow{v}}_{avg}\Delta t$
- The motion of the cart is represented using the following motion diagram.

{{< simulation src="https://glowscript.org/#/user/danny/folder/Shared/program/FanCarConstantVelocity" title="Simulation of Fan Cart moving with Constant Velocity" >}}

## Solution

We can compute the final location,

$$
{\overrightarrow{r}}_{f} = {\overrightarrow{r}}_{i} + {\overrightarrow{v}}_{avg}\Delta t = {\overrightarrow{r}}_{i} + {\overrightarrow{v}}_{cart}\Delta t = {\overrightarrow{r}}_{i} + \langle 1.2,0,0\rangle\frac{m}{s}(3s) = {\overrightarrow{r}}_{i} + \langle 3.6,0,0\rangle m
$$

You might use the video to define an origin such that the initial position of the cart is ${\overrightarrow{r}}_{i} = \langle 0.4,1.1,0\rangle m$. With that new information, the final location of the cart can be computed exactly,

$$
{\overrightarrow{r}}_{f} = {\overrightarrow{r}}_{i} + \langle 3.6,0,0\rangle m = \langle 0.4,1.1,0\rangle m + \langle 3.6,0,0\rangle m = \langle 4.0,1.1,0\rangle m
$$

.

Notice that $y$-position of the cart remained unchanged because all the motion of the cart was in the $x$-direction.
