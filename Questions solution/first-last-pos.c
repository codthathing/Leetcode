#include <stdio.h>
#include <stdlib.h>

int *searchRange(int *nums, int numsSize, int target, int *returnSize)
{
  int *returnArray = (int *)malloc(2 * sizeof(int));
  int enterReturn = 0;
  int mapNums = 0;

  returnArray[0] = -1;
  returnArray[1] = -1;

  while (mapNums < numsSize)
  {
    if (nums[mapNums] == target)
    {
      if (enterReturn == 0)
      {
        returnArray[0] = mapNums;
        enterReturn++;
      }
      returnArray[1] = mapNums;
    }
    mapNums++;
  };

  *returnSize = 2;

  return returnArray;
}

void main()
{
  int nums[] = {1};
  int numsSize = sizeof(nums) / sizeof(nums[0]);
  int target = 1;
  int returnSize;

  int *returns = searchRange(nums, numsSize, target, &returnSize);

  for (int i = 0; i < returnSize; i++)
  {
    printf("%d \n", returns[i]);
  };
}