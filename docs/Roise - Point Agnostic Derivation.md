# 1 Introduction & Remarks

This note rebuilds Rosei's interband $\epsilon_2(\hbar\omega,T)$ of gold from Fermi's Golden Rule, in his own notation, so that the ten numbered equations of Guerrisi, Rosei & Winsemius ("GRW", _Phys. Rev. B_ **12**, 557 (1975)) all come out of **one** derivation. The 1975 paper works the $X$ point explicitly and delegates $L$ to earlier work; here both edges come from a single point-agnostic calculation, and the three printed equations that don't reproduce — (4), (6), (8) — are flagged with corrected forms where they arise.

**The one idea that organizes everything.** The Golden-Rule integrand depends on the wavevector $\mathbf k$ only through two scalars: the _transition energy_ $W(\mathbf k)=\hbar\omega_u-\hbar\omega_l$, which sits inside the energy-conserving $\delta$, and the _final-state energy_ $E(\mathbf k)=\hbar\omega_u$, which is the only argument of the occupation. So the natural — indeed the _forced_ — move is a single change of variables $(k_\perp,k_\parallel)\to(E,W)$. Both $\delta$'s become coordinate conditions, the occupation carries out of the geometry untouched, and, because both bands are parabolic, the map is **linear**: its matrix carries the dispersion relations and its determinant is the Jacobian that becomes Rosei's $\mathcal F$. Every object in the paper — the energy-distributed JDOS $D$, the mass parameter $\mathcal F$, the integration window, the sub-gap tail — is a readout of this one map. There is no separate "insert a resolution of identity" step; that trick in the original derivation _was_ this change of variables, wearing a disguise.

**Point-agnostic by one sign.** $X$ and $L$ differ in exactly one place: the upper band curves _down_ along the zone axis at $X$ (a saddle) and _up_ at $L$ (a minimum). Carry a single label $s=\pm1$ for that curvature ($s=-1$ at $X$, $+1$ at $L$); everything else is identical. Two determinants then run the whole story, and each is a _sum-or-difference toggled by $s$_:

- $\bar B=B_l+sB_u$ — the axial curvature of the constant-energy-difference surface. Its sign fixes the **topology**: open hyperboloid (sub-gap tail) vs. closed ellipsoid (no tail).
- $\mathcal D=A_uB_l-sA_lB_u$ — the Jacobian. Its sign fixes **which band edge carries the van Hove singularity** (top of the window vs. bottom).

$X$ and $L$ are then two one-paragraph corollaries, read off at $s=\mp1$.

**Signs and magnitudes.** Every level ($\hbar\omega_{X_6^-},\hbar\omega_{X_7^+},\hbar\omega_{L_6^-},\hbar\omega_{L^+}$) and every mass ($m_{u\perp},m_{u\parallel},m_{l\perp},m_{l\parallel}$) is a _positive number_. Which way a band curves is set entirely by the explicit $\pm$ (or the label $s$) in front of each term — never by a sign hidden in a symbol. (The C&S table records some masses with a minus, e.g. $m_{u\parallel}\simeq-0.40$; that only marks downward curvature and here becomes a positive $m_{u\parallel}=0.40$ with the sign moved out front.)

## 2 Fermi's Golden Rule in $k$-space

Standard starting point. Minimal coupling in the Coulomb gauge gives $\hat H_{\rm int}=(e/mc),\mathbf A\cdot\hat{\mathbf p}$ (the $A^2$ term is interband-inert). Photon momentum is negligible on the zone scale, so transitions are vertical. FGR summed over $\mathbf k$ (spin explicit), set equal to the dissipated power $\omega\epsilon_2E_0^2/8\pi$ per unit volume, gives

$$\epsilon_2(\omega)=\frac{4\pi^2e^2}{m^2\omega^2},\frac{2}{(2\pi)^3}\int_{\rm BZ}\mathrm d^3k;\big|\hat{\boldsymbol\epsilon}\cdot\mathbf p_{ul}(\mathbf k)\big|^2,\delta\big(W(\mathbf k)-\hbar\omega\big),\big[f(\hbar\omega_l)-f(\hbar\omega_u)\big],\qquad W\equiv\hbar\omega_u-\hbar\omega_l.$$

Matrix elements are taken constant over each critical-point neighborhood and the polarization is averaged,

$$|P|^2\equiv\big|\langle u|\nabla|l\rangle\big|^2\ (\text{dimension length}^{-2}),\qquad\overline{\big|\hat{\boldsymbol\epsilon}\cdot\mathbf p_{ul}\big|^2}=\frac{\hbar^2|P|^2}{3},$$

so, per critical-point family,

$$\epsilon_2(\hbar\omega,T)=\frac{4\pi^2e^2\hbar^2}{3m^2\omega^2}\cdot\frac{2}{(2\pi)^3},N,|P|^2!\int\limits_{\rm half\text{-}nbhd}!\mathrm d^3k;\delta\big(W(\mathbf k)-\hbar\omega\big),\Delta f(E)\big|_{E=\hbar\omega_u(\mathbf k)},\tag{$\star$}$$

with

