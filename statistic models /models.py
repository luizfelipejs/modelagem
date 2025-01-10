import numpy as np
import matplotlib.pyplot as plt
from statistic_tools import linear_adjust, get_linear_correlation_coefficient
from functions import plot_exp_function, plot_geometric_function, plot_linear_function, plot_racional_function


def exponencial_model(x, y, title, x_label, y_label):
  z = [np.log(y_i) for y_i in y]
  alpha, beta = linear_adjust(x, z)

  b = np.exp(beta)
  print("Reta auxiliar")
  plot_linear_function(alpha, beta, title="Reta auxiliar")
  print("Modelo exponencial")
  plot_exp_function(alpha, b, title=title, x_label=x_label, y_label=y_label, _x=x, _y=y, _label='dados')


# exemplo do livro com rendimento da poupança
meses = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
capital = [1000.0, 1009.7, 1021.8, 1032.2, 1045.3, 1056.9, 1065.8, 1077.1, 1089.7, 1110.1, 1121.0, 1132.2]

exponencial_model(meses, capital, "Rendimento da poupança", "mêses", "capital")
get_linear_correlation_coefficient(meses, capital)

def geometric_model(x, y, x_label, y_label, title):
  X = [np.log(x_i) for x_i in x] # ln x
  Y = [np.log(y_i) for y_i in y] # ln y

  beta, alpha = linear_adjust(X, Y)

  print('Reta auxiliar')
  plot_linear_function(beta, alpha, title='reta auxiliar')
  a = np.exp(alpha)
  b = beta

  plot_geometric_function(a, b, x_label='Comprimento (cm)', y_label='Peso (g)', title='Crescimento das tilapias', start=10, end=40, sub_values=100, _x=x, _y=y, _label='dados')


# exemplo com tilapias
comprimento = [11.0, 15.0, 17.4, 20.6, 22.7, 25.3, 27.4, 28.2, 29.3]
peso = [26.0, 59.5, 105.4, 200.2, 239.5, 361.2, 419.8, 475.4, 488.2]

geometric_model(comprimento, peso, 'comprimento', 'peso', 'crescimento tilapia')
get_linear_correlation_coefficient(comprimento, peso)

def hiperbolic_model(x, y, title, x_label, y_label, start, end):
  z = [1 / x_i for x_i in x]
  alpha, beta = linear_adjust(z, y)
  print("Reta auxiliar")
  plot_linear_function(alpha, beta, title='Reta auxiliar')
  print("Modelo hiperbolico")
  plot_racional_function (alpha, beta, x_label=x_label, y_label=y_label, title=title, start=start, end=end, sub_values=100, _x=x, _y=y, _label='dados')


# exercicio de aplicação do livro
nivel_de_renda = [600, 750, 900, 1000, 1500, 3000, 4500]
no_de_pessoas_com_renda_maior_ou_igual = [280, 180, 120, 100, 98, 90, 87]

hiperbolic_model(nivel_de_renda, no_de_pessoas_com_renda_maior_ou_igual, 'distribuição de renda', 'nível de renda', 'Número de pessoas com renda maior ou igual a x', 500, 4500)
get_linear_correlation_coefficient(nivel_de_renda, no_de_pessoas_com_renda_maior_ou_igual)


# exemplo do livro com ração

tempo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
racao = [12.3, 32.4, 50.3, 65.2, 78.1, 87.9, 94.2, 98.1, 101.4]

hiperbolic_model(tempo, racao, 'Consumo de ração', 'tempo (mês)', 'Ração', 1, 9)
get_linear_correlation_coefficient(tempo, racao)