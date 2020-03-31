/**
 *      1
 *    2      3
 *  4   5   6
 * 7          8
 *          9
 */


const nums = [
  {
    id: 1,
    left: 2,
    right: 3,
  },
  {
    id: 2,
    left: 4,
    right: 5,
  },
  {
    id: 3,
    left: 6,
    right: null,
  },
  {
    id: 4,
    left: 7,
    right: null,
  },
  {
    id: 5,
    left: null,
    right: null,
  },
  {
    id: 6,
    left: null,
    right: 8,
  },
  {
    id: 7,
    left: null,
    right: null,
  },
  {
    id: 8,
    left: null,
    right: 9,
  },
  {
    id: 9,
    left: null,
    right: null,
  }
];

function Node(id) {
  this.id = id;
  this.left = null;
  this.right = null;
}

let root = null;
function buildTree() {
  const nodes = nums.map(num => new Node(num.id));

  root = nodes[0];

  nums.forEach(num => {
    const curNode = nodes.find(n => n.id === num.id);
    if (num.left) {
      curNode.left = nodes.find(n => n.id === num.left);
    }

    if (num.right) {
      curNode.right = nodes.find(n => n.id === num.right);
    }
  });
}
buildTree();

const unvisited = [root];
root.depth = 1;
let maxDepth = 0;

while (unvisited.length > 0) {
  const curNode = unvisited.pop();

  if (!curNode.left && !curNode.right) {
    maxDepth = Math.max(maxDepth, curNode.depth);
  }

  if (curNode.right) {
    curNode.right.depth = curNode.depth + 1;
    unvisited.push(curNode.right);
  }

  if (curNode.left) {
    curNode.left.depth = curNode.depth + 1;
    unvisited.push(curNode.left);
  }
}

console.log(maxDepth);

console.log(typeof typeof [])
console.log([1,2,3,4,5].map(parseInt));