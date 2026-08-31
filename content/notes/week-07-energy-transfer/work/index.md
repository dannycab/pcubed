---
title: "Work: Mechanical Energy Transfer"
weight: 3
textbook_ref: "Section 6.3 and 6.4 in Matter and Interactions (4th edition)"
---

As you read earlier, [the change in the total energy of a system is equal to the work done on that system by its surroundings](/notes/week-07-energy-transfer/point_particle/). **In these notes, you will read about the formal definition of work, which is the transfer of mechanical energy, and a mathematical idea that underpins work - the dot product.**

## Lecture Video

{{< youtube f99o5szn6xg >}}

## The Formal Definition of Work

The work that is done by a force is the ***scalar product*** (or dot product) of that force and the displacement.

$$
W = \overset{\rightarrow}{F} \cdot \Delta\overset{\rightarrow}{r} = F_{x}dx + F_{y}dy + F_{z}dz
$$

The dot product is one way that two vectors are “multiplied.” It is the sum of the product of each pair of components. This dot product is related to the angle that the force makes with the displacement. Essentially, the dot product will “pick out” the component of one vector that is parallel to another vector.

<img src="./media/rId15.png" style="width:3.64583in;height:1.90625in" alt="[ALT TEXT NEEDED: figure-01.png -- describe this figure for screen readers]" />

A point particle moves through a distance $d$ while a force $F$ is applied at an angle $\theta$ relative to the displacement.

Consider a point particle that moves through a displacement $\Delta\overset{\rightarrow}{r}$ while it experiences a force $\overset{\rightarrow}{F}$ at an angle $\theta$ relative to the displacement. The work that done on the particle by this force is,

$$
W = \overset{\rightarrow}{F} \cdot \Delta\overset{\rightarrow}{r} = F_{x}\Delta x + F_{y}\Delta y + F_{z}\Delta z = F\cos\theta\Delta r = F\cos\theta d
$$

where the last step considers that the only non-zero part of the dot product is the x bit. That is, the displacement is in the x-direction ($\Delta r$ = d), and the component of the force in that direction is $F\cos\theta$. In general, the work calculation picks out the piece of the force that is parallel to the displacement – that interaction is what increases the energy of the system.

$$
W = \overset{\rightarrow}{F} \cdot \Delta\overset{\rightarrow}{r} = F_{\parallel}\Delta r
$$

The units of work can be determined by the product of the units of its constituent bits.

$$
Work = (Force)*(distance) = (Newtons)*(meters) = Nm = Joule
$$

The units of work is a Joule named after [James Joule](http://en.wikipedia.org/wiki/James_Prescott_Joule), an English physicist and beer brewer. One Joule is equal to 1 $Nm$ or 1 $kgm^{2}/s^{2}$.

## Work can be positive, negative, or zero

<img src="./media/rId21.png" style="width:5.20833in;height:1.82292in" alt="[ALT TEXT NEEDED: figure-02.png -- describe this figure for screen readers]" />

The sign of the work done by a force is determined by the relative direction of the force and the displacement through which the force acts.

The work can increase or decrease the kinetic energy depending on the direction of the force. Consider three situations:

1.  A fan cart where the fan acts in the direction of motion (e.g., the cart starts from rest and speeds up)
2.  A fan cart where the fan acts opposite the direction of motion (here you only watch the fan cart until it is momentarily at rest).
3.  A fan cart where the fan acts perpendicular to the direction of motion (e.g., a fan mounted to push “down” on the car).

In case 1, the force is in the direction of motion, hence the car will speed up and increase its kinetic energy,

$$
W_{1} = {\overset{\rightarrow}{F}}_{1} \cdot \Delta{\overset{\rightarrow}{r}}_{1} = \Delta K_{1} > 0
$$

Evidently, when the force has a component in the direction of motion, the work done by the force is positive; it increases the kinetic energy of the system.

In case 2, the force is opposite the direction of motion, hence the car will slow down and decrease its kinetic energy,

$$
W_{2} = {\overset{\rightarrow}{F}}_{2} \cdot \Delta{\overset{\rightarrow}{r}}_{2} = \Delta K_{2} < 0
$$

When the force has a component opposite the direction of motion, the work done by the force is negative; it decreases the kinetic energy of the system.

In case 3, the force is perpendicular to the direction of motion, hence the cart will neither slow down or speed up. It will experience an increased vertical force due to the track (by [additional compression of the bonds in the track](/notes/week-04-05-springs-contact-interactions/friction/)). This doesn't change the kinetic energy of the cart.

$$
W_{3} = {\overset{\rightarrow}{F}}_{3} \cdot \Delta{\overset{\rightarrow}{r}}_{3} = \Delta K_{3} = 0
$$

When using work, it is critical to pay attention to the relative direction of the force and the displacement to determine how the kinetic energy will change (if at all).

## Lecture Video

\[SIMULATION LINK NEEDS MANUAL REVIEW: "Untitled" -- source URL could not be recovered from this export\]
