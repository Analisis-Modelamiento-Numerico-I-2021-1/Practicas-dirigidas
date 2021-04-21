#include <iostream>
#include <array>
#include <numeric>
#include <climits>

int main(int argc, char const *argv[])
{
  std::cout << 1e20 + 1 - 1e20 << "\n";

  std::array<float, 10> x = {0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1};

  for (const auto &i : x)
  {
    std::cout << i << "\n";
  }

  float sum = 0;
  std::cout << std::accumulate(x.begin(), x.end(), sum) << "\n";

  std::cout << INT64_MAX;

  return 0;
}
