#include <stdio.h>
#include <stdlib.h>

int maxArea(int *height, int heightSize)
{
  int maxArea = 0;

  int firstPole = 0;
  int lastPole = heightSize - 1;

  while ((lastPole - firstPole) != 0)
  {
    int newArea;

    if (height[lastPole] <= height[firstPole])
    {
      newArea = height[lastPole] * (lastPole - firstPole);
      lastPole--;
    }
    else if (height[firstPole] <= height[lastPole])
    {
      newArea = height[firstPole] * (lastPole - firstPole);
      firstPole++;
    }

    if (newArea > maxArea)
    {
      maxArea = newArea;
    }
  }

  return maxArea;
}

void main()
{
  int height[] = {1,1};
  int heightSize = sizeof(height) / sizeof(height[0]);

  int maxAreaValue = maxArea(height, heightSize);

  printf("%d", maxAreaValue);
}