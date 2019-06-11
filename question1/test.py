#!/usr/bin/env python3
import app

def main():
    # Number of test cases
    testCount = 10

    # List of text files
    textFilePaths = ['./testdata/text1.txt', './testdata/text2.txt', './testdata/text3.txt', './testdata/text4.txt', './testdata/text5.txt', './testdata/text6.txt', './testdata/text7.txt', './testdata/text8.txt', './testdata/text9.txt', './testdata/text10.txt']
    
    # List of pattern files
    patternFilePaths =['./testdata/pattern1.txt', './testdata/pattern2.txt', './testdata/pattern3.txt', './testdata/pattern4.txt', './testdata/pattern5.txt', './testdata/pattern6.txt', './testdata/pattern7.txt', './testdata/pattern8.txt', './testdata/pattern9.txt', './testdata/pattern10.txt']
    
    # List of output files
    outputFilePaths = ['./testdata/patternmatch1.output', './testdata/patternmatch2.output', './testdata/patternmatch3.output', './testdata/patternmatch4.output', './testdata/patternmatch5.output', './testdata/patternmatch6.output', './testdata/patternmatch7.output', './testdata/patternmatch8.output', './testdata/patternmatch9.output', './testdata/patternmatch10.output']
    
    # List of expected/correct outputs for the respective files
    expectedOutputs = ['0 8', '29', '153', '9', '0', '59', '4 8 21 29 46 62', '', '257', '230']

    testPassCount = 0
    for i in range(testCount):
        # Retrieve respective file paths from the lists
        textFilePath, patternFilePath, outputFilePath = textFilePaths[i], patternFilePaths[i], outputFilePaths[i]
        
        # Open respective files
        textFile, patternFile, outputFile = open(textFilePath, 'r'), open(patternFilePath, 'r'), open(outputFilePath, 'w+')
        
        print('TEST {}\nText: {}\tPattern: {}\tOutput: {}'.format(i, textFilePath, patternFilePath, outputFilePath))
        
        # Generate output
        app.patternMatch(textFile, patternFile, outputFile)
        
        # Close files
        textFile.close()
        patternFile.close()
        outputFile.close()

        # Retrieve output file content and check if it matches expected output
        try:
            outputFile = open(outputFilePaths[i], 'r')
            output = outputFile.readline().strip('\n ')
            print('Output: {}'.format(output))
            outputFile.close()
        except IOError:
            print("ERROR: Couldn't read output file!")
        
        print('Expected: {}'.format(expectedOutputs[i]))

        if (expectedOutputs[i]==output):
            print('PASS\n')
            testPassCount += 1
        else:
            print('FAIL\n')
        
        # Close files
        textFile.close()
        patternFile.close()
        outputFile.close()
    
    # Display final result
    print("\nTESTS: {}/{} ({}%)".format(testPassCount, testCount, testPassCount/testCount*100))

if __name__=='__main__':
    main()