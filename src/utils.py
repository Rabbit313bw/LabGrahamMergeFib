from typing import List

def rotate(A,B,C):
  return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

def find_start_point(A: List[list]) -> list:
  num_points = len(A)
  P = list(range(num_points))
  for i in range(1, num_points):
    if A[P[i]][0] < A[P[0]][0]:
      P[i], P[0] = P[0], P[i]
  return P