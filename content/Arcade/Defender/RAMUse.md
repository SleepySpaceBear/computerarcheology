![Defender RAM Use](Defender.jpg)

# Defender RAM Use

```
  <$20 (word?) = 
  <$21 (byte?) = 
  <$22 (word) = 
  <$24 (byte) = 
  <$25 (byte) = 
  <$26 (byte?) = 
  <$27 (byte?) = 
  <$28 (word) = 
  <$2A (word?) = 
  <$2B (byte?) = 
  <$2C (word) = 
  <$2E (word) = 
  <$30 (word) = 
  <$32 (word) = 
  <$34 (word) = 
  <$31 (byte) = 
  <$34 (byte) = ?? 
  <$36 (byte) = current page # for addresses $C000-$CFFF 
  <$37 (byte) = 
  <$38 (byte) = 
  <$39 (byte) = 
  <$3A (byte) = only known instance of use is at $D045 in fixed ROM bank. Does not appear to have a use. 
  <$3D (word) = address of position in jump table to go in fixed ROM bank 
  <$3F (word) = address to return to when called subroutine completes processing? 
  <$4C (byte) = 
  <$4E (word) = 
  <$50 (byte?) = 
  <$51 (byte?) = 
  <$52 (word) = 
  <$54 (word) = 
  <$56 (word) = 
  <$58 (byte) = 
  <$59 (word) = 
  <$5D (byte) = 
  <$5F (word) = the address of the 1st link in the event chain
  <$61 (word) = current link in chain beginning at $AF1B? 
  <$63 (word) = current link in "event chain" beginning at $A05F 
  <$65 (word) = 
  <$67 (word) = 
  <$69 (word) = current link in chain beginning at $AF2A? 
  <$6B (word) = 
  <$6D (word) = 
  <$6F (byte?) = 
  <$70 (byte?) = 
  <$71 (byte) = 
  <$73 (byte?) = 
  <$74 (byte?) = 
  <$77 (word?) = stack pointer storage? No?... maybe more like a scratch pad, I think. 
  <$78 (byte) = scratch pad? 
  <$79 (byte) = 
  <$7A (byte) = 
  <$7B (byte) = 
  <$7C (byte) = 
  <$7D (byte) = 
  <$7E (byte) = ?? only found in code w/o any identified entry points ?? 
  <$7F (byte) = 
  <$80 (byte) = 
  <$81 (byte) = 
  <$82 (word) = 
  <$84 (word) = 
  <$86 (word) = 
  <$88 (word) = 
  <$8A (byte) = 
  <$8B (byte) = 
  <$8C (byte) = 
  <$8D (word) = 
  <$8F (byte) = 
  <$90 (word) = 
  <$92 (byte) = 
  <$93 (byte?) = 
  <$94 (byte?) = 
  <$95 (word) = 
  <$99 (byte) = 
  <$9A (byte) = 
  <$9B (word) = 
  <$9D (word) = 
  <$9F (word) = 
  <$A1 (word?) = 
  <$A2 (byte?) = 
  <$A3 (byte?) = 
  <$A4 (word) = 
  <$A6 (word) = 
  <$A8 (word) = 
  <$AB (byte) = 
  <$AC (byte) = 
  <$AD (byte) = 
  <$AE (byte) = 
  <$AF (byte) = 
  <$B0 (word) = 
  <$B2 (byte) = 
  <$B3 (byte) = 
  <$B4 (byte) = 
  <$B5 (byte) = 
  <$B7 (byte) = 
  <$BA (byte) = 
  <$BB (word?) = 
  <$BD (word?) = 
  <$BE (byte?) = 
  <$BF (word?) = 
  <$C0 (byte?) = 
  <$C1 (word?) = 
  <$C2 (byte?) = 
  <$C3 (word?) = 
  <$C4 (byte?) = 
  <$C5 (word?) = 
  <$C7 (word?) = 
  <$C8 (word?) = 
  <$C9 (byte) = 
  <$CA (word) = 
  <$CC (word) = 
  <$CE (word?) = 
  <$CF (byte) = 
  <$D0 (word?) = 
  <$D1 (byte?) = 
  <$D2 (word?) = 
  <$D3 (byte?) = 
  <$D4 (byte) = 
  <$D5 (byte) = 
  <$D6 (word?) = 
  <$D7 (byte?) = 
  <$D8 (word?) = 
  <$D9 (byte?) = 
  <$DA (word) = 
  <$DC (word) = 
  <$DF (byte) = 
  <$E0 (byte?) = 
  <$E1 (byte?) = 
  <$FA (byte) = 
  <$FB (byte) = 
  <$FC (byte) = 
  <$FD (byte) = 
  <$FE (byte) = 
  <$FF (byte) = 
```


