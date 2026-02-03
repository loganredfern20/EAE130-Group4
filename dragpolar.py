import numpy as np
import matplotlib.pyplot as plt

# --- Given Constants ---
AR = 2.80672
s = 59.88512 
s_ref = 1053.94
S_wet = 2255.877
c_f = 0.0040

# Calculate base C_D_0 from wetted area
C_D_0_calc = c_f * (S_wet / s_ref)
print(f"Calculated base Zero-lift drag coefficient (C_D_0): {C_D_0_calc:.5f}")

# --- Drag Polar Equations Implementation ---
# Define Lift Coefficient ranges for each configuration
cL_clean = np.linspace(-0.9, 0.9, 100)
cL_takeoff = np.linspace(-2.0, 2.0, 100)
cL_landing = np.linspace(-2.6, 2.6, 100)

# 1. Clean Configuration: CD = 0.01597 + 0.0406 * CL^2
clean_drag = 0.01597 + 0.0406 * cL_clean**2

# 2. Takeoff Flaps: CD = 0.02597 + 0.0433 * CL^2
# Note: Using your provided 0.02597 constant
takeoff_drag = 0.02597 + 0.0433 * cL_takeoff**2

# 3. Landing Flaps: CD = 0.07097 + 0.0464 * CL^2
landing_flaps_drag = 0.07097 + 0.0464 * cL_landing**2

# 4. Landing Gear: CD = 0.03097 + 0.0406 * CL^2
# (Calculated using the landing CL range)
landing_gear_drag = 0.03097 + 0.0406 * cL_landing**2

# --- Plotting ---
plt.figure(figsize=(10, 6))
plt.title('Aircraft Drag Polars - Multi-Configuration')
plt.xlabel("Drag Coefficient ($C_D$)")
plt.ylabel("Lift Coefficient ($C_L$)")

plt.plot(clean_drag, cL_clean, label='Clean', linestyle='-', linewidth=2)
plt.plot(takeoff_drag, cL_takeoff, label='Takeoff Flaps', linestyle='-', linewidth=2)
plt.plot(landing_flaps_drag, cL_landing, label='Landing Flaps', linestyle='-', linewidth=2)
plt.plot(landing_gear_drag, cL_landing, label='Landing Gear', linestyle='-', linewidth=2)

# Grid and Legend adjustments
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.legend(loc='lower right')

# Set x-limits to focus on the flight envelope
plt.xlim(0, 0.45) 
plt.tight_layout()

plt.show()