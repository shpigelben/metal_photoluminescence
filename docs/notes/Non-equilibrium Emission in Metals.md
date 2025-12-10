---
degree: MSc
research: photoluminescence
type: note
---
w
- [ ] Is photoluminescence a general term? In equilibrium is it simply the usual blackbody radiation? Is it simply a general term for emission? **according to GPT - blackbody radiation is not a form of PL**.

- intraband transitions
	- equilibrium (energy vs momentum)
	- non-equilibrium (energy vs momentum)
- interband transitions (By this point, calculations in momentum space should be established as reliable).
	- equilibrium (momentum)
	- non-equilibrium (momentum)
- A1 - derivation of the emission integral
- A2 - gaussian approximation of the delta
- A3 - derivation of the non-equilibrium distribution
- A4 - Analytic approximation

![800](../../../9.%20Misc/Excalidraw/EMISSION%20TYPE%20COMPARISON.md)

****
$$
\begin{align} \frac{4\pi V^{2}}{\epsilon_{0}} \ \omega\rho _{\scriptsize \gamma}{\small (\omega) }
\int\limits_{\text{BZ}}\int\limits_{\text{BZ}} \Big|\mu {\small (\mathbf{k}_{1},\mathbf{k}_{2}) } \Big|^{2} f{ (\mathcal{E}_{\scriptsize \text{a}}{\small (\mathbf{k}_{2}) })\Big[ 1-f{ (\mathcal{E}_{\scriptsize \text{b}}{\small (\mathbf{k}_{2}) }) } \ \Big] }\ \delta\Big(\mathcal{E}_{\scriptsize \text{a}}{\small (\mathbf{k}_{1}) }-\mathcal{E}_{\scriptsize \text{b}}{\small (\mathbf{k}_{2}) }+\hbar\omega\Big)\ d^{3}k_{1} \ d^{3}k_{2}
\end{align}
$$

$$
\begin{align} \underbrace{ \frac{4\pi V^{2}}{\epsilon_{0}} \ \omega\rho _{\scriptsize \gamma}{\small (\omega) } }_{ I_{\gamma} } \ \underbrace{ \Big|\mu\Big|^{2}
\int\limits_{\text{BZ}}\int\limits_{\text{BZ}}  f{ (\mathcal{E}_{\scriptsize \text{a}}{\small (\mathbf{k}_{2}) })\Big[ 1-f{ (\mathcal{E}_{\scriptsize \text{b}}{\small (\mathbf{k}_{2}) }) } \ \Big] }\ \delta\Big(\mathcal{E}_{\scriptsize \text{a}}{\small (\mathbf{k}_{1}) }-\mathcal{E}_{\scriptsize \text{b}}{\small (\mathbf{k}_{2}) }+\hbar\omega\Big)\ d^{3}k_{1} \ d^{3}k_{2} }_{ I_{e} }
\end{align}
$$
___
# 1 - Emission due to Intraband Transitions

$$
\begin{align}
&f_{\scriptsize \text{FD}}(\mathbf{k})\equiv f^{\scriptsize T}(\mathbf{k}) = \frac{1}{\exp\Big(\frac{\mathcal{E}{\small (\mathbf{k}) }-\mu}{k_{\scriptsize B}T} \Big) + 1} \\ \\
&f_{\scriptsize \text{BE}}(\mathcal{E}) = \frac{1}{\exp\Big(\frac{\mathcal{E-\mu}}{k_{\scriptsize B}T} \Big) - 1} \ \ \underbrace{\ \longrightarrow \ }_{ \text{photons }\mu=0 } \ \frac{1}{\exp\Big(\frac{\mathcal{E}}{k_{\scriptsize B}T} \Big) - 1} 
\end{align}
$$
for photon gas $\mu=0$.
## 1.1 - Equilibrium Emission Integral

- Since transitions occur within the same band, there is no distinction between the dispersion relations $\mathcal{E}_{a}=\mathcal{E_{b}}\equiv \mathcal{E}$.
- The transition dipole moment is approximately constant (why?).

under these two conditions the general emission expression is proportional to the following

