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

class haplotype():

    def __init__(self, id, begin, end, sequence):
        self.id = id
        self.begin = begin
        self.end = end
        self.sequence = sequence

    # TODO: The text of these contain deletion characters.