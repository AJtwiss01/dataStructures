import random
class Heap:
##    create a heap class
    def _Init__(self):
##        create a empty list ot stuff random numbers in for heap list
        self.heap = []
        print(type(self.heap))
        self.lastIndex = -1

    def push(self, value):
        self.lastIndex += 1
        if self.lastIndex < len(self.heap):
            self.heap[self.lastIndex] = value
        else:
            self.heap.append(value)
        self.siftup(self.lastIndex)

    def pop(self):
        if self.lastIndex == -1:
            raise IndexError('pop from empty heap')

        min_value = self.heap[0]

        self.heap[0] = self.heap[self.lastIndex]
        self.lastIndex -= 1
        self.siftdown(0)

        return min_value

    def siftup(self, index):
        while index > 0:
            parentIndex, parent_value = self.get_parent(index)

            if parent_value <= self.heap[index]:
                break

            self.heap[parentIndex], self.heap[index] =\
                self.heap[index], self.heap[parentIndex]

            index = parentIndex

    def siftdown(self, index):
        while True:
            index_value = self.heap[index]

            left_childIndex, left_child_value = self.get_left_child(index, index_value)
            right_childIndex, right_child_value = self.get_right_child(index, index_value)

            if index_value <= left_child_value and index_value <= right_child_value:
                break

            if left_child_value < right_child_value:
                newIndex = left_childIndex
            else:
                newIndex = right_childIndex

            self.heap[newIndex], self.heap[index] =\
                self.heap[index], self.heap[newIndex]

            index = newIndex

    def get_parent(self, index):
        if index == 0:
            return None, None

        parentIndex = (index - 1) // 2

        return parentIndex, self.heap[parentIndex]

    def get_left_child(self, index, default_value):
        left_childIndex = 2 * index + 1

        if left_childIndex > self.lastIndex:
            return None, default_value

        return left_childIndex, self.heap[left_childIndex]

    def get_right_child(self, index, default_value):
        right_childIndex = 2 * index + 2

        if right_childIndex > self.lastIndex:
            return None, default_value

        return right_childIndex, self.heap[right_childIndex]

    def size(self):
        return self.lastIndex + 1

#test large values
##randomInts = random.sample(range(100), 100)
#test small values 
randomInts = random.sample(range(3), 3)
##Test random Numbers 
print(randomInts)

h = Heap()
print(h)
for v in randomInts:
    h.push(v)

while h.size() > 0:
    print(h.pop(), end=' ')