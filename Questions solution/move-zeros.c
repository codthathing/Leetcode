#include <stdio.h>
#include <stdlib.h>

void main()
{
  int nums[] = {0, 1, 0, 3, 12};
  int numsSize = sizeof(nums) / sizeof(nums[0]);
  int mapNums = 0;

  for (int i = 0; i < numsSize; i++) {
    if(nums[i] != 0) {
      nums[mapNums] = nums[i];
      mapNums++;
    }
  }

  while (mapNums < numsSize)
  {
    nums[mapNums] = 0;
    mapNums++;
  }

  for (int i = 0; i < numsSize; i++)
  {
    printf("%d \n", nums[i]);
  }
}