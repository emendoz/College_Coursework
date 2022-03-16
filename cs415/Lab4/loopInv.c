/* program provides a framework for studying simple loop invariants
   the basic problem is to read a number r and print
   r^0, r^1, r^2, ..., r^10
*/

#include <stdio.h>

int main () {
  int i;
  double prod;
  double r;

  /* read r */
  printf ("Please enter the number r for computing powers:  ");
  scanf ("%lf", &r);
