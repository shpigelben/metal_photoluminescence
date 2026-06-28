# Equivalence of My Absorption Integral and Rosei's $D_{l\to u}$

**Goal.** Show that my reduced absorption integrand and Rosei's energy-distributed joint density of states (EDJDOS), eqs (4)–(6) of Guerrisi–Rosei–Winsemius (1975), are the *same function* up to a multiplicative constant that is independent of $E$ and $\omega$. Along the way this resolves the two things that looked wrong:

1. **Units / prefactor.** Rosei's $D_{l\to u}$ appears short by a factor with the units of $2m/\hbar^2$, and carries $\mathcal{F}^{1}$ where my Jacobian carries $\mathcal{F}^{2}$.
2. **Occupation factor.** I keep $f(E-\hbar\omega)\,[1-f(E)]$; Rosei keeps only $[1-f(E)]$.

Throughout I take **my expression as correct** and show Rosei's is the same up to (i) a constant rescaling absorbed in his overall normalization and (ii) the valence-band-full approximation $f(E_l)\to 1$.

---

## 0. The two expressions

**Mine** (after the change of variables and collapsing the $\delta$):

$$
\epsilon''(\omega)\ \propto\ \int f(E-\hbar\omega)\,\big[1-f(E)\big]\,\mathcal{J}(E)\,dE,
\qquad
\mathcal{J}(E)=\frac{2\pi k_\perp}{|\det J|}\bigg|_{\Delta=\hbar\omega}.
$$

**Rosei's** (his eqs 4–6):

$$
D_{l\to u}(E,\hbar\omega)=\frac{1}{8\pi^{2}\hbar^{2}}\,\mathcal{F}_{l\to u}\,k_\|^{-1},
\qquad
\mathcal{F}_{l\to u}=\left(\frac{m_{l\perp}m_{u\|}+m_{l\|}m_{u\perp}}{m_{l\perp}m_{l\|}m_{u\perp}m_{u\|}}\right)^{-1/2}.
$$

The claim is $\mathcal{J}(E)=\text{const}\times D_{l\to u}(E,\hbar\omega)$ with the constant free of $E,\omega$.

---

## 1. Setup: dispersions and change of variables

Parabolic bands at $X$ (cylindrical symmetry, $k_\perp,k_\|$):

$$
\begin{aligned}
E_u &= \hbar\omega_{X_6^-} + A_u k_\perp^2 + B_u k_\|^2,\\
E_l &= -\hbar\omega_{X_7^+} - A_l k_\perp^2 + B_l k_\|^2,
\end{aligned}
\qquad
A_i=\frac{\hbar^2}{2m_{i\perp}},\quad B_i=\frac{\hbar^2}{2m_{i\|}} .
$$

New variables $(k_\perp,k_\|)\to(E,\Delta)$:

$$
E\equiv E_u = \hbar\omega_{X_6^-}+A_u k_\perp^2 + B_u k_\|^2,
\qquad
\Delta\equiv E_u-E_l = \hbar\omega_X + \bar A\,k_\perp^2 + (B_u-B_l)\,k_\|^2,
$$

with $\bar A=A_u+A_l$ and $\hbar\omega_X=\hbar\omega_{X_6^-}+\hbar\omega_{X_7^+}$. The measure is

$$
2\pi k_\perp\,dk_\perp\,dk_\| = \frac{2\pi k_\perp}{|\det J|}\,dE\,d\Delta,
\qquad
J=\frac{\partial(E,\Delta)}{\partial(k_\perp,k_\|)} .
$$

---

## 2. The Jacobian → curvature determinant

$$
J=\begin{pmatrix}
\partial_{k_\perp}E & \partial_{k_\|}E\\[2pt]
\partial_{k_\perp}\Delta & \partial_{k_\|}\Delta
\end{pmatrix}
=\begin{pmatrix}
2A_u k_\perp & 2B_u k_\|\\[2pt]
2\bar A k_\perp & 2(B_u-B_l)k_\|
\end{pmatrix}.
$$

