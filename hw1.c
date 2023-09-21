#include <stdio.h>
int main(void)
{
	int num1, num2;
	printf("두 개의 정수 입력: ");
	scanf_s("%d %d", &num1, &num2);
	int num3 = num1 & num2;
	printf("AND 연산의 결과: %d \n", num3);
	int num4 = num1 | num2;
	printf("OR 연산의 결과: %d \n", num4);
	int num5 = num1 ^ num2;
	printf("XOR 연산의 결과: %d \n", num5);
	return 0;
}