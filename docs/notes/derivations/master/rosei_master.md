<!-- TEX-PREAMBLE (verbatim; edit macros/packages here, not below) -->
% =====================================================================
%  rosei_master.tex
%  Master rederivation of Rosei's interband epsilon_2 for gold from
%  Fermi's Golden Rule in k-space, written throughout in Rosei's own
%  notation and symbols (GRW 1975), so that his ten numbered equations
%  pop out of one derivation.  Where the printed equations do not come
%  out -- (4), (6), (8) -- the failure is stated and fixed.  Includes
%  the photonic density of states, the emission counterpart, and the
%  k_parallel quadrature scheme used by the numerics.
%
%  Consolidates and supersedes (see derivations/README.md):
%    A1, A8, A8.L, "Absorption Integral (Using Rosei's Notations)",
%    "Interband Absorption at X and L (Rosei's Notation)",
%    "Equivalence of My Absorption Integral and Rosei's",
%    "Effective Mass Extraction", rosei_model_formulas.md,
%    interband_derivation{,_v2}.tex, rosei_equivalence_derivation.tex;
%    notation and fixes follow "Rebuilding Rosei's Interband Absorption
%    in His Own Notation & Suggesting Possible Fixes.md".
% =====================================================================
\documentclass[11pt,a4paper]{article}

\usepackage[hmargin=2.0cm,vmargin=2.4cm]{geometry}
\usepackage{amsmath,amssymb,mathtools,bm}
\usepackage{booktabs}
\usepackage{paracol}
\usepackage{needspace}
\usepackage[dvipsnames,table]{xcolor}
\usepackage{microtype}
\usepackage[colorlinks=true,linkcolor=MidnightBlue,citecolor=ForestGreen,urlcolor=MidnightBlue]{hyperref}

\numberwithin{equation}{section}

% ------------------------------ macros -------------------------------
\newcommand{\hw}{\hbar\omega}
\newcommand{\Eg}{\mathcal{E}_g}
\newcommand{\EgX}{\mathcal{E}_g^{X}}
\newcommand{\EgL}{\mathcal{E}_g^{L}}
\newcommand{\Elu}{\mathcal{E}_{lu}}
\newcommand{\cD}{\mathcal{D}}
\newcommand{\cF}{\mathcal{F}}
\newcommand{\cJ}{\mathcal{J}}
\newcommand{\Ab}{\bar{A}}
\newcommand{\Bb}{\bar{B}}
\newcommand{\kperp}{k_{\perp}}
\newcommand{\kpar}{k_{\parallel}}
\newcommand{\pul}{\mathbf{p}_{ul}}
\newcommand{\eps}{\varepsilon}
\newcommand{\dd}{\mathrm{d}}
\newcommand{\Dlu}{D_{l\to u}}
\newcommand{\wXu}{\hbar\omega_{X_6^-}}
\newcommand{\wXl}{\hbar\omega_{X_7^+}}
\newcommand{\wLu}{\hbar\omega_{L_6^-}}
\newcommand{\wLl}{\hbar\omega_{L^+}}
\newcommand{\wuz}{\hbar\omega_{u0}}
\newcommand{\wlz}{\hbar\omega_{l0}}
\newcommand{\fFD}{f}
\newcommand{\kB}{k_B}
\newcommand{\rme}{\mathrm{e}}

