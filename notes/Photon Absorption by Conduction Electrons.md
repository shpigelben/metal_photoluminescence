---
degree: MSc
research: photoluminescence
type: note
---


To the best of my understanding, absorption (or emission) of photons by free electrons cannot take place because energy an momentum cannot be conserved simultaneously.

Electrons in a lattice, electrons are subject o 

Bloch electrons, on the other hand, are subject to more lenient momentum conservation demands and are, theoretically, able to absorb photons.

The transition rate between two electronic states $\ket{\mathbf{k}_{1}}$ and $\ket{\mathbf{k}_{2}}$ by the absorption or emission of a photon of energy $\hbar\omega$ is generally given by Fermi's Golden Rule

$$
\begin{align}
\Gamma_{\mathbf{k}_{1}\to\mathbf{k}_{2}} (\hbar\omega) &= \frac{2\pi}{\hbar} |\braket{ \mathbf{k}_{1} | \mathcal{H'} | \mathbf{k}_{2} } |^{2}  \delta \Big( \mathcal{E}\small (\mathbf{k}_{1}) - \mathcal{E}\small (\mathbf{k}_{2}) \pm \hbar\omega\ \Big) \\
&= \frac{2\pi}{\hbar}|\mu(\mathbf{k}_{1},\mathbf{k}_{2})|^{2} \delta(\mathbf{k}_{1}-\mathbf{k}_{2}\pm \cancelto{0}{ \mathbf{q} } ) \delta \Big( \mathcal{E}\small (\mathbf{k}_{1}) - \mathcal{E}\small (\mathbf{k}_{2}) \pm \hbar\omega\ \Big)
\end{align}
$$

The absorption/emission of a photon is most generally given in the context of semi-conductor optics by the following equation

$$
I = \iint\limits f(\mathcal{E}{\small (\mathbf{k}_{1}) })\Big[ 1- f(\mathcal{E}{\small (\mathbf{k}_{2}) })\Big] \delta \Big( \mathcal{E}\small (\mathbf{k}_{1}) - \mathcal{E}\small (\mathbf{k}_{2}) - \hbar\omega\ \Big) \ d\mathbf{k}_{1} d\mathbf{k}_{2} $$

# Stack-exchange Question

## Interaction of Conduction Electrons with Light
I've been taught that the reflection of light from metals, in the classical view, is due to the response of free conduction electrons to incident radiation. Electrons oscillate out of phase with incoming electromagnetic wave and radiate according to classical electrodynamics. Some of the radiated light would then interfere constructively in the direction of specular reflection, and some would get absorbed.

If I misrepresent this classical view of the phenomenon I would gladly hear it.

On a quantum mechanical level, we describe the interaction of electrons (now described by wave functions) with photons (modes of the quantized electromagnetic field). These electrons sit in allowed energy states known as energy bands.
==Because of statistical mechanics electrons settle at lower energy bands, and because of the Pauli exclusion principle more electrons settle "on top of each other" filling higher and higher energy states. The surface in energy-momentum space that represents the highest occupied states is known as the Fermi surface. The extent of the Fermi surface depends on the number of constituent electrons and its shape depends on the underlying atomic structure of the lattice. Intersection of the Fermi surface with an energy band results in a band that is half full. Such solids are known as metals and they are unique in the sense that their electrons are free. Fermi surface in between bands, results in a lower band that is full and an upper band that is empty.== 
___
## My Understanding
I've been taught that the reflection of light from metals, in the classical view, is due to the response of free conduction electrons to incident radiation. Electrons oscillate out of phase with incoming electromagnetic wave and radiate according to classical electrodynamics. Some of the radiated light would then interfere constructively in the direction of specular reflection, and some would get absorbed.

On a quantum mechanical level, we describe the interaction of electrons (now described by wave functions) with photons (modes of the quantized electromagnetic field). These electrons sit in allowed energy states known as energy bands. An incident photon can excite an electron from a lower occupied state to a higher unoccupied state (as long as the transition conserves energy and momentum). A photon with a certain energy has negligible momentum relative to the electron and excites an electron to a higher energy state, but with effectively the same momentum (a process known as a direct transition). Direct transitions therefore only take place between different bands - an **interband** transition. Higher order processes, that include phonons for instance, can result in an **intraband** transition, where the electron shifts to a higher energy state inside the same band.

![](../../../9.%20Misc/attachments/Pasted%20image%2020250129170236.png)

## My Question

When a photon interacts with conduction electrons in metals which of the processes, interband or intraband, is the dominant or perhaps even responsible for the unique optical properties of metals (and presumably better corresponds to the aforementioned classical behavior)? Are there other mechanisms that I fail to consider?
