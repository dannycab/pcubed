---
title: "Impulse Graphs"
weight: 1
textbook_ref: "Section 2.1, 2.2, 2.3 and 2.4 in Matter and Interactions (4th edition)"
---

As you read earlier, the [Momentum Principle is used to explain and predict](/notes/week-02-modeling-motion-net-force/momentum_principle/) the motion of systems. These predictions and explanations can be [represented mathematically](/notes/week-02-modeling-motion-net-force/motionpredict/), but it also possible to make use graphs to do so. **In these notes, you will read about force vs time graphs and how they can be used to determine the change in momentum of a system.** This change is often called the *impulse* delivered to the system.

## Lecture Video

{{< youtube RXJ0XlcPBRg >}}

## Change in Momentum or the "Impulse"

The change in the momentum of a system (or the impulse delivered by the net force) is given mathematically by the Momentum Principle,

$$
\Delta\overset{\rightarrow}{p} = {\overset{\rightarrow}{F}}_{net}\Delta t
$$

In this form, the change in momentum is calculated over a “discrete” time step. That is, the calculation is done over a known or determined time interval. If the force is non-constant (i.e., depends on location or velocity), this calculation is not exact. In fact, in this case, the net force is the *average* net force over the time interval. So that a better definition is this:

$$
\Delta\overset{\rightarrow}{p} = {\overset{\rightarrow}{F}}_{net,avg}\Delta t
$$

This definition works well for case where you might use [iterative procedures to determine the change in momentum](/notes/week-02-modeling-motion-net-force/iterativepredict/) over small time intervals. If on the other hand, you can analytically integrate the force (e.g., it is or can be put into a form which is time dependent), then you can use the derivative form of the Momentum Principle,

$$
\Delta p = \int_{t_{i}}^{t_{f}}{\overset{\rightarrow}{F}}_{net}\mspace{6mu} dt
$$

In any event, either (or both) can be useful to think about graphs of force vs time.

## Force vs Time Graphs

In some situations, it is easier to empirically measure force versus time graphs because the situations lend themselves more easily to these empirical measurements rather than what might be more complex physical theories. This is true in different engineering contexts (e.g., impact design and the flow of fluids). In these cases, you are interested in determining the change in momentum (and thus the velocity) of the system in question[<sup>1)</sup>](/notes/week-04-05-springs-contact-interactions/impulsegraphs/#fn__1).

Below is a force vs time graph where the “area under the curve” has been highlighted. In this example, we are only looking at the component of the net force in the $x$-direction. Such graphs can be produced for each component of the net force, but let's say that for this system, there was a non-zero component of the net force only in the $x$-direction.

Interactive simulation: Impulse Graph — <https://msuperl.org/interactive/mechanics/net_force_vs_time_discrete.html>

For the above figure, the momentum change over the complete time interval can be determined in a straightforward way due to the simple geometric shapes produced. Area above the zero line are positive momentum changes, and area below are negative. By adding up the “area under the curve” in this way, we obtain a momentum change of 7 $N\mspace{6mu} s$.

The figure below shows the force vs time graph for another system. In this case, the graph has a smooth form, which doesn't appear to be analytic. The “area under the curve” for this graph could be analyzed computationally, by [taking small steps (i.e., Riemann Sum)](http://en.wikipedia.org/wiki/Riemann_sum), and the change in momentum could be determined.

Interactive simulation: Impulse Graph — <https://msuperl.org/interactive/mechanics/net_force_vs_time_smooth.html>

------------------------------------------------------------------------

[<sup>1)</sup>](/notes/week-04-05-springs-contact-interactions/impulsegraphs/#fnt__1)

It is possible to determine the displacement of such systems as well. This can be done using velocity vs time graphs that are produced from the analysis of force vs time graphs.