$$
\det J = 4k_\perp k_\|\Big[A_u(B_u-B_l)-B_u\bar A\Big]
= 4k_\perp k_\|\big[-(A_uB_l+A_lB_u)\big],
$$

so the $k_\perp$ cancels and

$$
\boxed{\,|\det J| = 4\,k_\perp k_\|\,\mathcal{D},\qquad \mathcal{D}\equiv A_uB_l+A_lB_u\, }.
$$

$\mathcal{D}$ is the **band-curvature determinant** — purely effective-mass constants, no $E,\omega,k$ dependence. Expanding:

$$
\mathcal{D}=A_uB_l+A_lB_u
=\Big(\tfrac{\hbar^2}{2}\Big)^{2}\!\left(\frac{1}{m_{u\perp}m_{l\|}}+\frac{1}{m_{l\perp}m_{u\|}}\right)
=\Big(\tfrac{\hbar^2}{2}\Big)^{2}\frac{m_{l\perp}m_{u\|}+m_{l\|}m_{u\perp}}{m_{u\perp}m_{l\|}m_{l\perp}m_{u\|}} .
$$

Comparing with $\mathcal{F}_{l\to u}^{-2}=\dfrac{m_{l\perp}m_{u\|}+m_{l\|}m_{u\perp}}{m_{l\perp}m_{l\|}m_{u\perp}m_{u\|}}$ gives exactly my note's identity:

$$
\boxed{\ \mathcal{D}=\Big(\tfrac{\hbar^2}{2}\Big)^{2}\mathcal{F}_{l\to u}^{-2}\ }
$$

This is the line my earlier note stopped at — it is the bridge between the two notations.

---

## 3. Assemble $\mathcal{J}(E)$ and compare

Insert $|\det J|=4k_\perp k_\|\mathcal{D}$ and integrate out $\Delta$ against $\delta(\Delta-\hbar\omega)$:

$$
\mathcal{J}(E)=\frac{2\pi k_\perp}{4k_\perp k_\|\,\mathcal{D}}
=\frac{\pi}{2\,k_\|\,\mathcal{D}}
=\frac{\pi}{2k_\|}\Big(\tfrac{\hbar^2}{2}\Big)^{-2}\mathcal{F}^2
=\frac{2\pi\,\mathcal{F}_{l\to u}^{2}}{\hbar^{4}\,k_\|}.
$$

Now divide by Rosei's $D_{l\to u}=\dfrac{\mathcal{F}}{8\pi^2\hbar^2 k_\|}$:

$$
\frac{\mathcal{J}(E)}{D_{l\to u}(E,\hbar\omega)}
=\frac{2\pi\mathcal{F}^2/(\hbar^4 k_\|)}{\mathcal{F}/(8\pi^2\hbar^2 k_\|)}
=16\pi^{3}\,\frac{\mathcal{F}_{l\to u}}{\hbar^{2}} .
$$

$$
\boxed{\ \mathcal{J}(E)=\underbrace{\left(16\pi^{3}\,\frac{\mathcal{F}_{l\to u}}{\hbar^{2}}\right)}_{\text{const in }E,\,\omega}\; D_{l\to u}(E,\hbar\omega)\ }
$$

The $k_\|^{-1}(E,\omega)$ structure — the **only** carrier of spectral shape — is identical in both. They differ solely by a constant.

---

## 4. Why the constant resolves the "units problem"

The prefactor difference is not an error; it is the units bridge. With $\mathcal{F}\sim$ mass,

$$
\Big[\frac{\mathcal{F}}{\hbar^2}\Big]=\frac{\mathrm{kg}}{\mathrm{J^2s^2}}=\frac{1}{\mathrm{J\,m^2}}=\Big[\frac{2m}{\hbar^2}\Big].
$$

