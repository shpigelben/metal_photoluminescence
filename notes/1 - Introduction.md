The emission of EM radiation from a body can be (in which cases?) attributed to photonic and electronic contributions separately [Novotny]. In this study we focus on the latter.

$$
\begin{align}
I(\hbar\omega) &= I_{\text{ph}}(\hbar\omega)\cdot I_{\text{e}}(\hbar\omega)
\end{align}
$$

Electronic transitions which begin at a high energy state and end up in a lower energy state result in the spontaneous emission of photons with ==appropriate energy==. Transitions such as these can occur either inside the conduction band (assisted by phonons) or between bands - intraband and interband transitions respectively[^1].

$$
I_{\text{e}} = I_{\text{cc}} + I_{\text{cv}}
$$

Out materials of interest are metals (specifically gold) in which the predominant electronic contribution to emission comes from intraband transitions[^2]. Therefore, in a state of thermal equilibrium we also don't expect measurable interband presence in emission spectrum from metals [Marini?].


> [!NOTE] Main Thesis
> In non-equilibrium scenarios, however, such as in the steady-state case of a metal illuminated by monochromatic radiation, incoming photons of sufficient energy might be able to generate a significant hole population in the valence band which would allow for interband transitions to be more prominent in the emission spectrum of the metal.


Non-equilibrium electronic distribution for the above scenario has been derived and applied to the case of intraband transitions [Sivan & Dubi]. These calculations, however, enjoyed the approximate isotropy of the conduction band which allows one to transition to the more lenient energy space.

The valence band is generally anisotropic and when performing interband calculations one has to remain in k-space, which is what we are going to do. 

Once we have established that our calculations in momentum space align with those performed in energy space - both in equilibrium and non-equilibrium settings - we proceed to perform the interband scenario. In the end, hopefully, we will be able to provide a more complete emission spectrum to both cases.

# Gold Nanoparticles

We focus on interband transitions from the X and L points in k-space whose approximate symmetry can be used to simplify calculations. They also account for lion-share of the interband transitions, but not all of them.

![center|300](../../../9.%20Misc/attachments/Pasted%20image%2020251029172425.png)

The overall electronic contribution to emission is therefore given by

$$
\Gamma = \Gamma_{\text{cc}} + 6\Gamma_{\text{cv}}^{\text{X}} + 8\Gamma_{\text{cv}}^{\text{L}}
$$

[^1]: Technically transitions can occur inside the valence band, but these are very unlikely and their contribution at standard cases is negligible.

## TOC

1. intraband comparison
	1. equilibrium
	2. non-equilibrium
2. intreband comparison
	1. equilibrium
	2. non-equilibrium

[^2]: Large band gap + Fermi energy is well within the conduction band