% step titles inside the two-column X/L comparison
% (vspace* so the gap survives at the top of a synchronized row)
\newcommand{\colstep}[1]{\par\vspace*{10pt}\noindent\textbf{#1}\par\nobreak\vspace*{3pt}\noindent\ignorespaces}

% shading for the core rows of the route map
\colorlet{corerow}{MidnightBlue!8}

\newtheorem{remark}{Remark}[section]

\title{\bfseries Interband Absorption in Gold from Fermi's Golden Rule:\\
a first-principles rederivation of Rosei's $\eps_2$ at the $X$ and $L$
critical points, in Rosei's own notation}
\author{Ben Shpigel\\ \small Department of Physics, Ben-Gurion University of the Negev}
\date{July 2026}

\begin{document}
<!-- END-TEX-PREAMBLE -->

<!-- MACROS-FOR-OBSIDIAN-PREVIEW-START -->
$$
\gdef\hw{\hbar\omega}
\gdef\Eg{\mathcal{E}_g}
\gdef\EgX{\mathcal{E}_g^{X}}
\gdef\EgL{\mathcal{E}_g^{L}}
\gdef\Elu{\mathcal{E}_{lu}}
\gdef\cD{\mathcal{D}}
\gdef\cF{\mathcal{F}}
\gdef\cJ{\mathcal{J}}
\gdef\Ab{\bar{A}}
\gdef\Bb{\bar{B}}
\gdef\kperp{k_{\perp}}
\gdef\pul{\mathbf{p}_{ul}}
\gdef\eps{\varepsilon}
\gdef\dd{\mathrm{d}}
\gdef\Dlu{D_{l\to u}}
\gdef\wXu{\hbar\omega_{X_6^-}}
\gdef\wXl{\hbar\omega_{X_7^+}}
\gdef\wLu{\hbar\omega_{L_6^-}}
\gdef\wLl{\hbar\omega_{L^+}}
\gdef\wuz{\hbar\omega_{u0}}
\gdef\wlz{\hbar\omega_{l0}}
\gdef\fFD{f}
\gdef\kB{k_B}
\gdef\rme{\mathrm{e}}
$$
*(live-preview macros only, mirrors the .tex preamble; stripped on reconversion -- edit macros there, not here)*
<!-- MACROS-FOR-OBSIDIAN-PREVIEW-END -->

\maketitle

\begin{abstract}
\noindent
This document rederives, from first principles and with every prefactor
tracked, the Rosei-model interband $\eps_2(\hw,T)$ of gold at the $X$
and $L$ critical points [Guerrisi, Rosei \& Winsemius, Phys.\ Rev.\ B
\textbf{12}, 557 (1975); hereafter simply ``Rosei''], written
throughout in Rosei's own notation, so that the paper's ten numbered
equations emerge explicitly from one derivation.  The route runs from
Fermi's Golden Rule (FGR) for Bloch states in $\mathbf{k}$-space,
through the reduction of the transition sum to a one-dimensional
energy integral by the change of variables $(u,v)=(\kperp^2,\kpar^2)$,
to the resolution of the double $\delta$-constraint by a single
$2\times2$ Jacobian.  Seven of the ten equations are recreated
verbatim; the printed Eqs.~(4), (6) and (8) do not come out as
written, and for each the failure is stated in one line and the
corrected form derived (Sec.~\ref{sec:grw}).  The photonic density of
states is derived by field quantization, the spontaneous-emission
counterpart is assembled, and the pair is shown to close exactly into
the detailed-balance relation between emission and absorption (van
Roosbroeck--Shockley/Kirchhoff) --- the global consistency check of
all prefactors.  A final section gives the $\kpar$ quadrature scheme
that evaluates the model without touching its edge singularities: the
groundwork for the numerical implementation.
\end{abstract}

\tableofcontents

% =====================================================================
# Scope \& sources {{label:sec:scope}}
% =====================================================================

Everything below is self-contained: it is built from Fermi's Golden
Rule and four primary sources.
\begin{itemize}
\item \textbf{Rosei 1975} (Guerrisi, Rosei \& Winsemius; ``Rosei''
      from here on) --- the paper recreated.  Only the $X$ point is
      actually derived there, and the printed Eqs.~(4), (6), (8) have
      defects --- fixed in Sec.~\ref{sec:grw}.
\item \textbf{Rosei 1974} --- the EDJDOS recipe and the $L$-point
      machinery (``will not be repeated here''; it is repeated here).
\item \textbf{Christensen \& Seraphin 1971} --- the band structure:
      levels and masses.  Rosei's own source as well (his Ref.~4).
\item \textbf{Johnson \& Christy 1972} --- the optical data the model
      is fitted to.
\end{itemize}
Notation is Rosei's: bands are $u$ (upper) and $l$ (lower), all levels
and masses are positive numbers with every sign written explicitly,
and an equation tagged \textbf{($n$)} is Rosei's Eq.~($n$) recreated
--- primes, as in ($6'$), mark corrected forms.  The rest of the
conventions live in App.~\ref{sec:conv}.

\medskip
\noindent Route map --- shaded rows are the heart of the document, the
Rosei recreation; the others are scaffolding that keeps it
self-contained:

\begin{center}
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{@{}lll@{}}
\toprule
where & what happens & leans on\\
\midrule
Sec.~\ref{sec:fgr} & golden-rule machinery, every constant tracked & ---\\
\rowcolor{corerow}
Sec.~\ref{sec:reduction} & $\mathbf k$-space reduction $\to$ Eqs.~($4'$), (5), (7) & Rosei 1975/1974\\
\rowcolor{corerow}
Sec.~\ref{sec:XL} & $X$ and $L$, side by side $\to$ Eqs.~($6'$), ($8'$) & Rosei 1975/1974\\
\rowcolor{corerow}
Sec.~\ref{sec:eps2} & $\eps_2$ assembled $\to$ (9)--(11); scorecard; corrections; Drude & C\&S; J\&C\\
Sec.~\ref{sec:photonic} & photonic DOS, emission, detailed balance & Novotny--Hecht\\
Sec.~\ref{sec:numerics} & $\kpar$ quadrature for the implementation & ---\\
\bottomrule
\end{tabular}
\end{center}

% =====================================================================
# Fermi's Golden Rule in $\mathbf{k}$-space {{label:sec:fgr}}
% =====================================================================

## Minimal coupling

With the radiation field described by a vector potential $\mathbf{A}$
in the Coulomb gauge ($\nabla\!\cdot\!\mathbf{A}=0$), the one-electron
Hamiltonian is
\begin{equation}
\hat H=\frac{[\hat{\mathbf p}+\tfrac{e}{c}\mathbf A(\hat{\mathbf r},t)]^2}{2m}
       +V(\hat{\mathbf r})
      =\underbrace{\frac{\hat p^2}{2m}+V}_{\hat H_0}
       +\underbrace{\frac{e}{2mc}\bigl(\mathbf A\!\cdot\!\hat{\mathbf p}
        +\hat{\mathbf p}\!\cdot\!\mathbf A\bigr)}_{\hat H_{\rm int}}
       +\underbrace{\frac{e^2A^2}{2mc^2}}_{\text{dropped}} .
\end{equation}
In the Coulomb gauge $\hat{\mathbf p}\!\cdot\!\mathbf A
=\mathbf A\!\cdot\!\hat{\mathbf p}$, so
\begin{equation}
\boxed{\;\hat H_{\rm int}=\frac{e}{mc}\,\mathbf A\!\cdot\!\hat{\mathbf p}\;}
\label{eq:Hint}
\end{equation}
(the $\tfrac12$ of the symmetrized form is consumed by the identity of
the two terms).  The $A^2$ term does not connect different bands to
first order and is dropped.

## Quantized field: absorption, stimulated and spontaneous emission
\label{sec:quantized}

Expanding the field in a quantization volume $V$,
\begin{equation}
\mathbf A(\mathbf r)=\sum_{\mathbf q,\lambda}
\sqrt{\frac{2\pi\hbar c^2}{\omega_q V}}\;\hat{\bm\eps}_\lambda
\Bigl(\hat a_{\mathbf q\lambda}\,\rme^{i\mathbf q\cdot\mathbf r}
     +\hat a^\dagger_{\mathbf q\lambda}\,\rme^{-i\mathbf q\cdot\mathbf r}\Bigr),
\label{eq:Aquant}
\end{equation}
the matrix elements of $\hat H_{\rm int}$ between joint
electron--photon states carry the boson factors
\begin{equation}
\bigl|\langle n_q-1|\hat a|n_q\rangle\bigr|^2=n_q
\quad\text{(absorption)},\qquad
\bigl|\langle n_q+1|\hat a^\dagger|n_q\rangle\bigr|^2=n_q+1
\quad\text{(emission)} .
\label{eq:bosefactors}
\end{equation}
The ``$+1$'' is the spontaneous channel: it survives at $n_q=0$ and is
invisible to a purely classical $\mathbf A$.  The semiclassical golden
rule gives absorption and \emph{stimulated} emission only; spontaneous
emission requires \eqref{eq:bosefactors}, and its mode sum produces the
photonic density of states in Sec.~\ref{sec:photonic}.

## Bloch states and vertical transitions

For Bloch states $\psi_{n\mathbf k}=\rme^{i\mathbf k\cdot\mathbf r}
u_{n\mathbf k}(\mathbf r)/\sqrt V$, the matrix element of
$\rme^{\pm i\mathbf q\cdot\mathbf r}\,\hat{\bm\eps}\!\cdot\!\hat{\mathbf p}$
enforces $\mathbf k'=\mathbf k\pm\mathbf q$.  At optical frequencies
$q\sim\omega/c\sim10^{-3}\,$\AA$^{-1}$ is negligible on the zone scale,
so transitions are vertical ($\mathbf k'=\mathbf k$) and
\begin{equation}
M_{ul}(\mathbf k)\equiv
\langle u\,\mathbf k|\,\hat{\bm\eps}\!\cdot\!\hat{\mathbf p}\,|l\,\mathbf k\rangle,
\qquad
\bigl|\langle f|\hat H_{\rm int}|i\rangle\bigr|^2
=\Bigl(\frac{e}{mc}\Bigr)^{2}\frac{2\pi\hbar c^2}{\omega V}\,
 |M_{ul}(\mathbf k)|^{2}\times\{n_q\text{ or }n_q+1\}.
\label{eq:MEsq}
\end{equation}

## Golden-rule rate, $\eps_2$, and the origin of the $1/\omega^2$
\label{sec:eps2def}

FGR for one photon mode, then summing over $\mathbf k$ (factor 2 for
spin, $\sum_{\mathbf k}\to V\!\int\!\dd^3k/(2\pi)^3$) with Pauli
blocking, gives the photon absorption rate.  Equating the absorbed
power to the electromagnetic dissipation rate
$P_{\rm abs}=\tfrac{1}{8\pi}\,\omega\,\eps_2(\omega)\,|\mathbf E_0|^2 V$
of a classical field $\mathbf E=\mathbf E_0\cos\omega t$ yields
\begin{equation}
\boxed{\;
\eps_2(\omega)=\frac{4\pi^2 e^2}{m^2\omega^2}\,
\frac{2}{(2\pi)^3}\int_{\rm BZ}\!\dd^3k\;
\bigl|M_{ul}(\mathbf k)\bigr|^{2}\,
\delta\!\bigl(\hbar\omega_u(\mathbf k)-\hbar\omega_l(\mathbf k)-\hw\bigr)\,
\bigl[1-\fFD\bigl(\hbar\omega_u(\mathbf k)\bigr)\bigr]\; }
\label{eq:eps2exact}
\end{equation}
per pair of bands (SI: replace $4\pi e^2\to e^2/\eps_0$).  The
occupation factor is Rosei's, discussed in Sec.~\ref{sec:occupation}.

Where does the $1/\omega^2$ up front come from?  It is fixed before
any band structure enters --- and it is worth watching, because
emission will carry a \emph{different} power
(Sec.~\ref{sec:photonic}).  Unpack \eqref{eq:eps2exact} into its three
$\omega$-carrying pieces, marking the net power each one contributes:
\begin{equation}
\eps_2=\frac{8\pi\,P_{\rm abs}/V}
{\underbrace{\textstyle\omega}_{-1}\;E_0^{2}},
\qquad
P_{\rm abs}=\underbrace{\textstyle\hw}_{+1}\times\ \text{rate},
\qquad
\text{rate}\;\propto\;
\Bigl(\frac{eA_0}{mc}\Bigr)^{\!2}
=\frac{e^{2}E_0^{2}}{m^{2}}\,
\underbrace{\frac{1}{\omega^{2}}}_{-2}\ \ (A_0=cE_0/\omega).
\label{eq:wcount}
\end{equation}
The $+1$ (one quantum per event) cancels the $-1$ (the $\omega$ in the
definition of dissipation); the $-2$ of the vertex is all that
survives.  It is the price of writing the
$\mathbf A\!\cdot\!\mathbf p$ coupling in terms of the measured field
--- pure kinematics, no density of states involved.  (Length-gauge
cross-check: $|\pul|^2=m^2\omega_{ul}^2\,|\mathbf r_{ul}|^2$ hides the
same factor inside the dipole element, so on shell the two forms agree
identically.)

Near a critical point the interband matrix element varies slowly;
following Rosei we freeze it and average over polarization, in his
gradient convention:
\begin{equation}
|P|^2\equiv\bigl|\langle u|\nabla|l\rangle\bigr|^2
\ \ (\text{length}^{-2}),
\qquad
\overline{|M_{ul}|^2}
=\overline{\bigl|\hat{\bm\eps}\!\cdot\!\pul\bigr|^2}
=\frac{\hbar^2|P|^2}{3} .
\label{eq:Pdef}
\end{equation}
Per critical-point family this turns \eqref{eq:eps2exact} into the
working form
\begin{equation}
\eps_2(\hw,T)=\frac{4\pi^2e^2\hbar^2}{3m^2\omega^2}\cdot
\frac{2}{(2\pi)^3}\,N\,|P|^2
\int_{\text{half-nbhd}}\!\!\dd^3k\;
\delta\bigl(\Elu(\mathbf k)-\hw\bigr)\,
\bigl[1-\fFD(E)\bigr]\Bigr|_{E=\hbar\omega_u(\mathbf k)},
\label{eq:star}
\end{equation}
with the interband energy $\Elu\equiv\hbar\omega_u-\hbar\omega_l$
(Sec.~\ref{sec:bands} connects it to Rosei's $\Omega_{lu}$) and $N$
the half-neighborhood count of App.~\ref{sec:conv}.

## Occupation factor: Rosei's $[1-f]$ {{label:sec:occupation}}

The exact net weight of \eqref{eq:eps2exact} --- absorption minus
stimulated emission --- is the difference
$\fFD(E-\hw)-\fFD(E)$ read at the final-state energy
$E=\hbar\omega_u(\mathbf k)$.  For the noble-metal $d$ bands the
initial state sits at $E-\hw\lesssim-1.5\,$eV${}\ll-\kB T$, so
$\fFD(E-\hw)=1$ to machine precision and the difference \emph{is}
Rosei's factor,
\begin{equation}
\fFD(E-\hw)-\fFD(E)\;\longrightarrow\;\bigl[1-\fFD(E,T)\bigr],
\label{eq:occup}
\end{equation}
which is used throughout this document, exactly as Rosei uses it.
(The \emph{emission} weight is a different object --- a product, not a
difference --- and is derived in Sec.~\ref{sec:photonic}.)

% =====================================================================
# Reduction of the $\mathbf{k}$-integral: the common machinery
\label{sec:reduction}
% =====================================================================

## The Rosei two-band model {{label:sec:bands}}

Both critical points are axially symmetric parabolic pairs.  The
parabolic dispersion relations are the primary sources': at $X$ they
are Rosei's own Eqs.~(1)--(2); at $L$ they are the forms of the 1974
Ag analysis, which the 1975 paper adopts for gold; levels and masses
for both come from the relativistic band calculation of Christensen \&
Seraphin --- Rosei's source too.  Why label the bands by $E$ and
$E-\hw$?  Because a vertical transition at photon energy $\hw$
connects exactly those two energies, so the occupation factors can be
read off directly at the final energy $E$.  With the positive
levels/masses of App.~\ref{sec:conv}, generic levels $\wuz>0$ (empty,
above $E_F$) and $\wlz>0$ (occupied $d$ level below $E_F$), and the
\emph{topology switch} $s$,
\begin{equation}
\boxed{\;
\begin{aligned}
E=\hbar\omega_u(\mathbf k)&=+\wuz+A_u\kperp^{2}+s\,B_u\kpar^{2},
&\qquad s_{X}&=-1\ \ \text{(saddle)},\\[2pt]
E-\hw=\hbar\omega_l(\mathbf k)&=-\wlz-A_l\kperp^{2}-B_l\kpar^{2},
&\qquad s_{L}&=+1\ \ \text{(minimum)},
\end{aligned}\;}
\label{eq:bands}
\end{equation}
where $(\wuz,\wlz)=(\wXu,\wXl)$ at $X$ and $(\wLu,\wLl)$ at $L$; the
lower band is a local maximum in both directions at both points.  The
interband energy is then
\begin{equation}
\Elu(\mathbf k)
=\Eg+\Ab\,\kperp^{2}+\Bb\,\kpar^{2},
\qquad
\Eg=\wuz+\wlz,\quad
\Ab=A_u+A_l>0,\quad
\boxed{\Bb=B_l+s\,B_u}
\label{eq:Omega}
\end{equation}
--- the entire topological difference between $X$ and $L$ is carried
by $s$ through $\Bb$ (and the determinant $\cD$ below).

A note on reach: \eqref{eq:bands} are local expansions, and the
constant matrix elements behind Eq.~(9) are claimed by Rosei only in a
region ${\sim}(\pi/10a)^{3}$ around each point --- yet no explicit
$k_{\max}$ will appear in any integration bound below.  That is
Rosei's own bookkeeping, not an omission: what polices locality
instead (the photon-energy range) is quantified after the window table
of Sec.~\ref{sec:eps2}.

A note on symbols: Rosei's own $\Omega_{lu}$ is not this energy but
the \emph{constraint} built from it,
\begin{equation}
\Omega_{lu}(\mathbf k)\equiv
\hbar\omega_u-\hbar\omega_l-\hw=\Elu(\mathbf k)-\hw=0,
\tag{3}
\label{eq:CEDS}
\end{equation}
whose zero set is the constant-energy-difference surface (CEDS) ---
the surface on which everything below happens.  We keep the two
apart: $\Elu$ is a function on $\mathbf k$-space; Rosei's Eq.~(3),
$\Omega_{lu}=0$, picks out the surface.  The gold parameters are
collected in the tables of Sec.~\ref{sec:eps2}.

## Sorting transitions by final energy
\label{sec:sort}

The occupation in \eqref{eq:star} depends on $\mathbf k$ only through
the final energy $E=\hbar\omega_u(\mathbf k)$ --- that is where
temperature enters --- so before any geometry we \emph{sort the
transitions by $E$}, by slipping the identity
$1=\int\dd E\;\delta(\hbar\omega_u(\mathbf k)-E)$ into \eqref{eq:star}:
\begin{equation}
\begin{aligned}
\int_{\kpar>0}\!\!\dd^3k\;\delta(\Elu-\hw)\,[1-\fFD]
&=\int_{E_{\min}}^{E_{\max}}\!\!\dd E\;[1-\fFD(E)]
\underbrace{\int_{\kpar>0}\!\!\dd^3k\;
\delta\bigl(\hbar\omega_u-E\bigr)\,
\delta\bigl(\Elu-\hw\bigr)}_{(2\pi)^3\,\Dlu(E,\hw)}\\[2pt]
&\equiv(2\pi)^3\,\cJ_{l\to u}(\hw,T) .
\end{aligned}
\label{eq:sort}
\end{equation}
The limits $[E_{\min},E_{\max}]$ are simply where the double-$\delta$
has support; they are worked out per critical point in
Sec.~\ref{sec:XL}.  Read \eqref{eq:sort} from the outside in: the
outer object $\cJ_{l\to u}$ is already Rosei's thermally weighted JDOS
--- his Eq.~(7), waiting only for its integrand --- and that integrand,
the inner integral, is his central object: the
\emph{energy-distributed joint density of states} (EDJDOS),
transitions per unit crystal volume, per unit final energy, per unit
transition energy (one half-neighborhood, one spin).  Both $\delta$'s
are accounted for: energy conservation was already in \eqref{eq:star};
the second is the inserted identity, and it is what lets $\cJ$ weight
each $E$ by its own occupation.

## Change of variables $(u,v)=(\kperp^2,\kpar^2)$ {{label:sec:linear}}

This is the step where the present derivation simplifies Rosei's
geometric construction --- and the form of \eqref{eq:sort} itself
dictates it.  The two $\delta$-functions in \eqref{eq:sort} have
arguments $\hbar\omega_u(\mathbf k)-E$ and $\Elu(\mathbf k)-\hw$, and
by \eqref{eq:bands} and \eqref{eq:Omega} both are \emph{affine in the
squared coordinates} $\kperp^2$ and $\kpar^2$.  A $\delta$-function of
a linear argument collapses trivially; so choose the variables in
which the constraints \emph{are} linear.  On the quadrant $u,v\ge0$
with $(u,v)=(\kperp^2,\kpar^2)$, fixing the final energy $E$ and the
interband energy $\Elu=\hw$ reads
\begin{equation}
\begin{pmatrix} E-\wuz\\[2pt] \hw-\Eg\end{pmatrix}
=\underbrace{\begin{pmatrix} A_u & s\,B_u\\[2pt] \Ab & \Bb\end{pmatrix}}_{\textstyle M}
\begin{pmatrix} u\\[2pt] v\end{pmatrix},
\qquad
\cD\equiv\det M=A_uB_l-s\,A_lB_u .
\label{eq:linsys}
\end{equation}
Stacking the two constraints \emph{is} the construction of the
transition matrix $M$; its determinant is the Jacobian that will
collapse the two $\delta$-functions below.  Inverting,
\begin{equation}
\boxed{\;
u=\frac{\Bb\,(E-\wuz)-s\,B_u(\hw-\Eg)}{\cD},
\qquad
v=\kpar^{2}=\frac{A_u(\hw-\Eg)-\Ab\,(E-\wuz)}{\cD}
\;}
\label{eq:uv}
\end{equation}
and the physical window is exactly $\{u\ge0\}\cap\{v\ge0\}$.
The two point-specific determinants:
\begin{equation}
\cD_X=A_uB_l+A_lB_u>0\ \ \text{always (either sign of $\Bb_X$)},
\qquad
\cD_L=A_uB_l-A_lB_u\ \ (<0\ \text{for Au}) .
\label{eq:Ds}
\end{equation}

## The EDJDOS: general derivation for both $X$ and $L$
\label{sec:kernel}

Now reduce the inner integral of \eqref{eq:sort} all the way --- this
is where $\cD$ and $\cF$ come from.
Axial symmetry gives $\dd^3k=2\pi\kperp\dd\kperp\,\dd\kpar$; in the
squared variables $\kperp\dd\kperp=\tfrac12\dd u$,
$\dd\kpar=\dd v/(2\sqrt v)$:
\begin{equation}
\frac{1}{(2\pi)^3}\int_{\kpar>0}\!\!\dd^3k
=\frac{1}{(2\pi)^3}\,\frac{\pi}{2}
\int_0^\infty\!\!\dd u\int_0^\infty\!\frac{\dd v}{\sqrt v}
=\frac{1}{16\pi^2}\int_0^\infty\!\!\dd u\int_0^\infty\!\frac{\dd v}{\sqrt v}.
\end{equation}
The two $\delta$'s are exactly the two rows of $M$ in
\eqref{eq:linsys}; linear $\delta$'s collapse onto the unique solution
\eqref{eq:uv} divided by $|\det M|=|\cD|$, and $\sqrt{v_*}=\kpar(E,\hw)$:
\begin{equation}
\Dlu(E,\hw)=\frac{1}{16\pi^2\,|\cD|}\,\frac{1}{\kpar(E,\hw)} .
\label{eq:Draw}
\end{equation}
\textbf{This is the whole result of the reduction: it contains only
$\cD$ and $\kpar$ --- no $\cF$ yet.}  Rosei's $\cF_{l\to u}$ is not an
independent input but a repackaging of $\cD$, manufactured here.
Expanding $\cD_X$ in the masses,
\begin{equation}
\cD_X=A_uB_l+A_lB_u
=\Bigl(\frac{\hbar^2}{2}\Bigr)^{2}
\frac{m_{l\perp}m_{u\parallel}+m_{l\parallel}m_{u\perp}}
{m_{l\perp}m_{l\parallel}m_{u\perp}m_{u\parallel}},
\end{equation}
and defining $\cF_{l\to u}\equiv\hbar^2/(2\sqrt{|\cD|})$ as pure
shorthand, the $\hbar^2/2$ cancels and Rosei's Eq.~(5) falls out ---
derived, not assumed --- together with its $L$ analogue:
\begin{equation}
\cF_X=\left[\frac{m_{l\perp}m_{u\parallel}+m_{l\parallel}m_{u\perp}}
{m_{l\perp}m_{l\parallel}m_{u\perp}m_{u\parallel}}\right]^{-1/2},
\qquad
\cF_L=\left[\frac{\bigl|m_{l\perp}m_{u\parallel}-m_{l\parallel}m_{u\perp}\bigr|}
{m_{l\perp}m_{l\parallel}m_{u\perp}m_{u\parallel}}\right]^{-1/2}
\tag{5}
\label{eq:Fmass}
\end{equation}
(the sum/difference structure is the $s=\mp1$ dichotomy of
\eqref{eq:Ds}).  Reading the shorthand backwards,
$|\cD|=\hbar^4/4\cF^2$, and \eqref{eq:Draw} becomes the EDJDOS in
Rosei's own symbols:
\begin{equation}
\boxed{\;
\Dlu(E,\hw)=\frac{1}{16\pi^2\,|\cD|}\,\frac{1}{\kpar(E,\hw)}
=\frac{\cF_{l\to u}^{2}}{4\pi^2\hbar^{4}}\,\frac{1}{\kpar(E,\hw)}
\;}
\tag{4$'$}
\label{eq:D4p}
\end{equation}
supported on $u,v\ge0$, with $\kpar$ from \eqref{eq:uv}.

\medskip
\noindent\textbf{Where the printed (4) falls.}  Rosei prints
$\Dlu=(8\pi^2\hbar^2)^{-1}\cF/\kpar$.  With $|P|^2$ the squared
gradient matrix element of \eqref{eq:Pdef}, the pair \{printed (4),
printed (9)\} does not balance dimensionally, whereas ($4'$) ---
forced, with nothing left to choose, by the definition of $\Dlu$ in
\eqref{eq:sort} --- closes the FGR chain exactly through to $\eps_2$
(Sec.~\ref{sec:eps2}).  The two forms differ only by the constant
$2\cF/\hbar^2$ per critical point; a constant cannot bend a line
shape, and it is absorbed into the fitted strength $S=\cF|P|^2$ of
Eq.~(10) --- which is why the slip is invisible in the published
numbers.  Details in Sec.~\ref{sec:grw}.

## The thermally weighted JDOS: Rosei's Eq.\ (7)

With $\Dlu$ in hand, the outer integral of \eqref{eq:sort} is,
verbatim as Rosei writes it,
\begin{equation}
\boxed{\;
\cJ_{l\to u}(\hw,T)=\int_{E_{\min}}^{E_{\max}}
\Dlu(E,\hw)\,\bigl[1-\fFD(E,T)\bigr]\,\dd E
\;}
\tag{7}
\label{eq:J7}
\end{equation}
with the windows $[E_{\min},E_{\max}]$ set by the geometry
($u,v\ge0$) and, where the geometry leaves an edge open, by the
occupation itself --- next section.

% =====================================================================
# The two critical points, side by side {{label:sec:XL}}
% =====================================================================

Everything so far is common.  The topology forks the derivation
through two signs only: $s$ (shape of $\Bb$) and
$\mathrm{sign}(\cD)$ (which window edge is singular).  The $X$ column
follows Rosei's own branch, $\Bb_X<0$ (see the mass fork,
Sec.~\ref{sec:fork}); his equations then pop out directly.

\Needspace{20\baselineskip}
\medskip
% \noindent\rule{\textwidth}{0.8pt}
\setlength{\columnsep}{22pt}
\columnratio{0.5}
\setlength{\columnseprule}{0.4pt}
\begin{paracol}{2}

\begin{center}\underline{{\Large\bfseries $X$ point\quad ($s=-1$)}}\end{center}
\switchcolumn
\begin{center}\underline{{\Large\bfseries $L$ point\quad ($s=+1$)}}\end{center}
\switchcolumn*

\colstep{Bands}
\begin{align*}
E&=+\wXu+\frac{\hbar^2\kperp^2}{2m_{u\perp}}
       -\frac{\hbar^2\kpar^2}{2m_{u\parallel}},\\
E-\hw&=-\wXl-\frac{\hbar^2\kperp^2}{2m_{l\perp}}
       -\frac{\hbar^2\kpar^2}{2m_{l\parallel}} .
\end{align*}
Rosei's Eqs.\ (1)--(2) verbatim: the $X_6^-$ ($sp$) band curves up in
the face, down along $\Delta$ --- a saddle; $X_7^+$ ($d$) is a
maximum.
\switchcolumn
\colstep{Bands}
\begin{align*}
E&=+\wLu+\frac{\hbar^2\kperp^2}{2m_{u\perp}}
      +\frac{\hbar^2\kpar^2}{2m_{u\parallel}},\\
E-\hw&=-\wLl-\frac{\hbar^2\kperp^2}{2m_{l\perp}}
      -\frac{\hbar^2\kpar^2}{2m_{l\parallel}} .
\end{align*}
Not derived in the 1975 paper (borrowed from Rosei 1974); rederived
here with the same tools.  $L_6^-$ is a \emph{minimum} in both
directions; $L^+$ ($d$ top) a maximum.  The only change from $X$ is
the sign of the upper $\kpar^2$ term; that one flip cascades through
everything below.
\switchcolumn*

\colstep{Transition surface (CEDS)}
\[
\Elu=\EgX+\Ab_X\kperp^2+\Bb_X\kpar^2,\quad
\Bb_X=B_l-B_u<0
\]
on Rosei's branch ($m_{u\parallel}<m_{l\parallel}$: the $sp$ band
falls along $\Delta$ faster than the $d$ band).  The CEDS is an
\emph{open} hyperboloid at every $\hw$: transitions exist on both
sides of $\EgX$ --- a real sub-gap tail.
\switchcolumn
\colstep{Transition surface (CEDS)}
\[
\Elu=\EgL+\Ab_L\kperp^2+\Bb_L\kpar^2,\quad
\Bb_L=B_l+B_u>0
\]
unconditionally: a closed ellipsoid, existing only for $\hw\ge\EgL$.
\emph{No sub-gap tail at $L$} --- the sharp-vs-tailed contrast of the
two edges is baked in right here.
\switchcolumn*

\colstep{Determinant}
\[
\cD_X=A_uB_l+A_lB_u>0\ \ \text{(either branch)} .
\]
\switchcolumn
\colstep{Determinant}
\[
\cD_L=A_uB_l-A_lB_u<0\ \ \text{for Au}
\]
($m_{l\perp}m_{u\parallel}=0.084<m_{l\parallel}m_{u\perp}=0.247$).
\switchcolumn*

\colstep{Constrained $\kpar$}
\[
\kpar^{2}
=\frac{2\cF_X^{2}}{\hbar^{2}}\Bigl[
\frac{\hw-\wXl-E}{m_{u\perp}}
+\frac{\wXu-E}{m_{l\perp}}\Bigr].
\]
Rosei's Eq.\ (6), corrected --- called ($6'$) throughout; see
Sec.~\ref{sec:grw}.
\switchcolumn
\colstep{Constrained $\kpar$}
\[
\kpar^{2}
=\frac{2\cF_L^{2}}{\hbar^{2}}\Bigl[
\frac{E-(\hw-\wLl)}{m_{u\perp}}
+\frac{E-\wLu}{m_{l\perp}}\Bigr].
\]
Same inversion, $\cD_L<0$ reversing both inequalities.
\switchcolumn*

\colstep{Window}
$E$ decreases without bound along the CEDS
($\dd E\propto-\cD_X\dd v<0$): no geometric floor.  The integral is
cut by occupation alone --- Rosei's practical floor
$E_{\min}=-20\kB T$.  The ceiling is geometric and changes character
at the gap:
\[
E_{\max}=\wXu+
\begin{cases}
\dfrac{A_u}{\Ab_X}(\hw-\EgX), & \hw\ge\EgX,\\[10pt]
-\dfrac{B_u}{|\Bb_X|}(\EgX-\hw), & \hw<\EgX,
\end{cases}
\]
the lower line being Rosei's Eq.\ (8), corrected --- ($8'$),
Sec.~\ref{sec:grw}.
\switchcolumn
\colstep{Window}
Both edges geometric ($v\ge0$ now gives the
\emph{lower} edge, $u\ge0$ the upper):
\begin{align*}
E_{\min}&=\wLu+\frac{A_u}{\Ab_L}(\hw-\EgL),\\
E_{\max}&=\wLu+\frac{B_u}{\Bb_L}(\hw-\EgL),
\end{align*}
slopes $0.745$ and $0.896$ for Au.  The whole window rides upward from
$\wLu=0.89$ eV (Remark~\ref{rem:neck}).
\switchcolumn*

\newpage
\colstep{Singular edge}
Above the gap the ceiling is the
$\kpar\to0$ circle, where $\Dlu\propto1/\kpar$ diverges:
\[
\frac{1}{\kpar(E)}=\sqrt{\frac{\cD_X}{\Ab_X}}\;
\frac{1}{\sqrt{E_{\max}-E}} .
\]
Below the gap the ceiling is the finite $\kperp=0$ point: no
divergence.
\switchcolumn
\colstep{Singular edge}
From \eqref{eq:uv} with $\cD_L<0$,
\[
\kpar^{2}=\frac{\Ab_L}{|\cD_L|}\,\bigl(E-E_{\min}\bigr),
\]
so $\Dlu\propto1/\kpar$ diverges at the \emph{lower} limit:
\[
\frac{1}{\kpar(E)}=\sqrt{\frac{|\cD_L|}{\Ab_L}}\;
\frac{1}{\sqrt{E-E_{\min}}} .
\]
\switchcolumn*

\colstep{Onset}
At $T=0$ absorption starts when $E_{\max}$ crosses
$E_F$:
\[
\hw_{\rm on}=\EgX-\wXu\,\frac{m_{l\parallel}-m_{u\parallel}}
{m_{l\parallel}}\simeq1.83\ \text{eV},
\]
the piezomodulation threshold; the tail $1.83$--$1.94$ eV is purely
geometric, and the onset is \emph{step-like} (Rosei's word), not
divergent.
\switchcolumn
\colstep{Onset}
At $\hw=\EgL$ exactly, with
$\cJ_L\propto\sqrt{\hw-\EgL}$; the inverse-square-root weight sits on
the onset edge itself, which is why the $L$ edge is sharp and strong.

\end{paracol}

\vspace{1em}
\bigskip
\noindent
\textbf{Punchline.}  The same machinery, forked only by two signs,
lands on two very different absorption edges.  At $L$ the $1/\kpar$
divergence of $\Dlu$ sits on the \emph{onset} edge itself, so
absorption switches on sharply and strongly at $\EgL=2.45$ eV.  At
$X$ the divergence sits at the \emph{top} of the window, far from
onset; the onset itself is a soft, step-like rise near $1.83$ eV with
a geometric sub-gap tail. One interband edge that is really two ---
soft at $X$, sharp half an eV above it at $L$ --- and that is exactly
the ``splitting of the interband absorption edge'' of the 1975 title.

\begin{remark}[The $L$ level and the Fermi-surface neck]\label{rem:neck}
Rosei's qualitative discussion attributes the strength of the $L$
singularity to the onset CEDS being tangent to the Fermi surface along
the neck --- which requires $L_6^-$ \emph{below} $E_F$.  The fitted
scheme ($\EgL=2.45$, $\wLl=1.56\Rightarrow\wLu=+0.89$ eV) puts the
whole $L$ window \emph{above} $E_F$, making the $L$ channel inert
through the Fermi factor.  Both statements cannot hold in one
parabolic model; the fitted scheme is what the code implements, and
the tension is recorded here rather than papered over.
\end{remark}

% ---------------------------------------------------------------------
## The $X$ mass fork: sign of $\Bb_X$ {{label:sec:fork}}
% ---------------------------------------------------------------------

One assignment at $X$ I am not sure of, flagged because it flips a
sign.  First, where the masses come from: they are not printed as
numbers anywhere --- they are read off the band diagram of C\&S
(Fig.~5), by fitting a parabola to the printed $E(\mathbf k)$ curves
around $X$, along $\Delta$ and in the face, and taking
$m=\hbar^2(\dd^2E/\dd k^2)^{-1}$.  Rosei's masses come from exactly
the same source (``the optical masses and the gaps\ldots were taken
from Ref.~4'', his Ref.~4 being C\&S), so the two readings of the same
figure ought to agree.  They do not: my extraction gives
$m_{u\parallel}=0.40$, $m_{l\parallel}=0.15$ --- the \emph{opposite}
$\parallel$ ordering to Rosei's, hence $\Bb_X>0$.  On that branch the
sub-gap picture changes: the integration window becomes \emph{closed}
--- finite at both ends by geometry, as at $L$ --- instead of Rosei's
bottomless, occupation-cut window; there is no geometric sub-gap tail,
and the onset is a $\sqrt{\hw-\EgX}$ rise sitting exactly at the gap
(any observed tail below $1.94$ eV would then be broadening only, and
the $-20\kB T$ floor would overshoot the true, geometric one).

Two facts keep the fork contained:
\begin{itemize}
\item Above the gap the branches are \emph{indistinguishable}: same
      line shape, same singular edge.  The $\parallel$ masses enter
      only through $\cF_X$, and the fit lumps $\cF_X$ into
      $S_X=\cF_X|P_X|^2$ --- so no fit to $\eps_2$ data can tell the
      branches apart; only sub-gap behaviour or the extracted
      $|P_X|^2$ could.  (The above-gap window slope $A_u/\Ab_X$ ---
      $0.62$ on Rosei's assignment, $0.38$ on mine --- is set by the
      $\perp$ masses, a separate assignment.)
\item Either ordering makes the $d$ band the \emph{lighter} one along
      $\Delta$, which goes against the flat-$d$ prior --- so the
      likeliest culprit is a transcription swap in my own mass table,
      not new physics.
\end{itemize}

\noindent\textbf{Bottom line: until C\&S Fig.~5 is re-measured, this
document follows Rosei's branch ($\Bb_X<0$) everywhere, and quotes the
branch wherever it matters.}

% =====================================================================
# Assembled $\eps_2$
\label{sec:eps2}
% =====================================================================

Insert the EDJDOS ($4'$) into the FGR form \eqref{eq:star}.  The
bridge is the definition of $\Dlu$ itself, Eq.~\eqref{eq:sort}: the
$(2\pi)^3$ cancels, and with spin (the explicit 2) and the
half-neighborhood counts $N_X=6$, $N_L=8$,
\begin{equation}
\eps_2(\hw,T)=\frac{4\pi^2e^2\hbar^2}{3m^2\omega^2}\cdot2\cdot
\sum_{i=X,L}N_i\,|P_i|^2\,\cJ_i(\hw,T),
\end{equation}
which tidies to Rosei's second headline equation, with no leftover
constant:
\begin{equation}
\boxed{\;
\eps_2(\hw,T)=\frac{8\pi^2e^2\hbar^4}{3m^2(\hw)^2}
\sum_{i=X,L}N_i\,|P_i|^2\,\cJ_i(\hw,T)
\;}
\tag{9}
\label{eq:eps9}
\end{equation}
(Rosei leaves the $N_i$ implicit, so the fitted $|P_i|^2$ really means
$N_i|P_i|^2$ up to normalization --- harmless for the quoted ratio).
That clean landing needs three things at once: $|P|^2$ is the squared
gradient element \eqref{eq:Pdef}; $\Dlu$ is ($4'$), not the printed
(4); spin and $N_i$ are kept where shown.  The quantities the data
actually fix are the strengths
\begin{equation}
S_X=\cF_X|P_X|^2,\qquad S_L=\cF_L|P_L|^2,
\tag{10}
\label{eq:S10}
\end{equation}
with $|P_X/P_L|^2=0.370$ from the fit to Johnson--Christy; under the
corrected ($4'$) the fitted combination maps onto the printed $S_i$
through exactly the constant $2\cF_i/\hbar^2$ of
Sec.~\ref{sec:kernel} --- every published number keeps its meaning.

Fully substituted --- the explicit integral a computer evaluates ---
($4'$) into (9), the $\hbar^4$'s cancelling:
\begin{equation}
\boxed{\;
\eps_2(\hw,T)=\frac{2e^{2}}{3m^{2}(\hw)^{2}}
\sum_{i=X,L}N_i\,\cF_i^{2}\,|P_i|^{2}
\int_{E_{\min}^{(i)}}^{E_{\max}^{(i)}}
\frac{1-\fFD(E,T)}{\kpar^{(i)}(E,\hw)}\,\dd E
\;}
\tag{11}
\label{eq:eps11}
\end{equation}
with $\kpar^{X}$ from ($6'$), $\kpar^{L}$ from its $L$ twin (same
bracket, every slot sign-reversed), and windows:

\begin{center}
\small
\begin{tabular}{lccl}
\toprule
 & $E_{\min}$ & $E_{\max}$ & edge behaviour\\
\midrule
$X$, $\hw\ge\EgX$ & $-20\kB T$ (occupation) &
$\wXu+\frac{A_u}{\Ab_X}(\hw-\EgX)$ & $1/\sqrt{\;}$ at $E_{\max}$\\
$X$, $\hw<\EgX$ & $-20\kB T$ (occupation) &
sub-gap line of ($8'$) & finite everywhere\\
$L$, $\hw\ge\EgL$ & $\wLu+\frac{A_u}{\Ab_L}(\hw-\EgL)$ &
$\wLu+\frac{B_u}{\Bb_L}(\hw-\EgL)$ & $1/\sqrt{\;}$ at $E_{\min}$\\
$L$, $\hw<\EgL$ & --- & --- & no states\\
\bottomrule
\end{tabular}
\end{center}

\medskip
\noindent\textbf{Domain of validity --- where is $k_{\max}$?}
The parabolic bands \eqref{eq:bands} and the constant $|P_i|^2$ hold
only near the critical points; Rosei sizes the trusted region as
${\sim}(\pi/10a)^3$ (matrix-element constancy, his Sec.~IV), while his
Figs.~3 and 5 draw the CEDS out to $k\sim2\times\pi/4a$.  Yet none of
the windows above carries an explicit $k_{\max}$ --- they encode CEDS
geometry and occupation only.  This is faithful to the paper: Rosei
polices locality through the \emph{photon energy} instead, fitting
only to 2.7 eV --- ``only limited regions in $K$ space around $X$ and
around $L$ are involved \dots\ when the fitting is extended a few
tenths of an eV above the absorption edge'', while ``the danger of
counting transitions twice and of a breakdown of our approximations''
(both channels are band-5\,$\to$\,band-6) ``may therefore arise at
higher photon energies''.  The numbers behind that policy, with the
parameters below ($a_{\rm Au}=4.08$~\AA, so
$\pi/4a=0.19$~\AA$^{-1}$):
\begin{itemize}
\item \emph{$L$ is safely local}: the CEDS ellipsoid lies entirely
      inside $|\mathbf k|\le\pi/4a$ for
      $\hw-\EgL\le\Ab_L(\pi/4a)^2\simeq0.79$ eV, i.e.\ up to
      $\hw\simeq3.2$ eV --- the whole fit range (inside $\pi/10a$ only
      for $\hw\lesssim2.6$ eV).
\item \emph{$X$ is marginal by construction}: the occupied edge of the
      window ($E\simeq E_F$, where the Fermi step sits) lies at
      $|\mathbf k|\simeq(0.8\text{--}1.5)\times\pi/4a$ for
      $\hw=2.0$--$2.7$ eV --- several times the strict
      constant-$|P|^2$ radius, and exactly the scale of Rosei's own
      figures.  The $-20\kB T$ floor is an \emph{occupation} cutoff,
      not a locality one --- it maps to $|\mathbf k|$ up to
      ${\sim}1.9\times\pi/4a$ --- but in equilibrium everything beyond
      the Fermi step carries $[1-\fFD]\approx0$, so the occupation
      acts as the de facto $k$-cutoff.  Nothing in the model
      \emph{checks} this.
\end{itemize}
Operationally: trust the model where Rosei did, $\hw\lesssim2.7$ eV;
above that, locality and single-counting fail together.  Out of
equilibrium the occupation excuse at $X$ weakens --- see the locality
guard in Sec.~\ref{sec:numerics}.

\medskip
\noindent\textbf{Parameters} (levels: Rosei's fit; masses: C\&S, the
$X$ row on Rosei's branch, subject to Sec.~\ref{sec:fork}; $\cF$ in
units of the free-electron mass $m$; $\cD$ in units $(\hbar^2/2m)^2$):

\begin{center}
\small
\begin{tabular}{lccccccc}
\toprule
 & $\Eg$ (eV) & upper level (eV) & lower level (eV)
 & $m_{u\perp}$ & $m_{u\parallel}$ & $m_{l\perp}$ & $m_{l\parallel}$\\
\midrule
$X$ & 1.94 & $\wXu=0.17$ & $\wXl=1.77$ & 0.19 & 0.15 & 0.31 & 0.40\\
$L$ & 2.45 & $\wLu=0.89$ & $\wLl=1.56$ & 0.24 & 0.12 & 0.70 & 1.03\\
\bottomrule
\end{tabular}

\medskip
\begin{tabular}{lcccc}
\toprule
 & $\cD$ & $\cF/m$ & window slopes & singular edge\\
\midrule
$X$ & $+34.7$ & 0.170 & $E_{\max}$ (above gap): 0.62 & upper ($\kpar\to0$)\\
$L$ & $-7.86$ & 0.357 & $E_{\min}$: 0.745,\ $E_{\max}$: 0.896 & lower ($\kpar\to0$)\\
\bottomrule
\end{tabular}
\end{center}

\medskip
\noindent\textbf{Scorecard --- the ten equations, one by one:}

\begin{center}
\small
\begin{tabular}{llll}
\toprule
Rosei & here & status & issue as printed\\
\midrule
(1)  & (1)    & recreated & ---\\
(2)  & (2)    & recreated & ---\\
(3)  & (3)    & recreated & ---\\
(4)  & ($4'$) & \textbf{suggested fix} &
prefactor $(8\pi^2\hbar^2)^{-1}\cF\to(4\pi^2\hbar^4)^{-1}\cF^2$;
off by const.\ $2\cF/\hbar^2$\\
(5)  & (5)    & recreated & ---\\
(6)  & ($6'$) & \textbf{suggested fix} & dimensionally impossible as printed\\
(7)  & (7)    & recreated & ---\\
(8)  & ($8'$) & \textbf{suggested fix} &
$m_{u\parallel}\leftrightarrow m_{l\parallel}$ subscripts swapped\\
(9)  & (9)    & recreated & $N_i$ made explicit\\
(10) & (10)   & recreated & absorbs the (4) constant; see App.~\ref{app:dict}\\
\bottomrule
\end{tabular}
\end{center}

% ---------------------------------------------------------------------
## Discrepancies \& suggested corrections {{label:sec:grw}}
% ---------------------------------------------------------------------

\noindent\textbf{At issue: the printed Eqs.~(4), (6) and (8) of the
1975 paper.}  None of the three comes out of the rederivation as
printed --- and none of the three failures touches a published number.
Each failure stated simply, then fixed.

\medskip
\textbf{Eq.\ (4).}  Printed:
$\Dlu=(8\pi^2\hbar^2)^{-1}\,\cF_{l\to u}\,\kpar^{-1}$.
\emph{Why it fails:} the definition of $\Dlu$ (Eq.~\eqref{eq:sort})
leaves nothing to choose --- the reduction of
Sec.~\ref{sec:kernel} gives $(16\pi^2|\cD|)^{-1}\kpar^{-1}
=\cF^2/(4\pi^2\hbar^4\kpar)$, Eq.~($4'$), and with the gradient
convention for $|P|^2$ only ($4'$) makes \{(4),(9)\} dimensionally
consistent and lands (9) with no leftover constant.  The printed form
is off by
\begin{equation}
\frac{\text{printed (4)}}{\text{correct }(4')}=\frac{2\cF_{l\to u}}{\hbar^2},
\end{equation}
a pure constant per critical point --- it cannot bend a line shape,
and it is absorbed once and for all into the fitted $S=\cF|P|^2$ of
Eq.~(10).  That is why the slip is easy to miss and costs nothing
physically; but the assembly only closes into (9) if ($4'$) is used.

\medskip
\textbf{Eq.\ (6).}  Printed:
\begin{equation}
\kpar=\Bigl(\hw-\wXl+\frac{\hbar^{2}}{2m_{l\perp}}(\wXu-E)
-\frac{\hbar^{2}}{2m_{u\perp}}E\Bigr)^{1/2}.
\tag{6, as printed}
\end{equation}
\emph{Why it fails:} a wavevector is set equal to the square root of a
sum of \emph{energies}, and inside the bracket a bare energy is added
to $(\hbar^2/2m)\times$energy terms --- mismatched units throughout;
the coefficients read $\hbar^2/2m$ where $2m/\hbar^2$ is needed for
the bracket to come out as length$^{-2}$.  Three small fixes turn it
into ($6'$): square the left-hand side; invert the coefficients and
pull out the overall $2\cF^2/\hbar^2$; restore the missing
$1/m_{u\perp}$ on the first term.  The three numerator slots of
\begin{equation}
\kpar^{2}
=\frac{2\cF_X^{2}}{\hbar^{2}}\Bigl[
\frac{\hw-\wXl-E}{m_{u\perp}}
+\frac{\wXu-E}{m_{l\perp}}\Bigr]
=\frac{A_u(\hw-\EgX)-\Ab_X(E-\wXu)}{\cD_X}
\tag{6$'$}
\end{equation}
then line up with the print term by term --- confirmation that ($6'$)
is what was meant: a typo, but a disabling one, since the printed
formula is unusable as written.

\medskip
\textbf{Eq.\ (8).}  Printed:
$E_{\max}=\wXu+(\EgX-\hw)\,m_{u\parallel}/(m_{l\parallel}-m_{u\parallel})$.
Solving the model for the $\kperp=0$ edge gives
\begin{equation}
E_{\max}
=\wXu+(\EgX-\hw)\,\frac{m_{l\parallel}}{m_{u\parallel}-m_{l\parallel}},
\tag{8$'$}
\end{equation}
i.e.\ the printed equation has $m_{u\parallel}$ and $m_{l\parallel}$
interchanged --- one consistent swap, specific to (8): the subscripts
of (6) are \emph{not} swapped, so it is not the same slip repeated.
\emph{The tell:} on Rosei's own branch $m_{u\parallel}<m_{l\parallel}$,
the printed denominator is positive and sends $E_{\max}$ \emph{above}
$\wXu$ as $\hw$ drops below the gap --- but the sub-gap CEDS has no
states up there.  ($8'$) puts the sub-gap edge sensibly \emph{below}
$\wXu$, which is what makes the tail (and the $1.83$ eV step onset)
work.  On the alternative branch of Sec.~\ref{sec:fork}
($\Bb_X>0$), the same algebraic edge is instead the \emph{lower}
window limit.

% ---------------------------------------------------------------------
## The Drude term: completing $\eps_2$ {{label:sec:drude}}
% ---------------------------------------------------------------------

Everything above is interband.  The measured $\eps_2$ of gold also
contains the free-carrier (intraband) response, which the Rosei model
deliberately leaves out --- so to compare with data, or to fit, it has
to be added back.  The Drude dielectric function
$\eps(\omega)=\eps_\infty-\omega_p^2/[\omega(\omega+i\gamma)]$ gives
\begin{equation}
\eps_2^{\rm D}(\omega)
=\frac{\omega_p^{2}\,\gamma}{\omega\,(\omega^{2}+\gamma^{2})}
\;\;\xrightarrow{\;\omega\gg\gamma\;}\;\;
\frac{\omega_p^{2}\,\gamma}{\omega^{3}} ,
\label{eq:drude}
\end{equation}
and in the optical window the high-frequency limit is all that is
needed: for Au, $\hbar\omega_p\simeq9.0$ eV and
$\hbar\gamma\simeq0.07$ eV, so $\omega\gg\gamma$ holds everywhere
above $\sim\!1$ eV (the fit code implements exactly this
$A_{\rm D}/\omega^3$ form, $A_{\rm D}=\omega_p^2\gamma\simeq5.7$
eV$^3$).  The total is a plain sum of channels:
\begin{equation}
\boxed{\;
\eps_2(\hw,T)
=\eps_2^{\rm D}(\omega)
+\frac{8\pi^2e^2\hbar^4}{3m^2(\hw)^2}
\sum_{i=X,L}N_i\,|P_i|^2\,\cJ_i(\hw,T)
\;}
\label{eq:total}
\end{equation}
The Drude part falls as $\omega^{-3}$ and carries no interband
structure: below the $X$ onset it \emph{is} $\eps_2$, through the edge
region it is a smooth declining background, and the temperature
dependence of the edge sits entirely in the $\cJ_i$.

% =====================================================================
# Photonic density of states and the emission counterpart
\label{sec:photonic}
% =====================================================================

## Mode counting

Periodic quantization in volume $V$: two transverse polarizations,
$\omega=cq$:
\begin{equation}
\rho(\omega)\,\dd\omega
=\frac{2}{V}\,\frac{V}{(2\pi)^3}\,4\pi q^2\,\dd q
\quad\Longrightarrow\quad
\boxed{\;\rho(\omega)=\frac{\omega^2}{\pi^2c^3}\;}
\label{eq:rhophot}
\end{equation}
modes per unit volume per unit angular frequency.  In a transparent
host of index $n$, $c\to c/n$; in a structured environment
$\rho\to\rho(\mathbf r,\omega)$, the \emph{local} density of states
(Novotny \& Hecht) --- precisely the photonic factor of the PL
factorization used in this thesis.

## Spontaneous emission rate of one pair

FGR with the quantized field \eqref{eq:Aquant} at $n_q=0$, summed over
modes, using
$\sum_\lambda\int\dd\Omega_q|\hat{\bm\eps}_\lambda\!\cdot\!\pul|^2
=\tfrac{8\pi}{3}|\pul|^2$ and $|\pul|^2=\hbar^2|P|^2$:
\begin{equation}
\boxed{\;
W_{\rm sp}(\omega)
=\frac{4e^2\,\omega\,\hbar\,|P|^2}{3m^2c^3}
=\underbrace{\frac{4\pi^2e^2\hbar\,|P|^2}{3m^2\omega}}_{\text{matter}}
\times\underbrace{\frac{\omega^2}{\pi^2c^3}}_{\rho(\omega)}
\;}
\label{eq:Wsp}
\end{equation}
--- the vacuum Einstein-$A$ rate in the
$\mathbf A\!\cdot\!\mathbf p$ form.  The factorization into a matter
part times $\rho(\omega)$ is exact and is the microscopic origin of
the LDOS $\times$ electronic split assumed in Chapter 2.

Why $1/\omega$ in the matter part here, when the absorption prefactor
of \eqref{eq:eps2exact} carries $1/\omega^2$?  Both rates contain the
identical vertex $(e/mc)^2|A|^2|M_{ul}|^2$; the different powers come
from what $|A|^2$ is normalized against.  In absorption, $\eps_2$ is
defined per unit \emph{classical field intensity}: expressing
$A_0=cE_0/\omega$ through the measured field costs two inverse powers
of $\omega$ (the $-2$ of Eq.~\eqref{eq:wcount}).  In spontaneous
emission there is no external field to normalize by; the reference
object is \emph{one photon per mode}, whose squared amplitude is fixed
by the field quantization \eqref{eq:Aquant} at $2\pi\hbar c^2/\omega
V$ --- a \emph{single} inverse power of $\omega$, the zero-point
amplitude of the mode.  The remaining $\omega$-dependence of
\eqref{eq:Wsp} is carried openly by the mode count
$\rho(\omega)\propto\omega^2$.  In short: same vertex, different
yardstick --- absorption is measured against $E_0^2$ (two powers),
emission against the vacuum fluctuation of one mode (one power).

## The interband PL spectrum and the Kirchhoff check

The emission weight is not a difference but a \emph{product}: the
upper level must be filled and the lower empty,
$\fFD(E)[1-\fFD(E-\hw)]$.  Summing \eqref{eq:Wsp} over pairs (spin 2,
$N$ half-neighborhoods, same $\Dlu$ and windows as in absorption):
\begin{equation}
\boxed{\;
R(\hw)=\rho(\omega)\,\frac{4\pi^2e^2\hbar\,|P|^2}{3m^2\omega}\,
2N\!\int\!\dd E\;
\fFD(E)\bigl[1-\fFD(E-\hw)\bigr]\,\Dlu(E,\hw)
\;}
\label{eq:PL}
\end{equation}
photons per unit time, volume and photon energy.  In equilibrium the
Fermi identity $[1-\fFD]/\fFD=\rme^{(E-\mu)/\kB T}$, applied at both
levels, collapses the product (detailed balance; only the
\emph{transition} energy survives):
\begin{equation}
\fFD(E)\bigl[1-\fFD(E-\hw)\bigr]
=n_B(\hw)\,\bigl[\fFD(E-\hw)-\fFD(E)\bigr],
\qquad n_B(x)=\frac{1}{\rme^{x/\kB T}-1},
\label{eq:BEcollapse}
\end{equation}
and since $[\fFD(E-\hw)-\fFD(E)]$ is Rosei's $[1-\fFD(E)]$ in the same
deep-$d$-band limit used throughout (Sec.~\ref{sec:occupation}), every
electronic factor of \eqref{eq:PL} maps onto (11) and the constants
collapse \emph{exactly}:
\begin{equation}
\boxed{\;
R(\hw)=\frac{\omega^3}{\pi^2\hbar c^3}\;\eps_2(\omega)\;n_B(\hw)
=\frac{\omega\,\rho(\omega)}{\hbar}\,\eps_2(\omega)\,n_B(\hw)
\;}
\label{eq:vRS}
\end{equation}
--- the van Roosbroeck--Shockley relation; per thermal photon,
emission over absorption is $\rme^{-\hw/\kB T}$: Kirchhoff.  That
\eqref{eq:eps9} and \eqref{eq:PL}, derived independently, satisfy
\eqref{eq:vRS} with no leftover constant is the strongest global check
that every prefactor in this document is right.

Out of equilibrium the collapse \eqref{eq:BEcollapse} fails --- it
used one shared $(\mu,T)$ at both levels --- and the ratio
$n_{\rm eff}(E,\hw)=\fFD(E)[1-\fFD(E-\hw)]/[\fFD(E-\hw)-\fFD(E)]$
retains genuine $E$-dependence: the emission line shape parts company
with $\eps_2$.  That deviation \emph{is} the non-equilibrium PL signal
this thesis is after; reproducing $n_{\rm eff}\to n_B$ under
$\fFD_{\rm FD}$ is a unit test, \emph{taking} it is throwing the
signal away.  In a structured environment,
$\rho(\omega)\to\rho(\mathbf r,\omega)$ in \eqref{eq:PL}.

% =====================================================================
# Numerics: evaluate in $\kpar$, not in $E$ {{label:sec:numerics}}
% =====================================================================

Groundwork for the implementation.  The $1/\sqrt{\;}$ edges of (11)
would force adaptive quadrature or endpoint-weighted rules --- but the
divergence is a pure coordinate artifact, manufactured in
Sec.~\ref{sec:kernel} when the smooth $\mathbf k$-space geometry was
re-parametrized by final energy.  One exact change of variable inside
the same 1D integral undoes it.  Take $k\equiv\kpar$ itself.  (Where
did $\kperp$ go?  Nowhere --- on the transition surface it is not an
independent variable.  With $\hw$ fixed, the constraint
$\Elu=\hw$ of \eqref{eq:Omega} slaves the perpendicular
coordinate, $\kperp^{2}=(\hw-\Eg-\Bb\kpar^{2})/\Ab$, exactly as $u$
was expressed through $v$ in \eqref{eq:uv}; substituting it into
$E=\hbar\omega_u(\mathbf k)$ of \eqref{eq:bands} leaves $E$ a function
of $\kpar$ alone, Eq.~\eqref{eq:Eofk} below --- $\kperp$ is
eliminated by the $\delta$-constraint, not set to zero.)  Then $E$ is
affine in $k^2$, so $\dd E=\mp(\mu_{i\perp}\hbar^2/\cF_i^2)\,k\,\dd k$
while $\Dlu\propto1/k$ --- the factors of $k$ cancel identically,
\begin{equation}
\Dlu\,\dd E=\mp\frac{\mu_{i\perp}}{4\pi^2\hbar^2}\,\dd\kpar ,
\end{equation}
i.e.\ $\kpar$ is (up to constants) the cumulative count of the
EDJDOS: integrating in $\kpar$ \emph{is} integrating in $E$ with the
known weight $\Dlu$ absorbed exactly into the node placement.
Eq.~(7) flattens to
\begin{equation}
\boxed{\;
\cJ_i(\hw,T)=\frac{\mu_{i\perp}}{4\pi^{2}\hbar^{2}}
\int_{k_1^{(i)}}^{k_2^{(i)}}
\bigl[1-\fFD\bigl(E_i(k),T\bigr)\bigr]\,\dd k
\;}
\qquad
\frac{1}{\mu_{i\perp}}\equiv\frac{1}{m_{u\perp}}+\frac{1}{m_{l\perp}},
\tag{12}
\label{eq:k12}
\end{equation}
\begin{equation}
E_i(k)=\underbrace{\hbar\omega_{i_6^-}
+\frac{\mu_{i\perp}}{m_{u\perp}}\bigl(\hw-\Eg^{i}\bigr)}_{\kpar=0\
\text{intercept}}
\;\mp\;\frac{\mu_{i\perp}\hbar^{2}}{2\cF_i^{2}}\,k^{2}
\qquad(-\ \text{at }X,\ +\ \text{at }L),
\label{eq:Eofk}
\end{equation}
valid on both sides of the $X$ gap --- all the branch logic lives in
the limits.  These are the $u=0$/$v=0$ endpoints of
Sec.~\ref{sec:XL}, written out since an implementation touches them
first.  At $X$ (Rosei's branch):
\begin{equation}
k_1^{X}=
\begin{cases}
0, & \hw\ge\EgX,\\[8pt]
\dfrac{1}{\hbar}\Bigl[\dfrac{2(\EgX-\hw)\,m_{u\parallel}m_{l\parallel}}
{m_{l\parallel}-m_{u\parallel}}\Bigr]^{1/2}, & \hw<\EgX ,
\end{cases}
\qquad
k_2^{X}=\kpar^{X}(E_{\rm floor},\hw)\ \ \text{from ($6'$)},
\end{equation}
with $E_{\rm floor}=-20\kB T$ in equilibrium; for a pumped
distribution take $E_{\rm floor}=-(\hbar\omega_{\rm pump}+20\kB T)$
--- generosity is cheap, since below the true floor the integrand is
${\approx}\,0$.  At $L$ both limits are geometric:
\begin{equation}
k_1^{L}=0,\qquad
k_2^{L}=\frac{1}{\hbar}\sqrt{2\mu_{L\parallel}\bigl(\hw-\EgL\bigr)},
\qquad
\frac{1}{\mu_{L\parallel}}\equiv\frac{1}{m_{u\parallel}}
+\frac{1}{m_{l\parallel}} .
\end{equation}

No singularity survives: the integrand of (12) is a bounded, smooth
occupation profile whose only feature is the Fermi step of width
$\sim\kB T$.  \textbf{Recipe} (composite Simpson on a uniform grid is
entirely adequate):
\begin{enumerate}
\item $k=\mathrm{linspace}(k_1(\hw),\,k_2(\hw),\,N)$, $N$ odd;
\item integrand $1-\fFD(E_i(k))$ --- Fermi--Dirac in equilibrium,
      interpolation of a tabulated non-equilibrium distribution
      otherwise (use a \emph{monotone} interpolant, e.g.\ PCHIP, to
      avoid overshoot at the distribution's kinks);
\item \texttt{simpson(y, x=k)}, times $\mu_{i\perp}/4\pi^2\hbar^2$;
      then into (9).
\end{enumerate}
Measured accuracy (equilibrium, $\hw=2.4$ eV, against a converged
reference): $X$ reaches $5\times10^{-10}$ relative error at $N=101$
and machine precision by $N=201$; the $L$ integrand in equilibrium is
constant across the window (Remark~\ref{rem:neck}), and even a hot
2000 K distribution gives $3\times10^{-14}$ at $N=101$.  By contrast,
uniform-grid Simpson in $E$ on a singular edge stalls near $10^{-2}$
even at $N=6401$ ($O(\sqrt h)$ decay).  Energy space \emph{done
properly} --- the substitution $t=\sqrt{E_{\rm edge}-E}$, or
Gauss--Jacobi with the $1/\sqrt{\;}$ weight --- is bit-identical to
(12), because $t\propto\kpar$ exactly: the geometry had already named
the correct quadrature variable.  Hence the division of labor:
\emph{derive and reason in $E$; evaluate in $\kpar$.}

\vspace{1em}
\textbf{Practical points.}
\begin{itemize}
\item \emph{Resolve the step}: the only feature sits at
      $k_{\rm step}=k(E{=}0)$, trivially located since $E_i(k)$ is
      affine in $k^2$; at low $T$ either raise $N$ or split the
      interval there and Simpson each panel.
\item \emph{Respect the kinks} of a pumped distribution: slope
      discontinuities at $E_F\pm\hbar\omega_{\rm pump}$ are
      \emph{distribution} features no variable change removes --- put
      panel boundaries at their images $k(E_F\pm\hbar\omega_{\rm pump})$.
\item \emph{Vectorize over $\hw$}: build
      $k=k_1[:,\!None]+(k_2-k_1)[:,\!None]\,\xi[None,:]$ with $\xi$
      uniform on $[0,1]$ and Simpson along the last axis --- the whole
      spectrum in one call.  Gauss--Legendre with 48--64 nodes does
      the same job with fewer points if node count matters.
\item \emph{Cache the geometry}: $k_{1,2}$, $E_i(k)$ and the grid
      depend on $(\hw)$ only --- not on $T$ or on the distribution ---
      so precompute them once and sweep temperatures/pump powers
      cheaply (this is what makes fitting fast).
\item \emph{Locality guard}: nothing in (12) knows where the parabolic
      neighbourhood ends --- compare $k_2(\hw)$ with
      $\pi/4a\simeq0.19$~\AA$^{-1}$ (Sec.~\ref{sec:eps2}).  In
      equilibrium the $X$ integrand dies of occupation before locality
      does; a pumped distribution re-weights exactly those deep-window
      nodes, and the generous floor pushes $k_2$ to
      ${\sim}2\times\pi/4a$.  Report the fraction of (12) accrued at
      $k>\pi/4a$ and distrust spectra where it is not small.
\item \emph{Error control}: recompute at $2N$ and compare (one
      doubling).
\item \emph{Emission}: the PL integrand \eqref{eq:PL} swaps
      $[1-\fFD]\to \fFD(E)[1-\fFD(E-\hw)]$ in the same quadrature ---
      geometry, windows and nodes unchanged.
\end{itemize}

\textbf{Built-in checks.}
(i) \emph{Empty-window arithmetic}: wherever the occupation factor is
$\equiv1$ across the window,
$\cJ_i=\frac{\mu_{i\perp}}{4\pi^2\hbar^2}(k_2-k_1)$ exactly; at $L$
with $T\to0$ this is the textbook $M_0$ onset
$\cJ_L=\frac{\mu_{L\perp}}{4\pi^2\hbar^2}
\sqrt{(\hw-\EgL)/\Bb_L}$ in closed form.
(ii) \emph{Two-forms agreement}: (11) by adaptive quadrature (endpoint
declared) and (12) by Simpson must agree to quadrature accuracy at
every $(\hw,T)$ --- a one-line unit test.
(iii) \emph{Kirchhoff}: with $\fFD=\fFD_{\rm FD}$, confirm
$n_{\rm eff}(E,\hw)\to n_B(\hw)$ independent of $E$
(Sec.~\ref{sec:photonic}).

% =====================================================================
\appendix
% =====================================================================
# Conventions {{label:sec:conv}}

Fixed once here, used silently throughout the document.

\begin{center}
\begin{tabular}{ll}
\toprule
Units & Gaussian throughout (Rosei's system); SI conversions noted where useful.\\
Energy zero & Fermi level, $E_F=0$; all electron energies $E$ from $E_F$.\\
Bands & $u$ = upper (conduction), $l$ = lower ($d$); Rosei's subscripts.\\
Levels \& masses & $\wXu,\wXl,\wLu,\wLl$ and $m_{u\perp},m_{u\parallel},
                   m_{l\perp},m_{l\parallel}$ are all\\
                 & \emph{positive numbers}; curvature directions and the side
                   of $E_F$ are carried\\
                 & only by explicit $\pm$ signs, never hidden in a symbol.\\
Band coefficients & $A_i=\hbar^2/2m_{i\perp}$, $B_i=\hbar^2/2m_{i\parallel}$,
                    $i=u,l$; all $A_i,B_i>0$.\\
Interband energy & $\Elu(\mathbf k)\equiv\hbar\omega_u-\hbar\omega_l$;
                   Rosei's $\Omega_{lu}=\Elu-\hw$, the CEDS being
                   $\Omega_{lu}=0$.\\
Local axes & $\kpar$ along $\Gamma X$ (resp.\ $\Gamma L$), $\kperp$ radial in
             the perpendicular plane;\\
           & $\mathbf{k}$ measured from the critical point.\\
Spin & carried explicitly as a factor 2, never absorbed silently.\\
Counting & $N$ counts equivalent \emph{half}-neighborhoods
           ($N_X=6$ faces, $N_L=8$),\\
         & paired with the half-space $\Dlu$ below --- or a factor 2 goes
           missing.\\
Occupation & Rosei's $[1-\fFD(E,T)]$, $\fFD(E)=[\rme^{E/\kB T}+1]^{-1}$;
             see Sec.~\ref{sec:occupation}.\\
Matrix element & $|P|^2\equiv|\langle u|\nabla|l\rangle|^2$
                 (dimension length$^{-2}$), Rosei's convention;\\
               & momentum form $|\pul|^2=\hbar^2|P|^2$.\\
Photon & energy $\hw$, wavevector $\mathbf{q}$, polarization
         $\hat{\bm{\eps}}_\lambda$.\\
\bottomrule
\end{tabular}
\end{center}

# Dictionary of conventions across the repository {{label:app:dict}}

\begin{center}
\footnotesize
\setlength{\tabcolsep}{4pt}
\begin{tabular}{lllll}
\toprule
Document & upper band & lower band & $\Bb$ & status\\
\midrule
Rosei 1975; this doc ($X$) &
$+A_u\kperp^2-B_u\kpar^2$ & $-A_l\kperp^2-B_l\kpar^2$ &
$B_l-B_u$ & canonical\\
\emph{Equivalence} note ($X$) &
$+A_u\kperp^2+B_u\kpar^2$ & $-A_l\kperp^2+B_l\kpar^2$ &
$B_u-B_l$ & same $\cD$ (sign-robust)\\
A8 / A8.L &
$+A_c u-B_c v$ & $-A_v u-B_v v$ & $B_v-B_c$ &
A8 ok$^{(a)}$; A8.L wrong at $L$$^{(b)}$\\
\texttt{interband\_derivation\_v2} & mixed & mixed & --- &
internally inconsistent$^{(c)}$\\
\bottomrule
\end{tabular}
\end{center}
{\footnotesize
$^{(a)}$ A8's $\mathcal{E}_{\min}$ denominator $(B_v{+}B_c)$ is the
$s{=}{+}1$ formula; for its own $X$ conventions it should be
$\Bb=B_v{-}B_c$.\quad
$^{(b)}$ A8.L models the $L$ conduction band as a saddle ($-B_c$);
C\&S give $m_{u\parallel}^L=+0.12$: it is a minimum, $s=+1$.\quad
$^{(c)}$ v2 asserts $\Bb>0$ \emph{and} a geometric sub-gap tail
(requires $\Bb<0$), and labels $L$ as M$_1$.}

\medskip
\noindent\textbf{Normalizations.}  Earlier repo documents use the
full-neighborhood, no-$(2\pi)^3$ kernel
$K(E,\hw)=\int\dd^3k\,\delta\delta$ and the half-line measure
$\mathcal J_{\rm eq}$ of the \emph{Equivalence} note; with $\Dlu$ from
($4'$),
\begin{equation}
K=2\,(2\pi)^3\,\Dlu,\qquad
\mathcal J_{\rm eq}=\tfrac12 K,\qquad
\text{printed (4)}=\frac{2\cF}{\hbar^2}\times(4') .
\end{equation}
Matrix elements: Rosei's $|P|^2$ is the squared \emph{gradient}
element, related to the SI momentum element by
$|\pul|^2=\hbar^2|P|^2$.  With these two conventions --- ($4'$) and
gradient $|P|^2$ --- Rosei's Eq.~(9) is exact as printed; no residual
constant needs to be hidden in $|P|^2$, and only the strengths
$S=\cF|P|^2$ of Eq.~(10) are fixed by the data (the printed-(4)
constant reshuffles $\Dlu$, $\cF$, $|P|^2$ among themselves without
touching $S$).

# Dimensional audit (Gaussian) {{label:app:dim}}

$[\,e^2\,]={\rm erg\,cm}$, $[\,|P|^2\,]={\rm cm^{-2}}$,
$[\,A_i\,]=[\,B_i\,]={\rm erg\,cm^2}$, $[\,\cD\,]={\rm erg^2cm^4}$,
$[\,\cF\,]={\rm g}$, $[\,\Dlu\,]={\rm erg^{-2}cm^{-3}}$,
$[\,\cJ\,]={\rm erg^{-1}cm^{-3}}$.
\begin{itemize}
\item ($4'$): $\cF^2/\hbar^4\kpar\sim
{\rm g^2}/({\rm erg^4s^4\,cm^{-1}})={\rm erg^{-2}cm^{-3}}$ ---
states per volume per (energy)$^2$, as a double-$\delta$ measure must
be. \checkmark
\item (9): $\dfrac{{\rm erg\,cm}\cdot{\rm erg^4s^4}}
{{\rm g^2}\,{\rm erg^2}}\cdot{\rm cm^{-2}}\cdot
{\rm erg^{-1}cm^{-3}}=1$ (using ${\rm erg\,s^2=g\,cm^2}$). \checkmark
\item (12): $\mu_\perp/\hbar^2\times[k]\sim
{\rm g\,cm^{-1}}/{\rm erg^2s^2}={\rm erg^{-1}cm^{-3}}=[\cJ]$. \checkmark
\item \eqref{eq:rhophot}: $[\rho]={\rm s\,cm^{-3}}$. \checkmark
\item \eqref{eq:Wsp}: $\dfrac{{\rm erg\,cm}\cdot{\rm s^{-1}}\cdot
{\rm erg\,s}\cdot{\rm cm^{-2}}}{{\rm g^2\,cm^3s^{-3}}}
={\rm erg^2\,cm^{-1}}/({\rm g^2cm^3s^{-3}}\,{\rm s})
={\rm s^{-1}}$. \checkmark
\item \eqref{eq:PL}: $[\rho]\cdot[\text{matter}]\cdot[\cJ]
={\rm s\,cm^{-3}}\cdot{\rm cm^3s^{-2}}\cdot{\rm erg^{-1}cm^{-3}}
={\rm erg^{-1}cm^{-3}s^{-1}}$ --- photons per time, volume and photon
energy. \checkmark
\item \eqref{eq:vRS}: $[\omega\rho/\hbar]
={\rm erg^{-1}cm^{-3}s^{-1}}$, times dimensionless
$\eps_2n_B$. \checkmark
\end{itemize}

# References {{starred}}
\begin{itemize}
\item M.~Guerrisi, R.~Rosei, P.~Winsemius,
\emph{Splitting of the interband absorption edge in Au},
Phys.\ Rev.\ B \textbf{12}, 557 (1975) --- the paper recreated here
($X$ derived, $L$ delegated); source of the $X$-point dispersion
relations, Eqs.~(1)--(2).
\item R.~Rosei, \emph{Temperature modulation of the optical
transitions involving the Fermi surface in Ag: theory},
Phys.\ Rev.\ B \textbf{10}, 474 (1974) --- the $L$ machinery (and the
EDJDOS recipe) the 1975 paper borrows; source of the $L$-point
dispersion relations.
\item N.~E.~Christensen, B.~O.~Seraphin,
\emph{Relativistic band calculation and the optical properties of
gold}, Phys.\ Rev.\ B \textbf{4}, 3321 (1971) --- source of the
levels and masses (Rosei's Ref.~4).
\item P.~B.~Johnson, R.~W.~Christy,
\emph{Optical constants of the noble metals},
Phys.\ Rev.\ B \textbf{6}, 4370 (1972) --- the data the fit targets.
\item Y.~Sivan, Y.~Dubi, non-equilibrium electron distributions and
metal photoluminescence (2021), and refs.\ therein.
\item L.~Novotny, B.~Hecht, \emph{Principles of Nano-Optics},
2nd ed., Cambridge (2012) --- LDOS.
\end{itemize}

<!-- TEX-FOOTER (verbatim) -->
\end{document}

<!-- END-TEX-FOOTER -->
