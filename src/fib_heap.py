import math
from typing import List
from utils import rotate, find_start_point
from generate_data import generate_random_data
from merged_sort import merge_sort




class Node():

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.parent = self.child = None
        self.left = self.right = self
        self.degree = 0
        self.flag = False


class FibonacciHeap():
    def __init__(self, start_point: list, C: List[list]):
        self.min = None
        self.no_nodes = 0
        self.start_point = start_point
        self.C = C

    def get_min(self):
        '''
        Returns minimum Node
        Сomplexity: O(1)
        '''

        return self.min

    def insert(self, key, value=None):
        '''
        Insert new value into the heap
        Complexety: O(1)
        '''

        if value is None:
            value = key
        n = Node(key, value)

        if self.no_nodes == 0:
            self.min = n
        else:
            self.add_root(n)

        self.no_nodes += 1

        return n

    def delete_min(self):
        '''
        Removes minimum node from the heap
        Complexety: O(log(n))
        '''

        prev_min = self.min
        if prev_min is not None:

            # move children to root
            if prev_min.child is not None:
                n = stop = prev_min.child
                first_loop = True
                while first_loop or n != stop:
                    first_loop = False
                    next_node = n.right
                    self.add_node_left(n, self.min)
                    n.parent = None
                    n = next_node

            if self.min.right != self.min:
                self.min = prev_min.right
                self.remove_node(prev_min)
                self.consolidate()
            # no nodes left
            else:

                start_for_newmin = prev_min.right
                self.remove_node(prev_min)
                self.find_new_min(start_for_newmin)

            self.no_nodes -= 1
        return prev_min

    def find_new_min(self, start_for_newmin):
        '''Finds new minimum in heap after previous was deleted'''

        node = stop = start_for_newmin
        flag = False
        min_value = float('inf')
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            if min_value == float('inf'):
                self.min = node
                min_value = node.key
            if rotate(self.C[self.start_point], self.C[node.key], self.C[min_value]) > 0:
                self.min = node
                min_value = node.key
            node = node.right

    def consolidate(self):
        '''Make the degrees of root elements unique, fibonacci sequence'''

        degree_arr = [None for _ in range(int(math.log(self.no_nodes, 2)) + 2)]
        root_items = self.layer_as_list(self.min)
        for n in root_items:

            degree = n.degree
            # combine nodes until no same root degrees exists
            while degree_arr[degree] is not None:
                m = degree_arr[degree]
                # make sure that n is always smaller
                if rotate(self.C[self.start_point], self.C[m.key], self.C[n.key]) > 0:
                    n, m = self.swap_vars(n, m)
                self.remove_node(m)
                self.add_child(m, n)
                degree_arr[degree] = None
                degree += 1

            degree_arr[degree] = n

        self.update_root_min()

    def update_root_min(self):
        '''Update self.min to lowest value from the root'''

        top = self.find_root_item()
        root_layer = self.layer_as_list(top)
        for n in root_layer:
            if rotate(self.C[self.start_point], self.C[self.min.key], self.C[n.key]) < 0:
                self.min = n
        # self.min = min(root_layer, key=lambda n: n.key)

    def find_root_item(self):
        '''Return an item from root layer'''

        top_item = self.min
        while top_item.parent is not None:
            top_item = top_item.parent
        return top_item

    def add_node_left(self, node, right_node):
        '''Add node to left side of the given right_node'''

        node.right = right_node
        node.left = right_node.left
        right_node.left.right = node
        right_node.left = node

    def add_root(self, node):
        '''Add node to left side of the given right_node'''

        self.add_node_left(node, self.min)
        if rotate(self.C[self.start_point], self.C[node.key], self.C[self.min.key]) > 0:
            self.min = node

    def add_child(self, child, parent):
        '''Add node as child to another node'''

        if parent.child is None:
            parent.child = child
            child.parent = parent
        else:
            self.add_node_left(child, parent.child)
            child.parent = parent
        parent.degree += 1

    def swap_vars(self, var1, var2):
        '''Swap variables'''

        return (var2, var1)

    def remove_node(self, node):
        '''Remove element from the double linked list'''

        node.left.right = node.right
        node.right.left = node.left
        node.left = node
        node.right = node
        node.parent = None

    def layer_as_list(self, node):
        '''
        Return the whole layer as a list.
        One node from the layer must be given
        '''

        items = []
        n = stop = node
        first_loop = True
        while first_loop or n != stop:
            first_loop = False
            items.append(n)
            n = n.right
        return items
    

def heap_sort(A: list, C: List[list], start_point: list) -> list:
    A_sorted = []
    heap_size = len(A)
    fib_heap = FibonacciHeap(start_point=start_point, C=C)
    for i in range(len(A)):
        fib_heap.insert(A[i])
    while heap_size > 0:
        A_sorted.append(fib_heap.get_min().val)
        fib_heap.delete_min()
        heap_size -= 1
    return A_sorted
    


if __name__ == "__main__":
    random_list_of_points = generate_random_data(100, 0.0, 10.0)
    P = find_start_point(random_list_of_points)
    print("Unsorted_data ----->")
    print(*P)
    sorted_points = heap_sort(P[1:], start_point=P[0], C=random_list_of_points)
    sorted_points_heap = sorted_points.copy()
    print("Heap_sort ------->")
    print(P[0], *sorted_points)