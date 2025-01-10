import numpy as np
import matplotlib.pyplot as plt

def plot_exp_function(a, b, x_label, y_label, title, start=0, end=30, sub_values=100, _x=[], _y=[], _label='dados'):
    x = np.linspace(start, end, sub_values)
    y = b * np.exp(x * a)  # b * e^(ax)

    plt.figure(figsize=(10, 6))

    plt.style.use('default')
    plt.plot(_x, _y, color='darkorange', linestyle=':', linewidth=1.5, marker='o', markersize=7, label=_label)


    plt.plot(x, y, color='royalblue', linestyle='-', linewidth=2, label=fr'$y = {b:.3f} * e^{{{a:.3f}x}}$')
    plt.title(title, fontsize=16, loc='center')
    plt.legend(loc='upper left', fontsize=12)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()
    return


def plot_linear_function(a, b, x_label='x', y_label='y', title='teste', start=-5, end=5, sub_values=100):
    x = np.linspace(start, end, sub_values)
    y = a * x + b

    label = ''
    if b > 0:
        label = f'$y = {a:.3f}x + {b:.3f}$'
    else:
        label = f'$y = {a:.3f}x {b:.3f}$'

    plt.style.use('default')
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='royalblue', linestyle='-', linewidth=2, label=label)
    plt.title(title, fontsize=16, loc='center')
    plt.legend(loc='upper left', fontsize=12)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()
    return

def plot_geometric_function(a, b, x_label='x', y_label='y', title='teste', start=-5, end=5, sub_values=100, _x=[], _y=[], _label='dados'):
  x = np.linspace(start, end, sub_values)
  y = a * (x ** b)

  plt.style.use('default')
  plt.figure(figsize=(10, 6))


  plt.plot(x, y, color='royalblue', linestyle='-', linewidth=2, label=rf'$y = {a:.3f} \cdot x^{{{b:.3f}}}$')
  plt.plot(_x, _y, color='darkorange', linestyle=':', linewidth=1.5, marker='o', markersize=7, label=_label)

  plt.title(title, fontsize=16, loc='center')
  plt.legend(loc='upper left', fontsize=12)


  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.grid(True)
  plt.show()
  return

def plot_racional_function (a, b, x_label='x', y_label='y', title='teste', start=-5, end=5, sub_values=100, _x=[], _y=[], _label='dados'):
  x = np.linspace(start, end, sub_values)
  y = a/x + b

  plt.style.use('default')
  plt.figure(figsize=(10, 6))

  label = ''
  if b > 0:
    label = rf'$y = {a:.3f}/x + {{{b:.3f}}}$'
  else:
    label = rf'$y = {a:.3f}/x {{{b:.3f}}}$'


  plt.plot(x, y, color='royalblue', linestyle='-', linewidth=2, label=label)
  plt.scatter(_x, _y, color='darkorange', s=70, label=_label)

  plt.title(title, fontsize=16, loc='center')
  plt.legend(loc='upper right', fontsize=12)


  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.grid(True)
  plt.show()
  return

def plot_custom_logistic_function(a, b, lambda_, x_label='Período', y_label='y', title='Logistic Curve', start=0, end=10, sub_values=100, _x=[], _y=[], _label='dados', periods=[]):
    x = np.linspace(start, end, sub_values)
    # Corrigir a fórmula de y
    y = a / (1 + b * np.exp(-lambda_ * x))
    
    plt.figure(figsize=(10, 6))
    plt.style.use('default')
    
    if _x and _y:
        plt.plot(_x, _y, color='darkorange', linestyle=':', linewidth=1.5, marker='o', markersize=7, label=_label)
    
    plt.plot(x, y, color='royalblue', linestyle='-', linewidth=2, label=fr'$y = \frac{{{a:.3f}}}{{1 + {b:.3f}e^{{-{lambda_:.3f}x}}}}$')
    
    plt.title(title, fontsize=16, loc='center')
    plt.legend(loc='upper right', fontsize=12)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    plt.xticks(ticks=range(len(periods)), labels=periods, rotation=45)
    
    plt.grid(True)
    plt.tight_layout()  
    
    plt.show()

def plot_quadratic_function(a, b, c, x_label='x', y_label='y', title='Gráfico Quadrático', start=-10, end=10, sub_values=100, _x=[], _y=[], _label='dados'):
    x = np.linspace(start, end, sub_values)
    y = a * x**2 + b * x + c

    plt.figure(figsize=(10, 6))
    plt.style.use('default')

    if _x and _y:
        plt.plot(_x, _y, color='darkorange', linestyle=':', linewidth=1.5, marker='o', markersize=7, label=_label)

    plt.plot(x, y, color='royalblue', linestyle='-', linewidth=2, label=fr'$y = {a:.3f}x^2 + {b:.3f}x + {c:.3f}$')

    plt.title(title, fontsize=16, loc='center')
    plt.legend(loc='upper left', fontsize=12)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)

    plt.show()
    return


def plot_custom_exp_function(y_star, a, b, x_label='x', y_label='y', title='Gráfico de y = y* - a * exp(bx)', start=0, end=10, sub_values=100, _x=[], _y=[], _label='dados'):
    x = np.linspace(start, end, sub_values)
    y = y_star - a * np.exp(b * x)
    
    plt.figure(figsize=(10, 6))
    plt.style.use('default')
    
    if _x and _y:
        plt.plot(_x, _y, color='darkorange', linestyle=':', linewidth=1.5, marker='o', markersize=7, label=_label)
    
    plt.plot(x, y, color='royalblue', linestyle='-', linewidth=2, label=fr'$y = {y_star:.3f} - {a:.3f} e^{{{b:.3f}x}}$')
    
    plt.title(title, fontsize=16, loc='center')
    plt.legend(loc='upper right', fontsize=12)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    
    plt.show()
    return