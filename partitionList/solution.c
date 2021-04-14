/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* partition(struct ListNode* head, int x){
    if (head == NULL || head->next == NULL) return head;
    struct ListNode* headless = NULL;
    struct ListNode* less = NULL;
    struct ListNode* headmore = NULL;
    struct ListNode* more = NULL;
    while(head) {
        if (head->val < x) {
            if (headless) {
                if (less) {
                    less->next = head;
                    less=head;
                } else {
                    less = head;
                    headless->next=less;
                }
            } else {
                headless = head;
            }
        } else {
            if (headmore) {
                if (more) {
                    more->next = head;
                    more=head;
                } else {
                    more = head;
                    headmore->next=more;
                }
            } else {
                headmore = head;
            }
        }
        head = head->next;
    }
    if (less) {
        less->next=headmore;
    } else {
        if (headless) {
            headless->next = headmore;
        }
    }
    if (more) {
        more->next = NULL;    
    } else {
        if (headmore) {
            headmore->next = NULL;
        }
    }
    if (headless) return headless;
    return headmore;
}
