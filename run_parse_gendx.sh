source /home/ben/minionvenv/bin/activate

inputFile="/home/ben/ben_share/GendxXmlExport/BC05.19583.short.fastq--131478206.DRA.tarr.xml"
outputFile="/home/ben/ben_share/GendxXmlExport/BC05.19583.Consensus.fasta"
python parse_gendx_xml_main.py \
 --input=$inputFile \
 --output=$outputFile



