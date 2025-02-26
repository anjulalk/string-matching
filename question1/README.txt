GROUP INFO
---------------------------------------------------------------------------------
17000777    anjulakarunarathne@gmail.com
17000793    piyuk.thilaka@gmail.com
17000752    punsarachamath@gmail.com


USAGE
---------------------------------------------------------------------------------
Linux: ./app.py text_file.txt pattern_file.txt output_file.txt
Windows: python text_file.txt pattern_file.txt output_file.txt

EXPLAINATION
---------------------------------------------------------------------------------
The program takes 3 command line arguments: text file, pattern, and output file.
It then tries to open the input and output files. If the files were not found it halts and returns an exit code of 1 or 2.
Then those files are passed over to the patternMatch function which will read the files and will save the content into temporary variables

patternMatch function uses naive approch to find the indexes where the pattern matches and saves them into the output file.
Naive algorithm was chosen because it's simplicity to be modified and implemented for this case of matching wildcards.
Modifying other algothms for this case turned out to require more logical changes and was more complex, so naive algorithm was used.
The naive algorithm is modified so that it skips over to the next character if an wildcard ('_') is found.

Complexity of the used algorithm: O(mn) 
where m and n are the lengths of text and pattern respectively.

RUNNING TESTS
---------------------------------------------------------------------------------
Tests are scripted and can be executed with test.py file

Linux: ./test.py
Windows: python test.py

Input files are located inside the 'testdata' directory.
eg: text1.txt, pattern1.txt, patternmatch1.output

Respective file paths of text, pattern and output filesare stored as lists in the test.py file.
Correct/expected output data is stored in a list in the test.py file as well.
When the test.py script is run it checks if the output files matches given correct/expected outputs.
It then gives a score point for each matches. At the end a total percentage is calculated.
