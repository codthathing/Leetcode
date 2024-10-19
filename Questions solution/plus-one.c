#include <stdio.h>
#include <stdlib.h>

int *plusOne(int *digits, int digitsSize, int *returnSize)
{
  int *returnArray = (int *)malloc((digitsSize + 1) * sizeof(int));
  int carry = 1;
  int mapDigits;

  for (mapDigits = digitsSize - 1; mapDigits >= 0; mapDigits--)
  {
    int sum = digits[mapDigits] + carry;
    carry = sum / 10;
    returnArray[mapDigits + 1] = sum % 10;
  }

  if (carry)
  {
    returnArray[0] = 1;
    *returnSize = digitsSize + 1;
  }
  else
  {
    for (mapDigits = 0; mapDigits < digitsSize; mapDigits++)
    {
      returnArray[mapDigits] = returnArray[mapDigits + 1];
    }
    *returnSize = digitsSize;
  }

  return returnArray;
}

void main()
{
  int digits[] = {9};
  int digitsSize = sizeof(digits) / sizeof(digits[0]);
  int returnSize;

  int *returnArray = plusOne(digits, digitsSize, &returnSize);

  for (int i = 0; i < returnSize; i++)
  {
    printf("%d \n", returnArray[i]);
  }
}