#include <stdio.h>

int binary_search(int[], int);

int main() {
  int array[] = {1, 2, 3, 4, 5, 6, 7, 8};
  int result = binary_search(array, 8);
  printf("%d\n", result);
}

int binary_search(int array[], int target) {
  int low_index = 0;
  int heigh_index = sizeof(array);
  while (low_index <= heigh_index) {
    int mid_index = (low_index + heigh_index) / 2;
    int guess_value = array[mid_index];
    if (target == guess_value) {
      return mid_index;
    }
    if (target < guess_value) {
      heigh_index = mid_index - 1;
    } else {
      low_index = mid_index + 1;
    }
  }
}
