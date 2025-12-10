	$$\small
\Gamma_{\alpha\beta}(\hbar\omega) = \frac{2\pi}{\hbar}\left( \frac{2V}{(2\pi)^{3}} \right)^{2} \iint\limits_{BZ} |\mu(\mathbf{k}_{\text{i}},\mathbf{k}_{\text{f}})|^{2} \  f\Big[\mathcal{E_{\alpha}}(\mathbf{k}_{\text{i}})  \Big]\overline{f\Big[\mathcal{E_{\beta}}(\mathbf{k}_{\text{f}})  \Big]}\  \delta\Big(\mathcal{E}_{\alpha}(\mathbf{k}_{\text{i}}) - \mathcal{E}_{\beta}(\mathbf{k}_{\text{f}}) - \hbar\omega   \Big) \  dk_{\text{i}}^{3} \ dk_{\text{f}}^{3} \tag{1}
$$
> [!NOTE]- Impossibility of a one step intraband transition 
> The transition dipole moment $\mu(\mathbf{k}_{\text{i}},\mathbf{k}_{\text{f}})$ implicitly contains a statement about the conservation of momentum, namely that $$\mathbf{k}_{i} = \mathbf{k}_{\text{i}} = \mathbf{k}_{\text{f}}+\mathbf{q} = \mathbf{k}_{f}$$ Where $\mathbf{q}$ is the momentum of the emitted photon. Since photons have negligible momenta relative to electrons' $(\mathbf{q}\ll \mathbf{k})$, the electron momentum should virtually remain unchanged $$\delta(\mathbf{k}_{\text{i}} - \mathbf{k}_{\text{f}}-\mathbf{q}) \to \delta(\mathbf{k}_{\text{i}} - \mathbf{k}_{\text{f}})$$. This result renders single process intraband transitions moot. These have zero probability of occurring. In Yonatan's calculations in energy space momentum is not conserved. The only reason why this would be ok (as I understand it) is if a two-step process is implicitly assumed in which for every energetic transition there exists a phonon which provides the exact amount of the missing momentum. This raises a couple of questions:
> 1. Is this even physically accurate assumption to make?
> 2. Even if it is, would every energetic transition have a proper phonon with the same probability? The current calculation would treat it as such.
>    
>    Bottom line is that, in my opinion, intraband transitions should be treated as two-step processes, and the interband calculations - under the assumption of direct transition - would become simpler.

- For intraband transition $\alpha=\beta=\text{c}$ where $\text{c}$ stands for conduction band.
- Constant transition dipole moment approximation $|\mu(\mathbf{k}_{\text{i}},\mathbf{k}_{\text{f}})|^{2}\to|\mu_{\text{cc}}|^{2}$ (for the conduction band).
$$
\Gamma_{\text{cc}}(\hbar\omega) = \frac{2\pi}{\hbar}\left( \frac{2\mu_{\text{cc}}V}{(2\pi)^{3}} \right)^{2} \iint\limits_{BZ} f\Big[\mathcal{E_{\text{c}}}(\mathbf{k}_{\text{i}})  \Big]\overline{f\Big[\mathcal{E_{\text{c}}}(\mathbf{k}_{\text{f}})  \Big]} \ \delta \Big( \mathcal{E}_{\text{c}}(\mathbf{k}_{\text{i}}) - \mathcal{E}_{\text{c}}(\mathbf{k}_{\text{f}}) - \hbar\omega \Big) \ d^{3}k_{\text{i}}d^{3}k_{\text{f}} \tag{2}
$$
The dispersion relation of the conduction band is isotropic. This allows us to move from the 3-dimensional momentum space to the 1-dimensional energy space using the [A2 - Electronic Density of States](A2%20-%20Electronic%20Density%20of%20States.md), namely
$$
d^{3}k\to \rho(\mathcal{E})d\mathcal{E} = \frac{4\pi \sqrt{2m_{e}^{3}\mathcal{E}}}{\hbar^3} \ d\mathcal{E}
$$
$$
\Gamma_{\text{cc}}(\hbar\omega) = \frac{2\pi}{\hbar}\left( \frac{2\mu_{\text{cc}}V}{(2\pi)^{3}} \right)^{2} \iint\limits_{\text{BZ}} f(\mathcal{E}_{c\text{i}})\overline{f(\mathcal{E_{\text{cf}}})}  \ \delta(\mathcal{E_{\text{ci}}-\mathcal{E}_{\text{cf}}-\hbar\omega}) \ \rho(\mathcal{E}_{\text{ci}}) \rho(\mathcal{E}_{\text{cf}})d\mathcal{E}_{\text{ci}}d\mathcal{E}_{\text{cf}} \tag{3}
$$
In energy space, the delta can be easily resolved

$$
\Gamma_{\text{cc}}(\hbar\omega) = \frac{2\pi}{\hbar}\left( \frac{2\mu_{\text{cc}}V}{(2\pi)^{3}} \right)^{2} \int\limits_{\text{BZ}} f(\mathcal{E}_{c\text{i}})\overline{f(\mathcal{E_{\text{ci}}-\hbar\omega})}  \ \ \rho(\mathcal{E}_{\text{ci}}) \rho(E_{\text{ci}}-\hbar\omega)d\mathcal{E}_{\text{ci}} \tag{4}
$$
Equation $(4)$ serves as our reference, since it is calculated in Yonatan's paper and is assumed to be correct due to its alignment with experimental evidence. Since we're later going approximate the delta function by a Gaussian, this is the place to establish the validity of such approximation
$$
\Gamma_{\text{cc}}(\hbar\omega) = \frac{2\pi}{\hbar}\left( \frac{2\mu_{\text{cc}}V}{(2\pi)^{3}} \right)^{2} \iint\limits_{\text{BZ}} f(\mathcal{E}_{c\text{i}})\overline{f(\mathcal{E_{\text{cf}}})}  \ \lim\limits_{\sigma_{\mathcal{E}}\to 0} G\Big(\mathcal{E_{\text{ci}}-\mathcal{E}_{\text{cf}}-\hbar\omega} \ ; \ \sigma_{\mathcal{E}}\Big) \ \rho(\mathcal{E}_{\text{ci}}) \rho(\mathcal{E}_{\text{cf}})d\mathcal{E}_{\text{ci}}d\mathcal{E}_{\text{cf}} \tag{5}
$$

$$
G\Big(\mathcal{E_{\text{ci}}-\mathcal{E}_{\text{cf}}-\hbar\omega} \ ; \ \sigma_{\mathcal{E}}\Big) = 
$$

==Under the assumption that the integral converges, the limit can be taken out of the integral==