$$
\begin{align}
\Gamma(\hbar\omega) \propto \int\limits_{\text{BZ}}\int\limits_{\text{BZ}} f^{\scriptsize T}{ (\mathbf{k}_{1})\Big[ 1-f^{\scriptsize T}{ (\mathbf{k}_{2}) } \ \Big] }\ \delta\Big(\mathcal{E}{\small (\mathbf{k}_{1}) }-\mathcal{E}{\small (\mathbf{k}_{2}) }+\hbar\omega\Big)\ d^{3}k_{1} \ d^{3}k_{2}
\end{align}
$$

The dispersion relation is isotropic (free electron approximation in the conduction band) and the number of integration variable therefore reduces from 6 to 2.

$$
\begin{align}
\Gamma(\hbar\omega) \propto &\int\limits_{\text{BZ}}\int\limits_{\text{BZ}} f^{\scriptsize T}{ (\mathcal{E}{\small (k_{1}) })\Big[ 1-f^{\scriptsize T}{ (\mathcal{E}{\small (k_{2}) }) } \ \Big] } \ \cdot \\ & \cdot \delta\Big(\mathcal{E}{\small (k_{1}) }-\mathcal{E}{\small (k_{2}) }+\hbar\omega\Big)\ (4\pi {k_{1}}^{2})(4\pi {k_{2}}^{2}) dk_{1} \ dk_{2}
\end{align}
$$

In this form, the $\delta$ cannot be resolved. But under the consideration that $k_{1}\approx k_{2}$ (a direct transition) we can loosely resolve it in the following fashion
$$
\Gamma(\hbar\omega)\propto \int\limits_{BZ} f^{\small T}(\mathcal{E}{\small (k_{2})+\hbar\omega })\Big[ 1-f^{\scriptsize T}(\mathcal{E}{\small (k_{2}) }) \Big](16\pi^{2} {k_{2}}^{4}) \ dk_{2}
$$
This allows us to reduce the number of integration dimensions from 6 to 2 by integrating over the magnitude of the momenta.


The dispersion relation of the nearly free electron in the conduction band is approximately parabolic (isotopic). This allows us to conveniently transition from 6-dimensional integral of momenta states into a 2-dimensional integral of energy states by making a change of variables and identifying the density of states $\rho(\mathcal{E})$.

$$
\begin{align}
\Gamma(\hbar\omega)&  \propto\int\limits_{0}^{\infty}\int\limits_{0}^{\infty} f{ (\mathcal{E_{1}})\rho(\mathcal{E_{1}})\Big[ 1-f{ (\mathcal{E_{2}}) } \ \Big] }\rho(\mathcal{E_{2}})\ \delta(\mathcal{E_{1}}-\mathcal{E_{2}}+\hbar\omega)\ d\mathcal{E_{1}} \ d\mathcal{E_{2}}\\ \tag{1.1.3}
&=\int\limits_{0}^{\infty} f{ (\mathcal{E}_{2}+\hbar\omega)\rho(\mathcal{E}_{2}+\hbar\omega)\Big[ 1-f{ (\mathcal{E}_{2}) } \Big] }\rho(\mathcal{E}_{2}) \ d\mathcal{E_{2}} \\
&\approx \rho^{2}(\mathcal{E}_{\scriptsize F}) \int\limits_{0}^{\infty} f{ (\mathcal{E}_{2}+\hbar\omega)\Big[ 1-f{ (\mathcal{E}_{2}) } \Big] } \ d\mathcal{E}_{2} \tag{1.1.4}
\end{align}
$$
where the first transition is a reduction through the delta function, and in the second transition we make the simplifying assumption that the density of states can be approximated as constant at the fermi energy.

==comparison between $(1.1.2)$ with variable eDOS and $(1.1.3)$ with constant eDOS at the Fermi energy==

## 1.2 - Equilibrium Analytic Solution
It can be shown that the following holds
$$
f_{\scriptsize FD}(\mathcal{E}+\hbar\omega)\Big[ 1-f_{\scriptsize FD}(\mathcal{E}) \Big] = f_{\scriptsize BE}(\hbar\omega)\Big[ f_{\scriptsize FD}(\mathcal{E})-f_{\scriptsize FD}(\mathcal{E}+\hbar\omega) \Big] \tag{1.2.1}
$$
plugging $(1.2.1)$ into $(1.1.3)$ yields
$$
\begin{align}
\Gamma(\hbar\omega)&= \rho^{2}(\mathcal{E}_{\scriptsize F}) \ f_{\scriptsize BE}(\hbar\omega)\int\limits_{0}^{\infty}  \, \Big[ f_{\scriptsize FD}(\mathcal{E})-f_{\scriptsize FD}(\mathcal{E}+\hbar\omega) \Big] d\mathcal{E} \\
&=\rho^{2}(\mathcal{E}_{\scriptsize F}) \ f_{\scriptsize BE}(\hbar\omega) \ \underbrace{ \frac{1}{\beta} \bigg( \ln\left(1+e^{\beta\mu}\right) - \ln\left(1+e^{\beta(\mu-\hbar\omega)}\right) \bigg) }_{ \approx \hbar\omega }  \tag{1.2.2}
\end{align}
$$

