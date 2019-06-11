#!/usr/bin/env python3
import app

def main():
    testPassCount = 0
    testCount = 1
    textFiles = ['./testdata/pattern1.txt']
    patternFiles =['./testdata/text1.txt']
    outputFiles = ['./testdata/patternmatch1.output']
    expectedOutputs = ['']
    for i in range(testCount):
        print('Test: {} - Text:{} Pattern:{} Output:{}'.format(i, textFiles[i], patternFiles[i], outputFiles[i]))
        app.patternMatch(open(textFiles[i], 'r'), open(patternFiles[i], 'r'), open(outputFiles[i], 'w+'))
        print('Expected output: {}'.format(expectedOutputs[i]))
        #try:
            #outputFile = open(outputFiles[i], 'r')
            #returnedOutput = outputFile.readline().strip('\n ')
            #print('Returned output: {}'.format(returnedOutput))
            #outputFile.close()
        #except IOError:
            #print("ERROR: Couldn't read output file!")
        #if (expectedOutputs[i]==returnedOutput):
            #print('PASS')
            #testPassCount += 1
        #else:
            #print('FAIL')
    print("\nTESTS: {}/{} ({}%)".format(testPassCount, testCount, testPassCount/testCount*100))

if __name__=='__main__':
    main()