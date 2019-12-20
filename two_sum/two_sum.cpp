#include <iostream>
#include <vector>
#include <array>
#include <unordered_map>

using namespace std;

array<int, 2> two_sum(vector<int> input, int target);

int
main(int argc, char **argv) {
  array<int, 2> result = two_sum(vector<int>{2, 7, 11, 15}, 9);
  for (auto i : result)
    cout << i << endl;
  return 0;
}

array<int, 2> 
two_sum(vector<int> input, int target) {
  unordered_map<int, int> h;
  for (int i = 0; i <= input.size(); i++){
    try {
      int j = h.at(target - input[i]);
      return array<int, 2> {j, i};
    } catch (const std::out_of_range&) {
      h[input[i]] = i;
    }
  }
  return array<int, 2>{};
}
