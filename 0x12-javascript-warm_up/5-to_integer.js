#!/usr/bin/node
let firstArg = process.argv[2];

let num = parseInt(firstArg);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