the approximation made in $(1.2.2)$  is based on the fact that $\mu, \ \mu-\hbar\omega \gg k_{\scriptsize B}T$

$$
\Gamma_{\text{analytic}}(\hbar\omega) = \rho^{2}(\mathcal{E}_{\scriptsize F}) \ \frac{\hbar\omega}{\exp\left( \frac{\hbar\omega }{k_{\scriptsize B}T} \right)+1} \tag{1.2.3}
$$
## 1.3 - Numeric - Analytic Comparison
The following is a comparison between the numeric integration of $(1.1.3)$ and the analytic approximation $(1.2.3)$

![fig 1 : a comaprison between the numeric integration of (1.1.3) and the analytic approximation in (1.2.3)|center|400](../../../9.%20Misc/attachments/Pasted%20image%2020241027201518.png)

When $\hbar\omega \approx \mu \approx \mathcal{E}_{\scriptsize F}$ the approximation is no longer a good one. This can be validated by the deviation from the numeric integration which increases with $\hbar\omega$.

# 2. Non-equilibrium Emission Due to Intraband Transitions


# 3. Equilibrium Emission Due to Interband Transitions

## 2.1 Equilibrium Emission Integral
## 2.2 Equilibrium Analytic Solution
## 2.3 Numeric - Analytic Comparison


## Energy Space
### Equilibrium (no eDOS)
$$
\begin{align}
I_{e}^{T}(\omega)_{\text{numeric}} &= \int\limits f^{T}(\mathcal{E+\hbar\omega})\Big[ 1-f^{T}(\mathcal{E}) \Big]d\mathcal{E} &&[eV] \\
I_{e}^{T}(\omega)_{\text{analytic}} &= \frac{\hbar\omega}{e^{\beta \hbar\omega}-1}&&[eV]
\end{align}
$$

### Equilibrium (with eDOS)
$$
\begin{align}
I_{e}^{T}(\omega)_{\text{numeric}} &= \int\limits f^{T}(\mathcal{E+\hbar\omega})\Big[ 1-f^{T}(\mathcal{E}) \Big]g(\mathcal{E})d\mathcal{E} &&\left[ \frac{1}{m^{3}} \right] \\
I_{e}^{T}(\omega)_{\text{analytic}} &= g(\mathcal{E}_{\scriptsize F})\frac{\hbar\omega}{e^{\beta \hbar\omega}-1} &&\left[ \frac{1}{m^{3}} \right]
\end{align}
$$


### non-Equilibrium (no eDOS)
$$
\begin{align}
I_{e}(\omega)_{\text{numeric}} &= \int\limits f(\mathcal{E+\hbar\omega})\Big[ 1-f(\mathcal{E}) \Big]d\mathcal{E} &&[eV] \\
I_{e}(\omega)_{\text{analytic}} &= \frac{\hbar\omega}{e^{\beta \hbar\omega}-1} + A\cdot \delta _{\scriptsize E} + B\cdot\delta _{\scriptsize E}^2 &&[eV]
\end{align}
$$

mean relative value = 0.2211

### non-Equilibrium (with eDOS)
$$
\begin{align}
I_{e}(\omega)_{\text{numeric}} &= \int\limits f(\mathcal{E+\hbar\omega})\Big[ 1-f(\mathcal{E}) \Big]g(\mathcal{E})d\mathcal{E} &&\left[ \frac{1}{m^{3}} \right] \\
I_{e}(\omega)_{\text{analytic}} &= \left[ \frac{\hbar\omega}{e^{\beta \hbar\omega}-1} + A\cdot \delta _{\scriptsize E} + B\cdot\delta _{\scriptsize E}^2 \right]g(\mathcal{E}_{\scriptsize F}) &&\left[ \frac{1}{m^{3}} \right]
\end{align}
$$

