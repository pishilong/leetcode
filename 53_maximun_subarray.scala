object Solution {
  def main(args: Array[String]) {
    val testCase = Array(-2, 1, -3, 4, -1, 2, 1, -5, 4);
    // val testCase = Array(-1, -1, -3, -4, -1, -2, -1, -5, -4);

    val result = maxSubArray(testCase);

    println(result);
  }

  def maxSubArray(nums: Array[Int]): Int = {
    val length = nums.length

    val maxArray = nums.clone

    var max = maxArray(0)

    def cal(endLoc: Int): Int = {
      val curValue = nums(endLoc)

      val compValue = if (maxArray(endLoc - 1) < 0) curValue else maxArray(endLoc - 1) + curValue

      max = if (compValue > max) compValue else max

      compValue
    }

    for (endLoc <- 1 to length - 1) {
      maxArray(endLoc) = cal(endLoc)
    }

    max
  }
}
