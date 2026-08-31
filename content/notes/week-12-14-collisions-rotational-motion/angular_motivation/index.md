---
title: "Why Angular Momentum?"
weight: 2
textbook_ref: "Section 5.4 in Matter and Interactions (4th edition)"
---

It seems like [conservation of momentum](/notes/week-04-05-springs-contact-interactions/collisions/#momentum_is_never_conserved) and [conservation of energy](https://www.msuperl.org/wikis/pcubed/doku.php?id=183_notes:energy_cons) can helps us describe any and all observations that you have. Indeed, both of these principles are quite powerful and can be used in many situations. However, there are some situations where a new idea must be brought to bear to be able to predict or explain the motion of the system. **In these notes, you will read about a puzzle where linear momentum and energy are insufficient to explain the motion.**

## Catching A Ball

### An Observation You Can Explain With Momentum and Energy

Consider a person sitting on a stool that is free to rotate. Another person throws a heavy ball (like a medicine ball) directly at the sitting person and “nothing happens”. The sitting person catches the ball but there's no observable motion. This is demonstrated in the first clip in the video below.

{{< youtube dOIrX12UXQU >}}

*This video is primarily used for visual learning. No audio is within this demonstration video.*

**This is an inelastic collision.** You have read how to [deal with this kind of collision](/notes/week-08-potential-energy-applications/colliding_systems/#inelastic_collisions) and you can explain this observation relatively well with conservation of momentum and energy.

- The frictional force by the floor is large enough to keep the stool and the sitting person from sliding away. That is, for the system of the sitting person, the ball, and the stool, *there is an external force by the floor that changes the momentum of that system.*

$$
\Delta{\overset{\rightarrow}{p}}_{sys} = {\overset{\rightarrow}{F}}_{ext}\Delta t
$$

$$
{\overset{\rightarrow}{F}}_{floor} = \frac{\Delta{\overset{\rightarrow}{p}}_{sys}}{\Delta t}
$$

With estimates of the velocity and mass of the ball as well as the collision time, you can determine the frictional force that the floor exerts on the stool.

- The collision is inelastic, so the kinetic energy of this system is not conserved, which is fairly obvious. Initially, the system has kinetic energy (the ball is moving) and in the final state, it does not. The system's internal energy has increased as a result. Because there is no displacement, the floor does not work. We can further assume (as we have in other collisions) that there is no exchange of energy due to a temperature difference.

$$
\Delta E_{sys} = W_{surr} + Q
$$

$$
\Delta E_{sys} = \Delta K_{ball} + \Delta E_{internal} = 0
$$

$$
\Delta E_{internal} = - \Delta K_{ball}
$$

Again, with estimates of the velocity and mass of the ball, you can determine the increase in internal energy of the system as a result of the collision.

- Changing the mass or speed of the ball, changes the force entered by the floor, and internal energy changes up to a point. Perhaps, with a large enough ball thrown fast enough, the stool will slide (or the person is knocked over).

### An Observation You Can't Fully Explain

Consider the same two people, but now the ball is thrown just to the left (or right) of the stool so that the person on the stool catches it just to the side. This is demonstrated in the second and third clips in the video below.

{{< youtube dOIrX12UXQU >}}

*This video is primarily used for visual learning. No audio is within this demonstration video.*

Now, when the ball is caught, the person in the stool begins to rotate. There are a few other observations that you can make (depending on how much friction is in the bearings):

- Tossing a bigger (more massive) ball at the same speed results in a faster rotation.
- Tossing the same ball faster results in the a faster rotation.
- Tossing the same ball at the same speed, but catching it farther from the rotation axis results in a faster rotation.

This situation is similar to the the previous one, linear momentum can help explain the size of the frictional force due to the floor. Furthermore, the system has translational kinetic energy to begin with. But, the system now has rotational kinetic energy in addition to internal energy in the final state. So, you unable to predict how it is going to rotate because the system experiences both changes.

$$
\Delta E_{sys} = W_{surr} + Q
$$

$$
\Delta E_{sys} = \Delta K_{ball} + \Delta K_{rot} + \Delta E_{internal} = 0
$$

$$
\Delta K_{rot} + \Delta E_{internal} = - \Delta K_{ball}
$$

Conservation of linear momentum and energy are insufficient to describe this observation fully. You will need a new physical principle to do so: [conservation of angular momentum](/notes/week-12-14-collisions-rotational-motion/l_conservation/).
