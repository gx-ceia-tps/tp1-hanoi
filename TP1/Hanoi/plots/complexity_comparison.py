import numpy as np
import matplotlib.pyplot as plt

# Constants
b = 3
b_star = 1.189496356

# Range for h
h = np.linspace(10, 500, 100)

# Functions
b_h = b ** h
b_star_h = b_star ** h
log_b_star_h_b_star_h = np.log(b_star_h) * b_star_h

# Plotting
plt.figure(figsize=(10, 6))

plt.loglog(h, b_h, label=r'$b^h$')
plt.loglog(h, b_star_h, linestyle='--', label=r'$(b^*)^h$')
# plt.loglog(h, log_b_star_h_b_star_h, label=r'$\log((b^*)^h) \cdot ((b^*)^h)$')

plt.xscale('linear')
plt.yscale('log')

plt.xlabel('h')
plt.ylabel('Values')
plt.title('Plot of $b^h$ and $(b^*)^h$')
plt.legend()
plt.grid(True)
plt.show()
