/************************************************************************************************/
/* Program: Exercise 2 Part 2                                                                   */
/* Author: Dr. Watts                                                                            */
/* Modified by: Erika Mendoza                                                                   */
/* Date: September 7, 2021                                                                      */
/* Description: This program uses a point calculation algorithm to draw a line segment between  */
/* 2 points in a bitmap image.                                                                  */
/************************************************************************************************/

#include <iostream>
#include <fstream>
#include <cmath>
#include "Bitmap_Image.hpp"
using namespace std;

// Function Prototypes
void DrawLine (bitmap_image & bmp, int x1, int y1, int x2, int y2, int red, int green, int blue);

/************************************************************************************************/
/* Function: main                                                                               */
/* Arguments: int argc, char * argv []                                                          */
/* Description: This function generates and saves a bitmap_image that holds the drawn lines     */
/* that are created from the endpoints provided to the DrawLine function.                       */
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
        int width, height;
        input >> width >> height;
        bitmap_image bitmap = bitmap_image (width+1, height+1);
        if (bitmap.failed())
        {
                cerr << "Bitmap could not be created\n";
                exit (3);
        }
        bitmap.clear(0xFF);
        int r = 0, g = 0, b = 0;
        input >> r >> g >> b;
        int x1, y1, x2, y2;
        while (input >> x1 >> y1 >> x2 >> y2)
        {
                cout << "Drawing line from (" << x1 << ',' << y1
                     << ") to (" << x2 << ',' << y2 << ")\n";
                DrawLine (bitmap, x1, y1, x2, y2, r, g, b);
        }
        input.close();
        bitmap.save_image (argv[2]);
        if (bitmap.failed())
        {
                cerr << "Bitmap could not be saved\n";
                exit (4);
        }
        return 0;
}

/************************************************************************************************/
/* Function: DrawLine                                                                           */
/* Arguments: bitmap_image & bmp, int x1, int y1, int x2, int y2, int red, int green, int blue  */
/* Description:  This function creates a line of pixels from one set of end points to the other */
/* set of endpoints provided.                                                                   */
/************************************************************************************************/

void DrawLine (bitmap_image & bmp, int x1, int y1, int x2, int y2, int red, int green, int blue) {

        //bmp.set_pixel (x1, y1, red, green, blue);
        //bmp.set_pixel (x2, y2, red, green, blue);

        float rise = y2 - y1;
        float run = x2 - x1;
        float m = rise / run;
        //cout << "The slope is " << m << endl;
        float b = y1 - m * x1;
        //cout << "The y-intercept is " << b << endl;

        if( x1 == x2 ) { // Vertical Line
                if( y1 < y2) { // Starting point y is less
                        for( int y = y1; y <= y2; y++ ){
                                bmp.set_pixel (x1, y, red, green, blue);
                        }
                } else { // Starting point y is greater
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
