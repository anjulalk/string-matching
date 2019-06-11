#!/usr/bin/env python3
import app

def main():
    testPassCount = 0
    testCount = 2
    textFiles = []
    patternFiles =[]
    outputFiles = []
    expectedOutputs = []
    for i in range(testCount):
        print('Test: {} - Text:{} Pattern:{} Output:{}'.format(i, textFiles[i], patternFiles[i], outputFiles[i]))
        app.patternMatch(textFiles[i], patternFiles[i], outputFiles[i])
        print('Expected output: {}'.format(expectedOutputs[i]))
        try:
            outputFile = open(outputFiles, 'r')
            returnedOutput = outputFile.readline()
            print('Returned output: {}'.format(returnedOutput))
        except IOError:
            print("ERROR: Couldn't write into output file!")
        if (expectedOutputs[i]==returnedOutput):
            print('PASS')
            testPassCount += 1
        else:
            print('FAIL')
    print("\nTESTS: {}/{}".format(testPassCount, testCount))

if __name__=='__main__':
    main()