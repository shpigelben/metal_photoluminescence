numeric_var_eDOS will serve as a reference

# Intraband transitions

| stage | expression_a         | expression_b          | purpose                                         |
| ----- | -------------------- | --------------------- | ----------------------------------------------- |
| **1** | analytic_const_eDOS  | ==numeric_var_eDOS==  | establish validity of analytic approx           |
| **2** | ==numeric_var_eDOS== | numeric_iso_delta_e   | establish validity of delta approx in e-space   |
| **3** | ==numeric_var_eDOS== | numeric_iso_delta_k   | establish validity of delta approx in k-space   |
| **4** | ==numeric_var_eDOS== | numeric_aniso_delta_k | establish validity parabolic band approximation |
