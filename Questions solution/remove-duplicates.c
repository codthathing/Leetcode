#include <stdio.h>

int removeDuplicates(int *nums, int numsSize)
{
  int j = 0;

  for (int i = 0; i < numsSize - 1; i++)
  {
    if (nums[i] != nums[i + 1])
    {
      nums[j] = nums[i];
      j++;
    }
  }

  nums[j] = nums[numsSize - 1];
  j++;

  return j;
}

int main()
{
  int nums[] = {0,0,1,1,1,2,2,3,3,4};
  int actualLength = sizeof(nums) / sizeof(nums[0]);

  int k = removeDuplicates(nums, actualLength);

  for (int i = 0; i < k; i++)
  {
    printf("%d", nums[i]);
  }

  return 0;
}