# %%
from file_readwrite import Crystal_red_density

# %%
matrix_out = "/home/mra/simulaciones/h_basicTest/h_pmat.out"

# %%
red_dens_test = Crystal_red_density()

# %%
red_dens_test.read_cry_density(printout_output=matrix_out)

# %%
red_dens_test.n_g

# %%



