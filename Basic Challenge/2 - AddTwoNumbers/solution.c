/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2)
{
    struct ListNode* head = l1;
    struct ListNode* before;
    int ret = 0;
    while(l1 && l2)
    {
        if((l1->val+=l2->val + ret) >= 10)
        {
            l1->val %= 10;
            ret = 1;
        }
        else
        {
            ret = 0;
        }
        before = l1;
        l1=l1->next;
        l2=l2->next;
    }
    if(l2)
    {
        before->next = l2; //rattache la suite de l2
        while(ret && l2)
        {
            if ((l2->val+=ret) >= 10)
            {
                l2->val%=10;
                ret = 1;
                before = l2;
                l2=l2->next;
            }
            else
            {
                ret =0;
            }
        }
        if(ret)
        {
            before->next = malloc(sizeof(struct ListNode));
            before->next->val = ret;
            before->next->next = NULL;
        }
    }else
    {
        while(ret && l1)
        {
            if ((l1->val+=ret) >= 10)
            {
                l1->val%=10;
                ret = 1;
                before = l1;
                l1=l1->next;
            }
            else
            {
                ret = 0;
            }
        }
        if(ret)
        {
            before->next = malloc(sizeof(struct ListNode));
            before->next->val = ret;
            before->next->next = NULL;
        }
    }
    return head;
}
