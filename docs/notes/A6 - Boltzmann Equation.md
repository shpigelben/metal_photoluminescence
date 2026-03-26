---
type: note
section: appendix
---
==A semi-classical theory treats one part of a system quantum-mechanically and the other classically.== In the context of Boltzmann equation, a semi-classical Boltzmann equation treats the particles between collisions classically and the collisions are treated quantum-mechanically.
# Classical Boltzmann Equation
A PDE whose solution is a single-particle-distribution (SPD). The LHS resembles [Liouville equation](2.%20Notes/Liouville%20Equation.md) for an SPD and the RHS has a collision term that accounts for the interaction with the rest of the particles.

$$
\frac{ \partial f }{ \partial t } + \Big\{ f, \mathcal{H}_{\text{ext}} \Big\} = \left( \frac{ \partial f }{ \partial t }  \right)_{\text{coll}}
$$

The hamiltonian on the RHS describes the dynamics of the free particle under external influences, and the RHS collision term contains the interaction hamiltonians.
$$
\frac{df}{dt} = \frac{ \partial f }{ \partial t } + \mathbf{v}\cdot\boldsymbol{\nabla_{r}}f + \mathbf{r}\cdot\boldsymbol{\nabla_{v}}f = \left( \frac{ \partial f }{ \partial t }  \right)_{\text{coll}} 
$$
# Quantum Boltzmann Equation
$$
\frac{ \partial f }{ \partial t } + \frac{i}{\hbar}\Big[ f, \mathcal{H}_{\text{ext}} \Big] = \left( \frac{ \partial f }{ \partial t }  \right)_{\text{coll}}
$$
## QBE for Electron Dynamics
$$
\left( \frac{ \partial f }{ \partial t } \right)_{\text{coll}} = \sum\limits_{\text{coll type}} \left( \sum\limits_{j} f_{i}f_{j}W_{i\to j}  \right)
$$
Where $f_{i}$ is the SPD of the first state and $f_{j}$ is the SPD of the final state summed over all possible final states. $W_{i\to j}$ is the transition rate given by [Fermi golden rule](2.%20Notes/Fermi%20Golden%20Rule.md).
# Relaxation Time Approximation

# Photon Absorption

$$
\begin{align}
\cancelto{\text{steady state}}{ \frac{ \partial f }{ \partial t } } &= \left( \frac{ \partial f }{ \partial t }  \right)_{\text{ex}} + \left( \frac{ \partial f }{ \partial t }  \right)_{\text{e-e}} +  \cancelto{\text{far from }\mathcal{E}_{F}}{ \left( \frac{ \partial f }{ \partial t }  \right)_{\text{e-ph}} }\\ \\  &\Rightarrow\left( \frac{ \partial f }{ \partial t }  \right)_{\text{ex}} = - \left( \frac{ \partial f }{ \partial t }  \right)_{\text{e-e}}  \tag{1}
\end{align}
$$

Technically, there should also be a term for the recombination (and emission) of electrons, but it is very negligible in metals (according to Yonatan - need to check why).

An involved calculation leads to the excitation (absorption) term

$$
 \left( \frac{ \partial f }{ \partial t }  \right)_{\text{ex}} = R(\omega _{\scriptsize L})|E_{\scriptsize L}|^{2} \cdot B(\mathcal{E};\omega _{\scriptsize L}) \tag{2}
 $$
 
with $E_{\scriptsize L}$ as the electric field strength of the pump and $R$ is a function of the pump photon's frequency (see explicit expressions for R and B below). Relaxation time approximation gives

$$
 \left( \frac{ \partial f }{ \partial t }  \right)_{\text{e-e}} \approx \frac{f^{T}-f}{\tau_{e-e}} \equiv - \frac{\Delta f}{\tau_{e-e}}\tag{3}
$$

Plugging (3) and (2) into (1) results in

$$
\begin{align}
\Delta f &= \tau_{e-e}R(\omega _{\scriptsize L}) |E_{\scriptsize L}|^{2} \cdot B(\mathcal{E},\omega _{\scriptsize L}) \\ \\
&\equiv\delta_{E}\cdot B(\mathcal{E};\omega _{\scriptsize L}) \tag{4}
\end{align}
$$

(see the definition of $\delta_{E}$ below)
Finally, the non-equilibrium distribution is
$$
f(\mathcal{E};\omega _{\scriptsize L}) = f^{\scriptsize T}(\mathcal{E}) + \underbrace{ \delta E(\omega _{\scriptsize L})\cdot B(\mathcal{E},\omega _{\scriptsize L}) }_{ f^{\scriptsize NT}(\mathcal{E};\omega _{\scriptsize L}) } \tag{4*}
$$
> [!NOTE]- Definitions of B, $\boldsymbol{\delta_{E}}$ and R
> $$\begin{align} B(\mathcal{E};\omega _{\scriptsize L}) &= f(\mathcal{E}-\hbar\omega _{\scriptsize L})\Big[ 1-f(\mathcal{E}) \Big] - f(\mathcal{E})\Big[ 1-f(\mathcal{E}+\hbar\omega _{\scriptsize L}) \Big] \\ \\ \delta E &\equiv \left| \frac{E_{\scriptsize L}}{E_{\text{sat}}} \right|^{2} = |\tau_{e-e}R(\omega _{\scriptsize L})E_{\scriptsize L}|^{2} \\ \\
R(\omega _{\scriptsize L}) &= \frac{4\epsilon_{0}\epsilon_{m}''(\omega _{\scriptsize L})}{3\hbar n_{e}} \frac{\mathcal{E}_{\scriptsize F}}{\hbar \omega _{\scriptsize L}}\end{align}$$ 
> Need to read about the source of these expressions

