/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
  const size = matrix.length;
  /**
   * 旋转一层
   * 第idx行到第size - idx - 1列
   * 第size - idx - 1列到size - idx - 1行
   * 第size - idx - 1行到第idx列
   * 第idx列到第idx行
   * @param {int} idx
   */
  const rotateLayer = (idx) => {
    console.log('----start rotate layer', idx);
    for (let i = 0; i < size / 2; i ++) {
      const stash = matrix[i][size - idx -1];
      console.log(matrix);
      matrix[i][size - idx - 1] = matrix[idx][i];
      console.log(matrix);
      matrix[idx][i] = matrix[size - i - 1][idx];
      console.log(matrix);
      matrix[size - i - 1][idx] = matrix[size - idx - 1][size - i -1];
      console.log(matrix);
      matrix[size - idx - 1][size - i - 1] = stash;
      console.log(matrix);
      console.log('-----------------')
    }
  };

  /**
   * 旋转需要pair, 一共旋转parseInt(size / 2)
   */
  for (let i = 0; i < parseInt(size / 2); i ++) {
    rotateLayer(i);
  }
};

// let matrix = [
//   [1,2,3],
//   [4,5,6],
//   [7,8,9]
// ];

let matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
];

rotate(matrix);
console.log(matrix);