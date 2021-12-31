g = """| 01A7:01A8 | tmp1A7                | used in decoding the input |                   
| 01A9      | tmp1A9                | used in comparing X to Y |                     
| 01AA      | not1AA                | never used |
| 01AB      | tmp1AB                | used in lots of places |                       
| 01AC      | not1AC                | never used |
| 01AD      | tmp1AD                | used in the phrase decoding |                  
| 01AE      | not1AE                | never used |
| 01AF      | not1AF                | never used |
| 01B0      | not1B0                | never used |
| 01B1      | not1B1                | never used |
| 01B2      | tmp1B2                | used in word decoding |                        
| 01B3      | verbWord              | input verb word number |                     
| 01B4      | perpWord              | preposition word number |                     
| 01B5      | prepGiven             | preposition given flag |                       
| 01B6      | phrasePrep            | used in phrase decoding |                      
| 01B7      | adjWord               | adjective word number |                        
| 01B8      | commandTarg           | target object of input command |               
| 01B9      | not1B9                | cleared before decode but never used |        
| 01BA      | lsbAdj1               | screen LSB of 1st adjective |                  
| 01BB      | lsbVerb               | screen LSB of verb |                           
| 01BC      | lsbCursor             | screen lsb used in decoding the input line |   
| 01BD      | lsbError              | screen lsb used for flashing error messages |  
| 01BE      | lastChar              | last character printed to screen |             
| 01BF      | VAR_OBJ_NUMBER        | variable object number |                       
| 01C0:01C1 |  VAR_OBJ_DATA         | variable object data |                         
| 01C2      | not1C2                | never used |
| 01C3      | FIRST_NOUN_NUM        | first input noun number |                      
| 01C4      | firstNounAdj          | first input noun adjective word number |
| 01C5      | firstNounLSB          | first input noun screen LSB |                  
| 01C6:01C7 | FIRST_NOUN_DATA       | first input noun object data |                
| 01C8      | firstNounParams       | first input noun parameter bits |             
| 01C9      | SECOND_NOUN_NUM       | second input noun number |                     
| 01CA      | secondNounAdj         | second input noun adjective word number |
| 01CB      | secondNounLSB         | second input noun noun screen LSB |           
| 01CC:01CD | SECOND_NOUN_DATA      | second input noun object data |                
| 01CE      | secondNounParams      | second input noun parameter bits |             
| 01CF      | tmp1CF                | another screen pointer used in decode |       
| 01D0      | tmp1DO                | used in making index of data fields |         
| 01D1      | PHRASE_FORM           | decoded phrase form |                          
| 01D2      | ACTIVE_OBJ_NUM        | active object |                                
| 01D3:01D4 | ACTIVE_OBJ_DATA       | active object data |                          
| 01D5      | CUR_ROOM              | current room number |                         
| 01D6:01D7 | CUR_ROOM_DATA         | current room data |                          
| 01D8:01D9 | nextToken             | used in decoding input |                      
| 01DA      | tmp1DA                | used in unpacking bytes |                      
| 01DB      | tmp1DB                | used in unpacking bytes |                    
| 01DC      | tmp1DC                | used in unpacking bytes |                     
| 01DD      | tmp1DD                | used in unpacking bytes |                     
| 01DE      | tmp1DE                | used in unpacking bytes |                      
| 01DF      | tmp1DF                | used in unpacking bytes |                     
| 01E0      | tmp1EO                | used in unpacking bytes |                      
| 01E1      | tmp1E1                | used in making index of data fields |         
| 01E2      | tmp1E2                | used in input processing |                    
| 01E3      | tillMORE              | rows left until MORE prompt (not used here) |"""

g = g.split('\n')

ofs = 0x4E4E

def do_trans(s):
    s = int(s,16)+ofs
    s = hex(s).upper()[2:].rjust(4,'0')
    return s

for m in g:
    i = m.index('|',1)
    org = i
    orgm = m
    m = m[1:i].strip()
    i = m.find(':')
    if i>=0:
        a = do_trans(m[0:i])
        b = do_trans(m[i+1:])
        print('| '+a+':'+b+' '+orgm[org:])
    else:
        print('| '+do_trans(m)+'      '+orgm[org:])

