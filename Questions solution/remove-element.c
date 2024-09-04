#include <stdio.h>

int removeElements(int nums[], int numsSize, int val) {
  int j = 0;

  for (int i = 0; i < numsSize; i++) {
    if (nums[i] != val) {
      nums[j] = nums[i];
      j++;
    }
  }

  return j;
}

int main() {
  int nums[] = {3, 2, 2, 3};
  int actualLength = sizeof(nums) / sizeof(nums[0]);
  int val = 3;

  int k = removeElements(nums, actualLength, val);

  for (int i = 0; i < k; i++) {
    printf("%d", nums[i]);
  }

  return 0;
}