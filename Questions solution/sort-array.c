#include <stdio.h>

int sortArray(int *nums, int numsSize) {
  int mapNum = 0;
  int compareNum = 0;
  int mapValue;
  int compareValue;

  while (mapNum < numsSize)
  {
    while (compareNum < mapNum)
    {
      mapValue = nums[mapNum];
      compareValue = nums[compareNum];
      if (nums[mapNum] < nums[compareNum])
      {
        nums[mapNum] = compareValue;
        nums[compareNum] = mapValue;
      }
      compareNum++;
    }
    compareNum = 0;
    mapNum++;
  }
}

void main()
{
  int nums[] = {3, 4, -1, 1};
  int numsSize = sizeof(nums) / sizeof(nums[0]);

  sortArray(nums, numsSize);

  for (int i = 0; i < numsSize; i++)
  {
    printf("%d \n", nums[i]);
  }
}