```
; From MAME
;	ROM_REGION( 0x19000, "maincpu", 0 )
;	ROM_LOAD( "defend.1",     0x0d000, 0x0800, CRC(c3e52d7e) SHA1(a57f5278ffe44248fc73f9925d107f4024ad981a) )
;	ROM_LOAD( "defend.4",     0x0d800, 0x0800, CRC(9a72348b) SHA1(ed6ce796702ff32209ced3cb1ba3837dbafa526f) )
;	ROM_LOAD( "defend.2",     0x0e000, 0x1000, CRC(89b75984) SHA1(a9481478da38f99efb67f0ecf82d084e14b93b42) )
;	ROM_LOAD( "defend.3",     0x0f000, 0x1000, CRC(94f51e9b) SHA1(a24cfc55de56a72758c76fe2a55f1ec6c353b16f) )
; 1
;	ROM_LOAD( "defend.9",     0x10000, 0x0800, CRC(6870e8a5) SHA1(67ccc194b1753a18af0c85f5e603355549c4f727) )
;	ROM_LOAD( "defend.12",    0x10800, 0x0800, CRC(f1f88938) SHA1(26e48dfeefa0766837b1e762695b9532dbc8bc5e) )
; 2
;	ROM_LOAD( "defend.8",     0x11000, 0x0800, CRC(b649e306) SHA1(9d7bc3c89e5a53c575946f06702c722b864b1ff0) )
;	ROM_LOAD( "defend.11",    0x11800, 0x0800, CRC(9deaf6d9) SHA1(59b018ba0f3fe6eadfd387dc180ac281460358bc) )
; 3
;	ROM_LOAD( "defend.7",     0x12000, 0x0800, CRC(339e092e) SHA1(2f89951dbe55d80df43df8dcf497171f73e726d3) )
;	ROM_LOAD( "defend.10",    0x12800, 0x0800, CRC(a543b167) SHA1(9292b94b0d74e57e03aada4852ad1997c34122ff) )
; 7
;	ROM_LOAD( "defend.6",     0x16000, 0x0800, CRC(65f4efd1) SHA1(a960fd1559ed74b81deba434391e49fc6ec389ca) )


; Fixed ROM (always available in memory map)
```



# Fixed Bank ($D000 - $FFFF) subroutines 

