// File: Data.java
// Originally written by: Dr. Watts
// Modified by: Erika Mendoza
// Contents: This class holds the different shape functions.

import java.awt.*;
import java.util.*;
import javax.swing.*;
import java.awt.geom.GeneralPath;
import java.awt.image.*;

public class Data
{
        public Canvas canvas;
        public Image image;
        public Design6 design6;
        public ArrayList<DesignElement> elements;
        public DesignElement selectedElement = null;
        public int selectedIndex = -1;
        public Color currentStroke = Color.BLACK;
        public Color currentFill = Color.WHITE;
        public DesignElement onDeckElement = newHeart (0, 0, 90, 90, Color.BLACK, Color.WHITE);
        public SelectedPanel selected;

        public Data ()
        {
                        elements = new ArrayList<DesignElement> ();
                        // Add your element instantiations here
                        elements = new ArrayList<DesignElement> ();
                        elements.add (newRectangle(300, 300, 200, 100, Color.BLUE, Color.CYAN));
                        elements.add (newRectangle(100, 200, 100, 150, Color.BLACK, Color.WHITE));
                        elements.add (newHeart(100, 200, 100, 150, Color.RED, Color.PINK));
                        elements.add (newHeart(300, 300, 200, 100, new Color(167,66,245), new Color(230,191,245)));
                        // added shapes
                        elements.add (newTriangle(500, 400, 100, 100, Color.MAGENTA, Color.lightGray));
                        elements.add (newPetal(300, 200, 200, 100, Color.green, Color.yellow));
                        elements.add (newStar(200, 500, 50, 50, Color.PINK, new Color(21, 33, 15)));
                        elements.add (newPentagon(200, 300, 50, 50, Color.BLACK, Color.RED));

                        for (int i = 0; i < elements.size(); i++)
                                System.out.println (elements.get(i));
        }

        public Data (String fileName)
        {
                elements = new ArrayList<DesignElement> ();
                FileIO io = new FileIO (this);
                io.readFile (fileName);
        }

        public DesignElement getSelected (int mouseX, int mouseY)
        {
                if (selectedElement != null)
                        selectedElement.isSelected = false;
                selectedElement = null;
                selectedIndex = -1;
                for (int i = elements.size() - 1; i >= 0 && selectedElement == null; i--)
                        if (elements.get(i).inElement (mouseX, mouseY))
                        {
                                selectedElement = elements.get(i);
                                selectedIndex = i;
                        }
                if (selectedElement != null)
                        selectedElement.isSelected = true;
                return selectedElement;
        }

        public DesignElement getNewElement (int mouseX, int mouseY)
        {
                DesignElement newOne = onDeckElement.clone ();
                newOne.moveTo (mouseX, mouseY);
                newOne.isSelected = true;
                elements.add (newOne);
                selectedElement = newOne;
                selectedIndex = elements.size() - 1;
                return newOne;
        }

        public DesignElement deleteSelected ()
        {
                if (selectedElement != null)
                        selectedElement.isSelected = false;
                selectedElement = null;
                selectedIndex = -1;
                for (int i = elements.size() - 1; i >= 0 && selectedElement == null; i--)
                        if (elements.get(i).inElement (mouseX, mouseY))
                        {
                                selectedElement = elements.get(i);
                                selectedIndex = i;
                        }
                if (selectedElement != null)
                        selectedElement.isSelected = true;
                return null;
        }

        public boolean moveSelectedBack ()
        {
                if( selectedElement == elements.get(0) )
                        return false;
                elements.add(selectedElement);
                selectedIndex += 1;
                return true;
        }
        
        public boolean moveSelectedForward ()
        {
                if( selectedElement == elements.get(0) )
                        return false;
                elements.add(selectedElement);
                selectedIndex += 1;
                return true;
        }

