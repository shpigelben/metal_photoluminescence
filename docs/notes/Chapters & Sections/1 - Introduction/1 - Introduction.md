- Total emission
	- usage of FGR and the valid field strengths.
	- photonic & electronic parts (when are they separable?).
	- ==focusing on bulk metals (photonic DOS is that of free space WHY? maybe electrons are free, photons inside metals will immediately get absorbed and reemitted)==
		- photonic modes propagate outside the metal, so the approximation holds but this leads to a different issue - absorption and emission happen only in skin-depth. When counting states in the transition from a single localized emitter to a bulk continuous metal we are summing over all of the metal's size. This shouldn't be the case. Instead we should compute an intrinsic specific emission (per unit volume).
		- Does the fact this happen only near the metal surface somehow modify the Bloch states due to surface effects?
___
# Introduction
*Luminescence* generally refers to the spontaneous emission of light (generally incoherent and omnidirectional) due to the decay of an electron which had been perturbed into an exited state. *Photoluminescence* (PL), which is the focus of this work, is one of many such phenomena where excitation is due to electromagnetic radiation.

==A better understanding of PL is requisite, apart from fundamental scientific inquiry, for interpreting **plasmon-assisted photocatalysis** and **hot photoluminescence**, ultimately finding utility in applications such as **nano-thermometry**.

When it comes to metals, PL predominantly takes place in the conduction band, in so called intraband transitions. Previous work by [Sivan & Dubi] calculated the steady-state distribution of electronic states in gold under continuous wave (CW) illumination, and consequently the intraband contribution to PL.

In this work, we wish to expand upon previous endeavors not only by calculating intraband PL following transient (pulsed) illumination, but also by quantifying interband contributions PL taking place between the conduction and valence bands.

- Do we focus on bulk metals or nano-particles this should have quantitative and qualitative effect on the result.
- Geometry and size are commonly thought of as affecting the photonic DOS, but nano-particles also modify electron behavior, broadening the amount of momentum states, potentially allowing for direct intraband transitions that are forbidden in bulk metals.

