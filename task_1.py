class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            sorted_list.insert_sorted(current.data)
            current = current.next
        self.head = sorted_list.head

    def insert_sorted(self, data):
        new_node = Node(data)
        if not self.head or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    @staticmethod
    def merge_sorted(list1, list2):
        merged_list = LinkedList()
        current1, current2 = list1.head, list2.head
        while current1 and current2:
            if current1.data < current2.data:
                merged_list.append(current1.data)
                current1 = current1.next
            else:
                merged_list.append(current2.data)
                current2 = current2.next
        while current1:
            merged_list.append(current1.data)
            current1 = current1.next
        while current2:
            merged_list.append(current2.data)
            current2 = current2.next
        return merged_list

    # Виведення списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

list1 = LinkedList()
list1.append(3)
list1.append(1)
list1.append(4)
list1.append(2)

print("Оригінальний список:")
list1.print_list()

list1.reverse()
print("Реверсований список:")
list1.print_list()

list1.sort()
print("Відсортований список:")
list1.print_list()

list2 = LinkedList()
list2.append(5)
list2.append(0)
merged_list = LinkedList.merge_sorted(list1, list2)
print("Об'єднаний відсортований список:")
merged_list.print_list()
