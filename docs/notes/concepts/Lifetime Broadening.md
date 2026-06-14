photon energy must be complex: $\hbar\omega \to \hbar\omega + i\Gamma$.
Because we are using momentum matrix elements rather than position/dipole elements, linear response theory pulls out a global $1/\omega^2$ prefactor. Plugging the complex energy into the resonant susceptibility gives:

$$\chi(\omega) \propto \frac{1}{\omega^2} \int d^3k \, \frac{|\mathbf{p}_{cv}(\mathbf{k})|^2}{\Delta E(\mathbf{k}) - (\hbar\omega + i\Gamma)}$$

Since I only care about the absorption here, I take the imaginary part ($\chi'' = \text{Im}[\chi]$). Using the standard complex fraction identity $\text{Im}\left[\frac{1}{x - i\Gamma}\right] = \frac{\Gamma}{x^2 + \Gamma^2}$, the Lorentzian shape emerges immediately for every $k$-point:

$$\chi''(\omega) \propto \frac{1}{\omega^2} \int d^3k \, |\mathbf{p}_{cv}(\mathbf{k})|^2 \left[ \frac{1}{\pi} \frac{\Gamma}{(\Delta E(\mathbf{k}) - \hbar\omega)^2 + \Gamma^2} \right]$$


By assuming infinite lifetimes, I get infinitely sharp Dirac delta peaks for the unbroadened integral (let's call this raw phase space integral $I_0$):

$$I_0(\omega) = \int d^3k \, |\mathbf{p}_{cv}(\mathbf{k})|^2 \delta(\Delta E(\mathbf{k}) - \hbar\omega)$$

**Step B: The Smearing Process**
I then take that sharp result and convolve it with a standard Lorentzian kernel $L(\omega, \Gamma)$:

$$I_{\text{conv}}(\omega) = \int d(\hbar\omega') \, I_0(\omega') \left[ \frac{1}{\pi} \frac{\Gamma}{(\hbar\omega - \hbar\omega')^2 + \Gamma^2} \right]$$

**Step C: Swapping the Integrals**

I substitute my full FGR integral from Step A into the convolution:

$$I_{\text{conv}}(\omega) = \int d(\hbar\omega') \left[ \int d^3k \, |\mathbf{p}_{cv}(\mathbf{k})|^2 \delta(\Delta E(\mathbf{k}) - \hbar\omega') \right] \frac{1}{\pi} \frac{\Gamma}{(\hbar\omega - \hbar\omega')^2 + \Gamma^2}$$

Because these integrals are well-behaved, I can safely use Fubini's theorem to swap the order of integration, bringing the energy integral inside:

$$I_{\text{conv}}(\omega) = \int d^3k \, |\mathbf{p}_{cv}(\mathbf{k})|^2 \left[ \int d(\hbar\omega') \, \delta(\Delta E(\mathbf{k}) - \hbar\omega') \frac{1}{\pi} \frac{\Gamma}{(\hbar\omega - \hbar\omega')^2 + \Gamma^2} \right]$$

**Step D: The Sifting Property**

The delta function makes the inner integral trivial. It "sifts" out the value where $\hbar\omega'$ exactly equals $\Delta E(\mathbf{k})$. So, I simply replace $\hbar\omega'$ with $\Delta E(\mathbf{k})$ in the Lorentzian:

$$I_{\text{conv}}(\omega) = \int d^3k \, |\mathbf{p}_{cv}(\mathbf{k})|^2 \left[ \frac{1}{\pi} \frac{\Gamma}{(\hbar\omega - \Delta E(\mathbf{k}))^2 + \Gamma^2} \right]$$

_(Note: squaring $(\hbar\omega - \Delta E)$ is exactly equivalent to squaring $(\Delta E - \hbar\omega)$)._

**Step E: Applying the Prefactor**

Finally, to get the actual macroscopic absorption, I multiply the smeared integral by the global frequency scaling factor:

$$\chi''_{\text{conv}}(\omega) \propto \frac{1}{\omega^2} I_{\text{conv}}(\omega)$$

### Conclusion

$$\chi''_{\text{Fundamental}} \equiv \chi''_{\text{Convolution}}$$