mean relative error = 0.3487
## Momentum (wave-vector) Space

### Equilibrium
$$
\begin{align}
I_{e}(\omega)_{\text{numeric}} &= \int\limits f^{T}(\mathcal{E}{\small (k)}+\hbar\omega)\Big[ 1-f^{T}(\mathcal{E}{\small (k)}) \Big] \ 4\pi k^{2} dk &&\left[ \frac{1}{m^{3}} \right] \\
I_{e}(\omega)_{\text{analytic}} &= \left[ \frac{\hbar\omega}{e^{\beta \hbar\omega}-1} + A\cdot \delta _{\scriptsize E} + B\cdot\delta _{\scriptsize E}^2 \right]g(\mathcal{E}_{\scriptsize F}) &&\left[ \frac{1}{m^{3}} \right]
\end{align}
$$

### non-Equilibrium
$$
\begin{align}
I_{e}(\omega)_{\text{numeric}} &= \int\limits f(\mathcal{E}{\small (k)}+\hbar\omega)\Big[ 1-f(\mathcal{E}{\small (k)}) \Big] \ 4\pi k^{2} dk &&\left[ \frac{1}{m^{3}} \right] \\
I_{e}^{T}(\omega)_{\text{analytic}} &= g(\mathcal{E}_{\scriptsize F})\frac{\hbar\omega}{e^{\beta \hbar\omega}-1} &&\left[ \frac{1}{m^{3}} \right]
\end{align}
$$

## one more comparison (to be made)
constant eDOS vs energy-dependent eDOS
$$
\begin{align}
I_{e}(\omega)_{\text{numeric}} &= \int\limits f(\mathcal{E+\hbar\omega})\Big[ 1-f(\mathcal{E}) \Big]g(\mathcal{E})d\mathcal{E} &&\left[ \frac{1}{m^{3}} \right] \\
I_{e}(\omega)_{\text{numeric}} &= \int\limits f(\mathcal{E+\hbar\omega})\Big[ 1-f(\mathcal{E}) \Big]g(\mathcal{E}_{\scriptsize F})d\mathcal{E} &&\left[ \frac{1}{m^{3}} \right] 
\end{align}
$$


## Insights
1. The non-equilibrium distribution as given in `Theory of“Hot” Photoluminescence from Drude Metals` is incorrect and shows occupations of electrons greater than one. A more correct expression is given in `Assistance of metal nanoparticles in photocatalysis– nothing more than a classical heat source`.
2. A typo (or misuse)  of $\rho_{J}$ in both `Theory of“Hot” Photoluminescence from Drude Metals` and `Supporting Information: Theory of “Hot” Photoluminescence from Drude Metals`.
3. Discrepancy (for high energy ranges) between numeric and analytic solutions is likely to stem from the utilization of the wrong distribution (as pointed out in 1.) in the calculation of the analytic expression.
___

# 1.1 Equilibrium (Fermi-Dirac) Distribution (Intranband)
$$
\begin{align}
  f^{T}\Big(\mathcal{E}(k),\omega\Big) &= \large \frac{1}{\exp\Big( \frac{\mathcal{E}{ (k) } - \mu}{k_{\small B}T} \Big) + 1} \tag{1.1}\\ \\
\mathcal{E}(k)  &= \frac{\hbar^{2}k^{2}}{2m_{e}} \\ \\  \mu &= \mathcal{E}_{\scriptsize F}\left[1- \frac{\pi^{2}}{12}\left( \frac{T}{T_{\scriptsize F}} \right)^{2}\right]
\end{align}
$$

# Counting States in Phase Space

$$
\begin{aligned}
N &= \sum\limits_{\mathbf{x}, \ \mathbf{k}} \ f(\mathbf{x,\mathbf{k}})\\
 &\Rightarrow \iint\limits \frac{d^{3}x \ d^{3}k}{(2\pi)^{3}} \ f(\mathbf{x},\mathbf{k})
