class ListNode:
    # Constructor for ListNode class
    def __init__(self, value=0, next=None):
        # Initialize the value and next pointer for the node
        self.value = value
        self.next = next

# Merge two sorted linked lists
def merge_sorted_lists(list1, list2):
    result = ListNode()
    current = result

    # Loop until either list1 or list2 becomes empty
    while list1 is not None and list2 is not None:
        # Compare values of the current nodes in list1 and list2
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    # If there are remaining nodes in list1, append them to the result list
    if list1 is not None:
        current.next = list1
    # If there are remaining nodes in list2, append them to the result list
    elif list2 is not None:
        current.next = list2

    return result.next

# Take input from the user and create a sorted linked list
def input_linked_list():
    input_list = input("Enter elements separated by space: ")
    elements = list(map(int, input_list.split()))   # Convert the input string into a list of integers

    # Check if the number of nodes in the list exceeds 50
    if len(elements) > 50:
        print("Error: The number of nodes in the list cannot exceed 50.")
        return None

    # Check if node values are within the range [-100, 100]
    for element in elements:
        if not (-100 <= element <= 100):
            print("Error: Node value should be in the range [-100, 100].")
            return None

    elements.sort()   # Sort the elements in ascending order

    result = ListNode()
    current = result

    # Create nodes with sorted values and append them to the result list
    for element in elements:
        current.next = ListNode(element)
        current = current.next

    # Return the sorted linked list
    return result.next

# Print the elements of a linked list
def print_list(head):
    current = head
    while current:
        print(current.value, end="")
        current = current.next
        if current:
            print(" -> ", end="")
    print()

# ==== Result =====
print("\n>>> Enter elements for the first linked list")
list1 = input_linked_list()

print("\n>>> Enter elements for the second linked list")
list2 = input_linked_list()

print("\nList 1: ", end="")
print_list(list1)

print("List 2: ", end="")
print_list(list2)

merged_list = merge_sorted_lists(list1, list2)
print("\nMerged List:", end=" ")
print_list(merged_list)