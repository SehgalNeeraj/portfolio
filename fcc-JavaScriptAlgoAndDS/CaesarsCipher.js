// CAESAR CIPHER
// One of the simplest and most widely known ciphers is a Caesar cipher,
// also known as a shift cipher.
// In a shift cipher the meanings of the letters are shifted by some set amount.
// A common modern use is the ROT13 cipher, where the values of the letters
// are shifted by 13 places.Thus 'A' ↔ 'N', 'B' ↔ 'O' and so on.

// Write a function which takes a ROT13 encoded string as input and returns a
// decoded string.
// All letters will be uppercase. Do not transform any non-alphabetic character (i.e. spaces, punctuation), but do pass them on.

// e.g,
// rot13("SERR PBQR PNZC") should decode to FREE CODE CAMP

// rot13("SERR CVMMN!") should decode to FREE PIZZA!

// rot13("SERR YBIR?") should decode to FREE LOVE?

// rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT.") should decode to
// THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
function isAlpha(character) {
    // #TODO: maybe use RegEX instead???
  if (character.toLowerCase() != character.toUpperCase()) {
    return true;
  }
  return false;
}

function decode(character) {
  // bound b/w A <-> Z
  let ascii = character.charCodeAt() - 13;
  if (ascii < "A".charCodeAt()) {
    ascii = "Z".charCodeAt() - ("A".charCodeAt() - ascii) + 1;
  }

  return String.fromCharCode(ascii);
}

function rot13(input) {
  // 1. iterate thru input
  // 2. ignore non-alpha
  // 3. decode logic
  // 4. print
  let response = "";
  for (let i = 0; i < input.length; ++i) {
    response += isAlpha(input[i]) ? decode(input[i].toUpperCase()) : input[i];
  }
  console.log(response);
}

////////////////////////
////// MAIN
////////////////////////
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

// MAIN
readline.question("", (input) => {
  rot13(input);
  readline.close();
});
