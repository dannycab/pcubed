---
title: "Escape Speed"
weight: 5
textbook_ref: "Section 6.10 in Matter and Interactions (4th edition)"
---

Gravitational systems are particularly interesting because there are so many examples of such systems. The formation of our universe from immense galactic structures to solar systems with planets and moons, and even the orbits of asteroids and comets are all examples of gravitational systems. **In these notes, you will read about a particular gravitational phenomenon: how a small object can escape the gravitational bounds of a much more massive object. This object must move with at least the escape speed.**

## Conditions on the Speed

Consider trying to throw a rock with a speed $v$ away from an airless planet. There's three possible outcomes:

1.  $v < v_{esc}$; the rock will rise to a maximum height above the surface and fall back down.
2.  $v > v_{esc}$; the rock will be moving with some speed as it approaches $r \rightarrow \infty$.
3.  $v = v_{esc}$; the rock will have just enough kinetic energy to escape the planet (as $r \rightarrow \infty$; $v \rightarrow 0$)

The final outcome defines the escape speed ($v_{esc}$).

## Calculating the Escape Speed

Consider a planet of mass $M$ and radius $R$. A small object of mass $m$ is thrown with a speed equal to the escape speed for the planet. What is this speed? First, you define a system.

- System: Planet + object
- Surroundings: nothing

The initial and final states are well-defined because you know the condition for escape.

- Initial: $r = R$ (surface of planet); $v = v_{esc}$
- Final: $r = \infty$; $v = 0$

The [Energy Principle tells you that the energy of this system is conserved](https://www.msuperl.org/wikis/pcubed/doku.php?id=183_notes:energy_cons). *Moreover, you know from the final state where* $r \rightarrow \infty$ *and* $v \rightarrow 0$ *that both the final potential and final kinetic energies are zero. Hence, the total energy of the system must be zero.*

$$
\Delta E_{sys} = W_{surr} = 0 \rightarrow E_{sys,f} = E_{sys,i}
$$

$$
K_{f} + U_{f} = K_{i} + U_{i} = 0
$$

So the you can use the initial kinetic and potential energy here because they are both nonzero,

$$
K_{i} + U_{i} = \frac{1}{2}mv_{esc}^{2} - G\frac{Mm}{R} = 0 \rightarrow \frac{1}{2}mv_{esc}^{2} = G\frac{Mm}{R}
$$

Solving for $v_{esc}$, you find:

$$
v_{esc} = \sqrt{\frac{2GM}{R}}
$$

This speed defines the minimum speed needed to leave the planet and never return under the gravitational interaction between the object and the planet. ***Reminder that this speed term utilizes the SI unit of m/s.*** Notice that this speed doesn't depend on the mass of the launched object (so long as it is much less than the planet).
