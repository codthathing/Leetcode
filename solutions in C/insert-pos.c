#include <stdio.h>

int searchInsert(int *nums, int numsSize, int target)
{
  int mapNum = 0;

  while (mapNum < numsSize)
  {
    if (nums[mapNum] == target)
    {
      return mapNum;
    }
    else if (nums[mapNum] > target)
    {
      return mapNum;
    }
    mapNum++;
  }

  return mapNum;
}

void main()
{
  int nums[] = {1, 3, 5, 6};
  int numsSize = sizeof(nums) / sizeof(nums[0]);
  int target = 7;

  int insertPos = searchInsert(nums, numsSize, target);

  printf("%d", insertPos);
}