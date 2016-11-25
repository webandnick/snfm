#include <stdlib.h>
#include <stdio.h>


//speicher übergegebn


void fun(int *a,int len){

int *c = (int *) malloc(sizeof(*a) * 10);           // Speicher anfordern
int *o = (int *) malloc(sizeof(*a) * 10);
if (c == NULL) {
    perror("Nicht genug Speicher vorhanden."); // Fehler ausgeben
    exit(EXIT_FAILURE);                        // Programm mit Fehlercode abbrechen
}



	//int o[len];
/*
	for (int i=0;i<len;i++){
		c[i] = 0;
		o[i] = 0;
	}
*/
	for(int i=0;i<=len;i++){
		c[*&a[i]]++;
	}

	int k = 0;
	for(int i=0;i<=len+2;i++){
		for(int j=0;j<c[i];j++){
		o[k] =  i;
		k++;
		
		}
	}

for (int i=0;i<=len;i++){
		printf("%d\n",o[i]);
	}

free(c);
free(o);

}

int main(){
int a[7] = {3,5,46,7,3,5,6};
int len = 7;
fun(&*a,len);






















/*

int c[len];
	int o[len];
	for (int i=0;i<len;i++){
		c[i] = 0;
		o[i] = 0;
	}

	for(int i=0;i<=len;i++){
		c[a[i]]++;
	}

	int k = 0;
	for(int i=0;i<len;i++){
		for(int j=0;j<c[i];j++,k++){
		o[k] =  i;
		
		}
	}

for (int i=0;i<len;i++){
		printf("%d\n",c[i]);
	}


*/

}
