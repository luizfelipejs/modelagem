import numpy as np
import matplotlib.pyplot as plt

def logistic_map(steps, r_value):
    values_to_plot = []
    x = 0.1  
    for c in range(steps):
        x = r_value * x * (1 - x)  
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
    y_logistic = r_value * x * (1 - x)
    y_identity = x  
    
    plt.plot(x, y_logistic, color="blue", label="Logística")
    plt.plot(x, y_identity, color="orange", label="Identidade")
    
    y = initial_value
    for _ in range(iterations):
        y_next = r_value * y * (1 - y)
        plt.plot([y, y], [y, y_next], 'k-', marker='.')
        plt.plot([y, y_next], [y_next, y_next], 'k-', marker='.')
        y = y_next
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()

# Exemplo de uso
logistic_map(200, 3.9)
logistic_(3.9)

logistic_map(200, 1.90)
logistic_(1.9)

logistic_map(200, 3.4)
logistic_(3.4)

logistic_map(200, -0.9)
logistic_(-0.9)