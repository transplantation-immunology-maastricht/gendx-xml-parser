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

from os.path import split, isdir
#join, basename,
from os import makedirs

#from shutil import copyfile
#from os.path import splitext, isdir, split, join
#from os import makedirs, system

from Bio.SeqIO import parse, write

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

#from pysam import AlignmentFile

from Bio.Alphabet.IUPAC import IUPACUnambiguousDNA

from xml.etree import ElementTree as ET

from gendx_xml_parser.haplotype import haplotype

#from xml.dom import minidom as MD

def getHaplotypeByID(haplotypes, id):
    for haplotype in haplotypes:
        if(id == haplotype.id):
            return haplotype
    return None

def parseXml(inputFile, outputFile):
    #print('inside parse xml methods.')

    # Open XML file.
    tree = ET.parse(inputFile)
    root = tree.getroot()

    haplotypeList = []

    # Open haplotypes nodes, record their information. Name, End, Begin, Sequence.
    for haplotypesNode in root.iter('Haplotypes'):
        for haplotypeNode in haplotypesNode.iter('Haplotype'):
            id = haplotypeNode.attrib['ID']
            begin = haplotypeNode.attrib['begin']
            end = haplotypeNode.attrib['end']
            sequence = haplotypeNode.text

            print('Haplotype ' + str(id) + ' located at (' + str(begin) + ':' + str(end)
                  + '), EndMinusBegin=' + str(int(end) - int(begin)) + ', LengthOfSequence=' + str(len(sequence)))
            haplotypeList.append(haplotype(id, begin, end, sequence))

        # Check each one, raise an exception if the indexes don't make sense. They should. They don't of course.

    sequenceRecords = []
    # Iterate "Match" objects.
    for matchingNode in root.iter('Matching'):
        for matchesNode in matchingNode.iter('Matches'):
            for matchNode in matchesNode.iter('Match'):
                # each match node represents an allele sequence.
                # The ID is the allele that this sequence is matched to.  Closest allele, maybe.
                id = matchNode.attrib['ID'] + '_' + matchNode.attrib['phasing']
                alleleSequence = ''
                for haplotypeCombinationNode in matchNode.iter('HaplotypeCombination'):
                    for haplotypeIDNode in haplotypeCombinationNode.iter('HaplotypeID'):
                        haplotypeID = haplotypeIDNode.text
                        haplotypeObject = getHaplotypeByID(haplotypeList, haplotypeID)
                        alleleSequence = alleleSequence + haplotypeObject.sequence

                # make a SeqIO Object, add it to the list.
                currentSequenceRecord = SeqRecord(Seq(alleleSequence.replace('-',''), IUPACUnambiguousDNA),
                    id=id,
                    description='')
                sequenceRecords.append(currentSequenceRecord)

                # make a seqIO Object, replacing the deletions, add it to the list.
                # nah, just do it by hand for testing.

    write(sequenceRecords, createOutputFile(outputFile), 'fasta')



def createOutputFile(outputfileName):
    tempDir, tempFilename = split(outputfileName)
    if not isdir(tempDir):
        print('Making Directory:' + tempDir)
        makedirs(tempDir)
    resultsOutput = open(outputfileName, 'w')
    return resultsOutput