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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        
        ListNode* c1 = list1;
        ListNode* c2 = list1;

        int i = 0;

        while(c1!=NULL)
        {
            if(i==a-1)
            {
                break;
            }

            c1 = c1->next;

            i++;
        }


        int j = 0;

        while(c2!=NULL)
        {
            if(j==b+1) break;

            c2 = c2->next;

            j++;
        }
        

        ListNode* point = list2;

   

        while(point->next!=NULL)
        {
            point = point->next;
        }

        // cout<<point->val;

        c1->next =NULL;

        c1->next = list2;

        point->next = c2;

        return list1;
    }
};