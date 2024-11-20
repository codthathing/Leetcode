#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool searchMatrix(int matrix[3][4], int matrixSize, int *matrixColSize, int target)
{
  int verticalPointer = 0;
  int horizontalPointer = 0;

  while (verticalPointer < matrixSize)
  {
    while (horizontalPointer < matrixColSize[verticalPointer])
    {
      if (matrix[verticalPointer][horizontalPointer] == target)
      {
        return true;
      };
      horizontalPointer++;
    };

    horizontalPointer = 0;
    verticalPointer++;
  };

  return false;
};

void main()
{
  int matrix[3][4] = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
  int matrixSize = sizeof(matrix) / sizeof(matrix[0]);
  int matrixColSize[] = {4, 4, 4};
  int target = 13;

  int returnValue = searchMatrix(matrix, matrixSize, matrixColSize, target);

  printf("%d", returnValue);
};