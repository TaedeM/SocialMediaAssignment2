# This file generates a 4-line .txt file with in each line the type of interaction with padding.
# This way, we can create a timeline where a conversation is displayed way more clearly. 
# Unfortunately, most files are so big that text viewers display 1 line on multiple lines when generating a whole interaction at once.
# Because of this, with most files list slicing should be used. The slicing can be edited on line 44

def key_interface_to_out(keypresses):
    key_out = ""
    for char in keypresses:
        if char == '':
            key_out+=('    |')
        else:
            key_out+=(char + '   |')    
    return key_out + '\n'


def timestamps_to_out(timestamps):
    time_out = ""
    for time in timestamps:
        if len(time) <= 4:
            time_out += time.ljust(4) + '|'
        else:
            time_out += "9999|"
    return time_out + '\n'


with open('NEWwysiwyg_cie_LLLL0_2721341_s_.txt', 'r', encoding="utf8") as infile:
    keypress_self = infile.read().split('¦')
with open('NEWwysiwyg_cie_LLLL0_2721341_o_s2019779.txt', 'r', encoding="utf8") as infile:
    keypress_other = infile.read().split('¦')
with open('NEWwysiwyg_cie_LLLL0_2721341_t_.txt', 'r', encoding="utf8") as infile:
    timestamps = infile.read().split('¦')[2:] # remove first 2 values
with open('NEWwysiwyg_cie_LLLL0_2721341_w_.txt', 'r', encoding="utf8") as infile:
    interface = infile.read().split('¦')

# Measures
print(len(keypress_self), len(keypress_other), len(timestamps), len(interface)) # these should all be equal to each other


# Generate txt file for analysis, the use of slicing is explained at the top of this file
slice_start = 0; slice_end = 1000

key_self_out = key_interface_to_out(keypress_self[slice_start:slice_end])
key_other_out = key_interface_to_out(keypress_other[slice_start:slice_end])
timestamps_out = timestamps_to_out(timestamps[slice_start:slice_end])
interface_out = key_interface_to_out(interface[slice_start:slice_end])

# Write output file
with open('test.txt', 'w', encoding='utf8') as outfile:
    outfile.write(key_self_out)
    outfile.write(key_other_out)
    outfile.write(timestamps_out)
    outfile.write(interface_out.rstrip())