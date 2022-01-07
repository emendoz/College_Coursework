// File: Exercise10.java
// Originally written by: Dr. Watts
// Modified by: Erika Mendoza
// Contents: This class creates the dimensions of Exercise10's userface.

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Exercise10
{
        public static void main (String[] args)
        {
                Data data;
                if (args.length > 0)
                        data = new Data (args[0]);
                else
                        data = new Data ();
                JFrame frame = new JFrame ("Exercise 10");
                frame.setSize (1000,700);
                frame.setResizable (false);
                frame.setLocation (200, 200);
                frame.setBackground (Color.BLACK);
                Container pane = frame.getContentPane();
                Palette palette = new Palette (data);
                JTabbedPane tabpane = new JTabbedPane ();
                Canvas canvas = new Canvas (data);
                tabpane.add ("Canvas", canvas);
                Image pattern = new Image (data);
                tabpane.add ("Image", pattern);
                Design6 design6 = new Design6 (data);
                tabpane.add ("Design6", design6);
                pane.setLayout (new BorderLayout());
                pane.add (palette, BorderLayout.WEST);
                pane.add (tabpane, BorderLayout.CENTER);
                frame.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);
                frame.setVisible (true);
        }
}
