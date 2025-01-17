#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int returnMax(int *candies, int candiesSize)
{
  int maxNum = 0;
  for (int i = 0; i < candiesSize; i++)
  {
    if (candies[i] > maxNum)
    {
      maxNum = candies[i];
    }
  }
  return maxNum;
}

bool *kidsWithCandies(int *candies, int candiesSize, int extraCandies, int *returnSize)
{
  bool *returnArray = (bool *)malloc(candiesSize * sizeof(bool));
  int maxNum = returnMax(candies, candiesSize);

  for (int i = 0; i < candiesSize; i++)
  {
    if ((candies[i] + extraCandies) >= maxNum)
    {
      returnArray[i] = true;
    }
    else
    {
      returnArray[i] = false;
    }
  }

  *returnSize = candiesSize;

  return returnArray;
}

void main()
{
  int candies[] = {12, 1, 12};
  int candiesSize = sizeof(candies) / sizeof(candies[0]);
  int extraCandies = 10;
  int returnSize;

  bool *returnArray = kidsWithCandies(candies, candiesSize, extraCandies, &returnSize);

  for (int i = 0; i < candiesSize; i++)
  {
    printf("%d \n", returnArray[i]);
  }

  free(returnArray);
}