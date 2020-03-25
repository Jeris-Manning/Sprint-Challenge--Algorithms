#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^3) - loop is O(n*n*n), body is calculates as O(1)  [this maybe actually runs at O(n^2) because the body approaches the n^3 loop value with n^2 each iteration?]


b) O(n^2) - while loop of O(n) inside for loop of O(n) both reliant on single variable n O(n*n)


c) O(n) - simple recursion of O(1) processes dropping constants

## Exercise II

I'd approach this problem in the style of a binary search. I'd pick my starting point not at half of n, but
at an estimated egg cracking threshold floor as f.

 If the egg cracks from that floor, I would move down a number of floors relative to the degree of the eggs destruction (possibly to floor 1/2(n - (n-f))) and try another egg.

 I would continue doing this until a dropped egg survived.

 I would then take into account the lowest level from which a dropped egg broke, and move to a floor between that one, and the egg survival floor I'm on.

 I would repeat this, shrinking this range until I am on a floor from which a dropped egg breaks that has a floor directly below it that
an egg can be safely dropped from.

The floor I am on is f.

the runtime would be O(logN)

