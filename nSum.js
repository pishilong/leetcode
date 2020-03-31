/**
 * 思路分析
 * 典型的DP，但相比最大自序和问题，这是二维问题
 */

const nums = [1, 0, -1, -2, 2, 3];
const m = 0;
const n = 4;

const answer = [
  [-2, 3, 0, -1],
  [-2, -1, 1, 2],
];

/**
 * 递归算法
 * 核心思想是缩减问题规模： sumN(m, n) = sumN(m - nums[i], n - 1) + nums[i] 考察第i个元素
function sumN(nums, m, n) {
  if (n === 1 && nums.indexOf(m) > -1) return m;
  if (n < 1) return null;

  let result = [];

  nums.forEach((num, idx) => {
    const rest = nums.slice(idx + 1);

    if (rest.length >= n - 1) {
      const _result = sumN(rest, m - num, n - 1);

      if (_result) {
        if (typeof _result === 'number') {
          result.push([_result, num]);
        } else {
          result = result.concat(_result.map(r => r.concat([num])));
        }
      }
    }
  });

  console.log(`nums: ${nums}, m: ${m}, n:${n}, results: ${result}`);
  return result;
}
 */

/**
 * 动态规划的核心是反向构造一个DP表
 *
 * DP表的行为1..n
 * 列为各个可能的和值
 * 单元格i,j的意义为选取i个元素，其和为j的组合
 *
 * 在迭代考察元素i时，其值为nums[i], 在dp表中，单元格[m - nums[i]][n - 1]有值，说明选取n-1个元素，和为m - nums[i]是有组合的，此组合加上nums[i]即为答案
 * 动态规划和递归的区别，只在于动态规划是迭代着构建出dp表，而递归是就地进行计算，如果没有合理的剪枝，会有大量重复计算
 */
function sumNDP(nums, m, n) {
  const dp = new Array(n);

  dp[0] = { 0: []}; // 选取0个元素时，和为0，组合为空
  for (let i = 1; i <= 4; i ++) {
    dp[i] = {};
    const lastSums = Object.keys(dp[i - 1]).map(k => parseInt(k)); // 上一层所有的和值

    nums.forEach(num => {
      lastSums.forEach(lastSum => {
        const newSum = lastSum + num; // 新的组合和值
        if (!dp[i][newSum]) {
          dp[i][newSum] = [];
        }

        const lastCombs = dp[i - 1][lastSum]; // 上一层对应和值的组合
        if (lastCombs.length === 0) {
          dp[i][newSum].push([num]);
        } else {
          lastCombs.forEach(lastComb => {
            if (lastComb.indexOf(num) === -1) { // 不能重复组合元素
              const newComb = lastComb.concat([ num ]).sort();

              const hasDup = dp[i][newSum].some(x => x.join(',') === newComb.join(','));
              if (!hasDup) {
                dp[i][newSum].push(newComb);
              }
            }
          });
        }
      });
    });

    // 移除空的
    for (let s in dp[i]) {
      if (dp[i][s].length === 0) {
        delete dp[i][s];
      }
    }

    console.log(`-------------第${i}层（选取${i}个元素）-----------`);
    console.log(dp[i]);
  }

  return dp[n][m];
}


console.log(sumNDP(nums, m, n));
