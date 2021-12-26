#include <bits/stdc++.h>
using namespace std;

long long calcz(long long num) {
    long long w = 0, x = 0, z = 0, p = 0;

    
    p=(long long)(1e13); w=(num/p)%10; x=z%26;	    	x+=14;	x=x!=w;	z*=25*x+1;	z+=(w+8)*x;	if (!w)    return -p;
    p=(long long)(1e12); w=(num/p)%10; x=z%26;	    	x+=13;	x=x!=w;	z*=25*x+1;	z+=(w+8)*x;	if (!w)    return -p;
    p=(long long)(1e11); w=(num/p)%10; x=z%26;	    	x+=13;	x=x!=w;	z*=25*x+1;	z+=(w+3)*x;	if (!w)    return -p;
    p=(long long)(1e10); w=(num/p)%10; x=z%26;	    	x+=12;	x=x!=w;	z*=25*x+1;	z+=(w+10)*x;if (!w)    return -p;
    p=(long long)(1e9);  w=(num/p)%10; x=z%26;	z/=26;	x+=-12;	x=x!=w;	z*=25*x+1;	z+=(w+8)*x;	if (!w||x) return -p;
    p=(long long)(1e8);  w=(num/p)%10; x=z%26;	    	x+=12;	x=x!=w;	z*=25*x+1;	z+=(w+8)*x;	if (!w)    return -p;
    p=(long long)(1e7);  w=(num/p)%10; x=z%26;	z/=26;	x+=-2;	x=x!=w;	z*=25*x+1;	z+=(w+8)*x;	if (!w||x) return -p;
    p=(long long)(1e6);  w=(num/p)%10; x=z%26;	z/=26;	x+=-11;	x=x!=w;	z*=25*x+1;	z+=(w+5)*x;	if (!w||x) return -p;
    p=(long long)(1e5);  w=(num/p)%10; x=z%26;	    	x+=13;	x=x!=w;	z*=25*x+1;	z+=(w+9)*x;	if (!w)    return -p;
    p=(long long)(1e4);  w=(num/p)%10; x=z%26;	    	x+=14;	x=x!=w;	z*=25*x+1;	z+=(w+3)*x;	if (!w)    return -p;
    p=(long long)(1e3);  w=(num/p)%10; x=z%26;	z/=26;	x+=0;	x=x!=w;	z*=25*x+1;	z+=(w+4)*x;	if (!w||x) return -p;
    p=(long long)(1e2);  w=(num/p)%10; x=z%26;	z/=26;	x+=-12;	x=x!=w;	z*=25*x+1;	z+=(w+9)*x;	if (!w||x) return -p;
    p=(long long)(1e1);  w=(num/p)%10; x=z%26;	z/=26;	x+=-13;	x=x!=w;	z*=25*x+1;	z+=(w+2)*x;	if (!w||x) return -p;
    p=(long long)(1e0);  w=(num/p)%10; x=z%26;	z/=26;	x+=-6;	x=x!=w;	z*=25*x+1;	z+=(w+7)*x;	if (!w||x) return -p;
    return z;
}

int main() {
    for (long long i = 99999999999999; i > 0; i--) {
        long long z = calcz(i);
        if (z < 0)
            i += z + 1;
        if (z == 0) {
            cout << i << endl;
            return 0;
        }
    }
}

