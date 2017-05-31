#include <iostream>
using namespace std;

int nim(int a, int b, int c){
	int r;
	r=a^b^c;
	return r;
}

int main(){
	int n;
	int i = 1;
	int zeroes = 0;
	int limit = 1073741824;
	limit++;

	while(i<limit){
		n = nim(i,i*2,i*3);
		if(n==0){
			zeroes++;
		}
		i++;
	}
	cout << zeroes << endl;
}