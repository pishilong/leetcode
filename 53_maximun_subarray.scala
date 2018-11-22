object Solution {
  def main(args: Array[String]) {
    val testCase = Array(-2, 1, -3, 4, -1, 2, 1, -5, 4);

    val result = maxSubArray(testCase);

    println(result);
  }

  def maxSubArray(nums: Array[Int]): Int = {
    var result = 0;

    for (endLoc <- 1 to nums.length) {
      val currentSubArray = nums.slice(0, endLoc);

      val currentValue = nums( endLoc - 1 );

      if (currentValue > 0 && maxSubArray(currentSubArray) + currentValue > result) {
        result = maxSubArray(currentSubArray) + currentValue;
      }
    }

    result
  }
}
