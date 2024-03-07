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
    // hare and tortoise aldo
    // here slow pointer moves x nodes and fast traveles 2x nodes 
    // so fast either reaches NULL or the last node.
    ListNode* middleNode(ListNode* head) {
        ListNode*slow= head;
        ListNode*fast= head;
        while((fast!=NULL)&&(fast->next!=NULL)){
            fast=fast->next->next;
            slow=slow->next;
        }
        return slow;
    }
};