```
## $D013 
The same as the routine at $D015 except the source of the value in the X register 
is provided at an address at 6,X with this entry point.

### Called from:  
Fixed ROM:  $EBF1 : $EDC1 : $F40F : $F418   

## $D015 


### Called from:  
Fixed ROM:  $D00C : $D08F : $F3D8  Bank 1 ROM:/ $C472   


## $D03A 

### Called from: 
Fixed ROM:  $D044 : $D05B : $D0B3 : $D0EF : $EDD5   


## $D03E  
This is one entry point for a subroutine that fits into the address space from 
$D03E to $D07B. The other, much more heavily used, entry point is at $D055. 
This one is used only once. $D055 is used 42 times that I know about. The two 
subroutines converge at address $D066 and continue to the exit point
at $D07A.
### Called from: 
Fixed ROM:  $F2AE     


## $D055 
This is the main entry point for a subroutine that fits into the address space from 
$D03E to $D07B. The other entry point, which is only used once as far as I am aware, is at $D03E. 
$D055 is used 42 times that I know about. The two subroutines converge at address $D066 and continue to the exit point at $D07A.
### Called from: 
Fixed ROM:  $D7AC : $D8C1 : $D94A : $D9D2 : $D9DA : $D9E2 : $D9EA : $D9F2 : $D9FA : 
$DC23 : $E843 : $E88B : $EA85 : $EBB2 : $EDAE : $EDE5 : $EF1E : $EFAC : $F1F4 : 
$F27E    
Bank 1 ROM: $C027 : $C0B2 : $C0BA : $C0C2 : $C279 : $C2E3 : $C363 : $C374 : 
$C37C : $C384 : $C38C : $C394 : $C42E : $C58A : $C690 : $C698 : $C725 : $C735 : 
$C7C9 : $C7D9 : $C829 : $C861    


## $D07C 

### Called from: 
Fixed ROM:  $D86C : $D921 : $DABA : $DCF9  
Bank 1 ROM: $C006 : $C10E : $C266 : $C351 : $C677    


## $D095 

### Called from: 
Fixed ROM:  $DBE5 : $E975 : $EA8A : $EBB7 : $EE65 : $EE73 : $EF23 : $EFB1 : $F2C1 :   

## $D0AD 

### Called from: 
Fixed ROM:  $D095 : $DC77   
Bank 1 ROM: $C397 : $C3BC : $C3E1 : $C4B5 : $C54F : $C5A1    

## $D0C7 

### Called from: 
Fixed ROM:  $F3FB : $F41D  
Bank 1 ROM: $C47A : $C546 : $C59E    

## $D0F2 

### Called from: 
Fixed ROM:  $E526 : $E93A    


## $D21F 
Looks like a subroutine on its face. I have two problems with it that make me think otherwise, however.    1) I can't find where it is ever called. It may be in a jump table that I have not yet discovered, though. 
2) It uses the S register to pick up data in 4 byte packs, which would presumably be OK if you disabled the interrupts first. This routine does not disable the interrupts, though. However, it could be that the calling routine does this so it is unnecessary to do it here. In either case, it sounds like a recipe for disaster to me.
    


## $D260 
I can't find where this is ever called from anywhere. However, it does seem to be a 
clear routine for a structure such as the one that appears to be created by $D21F. 
Unfortunately, I can't find where $D21F is ever called either.    


## $F57B (ScrnBlkClrP2) 
This looks like it will clear a block of screen memory, of any size with byte granularity. It sets the ROM page # to 2 for some reason that I haven't figured out yet. On completion it restores the ROM page # to its previous setting. 
### Entry conditions: 
  X = address to begin
  Y = pointer to size of block to clear 
    1st byte = # lines to clear 
    2nd byte = # of bytes/line to clear 
### Exit conditions: 
  The block is cleared
### Called from: 
Fixed ROM:  $FFB6 : $D41B : $DA81 
Bank 3 ROM: $C533   


## $F5C7 (ScrnBlkClr) 
This subroutine will clear a block of screen memory of any size, with byte granularity. It bypasses the part of ScrnBlkClrP2 that changes the ROM page. Then it converges with ScrnBlkClrP2 at $F58C. Because it restores the ROM page #, this routine also must save the ROM page #. 
### Entry conditions: 
  X = address to begin
  Y = pointer to size of block to clear 
    1st byte = # lines to clear 
    2nd byte = # of bytes/line to clear 
### Exit conditions: 
  The block is cleared
### Called from: 
Fixed ROM:  $FFB9 : $D64D : $D66D : $D6A4 : $DA53 : $F4A5 
Bank 1 ROM: $C15E   


## $F5D1 (VidMemClr) 
### Entry conditions: 

### Exit conditions: 

### Called from: 
Fixed ROM:  $FFBC : $D75A : $D86F : $D959 
Bank 1 ROM: $C043 : $C26C : $C443 : $C681 
Bank 3 ROM: $C24A : $C2C6 : $C5E6 : $C7C8 : $CA2A 
Bank 7 ROM: $C7C8   


## $F7DB (WriteIOPort) 
Saves current ROM page #, switches to I/O page, and writes a byte to the port # specified. Then restores the ROM page #.
### Entry conditions: 
  B = byte to write to port 
  X = I/O port to write 
### Exit conditions: 
  no change 
### Called from:   
Bank 1 ROM: $C068 : $C06D : $C075 : $C07A  
Bank 3 ROM: $C114 : $C224 : $C36D : $C3EF : $C4F8 : $C506 : $C5F1 : $C5F9 : 
$C601 : $C609 : $C77C? : $C796? : $C9CB : $CA70 : $CA9E : $CAB8 : $CAC3 : $CAFF : 
$CB13 : $CB1B    

## $F7F1 (ReadIOPort) 
Saves current ROM page #, switches to I/O page, and reads a byte from the port # specified. Then returns the ROM page # to the same as it was on entry.
### Entry conditions: 
  X = I/O port to read 
### Exit conditions: 
  B = data read from port 
### Called from: 
Bank 1 ROM: $C312 
Bank 3 ROM: $C0EB : $C10B : $C1C6 : $C1E2 : $C322 : $C347 : $C34E : $C42F : 
$C4C4 : $C4EE : $C55C : $C5A1 : $C5B5 : $C7FB : $C878 : $C9AC : $CA18 : $CA22 : 
$CA76    

## $F813 (SRAMRead) 
Performs the actual reading of the nybbles out of the SRAM.
### Entry conditions:  
  X = the memory location to be read 
### Exit conditions: 
  A = the contents of the ,X and the 1,X. They are each only 4 bits wide and thus are packed into a single byte in the A register. ,X is the MSNybble and 1,X is the LSNybble. 
  X = memory location + 2.

See $F822    

## $F822 (RdSRAMbyte) 
  Saves the contents of the $Cxxx page before switching to the 0, or I/O, page, calls $F813, and then restores the previous contents of the $Cxxx page. $F813 is not called from any other location so, if one wanted to speed things up just a bit, it could be incorporated into this subroutine.
### Entry conditions: 
  X = the address of the first of the two memory locations to be read
### Exit conditions: 
  A = the contents of the ,X and the 1,X. They are each only 4 bits wide and thus are packed into a single byte in the A register. ,X is the MSNybble and 1,X is the LSNybble.  
  X = memory location + 2.

### Called from: 
Fixed ROM:  $D82B : $D88B : $DE83 : $F838 : $F83C : $FFA1  
Bank 1 ROM: $C151 : $C332  
Bank 3 ROM: $C8DD : $C951 : $C973 : $C991    

## $F838 (SRAMWordRd) 
### Entry conditions: 
  X = the address of the first of the two memory locations to be read
### Exit conditions: 
  D = the contents of the ,X , 1,X, 2,X and 3,X. They are each only 4 bits wide and thus are packed into a single word in the D register. As with the 8 bit variation the MSNybble is first followed by decreasingly significant digits.   
  X = memory location + 4.
### Called from: 
Fixed ROM:  $D8A4 : $DEC5 : $FFA7 
Bank 1 ROM: $C149 : $C1C7 : $C32D 
Bank 3 ROM: $C937 : $C963    

## $F83A (SRAMByteRd) 
### Entry conditions: 
  X = the address of the first of the two memory locations to be read
### Exit conditions: 
  B = the contents of the ,X and the 1,X. They are each only 4 bits wide and thus are packed into a single byte in the B register. ,X is the MSNybble and 1,X is the LSNybble.  
  X = memory location + 2.

### Called from: 
Fixed ROM:  $D775 : $FFA4 
Bank 3 ROM: $C101 : $C11A : $C835 : $C8C8 : $CBF2 : $CBF7 : $CC38 : $CC4E : 
$CC5E : $CC6C     

## $F842 (SRAMWrite) 
Performs the actual writing into the SRAM.
### Entry conditions: 
  A = byte to be written into 2 nybbles of SRAM. 
  X = address of first, most signigicant nybble. 
### Exit conditions: 
  The byte is written into 2 nybbles in the SRAM

See $F84E    

## $F84E (WrSRAMbyte) 
### Entry conditions: 

### Called from: 
Fixed ROM:  $D8D0 : $F864 : $F86A : $FFAA 
Bank 1 ROM: $C1B1 : $C1B9 
Bank 3 ROM: $C120 : $C95B : $CBB5 : $CBC8 : $CC1B : $CCCE   

## $F864 (SRAMWordWr) 
### Entry conditions: 

### Called from: 
Fixed ROM:  $FFB0 
Bank 1 ROM: $C1AC : $C1CC 
Bank 3 ROM: $C94E? : $CC08   

## $F866 (SRAMByteWr) 
### Entry conditions: 

### Called from: 
Fixed ROM:  $FFAD 
Bank 3 ROM: $C84B : $C854 : $CB9C   


## $FC60 (see $FC60) 
This routine consists of a single instruction: JMP  $FC69  Further discussion will be found in the $FC69 subroutine entry.    


## $FC63 (see $FCCC)
This routine consists of a single instruction: JMP  $FCCC  Further discussion will be found in the $FCCC subroutine entry.    


## $FC66 (see $FD2D)
This routine consists of a single instruction: JMP  $FD2D  Further discussion will be found in the $FD2D subroutine entry.    



## $FC69 
All known calls to this routine are made via a jump to $FC60.
The reasoning behind this remains a mystery to me.

### Called from:  
Fixed ROM:  $E9A1 : $EAB1 : $EB6C : $EF5D : $EFE6[[br]]
Bank 1 ROM: $C404 : $C574 : $C5BC : $C79B   



## $FCCC 
All known calls to this rountine are made via a jump to $FC63.

### Called from:  
Fixed ROM:  $E541 : $EC08 : $EE88 : $EE20 : $F438



## $FD2D 
All known calls to this rountine are made via a jump to $FC66.

### Called from:  
Fixed ROM:  $E823 
```