        public DesignElement newRectangle (double cx, double cy, double width, double height, Color stroke, Color fill)
        {
                DesignElement rect = new DesignElement ();
                rect.centerX = cx;
                rect.centerY = cy;
                rect.strokeColor = stroke;
                rect.fillColor = fill;
                rect.path.moveTo (cx-width/2, cy-height/2);
                rect.path.lineTo (cx+width/2, cy-height/2);
                rect.path.lineTo (cx+width/2, cy+height/2);
                rect.path.lineTo (cx-width/2, cy+height/2);
                rect.path.lineTo (cx-width/2, cy-height/2);
                return rect;
        }

        public DesignElement newHeart (double cx, double cy, double width, double height, Color stroke, Color fill)
        {
                DesignElement heart = new DesignElement ();
                heart.centerX = cx;
                heart.centerY = cy;
                heart.strokeColor = stroke;
                heart.fillColor = fill;
                heart.path.moveTo (cx, cy-height/3);
                heart.path.curveTo (cx-0.44*width, cy-0.87*height, cx-0.87*width, cy, cx, cy+height/2);
                heart.path.curveTo (cx+0.87*width, cy, cx+0.44*width, cy-0.87*height, cx, cy-height/3);
                return heart;
        }

        // Add your DesignElement creation functions below this line
        public DesignElement newTriangle (double cx, double cy, double width, double height, Color stroke, Color fill)
        {
                DesignElement triangle = new DesignElement ();
                triangle.centerX = cx;
                triangle.centerY = cy;
                triangle.strokeColor = stroke;
                triangle.fillColor = fill;
                triangle.path.moveTo (cx-width/2, cy-height/2);
                triangle.path.lineTo (cx+width/2, cy-height/2);
                triangle.path.lineTo (cx+width, cy);
                triangle.path.lineTo(cx-width/2, cy-height/2);
                return triangle;
        }

        public DesignElement newPetal (double cx, double cy, double width, double height, Color stroke, Color fill)
        {
                DesignElement petal = new DesignElement ();
                petal.centerX = cx;
                petal.centerY = cy;
                petal.strokeColor = stroke;
                petal.fillColor = fill;
                petal.path.moveTo(cx, cy);
                petal.path.curveTo(cx, cy, cx-width/2, cy+height/2, cx+width, cy+height);
                petal.path.curveTo(cx+width, cy+height, cx+width/2, cy-height/2, cx, cy);
                return petal;
        }
                                               
        public DesignElement newStar (double cx, double cy, double width, double height, Color stroke, Color fill)
        {
                DesignElement star = new DesignElement ();
                star.centerX = cx;
                star.centerY = cy;
                star.strokeColor = stroke;
                star.fillColor = fill;
                star.path.moveTo(cx, cy-height);
                star.path.lineTo(cx+14, cy+30);
                star.path.lineTo(cx+33, cy+5);
                star.path.lineTo(cx-24, cy+22);
                star.path.lineTo(cx+6, cy+33);
                star.path.lineTo(cx, cy-15);
                star.path.lineTo(cx-29, cy+15);
                star.path.lineTo(cx+6, cy-22);
                star.path.lineTo(cx-24, cy-22);
                star.path.lineTo(cx-33, cy-5);
                return star;
        }
                                                  
        public DesignElement newPentagon (double cx, double cy, double width, double height, Color stroke, Color fill)
        {
                DesignElement pentagon = new DesignElement ();
                pentagon.centerX = cx;
                pentagon.centerY = cy;
                pentagon.strokeColor = stroke;
                pentagon.fillColor = fill;
                pentagon.path.moveTo (cx-width/2, cy-height/2);
                pentagon.path.lineTo (cx+width/2, cy-height/2);
                pentagon.path.lineTo (cx+width/2, cy+height/2);
                pentagon.path.lineTo (cx, cy+width/2);
                pentagon.path.lineTo (cx-width, cy);
                pentagon.path.lineTo (cx, cy-height/2);
                return pentagon;
        }
}
