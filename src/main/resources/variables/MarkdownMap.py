#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

# Header is necessary to render a table
markdown =  "|{}|{}|\n".format(keyHeader, valueHeader)
markdown += "|-|-|\n"

for key, value in map.iteritems():
    markdown += "|{}|{}|\n".format(key, value)