- $N$ the number of equivalent _half_-neighborhoods ($N_X=6$, $N_L=8$), paired with the half-space measure below;
- $\Delta f(E)\equiv f(E-\hbar\omega)-f(E)$ the full occupation difference (this is _absorption_: raw upward rate net of stimulated emission — Appendix B). For the deep $d$ bands it reduces to Rosei's $[1-f]$; kept general here for the non-equilibrium case ($f^S$, $f^P$). Emission (PL) carries a product instead — Appendix B.

Everything below evaluates the $\mathbf k$-integral in $(\star)$ by the single change of variables promised in §1.

## 3 One change of variables

### 3.1 A point-agnostic band pair

Both critical points carry an axially symmetric parabolic pair (energies measured from $E_F$; $k_\parallel$ along the zone axis $\Gamma X$ or $\Gamma L$, $k_\perp$ in the transverse plane). Write them once, with the single sign $s$ on the upper band's axial curvature:

$$ \begin{aligned} E=\hbar\omega_u(\mathbf k)&=\ \ \ \epsilon_u+A_u k_\perp^2+s,B_u k_\parallel^2,\[2pt] E-\hbar\omega=\hbar\omega_l(\mathbf k)&=-\epsilon_l-A_l k_\perp^2-B_l k_\parallel^2, \end{aligned}\qquad \begin{aligned} A_i&=\tfrac{\hbar^2}{2m_{i\perp}}>0,\ B_i&=\tfrac{\hbar^2}{2m_{i\parallel}}>0, \end{aligned}\tag{1,2} $$

with $\epsilon_u=\hbar\omega_{X_6^-}$ or $\hbar\omega_{L_6^-}$, $\epsilon_l=\hbar\omega_{X_7^+}$ or $\hbar\omega_{L^+}$, and

$$\boxed{,s=-1\ \text{at }X\ (\text{saddle: down along }\Delta),\qquad s=+1\ \text{at }L\ (\text{minimum}),.}$$

The lower $d$ band is a maximum in both directions at _both_ points, so its signs are fixed; the upper band's transverse curvature is a minimum at both ($A_u>0$); only its axial sign differs. That single fact is what makes one label enough. (It is an empirical feature of Au's bands, from C&S — stated as a hinge, not a theorem.)

The **transition energy** follows by subtraction:

$$W=\hbar\omega_u-\hbar\omega_l=\mathcal E_g+\bar A,k_\perp^2+\bar B,k_\parallel^2,\qquad \mathcal E_g=\epsilon_u+\epsilon_l,\quad \bar A=A_u+A_l>0,\quad \bar B=B_l+s,B_u.\tag{3}$$

### 3.2 The map, its Jacobian, and its inverse

Set $u=k_\perp^2,\ v=k_\parallel^2$ ($u,v\ge0$). Both $E$ and $W$ are _linear_ in $(u,v)$ — that linearity is the whole reason energy space is clean here — so (1) and (3) are one matrix equation:

$$\begin{pmatrix}E-\epsilon_u\[2pt]W-\mathcal E_g\end{pmatrix}=\underbrace{\begin{pmatrix}A_u & sB_u\[2pt]\bar A & \bar B\end{pmatrix}}_{M}\begin{pmatrix}u\ v\end{pmatrix},\qquad \boxed{\ \mathcal D\equiv\det M=A_u\bar B-sB_u\bar A=A_uB_l-s,A_lB_u\ }.$$

$M$ _is_ the change of variables from wavevector to energies; it carries the dispersions (1)–(3), and $\mathcal D$ is its Jacobian — the object that will become Rosei's $\mathcal F$. Note $\mathcal D$ is a determinant, i.e. built entirely from the band curvatures, and it appears here once and is reused everywhere. Inverting,

