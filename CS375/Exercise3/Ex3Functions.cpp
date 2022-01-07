/************************************************************************************************/
/* Program: Exercise 3 Graphics Program                                                         */
/* File: Ex3Functions.cpp                                                                       */
/* Author: Dr. Watts                                                                            */
/* Date: 1 September 2021                                                                       */
/* Modified by: Erika Mendoza                                                                   */
/* Date: 16 September 2021                                                                      */
/* Description: This program will read shape parameters from an input file and will create      */
/*              a bitmap file illustrating the shapes.                                          */
/*              This file contains a DrawLine function, DrawRectangle function, DrawCircle      */
/*              function, and a DrawEllipse function.                                           */
/************************************************************************************************/

#include <iostream>
#include <fstream>
#include <cmath>
#include "Bitmap_Image.hpp"
#include "Ex3Functions.h"
using namespace std;

/************************************************************************************************/
/* Function: DrawLine                                                                           */
/* Arguments: bitmap_image & bmp, int x1, int y1, int x2, int y2, int red, int green, int blue  */
/* Description: This function creates a line of pixels from one set of end points to the other  */
/* set of endpoints provided.                                                                   */
/************************************************************************************************/

void DrawLine (bitmap_image & bmp, int x1, int y1, int x2, int y2, int red, int green, int blue) {

        float rise = y2 - y1;
        float run = x2 - x1;
        float m = rise / run;
        //cout << "The slope is " << m << endl;
        float b = y1 - m * x1;
        //cout << "The y-intercept is " << b << endl;

        if( x1 == x2 ) { // Vertical Line
                if( y1 < y2) { //Starting point y is less
                        for( int y = y1; y <= y2; y++ ){
                                bmp.set_pixel (x1, y, red, green, blue);
                        }
                } else { //Starting point y is greater
                        for( int y = y1; y >= y2; y-- ) {
                                bmp.set_pixel (x1, y, red, green, blue);
                        }
                }
        }

        else if( abs(run) >= abs(rise) ) { // |run| >= |rise|
                if( x1 < x2 ) {
                        for( int x = x1; x <= x2; x++ ){
                                int y = m * x + b + 0.5;
                                bmp.set_pixel (x, y, red, green, blue);
                        }
                } else {
                        for( int x = x1; x >= x2; x-- ) {
                                int y = m * x + b + 0.5;
                                bmp.set_pixel (x, y, red, green, blue);
                        }
                }
        }

        else if( abs(rise) >= abs(run) ) { // |rise| >= |run|
                if( y1 < y2 ) {
                        for( int y = y1; y <= y2; y++ ) {
                                int x = (y - b) / m + 0.5;
                                bmp.set_pixel (x, y, red, green, blue);
                        }
                } else {
                        for( int y = y1; y > y2; y-- ) {
                                int x = (y - b) / m + 0.5;
                                bmp.set_pixel (x, y, red, green, blue);
                        }
                }
        }

}

/************************************************************************************************/
/* Function: DrawRectangle                                                                      */
/* Arguments: bitmap_image & bmp, int ulX, int ulY, int width, int height, int red, int green,  */
/* int blue                                                                                     */
/* Description: This function creates a rectangle of pixels.                                    */
/************************************************************************************************/

void DrawRectangle (bitmap_image & bmp, int ulX, int ulY, int width, int height, int red, int green, int blue) {

        //upper left corner
        int c1x = ulX;
        int c1y = ulY;
        //upper right corner
        int c2x = ulX + width;
        int c2y = ulY;
        //lower left corner
        int c3x = ulX;
        int c3y = ulY + height;
        //lower right corner
        int c4x = ulX + width;
        int c4y = ulY + height;

        //upper left corner to upper right corner
        DrawLine (bmp, c1x, c1y, c2x, c2y, red, green, blue);
        //upper left corner to lower left corner
        DrawLine (bmp, c1x, c1y, c3x, c3y, red, green, blue);
        //upper right corner to lower right corner
        DrawLine (bmp, c2x, c2y, c4x, c4y, red, green, blue);
        //lower left corner to lower right corner
        DrawLine (bmp, c3x, c3y, c4x, c4y, red, green, blue);

}

/************************************************************************************************/
/* Function: DrawCircle                                                                         */
/* Arguments: void DrawCircle (bitmap_image & bmp, int centerX, int centerY, int radius,        */
/* int red, int green, int blue)                                                                */
/* Description: This function creates a circle of pixels.                                       */
/************************************************************************************************/

void DrawCircle (bitmap_image & bmp, int centerX, int centerY, int radius, int red, int green, int blue) {

for (float a = 0; a < 2*M_PI; a += 0.1)
{
        float x = radius * cos (a) + centerX;
        float y = radius * sin (a) + centerY;
        bmp.set_pixel(x, y, 0, 0, 0);
}

/* 
        // Alternative way of generating a cirle
        for( float a = 0; a < 360; a += 0.03) {
                int x = radius * sin(a);
                int y = radius * cos(a);
                bmp.set_pixel(x + centerX, y + centerY, red, green, blue);
        }
*/
}

/************************************************************************************************/
/* Function: DrawEllipse                                                                        */
/* Arguments: bitmap_image & bmp, int centerX, int centerY, int radiusX, int radiusY,           */
/* int red, int green, int blue                                                                 */
/* Description: This function creates an ellipse of pixels.                                     */
/************************************************************************************************/

void DrawEllipse (bitmap_image & bmp, int centerX, int centerY, int radiusX, int radiusY, int red, int green, int blue) {

        for( float a = 0; a < 360; a += 0.03) {
                int x = radiusX * sin(a);
                int y = radiusY * cos(a);
                bmp.set_pixel(x + centerX, y + centerY, red, green, blue);
        }

}
