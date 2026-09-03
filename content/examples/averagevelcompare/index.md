---
title: 'Example: Comparing two ways of calculating the average velocity'
weight: 20
---

You have learned about [two ways of computing the average velocity](/notes/week-01-modeling-motion-no-net-force/displacement_and_velocity/). The *arithmetic* average is an approximation and it can be a poor one. Consider the driving from East Lansing to Chicago (222 miles or 358 km). To get to Chicago, you drive at 55.0 mph (24.6 $\frac{m}{s}$) for 1 hour and 66.8 mph (29.9 $\frac{m}{s}$) for 2.5 hours. Compare the average velocity to the *arithmetic* average velocity.

## Setup

You will compare the two ways of computing the average velocity using the information provided and any information that you can collect or assume.

### Facts

- The distance from East Lansing to Chicago is 3.58$\times 10^{5}m$.
- For the first hour (3600 s), you drive at 24.6 $\frac{m}{s}$.
- For the next 2.5 hours (9000 s), you drive at 29.9 $\frac{m}{s}$.

### Lacking

- Information about stops for gas, breaks, etc. are not known.

### Approximations & Assumptions

- You drive straight through with no breaks.
- You use cruise control and do not deviate from the above speeds.
- The problem can be considered to be in “one dimension” (along the road to Chicago).

### Representations

- The average velocity is given by $v_{avg,x} = \frac{\Delta x}{\Delta t}$.
- The *arithmetic* average velocity is an approximation to the average velocity and is given by $v_{avg,x} \approx \frac{v_{i} + v_{f}}{2}$.

## Solution

For this situation, the average velocity can be computed,

$$
v_{avg,x} = \frac{\Delta x}{\Delta t} = \frac{3.58 \times 10^{5}m}{3600s + 9000s} = 28.4\frac{m}{s}
$$

You can compare that to the *arithmetic* average velocity,

$$
v_{avg,x} \approx \frac{v_{i} + v_{f}}{2} = \frac{24.6\frac{m}{s} + 29.9\frac{m}{s}}{2} = 27.3\frac{m}{s}
$$

You can see that the *arithmetic* average is (in this case) less than the average velocity. It also under-predicts how far you would have driven,

$$
\Delta x = v_{avg,x}\Delta t = 27.3\frac{m}{s}(3600s + 9000s) = 3.43 \times 10^{5}m = 343km
$$

which is leaves you at the “outskirts” of Chicago (about 15 $km$ away).
