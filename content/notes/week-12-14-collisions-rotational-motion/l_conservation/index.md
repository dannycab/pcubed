---
title: "Conservation of Angular Momentum"
weight: 8
textbook_ref: "Section 11.7 in Matter and Interactions (4th edition)"
---

You have read about the angular momentum principle and how systems with no net torque about a point experience no change in angular momentum. This is the final conservation principle of mechanics: the conservation of angular momentum. **In these notes, you will learn how to predict the motion of systems using conservation of angular momentum, and resolve [the puzzle of the tossed ball-stool rotation demo](/notes/week-12-14-collisions-rotational-motion/angular_motivation/).**

## Reminder

{{< youtube dOIrX12UXQU >}}

**Video Note:** *There is no audio component to this demonstration video. Focus on the visual aid of the placement of the ball and how it affects the instructors motion in the chair specifically as it related to the circular motion.*

## Angular Momentum is Conserved

**When a system experiences no net torque about a point, angular momentum is conserved.** But, sometimes, there is no location about which a system experiences no net torque; other times, it might be difficult to find that point. Choosing the system appropriately will often ensure there is no external torque on the system.

For example, if the rotation occurs due to the torque exerted by some known object, putting that object into the system removes it from the surroundings. Thus that object is no longer considered to exert a torque on the system (a system cannot exert a torque on itself). The object transfers angular momentum to other parts of the system. This is a good method for dealing with the situations.

For the [ball-person-stool demonstration](/notes/week-12-14-collisions-rotational-motion/angular_motivation/) a good choice of system is the ball, person, and stool. In this case, initially the ball has translational angular momentum about the stool axis (remember you still have to pick an axis to determine the angular momentum). *As the ball is caught, some of that translational angular momentum is transferred to the person and stool.* You read that this translational angular momentum of the ball becomes rotational angular momentum because the whole system rotates with the same angular speed.

If all the objects are in the system, there are no external torques hence, the initial and final angular momentum of the system are the same,

$$
\Delta{\overset{\rightarrow}{L}}_{sys} = 0 \rightarrow {\overset{\rightarrow}{L}}_{sys,i} = {\overset{\rightarrow}{L}}_{sys,f}
$$

The magnitude of the translational angular momentum of the system initially is related to the ball's mass, speed, and the perpendicular distance between the ball and the chosen rotation rotation axis,

$$
L_{sys,i} = m_{ball}v_{ball}r_{\bot}
$$

The magnitude of the rotational angular momentum of the system in the final state is related to the moment of inertia of the whole ball-stool-person system and the angular speed of the system about its rotation axis.

$$
L_{sys,f} = I_{sys}\omega
$$

Hence, we can predict the angular speed of the system in the final state given the system's initial state.

$$
L_{sys,i} = m_{ball}v_{ball}r_{\bot} = I_{sys}\omega = L_{sys,f}
$$

$$
\omega = \frac{m_{ball}v_{ball}r_{\bot}}{I_{sys}}
$$

The [prior observations that you](/notes/week-12-14-collisions-rotational-motion/angular_motivation/) had fit with this result. The rotation is increased by increasing the mass or speed of the ball, or by increasing the perpendicular distance the ball is from the rotation axis.
