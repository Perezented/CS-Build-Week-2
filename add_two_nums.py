# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = []

        curr1 = l1
        curr2 = l2
        extra = 0
        # r = ListNode()
        i = 0
        # current = r

        while curr1 is not None or curr2 is not None:
            if i == len(ans):
                ans.append(0)

            # print(curr1.val, curr2.val)
            if curr2 is not None and curr1 is not None:
                total_curr = curr1.val + curr2.val
            elif curr2 is None:
                total_curr = curr1.val
            elif curr1 is None:
                total_curr = curr2.val
            # print(total_curr)
            if total_curr >= 10:
                total_curr -= 10
                extra = 1

            if extra == 1:
                ans.append(1)
                extra = 0

            if total_curr + ans[i] >= 10:
                ans[i] = ans[i] + total_curr - 10

                if(len(ans)-1 == i):
                    ans.append(1)
                else:
                    ans[i+1] = 1

            else:
                ans[i] += (total_curr)

            if curr1 is not None:
                curr1 = curr1.next
            if curr2 is not None:
                curr2 = curr2.next
            i += 1
        print(ans)

#         for i in range(len(ans)-1):
#             if ans[i] >= 10:
#                 ans[i] -= 10

        r = ListNode(ans[0])
        current = r
        print(current.val)
        for i in range(len(ans)-1):
            i += 1
            current.next = ListNode(ans[i])
            current = current.next
        print(r)
        return r
