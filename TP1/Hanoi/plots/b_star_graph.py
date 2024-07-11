import matplotlib.pyplot as plt

# Extracted data
disco_values = [4, 5, 6, 7, 8, 9, 10]
b_star_values = [1.2801186032286365, 1.1727727605342806, 1.103647779224384, 1.0604579609972051,
                 1.0344593311391217, 1.0193528544316608, 1.0107383547267907]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(disco_values, b_star_values, marker='o', linestyle='-', color='b')

# Add titles and labels
plt.title('Disco vs b*')
plt.xlabel('Disco')
plt.ylabel('b*')
plt.grid(True)

# Show the plot
plt.show()