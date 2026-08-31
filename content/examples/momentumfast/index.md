---
title: 'Example: Calculating the momentum of a fast-moving object'
weight: 13
---

An electron is observed to be moving with a velocity of $\langle - 2.05 \times 10^{7},6.02 \times 10^{7},0\rangle\frac{m}{s}$. Determine the momentum of this electron.

## Setup

You need to compute the momentum of this electron using the information provided and any information that you can collect or assume.

### Facts

- An electron is in motion
- It has a velocity, ${\overset{\rightarrow}{v}}_{e} = \langle - 2.05 \times 10^{7},6.02 \times 10^{7},0\rangle\frac{m}{s}$.
- The speed of the electron is near the speed of light ($c = 3.00 \times 10^{8}\frac{m}{s}$).

### Lacking

- The mass of the electron is not given, but can be [found online](https://en.wikipedia.org/wiki/Electron_mass) ($m_{e} = 9.11 \times 10^{- 31}kg$).

### Approximations & Assumptions

- The electron does not experience any interactions, so its velocity will remain unchanged.

### Representations

- The momentum of the electron is given by $\overset{\rightarrow}{p} = \gamma m\overset{\rightarrow}{v}$ where $\gamma = \frac{1}{\sqrt{1 - \left( \frac{|\overset{\rightarrow}{v}|}{c} \right)^{2}}}$.

## Solution

First, we compute the speed of the electron.

$$
|{\overset{\rightarrow}{v}}_{e}| = \sqrt{v_{x}^{2} + v_{y}^{2} + v_{z}^{2}} = \sqrt{( - 2.05 \times 10^{7}\frac{m}{s})^{2} + (6.02 \times 10^{7}\frac{m}{s})^{2} + (0)^{2}} = 6.36 \times 10^{7}\frac{m}{s}
$$

Next, we compute the gamma factor.

$$
\gamma = \frac{1}{\sqrt{1 - \left( \frac{|\overset{\rightarrow}{v}|}{c} \right)^{2}}} = \frac{1}{\sqrt{1 - \left( \frac{6.36 \times 10^{7}\frac{m}{s}}{3.00 \times 10^{8}\frac{m}{s}} \right)^{2}}} = \frac{1}{\sqrt{1 - (0.212)^{2}}} = 1.02
$$

Finally, we compute the momentum vector.

$$
{\overset{\rightarrow}{p}}_{e} = \gamma m_{e}{\overset{\rightarrow}{v}}_{e} = (1.02)(9.11 \times 10^{- 31}kg)\langle - 2.05 \times 10^{7},6.02 \times 10^{7},0\rangle\frac{m}{s} = \langle - 1.91 \times 10^{- 23},5.61 \times 10^{- 23},0\rangle\frac{kg\ m}{s}
$$
