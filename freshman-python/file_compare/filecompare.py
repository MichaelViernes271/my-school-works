"""
Author: Viernes, Michael
Date:6:52 PM Thursday, April 14, 2022
Objective: Create a regex that compares string files.
"""
import re, sys, string

def readfiles(file1, file2):
    """ Reads both file for the differences. """
    with open(file1) as f1:
        with open(file2) as f2:
            filecomp1 = f1.read()
            filecomp2 = f2.read()
            return compare(filecomp1, filecomp2) # Returns the identified similarities and differences.
            
def compare(fc1, fc2):
    results = [] # Store the findings in both files.
    if fc1 == fc2:
        results.append("The file objects are similar.")
    if sys.getsizeof(fc1) == sys.getsizeof(fc2):
        results.append("The files have same byte sizes.")
        
    # similarities = [ words for w in word_match() ] # Searches for similar lines.
    return results

if __name__ == "__main__":
    try:
        file1 = (input("Pass two files to compare: \n"))
        file2 = (input())
        file_findings = readfiles(file1, file2) # Pass two files or strings.
        print(file_findings)
    except ValueError as e:
        print("Please use a filename with extension.\n")