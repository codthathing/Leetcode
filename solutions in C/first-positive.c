#include <stdio.h>
#include <stdlib.h>

int cmpfunc(const void *a, const void *b)
{
  int num1 = *(int *)a;
  int num2 = *(int *)b;

  if (num1 > num2)
    return 1;
  else if (num1 < num2)
    return -1;
  else
    return 0;
}

int firstMissingPositive(int *nums, int numsSize)
{
  qsort(nums, numsSize, sizeof(int), cmpfunc);

  int mapNum = 0;
  int maxPositive = 1;

  while (mapNum < numsSize)
  {
    if (nums[mapNum] > 0 && nums[mapNum] == maxPositive)
    {
      maxPositive++;
    }
    mapNum++;
  }

  return maxPositive;
}

void main()
{
  int nums[] = {1, 2, 0};
  int numsSize = sizeof(nums) / sizeof(nums[0]);

  int maxPositive = firstMissingPositive(nums, numsSize);

  printf("%d", maxPositive);
}