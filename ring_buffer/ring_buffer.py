from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if self.current is none:
        #     self.current = item

        if self.storage.length+1 > self.capacity:
            print("too much")
            # self.storage.head.next.insert_before(item)
            # self.storage.remove_from_head()
            # print(self.storage.remove_from_tail())
            # while self.storage.head.next:
            # print(self.storage.head.value)
            # self.storage.head = self.storage.head.next
            # self.current += 1

            # newDLL = DoublyLinkedList()
            # gg = self.storage.head
            # while gg:
            #     print(gg.value)
            #     if(gg.value == self.current):
            #         newDLL.add_to_head(item)
            #     else:
            #         newDLL.add_to_tail(item)
            #     gg = gg.next

            # print(newDLL)

            # while newDLL.head:
            #     print(newDLL.head.value)
            #     newDLL.head = newDLL.head.next
            # pass
        else:
            self.storage.add_to_tail(item)
            self.current = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        # return [number for number in self.storage if number != None]
        # return list(filter(lambda x: x != None, self.storage))

        gg = self.storage.head
        # print(gg.next)
        while gg:
            print(gg.value)
            list_buffer_contents.append(gg.value)
            gg = gg.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity
        pass

    def append(self, item):
        # print(self.current)
        if self.current+1 == self.capacity:
            # self.storage.pop(0)
            # print("here")
            self.current = 0
        else:
            self.current += 1

        self.storage[self.current-1] = item
        # self.current += 1

    def get(self):
        return [number for number in self.storage if number != None]
        return list(filter(lambda x: x != None, self.storage))
        # return self.storage


buffer = RingBuffer(5)
print(buffer.storage.length)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
print()
print(buffer.storage.length)
print()
print(buffer.get())

# buffer_2 = ArrayRingBuffer(5)
# buffer_2.append('a')
# buffer_2.append('b')
# buffer_2.append('c')
# buffer_2.append('d')
# buffer_2.append('e')
# buffer_2.append('f')
# print(buffer_2.get())
