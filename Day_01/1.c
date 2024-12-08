#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define MIN(x,y) (x>y?y:x)
#define MAX(x,y) (x>y?x:y)


void read_lists(char* filename, int* list_1, int* list_2) {
    FILE* file = fopen(filename, "r");

    int index = 0;
    while (fscanf(file, "%d   %d", &(list_1[index]), &(list_2[index])) > 0) {
        index++;
    }

    fclose(file);
}

void sort_list(int* list, int n) {
    int* sorter_help = malloc(n*sizeof(int));

    int max = 0;
    for (int i = 0; i < n; i++) {
        if (max < list[i]) max = list[i];
    }
    
    int min_index;
    int min;
    int sorter_index = 0;
    while (sorter_index < 1000) {
        min = list[0];
        min_index = 0;
        for (int i = 0; i < n; i++) {
            if (min > list[i]) {
                min_index = i; 
                min = list[min_index];
            }
        }
        sorter_help[sorter_index] = min;
        list[min_index] = max;
        sorter_index++;
    }

    for (int i = 0; i < n; i++) {
        list[i] = sorter_help[i];
    }

    free(sorter_help);
}

void print_lists(int* list_1, int* list_2, int n) {
    for (int i = 0; i < n; i++) {
        printf("%d   %d\n", list_1[i], list_2[i]);
    }
}

int* difference(int* list_1, int* list_2, int n) {
    int* return_list = malloc(n*sizeof(int));

    for (int i = 0; i < n; i++) {
        return_list[i] = MAX(list_1[i], list_2[i]) - MIN(list_2[i], list_1[i]);
    }
    

    free(list_1);
    free(list_2);
    return return_list;
}

int sum(int* list, int n) {
    int somme = 0;
    for (int i = 0; i < n; i++) {
        somme += list[i];
    }
    free(list);
    return somme;
}

int count_occurences(int* list, int taille, int occurence) {
    int nombre = 0;
    for (int i = 0; i < taille; i++) {
        if (list[i] == occurence) nombre ++;
    }
    return nombre;
}

int main(int argc, char** argv) {
    assert(argc>2);
    if (argv[2][0] == '1') {
        /*First star*/
        int* list_1 = malloc(1000*sizeof(int));
        int* list_2 = malloc(1000*sizeof(int));
        read_lists(argv[1], list_1, list_2);
        sort_list(list_1, 1000);
        sort_list(list_2, 1000);
        int* list = difference(list_1, list_2, 1000);
        printf("%d\n", sum(list, 1000));
    } else {
        /*Second Star*/
        int* list_1 = malloc(1000*sizeof(int));
        int* list_2 = malloc(1000*sizeof(int));
        read_lists(argv[1], list_1, list_2);
        int somme = 0;
        for (int i = 0; i < 1000; i++) {
            somme += list_1[i] * count_occurences(list_2, 1000, list_1[i]);
        }
        printf("%d\n", somme);
        free(list_1);
        free(list_2);
    }
    return 0;
}