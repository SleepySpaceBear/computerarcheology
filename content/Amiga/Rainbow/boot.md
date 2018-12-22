![boot](Rainbow.jpg)

The first part that's loaded is the boot block, it's located on the first sector of the first track,

it looks like this -- taken from the [ADF-faq](http://lclevy.free.fr/adflib/adf_info.html#p41):

```plain
* BootBlock
-------------------------------------------------------------------------------
offset	size    number	name		meaning
-------------------------------------------------------------------------------
0/0x00  char    4       DiskType	'D''O''S' + flags
                                        flags = 3 least signifiant bits
                                               set         clr
					  0    FFS         OFS
                                          1    INTL ONLY   NO_INTL ONLY
                                          2    DIRC&INTL   NO_DIRC&INTL
4/0x04  ulong   1       Chksum          special block checksum
8/0x08  ulong   1       Rootblock       Value is 880 for DD and HD 
					 (yes, the 880 value is strange for HD)
12/0x0c char    *       Bootblock code  (see 5.2 'Bootable disk' for more info)
                                        The size for a floppy disk is 1012,
                                        for a harddisk it is
                                        (DosEnvVec->Bootblocks * BSIZE) - 12
-------------------------------------------------------------------------------
```

This is the boot block from Rainbow Islands.

The code in the boot block allocates 3584 bytes of memory. Then it reads 3584 bytes from offset 1024 (just after the boot block) from the disk and jumps to it.

```plain
		dc.b $44 ; D
		dc.b $4F ; O
		dc.b $53 ; S
		dc.b   0
		dc.b $82
		dc.b $B6 ; 
		dc.b $CC ; 
		dc.b $82 ; 
		dc.b 0
		dc.b   0
		dc.b   3
		dc.b $70 ; p

start:
		bra.s	allocate_mem
	
		dc.b $19
		dc.b   2
		dc.b   1
		dc.b   0
		dc.b   0
		dc.b $E0
		dc.b   6
		dc.b   2
		dc.b   3
		dc.b   0
		dc.b  $B
		dc.b   0
		dc.b   2
		dc.b   0
		dc.b   0
		dc.b   2
		dc.b $4B
		dc.b $32
		dc.b   0
		dc.b $16
		dc.b   0
		dc.b $55
		dc.b   1
		dc.b $C4
		dc.b $FF
		dc.b   0

allocate_mem:
		move.l	a1,-(sp)
		move.l	#3584,d0
		move.l	#$10002,d1
		movea.l	(4).w,a6
		jsr	-$C6(a6) ;LVOAllocMem
		movea.l	d0,a3
		movea.l	(sp)+,a1
		tst.l	d0
		beq.s	fail
		movea.l	a1,a2

loader:
		move.l	a3,$28(a1)
		move.l	#3584,$24(a1)
		move.l	#1024,$2C(a1)
		move.w	#2,$1C(a1)
		movea.l	(4).w,a6
		jsr	-$1C8(a6) ; LVODoIO
		movea.l	a2,a1
		move.b	$1F(a1),d0
		bne.s	loader
		movea.l	(8).l,a5
		jmp	(a3)

fail:
		moveq	#$FFFFFFFF,d0
		rts
	
		dc.b   0
		dc.b   0
		
copyright:      dc.b 'Copylock Amiga (c)1988-90 Rob Northen Computing, U.K. All Rights Reserved.',0

```
