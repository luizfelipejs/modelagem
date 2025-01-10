import numpy as np 

def get_linear_correlation_coefficient(x, y):
  product_of_x_and_y = [x_i * y_i for x_i, y_i in zip(x, y)]
  squares_of_x = [x_i ** 2 for x_i in x]
  squares_of_y = [y_i ** 2 for y_i in y]


  sum_of_product_of_x_and_y = sum(product_of_x_and_y)
  sum_of_x = sum(x)
  sum_of_y = sum(y)
  sum_squares_of_x = sum(squares_of_x)
  sum_squares_of_y = sum(squares_of_y)
  n = len(x)

  numerator = (sum_of_product_of_x_and_y) - ((sum_of_x * sum_of_y) / n)
  denominator = ((sum_squares_of_x) - ((sum_of_x ** 2) / n)) * ((sum_squares_of_y) - ((sum_of_y ** 2) / n))

  r = numerator / (denominator ** 0.5)

  return r

def linear_adjust(x, y):
  product_of_x_and_y = [x_i * y_i for x_i, y_i in zip(x, y)]
  squares_of_x = [x_i ** 2 for x_i in x]
  squares_of_y = [y_i ** 2 for y_i in y]


  sum_of_product_of_x_and_y = sum(product_of_x_and_y)
  sum_of_x = sum(x)
  sum_of_y = sum(y)
  sum_squares_of_x = sum(squares_of_x)
  sum_squares_of_y = sum(squares_of_y)
  n = len(x)

  alpha = (sum_of_product_of_x_and_y - ((sum_of_x * sum_of_y) / n)) / (sum_squares_of_x - ((sum_of_x ** 2) / n))
  beta = (sum_of_y / n) - alpha * (sum_of_x / n)

  return [alpha, beta]



def ford_walford_method(y): 
    y_i = [] 
    y_i_plus_1 = [] 
    for i in range (1, len(y)):
        y_i_plus_1.append(y[i])
    for i in range (0, len(y) - 1):
        y_i.append(y[i])

    a, b = linear_adjust(y_i, y_i_plus_1) # y = ay + b => y - ay = b => y = b/(1-a) 
    result = b/(1 - a)
    return result


def quadratic_adjust(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(x_i ** 2 for x_i in x)
    sum_x3 = sum(x_i ** 3 for x_i in x)
    sum_x4 = sum(x_i ** 4 for x_i in x)
    sum_y = sum(y)
    sum_xy = sum(x_i * y_i for x_i, y_i in zip(x, y))
    sum_x2y = sum((x_i ** 2) * y_i for x_i, y_i in zip(x, y))
    
    A = [
        [n, sum_x, sum_x2],
        [sum_x, sum_x2, sum_x3],
        [sum_x2, sum_x3, sum_x4]
    ]
    
    B = [sum_y, sum_xy, sum_x2y]
    
    a, b, c = np.linalg.solve(A, B)
    
    return c, b, a