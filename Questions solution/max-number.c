#include <stdio.h>

int maxOperations(int *nums, int numsSize, int k)
{
  int pairsSum = 0;
  int firstPoint = 0;
  int lastPoint = numsSize - 1;

  while (firstPoint < lastPoint)
  {
    if ((nums[firstPoint] + nums[lastPoint]) == k)
    {
      pairsSum++;
      firstPoint++;
      lastPoint--;
    }
    else
    {
      if (nums[firstPoint] < k && nums[firstPoint] < nums[lastPoint])
      {
        lastPoint--;
      }
      else if (nums[lastPoint] < k && nums[lastPoint] < nums[firstPoint])
      {
        lastPoint--;
      }
      else
      {
        firstPoint++;
        lastPoint--;
      }
    }
  }

  return pairsSum;
}

void main()
{
  int nums[] = {2,2,2,3,1,1,4,1};
  int numsSize = sizeof(nums) / sizeof(nums[0]);
  int k = 4;

  int pairsSum = maxOperations(nums, numsSize, k);

  printf("%d", pairsSum);
}