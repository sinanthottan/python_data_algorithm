class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def printer(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head
        lstr = ''

        while itr:
            lstr += str(itr.data) + '-->'
            itr = itr.next

        print(lstr)

    def create_list(self, data):
        self.head = None
        for item in data:
            self.insert_at_end(item)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count+=1
        return count

    def remove_at(self,ind):
        if ind >= self.get_length() or ind < 0:
            raise Exception("invalid index")

        if ind == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == ind-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

    def add_at(self,ind,data):
        if ind > self.get_length() or ind < 0:
            raise Exception("invalid index")

        if ind == 0:
            self.insert_at_begining(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == ind-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1




if __name__ == '__main__':
    ll = LinkedList()
    ll.create_list([1,2,3,4,5,9,10])
    print(ll.get_length())
    ll.add_at(6,4)
    ll.printer()
