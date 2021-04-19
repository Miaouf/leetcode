/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int listnodeLength(struct ListNode* l) {
    int res = 0;
    while (l) {
        res++;
        l=l->next;
    }
    return res;
}

struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    int len = listnodeLength(head);
    
    if (len < 1 || n > len) return head;
    if (len == n) return head->next;
    
    int index = len - n;
    struct ListNode* before = head;
    while (index > 1 && before->next) {
        index--;
        before = before->next;
    }
    /* now we are before the desired node */ 
    before->next = (before->next)?before->next->next:NULL;
    return head;
}
