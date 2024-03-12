/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        if (!head) return 0;
        head->next = removeZeroSumSublists(head->next);
        int sum = 0;
        ListNode *cur = head, *ret = head;
        while (cur) {
            sum += cur->val;
            cur = cur->next;
            if (!sum) ret = cur;
        }
        return ret;
    }
};
