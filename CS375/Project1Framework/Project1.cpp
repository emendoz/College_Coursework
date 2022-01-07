/*******************************************************************************
* Assignment:  CS 375 Project 1 - SVG to BMP Converter                         *
* Author: Dr. Watts                                                            *
* Modified by: Erika Mendoza                                                   *
* Date: Fall 2021                                                              *
* File: Project1.cpp                                                           *
*                                                                              *
* Description: This file contains the main function for Project 1.             *
*******************************************************************************/

#include <cstdlib>
#include <iostream>
#include <iomanip>
#include "SetLimits.h"
#include "Svg2Bmp.h"

int main (int argc, char * argv[])
{
        if (argc < 2)
        {
                cerr << "format: " << argv[0] << " <filename>\n";
                exit (1);
        }
        SetLimits ();
        Svg2Bmp svg2bmp (argv[1]);

        return 0;
}
