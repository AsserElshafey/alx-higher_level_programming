#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const firstArg = process.argv[2];
const secondArg = process.argv[3];

const firstNum = parseInt(firstArg);
const secondNum = parseInt(secondArg);

console.log(add(firstNum, secondNum));
