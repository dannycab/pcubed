---
title: "Applying the Momentum Principle"
weight: 4
textbook_ref: "Section 2.3 in Matter and Interactions (4th edition)"
---

Your primary job in mechanics is to be able to predict or explain the motion of systems. Previously, you read about the [position update formula](/notes/week-01-modeling-motion-no-net-force/displacement_and_velocity/#what_s_so_special_about_constant_velocity_motion), which allows you to predict the future location of a system given information about its current location and its velocity (or [momentum](/notes/week-02-modeling-motion-net-force/momentum/)).

But, a system doesn't need to move with [constant velocity](/notes/week-01-modeling-motion-no-net-force/displacement_and_velocity/) (or momentum); [it can change its momentum (or velocity) as a result of interacting with it surroundings](/notes/week-02-modeling-motion-net-force/momentum_principle/). In these notes, you will read how to predict the future motion of an system that interacts with its surroundings.

### Predicting the Future Momentum

[The Momentum Principle is a central principle of mechanics](/notes/week-02-modeling-motion-net-force/momentum_principle/); it tells you how the momentum of a system will change as a result of its interactions with its surroundings,

$$
\Delta\overset{\rightarrow}{p} = {\overset{\rightarrow}{p}}_{f} - {\overset{\rightarrow}{p}}_{i} = {\overset{\rightarrow}{F}}_{net}\Delta t
$$

which can be rewritten to predict the system's final momentum given information about the system's initial momentum and its interactions (net force). The Update Form of the Momentum Principle is represented mathematically like this:

$$
{\overset{\rightarrow}{p}}_{f} = {\overset{\rightarrow}{p}}_{i} + {\overset{\rightarrow}{F}}_{net}\Delta t
$$

It is critical that the time step over which we are doing the prediction be small enough such that the [net force can be considered a constant vector](/notes/week-02-modeling-motion-net-force/constantf/).

In later notes, you will learn about the [special case of constant force motion](/notes/week-02-modeling-motion-net-force/constantf/) – in that case, the length of the time interval will not matter. But for all other cases you will work with (e.g., [gravitational interactions](/notes/week-03-newtonian-gravitation/gravitation/), [spring-like interactions](/notes/week-04-05-springs-contact-interactions/springmotion/)), the length of the time interval absolutely matters.

#### Separation of Components

The Update Form of the Momentum Princple, like the Momentum Principle itself, is a vector principle. And thus each component of the momentum vector can be predicted,

$$
p_{fx} = p_{ix} + F_{net,x}\Delta t
$$

$$
p_{fy} = p_{iy} + F_{net,y}\Delta t
$$

$$
p_{fz} = p_{iz} + F_{net,z}\Delta t
$$

This might seem trivial, but there is a critical implication. If the force in any direction is zero, then the momentum, and thus the velocity, does not change in that direction.

## Examples

[Predicting the final momentum & velocity using the Momentum Principle](/examples/finalp/)
