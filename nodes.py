# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class listhead:
#     def __init__(self):
#         self.head = None
#
#
#     def to(self):
#         total = self.head
#         while total :
#             print(total.data)
#             total = total.next
#
#     def add_h(self, new_h):
#         new_h.next = self.head
#         self.head = new_h
#
#     def add_l(self,new_l):
#         he = self.head
#         while (he.next) :
#             he = he.next
#         he.next = new_l
#
#     def rem_h(self):
#         self.head = self.head.next
#
#     def rem_l(self):
#         he = self.head
#         while he:
#             he = he.next
#         he = None
#
#
#
# list = listhead()
#
# first = node(1)
# second = node(2)
# third = node(3)
# new = node(9)
# newl = node(8)
#
# list.head = first
#
# list.head.next = second
#
# second.next = third
#
# list.to()
# list.add_h(new)
# list.add_l(newl)
# list.rem_h()
# list.rem_l()
# list.to()
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class listhead:
    def __init__(self):
        self.head = None

    def to(self):
        total = self.head
        while total:
            print(total.data)
            total = total.next

    def add_h(self, new_h):
        new_h.next = self.head
        self.head = new_h

    def add_l(self, new_l):
        he = self.head
        while he.next:
            he = he.next
        he.next = new_l

    def rem_h(self):
        if self.head:
            self.head = self.head.next

    def rem_l(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        he = self.head
        while he.next.next:
            he = he.next
        he.next = None

    # def rem_l(self):               (((((  الحل السابق : لماذا هذه الدالة لا تعمل عكس الدالة الأولى   )))))))
    #     if not self.head:
    #         return
    #     if not self.head.next:
    #         self.head = None
    #         return
    #     he = self.head
    #     while he.next:
    #         he = he.next
    #     he = None


list = listhead()

first = node(1)
second = node(2)
third = node(3)
new = node(9)
newl = node(8)

list.head = first
list.head.next = second
second.next = third

print("\nقبل العمليات:")
list.to()

list.add_h(new)
list.add_l(newl)

print("\nبعد الإضافة:")
list.to()

list.rem_h()
list.rem_l()

print("\nبعد الحذف:")
list.to()
