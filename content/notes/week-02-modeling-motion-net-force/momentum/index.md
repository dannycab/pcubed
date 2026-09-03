---
title: "Momentum"
weight: 1
textbook_ref: "Section 1.8, 1.9, 1.10 and 1.12 in Matter and Interactions (4th edition)"
---

A [central principle of mechanics](https://www.msuperl.org/wikis/pcubed/doku.php?id=course_planning:course_notes:momentum_principle) involves the relationship between momentum and force. *In these notes, you will learn about the concept of momentum, and when it is ok to use the approximate form of the momentum vector.*

### Changes in Motion

When you observe an object's motion changing, you are typically paying attention to how it changes its position. The object can speed up, slow down, or change direction. Each of these changes are changes to the object's velocity.

You might have noticed that when you try to change an object's velocity, for example, by slowing it down, it is often easier to do it for “lighter” objects. That is, it is somehow easier to change the motion of objects that have less mass. *This is due to the plain fact that an object with mass has momentum, and that momentum depends on the mass of the object.*

### Definition of Momentum

**Momentum** is a [vector](/notes/week-01-modeling-motion-no-net-force/scalars_and_vectors/) that quantifies the “ease” with which an object's motion can be changed.

More formally, it is the product of the object's mass (a scalar), its velocity (a vector), and a proportionality constant (that takes into account [relativistic motion](https://en.wikipedia.org/wiki/Special_relativity)). Mathematically, we represent the momentum like this:

$$
\overset{\rightarrow}{p} = \gamma m\overset{\rightarrow}{v}
$$

where the proportionality constant is needed when [objects travel near the speed of light](http://en.wikipedia.org/wiki/Special_relativity). This proportionality constant ($\gamma$, gamma) is given by:

$$
\gamma = \frac{1}{\sqrt{1 - \left( \frac{|\overset{\rightarrow}{v}|}{c} \right)^{2}}}
$$

where $c$ *is the speed of light in vacuum* **(**$c = 3.00 \times 10^{8}\frac{m}{s}$**).**

### When does the $\gamma$ factor matter?

For most motion that is far from the speed of light, the $\gamma$ factor will not result in a major discrepancy between being included and not being included. For example, consider the following table of speeds.

| $&#124;\overset{\rightarrow}{\mathbf{v}}&#124;$ m/s | $&#124;\overset{\rightarrow}{\mathbf{v}}&#124;/\mathbf{c}$​ | $\gamma$​ |
|----|----|----|
| 0 | 0 | 1.0000 |
| 3 | 1e-8 | 1.0000 |
| 300 | 1e-6 | 1.0000 |
| 3e6 | 1e-2 | 1.0001 |
| 3e7 | 0.1 | 1.0050 |
| 1.5e8 | 0.5 | 1.1547 |
| 2.997e8 | 0.999 | 22.3663 |
| 2.9997e8 | 0.9999 | 70.7124 |
| 3e8 | 1 | Infinite! Impossible! |

For most purposes, $\gamma \approx 1$, so we can often use the approximate formula for the momentum vector,

$$
\overset{\rightarrow}{p} = m\overset{\rightarrow}{v}
$$

## Examples

- [Calculating the momentum of a fast-moving object ($v \sim c$)](/examples/momentumfast/)
- [Calculating the momentum of a slow-moving object ($v \ll c$)](/examples/momentumslow/)
