#!/usr/bin/node

const size = parseInt(Number(process.argv[2]));
if (!size) {
  console.log('Missing size');
} else {
  let character = 'X';
  for (let i = 0; i < size; i++) {
    if (character.length === 1) {
      for (let j = 0; j < (size - 1); j++) {
        character = character + 'X';
      }
    }
    console.log(character);
  }
}
