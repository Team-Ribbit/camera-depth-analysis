import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create some data
np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)
hue = np.random.choice(['aaaaA', 'bbbbB'], 100)

print(hue)
exit(0)
# Create the plot
sns.scatterplot(x=x, y=y, hue=hue, palette={'aaaaA': 'red', 'bbbbB': 'blue'})

# Create proxy artists for legend
# red_dot = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Group A')
# blue_dot = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Group B')


# Combine proxy artists into legend
# plt.legend(handles=[red_dot, blue_dot])

plt.show()