\end{aligned}
$$
where counting electron states $f$ is the Fermi-Dirac (FD) distribution and each count is multiplied by the spin degeneracy factor (2). Usually the FD distribution is homogenous $f(\mathbf{x},\mathbf{k})\to f(\mathbf{k})$ and the above gets the more familiar form
$$
N = 2V \int\limits \frac{d^{3}k}{(2\pi)^{2}}f(\mathbf{k})
$$
Computing a macroscopic property of the electronic system utilizes the above and has the general form
$$
\braket{ H } = 2V \int\limits H(\mathbf{k}) \ f(\mathbf{k})\ \frac{d^{3}k}{(2\pi)^{3}}
$$
where H can be energy, or any other k-dependent property of the system.
# Emission Derivation (Energy Space)
The transition rate of an electron from a **single** higher energy state $\ket{\mathcal{E_{i}}}$ to a **single** lower energy state $\ket{\mathcal{E_{f}}}$, accompanied by an emission of a photon with appropriate energy $\hbar\omega$, is given by [Fermi's golden rule](2.%20Notes/Fermi%20Golden%20Rule.md).

$$
\begin{align}
\Gamma_{i\to f}({\small\hbar\omega}) &= \frac{2\pi}{\hbar}|\braket{ \mathcal{E_{i}} |H' | \mathcal{E_{f}} } |^{2} \ \delta({\small \mathcal{E_{f}}-\mathcal{E_{i}}+\hbar\omega}) \\
&= \frac{2\pi}{\hbar}|\mu({\small\mathcal{E_{i}},\mathcal{E_{f}}}) |^{2} \ \delta({\small \mathcal{E_{f}}-\mathcal{E_{i}}+\hbar\omega}) \tag{1}
\end{align} 
$$

The transition rate from a single state $\ket{\mathcal{E}_{i}}$ to all possible final states is gained by integrating over all possible final energy states, weighed by the probability of **vacancy** at each state.

$$
\begin{align}
\Gamma_{i}({\small\hbar\omega}) &= \sum\limits_{\mathcal{E_{f}}} \ \Gamma_{i\to f}{\small (\hbar\omega) } \ \big[ 1-f{\small (\mathcal{E}_{f}) } \big]\\
&\Rightarrow V\int \Gamma_{i\to f}{\small (\hbar\omega) } \ \big[ 1-f{\small (\mathcal{E}_{f}) } \big] \  \rho{\small (\mathcal{E_{f}}) } \ d\mathcal{E_{f}} \tag{2}
\end{align}
$$
And the transition rate from all possible initial states to all possible final states is gain by again integrating over all possible initial energy states, weighed by the probability of **occupancy** at each state.
$$
\begin{align}
\Gamma(\hbar\omega) &= \sum\limits_{\mathcal{E_{i}}}  \ \Gamma_{i}{\small (\hbar\omega) } \ f{\small (\mathcal{E_{i}}) }\\
&\Rightarrow V \int\limits\Gamma_{i}{\small (\hbar\omega) } \ f{\small (\mathcal{E_{i}}) } \ \rho {\small (\mathcal{E_{i}}) } \ d\mathcal{E_{i}} \tag{3}
\end{align}
$$
This accounts for all the possible transitions that result in the emission of a photon with energy $\hbar \omega$, namely this is the emission spectra due to this process. Writing $(3)$ explicitly looks like

$$
\begin{align}
\Gamma(\hbar\omega) &=\frac{2\pi V^{2}}{\hbar} \iint\limits |\mu {\small (\mathcal{E_{i},\mathcal{E_{f}}}) }|^{2}\underbrace{ f{\small (\mathcal{E_{i}})}\rho {\small (\mathcal{E_{i}}) }\big[ 1-f{\small (\mathcal{E_{f}}) } \big]\rho {\small (\mathcal{E_{f}}) }  }_{\Large \equiv \rho _{\scriptsize J}{\small (\mathcal{E_{i},\mathcal{E_{f}}}) } } \ \delta {\small (\mathcal{E_{f}-\mathcal{E_{i}}+\hbar\omega}) } \ d\mathcal{E_{i}} \ d\mathcal{E_{f}} \\ \\
&= \frac{2\pi V^{2}}{\hbar}\int |\mu {\small (\mathcal{E_{i},\mathcal{E_{i}-\hbar\omega}}) }|^{2} \ \rho_{\scriptsize J}{\small (\mathcal{E_{i},\mathcal{E_{i}-\hbar\omega}}) } \ d\mathcal{E_{i}} \tag{4}
\end{align}
$$

Where in the last term we resolved the conservation of energy due to the delta, leaving us with the more practical expression in $(4)$.

When $\mathcal{E}(\mathbf{k})$ is not isotropic in $\mathbf{k}$, calculation such as this in energy space is not readily (if at all) possible, and working in k-space might be more doable.

# Emission Derivation (Momentum Space)
We'll follow the above steps, counting all energy-conserving transitions

$$
\begin{align}
\Gamma_{i\to f}{\small (\hbar\omega) } &= \frac{2\pi}{\hbar}|\braket{ k_{\text{i}} | H'|k_{\text{f}} } |^{2} \ \delta(\mathcal{E}{\small (\mathbf{k_{f}}) - \mathcal{E}{\small (\mathbf{k_{i}})+\hbar\omega } })  \\
&= \frac{2\pi}{\hbar}|\mu_{\text{i,f}} |^{2} \ \delta(\mathcal{E}{\small (\mathbf{k_{f}}) - \mathcal{E}{\small (\mathbf{k_{i}})+\hbar\omega } }) 
\end{align}
$$



$$
\begin{align}
\Gamma_{i}{\small (\hbar\omega) } &= \overbrace{2}^{\text{ spin states}} \cdot\sum\limits_{\mathbf{k_{f}}}\Gamma_{\text{i}\to \text{f}}{\small (\hbar\omega) }\Big[ 1-f ({\small \mathcal{E}(\mathbf{k_{f}})})  \Big] \\
&= 2V\int\limits_{\text{BZ}} \frac{{d^{3}k_{\text{f}}}}{(2\pi)^{3}} \ \Gamma_{\text{i}\to \text{f}}{\small (\hbar\omega) }\Big[ 1-f ({\small \mathcal{E}(\mathbf{k_{f}})})  \Big] 
\end{align}
$$

$$
\begin{align}
\Gamma_{i}{\small (\hbar\omega) } &= 2 \cdot\sum\limits_{\mathbf{k_{f}}} \ \Gamma_{\text{i}}{\small (\hbar\omega) } \ f ({\small \mathcal{E}(\mathbf{k_{i}})}) \\
&= 2V\int\limits_{\text{BZ}} \frac{{d^{3}k_{\text{i}}}}{(2\pi)^{3}} \  \ \Gamma_{\text{i}}{\small (\hbar\omega) } \ f ({\small \mathcal{E}(\mathbf{k_{i}})}) 
\end{align}
$$

$$
\Gamma {\small (\hbar\omega) } = 4V^{2} \iint\limits_{\text{BZ}} \frac{2\pi}{\hbar}|\mu {\small (k_{\text{i}},k_{\text{f}}) }|^{2} \  f({\small \mathcal{E}{\small (\mathbf{k_{\text{i}}}) }}) \Big[ 1 - \  f({\small \mathcal{E}{\small (\mathbf{k_{\text{f}}}) }}) \Big] \ \delta(\mathcal{E}{\small (\mathbf{k_{f}}) - \mathcal{E}{\small (\mathbf{k_{i}})+\hbar\omega } }) \frac{d^{3}k_{\text{i}}}{(2\pi)^{3}} \frac{d^{3}k_{\text{f}}}{(2\pi)^{3}}
$$

$$
\Gamma {\small (\hbar\omega) } = 4V^{2} \int\limits_{\text{BZ}} \frac{2\pi}{\hbar}  \ f(\mathcal{E}{\small (\mathbf{k_{i}}) }) \left[ \int\limits_{\text{BZ}} |\mu {\small (k_{\text{i}},k_{\text{f}}) }|^{2} \Big[1-f(\mathcal{E}{\small (\mathbf{k_{f}}) })  \Big] \delta(\mathcal{E}{\small (\mathbf{k_{f}}) - \mathcal{E}{\small (\mathbf{k_{i}})+\hbar\omega } })  \frac{d^{3}k_{\text{f}}}{(2\pi)^{3}} \right]  \frac{d^{3}k_{\text{i}}}{(2\pi)^{3}}
$$
The integral in the square brackets is where I'm stuck
# 1.2 Equilibrium Emission (Intranband)
$\mathcal{E}(k)\equiv \mathcal{E}_{k}$ for brevity
$$
I^{T}_{e}(\omega) =  \int\limits_{0}^{\infty} f^{T}\big(\mathcal{E}_{k}+\hbar\omega\big) \Big[ 1-f^{T}\big(\mathcal{E}_{k}\big) \Big] 4\pi k^{2}dk \tag{1.2}
$$
# 2.1 Non-equilibrium Distribution (Intranband)
based on (A7) and (A8) from the appendix of "Assistance of metal nanoparticles in photocatalysis– nothing more than a classical heat source"
$$
f\big( { \mathcal{E}_{k} \ ; \ \omega _{\scriptsize L} }\big) = f^{T}({ \mathcal{E}_{k}}) + \delta E(\omega _{\scriptsize L})\cdot B({ \mathcal{E}_{k} \ ; \ \omega _{\scriptsize L}}) \tag{2.1.1}
$$
$$
B({ \mathcal{E}_{k} \ ; \ \omega _{\scriptsize L}}) = f^{T}({\mathcal{E}_{k} - \hbar\omega _{\scriptsize L}})\Big[ 1-f^{T}({\mathcal{E}_{k}}) \Big] - f^{T}(\mathcal{E}_{k})\Big[ 1- f^{T}(\mathcal{E}_{k}+\hbar\omega _{\scriptsize L}) \Big] \tag{2.1.2}
$$
# 2.2 Non-equilibrium Emission (Intranband)
using the non-equilibrium distribution $f$
$$
I_{e}(\omega \ ; \ \omega _{\scriptsize L}) =  \int\limits_{0}^{\infty} f\big(\mathcal{E}_{k}+\hbar\omega \ ; \ \omega _{\scriptsize L}\big) \Big[ 1-f\big(\mathcal{E}_{k} \ ; \ \omega _{\scriptsize L}\big) \Big] 4\pi k^{2}dk \tag{2.2}
$$
The above equilibrium and non-equilibrium emissions, calculated in momentum space, have been found to follow (9) from "Theory of “Hot” Photoluminescence from Drude Metals" (more so for lower frequency emissions than higher ones).
# 3.1 Equilibrium Distribution for (Interband)
electron dispersion relations in the valence and conduction bands are taken from "Ultrafast nonlinear dynamics of surface plasmon-polaritons in gold nanowires due to the intrinsic nonlinearity of metals".

$$
  f^{T}\Big(\mathcal{E}_{b}(\mathbf{k})\Big) = \large \frac{1}{\exp\Big( \frac{\mathcal{E}_{b}{ (\mathbf{k}) } - \mu}{k_{\small B}T} \Big) + 1} \tag{3.1.1}
$$

$$
\mathcal{E}_{b}(\mathbf{k})  = \begin{cases}
\mathcal{E}_{0V} - \frac{{\hbar ^{2}k_{\perp}^{2}}}{2m_{V \perp}} - \frac{{\hbar ^{2}k_{\parallel}^{2}}}{2m_{V \parallel}} && (b=V)\\ \\
\mathcal{E}_{0C} + \frac{{\hbar ^{2}k_{\perp}^{2}}}{2m_{C \perp}} - \frac{{\hbar ^{2}k_{\parallel}^{2}}}{2m_{C \parallel}} && (b=C)
\end{cases} \tag{3.1.2}
$$

# 3.2 Equilibrium Emission (Interband)

$$
\begin{align}
\Gamma  &= \frac{2\pi}{\hbar}\sum\limits_{\mathbf{\mathbf{k,}k'}} |\braket{ \psi_{k} |H'|\psi_{k'}  } |^{2} \ \ \delta({\small E(k') - E(k)-\hbar\omega}) \\ \\
&=\frac{2\pi}{\hbar}\int\limits_{\text{BZ}} \int\limits_{\text{BZ}} |\braket{ \psi_{k} |H'|\psi_{k'}  } |^{2} \ f({\small E(k)}) \ \Big[1- f({\small E(k')}) \Big] \ \delta({\small E(k') - E(k)-\hbar\omega}) \frac{d^{3}k}{(2\pi)^{3}} \frac{d^{3}k}{(2\pi)^{3}}
\end{align}

$$

# 3.3 Non-equilibrium Distribution (Interband)

Not sure how to implement the changes for the non-equilibrium case.
- There is the $\epsilon''$ in $\delta E$ which should now be according to Lorentz and not Drude.
- Shouldn't the distinction between the bands be taken into account in the non-equilibrium distribution $f$?




