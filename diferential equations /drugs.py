import numpy as np
import matplotlib.pyplot as plt

C0 = 10
k = 0.1
T = 5
n_doses = 100

r = np.exp(-k * T)

tempo = np.linspace(0, T * (n_doses + 1), 1000)
concentracao = np.zeros_like(tempo)

for i in range(len(tempo)):
    t = tempo[i]
    dose_atual = int(t // T)
    if dose_atual <= n_doses:
        soma_pg = (1 - r**(dose_atual + 1)) / (1 - r)
        tempo_desde_ultima_dose = t - dose_atual * T
        concentracao[i] = C0 * soma_pg * np.exp(-k * tempo_desde_ultima_dose)
    else:
        concentracao[i] = C0 * soma_pg * np.exp(-k * tempo_desde_ultima_dose)


plt.figure(figsize=(10, 6))
plt.plot(tempo, concentracao, color="blue")
plt.title("Uso de Drogas")
plt.xlabel("Tempo (horas)")
plt.ylabel("Concentração da droga")
plt.grid()
plt.show()
