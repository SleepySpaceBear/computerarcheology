![orig-boot](Rainbow.jpg)

After running the protection, this is what we end up with, the original boot block in all it's glory:

```plain
bootblock:      dc.b 'DOS',0
checksum:       dc.l $D5245E13
rootblock:      dc.l 0
sub_59F4:
                bra.s   loc_5A10
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
loc_5A10:
                lea     (unk_DFF000).l,a4
                move.w  #$7FFF,$9A(a4)
                move.w  #$7FFF,$96(a4)
                lea     $180(a4),a0
                moveq   #15,d0

loc_5A28:
                clr.l   (a0)+
                dbf     d0,loc_5A28
                lea     (relocation).w,a5
                lea     loc_5A3C,a0
                move.l  a0,(dword_80).w
                trap    #0

loc_5A3C:
                movea.l a5,sp
                movea.l a5,a0
                lea     bootblock,a1
                move.w  #$FF,d0

loc_5A48:
                move.l  (a1)+,(a0)+
                dbf     d0,loc_5A48
                jmp     $6A(a5)




sub_5A52:
                lea     (copperlist+$2E),a0
                lea     $4480(a5),a1
                move.l  a1,d1
                moveq   #$28,d2
                moveq   #3,d0

loc_5A60:
                move.w  d1,4(a0)
                swap    d1
                move.w  d1,(a0)
                swap    d1
                add.l   d2,d1
                addq.l  #8,a0
                dbf     d0,loc_5A60
                lea     copperlist,a0
                move.l  a0,$80(a4)
                clr.w   $88(a4)
                move.w  #$8280,$96(a4)
                lea     $4400(a5),a3
                move.w  $20(a5),d3
                beq.s   loc_5A9A
                moveq   #$3F,d5
                bsr.w   sub_5BAE
                moveq   #1,d5
                moveq   #1,d6
                bsr.s   sub_5AB8

loc_5A9A:
                move.w  $22(a5),d3

loc_5A9E:
                beq.s   loc_5A9E
                move.w  $24(a5),d5
                move.l  a3,-(sp)
                bsr.w   sub_5BAE
                move.w  $20(a5),d0
                beq.s   locret_5AB6
                moveq   #$10,d5
                moveq   #$FFFFFFFF,d6
                bsr.s   sub_5AB8

locret_5AB6:
                rts




sub_5AB8:
                move.w  #$20,$9C(a4)

loc_5ABE:
                btst    #5,$1F(a4)
                beq.s   loc_5ABE
                lea     $4404(a5),a0
                lea     (copperlist+$4E),a1
                move.b  d5,d0
                moveq   #$B,d1
                asl.w   d1,d0
                moveq   #$F,d4

loc_5AD6:
                move.w  (a0)+,d1
                add.w   d1,d1
                moveq   #$1E,d2
                and.w   d1,d2
                mulu.w  d0,d2
                swap    d2
                move.w  #$1E0,d3
                and.w   d1,d3
                mulu.w  d0,d3
                swap    d3
                andi.w  #$F0,d3
                or.w    d3,d2
                clr.b   d1
                mulu.w  d0,d1
                swap    d1
                move.b  d2,d1
                move.w  d1,(a1)
                lea     4(a1),a1
                dbf     d4,loc_5AD6
                add.b   d6,d5
                cmp.b   #$10,d5
                bls.s   sub_5AB8
                rts

copperlist:     dc.w     1,$FF7E
                dc.w   $96, $100
                dc.w   $8E,$2C81
                dc.w   $90,  $C1
                dc.w   $92,  $38
                dc.w   $94,  $D0
                dc.w  $100,$4200
                dc.w  $102,    0
                dc.w  $104,    0
                dc.w  $108,  $78
                dc.w  $10A,  $78
                dc.w   $E0,    0
                dc.w   $E2,    0
                dc.w   $E4,    0
                dc.w   $E6,    0
                dc.w   $E8,    0
                dc.w   $EA,    0
                dc.w   $EC,    0
                dc.w   $EE,    0
                dc.w  $180,    0
                dc.w  $182,    0
                dc.w  $184,    0
                dc.w  $186,    0
                dc.w  $188,    0
                dc.w  $18A,    0
                dc.w  $18C,    0
                dc.w  $18E,    0
                dc.w  $190,    0
                dc.w  $192,    0
                dc.w  $194,    0
                dc.w  $196,    0
                dc.w  $198,    0
                dc.w  $19A,    0
                dc.w  $19C,    0
                dc.w  $19E,    0
                dc.w $3701,$FF7E
                dc.w   $96,$8100
                dc.w $FF01,$FF7E
                dc.w   $96, $100
                dc.w $FF7F,$FF7E



sub_5BAE:
                ext.l   d3
                divu.w  #$B,d3
                move.w  d3,d4
                swap    d3

loc_5BB8:
                moveq   #$B,d6
                ext.l   d3
                divu.w  d6,d3
                swap    d3
                sub.w   d3,d6
                sub.w   d6,d5
                bpl.s   loc_5BCA
                add.w   d5,d6
                clr.w   d5

loc_5BCA:
                movem.l d2-d7/a2-a3/a6,-(sp)
                lea     (CIA_offset).l,a1
                moveq   #2,d7
                lea     $26(a5),a6
                moveq   #$79,d0
                lsr.w   #1,d4
                bcs.s   loc_5BE2
                moveq   #$7D,d0

loc_5BE2:
                move.b  d0,$100(a1)     ; CIA_B_PRB
                nop
                andi.b  #$F7,d0
                move.b  d0,$100(a1)     ; CIA_B_PRB
                move.b  d0,$A(a5)
                move.b  #$9C,$400(a1)   ; CIA_B_TALO
                move.b  #$AE,$500(a1)   ; CIA_B_TAHI 0xae9c = 63ms
                bsr.w   start_timer_A_and_wait_for_eqpiration
                move.w  d4,2(a5)
                move.w  d3,4(a5)
                move.w  d6,(a5)
                move.l  a3,6(a5)
                tst.w   (a6)
                bpl.s   loc_5C1A
                bsr.w   find_track_0

loc_5C1A:
                bsr.w   step_x_steps_in_y_dir
                move.w  #$8210,$96(a4)
                move.w  #$4489,$7E(a4)
                move.w  #$9500,$9E(a4)
                move.w  #$4000,$24(a4)
                move.w  #2,$9C(a4)
                lea     $406(a5),a0
                clr.l   (a0)
                move.l  a0,$20(a4)
                moveq   #$A,d0

loc_5C48:
                clr.w   $438(a0)
                lea     $440(a0),a0
                dbf     d0,loc_5C48
                move.b  $D00(a1),d0     ; CIA_B_ICR

loc_5C58:
                btst    #ICR_FLG,$D00(a1) ; CIA_B_ICR
                beq.s   loc_5C58
                move.w  #$9F40,$24(a4)
                move.w  #$9F40,$24(a4)
                move.w  4(a5),d5
                move.w  (a5),d6
                lea     $400(a5),a2
                move.w  #$440,d0
                mulu.w  d5,d0
                adda.w  d0,a2
                movea.l 6(a5),a3
                move.l  #$186A0,d3
                bra.s   loc_5CA2

loc_5C8A:
                subq.l  #1,d3
                beq.s   loc_5CCE
                tst.w   $43E(a2)
                beq.s   loc_5C8A
                bsr.s   MFM_decode
                bmi.s   loc_5CCE
                lea     $440(a2),a2
                lea     $200(a3),a3
                addq.w  #1,d5

loc_5CA2:
                dbf     d6,loc_5C8A

loc_5CA6:
                btst    #1,$1F(a4)
                beq.s   loc_5CA6
                bsr.w   delay_3ms
                move.w  #$4000,$24(a4)
                movem.l (sp)+,d2-d7/a2-a3/a6
                add.w   d6,d3
                addq.w  #1,d4
                mulu.w  #$200,d6
                adda.w  d6,a3
                tst.w   d5
                bne.w   loc_5BB8
                rts

loc_5CCE:
                bsr.w   delay_3ms
                bsr.w   find_track_0_
                dbf     d7,loc_5C1A
                move.w  #$A00,$174(a5)
                move.w  #$7FFF,$96(a4)

loc_5CE6:
                bra.s   loc_5CE6




MFM_decode:
                movem.l d2-d4/a1/a3,-(sp)
                move.l  #$55555555,d3
                lea     $40(a2),a0
                lea     $200(a0),a1
                moveq   #127,d4

loop:
                move.l  (a0)+,d0
                move.l  (a1)+,d1
                and.l   d3,d0
                and.l   d3,d1
                add.l   d0,d0
                or.l    d1,d0
                move.l  d0,(a3)+
                dbf     d4,loop
                moveq   #0,d0
                bra.s   loc_5D14

                moveq   #$FFFFFFFF,d0
loc_5D14:
                movem.l (sp)+,d2-d4/a1/a3
                rts




sub_5D1A:
                move.l  (a0)+,d0
                move.l  (a0)+,d1
                and.l   d3,d0
                and.l   d3,d1
                add.l   d0,d0
                or.l    d1,d0
                rts




find_track_0_:
                bsr.s   find_track_0




step_x_steps_in_y_dir:
                lea     step_out,a2
                move.w  2(a5),d2
                sub.w   (a6),d2
                bpl.s   decrement
                lea     step_in,a2
                neg.w   d2
                bra.s   decrement

step:
                jsr     (a2)

decrement:
                dbf     d2,step
                move.w  2(a5),(a6)
                bra.s   loop


find_track_0:
                bra.s   check_for_track_0

loop:
                bsr.s   step_in
                bsr.s   delay_3ms

check_for_track_0:
                btst    #PRA_TK0,(CIA_A_PRA_0).l
                bne.s   loop
                clr.w   (a6)
                bra.s   loop




step_out:
                moveq   #0,d1
                bra.s   step




step_in:
                moveq   #DIR,d1

step:
                moveq   #SIDE|SEL0|SEL1|SEL2|SEL3,d0
                and.b   $A(a5),d0
                or.b    d1,d0
                move.b  d0,$100(a1)     ; CIA_B_PRB
                nop
                addq.b  #STEP,d0        ; CIA_B_PRB
                move.b  d0,$100(a1)
                bsr.s   delay_3ms

loop:
                btst    #PRA_RDY,(CIA_A_PRA_0).l
                bne.s   loop
                rts




delay_3ms:
                move.b  #$50,$400(a1)   ; CIA_B_TALO
                move.b  #9,$500(a1)     ; CIA_B_TAHI 0x950 = 3ms




start_timer_A_and_wait_for_eqpiration:
                move.b  #START|RUNMODE|LOAD,$E00(a1) ; CIA_B_CRA

loc_5D98:
                btst    #ICR_TA,$D00(a1) ; CIA_B_ICR
                beq.s   loc_5D98
                rts
```