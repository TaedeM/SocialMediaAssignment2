# Probeersel, om de 4 bestanden in 1 overzichtelijk bestand te zetten met padding zoals in de opdracht weergegeven staat
# De bedoeling was om een txt bestand te maken met 4 lines, eentje voor elke type observatie
# Het werkt, maar de realiteit is dat 1 line zo lang wordt dat elk programma de enkele line toch op meerdere lines plaatst,
# waardoor het visueel niet werkt.
# Het is misschien wel handig voor (handmatige) analyse om bepaalde stukken van text uit te printen door de lists te slicen

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
    keypress_self = infile.read()
    keypress_self = keypress_self.split('¦')
with open('NEWwysiwyg_cie_LLLL0_2721341_o_s2019779.txt', 'r', encoding="utf8") as infile:
    keypress_other = infile.read()
    keypress_other = keypress_other.split('¦')
with open('NEWwysiwyg_cie_LLLL0_2721341_t_.txt', 'r', encoding="utf8") as infile:
    timestamps = infile.read()
    timestamps = timestamps.split('¦')[2:] # remove first 2 values
with open('NEWwysiwyg_cie_LLLL0_2721341_w_.txt', 'r', encoding="utf8") as infile:
    interface = infile.read()
    interface = interface.split('¦')

# Measures
print(len(keypress_self), len(keypress_other), len(timestamps), len(interface)) # show lengths, should be equal

# Generate txt file for analysis
key_self_out = key_interface_to_out(keypress_self)
key_other_out = key_interface_to_out(keypress_other)
time_out = timestamps_to_out(timestamps)
interface_out = key_interface_to_out(interface)

with open('test.txt', 'w', encoding='utf8') as outfile:
    outfile.write(key_self_out)
    outfile.write(key_other_out)
    outfile.write(time_out)
    outfile.write(interface_out)