#include <stdio.h>
int main(void)
{
	int num1, num2;
	printf("�� ���� ���� �Է�: ");
	scanf_s("%d %d", &num1, &num2);
	int num3 = num1 & num2;
	printf("AND ������ ���: %d \n", num3);
	int num4 = num1 | num2;
	printf("OR ������ ���: %d \n", num4);
	int num5 = num1 ^ num2;
	printf("XOR ������ ���: %d \n", num5);
	return 0;
}