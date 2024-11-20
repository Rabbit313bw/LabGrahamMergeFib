from typing import List
from utils import rotate, find_start_point
from merged_sort import merge_sort


def grahamscan(A: List[list], sort=merge_sort):
  n = len(A)
  P_with_start_point = find_start_point(A)
  sorted_P = [P_with_start_point[0], *sort(P_with_start_point[1:], A, P_with_start_point[0])]
  S = [sorted_P[0], sorted_P[1]]
  for i in range(2,n):
    while rotate(A[S[-2]],A[S[-1]],A[sorted_P[i]])<0:
      del S[-1]
    S.append(sorted_P[i])
  return S

