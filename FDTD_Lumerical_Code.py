import lumapi
import numpy as np
import matplotlib.pyplot as plt

# Initialize Lumerical FDTD session
fdtd = lumapi.FDTD()

# Define TFLN waveguide parameters
wavelength = 1.55e-6  # 1550 nm
width = 500e-9  # 500 nm
thickness = 200e-9  # 200 nm
n_TFLN = 2.21  # Refractive index of TFLN
r33 = 30e-12  # Electro-optic coefficient (m/V)

# Set up FDTD simulation
fdtd.addfdtd()
fdtd.set("x span", 10e-6)
fdtd.set("y span", 2e-6)
fdtd.set("z span", 2e-6)
fdtd.set("wavelength start", 1.5e-6)
fdtd.set("wavelength stop", 1.6e-6)

# Define waveguide
fdtd.addrect()
fdtd.set("name", "waveguide")
fdtd.set("x span", 8e-6)
fdtd.set("y span", width)
fdtd.set("z span", thickness)
fdtd.set("material", "LiNbO3")

# Sweep electric field and collect data
electric_fields = np.linspace(0, 10e6, 5)  # 0 to 10 V/µm
refractive_indices = []
s_parameters = []

for E in electric_fields:
    delta_n = 0.5 * n_TFLN**3 * r33 * E  # Electro-optic effect
    n_eff = n_TFLN + delta_n
    refractive_indices.append(n_eff)
    fdtd.set("index", n_eff)
    fdtd.run()
    s_matrix = fdtd.getsweepresult("monitor", "S_parameters")
    s_parameters.append(s_matrix)
    print(f"Simulated for E = {E/1e6:.2f} V/µm, n_eff = {n_eff:.4f}")

# Save reference table
table = np.column_stack((electric_fields, refractive_indices))
np.savetxt("refractive_index_table.csv", table, header="E_field(V/m),n_eff", delimiter=",")

# Plot results
plt.plot(electric_fields * 1e-6, refractive_indices, 'b-', label='Refractive Index')
plt.xlabel("Electric Field (V/µm)")
plt.ylabel("Effective Refractive Index")
plt.title("Electro-Optic Modulation in TFLN Waveguide")
plt.grid(True)
plt.legend()
plt.savefig("refractive_index_plot.png")
plt.show()

# Clean up
fdtd.close()
