![1loader-dec](Rainbow.jpg)

This is what the encrypted part looks after decryption:

```
sub_5A68:
                subq.l  #6,(TRACE_VECTOR).l
                clr.l   (ACCESS_FAULT).l
                clr.l   (ILLEGAL_INSTRUCTION).l
                subq.w  #7,a2
                adda.w  a4,a2
                tst.w   d3
                negx.b  d5
                clr.l   d1
                exg     a3,a2
                move.l  #$B386B186,$14(sp)
                bset    #$6E,d5
                adda.w  d0,a4
                tst.b   d5
                negx.l  d1
                clr.w   d3
                exg     d5,d4
                cmpa.l  (TRACE_VECTOR).l,sp
                subq.w  #2,d0
                cmpi.l  #$957C957C,d1
                lsl.w   #3,d0
                and.l   d0,d3
                neg.b   d2
                ori.w   #$96F2,d3
                subx.w  d3,d5
                move.l  #$42C6F,4(sp)
                nop
                lsr.b   d4,d2
                and.b   d2,d5
                bset    d2,d1
                tst.w   d3
                negx.l  d4
                roxl.b  d1,d5
                btst    #$88,d1
                addq.b  #4,d1
                bchg    d3,d2
                bset    #$76,d5
                adda.w  d0,a4
                lsl.l   d1,d4
                and.b   d4,d1
                addq.b  #4,d1
                bchg    d4,d3
                bset    #$66,d5
                adda.w  d0,a5
                lsl.b   #1,d5
                and.b   d5,d1
                neg.w   d0
                btst    #$20,d3
                addq.w  #6,a3
                moveq   #$FFFFFFCA,d5
                bset    #$E,d1
                add.l   #$9D749D85,d1
                lsl.w   #2,d0
                and.w   d0,d2
                addx.w  d0,d2
                bchg    #$EA,d2
                subx.b  d2,d4
                eor.w   d5,d3
                adda.w  a4,a2
                lsr.b   d5,d2
                and.w   d2,d5
                neg.l   d4
                btst    #$81,d0
                addq.l  #8,a0
                moveq   #$1A,d3
                bset    #$5E,d5
                adda.w  d0,a4
                tst.b   d5
                negx.l  d1
                clr.w   d3
                exg     d5,d4
                cmpa.l  (TRACE_VECTOR).l,sp
                subq.w  #2,d0
                move.l  #$D246D046,$10(sp)
                negx.b  d2
                roxr.b  #5,d3
                btst    #$C0,d5
                addq.w  #3,d5
                bchg    d1,d0
                bset    #$AE,d3
                adda.w  a4,a2
                lsr.b   #5,d2
                and.w   #$A8F1,d5
                addx.b  d1,d4
                sub.l   $14(sp),d0
                addx.b  d1,d4
                sub.l   $14(sp),d0
                subq.l  #5,d4
                cmpa.l  (TRACE_VECTOR).l,sp
                negx.l  d1
                clr.w   d3
                addx.l  d3,d0
                cmpa.l  (TRACE_VECTOR).l,sp
                move.l  #$246A71F,$C(sp)
                adda.w  d0,a4
                lsr.l   d1,d4
                and.b   #$91,d1
                addx.l  d3,d0
                cmpa.l  (TRACE_VECTOR).l,sp
                subq.l  #2,a0
                adda.l  a1,a2
                bclr    #$E4,d4
                tas     d0
                neg.b   d2
                btst    #$B0,d5
                addq.b  #3,d1
                subq.b  #3,d2
                sub.l   $1C(sp),d0
                negx.b  d5
                clr.w   d1
                exg     a3,a2
                sub.l   $14(sp),d0
                subq.l  #5,d3
                cmpa.l  (TRACE_VECTOR).l,sp
                subq.l  #5,a1
                nop
                lsl.l   #1,d4
                and.b   d4,d1
                neg.b   d5
                ori.l   #$AC32AC32,d1
                subx.l  d0,d2
                eor.l   d3,d1
                move.b  d0,d2
                lsl.w   d3,d0
                neg.w   d0
                btst    #0,d3
                addq.w  #6,a2
                moveq   #$FFFFFFAA,d5
                bset    #$EE,d1
                add.l   #$BD54BD54,d1
                lsl.w   #3,d0
                and.l   #$BE31BE42,d3
                addx.b  d5,d1
                move.l  #$D246D046,$10(sp)
                bset    #$96,d3
                adda.w  a4,a2
                lsr.b   #5,d2
                and.w   d2,d5
                addx.b  d2,d4
                bchg    #$72,d5
                subx.l  d4,d0
                eor.b   d1,d5
                adda.w  d0,a4
                lsr.l   d1,d4
                and.b   #$81,d1
                addx.l  d3,d0
                cmpa.l  (TRACE_VECTOR).l,sp
                subq.l  #2,a0
                adda.l  a1,a2
                bclr    #$E5,d4
                tas     d0
                neg.b   d2
                btst    #$A0,d5
                addq.b  #3,d1
                subq.b  #3,d1
                sub.l   $1C(sp),d0
                negx.b  d5
                clr.w   d0
                exg     a3,a2
                move.l  #$B386B186,$14(sp)
                bset    #$36,d5
                adda.w  d0,a4
                tst.b   d5
                negx.l  d1
                clr.w   d3
                exg     d5,d4
                sub.l   $C(sp),d0
                addx.l  d3,d0
                cmpa.l  (TRACE_VECTOR).l,sp
                subq.w  #6,a0
                cmpi.l  #$BD54BD54,d1
                lsl.w   #3,d0
                and.l   #$BE31BE31,d3
                addx.w  d5,d2
                sub.l   $14(sp),d0
                bset    d0,d5
                cmpa.w  d0,a4
                tas     d1
                move.l  #$B386B186,$14(sp)
                subx.w  d2,d5
                eor.w   d5,d3
                move.b  d3,d5
                lsr.b   d5,d2
                and.w   d2,d5
                neg.l   d4
                btst    #$51,d0
                addq.l  #8,a0
                moveq   #$FFFFFFEA,d3
                bset    #$2E,d5
                adda.w  d0,a4
                tst.b   d5
                negx.l  d1
                clr.w   d3
                exg     d5,d4
                cmpa.l  (TRACE_VECTOR).l,sp
                subq.w  #2,d0
                move.l  #$D446D246,$10(sp)
                negx.w  d2
                roxr.w  d5,d3
                btst    #$90,d5
                addq.w  #3,d5
                bchg    d2,d0
                bset    #$7E,d3
                adda.w  a4,a2
                lsr.b   d5,d2
                and.w   #$D8C1,d5
                addx.b  d1,d4
                sub.l   $14(sp),d0
                subq.l  #5,d4
                cmpa.l  (TRACE_VECTOR).l,sp
                negx.l  d1
                clr.w   d3
                addx.w  d3,d5
                move.l  #$B386B586,$14(sp)
                bset    #$CE,d1
                adda.w  d0,a4
                or.b    #$AB,d1
                cmpa.l  (TRACE_VECTOR).l,sp
                tst.l   d1
                negx.b  d3
                roxr.w  d5,d3
                btst    #$98,d5
                move.l  sp,(TRACE_VECTOR).l
                bset    #$86,d3
                move.w  d0,d4
                and.l   #$DE11DE22,d3
                addx.b  d5,d1
                move.l  sp,(TRACE_VECTOR).l
                subq.b  #7,d2
                sub.l   $1C(sp),d0
                negx.b  d5
                clr.l   d1
                exg     a3,a2
                sub.l   $14(sp),d0
                subq.l  #8,d3
                cmpa.l  (TRACE_VECTOR).l,sp
                move.l  #$1014E73,-(sp)
                move.l  #$4E924CDF,-(sp)
                move.l  #$FFFC6602,-(sp)
                move.l  #$C68CF47,-(sp)
                move.l  #$B198B190,-(sp)
                move.l  #8,-(sp)
                move.l  #$FFFCD0B9,-(sp)
                move.l  #$C2028,-(sp)
                move.l  #$23C80000,-(sp)
                move.l  #$206F000A,-(sp)
                move.l  #$B198B190,-(sp)
                move.l  #8,-(sp)
                move.l  #$FFFCD0B9,-(sp)
                move.l  #$C2028,-(sp)
                move.l  #$20790000,-(sp)
                move.l  #$27CFFFF,-(sp)
                move.l  #$48E78080,-(sp)
                move.l  #$4E714E71,-(sp)
                move.l  #$44E71,-(sp)
                move.l  #$BD96BDAE,-(sp)
                move.l  #$10,(ADDRESS_ERROR).l
                move.l  sp,(TRACE_VECTOR).l ; set new TRACE function
                addi.l  #$C,(TRACE_VECTOR).l ; skip reencryption from now on
                move.w  $B8(sp),d6
                ori.w   #$F8FF,d6
                move.w  d6,$12(sp)
                moveq   #0,d0
                moveq   #1,d1
                movem.l d2-a3,-(sp)
                moveq   #0,d2
                roxr.l  #3,d0
                roxr.l  #1,d2
                roxl.l  #3,d0
                move.b  d0,d2
                move.l  d1,d3
                moveq   #3,d7           ; loop counter
                moveq   #0,d6

loc_5DE4:
                bsr.w   go_to_track_0
                beq.s   loc_5DF8
                moveq   #1,d0
                bsr.w   step_to_track
                bsr.w   wait_up_to_3s_for_RDY
                bsr.w   read_key

loc_5DF8:
                bsr.w   step_back_to_original_track
                tst.l   d6
                bne.s   loc_5E0E
                tst.l   d2
                bpl.s   loc_5E0E
                addq.b  #1,d2
                andi.b  #3,d2
                dbf     d7,loc_5DE4

loc_5E0E:
                bsr.w   erase_disk_buffer
                move.w  d2,d1
                move.l  d6,d0
                movem.l (sp)+,d2-a3
                bra.w   decrypt

read_key:
                subq.w  #4,sp

loc_5E20:
                move.w  #$8914,d0
                move.w  #$32,d1         ; disklen
                lea     disk_buffer,a0  ; buffer
                bsr.w   sub_5F4C
                bmi.s   loc_5EA8
                move.w  #7,d1

loc_5E36:
                sub.l   (a0)+,d0
                dbf     d1,loc_5E36
                cmp.l   #$A573632C,d0
                bne.s   loc_5E20
                lea     disk_buffer,a0

loc_5E48:
                move.w  #$8911,d0       ; syncword
                bsr.w   sub_5F86
                beq.s   loc_5EA8
                cmpi.w  #$2A91,(a0)
                bne.s   loc_5E48
                move.l  d0,(sp)

loc_5E5A:
                move.w  #$8912,d0       ; syncword
                bsr.w   sub_5F86
                beq.s   loc_5EA8
                cmpi.w  #$AA92,(a0)
                bne.s   loc_5E5A
                move.l  d0,d1
                move.l  (sp),d0
                bsr.w   sub_5EAC
                bmi.s   loc_5EA8

loc_5E74:
                move.w  #$8914,d0       ; syncword
                bsr.w   sub_5F86
                beq.s   loc_5EA8
                cmpi.w  #$AA94,(a0)
                bne.s   loc_5E74
                move.l  (sp),d1
                bsr.s   sub_5EAC
                bmi.s   loc_5EA8
                move.w  #$8951,d0       ; syncword
                bsr.w   sub_5FEA
                cmp.w   #$3AC,d0
                blt.s   loc_5EA8
                cmp.w   #$53C,d0
                bgt.s   loc_5EA8
                move.w  #$B,d1

loc_5EA2:
                sub.l   (a0)+,d6
                dbf     d1,loc_5EA2

loc_5EA8:
                addq.w  #4,sp
                rts

sub_5EAC:
                sub.l   d1,d0
                bmi.s   loc_5EC0
                mulu.w  #$64,d0
                divu.w  d1,d0
                cmp.b   #2,d0
                blt.s   loc_5EC0
                moveq   #0,d0
                rts

loc_5EC0:
                moveq   #$FFFFFFFF,d0
                rts

erase_disk_buffer:
                lea     disk_buffer,a0
                move.w  #$19,d1
                move.l  #$E3B6,d0

loc_5ED2:
                mulu.w  #$11,d0
                addq.l  #1,d0
                move.w  d0,(a0)+
                dbf     d1,loc_5ED2
                rts

go_to_track_0:
                bsr.w   enable_df0
                bsr.w   find_track_0
                move.w  d0,d5           ; store number of tracks we stepped * 2 in d5
                addq.w  #1,d0
                beq.s   locret_5F06
                btst    #2,(CIA_A_PRA).l ; check CHNG
                bne.s   locret_5F06
                moveq   #2,d0
                bsr.w   step_to_track
                btst    #2,(CIA_A_PRA).l ; check CHNG

locret_5F06:
                rts

step_back_to_original_track:
                move.w  d5,d0
                bmi.s   locret_5F18
                bsr.w   step_to_track
                tst.l   d6
                beq.s   loc_5F2E
                tst.b   d3
                beq.s   loc_5F2E

locret_5F18:
                rts

enable_df0:
                moveq   #$FFFFFFFF,d0
                move.b  d0,(CIA_B_PRB).l
                bclr    #7,d0           ; clear MOTOR bit
                bsr.s   toggle_motor
                moveq   #$1E,d0         ; delay 30 ms
                bra.w   delay_ms

loc_5F2E:
                moveq   #$FFFFFFFF,d0

toggle_motor:
                move.b  d0,(CIA_B_PRB).l ; write to motor bits
                addq.b  #3,d2
                bclr    d2,d0
                move.b  d0,(CIA_B_PRB).l ; select DF0
                bset    d2,d0
                move.b  d0,(CIA_B_PRB).l ; unselect
                subq.b  #3,d2
                rts

sub_5F4C:
                bsr.w   sub_6046
                lsr.w   #1,d1
                ori.w   #$8000,d1       ; Disk DMA enable
                move.w  d1,$24(a1)
                move.w  d1,$24(a1)
                move.l  #3000,d0        ; start a 3 second timer
                bsr.w   setup_1_ms_timer

loc_5F68:
                btst    #1,$1F(a1)
                bne.s   loc_5F7E
                bsr.w   check_for_timeout
                bne.s   loc_5F68
                bsr.w   sub_6074
                moveq   #$FFFFFFFF,d0
                rts

loc_5F7E:
                bsr.w   sub_6074
                moveq   #0,d0
                rts

sub_5F86:
                movea.l a0,a3
                bsr.w   sub_6046
                move.w  #$8000,d1
                move.l  #$FFF64E75,-(sp)
                move.l  #$6AF851C8,-(sp)
                move.l  #$4A29001A,-(sp)
                move.l  #$72005281,-(sp)
                move.l  #$6AFA16C1,-(sp)
                move.l  #$3229001A,-(sp)
                move.l  #$6AFA16C1,-(sp)
                move.l  #$3229001A,-(sp)
                move.l  #$1A67F8,-(sp)
                move.l  #$8290004,-(sp)
                move.l  #$303C03FE,-(sp)
                move.w  d1,$24(a1)
                move.w  d1,$24(a1)
                movea.l sp,a2
                exg     d7,d7
                lea     $2C(sp),sp
                bsr.w   sub_6074
                move.l  d1,d0
                rts

sub_5FEA:
                bsr.w   sub_6046
                move.w  #$8000,d1
                move.l  #$4E714E75,-(sp)
                move.l  #$DD0067EE,-(sp)
                move.l  #$400BF,-(sp)
                move.l  #$52410839,-(sp)
                move.l  #$1A6A02,-(sp)
                move.l  #$DD001029,-(sp)
                move.l  #$400BF,-(sp)
                move.l  #$72000839,-(sp)
                move.l  #$1A67F8,-(sp)
                move.l  #$8290004,-(sp)
                move.w  d1,$24(a1)
                move.w  d1,$24(a1)
                movea.l sp,a2
                exg     d7,d7
                lea     $28(sp),sp
                bsr.w   sub_6074
                move.l  d1,d0
                rts

sub_6046:
                lea     (DFF000).l,a1
                move.w  #$4000,unk_F024-DFF000(a1)
                move.l  a0,$20(a1)
                move.w  d0,$7E(a1)
                move.w  #$8010,$96(a1)
                move.w  #$6600,$9E(a1)
                move.w  #$9500,$9E(a1)
                move.w  #2,$9C(a1)
                rts

sub_6074:
                move.w  #2,$9C(a1)
                move.w  #$4000,$24(a1)
                move.w  #$400,$9E(a1)
                rts


wait_up_to_3s_for_RDY:
                move.l  #$BB8,d0        ; delay 3 seconds
                bsr.w   setup_1_ms_timer

loc_6092:
                btst    #5,(CIA_A_PRA).l ; check RDY
                beq.s   loc_60A6
                bsr.w   check_for_timeout
                bne.s   loc_6092        ; check RDY
                moveq   #$FFFFFFFF,d0
                rts

loc_60A6:
                moveq   #0,d0
                rts

step_to_track:
                move.w  d0,-(sp)
                lsr.w   #1,d4
                lsr.w   #1,d0
                moveq   #0,d1
                sub.w   d4,d0
                bpl.s   loc_60BA
                moveq   #$FFFFFFFF,d1
                neg.w   d0

loc_60BA:
                bsr.w   step_track
                move.w  (sp)+,d4
                bra.s   sub_6122


find_track_0:
                moveq   #$55,d1         ; number of tracks to step

loc_60C4:
                btst    #4,(CIA_A_PRA).l
                beq.s   loc_60E2
                move.l  d1,-(sp)
                moveq   #1,d0
                moveq   #$FFFFFFFF,d1
                bsr.w   step_track
                move.l  (sp)+,d1
                dbf     d1,loc_60C4
                move.w  d1,d0
                rts

loc_60E2:
                moveq   #0,d4
                bsr.w   sub_6122
                moveq   #$55,d0
                sub.w   d1,d0
                add.w   d0,d0           ; double it
                rts



step_track:
                tst.b   d0
                beq.s   exit
                move.w  d0,-(sp)
                bsr.w   setup_prb_in_D0
                tst.b   d1              ; step in or out
                bne.s   loc_6102
                bclr    #1,d0           ; clear DIR

loc_6102:
                bclr    #0,d0           ; clear STEP
                move.b  d0,(CIA_B_PRB).l ; step drive
                bset    #0,d0           ; set STEP
                move.b  d0,(CIA_B_PRB).l ; stop STEP
                moveq   #4,d0           ; delay 4 ms
                bsr.s   delay_ms
                move.w  (sp)+,d0
                subq.b  #1,d0
                bne.s   step_track

exit:
                rts


sub_6122:
                bsr.w   setup_prb_in_D0
                move.b  d0,(CIA_B_PRB).l
                rts

setup_prb_in_D0:
                move.b  (CIA_B_PRB).l,d0 ; get PRB from CIAB
                ori.b   #$7F,d0          ; keep all but motor
                addq.b  #3,d2
                bclr    d2,d0            ; clear SEL0
                subq.b  #3,d2
                btst    #0,d4
                beq.s   locret_6148
                bclr    #2,d0            ; clear SIDE

locret_6148:
                rts

delay_ms:
                bsr.w   setup_1_ms_timer

loc_614E:
                btst    #0,(CIA_B_CRA).l
                bne.s   loc_614E
                subq.l  #1,d0           ; decrement delay length
                bne.s   delay_ms
                rts

check_for_timeout:
                btst    #0,(CIA_B_CRA).l
                bne.s   locret_6184
                subq.l  #1,d0
                beq.s   locret_6184

setup_1_ms_timer:
                move.b  #8,(CIA_B_CRA).l
                move.b  #$CC,(CIA_B_TALO).l
                move.b  #2,(CIA_B_TAHI).l

locret_6184:
                rts

disk_buffer:    dc.b $27
                dcb.b 2,$80
                dc.b $D6, 6, $1E, $B9, $12, $5A, $32, $DF, $76, $FC, $A4
                dc.b $E9, $E4, $48, $5F, $8E, $2E, $FB, $E, $26, $32, $DD
                dc.b $D2, $98, $E4, $AF, $76, $B7, $F2, $34, $52, $B1
                dc.b $5E, $A4, $3E, $3B, $32, $4C, $52, $91, $56, $BF
                dc.b $F6, $3C, $72, $84, $D2, $53, $EE, $1E, $78, 5, $BE

decrypt:
                moveq   #0,d1
                lea     $61C0,a6
                adda.l  #(unk_62A8-$61C0),a6
                move.l  #$400,d6

loc_61D0:
                rol.l   d0,d1
                add.l   d1,d2
                ror.l   d2,d3
                add.l   d3,d4
                ror.l   d4,d5
                add.l   d5,d0
                add.l   d0,(a6)+
                subq.l  #4,d6
                bne.s   loc_61D0
                lea     $61F4,a6
                move.l  loc_61F0-loc_61F4(a6),d6
                add.l   (ACCESS_FAULT).l,d6

loc_61F0:
                ori     #$A71F,sr

loc_61F4:
                addi.l  #$44,(TRACE_VECTOR).l
                adda.l  #$50,sp
                move.l  #$7FFF4E73,-(sp)
                move.l  #$584F0257,-(sp)
                move.l  #$4CDF7FFF,-(sp)
                move.l  #$4FEE007C,-(sp)
                move.l  #$2D4C00BE,-(sp)
                move.l  #$598066FA,-(sp)
                move.l  #$67064299,-(sp)
                move.l  #$66FA200B,-(sp)
                move.l  #$22D85980,-(sp)
                move.l  #$66FA6006,-(sp)
                move.l  #$23205980,-(sp)
                move.l  #$D1C0D3C0,-(sp)
                move.l  #$B3C86F0C,-(sp)
                move.l  #$200A6720,-(sp)
                move.l  #$4E7B0002,-(sp)
                move.l  #$202E00B8,-(sp)
                move.l  #$4DFAFFEE,-(sp)
                move.l  #$10,-(sp)
                move.l  #$1423DF,-(sp)
                move.l  #$4487A,-(sp)
                move.l  #$BD96BDAE,-(sp)
                lea     unk_62A8,a0
                movea.l a0,a1
                suba.l  #$8C0,a1
                movea.l #$400,a2
                movea.l #$8C0,a3
                movea.l a1,a4
                adda.l  #$C,a4
                move.l  sp,(TRACE_VECTOR).l
```