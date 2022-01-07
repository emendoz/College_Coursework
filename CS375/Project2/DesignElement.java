// File: DesignElement.java
// Originally written by: Dr. Watts
// Modified by: Erika Mendoza
// Contents: This class covers the transformations affecting the shapes created.

import java.awt.*;
import java.util.*;
import javax.swing.*;
import java.awt.geom.GeneralPath;
import java.awt.geom.AffineTransform;
import java.awt.geom.PathIterator;
import java.awt.geom.Rectangle2D;
import java.lang.Math.*;

public class DesignElement {
        public double centerX;
        public double centerY;
        public double angle;
        public Color fillColor;
        public Color strokeColor;
        public boolean isSelected;
        public GeneralPath path;

        public DesignElement() {
                centerX = centerY = 0;
                angle = 0;
                fillColor = Color.WHITE;
                strokeColor = Color.BLACK;
                isSelected = false;
                path = new GeneralPath();
        }

        public DesignElement clone() {
                DesignElement copy = new DesignElement();
                copy.centerX = centerX;
                copy.centerY = centerY;
                copy.angle = angle;
                copy.fillColor = fillColor;
                copy.strokeColor = strokeColor;
                copy.path = (GeneralPath) path.clone();
                return copy;
        }

        public void setStroke(Color C) {
                strokeColor = C;
        }

        public void setFill(Color C) {
                fillColor = C;
        }

        public void paintElement(Graphics2D g2) {
                g2.setStroke(new BasicStroke(2.0f));
                g2.setPaint(fillColor);
                g2.fill(path);
                g2.setPaint(strokeColor);
                g2.draw(path);
                g2.fillOval((int) (centerX - 1), (int) (centerY - 1), 2, 2); // Draw the center point
        }

        public boolean inElement(int mouseX, int mouseY) {
                return path.contains(mouseX, mouseY);
        }

        public void moveTo(double newCenterX, double newCenterY) {
                double deltaX = newCenterX - centerX;
                double deltaY = newCenterY - centerY;
                translate(deltaX, deltaY);
        }

        public void rotate(double deltaA) {
                //System.out.printIn ("Rotate (1) called");
                AffineTransform tx = new AffineTransform();
                tx.rotate(deltaA, centerX, centerY);
                path.transform(tx);
                angle += deltaA;
        }

        public void rotate(double mouseX1, double mouseY1, double mouseX2, double mouseY2) {
                //System.out.printIn ("Rotate (4) called");
                double a1 = Math.atan2(mouseY1 - centerY, mouseX1 - centerX);
                double a2 = Math.atan2(mouseY2 - centerY, mouseX2 - centerX);
                double deltaA = a2 - a1;
                rotate(deltaA);
        }

        public void scale(double scaleX, double scaleY) {
                //System.out.println ("Scale (2) called");
                Rectangle2D bounds = path.getBounds2D();
                if (Math.abs(bounds.getWidth() * scaleX) < 5)
                        return;
                if (Math.abs(bounds.getHeight() * scaleY) < 5)
                        return;
                AffineTransform tx = new AffineTransform();
                tx.translate(centerX, centerY);
                tx.scale(scaleX, scaleY);
                tx.translate(-centerX, -centerY);
                path.transform(tx);
        }

        public void scale(double mouseX1, double mouseY1, double mouseX2, double mouseY2) {
                //System.out.println ("Scale (4) called");
                double scaleXY;
                double d1 = Math.hypot(mouseX1 - centerX, mouseY1 - centerY);
                double d2 = Math.hypot(mouseX2 - centerX, mouseY2 - centerY);
                if (d1 == 0 || d2 == 0)
                        scaleXY = 1;
                else
                        scaleXY = d2 / d1;
                scale(scaleXY, scaleXY);
        }

        public void translate(double deltaX, double deltaY) {
                centerX += deltaX;
                centerY += deltaY;
                AffineTransform tx = new AffineTransform();
                tx.translate(deltaX, deltaY);
                path.transform(tx);
        }

        public void translate(double mouseX1, double mouseY1, double mouseX2, double mouseY2) {
                double deltaX = mouseX2 - mouseX1;
                double deltaY = mouseY2 - mouseY1;
                translate(deltaX, deltaY);
        }

        public void fromString(String str) {
                String[] parts = str.split(" ");
                try {
                        centerX = Double.parseDouble(parts[0]);
                        centerY = Double.parseDouble(parts[1]);
                        angle = Double.parseDouble(parts[2]);
                        strokeColor = new Color(Integer.parseInt(parts[3]));
                        fillColor = new Color(Integer.parseInt(parts[4]));
                        path = new GeneralPath();

                        int i = 5;
                        while (i < parts.length) {
                                if (parts[i].equals("M")) {
                                        double x = Double.parseDouble(parts[i + 1]);
                                        double y = Double.parseDouble(parts[i + 2]);
                                        path.moveTo(x, y);
                                        i += 3;
                                } else if (parts[i].equals("L")) {
                                        double x = Double.parseDouble(parts[i + 1]);
                                        double y = Double.parseDouble(parts[i + 2]);
                                        path.lineTo(x, y);
                                        i += 3;
                                } else if (parts[i].equals("Q")) {
                                        double x1 = Double.parseDouble(parts[i + 1]);
                                        double y1 = Double.parseDouble(parts[i + 2]);
                                        double x2 = Double.parseDouble(parts[i + 3]);
                                        double y2 = Double.parseDouble(parts[i + 4]);
                                        path.quadTo(x1, y1, x2, y2);
                                        i += 5;
                                } else if (parts[i].equals("C")) {
                                        double x1 = Double.parseDouble(parts[i + 1]);
                                        double y1 = Double.parseDouble(parts[i + 2]);
                                        double x2 = Double.parseDouble(parts[i + 3]);
                                        double y2 = Double.parseDouble(parts[i + 4]);
                                        double x3 = Double.parseDouble(parts[i + 5]);
                                        double y3 = Double.parseDouble(parts[i + 6]);
                                        path.curveTo(x1, y1, x2, y2, x3, y3);
                                        i += 7;
                                } else if (parts[i].equals("Z")) {
                                        path.closePath();
                                        i += 1;
                                } else
                                        i++;
                        }
                } catch (NumberFormatException e) {
                        System.out.println("File input error - invalid numeric value");
                        ;
                }
        }

        public String toString() {
                String string = new String();
                string += centerX + " ";
                string += centerY + " ";
                string += angle + " ";
                string += strokeColor.getRGB() + " ";
                string += fillColor.getRGB() + " ";
                final PathIterator itr = path.getPathIterator(null);
                while (!itr.isDone()) {
                       double[] points = new double[6];
                       int t = itr.currentSegment(points);
                       switch (t) {
                               case PathIterator.SEG_MOVETO:
                                       string += "M " + points[0] + " " + points[1] + " ";
                                       break;
                               case PathIterator.SEG_LINETO:
                                       string += "L " + points[0] + " " + points[1] + " ";
                                       break;
                               case PathIterator.SEG_QUADTO:
                                       string += "Q " + points[0] + " " + points[1] + " "
                                                      + points[2] + " " + points[3] + " ";
                                       break;
                               case PathIterator.SEG_CUBICTO:
                                       string += "C " + points[0] + " " + points[1] + " "
                                                      + points[2] + " " + points[3] + " "
                                                      + points[4] + " " + points[5] + " ";
                                       break;
                               case PathIterator.SEG_CLOSE:
                                       string += "Z ";
                       }
                       itr.next();
               }
               return string;
       }

        public void deleteSelected() {
        }

        public void moveSelectedBackward() {
        }

        public void moveSelectedForward() {
        }
}
