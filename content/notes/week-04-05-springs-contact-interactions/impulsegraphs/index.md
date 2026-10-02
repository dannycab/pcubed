---
title: "Impulse Graphs"
weight: 1
textbook_ref: "Sections 2.1, 2.2, 2.3 and 2.4 in Matter and Interactions (4th edition)"
---

As you read earlier, the [Momentum Principle is used to explain and predict](/notes/week-02-modeling-motion-net-force/momentum_principle/) the motion of systems. These predictions and explanations can be [represented mathematically](/notes/week-02-modeling-motion-net-force/motionpredict/), but it also possible to make use graphs to do so. **In these notes, you will read about force vs time graphs and how they can be used to determine the change in momentum of a system.** This change is often called the *impulse* delivered to the system.

## Lecture Video

{{< youtube id="RXJ0XlcPBRg" title="Lecture 4: Force vs. Time" >}}

## Change in Momentum or "Impulse"

The change in the momentum of a system (also called the *impulse* delivered by the net force) is related by the Momentum Principle to the force acting on the system:

$$\Delta\overset{\rightarrow}{p} = {\overset{\rightarrow}{F}}_{net}\Delta t$$

In this form, the change in momentum is the total change over some discrete time interval $\Delta t$. If the force is not constant (e.g., if it depends on location or velocity), the impulse depends on the *average* net force over the time interval:

$$\Delta\overset{\rightarrow}{p} = {\overset{\rightarrow}{F}}_{net,avg}\Delta t$$

This definition works well if you are using [iterative procedures to determine the change in momentum](/notes/week-02-modeling-motion-net-force/iterativepredict/) over small time intervals, such as with computer modeling.

On the other hand, if you know the force in a form you can integrate analytically, then you can use the differential form of the momentum principle,

$$\Delta\vec{p} = \int_{t_{i}}^{t_{f}}{\vec{F}}_{net}\mkern{6mu} dt.$$

These are vector equations, so they apply to each component individually: for example, $\Delta p_{x} = F_{x,net}\,\Delta t$, and similarly for $y$ and $z$.

## Force vs. Time Graphs

As usual when dealing with integrals, graphs of force vs. time can be useful for understanding and visualizing changes in momentum. And in many situations, it is easier to measure force empirically because the physical dynamics are too complex to describe theoretically, so the force vs. time graph is the only information available about the system. This is true in various engineering contexts (e.g., impact design and fluid flow) as well as scientific contexts such as plasma dynamics or cosmology.

In these cases, we can determine the change in momentum (and thus the velocity) of the system based on repeated measurements of the net force acting on the system. (We can also go further and determine the displacement of the system based on velocity vs. time graphs produced from analyzing the force vs time graphs.)

Below is a force vs time graph where the “area under the curve” has been highlighted. In this example, we are only looking at the component of the net force in the $x$-direction. Such graphs can be produced for each component of the net force, but let's assume that for this system, the net force was non-zero only in the $x$-direction.

{{< simulation src="https://demos.msuperl.org/interactive/mechanics/net_force_vs_time_discrete.html" title="Impulse Graph" >}}

For the above figure, the momentum change over the complete time interval can be added up in a straightforward way due to the simple geometric shapes produced. Areas above the zero line (in blue) are positive momentum changes, and areas below (in red) are negative. By adding up the “area under the curve” in this way, we obtain a momentum change of 7 N$\bullet$s.

The figure below shows the force vs time graph for another system. In this case, the graph has a smooth form, which doesn't appear to be analytic. The “area under the curve” for this graph could be analyzed computationally, by [taking small steps (i.e., Riemann Sum)](http://en.wikipedia.org/wiki/Riemann_sum), and the change in momentum could be estimated.

{{< simulation src="https://demos.msuperl.org/interactive/mechanics/net_force_vs_time_smooth.html" title="Impulse Graph" >}}
