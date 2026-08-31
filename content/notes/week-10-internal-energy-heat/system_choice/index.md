---
title: "Choosing a System Matters"
weight: 4
textbook_ref: "Section 7.7, 7.8 and 7.9 in Matter and Interactions (4th edition)"
---

Earlier, [you read about a puzzle involving a ball falling to the Earth](https://www.msuperl.org/wikis/pcubed/doku.php?id=183_notes:energy_cons#multi-particle_systems). We resolved this puzzle by introducing [the concept of potential energy](/notes/week-07-energy-transfer/potential_energy/). **In these notes, you will look an example of a person lifting a box using different choices of system**. The goal here is to demonstrate that the choice of a system matters.

## Lifting a box

A person is lifting a box (of mass $m$) from the ground to a height $h$. At that height, the box is moving with an upward speed $v$. To lift the box, we assume the person applies a force $F$ upward. Let's consider three different choices of the system to demonstrate what can be learned from each choice.

### System 1: Box, Earth, and Person

While lifting the box, the person's internal energy will change, so we will keep track of that change with $E_{person}$.

- System: Box, Earth, and Person; Surroundings: Nothing
- Initial State: Box on the ground with no velocity; Box at height $h$ with velocity $v$

$$
\Delta E_{sys} = W_{surr}
$$

$$
\Delta K_{box} + \Delta U_{grav} + \Delta E_{person} = 0
$$

$$
\frac{1}{2}mv^{2} + mgh + \Delta E_{person} = 0
$$

$$
\Delta E_{person} = - \left( \frac{1}{2}mv^{2} + mgh \right)
$$

Here we find that the person experiences an internal energy change that is negative, which makes sense because they are expending energy to lift the box. This system is the only one in which we can find this energy change because it is the only one that includes the person.

Notice that in this system, the person does no work on the box because the box and person are in the system. Instead, we are accounting for the change in energy of the person.

### System 2: Box only

Because the system is only a single particle, there can be no potential energy. There is work done by both the person and the Earth, but they have opposite signs because the applied force and the gravitational force are in different directions.

- System: Box; Surroundings: Earth and Person
- Initial State: Box on ground with no velocity; Box at height $h$ with velocity $v$

$$
\Delta E_{sys} = W_{surr}
$$

$$
\Delta K_{box} = W_{person} + W_{Earth}
$$

$$
\frac{1}{2}mv^{2} = Fh - mgh
$$

$$
\frac{1}{2}mv^{2} = (F - mg)h
$$

Here we find that the person had to exert a force that was larger than the weight of the box because the kinetic energy change is positive and thus the work done must be positive. We could not conclude that from an analysis of System 1; it required a different system.

Notice also that because the person is outside the system, we no longer consider the internal energy change of the person, but the work the person does on the box while lifting it.

### System 3: Box and Earth

Finally, this system has potential energy, but there is work done by the person.

- System: Box and Earth; Surroundings: Person
- Initial State: Box on ground with no velocity; Box at height $h$ with velocity $v$

$$
\Delta E_{sys} = W_{surr}
$$

$$
\Delta K_{box} + \Delta U_{grav} = W_{person}
$$

$$
\frac{1}{2}mv^{2} + mgh = Fh
$$

Here we find that a similar result as in System 2, but also explicitly note the the person does no work on the Earth because the displacement of the Earth as result of the person's feet pushing down is negligible. This realization requires analysis using System 3.

### The Choice of System Determines Energy Accounting

As you read, different choices of system result in different conclusions that you can make about the motion of the system. How energy is accounted for is different in different systems (e.g. whether to consider internal energy changes or work done). Choosing different systems in which to analyze the energy can help draw more complete conclusions and explanations about the motion of systems.
