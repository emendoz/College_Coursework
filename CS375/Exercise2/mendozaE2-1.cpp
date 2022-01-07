/*****************************************************************/
/*                                                               */
/* Assignment: CS 375 Exercise 2 Part 1                          */
/* File: mendozaE2-1.cpp                                         */
/* Author: Erika Mendoza                                         */
/* Date: 26 August 2021                                          */
/* Description: This program will read the endpoints of a line   */
/*              segment and write out the coordinates of the     */
/*              integer points between and including the end     */
/*              points.                                          */
/*                                                               */
/*****************************************************************/

#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        float rise = y2 - y1;
        float run = x2 - x1;
        float m = rise / run;
        //cout << "The slope is " << m << endl;
        float b = y1 - m * x1;
        //cout << "The y-intercept is " << b << endl;

        if( x1 == x2 ) { // Vertical Line
                if( y1 < y2) { //Starting point y is less
                        for( int y = y1; y <= y2; y++ ){
                                cout  << x1 << ',' << y << endl;
                        }
                } else { //Starting point y is greater
                        for( int y = y1; y >= y2; y-- ) {
                                cout << x1 << ',' << y << endl;
                        }
                }
        }

        else if( abs(run) >= abs(rise) ) { // |run| >= |rise|
                if( x1 < x2 ){
                        for( int x = x1; x <= x2; x++ ){
                                int y = m * x + b + 0.5;
                                cout << x << ',' << y << endl;
                        }
                } else {
                        for( int x = x1; x >= x2; x-- ) {
                                int y = m * x + b + 0.5;
                                cout << x << ',' << y << endl;
                        }
                }
        }

        else if( abs(rise) >= abs(run) ) { // |rise| >= |run|
                if( y1 < y2 ) {
                        for( int y = y1; y <= y2; y++ ) {
                                int x = (y - b) / m + 0.5;
                                cout << x << ',' << y << endl;
                        }
                } else {
                        for( int y = y1; y > y2; y-- ) {
                                int x = (y - b) / m + 0.5;
                                cout << x << ',' << y << endl;
                        }
                }
        }
        }

        return 0;
}
