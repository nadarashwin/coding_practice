# Given two sorted lists, merge them so as to produce a combined sorted list.

# Examples:

# Input : head1: 5->7->9
#         head2: 4->6->8 
# Output : 4->5->6->7->8->9

# Input : head1: 1->3->5->7
#         head2: 2->4
# Output : 1->2->3->4->5->7



def mergeTwoLists(l1, l2):
    temp_list = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            temp_list.append(l1[i])
            i += 1
        else:
            temp_list.append(l2[j])
            j += 1
    
    temp_list = temp_list + l1[i:] + l2[j:]

    return temp_list


a = [1,2,4]
b = [1,3,4]

print(mergeTwoLists(a,b))