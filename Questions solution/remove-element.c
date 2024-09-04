#include <stdio.h>

int main() {
  int nums[] = {3, 2, 2, 3, 6};
  int expectedNums[5];

  for (int i = 0; i < sizeof(nums) / sizeof(nums[0]); i++) {
    for (int j = 0; j < 3; j++) {
      if (nums[i] != 3) {
        expectedNums[j] = nums[i];
      }
    }
  }

  for (int i = 0; i < 3; i++) {
    printf("%d", expectedNums[i]);
  }

  return 0;
}