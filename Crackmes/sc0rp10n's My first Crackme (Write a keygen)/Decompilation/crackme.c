#include <stdio.h>
#include <string.h>
#include <stdbool.h>

const int keySegmentLength = 4;
const int keySegmentCount = 4;

// returns true if input is prime
bool isPrime(int number)

{
  bool returnVal;
  int i;
  
  if ((number == 0) || (number == 1)) {
    returnVal = false;
  }
  else {
    for (i = 2; i < number / 2; i++) {
      if (number % i == 0) {
        return false;
      }
    }
    returnVal = true;
  }
  return returnVal;
}



bool keyCheck(char inputKey[])

{
  int charBlockSum;
  int lastCharBlockSum = 0;
  
  int i = 0;
  while( true ) {
    if (keySegmentCount <= i) {
      return true;
    }
    charBlockSum = 0;
    for (int j = 0; j < keySegmentLength; j++) {
      charBlockSum += inputKey[j + i * 5];
    }
    if (!isPrime(charBlockSum)) break;
    if (charBlockSum <= lastCharBlockSum) {
      return false;
    }
    lastCharBlockSum = charBlockSum;
    i++;
  }
  return false;
}



bool checkKeyFormat(char *input_key)

{
  bool retVal;
  
  long keylength = strlen(input_key);
                    // keylength == 19     (4+4*4-1=19)
  if (keylength == keySegmentLength + keySegmentLength * keySegmentCount - 1) {
                    // for i=0;i<3;i++
    for (int i = 0; i < keySegmentCount - 1; i++) {
                    // check if format is xxxx-xxxx-xxxx-xxxx
      if (input_key[keySegmentLength + (keySegmentLength + 1) * i] != '-') {
        return false;
      }
    }
    retVal = true;
  }
  else {
    retVal = false;
  }
  return retVal;
}

int main(int argc, char* argv[])

{
  if (argc == 2) {
    if (checkKeyFormat(argv[1])) {
      if (keyCheck(argv[1])) {
        puts("Access granted!");
      }
      else {
        puts("Invalid key!");
      }
    }
    else {
      puts("Invalid key!");
    }
  }
  else {
    puts("Usage: <key>");
  }
  return 0;
}
