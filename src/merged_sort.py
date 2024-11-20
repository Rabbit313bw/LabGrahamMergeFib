from utils import rotate, find_start_point
from generate_data import generate_random_data
# from graham import find_start_point
from typing import List


def merge(left_list: list, right_list: list, C : List[list], start_point: list) -> list:
    sorted_list = []
    i = j = 0
    l_upper = len(left_list)
    r_upper = len(right_list)
    while i < l_upper and j < r_upper:
        if rotate(C[start_point], C[left_list[i]], C[right_list[j]]) >0:
            sorted_list.append(left_list[i])
            i += 1
        else:
            sorted_list.append(right_list[j])
            j += 1
    while i < l_upper:
        sorted_list.append(left_list[i])
        i += 1
    while j < r_upper:
        sorted_list.append(right_list[j])
        j += 1
    
    return sorted_list

def merge_sort(A: list, C: List[list], start_point: list) -> list:
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left_list = merge_sort(A[:mid], C, start_point)
    right_list = merge_sort(A[mid:], C, start_point)
    return merge(left_list, right_list, C, start_point)

if __name__ == "__main__":
    random_list_of_points = generate_random_data(5, 0.0, 10.0)
    P = find_start_point(random_list_of_points)
    sorted_points = merge_sort(P[1:], random_list_of_points, P[0])  
    print(P[0], *sorted_points)