$$u=\frac{\bar B(E-\epsilon_u)-sB_u(W-\mathcal E_g)}{\mathcal D},\qquad v=k_\parallel^2=\frac{A_u(W-\mathcal E_g)-\bar A(E-\epsilon_u)}{\mathcal D}.\tag{6$'$}$$

Written in masses at $W=\hbar\omega$, the second line is Rosei's Eq. (6):

$$k_\parallel^2=\frac{2\mathcal F^2}{\hbar^2}\left[\frac{\hbar\omega-\hbar\omega_{X_7^+}-E}{m_{u\perp}}+\frac{\hbar\omega_{X_6^-}-E}{m_{l\perp}}\right]\quad(\text{$X$; general form below}),\qquad \mathcal F^2\equiv\frac{\hbar^4}{4|\mathcal D|}.$$

> [!warning] Printed Eq. (6) is dimensionally impossible Rosei prints $k_\parallel=\big(\hbar\omega-\hbar\omega_{X_7^+}+\tfrac{\hbar^2}{2m_{l\perp}}(\hbar\omega_{X_6^-}-E)-\tfrac{\hbar^2}{2m_{u\perp}}E\big)^{1/2}$: a wavevector set equal to $\sqrt{\text{energies}}$, with a bare energy added to $(\hbar^2/2m)\times$energy terms — mismatched units, and coefficients $\hbar^2/2m$ where $2m/\hbar^2$ is needed for $k_\parallel^2\sim\text{length}^{-2}$. Squaring the left side, inverting the coefficients into the overall $2\mathcal F^2/\hbar^2$, and restoring the missing $1/m_{u\perp}$ turns it into $(6')$ — which is forced, term by term, by inverting $M$. A disabling typo, since the printed line is unusable as written.

### 3.3 Pushforward of the measure → the EDJDOS $D$, and its window, together

Axial symmetry gives $\mathrm d^3k=2\pi k_\perp,\mathrm dk_\perp,\mathrm dk_\parallel$; with $k_\perp\mathrm dk_\perp=\tfrac12\mathrm du$ and $\mathrm dk_\parallel=\mathrm dv/2\sqrt v$,

$$\frac{1}{(2\pi)^3}\int_{\rm half}\mathrm d^3k=\frac{1}{16\pi^2}\int_0^\infty!\mathrm du\int_0^\infty!\frac{\mathrm dv}{\sqrt v};\xrightarrow{\ (u,v)\to(E,W)\ };\frac{1}{16\pi^2|\mathcal D|}\int!\frac{\mathrm dE,\mathrm dW}{k_\parallel(E,W)},$$

using $\mathrm du,\mathrm dv=\mathrm dE,\mathrm dW/|\mathcal D|$ and $\sqrt v=k_\parallel$. The energy-conserving $\delta(W-\hbar\omega)$ in $(\star)$ now does its one job — fix $W=\hbar\omega$ — and the _energy-distributed JDOS_ (transitions per unit volume, per unit final energy $E$, per unit transition energy, one half-neighborhood, one spin) reads straight off the pushforward:

$$\boxed{;D_{l\to u}(E,\hbar\omega)=\frac{1}{16\pi^2,|\mathcal D|,k_\parallel(E,\hbar\omega)}=\frac{\mathcal F^2_{l\to u}}{4\pi^2\hbar^4},\frac{1}{k_\parallel(E,\hbar\omega)};}\tag{4$'$}$$

with $k_\parallel(E,\hbar\omega)$ from $(6')$ at $W=\hbar\omega$. No identity was inserted and no $\delta$ was manufactured: $D$ is the Jacobian of one change of variables, and the two $\delta$'s of the original treatment are the two rows of $M$. **The integration window is part of the same readout** — it is nothing but the image of the physical quadrant ${u\ge0,,v\ge0}$ under $M$. Setting each coordinate to zero gives the two edges:

$$E_\parallel(\hbar\omega)=\epsilon_u+\frac{A_u}{\bar A}(\hbar\omega-\mathcal E_g)\quad(v=k_\parallel^2=0:\ D\propto k_\parallel^{-1}\ \text{diverges}),$$ $$E_\perp(\hbar\omega)=\epsilon_u+s,\frac{B_u}{\bar B}(\hbar\omega-\mathcal E_g)\quad(u=k_\perp^2=0:\ k_\parallel\ \text{and }D\ \text{finite}),$$

tied by the single identity that decides the whole edge story:

$$\boxed{;E_\parallel-E_\perp=\frac{\mathcal D}{\bar A,\bar B},(\hbar\omega-\mathcal E_g);}\tag{edge}$$

Read off both determinants at once:

- **$\operatorname{sign}\bar B$ sets the topology.** $\bar B>0$: CEDS is a closed ellipsoid, states only for $\hbar\omega\ge\mathcal E_g$, both edges finite → a _bounded_ window $[\min,\max]$ of ${E_\parallel,E_\perp}$. $\bar B<0$: open hyperboloid, states on both sides of $\mathcal E_g$, $E$ unbounded on one side → a _half-line_ cut not by geometry but by occupation, at the practical floor $E_{\rm floor}=-20k_BT$ (below which $\Delta f\to0$).
- **$\operatorname{sign}\mathcal D$ sets which geometric edge is singular.** By (edge), with $\bar A>0$, the ordering of $E_\parallel$ (singular) and $E_\perp$ (finite) flips with $\operatorname{sign}(\mathcal D/\bar B)$ and with the sign of $\hbar\omega-\mathcal E_g$.

That is the entire content of §3, and the window came free with the map — no separate limits section.

$\mathcal F$ is not an independent input. Expanding $\mathcal D=A_uB_l-sA_lB_u$ in the masses,

$$\mathcal D=\Big(\frac{\hbar^2}{2}\Big)^2\frac{m_{l\perp}m_{u\parallel}-s,m_{u\perp}m_{l\parallel}}{m_{u\perp}m_{l\perp}m_{u\parallel}m_{l\parallel}},\qquad \boxed{;\mathcal F_{l\to u}\equiv\frac{\hbar^2}{2\sqrt{|\mathcal D|}}=\left[\frac{\big|m_{l\perp}m_{u\parallel}-s,m_{u\perp}m_{l\parallel}\big|}{m_{u\perp}m_{l\perp}m_{u\parallel}m_{l\parallel}}\right]^{-1/2};}\tag{5}$$

— Rosei's Eq. (5), derived (not assumed), and valid at _both_ points: the sum at $X$ ($s=-1$), the difference at $L$ ($s=+1$). Reading $|\mathcal D|=\hbar^4/4\mathcal F^2$ back into $(4')$ is what puts $D$ into Rosei's notation.

> [!warning] Printed Eq. (4) is off by a constant — likely a typo Rosei prints $D_{l\to u}=(8\pi^2\hbar^2)^{-1}\mathcal F,k_\parallel^{-1}$. The definition of $D$ forces $(4')$, $D_{l\to u}=(16\pi^2|\mathcal D|)^{-1}k_\parallel^{-1}=\mathcal F^2(4\pi^2\hbar^4 k_\parallel)^{-1}$ — the only form that closes the FGR chain through to $\epsilon_2$ dimensionally (§5). The two differ by a pure per-critical-point constant $2\mathcal F_{l\to u}/\hbar^2$, which cannot bend a line shape and is absorbed into the fitted strength $S=\mathcal F|P|^2$ of Eq. (10). Published numbers keep their meaning; only the bookkeeping between $D,\mathcal F,|P|^2$ shifts.

## 4 $X$ and $L$ as corollaries

Everything is now a substitution $s=\mp1$ into §3. The only algebra is reading the two determinants.

### 4.1 $X$ point ($s=-1$): saddle, open window, tail

$$\bar B_X=B_l-B_u\ \ (\text{sign-indefinite}),\qquad \mathcal D_X=A_uB_l+A_lB_u>0\ \ (\text{always}).$$

Because $\mathcal D_X>0$ the singular edge $E_\parallel$ sits at the **top** of the window (by (edge), $E_\parallel>E_\perp$ above the gap). The physics lives in $\operatorname{sign}\bar B_X$:

- **Rosei's branch $\bar B_X<0$** ($m_{u\parallel}<m_{l\parallel}$, the flat-$d$ picture). Open hyperboloid at every $\hbar\omega$; $E$ unbounded below, cut by the floor $E_{\min}=-20k_BT$. The upper edge changes character at the gap: $$E_{\max}(\hbar\omega)=\hbar\omega_{X_6^-}+\begin{cases}\dfrac{A_u}{\bar A_X}(\hbar\omega-\mathcal E_g^X)=\dfrac{m_{l\perp}}{m_{u\perp}+m_{l\perp}}(\hbar\omega-\mathcal E_g^X)=E_\parallel, & \hbar\omega\ge\mathcal E_g^X\ (\text{singular}),\[12pt]-\dfrac{B_u}{|\bar B_X|}(\mathcal E_g^X-\hbar\omega)=\dfrac{m_{l\parallel}}{m_{u\parallel}-m_{l\parallel}}(\mathcal E_g^X-\hbar\omega)=E_\perp, & \hbar\omega<\mathcal E_g^X\ (\text{finite sub-gap edge}).\end{cases}\tag{8$'$}$$ The finite sub-gap edge (the $u=0$ point, which the $v=0$ circle has vacated) is Rosei's Eq. (8), and it is what makes the $X$ onset _step-like_ rather than a sharp divergence: at $T=0$ absorption switches on when it crosses $E_F$, $$\hbar\omega_{\rm on}=\mathcal E_g^X-\hbar\omega_{X_6^-}\frac{m_{l\parallel}-m_{u\parallel}}{m_{l\parallel}}\simeq1.94-0.17\times\frac{0.40-0.15}{0.40}=1.83\ \text{eV},$$ the piezomodulation threshold, the tail $1.83$–$1.94$ eV filling in purely geometrically.
- **Closed branch $\bar B_X>0$** (the extraction in the mass-fork note below): a _bounded_ window, no sub-gap tail, a $\sqrt{\hbar\omega-\mathcal E_g^X}$ onset sitting exactly at the gap.

> [!warning] Printed Eq. (8) has two subscripts swapped — likely a typo Print carries $m_{u\parallel}/(m_{l\parallel}-m_{u\parallel})$ where $(8')$ gives $m_{l\parallel}/(m_{u\parallel}-m_{l\parallel})$ — one consistent $m_{u\parallel}\leftrightarrow m_{l\parallel}$ swap, specific to (8) (the subscripts of (6) aren't swapped, so it isn't the same slip). **The tell:** on $\bar B_X<0$, $m_{u\parallel}<m_{l\parallel}$, so the printed denominator is positive and pushes $E_{\max}$ _above_ $\hbar\omega_{X_6^-}$ as $\hbar\omega$ drops below the gap — where the sub-gap CEDS has no states. $(8')$ puts the sub-gap edge sensibly _below_ $\hbar\omega_{X_6^-}$, which is what makes the tail work.

> [!note] Remark — the one mass assignment I'm unsure of at $X$ My extraction of the C&S Fig. 5 curvatures gives $m_{u\parallel}=0.40$, $m_{l\parallel}=0.15$ — the opposite $\parallel$ ordering, i.e. $\bar B_X>0$, the closed branch. Above the gap both branches share the same line shape and singular edge $(8')$ — the $\parallel$ masses enter only through $\mathcal F_X$, absorbed by the fit into $S_X$ — so optics alone can't distinguish them; only the sub-gap physics and extracted $|P_X|^2$ can. Both orderings make the $d$ band the lighter one, against the flat-$d$ prior, so a transcription swap in my own table is the likeliest fix. This note follows Rosei ($\bar B_X<0$) and flags where the branch matters.

### 4.2 $L$ point ($s=+1$): minimum, closed window, sharp edge

$$\bar B_L=B_u+B_l>0\ \ (\text{always}),\qquad \mathcal D_L=A_uB_l-A_lB_u\ \ (\text{sign-indefinite}).$$

Now the roles of "guaranteed sum" and "indefinite difference" have swapped between $\bar B$ and $\mathcal D$ — the structural fingerprint of the $X!\leftrightarrow!L$ contrast. $\bar B_L>0$ forces a **closed ellipsoid, existing only for $\hbar\omega\ge\mathcal E_g^L$: no sub-gap tail at $L$.** For gold, $m_{l\perp}m_{u\parallel}=0.70\times0.12=0.084$ and $m_{l\parallel}m_{u\perp}=1.03\times0.24=0.247$, so $\mathcal D_L<0$; by (edge) the singular $v=0$ edge is now the **lower** limit, exactly opposite $X$:

$$E_{\min}=E_\parallel=\hbar\omega_{L_6^-}+\frac{A_u}{\bar A_L}(\hbar\omega-\mathcal E_g^L)\ (\text{singular}),\qquad E_{\max}=E_\perp=\hbar\omega_{L_6^-}+\frac{B_u}{\bar B_L}(\hbar\omega-\mathcal E_g^L)\ (\text{finite}),$$

with slopes $A_u/\bar A_L=0.745$, $B_u/\bar B_L=0.896$ for Au. Nothing physical was added; the edge swap is purely $\mathcal D_L<0$ vs. $\mathcal D_X>0$. So: **$L$ is sharp and strong, $X$ soft and tailed** — Rosei's "splitting of the interband absorption edge," both halves from one formula set.

> [!note] Remark — a tension in the $L$ level scheme, recorded on purpose Fitted levels ($\mathcal E_g^L=2.45$, $\hbar\omega_{L^+}=1.56\Rightarrow\hbar\omega_{L_6^-}=+0.89$ eV) put the whole $L$ window _above_ $E_F$: the Fermi factor is inert at $L$, and $L$'s $T$-dependence enters only through broadening and gap shift. But Rosei's qualitative picture of the $L$ singularity — onset CEDS tangent to the Fermi surface along the neck — needs $L_6^-$ _below_ $E_F$. Both can't hold in one parabolic model; the fitted scheme is what the code implements.

## 5 Assembly: the thermal integral and $\epsilon_2$

With $D$ and its window in hand (both points), the two headline results follow with nothing left to choose. The thermally weighted JDOS is Eq. (7),

$$\mathcal J_i(\hbar\omega,T)=\int_{E_{\min}^{(i)}}^{E_{\max}^{(i)}}D_{l\to u}^{(i)}(E,\hbar\omega),\Delta f(E,T),\mathrm dE,\qquad \Delta f\to[1-f]\ \text{for the equilibrium $d$ band},\tag{7}$$

and inserting $(4')$ into $(\star)$ — the definition of $D$ is exactly the bridge $\int\mathrm d^3k,\delta(W-\hbar\omega)[\cdots]=(2\pi)^3!\int\mathrm dE,D[\cdots]$ per half-neighborhood, so the $(2\pi)^3$ cancels — gives Rosei's Eq. (9) with no leftover constant:

$$\boxed{;\epsilon_2(\hbar\omega,T)=\frac{8\pi^2e^2\hbar^4}{3m^2(\hbar\omega)^2}\sum_{i=X,L}N_i,|P_i|^2,\mathcal J_i(\hbar\omega,T);}\tag{9}$$

The clean landing needs three things kept straight: $|P|^2$ the squared $\nabla$ matrix element of §2; $D$ the revised $(4')$, not the printed (4); and spin (the explicit 2) with the half-point counts $N_X=6,\ N_L=8$. The quantities the data fix are the strengths,

$$S_X=\mathcal F_X|P_X|^2,\qquad S_L=\mathcal F_L|P_L|^2,\qquad |P_X/P_L|^2=0.370\ (\text{fit to Johnson–Christy}).\tag{10}$$

(Rosei leaves $N_i$ implicit, so his fitted $|P_i|^2$ means $N_i|P_i|^2$; under revised (4) the combination the data pin is $N_i\mathcal F_i^2|P_i|^2$, mapping onto the printed $S_i$ through the constant $2\mathcal F_i/\hbar^2$ — the published numbers keep their meaning.)

Fully substituted, (7)+(9) is the one explicit energy-space integral a computer would evaluate (Rosei's Eq. 11):

$$\boxed{;\epsilon_2(\hbar\omega,T)=\frac{2e^2}{3m^2(\hbar\omega)^2}\sum_{i=X,L}N_i,\mathcal F_i^2,|P_i|^2\int_{E_{\min}^{(i)}}^{E_{\max}^{(i)}}\frac{\Delta f(E,T)}{k_\parallel^{(i)}(E,\hbar\omega)},\mathrm dE;}\tag{11}$$

$$k_\parallel^{(i)}(E,\hbar\omega)=\frac{\sqrt2,\mathcal F_i}{\hbar}\left[\frac{\pm\big[(\hbar\omega-\epsilon_l^{(i)})-E\big]}{m_{u\perp}}+\frac{\pm(\epsilon_u^{(i)}-E)}{m_{l\perp}}\right]^{1/2}\quad(+\ \text{at }X,\ -\ \text{at }L),$$

the same bracket at both points with every slot sign-reversed — the single sign of §3, one last time. At $X$ the bracket falls with $E$ (singularity at the top); at $L$ it rises (singularity at the bottom). Inside each window the inversion guarantees the bracket $\ge0$.

**Parameters** (levels: Rosei's fit; masses: C&S, $X$ row subject to the §4.1 mass-fork; $\mathcal F$ in free-electron-mass units):

||$\mathcal E_g$ (eV)|upper (eV)|lower (eV)|$m_{u\perp}$|$m_{u\parallel}$|$m_{l\perp}$|$m_{l\parallel}$|
|---|---|---|---|---|---|---|---|
|$X$ ($s=-1$)|1.94|$\hbar\omega_{X_6^-}=0.17$|$\hbar\omega_{X_7^+}=1.77$|0.19|0.15|0.31|0.40|
|$L$ ($s=+1$)|2.45|$\hbar\omega_{L_6^-}=0.89$|$\hbar\omega_{L^+}=1.56$|0.24|0.12|0.70|1.03|

||$s$|$\bar B$|$\mathcal D$|$\mathcal F/m$|singular edge|
|---|---|---|---|---|---|
|$X$|$-1$|$B_l-B_u<0$ (open, tail)|$+34.7>0$|0.170|upper $E_{\max}$ ($k_\parallel\to0$)|
|$L$|$+1$|$B_u+B_l>0$ (closed)|$-7.86<0$|0.357|lower $E_{\min}$ ($k_\parallel\to0$)|

**Scorecard — the ten GRW equations:**

|GRW|here|status|issue as printed|
|---|---|---|---|
|(1)–(3)|(1)–(3)|recreated|—|
|(4)|$(4')$|**suggested fix**|prefactor $(8\pi^2\hbar^2)^{-1}\mathcal F\to(4\pi^2\hbar^4)^{-1}\mathcal F^2$; off by const. $2\mathcal F/\hbar^2$|
|(5)|(5)|recreated|now point-agnostic (sign $s$)|
|(6)|$(6')$|**suggested fix**|dimensionally impossible as printed|
|(7)|(7)|recreated|occupation generalized to $\Delta f$|
|(8)|$(8')$|**suggested fix**|$u!\parallel!\leftrightarrow!l!\parallel$ subscripts swapped|
|(9)|(9)|recreated|$N_i$ made explicit|
|(10)|(10)|recreated|units note (the (4) constant)|

## 6 Computing it: integrate in $k_\parallel$

The $1/\sqrt{}$ edge of (11) is a coordinate artifact — the map of §3 traded a smooth $k$-space geometry for the label $E$, and one substitution undoes it. Take $k\equiv k_\parallel$ as the variable. From $(6')$, $E$ is affine in $k^2$, so $\mathrm dE=-(\mathcal D/\bar A),2k,\mathrm dk$ while $D\propto1/k$: the $k$'s cancel, and the differential identity behind the flattening is one line,

$$D_{l\to u},\mathrm dE=\mp\frac{\mu_\perp}{4\pi^2\hbar^2},\mathrm dk_\parallel,\qquad \frac{1}{\mu_\perp}\equiv\frac{1}{m_{u\perp}}+\frac{1}{m_{l\perp}}.$$

So $k_\parallel$ is (up to a constant) the antiderivative of $D$: integrating in $k_\parallel$ **is** integrating in $E$ with $D$ absorbed into the node spacing. Eq. (7) flattens to a smooth integral with no singularity anywhere,

$$\boxed{;\mathcal J_i(\hbar\omega,T)=\frac{\mu_{i\perp}}{4\pi^2\hbar^2}\int_{k_1^{(i)}}^{k_2^{(i)}}\Delta f\big(E_i(k),T\big),\mathrm dk;}\tag{12}$$

$$E_i(k)=\underbrace{\epsilon_u+\frac{\mu_{i\perp}}{m_{u\perp}}(\hbar\omega-\mathcal E_g^i)}_{k_\parallel=0\ \text{intercept},=,E_\parallel}\ \mp\ \frac{\mu_{i\perp}\hbar^2}{2\mathcal F_i^2},k^2\qquad(-\ \text{at }X,\ +\ \text{at }L,\ \text{i.e. }-\operatorname{sign}\mathcal D).$$

The limits are the same $u=0/v=0$ endpoints of §3.3, now in $k$. At $X$ ($\bar B_X<0$) the lower limit is geometric only below the gap, the upper limit is the occupation floor:

$$k_1^X=\begin{cases}0, & \hbar\omega\ge\mathcal E_g^X,\[6pt]\dfrac{1}{\hbar}!\left[\dfrac{2(\mathcal E_g^X-\hbar\omega),m_{u\parallel}m_{l\parallel}}{m_{l\parallel}-m_{u\parallel}}\right]^{1/2}, & \hbar\omega<\mathcal E_g^X,\end{cases}\qquad k_2^X=k_\parallel^X(E_{\rm floor},\hbar\omega),$$

with $E_{\rm floor}=-20k_BT$ in equilibrium (or, for a CW pump reaching $E_F\pm\hbar\omega_{\rm pump}$, $-(\hbar\omega_{\rm pump}+20k_BT)$; over-deep floors cost a few nodes, never accuracy). At $L$ both limits are geometric and the window exists only above the gap:

$$k_1^L=0,\qquad k_2^L=\frac{1}{\hbar}\sqrt{2\mu_{L\parallel}(\hbar\omega-\mathcal E_g^L)},\qquad \frac{1}{\mu_{L\parallel}}\equiv\frac{1}{m_{u\parallel}}+\frac{1}{m_{l\parallel}}.$$

All branch logic lives in $k_1^X$; $E_i(k)$ is the single display above on both sides of the $X$ gap. The integrand is now a bounded, smooth occupation profile whose only feature is the Fermi step ($\sim k_BT$ wide), so **composite Simpson on a uniform grid** is adequate:

1. $k=\mathrm{linspace}(k_1,k_2,N)$, $N$ odd;
2. $y=\Delta f(E_i(k))$ (Fermi–Dirac, or interpolation of tabulated $f^S/f^P$);
3. `simpson(y, x=k)` times $\mu_{i\perp}/4\pi^2\hbar^2$; then into (9).

Measured against a converged reference (equilibrium, $\hbar\omega=2.4$ eV): at 300 K the $X$ integral is at $5\times10^{-10}$ relative error with $N=101$, machine precision by $N=201$; the $L$ integrand is constant to machine precision (window above $E_F$), and even at 2000 K, $N=101$ gives $3\times10^{-14}$. Two things to watch: **resolve the step** at $k_{\rm step}=k(E{=}0)$ (trivial to locate; or split there and Simpson each panel); and **respect the kinks** of a pumped $f^S$ at $E_F\pm\hbar\omega_{\rm pump}$ by placing panel boundaries at their images $k(E_F\pm\hbar\omega_{\rm pump})$ — distribution features no change of variable removes. Error control is one doubling ($N\to2N$). Two free closed-form checks: **empty-window arithmetic** ($\Delta f\equiv1\Rightarrow\mathcal J_i=\frac{\mu_{i\perp}}{4\pi^2\hbar^2}(k_2-k_1)$; at $L$, $T\to0$ this is the textbook $M_0$ $\sqrt{\ }$ onset) and **two-forms agreement** ((11) and (12) must match to quadrature accuracy).

### 6.1 Why derive in $E$ but evaluate in $k_\parallel$

A fair worry: §3 works to reach an energy-space integral and §6 seems to leave it. It doesn't — the two are the same integral, resolved in opposite order.

|route|$\delta$ resolved against|surviving label|Jacobian left behind|
|---|---|---|---|
|§3 → (7)/(11)|$(u,v)$ jointly, at fixed $W=\hbar\omega$|$E$|$1/(16\pi^2|
|§6 → (12)|$u=k_\perp^2$, at fixed $k_\parallel$|$k_\parallel$|$1/\bar A$ — a constant|

Energy space is entered for exactly one reason, and it is _not_ symmetry: the occupation depends on $\mathbf k$ **only through the final energy** $E$. That is what lets electronics factor out of geometry as the reusable weight $D(E,\hbar\omega)$ — the object Rosei tabulates, and the one that answers "which final energies does a given photon probe," the working question for thermomodulation and the pumped-PL problem. (It is _function-of-$E$-only_, not isotropy: $f$'s level sets are the anisotropic CEDS themselves. It holds because elastic scattering $\sim10$ fs equalizes occupation across each iso-energy surface long before energy relaxation $\gtrsim100$ fs — the regime $f^S,f^P$ describe.) So: **derive and reason in $E$; evaluate in $k_\parallel$.** Where a window has a singular edge, uniform-grid quadrature in $E$ decays like $O(\sqrt h)$ (still $\sim1%$ at $N=6401$) while $k_\parallel$ gives Simpson's clean $O(N^{-4})$; where it doesn't, the two agree. Equivalently, the correct $E$-space substitution $t=\sqrt{E_{\rm edge}-E}$ _is_ $k_\parallel$ up to a constant — the geometry had already named the right variable.

## Appendix A Dimensional audit (Gaussian)

$[e^2]=\mathrm{erg,cm}$, $[|P|^2]=\mathrm{cm}^{-2}$, $[\mathcal D]=\mathrm{erg^2cm^4}$, $[\mathcal F]=\mathrm g$, $[D_{l\to u}]=\mathrm{erg^{-2}cm^{-3}}$, $[\mathcal J]=\mathrm{erg^{-1}cm^{-3}}$.

- $(4')$: $\mathcal F^2/\hbar^4k_\parallel\sim\mathrm g^2/(\mathrm{erg^4s^4,cm^{-1}})=\mathrm{erg^{-2}cm^{-3}}$. ✓
- $(9)$: $\dfrac{\mathrm{erg,cm}\cdot\mathrm{erg^4s^4}}{\mathrm g^2,\mathrm{erg^2}}\cdot\mathrm{cm^{-2}}\cdot\mathrm{erg^{-1}cm^{-3}}=1$. ✓
- $(12)$: $\mu_\perp k/\hbar^2\sim\mathrm{g,cm^{-1}}/(\mathrm{erg^2s^2})=\mathrm{erg^{-1}cm^{-3}}=[\mathcal J]$. ✓

## Appendix B From absorption to emission: where the Bose–Einstein factor hides

The body computes $\epsilon_2$ — absorption — with weight $\Delta f(E)=f(E-\hbar\omega)-f(E)$. Photoluminescence is spontaneous _emission_, whose weight is a _product_, $f(E)[1-f(E-\hbar\omega)]$. Name the states by the energies already used: lower (initial, $d$) at $E_l\equiv E-\hbar\omega$, upper (final, $sp$) at $E_u\equiv E$; $f_l\equiv f(E-\hbar\omega)$, $f_u\equiv f(E)$, $\beta\equiv1/k_BT$.

**Three rates.** One $|M|^2\propto|\hat{\boldsymbol\epsilon}\cdot\mathbf p_{ul}|^2$ drives absorption $W_{\rm abs}\propto|M|^2N_{\rm ph}f_l(1-f_u)$, stimulated emission $W_{\rm stim}\propto|M|^2N_{\rm ph}f_u(1-f_l)$, and spontaneous emission $W_{\rm spon}\propto|M|^2\rho_{\rm ph}f_u(1-f_l)$ (the PL rate; $\rho_{\rm ph}$ the photonic LDOS). Absorption and stimulated emission carry _opposite_ electronic factors; stimulated and spontaneous carry the _same_ one.

**Absorption → a difference.** $\epsilon_2$ is _net_ power, up minus stimulated-down; $|M|^2N_{\rm ph}$ cancels out of the response function, leaving

$$f_l(1-f_u)-f_u(1-f_l)=f_l-f_u=\Delta f(E).$$

The cross term $f_lf_u$ subtracts to zero. This is the origin of the difference in (11) — raw rate net of stimulated emission — and it assumed nothing about equilibrium, which is why the body carries $\Delta f$ unmodified into the $f^S,f^P$ case.

**Emission in equilibrium → a Bose factor.** The PL weight $f_u(1-f_l)$ has no subtraction. In equilibrium, from $1-f=e^{\beta(E-\mu)}f$ applied at both levels,

$$\frac{f_u(1-f_l)}{f_l(1-f_u)}=e^{-\beta(E_u-E_l)}=e^{-\beta\hbar\omega}\quad(\mu\ \text{and level energies cancel; only }\hbar\omega\ \text{survives}).$$

Feeding detailed balance back into $\Delta f=f_l(1-f_u)(1-e^{-\beta\hbar\omega})$ and solving,

$$\boxed{;f_u(1-f_l)=n_{\rm BE}(\hbar\omega),\Delta f(E),\qquad n_{\rm BE}=\frac1{e^{\beta\hbar\omega}-1};}$$

with the twin $f_l(1-f_u)=(1+n_{\rm BE})\Delta f$ — the $n$ vs. $n+1$ of emission vs. absorption, read off the electron occupations ($n_{\rm BE}$ is manufactured from two Fermi factors, not the driving field; it coincides with a photon Bose function only because both bands share one $(\mu,T)$). The PL spectrum is then a one-line edit of (11) — replace $\Delta f$ by $f_u(1-f_l)$, restore $\rho_{\rm ph}$ — evaluated on the _same_ geometry, windows, and $k_\parallel$ of §6:

$$R_{\rm PL}(\hbar\omega,T)\propto\rho_{\rm ph}(\hbar\omega)\sum_{i=X,L}N_i\mathcal F_i^2|P_i|^2\int_{k_1^{(i)}}^{k_2^{(i)}}\frac{\mu_{i\perp}}{4\pi^2\hbar^2},f(E)[1-f(E-\hbar\omega)],\mathrm dk_\parallel.$$

In equilibrium the box turns this into $R_{\rm PL}\propto\rho_{\rm ph},n_{\rm BE},\epsilon_2$ — Kirchhoff recovered.

> [!warning] The collapse is equilibrium-only Every step used $1-f=e^{\beta(E-\mu)}f$ twice with **one shared** $(\beta,\mu)$. Under a pumped $f^S/f^P$ — non-thermal, with slope breaks at $E_F\pm\hbar\omega_{\rm pump}$ — no single $(\mu,T)$ exists, and $$n_{\rm eff}(E,\hbar\omega)\equiv\frac{f(E)[1-f(E-\hbar\omega)]}{f(E-\hbar\omega)-f(E)}$$ retains genuine $E$-dependence: it cannot be pulled out of the integral as any Bose factor. The PL integrand must be carried as the full product, node by node — exactly what §6 already does for $\Delta f$, now with the emission weight. This is the physics the pumped problem is _about_: equilibrium PL is enslaved to absorption ($R_{\rm PL}\propto n_{\rm BE}\epsilon_2$, no independent information); the pump reshapes $f(E)$ so $n_{\rm eff}$ varies across the window and the emission line shape parts company with absorption. Reproducing $n_{\rm eff}\to n_{\rm BE}$ under $f=f_{\rm FD}$ is a good unit test; _taking_ it throws the signal away.

## References

- M. Guerrisi, R. Rosei, P. Winsemius, _Phys. Rev. B_ **12**, 557 (1975) — the paper recreated here ($X$ derived, $L$ delegated).
- R. Rosei, _Phys. Rev. B_ **10**, 474 (1974) — the $L$ machinery (and EDJDOS recipe) Rosei borrows.
- N. E. Christensen, B. O. Seraphin, _Phys. Rev. B_ **4**, 3321 (1971) — band structure; source of the masses.
- P. B. Johnson, R. W. Christy, _Phys. Rev. B_ **6**, 4370 (1972) — the data Rosei fits.