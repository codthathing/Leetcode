#include <stdio.h>

int search(int *nums, int numsSize, int target)
{
  int numCount = 0;

  while (numCount < numsSize)
  {
    if (nums[numCount] == target)
    {
      return numCount;
    }
    numCount++;
  }

  return -1;
}

void main()
{
  int nums[] = {1};
  int target = 0;
  int numsSize = sizeof(nums) / sizeof(nums[0]);

  int numReturn = search(nums, numsSize, target);

  printf("%d", numReturn);
}