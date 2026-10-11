class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = new

    def add_start(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def add_after(self, x, data):
        t = self.head
        while t != None:
            if t.data == x:
                new = Node(data)
                new.next = t.next
                t.next = new
                return
            t = t.next
        print("Element tapilmadi")

    def delete(self, x):
        t = self.head
        if t != None and t.data == x:
            self.head = t.next
            return
        while t != None and t.next != None:
            if t.next.data == x:
                t.next = t.next.next
                return
            t = t.next
        print("Element tapilmadi")

    def search(self, x):
        t = self.head
        while t != None:
            if t.data == x:
                print("Element tapildi.")
                return
            t = t.next
        print("Element tapilmadi.")

    def length(self):
        c = 0
        t = self.head
        while t != None:
            c += 1
            t = t.next
        return c

    def max_min(self):
        mx = self.head.data
        mn = self.head.data
        t = self.head
        while t != None:
            if t.data > mx:
                mx = t.data
            if t.data < mn:
                mn = t.data
            t = t.next
        return mx, mn

    def reverse(self):
        prev = None
        cur = self.head
        while cur != None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def show(self):
        t = self.head
        while t != None:
            print(t.data, end=" -> ")
            t = t.next
        print("None")


def make_list(arr):
    l = LinkedList()
    for i in arr:
        l.add_end(i)
    return l


# Tapsiriq 1
print("Tapsiriq 1")
n = Node(15)
print(n.data)

# Tapsiriq 2
print("\nTapsiriq 2")
l = make_list([10, 20, 30, 40])
l.show()

# Tapsiriq 3
print("\nTapsiriq 3")
l = make_list([20, 30, 40])
l.add_start(10)
l.show()

# Tapsiriq 4
print("\nTapsiriq 4")
l = make_list([10, 20, 40])
l.add_after(20, 30)
l.show()

# Tapsiriq 5
print("\nTapsiriq 5")
l = make_list([10, 20, 30, 40, 50])
l.delete(30)
l.show()

# Tapsiriq 6
print("\nTapsiriq 6")
l.search(40)
l.search(30)

# Tapsiriq 7
print("\nTapsiriq 7")
l = make_list([11, 22, 33, 44, 55])
print("List length =", l.length())

# Tapsiriq 8
print("\nTapsiriq 8")
l = make_list([23, 8, 91, 15, 42])
mx, mn = l.max_min()
print("Maksimum:", mx)
print("Minimum:", mn)

# Tapsiriq 9
print("\nTapsiriq 9")
l = make_list([10, 20, 30, 40, 50])
l.reverse()
l.show()


# Tapsiriq 10
class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add(self, id, name, gpa):
        new = Student(id, name, gpa)
        if self.head == None:
            self.head = new
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = new

    def remove(self, id):
        t = self.head
        if t != None and t.id == id:
            self.head = t.next
            return
        while t != None and t.next != None:
            if t.next.id == id:
                t.next = t.next.next
                return
            t = t.next
        print("Tapilmadi")

    def show_all(self):
        t = self.head
        while t != None:
            print(t.id, t.name, t.gpa)
            t = t.next

    def show_gpa(self):
        t = self.head
        while t != None:
            if t.gpa > 80:
                print(t.id, t.name, t.gpa)
            t = t.next

    def find(self, name):
        t = self.head
        while t != None:
            if t.name == name:
                print("Tapildi:", t.id, t.name, t.gpa)
                return
            t = t.next
        print("Tapilmadi")

    def count(self):
        c = 0
        t = self.head
        while t != None:
            c += 1
            t = t.next
        return c


print("\nTapsiriq 10")
s = StudentList()
s.add(1, "Aysel", 85)
s.add(2, "Elvin", 72)
s.add(3, "Nigar", 91)
s.add(4, "Murad", 78)

print("Butun telebeler:")
s.show_all()
print("GPA > 80:")
s.show_gpa()
print("Ada gore axtaris:")
s.find("Nigar")
s.find("Kamran")
print("Telebe sayi:", s.count())
s.remove(2)
print("ID=2 silindi:")
s.show_all()
print("Telebe sayi:", s.count())
