class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.head = None
    
    def insertAtBegin(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return new_node
        else:
            new_node.next = self.head
            self.head = new_node

def reverseList(headNode, list):
    if len(list) < 1:
        return
    else:
        return reverseList(headNode.insertAtBegin(list.pop()), list)

initNode = ListNode()
ans = reverseList(initNode, [1,2,3,4,5])
print(ans)

# print(initNode.val)
# testList = [1, 2]
# print(testList.pop())
# print(testList)