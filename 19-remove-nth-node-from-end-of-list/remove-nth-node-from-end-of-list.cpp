class Solution {
public:
    int lengthOfLinkedList(ListNode *head){
        ListNode *temp=head;
        int length=0;
        while(temp!=NULL){
            length++;
            temp=temp->next;
        }
        return length;
    }


    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int length=lengthOfLinkedList(head);
        n=length-n+1;
        if(n==1){
            return head->next;
        }
        int cnt=0;
        ListNode* temp=head;
        ListNode* prev=head;
        while(temp!=NULL){
            cnt++;
            if(cnt==n){
                prev->next=prev->next->next;
            }
            prev=temp;
            temp=temp->next;
        }
        return head;
    }
};