# TFLN
TFLN Waveguide Simulation Automation
This project automates finite-difference time-domain (FDTD) simulations of a thin-film lithium niobate (TFLN) waveguide under varying electric fields using Lumerical’s Python API.
Project Overview
The script simulates refractive index changes in a TFLN waveguide due to the electro-optic effect, extracts S-parameters, and compiles a reference table mapping electric field to refractive index. Results are visualized as a plot.
Key Features:

Configures a TFLN waveguide (500 nm width, 200 nm thickness) in Lumerical FDTD.
Sweeps electric fields (0–10 V/µm) to simulate electro-optic modulation.
Uses NumPy for data processing and Matplotlib for visualization.
Exports a CSV table (refractive_index_table.csv) and a plot (refractive_index_plot.png).

Relevance to QCi: Supports chip design and mode simulation tasks, producing data critical for photonic computing hardware development.
Installation

Python Setup:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install numpy matplotlib


Lumerical FDTD:
Install Lumerical FDTD (trial or academic license) from Ansys Lumerical.
Ensure the lumapi Python module is installed (included with Lumerical).



Usage
Run the script:
python TFLN_Waveguide_Simulation_Automation.py


Requirements: Lumerical FDTD and lumapi module.
Outputs:
refractive_index_table.csv: Table of electric field vs. refractive index.
refractive_index_plot.png: Plot of refractive index vs. electric field.



Dependencies

Python 3.8+
lumapi (Lumerical FDTD Python API)
numpy
matplotlib

Install Python dependencies:
pip install numpy matplotlib

Example Output

Table: refractive_index_table.csvE_field(V/m),n_eff
0.0,2.2100
2000000.0,2.2105
...


Plot: refractive_index_plot.png (shows refractive index vs. electric field).

Resources

Lumerical Python API Documentation
Ansys Lumerical FDTD Getting Started
NumPy Documentation
Matplotlib Documentation
YouTube: Lumerical Python API Tutorial


Contact
For questions, open an issue or contact [aryaputradas8@gmail.com].
