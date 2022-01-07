/************************************************************************************************/
/* Program: Ex4a.cpp                                                                            */
/* Author: Erika Mendoza                                                                        */
/* Date: September 23, 2021                                                                     */
/* Description: This file creates a quadratic bezier curve through points.                      */
/************************************************************************************************/

#include <iostream>
#include <fstream>
#include <vector>
#include "Bitmap_Image.hpp"
using namespace std;

/************************************************************************************************/
/* Data structure: Point                                                                        */
/* Description: A struct containing two float arguments to use as points.                       */
/************************************************************************************************/

struct Point
{
        float x;
        float y;
};

/************************************************************************************************/
/* Prototypes                                                                                   */
/************************************************************************************************/

Point GetPoint (float percent, const Point & P1, const Point& P2, const Point & P3);

/************************************************************************************************/
/* Function: main                                                                               */
/* Arguments:  int argc, char * argv []                                                         */
/* Description:  This function generates and saves a bitmap_image for the function calls made.  */
/************************************************************************************************/

int main (int argc, char * argv [])
{
        if (argc < 3)
        {
                cerr << "Usage: " << argv[0] << " <input_file> <bitmap_file>\n";
                exit (1);
        }
        ifstream input (argv[1]);
        if (input.fail())
        {
                cerr << "File: " << argv[1] << " cannot be opened.\n";
                exit (2);
        }
        ofstream output (argv[2]);

        float num;
        for (int i = 1; i <= 7; i++) {
        int N = int(num);
        filein >> num >> P1.x >> P1.y >> P2.x >> P2.x >> P3.y;
        switch (i) {
            case 1:
                //
                                break;
            case 'H' | 'h': // Set hue (color)
                input >> red >> green >> blue;
                break;
        }
    }
        input.close();
        output.close();
        return 0;
}

/************************************************************************************************/
/* Function: GetPoint                                                                           */
/* Arguments: float percent, const Point & P1, const Point& P2, const Point & P3                */
/* Description: returns a Quadratic Bezier Curve                                                */
/************************************************************************************************/

Point GetPoint (float percent, const Point & P1, const Point& P2, const Point & P3)
{
        Point P;
        if (P.size() == 3) {
                //return quadratic solution

                for (int i = 0; i <= N; i++) {
                        float percent = float(i) / N;
                        Point B = GetPoint(percent, P1, P2, P3);
                        Curve,.push_back(B);
                }
        }

        vector <Point> Q;
        for (int i = 1; i < P.size(); i++) {
                Point R;
                // Point R is calculate using P[i-1] and P[i]
                R.x = P[i-1].x + percent * (P[i].x - P[i-1].x);
                R.y = P[i-1].y + percent * (P[i].y - P[i-1].y);
                Q.push_back(R);
        }

        return GetPoint(percent, Q);
}
