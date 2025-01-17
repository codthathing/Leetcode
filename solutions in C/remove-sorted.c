#include <stdio.h>

int removeDuplicates(int *nums, int numsSize)
{
  if (numsSize <= 2)
  {
    return numsSize;
  }

  int k = 2;

  for (int i = 2; i < numsSize; i++)
  {
    if (nums[i] != nums[k - 2])
    {
      nums[k] = nums[i];
      k++;
    }
  }

  return k;
}

void main()
{
  int nums[] = {1, 1, 1, 2, 2, 3};
  int numsSize = sizeof(nums) / sizeof(nums[0]);

  int returnValue = removeDuplicates(nums, numsSize);

  printf("%d", returnValue);
}