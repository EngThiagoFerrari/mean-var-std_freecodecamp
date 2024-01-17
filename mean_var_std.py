import numpy as np

def calculate(num_list):
  if len(num_list) < 9:
    raise ValueError("List must contain nine numbers.")

  matrix_num = np.array([[num_list[0:3]], [num_list[3:6]], [num_list[6:]]])
  ### Mean ###
  mean_axis1 = np.mean(matrix_num, axis=0).flatten().tolist()
  mean_axis2 = np.mean(matrix_num, axis=2).flatten().tolist()
  mean_list = np.mean(matrix_num)
  mean = [mean_axis1, mean_axis2, mean_list]

  ### Var ###
  var_axis1 = np.var(matrix_num, axis=0).flatten().tolist()
  var_axis2 = np.var(matrix_num, axis=2).flatten().tolist()
  var_list = np.var(matrix_num)
  variance = [var_axis1, var_axis2, var_list]

  ### std-dev ###
  dev_axis1 = np.std(matrix_num, axis=0).flatten().tolist()
  dev_axis2 = np.std(matrix_num, axis=2).flatten().tolist()
  dev_list = np.std(matrix_num)
  std_dev = [dev_axis1, dev_axis2, dev_list]

  ### Max ###
  max_axis1 = np.max(matrix_num, axis=0).flatten().tolist()
  max_axis2 = np.max(matrix_num, axis=2).flatten().tolist()
  max_list = np.max(matrix_num)
  maximum = [max_axis1, max_axis2, max_list]

  ### Min ###
  min_axis1 = np.min(matrix_num, axis=0).flatten().tolist()
  min_axis2 = np.min(matrix_num, axis=2).flatten().tolist()
  min_list = np.min(matrix_num)
  minimum = [min_axis1, min_axis2, min_list]

  ### Addition ###
  sum_axis1 = np.sum(matrix_num, axis=0).flatten().tolist()
  sum_axis2 = np.sum(matrix_num, axis=2).flatten().tolist()
  sum_list = np.sum(matrix_num)
  addition = [sum_axis1, sum_axis2, sum_list]

  calculations = {
    'mean': mean,
    'variance': variance,
    'standard deviation': std_dev,
    'max': maximum,
    'min': minimum,
    'sum': addition
        }

  return calculations
  