That is exactly the $\mathrm{J^{-1}m^{-2}}$ by which Rosei's $D_{l\to u}$ fell short of a properly normalized EDJDOS ($[\,\text{vol}\,]^{-1}[\,\text{energy}\,]^{-2}=\mathrm{m^{-3}J^{-2}}$). In other words:

- My $\mathcal{J}(E)\propto\mathcal{F}^2/k_\|$ has the dimensionally complete coefficient because I carried every $\hbar^2/2m$ explicitly through the Jacobian.
- Rosei pushed one power of $2m/\hbar^2$ into his definition of $\mathcal{F}$ (leaving $\mathcal{F}^1$) and the rest into the normalization that sits in front of his $\varepsilon_2$. His $D_{l\to u}$ is therefore a *rescaled* EDJDOS, not the bare one.

Because $16\pi^3\mathcal{F}/\hbar^2$ is constant across the band, it is absorbed into the single overall prefactor of $\varepsilon_2(\omega)$ (the `Scale` parameter in `rosei_model_formulas.md`). **No spectral information is lost or changed.**

> **Caveat on eq (6).** As printed in the OCR'd `.tex`, Rosei's $k_\|$ adds an energy to terms $\frac{\hbar^2}{2m}\times$energy and is dimensionally inhomogeneous; the coefficients must read $\frac{2m}{\hbar^2}$ for $k_\|$ to come out in $\mathrm{m^{-1}}$. Verify against `7 - Rosei.pdf`: if the PDF shows $\hbar^2/2m$ it is Rosei's own shorthand (constants reshuffled as above); if it shows $2m/\hbar^2$ it is a Mathpix artifact to patch.

---

## 5. Why the occupation factors agree

I keep the full product
$$
f(E_l)\,[1-f(E_u)] = f(E-\hbar\omega)\,[1-f(E)] ,
$$
Rosei keeps only $[1-f(E)]$. For **absorption** the initial state $l$ is the (nearly full) valence band well below $E_F$, so at the relevant energies

$$
E-\hbar\omega = E_l \ll E_F \ \Rightarrow\ f(E-\hbar\omega)\to 1 .
$$

Hence Rosei's integrand is the $f(E_l)\to1$ limit of mine. Keeping $f(E-\hbar\omega)$ explicit (as I do) is the more general form — necessary once the bands are driven out of equilibrium or at elevated $T_e$, where the initial-state occupation is no longer unity. At equilibrium absorption the two coincide.

---

## 6. Conclusion

$$
\epsilon''(\omega)\ \propto\ \int f(E-\hbar\omega)\,[1-f(E)]\,\mathcal{J}(E)\,dE
\quad\xrightarrow[\ \text{absorb const into Scale}\ ]{\ f(E_l)\to1\ }\quad
\epsilon_2^{\text{Rosei}}(\omega)\ \propto\ \int [1-f(E)]\,D_{l\to u}(E,\hbar\omega)\,dE .
$$

The expressions are equivalent:

- **Functional form:** identical, both $\propto k_\|^{-1}(E,\omega)$ with the same integration limits.
- **Prefactor:** differ by the constant $16\pi^3\mathcal{F}/\hbar^2$, whose units ($2m/\hbar^2$) are precisely what makes Rosei's $D$ dimensionally complete; absorbed into the overall $\varepsilon_2$ scale.
- **Occupation:** Rosei's $[1-f]$ is my $f(E-\hbar\omega)[1-f]$ under $f(E_l)\to1$, valid for equilibrium interband absorption.

So there was never a real disagreement — only Rosei's habit of folding the $2m/\hbar^2$ constants into $\mathcal{F}$ and his normalization, plus the full-valence-band approximation. My form is the dimensionally explicit, non-equilibrium-ready version, which is what I need for the emission and pulsed extensions.

---

*Related:* [[Absorption Integral (Using Rosei's Notations)]] · `code/main/rosei_model_formulas.md` · ref 7 (`TEXs/7 - Rosei`).
