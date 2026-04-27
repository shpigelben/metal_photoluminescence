import nbformat

with open('code/main/2_RoseiAnalysis.ipynb', 'r') as f:
    nb = nbformat.read(f, as_version=4)

markdowns = [
    r"""This cell implements the theoretical models for interband transitions at the $X$ and $L$ symmetry points based on Rosei's analysis. 
The $X$-point transitions are modeled with a constant step-like joint density of states (JDOS) integrated over the thermal window, resulting in a linear rise. 
The $L$-point transitions are modeled using a standard 3D parabolic band edge, giving a JDOS proportional to $\sqrt{\hbar\omega - E_{band}}$, which is cut off by the Fermi-Dirac distribution near the Fermi level $E_{g,L}$.""",

    r"""This cell explores an alternative derivation assuming closed ellipsoidal surfaces (an $M_0$ critical point) for the $X$-transition. 
The derivation yields an integral of the form $\int \frac{1}{\sqrt{E_{\text{max}} - E}} f(E) dE$. 
By applying the substitution $u = \sqrt{E_{\text{max}} - E}$ to remove the singularity at the kinematic limit, the model computes a square-root rise in absorption, comparing it alongside the standard $L$-point model.""",

    r"""An interactive visualization of the user's analytical derivation for both the $X$ and $L$ transitions. 
It allows dynamical adjustment of the effective temperature $T$, matrix element scaling factors, onset energies ($E_{g,X}$, $E_{g,L}$), and band curvature ($m_{\text{ratio}}$) to explore their impact on the simulated imaginary dielectric function $\epsilon_2$ spectrum.""",

    r"""This cell computes the exact analytical forms for the interband transitions. 
The $L$-transition ($M_0$ topology) uses the exact JDOS proportional to $\sqrt{E}$ multiplied by the probability of an empty final state. 
The $X$-transition ($M_1$ topology) is approximated by a step-function JDOS integrated against the Fermi distribution. The components are summed and scaled by $1/(\hbar\omega)^2$ to yield the final $\epsilon_2$ profile.""",

    r"""Constructs a phenomenological tight-binding-like model of the energy difference surface $\Delta E(\mathbf{k}) = E_c(\mathbf{k}) - E_v(\mathbf{k})$ for gold. 
The model is tuned to reproduce the local minima at the $L$-points and saddle points at the $X$-points. 
The Constant Energy Difference Surface (CEDS) for a given photon energy $\hbar\omega$ is then computed via the marching cubes algorithm and visualized in 3D momentum space.""",

    r"""Utilizes the custom `RoseiLikeGoldModel` to compute and visualize the full band structure along the high-symmetry path $\Gamma-X-W-L-\Gamma$. 
Directional quadratic fits are performed around the $X$ and $L$ points to extract the corresponding effective masses ($m^*$) for the conduction ($c$) and valence ($v$) bands.""",

    r"""Generates an interactive 3D visualization of the Constant Energy Difference Surface (CEDS) at a specific photon energy $\hbar\omega = 2.5$ eV. 
It leverages the `RoseiLikeGoldModel` to accurately map the isosurface where vertical transitions $\Delta E(\mathbf{k}) = \hbar\omega$ are allowed, marking the $L$, $X$, and $\Gamma$ points for reference."""
]

new_cells = []
code_cell_idx = 0
for cell in nb.cells:
    if cell.cell_type == 'code':
        if code_cell_idx < len(markdowns):
            md_cell = nbformat.v4.new_markdown_cell(markdowns[code_cell_idx])
            new_cells.append(md_cell)
        code_cell_idx += 1
    new_cells.append(cell)

nb.cells = new_cells

with open('code/main/2_RoseiAnalysis.ipynb', 'w') as f:
    nbformat.write(nb, f)

print(f"Updated notebook with {code_cell_idx} code cells processed.")
