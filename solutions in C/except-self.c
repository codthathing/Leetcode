#include <stdio.h>
#include <stdlib.h>

int *productExceptSelf(int *nums, int numsSize, int *returnSize)
{
  int *returnArray = (int *)malloc(numsSize * sizeof(int));
  int mapNum = 0;
  int multNum = 0;
  int sum = 1;

  while (mapNum < numsSize)
  {
    while (multNum < numsSize)
    {
      if (multNum != mapNum)
      {
        sum *= nums[multNum];
        multNum++;
      }
      else
      {
        multNum++;
      }
    }
    returnArray[mapNum] = sum;
    sum = 1;
    multNum = 0;
    mapNum++;
  }
  *returnSize = numsSize;
  return returnArray;
}

void main()
{
  int nums[] = {0, 4, 0};
  int numsSize = sizeof(nums) / sizeof(nums[0]);
  int returnSize;

  int *returnArray = productExceptSelf(nums, numsSize, &returnSize);

  for (int i = 0; i < numsSize; i++)
  {
    printf("%d \n", returnArray[i]);
  }
}