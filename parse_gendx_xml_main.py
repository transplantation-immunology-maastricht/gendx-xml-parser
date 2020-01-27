# This file is part of gendx_xml_parser.
#
# gendx_xml_parser is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gendx_xml_parser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with gendx_xml_parser. If not, see <http://www.gnu.org/licenses/>.

from sys import argv, exc_info
from getopt import getopt, GetoptError
from os.path import isdir, isfile

#from find_homopolymers.find_homopolymers import findHomopolymers
from gendx_xml_parser.parse_gendx_xml import parseXml

def usage():
    print("usage:\n" + 
    "\tThis script is written for python 3.6\n" + 
    "\tI haven't written the usage tutorial yet.  Oops.  Do this now please."
    )      

# Read Commandline Arguments.  Return true if everything looks okay for read extraction.
def readArgs():
    if(len(argv) != 3):
        print ('I don\'t think you have proper arguments. I expect -i for inputfile and -o for outputfile.\n')
        usage()
        return False

    global inputFile
    global outputFile

    # https://www.tutorialspoint.com/python/python_command_line_arguments.htm
    try:
        opts, args = getopt(argv[1:]
            ,"i:o:"
            ,['input=','output='])

        # in this case, the input is a fasta file with a bunch of feature sequences
        for opt, arg in opts:

            if opt in ("-i", "--input"):
                inputFile = arg
            elif opt in ("-o", "--output"):
                outputFile = arg
            else:
                print('Unknown Commandline Option:' + str(opt) + ':' + str(arg))
                raise Exception('Unknown Commandline Option:' + str(opt) + ':' + str(arg))

    except GetoptError:
        print ('Something seems wrong with your commandline parameters.')
        print (exc_info())
        usage()
        return False

    # Sanity Checks
    if (isfile(inputFile)):
        #print ('Read input is a file that exists.')
        #print('inputFile=' + inputFile)
        pass
    else:
        raise Exception('Input file is not a file. ' + str(inputFile))
        return False


    return True

if __name__=='__main__':
    try:
        if(readArgs()):
            print('Commandline arguments look fine.  The hour is at hand.')
            #print('InputFile=' + inputFile)

            #findHomopolymers(inputFile, outputDirectory)
            parseXml(inputFile, outputFile)
            
            print ('I am done for now, have a nice day.')    
        else:
            print('\nI\'m giving up because I was not satisfied with your commandline arguments.')  
            
    except Exception:
        # Top Level exception handling like a pro.
        # This is not really doing anything.
        print ('Fatal problem during parsing:')
        print (exc_info())
        raise


