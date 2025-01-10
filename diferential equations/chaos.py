import numpy as np
import matplotlib.pyplot as plt

def function_(x, r):
    return r * x * (1 - x)


def plot_chaos_function():
  r_values = np.linspace(3.5, 4, 100)
  x = 0.5
  values_to_plot = []

  for r in r_values:
        x = 0.5
        for i in range(150):
            x = function_(x, r)
            if i > 50:
              values_to_plot.append((r, x))

  values_to_plot = np.array(values_to_plot)
  print(values_to_plot)

  plt.figure(figsize=(7, 5))
  plt.plot(values_to_plot[:, 0], values_to_plot[:, 1], 'ok', alpha=0.5, markersize=2)
  plt.title('Mapa logistico (caos)', fontsize=16)
  plt.xlabel('r', fontsize=14)
  plt.ylabel('x', fontsize=14)
  plt.show()

plot_chaos_function()