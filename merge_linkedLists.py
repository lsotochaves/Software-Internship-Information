# Definition for singly-linked list node 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeLinkedLists:

    #Trying new forms of introducing parameters to function
    def merge_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        # Both will point to the same node to get the head
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:

                #Assigns value and updates (dummy updates too and .next serves as the head)
                current.next = list1
                list1 = list1.next 
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1 # Completes with list1
        else:
            current.next = list2

        return dummy.next
        
'''
Tests not made by me
'''
def create_linked_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))

# --- Execution ---

# 1. Create the input data
input1 = create_linked_list([1, 2, 4, 20, 50])
input2 = create_linked_list([1, 3, 4, 6, 7])

print("List 1:")
print_linked_list(input1)
print("List 2:")
print_linked_list(input2)

# 2. Run your solution
solver = MergeLinkedLists()
result_head = solver.merge_lists(input1, input2)

# 3. Verify the output
print("\nMerged List:")
print_linked_list(result_head)

# Expected Output:
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 6 -> 7 -> 20 -> 50