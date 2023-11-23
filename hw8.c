#include <math.h>
#include <stdio.h>
int calculateSD(int data[]);
int main() 
{
    int i;
    int data[10];
    printf("5개의 요소 입력: ");
    for (i = 0; i < 5; ++i)
        scanf("%f", &data[i]);
    printf("\n표준 편차 = %.6f", calculateSD(data));
    return 0;
}
 
int calculateSD(int data[]) 
{
    int sum = 0.0, mean, SD = 0.0;
    int i;
    for (i = 0; i < 5; ++i) {
        sum += data[i];
    }
    mean = sum / 5;
    for (i = 0; i < 5; ++i)
        SD += pow(data[i] - mean, 2);
    return sqrt(SD / 5);
}
