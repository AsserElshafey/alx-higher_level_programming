#!/usr/bin/node
const firstArg = process.argv[2];

if (firstArg) {
  console.log('My number: ' + Number(firstArg));
} else {
  console.log('Not a number');
}
