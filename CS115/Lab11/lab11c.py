"""
Program: Lab 11c
Author: Erika Garnica Mendoza
Description: This program will read in a list of students and grades from a text file, 
             calculate the students' averages, and print the list of students as well 
             as the overall average of the students scores.
"""


class Student:
    """A class that holds the data for an individual student."""

    def __init__(self, name, scores):
        """Inits the Student class.

        Args:
            name (str): The name of the student.
            scores (list): The scores for the student.
        """
        self.name = name
        self.scores = scores

    @property
    def get_average(self):
        """Returns the average grade."""
        if self.scores == 0:
            return None
        else:
            average = sum(self.scores) / len(self.scores)
            return round(average, 5)

    def print(self):
        """Prints the student info in the following format:
            name (12 characters), grades (separated by tabs),
            average (formatted to 5 decimal places).
        """
        # Right now, just prints the student name padded out to 12 characters
        string_to_print = self.name.ljust(12)
        # Convert list of integers to strings for printing purposes
        # There are shorter ways to do this, but this is the clearest.
        for score in self.scores:
            string_to_print += '\t' + str(score)
        string_to_print += '\t' + str(self.get_average)
        print(string_to_print)


def readfile(filename):
    """Reads the entire contents of a file into a single string using
    the read() method.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The text in the file as a large, possibly multi-line, string.
    """
    infile = open(filename, 'r')  # opens file for reading

    filetext = infile.read().splitlines()  # reads the file contents into filetext

    infile.close()  # closes the file

    return filetext  # returns text of the file, as a long string


def get_average(self):
    """Returns the average grade."""
    if self.scores == 0:
        return None
    else:
        average = sum(self.scores) / len(self.scores)
        return round(average, 5)


def main():
    """A simple program to test our Student class."""
    # Total average list for later
    totalAvg = []

    studentlines = readfile("students.txt")
    # print(studentlines[0]) (the example output of question 4)

    # Loop over the list of lines from the file and
    #   break each line down into a name and scores
    for line in studentlines:
        # Split line into a list. If list is empty, break out of the loop.
        splitLines = line.split()
        if len(splitLines) == 0:
            break
        # The first item in the list is the student's name
        name = splitLines[0]
        # Convert the remaining items in the list into integers
        studentScores = []
        for i in splitLines[1:]:
            number = int(i)
            studentScores.append(number)
        # Create a new Student variable with that name and scores
        test_student = Student(name, studentScores)
        # Call the Student print method to print that student's information
        test_student.print()

        # Call the get_average function to get the average of each student's scores
        average = get_average(test_student)
        # Store the average values in a  list
        totalAvg.append(average)

    # Calculates the overall average
    overallAvg = (sum(totalAvg) / len(totalAvg))
    print('\nOverall average:', round(overallAvg, 5))


main()
