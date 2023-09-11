#!/usr/bin/node
const args = process.argv.slice(2);

const nums = args.map(arg => parseInt(arg));

nums.sort((a, b) => b - a);

if (nums.length < 2) {
  console.log(0);
} else {
  console.log(nums[1]);
}
