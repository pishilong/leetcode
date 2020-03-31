/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
  const addElem = (exists, elem) => {
    if (elem !== ".") {
      const idx = parseInt(elem);
      if (exists[idx]) {
        return false;
      }
      exists[idx] = elem;
    }
    return true;
  };

  const blocks = Array(9).fill();
  for (let i = 0; i < 9; i++) {
    const row = Array(9).fill(null);
    const column = Array(9).fill(null);
    for (let j = 0; j < 9; j ++) {
      const rowElem = board[i][j];
      if (!addElem(row, rowElem)) {
        return  false;
      }
      const columnElem = board[j][i];
      if (!addElem(column, columnElem)) {
        return false;
      }

      const blockIdx = 3 * parseInt(i / 3) + parseInt(j / 3);
      if (!blocks[blockIdx]) {
        blocks[blockIdx] = Array(9).fill(null);
      }
      if (!addElem(blocks[blockIdx], rowElem)) {
        return false;
      }
    }
  }

  return true;
};

// const board = [
//   ["5", "3", ".", ".", "7", ".", ".", ".", "."],
//   ["6", ".", ".", "1", "9", "5", ".", ".", "."],
//   [".", "9", "8", ".", ".", ".", ".", "6", "."],
//   ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
//   ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
//   ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
//   [".", "6", ".", ".", ".", ".", "2", "8", "."],
//   [".", ".", ".", "4", "1", "9", ".", ".", "5"],
//   [".", ".", ".", ".", "8", ".", ".", "7", "9"]
// ];

const board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
];

console.log(isValidSudoku(board))