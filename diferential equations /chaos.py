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

def logistic_map(steps, r_value):
    values_to_plot = []
    x = 0.1  # Valor inicial de x (entre 0 e 1)

    for c in range(steps):
        x = r_value * x * (1 - x)  # Função do mapa logístico
        values_to_plot.append((c, x))

    values_to_plot = np.array(values_to_plot)

    plt.figure(figsize=(10, 6))
    plt.plot(values_to_plot[:, 0], values_to_plot[:, 1], '-k', linewidth=1)
    plt.title(f'Logistic Map with r = {r_value}', fontsize=16)
    plt.xlabel('Iteration', fontsize=14)
    plt.ylabel('x', fontsize=14)
    plt.grid(True)
    plt.show()

def logistic_(r_value, initial_value=0.1, iterations=100):
    x = np.linspace(0, 1, 1000)
    y_logistic = r_value * x * (1 - x)  # Função logística
    y_identity = x  # Linha de identidade

    # Plot da função logística e da linha de identidade
    plt.plot(x, y_logistic, color="blue", label="Logística")
    plt.plot(x, y_identity, color="orange", label="Identidade")

    # Ponto inicial e iterações
    y = initial_value
    for _ in range(iterations):
        y_next = r_value * y * (1 - y)
        plt.plot([y, y], [y, y_next], 'k-', marker='.')
        plt.plot([y, y_next], [y_next, y_next], 'k-', marker='.')
        y = y_next

    # Configurações finais do gráfico
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()

# Exemplo de uso
# logistic_(4)

plot_chaos_function()