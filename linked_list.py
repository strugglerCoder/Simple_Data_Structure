class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Link_list:
    def __init__(self):
        self.start = None

    def insert_last(self, data):

        new_node = node(data)

        if self.start == None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def delete_first(self):
        if self.start == None:
            print("List is empty")
        else:
            # temp = self.start
            self.start = self.start.next

    def show_list(self):
        if self.start == None:
            print("List is empty")
        else:
            temp = self.start
            while temp.next != None:
                print(temp.data, end=' ')
                temp = temp.next

mylist = Link_list()
mylist.show_list()
mylist.insert_last(10)
mylist.show_list()
mylist.insert_last(20)
mylist.insert_last(30)
mylist.insert_last(40)
mylist.show_list()
print()
mylist.delete_first()
mylist.show_list()
