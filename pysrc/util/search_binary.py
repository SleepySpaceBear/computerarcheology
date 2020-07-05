from content_path import get_content_path

source = ('CoCo/RaakaTu/RaakaTu.bin',0x0600)
target = ('TRS80/RaakaTu/RAAKA.bin',0x4300)
#source_start = 0x3C2A
#source_len = 10

source_start = 0x152B
source_len = 20

with open(get_content_path(source[0]),'rb') as f:
    source_data = f.read()
    
with open(get_content_path(target[0]),'rb') as f:
    target_data = f.read()
    
sp = source_start-source[1]

dat = source_data[sp:sp+source_len]

i = target_data.index(dat)

while source_data[sp] == target_data[i]:
    sp -= 1
    i -= 1

sp+=1
i+=1
    
source_find_start = sp
target_find_start = i

while source_data[sp] == target_data[i]:
    sp += 1
    i += 1
    
print('Source',hex(source_find_start+source[1]),'to',hex(sp+source[1]),"("+hex(sp-source_find_start)+" bytes)")
print('Target',hex(target_find_start+target[1]),'to',hex(i+target[1]))

#print(hex(i+target[1]))