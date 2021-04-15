int digitToRoman(int value, char up, char mid, char bot, char * res, int res_index) {
    switch(value) {
        case 9:
            res[res_index] = bot;
            res[res_index+1] = up;
            res_index+=2;
            break;
        case 8:
            res[res_index] = mid;
            res[res_index+1] = bot;
            res[res_index+2] = bot;
            res[res_index+3] = bot;
            res_index+=4;
            break;
        case 7:
            res[res_index] = mid;
            res[res_index+1] = bot;
            res[res_index+2] = bot;
            res_index+=3;
            break;
        case 6:
            res[res_index] = mid;
            res[res_index+1] = bot;
            res_index+=2;
            break;
        case 5:
            res[res_index] = mid;
            res_index++;
            break;
        case 4:
            res[res_index] = bot;
            res[res_index+1] = mid;
            res_index+=2;
            break;
        default:
            for(int i = 0; i < value; i++) {
                res[res_index] = bot;
                res_index++;
            }
    }
    return res_index;
}

char * intToRoman(int num){
    char * res = malloc(sizeof(char)*16);
    int first_digit = num/1000;
    int res_index = 0;
    switch(first_digit) { // by not putting num/1000 inside switch test, we save 4ms wtf
        case 3:
            res[res_index] = 'M';
            res[res_index+1] = 'M';
            res[res_index+2] = 'M';
            res_index+=3;
            break;
        case 2:
            res[res_index] = 'M';
            res[res_index+1] = 'M';
            res_index+=2;
            break;
        case 1:
            res[res_index] = 'M';
            res_index++;
            break;
        default:
            break;
    }
    res_index = digitToRoman((num%1000)/100,'M','D','C',res,res_index);
    res_index = digitToRoman((num%100)/10,'C','L','X',res,res_index);
    res_index = digitToRoman(num%10,'X','V','I',res,res_index);
    
    res[res_index] = '\0';
    return res;
}
