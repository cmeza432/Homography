"""
Created on Mon Dec  4 13:35:24 2017

@author: Carlos Meza
"""

import numpy as np

def homographyStudent(points_skewed, points_corrected, test_points):
  # get x and y coordinates from starting points
  x1 = points_skewed[0, 0]
  x2 = points_skewed[0, 1]
  x3 = points_skewed[0, 2]
  x4 = points_skewed[0, 3]
  y1 = points_skewed[1, 0]
  y2 = points_skewed[1, 1]
  y3 = points_skewed[1, 2]
  y4 = points_skewed[1, 3]
  
  # Get x' and y' for desired points
  v1 = points_corrected[0, 0]
  v2 = points_corrected[0, 1]
  v3 = points_corrected[0, 2]
  v4 = points_corrected[0, 3]
  w1 = points_corrected[1, 0]
  w2 = points_corrected[1, 1]
  w3 = points_corrected[1, 2]
  w4 = points_corrected[1, 3]

  # Building solvable matrix
  c1 = np.array([x1, 0, 0, x2, 0, 0, x3, 0, 0, x4, 0, 0])
  c2 = np.array([y1, 0, 0, y2, 0, 0, y3, 0, 0, y4, 0, 0])
  c3 = np.array([1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])
  c4 = np.array([0, x1, 0, 0, x2, 0, 0, x3, 0, 0, x4, 0])
  c5 = np.array([0, y1, 0, 0, y2, 0, 0, y3, 0, 0, y4, 0])
  c6 = np.array([0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0])
  c7 = np.array([0, 0, x1, 0, 0, x2, 0, 0, x3, 0, 0, x4])
  c8 = np.array([0, 0, y1, 0, 0, y2, 0, 0, y3, 0, 0, y4])
  c9 = np.array([(-1) * v1, (-1) * w1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
  c10 = np.array([0, 0, 0, (-1) * v2, (-1) * w2, -1, 0, 0, 0, 0, 0, 0])
  c11 = np.array([0, 0, 0, 0, 0, 0, (-1) * v3, (-1) * w3, -1, 0, 0, 0])
  c12 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, (-1) * v4, (-1) * w4, -1])

  A = np.column_stack((c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12))
  b = np.array([[0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1]]).T

  # Get H by solving Ax = b, then reshape to 3 x 3 matrix
  H = np.linalg.solve(A, b)[:9]
  H = H.reshape(3, 3)
  H[2, 2] = 1

  # Use test points for projection
  projected = H.dot(test_points)
  for i in range(projected.shape[1]):
    projected[0, i] /= projected[2, i]
    projected[1, i] /= projected[2, i]

  return H, projected