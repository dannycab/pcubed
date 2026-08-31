---
title: "Proof of the Point Particle Energy Principle"
weight: 4
---

You can start this derivation from the momentum principle for a multi-particle system,

$$
\frac{d{\overset{\rightarrow}{p}}_{sys}}{dt} = {\overset{\rightarrow}{F}}_{ext}
$$

As you might remember, the momentum of the system is directly related to the total mass of the system ($m$) and the velocity of the center of mass (${\overset{\rightarrow}{v}}_{cm}$),

$$
{\overset{\rightarrow}{p}}_{sys} = m{\overset{\rightarrow}{v}}_{cm}
$$

Because this is the center of mass velocity, we then choose to integrate the momentum principle from some initial to some final state ($i \rightarrow f$) over the displacement of the center of mass,

$$
\int_{i}^{f}\frac{d{\overset{\rightarrow}{p}}_{sys}}{dt} \cdot d{\overset{\rightarrow}{r}}_{cm} = \int_{i}^{f}{\overset{\rightarrow}{F}}_{ext} \cdot d{\overset{\rightarrow}{r}}_{cm}
$$

The right-hand side already looks like the work done by the external force over the displacement of the center of mass. The left-hand side can be rewritten with a little vector manipulation as the integral of the center of mass velocity,

$$
\int_{i}^{f}m\frac{d{\overset{\rightarrow}{v}}_{cm}}{dt} \cdot d{\overset{\rightarrow}{r}}_{cm} = \int_{i}^{f}{\overset{\rightarrow}{F}}_{ext} \cdot d{\overset{\rightarrow}{r}}_{cm}
$$

$$
\int_{i}^{f}m\,{\overset{\rightarrow}{v}}_{cm} \cdot d{\overset{\rightarrow}{v}}_{cm} = \int_{i}^{f}{\overset{\rightarrow}{F}}_{ext} \cdot d{\overset{\rightarrow}{r}}_{cm}
$$

$$
\int_{i}^{f}m\frac{d{\overset{\rightarrow}{v}}_{cm}}{dt} \cdot d{\overset{\rightarrow}{r}}_{cm} = \int_{i}^{f}{\overset{\rightarrow}{F}}_{ext} \cdot d{\overset{\rightarrow}{r}}_{cm}
$$

$$
\int_{i}^{f}m\, d{\overset{\rightarrow}{v}}_{cm} \cdot \frac{d{\overset{\rightarrow}{r}}_{cm}}{dt} = \int_{i}^{f}{\overset{\rightarrow}{F}}_{ext} \cdot d{\overset{\rightarrow}{r}}_{cm}
$$

$$
\int_{i}^{f}m\,{\overset{\rightarrow}{v}}_{cm} \cdot d{\overset{\rightarrow}{v}}_{cm} = \int_{i}^{f}{\overset{\rightarrow}{F}}_{ext} \cdot d{\overset{\rightarrow}{r}}_{cm}
$$

$$
\int_{i}^{f}m\, v_{cm}dv_{cm} = \int_{i}^{f}{\overset{\rightarrow}{F}}_{ext} \cdot d{\overset{\rightarrow}{r}}_{cm}
$$

This involved moving a differential around, which some mathematicians would object to, but the more formal proof would still result in the same final expression. This integral can be done from the initial to final state (*state* here refers to both the position and velocity of the center of mass). The result is that the change in translational kinetic energy is the work done in the point particle system (i.e., the work done by the net force over the displacement of the center of mass).

$$
\frac{1}{2}m\, v_{cm,f}^{2} - \frac{1}{2}m\, v_{cm,i}^{2} = \int_{i}^{f}{\overset{\rightarrow}{F}}_{ext} \cdot d{\overset{\rightarrow}{r}}_{cm}
$$

$$
\Delta K_{trans} = W_{cm}
$$

This [derivation and an extended discussion of the point particle system](http://scitation.aip.org/content/aapt/journal/ajp/51/7/10.1119/1.13173) was written by Bruce Sherwood in the American Journal of Physics.
