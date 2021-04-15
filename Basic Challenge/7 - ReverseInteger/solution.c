
int len_int(int x)
{
    int len = -1;
    while(x > 0)
    {
        x/=10;
        len ++;
    }
    return len;
}

int old_reverse(int x){
    int res = 0;
    int isNegative = 0;
    if (x == -2147483648)
        return 0;
    if(x < 0 )
    {
        isNegative = 1;
        x = 0 - x;
    }
    int digit = len_int(x);
    while (x > 0)
    {
        if(digit>8 && x%10 >2)
        {
            return 0;
        }
        if (res > INT_MAX/10)
        res+=(x%10)*((int)pow(10,digit));
        x/=10;
        digit--;
    }
    if (isNegative)
    {
        return (0-res);
    }
    return res;
}
int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
}
