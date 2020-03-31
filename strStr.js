/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
  const stackLength = haystack.length;
  const needleLength = needle.length;
  let idx = 0;
  let needleIdx = 0;
  // KMP部分匹配表，主要看前缀
  // aabab
  const partialTable = [0];
  for (let i = 1; i < needleLength; i++) {
    if (needle[partialTable[i - 1]] === needle[i]) {
      partialTable.push(partialTable[i - 1] + 1);
    } else {
      partialTable.push(0);
    }
  }
  console.log(partialTable);
  while (idx < stackLength) {
    console.log(`idx: ${idx}, needleIdx: ${needleIdx}`);
    const curStack = haystack[idx];
    const curNeedle = needle[needleIdx];

    if (curStack === curNeedle) {
      idx ++;
      needleIdx ++;
    } else {
      idx = idx - needleIdx + partialTable[needleIdx] + 1;
      needleIdx = partialTable[needleIdx];
    }

    if (needleIdx === needleLength) {
      return idx - needleLength;
    }
  }

  return -1;
};

const cases = [{
  haystack: 'hello',
  needle: 'll',
  result: 2
}, {
  haystack: 'aaaaa',
  needle: 'bba',
  result: -1
}, {
  haystack: 'mississippi',
  needle: 'issip',
  result: 4,
}];

cases.forEach(item => {
  console.log(`result: ${strStr(item.haystack, item.needle)}, expected: ${item.result}`);
});
