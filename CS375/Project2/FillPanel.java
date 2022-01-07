// File: FillPanel.java
// Originally written by: Dr. Watts
// Modified by: Erika Mendoza
// Contents: a JPanel to display the fill color of a design element

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;
import java.util.*;

public class FillPanel extends JPanel
{
        Color [] colors = {Color.GREEN, new Color (68, 150, 24), new Color (17, 209, 148),
                           Color.LIGHT_GRAY, Color.BLUE, Color.RED, Color.YELLOW, Color.PINK,
                           Color.CYAN, Color.MAGENTA};
        Data data;

        public FillPanel (Data D)
        {
                data = D;
                setLayout (new GridLayout(3,3));
                for (int i = 0; i < 9; i++)
                {
                        OneColor one = new OneColor (colors[i]);
                        add (one);
                }
        }

        class OneColor extends JPanel implements MouseListener
        {
                Color color;

                public OneColor (Color C)
                {
                        color = C;
                        setBackground (color);
                        setBorder (BorderFactory.createRaisedBevelBorder());
                        addMouseListener(this);
                        repaint();
                }

                public void mousePressed (MouseEvent e)
                {
                        if (e.getButton() == e.BUTTON1) // Left mouse button
                        {
                                data.currentFill = color;
                                if (data.selectedElement != null)
                                {
                                        data.selectedElement.setFill (color);
                                        data.canvas.repaint();
                                }
                                if (data.onDeckElement != null)
                                {
                                        data.onDeckElement.setFill (color);
                                        data.selected.repaint();
                                }
                        }
                }
                public void mouseReleased (MouseEvent e) { }
                public void mouseEntered (MouseEvent e) { }
                public void mouseExited (MouseEvent e) { }
                public void mouseClicked (MouseEvent e) { }
        }
}
