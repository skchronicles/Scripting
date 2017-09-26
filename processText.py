########################################################
# Skyler Kuhn
# Interface text-processing & music track formatter
# https://www.ynonperek.com/2017/09/21/python-exercises/
########################################################


class file2dict(object):
    """Usage :: interfacelist, textdict = file2dict("textprocessingPractice.txt").process()
       Usage :: musicfilesobj = file2dict('oldmusicTrackFormat.txt').musicFormatter(formatsDict1)"""

    def __init__(self, filename):
        self.fH = open(filename)
        self.filedict = {}
        self.interfacelist = []
        self.inputDelimeters = ''
        self.outputDelimeters = ''

    def process(self):
        """Groups alike-interface-data together"""
        id = str
        for line in self.fH:
            linelist = line.strip('\n').split('\t')
            if len(linelist) == 1:
                id = linelist[0].split(":")[0]
                self.interfacelist.append(id)
                self.filedict[id] = []
            else:
                self.filedict[id].append(linelist[1])
        return self.interfacelist, self.filedict

    def musicFormatter(self, formatsdict):
        """Changes Track Formatting of Music Tracks in mass given dictionary containing input/output format"""

        inputformat, outputformat = formatsdict['input'], formatsdict['output']
        inputbase, outputbase, mappingDict = self.baseformat(formatsdict)
        #print(inputbase, outputbase, mappingDict)

        inputDelimInfo = self.evaluateDelimeter(inputformat, inputbase, self.inputDelimeters)
        outputDelimInfo = self.evaluateDelimeter(outputformat, outputbase, self.outputDelimeters)

        #print(inputDelimInfo, outputDelimInfo, "\n\n\n\n\n")

        for line in self.fH:
            linelist = line.strip('\n').split()
            lastelement = linelist.pop(-1)
            lastelement = lastelement.split(".")[0]
            linelist.append(self.removeDelimiters(lastelement,self.inputDelimeters))
            linelist = self.groupMetadata(linelist, inputDelimInfo)

            inputMappedDict = {}
            for i, element in enumerate(inputbase):
                inputMappedDict[element] = linelist[i]

            for attribute in outputbase:
                outputformat = outputformat.replace(attribute, inputMappedDict[attribute])
            print(outputformat)

    def groupMetadata(self, formatlist, inputDemlimInfo):
        def isdatatype(data, datatype):
            try:
                datatype(data)
                return True
            except ValueError:
                return False

        queue = formatlist
        group = ""
        newlist = []
        for i in range(len(queue)):
            if queue[i] not in inputDemlimInfo and not isdatatype(queue[i], int):
                group += queue[i] + " "

            elif isdatatype(queue[i], int):
                #print("Grouped together: ", group[:-1])
                newlist.append(group[:-1])
                newlist.append(queue[i])
                group = ""
        return newlist

    def baseformat(self, formatsdict):
        inputformat, outputformat = formatsdict['input'], formatsdict['output']
        print('Converting Formats...')
        print('{}  ----->  {}\n'.format(inputformat, outputformat))

        self.inputDelimeters = list(set(list(inputformat)) - set(list(outputformat)))
        self.outputDelimeters = list(set(list(outputformat)) - set(list(inputformat)))
        print(self.inputDelimeters, self.outputDelimeters)

        inputlist, outputlist = inputformat.split(".")[:-1], outputformat.split(".")[:-1]
        fileExtension = "." + inputformat.split(".")[-1]
        print(inputlist, outputlist, fileExtension)

        inputformat, outputformat = "".join(inputlist), "".join(outputlist)

        inputformat = self.removeDelimiters(inputformat, self.inputDelimeters).split()
        outputformat = self.removeDelimiters(outputformat, self.outputDelimeters).split()
        mappingDict = {}

        for element in inputformat:
            for i in range(len(outputformat)):
                if element == outputformat[i]:
                    if element not in mappingDict:
                        mappingDict[element] = [i]
                    else:
                        mappingDict[element].append(i)

        return inputformat, outputformat, mappingDict

    @staticmethod
    def evaluateDelimeter(givenformat, givenbase, delimList):
        delimeterInfo = {}
        for i, char in enumerate(givenformat):
            if char in delimList:
                if char not in delimeterInfo:
                    delimeterInfo[char] = [i]
                else:
                    delimeterInfo[char].append(i)
        return delimeterInfo

    @staticmethod
    def removeDelimiters(inputstring, delimetersList):
        for delimeter in delimetersList:
            inputstring = inputstring.replace(delimeter, '')
        return inputstring

def processText(interfacelist, textDictionary):
    for interface in interfacelist:
        otherinfolist = textDictionary[interface]
        inet = ''
        status = ''
        for thing in otherinfolist:
            if thing.split(':')[0] == 'status':
                status = thing.split(':')[1].strip()
            elif thing.split()[0] == 'inet':
                inet = thing.split()[1]
        yield interface,inet,status

if __name__ == '__main__':

    # Practice Problem 1).
    interfacelist, textdict = file2dict('textprocessingPractice.txt').process()
    print('\n\n\ninterface,inet,status')
    for interface,inet,status in processText(interfacelist, textdict):
        print('{},{},{}'.format(interface,inet,status))
    else:
        print("\n\n\n\n")

    # Practice Problem 2).
    formatsDict1 = {'input': '<album> - <track> <title> (<year>).mp3',
                   'output': '<album>/ <year> <album>/ <track> <title>.mp3'}

    musicfilesobj = file2dict('oldmusicTrackFormat.txt').musicFormatter(formatsDict1)
    print("\n\n")
    print("--------------------------------------------------")








