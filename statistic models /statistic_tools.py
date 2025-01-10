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