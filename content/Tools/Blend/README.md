%%title = Blending C Into Assembly
%%image = Blend.jpg

A professionally-edited version of this material can be found in my article [Java Utility for Assembly Programmers in Circuit Cellar Magazine August 2006](http://www.cc-webshop.com/Circuit-Cellar-Issue-193-August-2006-PDF-FI-2006-193.htm).

# Code Poetry

There is a certain charm to writing code in assembly language. Each individual opcode has a purity, a simplistic beauty, that makes an 
assembly program more like poetry than code. And with assembly, you aren't bogged down with a bustling high-level tool chain. All you 
need is a small assembler -- a composer to turn your assembly poetry into a song to play on your processor.

OK, romance aside, assembly remains the most logical choice of programming languages in situations where performance is crucial and/or 
resources are extremely limited. The old Atari 2600 game console from the late 1970's is a good example of such a platform. The system 
has 4K of direct code space and 128 bytes (that's BYTES) of RAM. And your program must count every CPU cycle as it closely follows the 
TV's electron gun. You paint the screen by hand 60 times a second. As we will see in dig, Atari 2600 game programming is very much alive 
and well.

Unfortunately, the features of a high level language like C or Java have spoiled us. Coding an "if" statement, for instance, is much 
easier in C. You use brackets to visually define blocks of code that may or may not get executed based on the outcome of a complex 
expression, and you code the expression in algebraic logic notation you learned in 5th grade. The expression and the code blocks are 
clearly defined and easy to follow when you look back on C code.

In assembly, however, you must litter the code with unique labels to define blocks of code, and you must string together several 
conditional jump statements in just the right order to implement the complex logic expression. Reading through a sequence of jumps 
and labels in a piece of assembly code is a lot like tracing a single strand of spaghetti through a can of Chef Boyardee.

I created the BLEND tool to bridge the gap a bit between C and assembly allowing you to sprinkle C-like program flow constructs 
directly into your assembly. The tool preprocesses your blended C/assembly and produces a pure assembly language file you then 
assemble for your target platform. The tool is written in Java, and it is easily customizable via an XML configuration file to 
support any assembly syntax you desire. The complete Java source code for the tool is available for download in the 
[blend.zip](blend.zip).

In this dig I will introduce you to the blend tool. I will discuss three high-level constructs: "if", "while", and "do-while", and 
show you how the tool translates the C forms into efficient assembly. I will explain the XML input file and how to customize it for 
different processors. Finally, I will show you the tool in action on my Atari 2600 game !DoubleGap written in 6502 assembler with 
high-level program-flow constructs.

# Program Flow Constructs

A program would be very trivial is it flowed from start to finish in a straight line. Real programs jump around from place to place 
based on the result of comparing (subtracting) two numbers as we'll see in the next section. The CPU attempts to flow through your 
program from top to bottom without interruption, but it might change direction for two basic reasons. First, it may decide to skip 
forward over a section of code (the classic "if" construct). Or it may decide to skip backwards to repeat a section of code (loop 
constructs like "do" and "while"). In each case there is a section of code that gets skipped or repeated, and there is a condition 
that controls the skipping or repeating.

High-level languages do a great job of isolating the condition and the code section visually. Below you see the basic layout of three 
Program-flow constructs as they would appear in C (or C++ or Java). In each case the condition code is defined in parenthesis and the 
section of code controlled by the condition is visually indented between curly brackets.

{{{
C Constructs
// C form
if( A==2 ) { ; Expression Code
  ; This is the PASS Code Block
} else {
  ; This is the ELSE Code Block
}

; Assembly form
START:
  ; Insert A==2 Expression Code Here
PASS:
  ; Insert PASS Code Block Here
  JMP OUT
FAIL:
  ; Insert ELSE Code Block Here
OUT:

------------------------------------------------

// C form
do {
  ; This is the PASS Code Block
} while( A==2 ) ; Expression Code

; Assembly form
START:
PASS:
  ; Insert PASS Code Block Here
  ; Insert A==2 Expression Code Here
FAIL:
OUT:

------------------------------------------------

// C form
while( A==2 ) {  ; Expression Code
  ; This is the PASS Code Block
}

; Assembly form
START:
  ; Insert A==2 Expression Code Here
PASS:
  ; Insert PASS Code Block Here
  JMP START
FAIL:
OUT:
}}}

When you write assembly you use these same flow-constructs. The snippets above shows the assembly for each C construct as it might appear in 
your 6502 program. You must use labels to identify the condition and the controlled section, and there isn't a clear visual separation between 
the construct pieces in assembly. You also have to juggle unique labels for every construct in your program. These labels rarely have meaning 
beyond the scope of the flow context, and you end up with labels like "Local_A_1" that you have to keep synchronized in two places: the jump 
statement itself and the jump's destination instruction. These are tedious tasks that the BLEND tool manages for you.

The first thing the tool does is convert the C-like constructs above from the C form to the assembly form. In each case, two labels are created: 
a "PASS" label that the CPU should go to if the tested condition passes, and a "FAIL" label that the CPU should go to if the condition fails. In 
the "if" construct, there are actually two sections of code identified. One section of code is executed if the condition passes and another, 
the "else" section, is executed if the condition fails. The tool inserts a jump statement at the end of the "PASS" section to skip over the "else" 
section.

The "do" loop flows straight into the controlled section of code. The condition is tested at the end of the controlled section. If the condition 
passes, the section is repeated. Otherwise program flow continues after the loop. This loop construct is used when you know that you will make at 
least one pass through the controlled section of code.

The "while" loop tests the condition first. If the condition fails, the controlled section is skipped. Otherwise the controlled section is executed, 
and the tool inserts a jump statement back up to the condition test. This loop construct is used when you aren't sure if you even need to execute the 
control section once

There are two special high-level language keywords that are important inside loop constructs. Often the code inside the loop decides to bypass the 
controlling condition and either "break" out of the loop directly or "continue" immediately back to the top of the loop. The BLEND tool detects these 
two keywords and replaces them with jump statements to the end label or start label respectively.

# Evaluating Expressions

In elementary school you learned to compare two numbers, A and B, and express their relationship as one of three possibilities. Either A is LESS-THAN 
B (A<B), or A is GREATER-THAN B (A>B), or A is EQUAL to B. CPUs are exclusively mathematical, and comparisons are made by subtracting one number (B) 
from the other (A). The CPU sets a group of binary flags based on the results of the subtraction. If the subtraction results in a borrow then the "Carry" 
flag is set (carry and borrow use the same binary flag). If the result is zero, the "Zero" flag is set.

The CPU then makes program-flow changes based on the flags. For instance, it might jump to a new spot if the "Zero" flag is set. Or it might jump to 
another place if the "Carry" flag is cleared. When you are programming in assembly, you have to remember that if the "Zero" flag is set then the two numbers A and B are the same. You must remember that if the "Carry" flag is set then A is less than B. And if neither flag is set then A is greater than B.

More often than not, a condition is really an "expression" ... a set of conditions. For instance, you might want to execute a section of code if "A>10" 
AND if "A<12". As an assembly programmer, you have to chain together two comparisons by hand. Your thinking might go something like this. Subtract 10 
from A. If the carry flag is set, jump to the end because A is less than 10. Otherwise if the zero flag is set, jump to the end because A is equal to 
10 -- not greater than 10. Otherwise subtract 12 from the original A value. If the carry flag is not set, jump to the end because A is not less than 
12. Otherwise the condition passes -- execute the section of code.

Wow! That's a lot of thinking for such a simple expression! Now you are exhausted and you have forgotten all about what you were trying to accomplish 
with the code decision in the first place. Converting an expression to a chain of conditions in assembly is a straightforward, algorithmic process, but 
it is tedious and time consuming. The good news is that the BLEND tool does all this tedious work for you!

The first step is to identify the individual conditions in the expression. Take the expression 
{{{
"(A==2) && (Y!=4 || X<8)"
}}} 
for instance as you might find in a C program. The parenthesis define order of operation. C, Java, and C++ all use the same notation: "&&" means "AND", || 
means "OR", and "!=" means "NOT-EQUAL". In this expression there are three conditions, one comparing A to 2, one comparing Y to 4, and one comparing X to 8. 
Each of these comparisons results in a block of assembly code that performs the subtraction jumps to a PASS destination if the condition passes, or jumps to 
a FAIL destination if the condition fails.

The picture below shows the assembly for the "A==2" condition block on the 6502 processor. Note that there are two possible assembly forms for the block. The 
first form is the one we are thinking of -- the jump-to-PASS-if-EQUAL. The second form is just as valid, but the logic has been flipped 
around -- jump-to-FAIL-if-NOT-EQUAL. Which form to choose depends on what block of code comes next. If the PASS block is next in the code, the tool will pick 
the second form and remove the jump to the very next line. If the FAIL block is next in the code, the tool will pick the first form and remove the wasted jump. 
In fact, the tool will try all possibilities of block order and form and pick the combinations with the fewest lines of code. Try doing that by hand!

{{{HTML
<img src="Blend1.png">
}}}

The picture also shows the expression parsed into a binary tree with the condition blocks on the leaves of operator-nodes. The parenthesis group the expression 
into nested AND and OR operations, each with two conditions -- one on each side of the operator. The AND and OR nodes do not result in any code. They simply link 
the PASS and FAIL labels of the condition blocks in the expression. Program flow enters the top of the tree and comes back out either the PASS or FAIL path 
depending on how the expression evaluated. The AND and OR nodes simply pass the flow down to their child nodes and relay the results back up the tree.

Let's follow the program flow through the expression tree. The top node of the tree is an AND node. Following the blue line into the top of the node, we come to 
the "A==2" code block. If the flow from that block comes back on the FAIL (red) line, the AND node short-circuits the flow back out the FAIL path at the top of 
the tree. Thus if A is not 2, the entire expression fails no matter what the conditions are at the other nodes.

But if A is 2, the flow comes back from the "A==2" block on the PASS (green) line and is shunted into the START (blue) line of the OR node. The OR gate tries 
its children one at a time and passes flow back up through the PASS (green) line if either child nodes return true.

The BLEND tool generates assembly for all three condition terms and uses the expression tree to wire the PASS, FAIL, and START labels together appropriately. 
The output of the top node is wired to the PASS and FAIL labels of the constructs we discussed in the previous section.

Below is the assembly generated by the BLEND tool for an "if" statement containing our complex expression. The top of the listing shows the high-level C flow 
construct. The middle of the listing shows the generated assembly before the tool removes the jumps-to-the-very-next-lines. The bottom of the listing shows the 
final form of the assembly after the tool has removed needless jumps and labels. The tool did pretty good! I couldn't have coded it any better by hand, and the 
process cost me no brain cycles at all.

{{{
if( (A==2)&&(Y!=4 || X<8) ) {
    ; Insert PASS Code Block Here
} else {
    ; Insert ELSE Code Block Here
}

------------------------------------------------

START1:  CMP    #2
         BNE    FAIL   ; Fail
         JMP    START2 ; Pass
<i>START2:</i>  CPY    #4
         BNE    PASS   ; Pass
         JMP    START3 ; Fail
START3:  CPX    #8
         BCC    PASS   ; Pass
         JMP    FAIL   ; Fail
FAIL:    ; Insert ELSE Code Block Here
         JMP    OUT
PASS:    ; Insert PASS Code Block Here
OUT:

------------------------------------------------

START1:  CMP    #2
         BNE    FAIL    
         CPY    #4
         BNE    PASS   
         CPX    #8
         BCC    PASS   
FAIL:    ; Insert ELSE Code Block Here
         JMP    OUT
PASS:    ; Insert PASS Code Block Here
OUT:
}}}

# Processor Configurations

C compilers must know the target processor intimately and are thus processor specific. If you switch processors, you have to go get another compiler to fit the 
new system. The BLEND tool, however, only needs to know a few assembly instructions for your target processor. It reads these instructions from an XML input file 
allowing you to configure this single tool for all your different processor. In fact, you can include all the various processor descriptions in one XML file and 
put the "processor" keyword at the top of your assembly program. The BLEND tool will see "processor 6502", for instance, and load the configuration section for 
the 6502.

The listing below shows a snippet of the configuration for the 6502 processor. The opening tag includes the unconditional jump statement that the tool inserts as 
it generates code. Notice the "@PASS@" in the instruction. The tool replaces this with the destination label. Most of the assembly instructions in the configuration 
file have replaceable content identified by surrounding '@' characters.

{{{
<BlendConfiguration>

  <Processor name="6502" jump="JMP @PASS@">    

      <Compare left="A" code="CMP @RIGHT@"/>
      <Compare left="X" code="CPX @RIGHT@"/>
      <Compare left="Y" code="CPY @RIGHT@"/> 

      <Condition symbol="==">
        <Code>@COMPARE@;BEQ @PASS@;JMP @FAIL@</Code>
        <Code>@COMPARE@;BNE @FAIL@;JMP @PASS@</Code> 
      </Condition> 

      <Condition symbol="<">
        <Code>@COMPARE@;BCC @PASS@;JMP @FAIL@</Code>
        <Code>@COMPARE@;BCS @FAIL@;JMP @PASS@</Code>
      </Condition> 

      <Condition symbol="<=">
        <Code>@COMPARE@;BEQ @PASS@;BCC @PASS@;JMP @FAIL@</Code>
        <Code>@COMPARE@;BEQ @PASS@;BCS @FAIL@;JMP @PASS@</Code>
      </Condition>

      ...

      <Sub key="A=@OPERAND@" code="LDA @OPERAND@"/>       
      <Sub key="@OPERAND@=A" code="STA @OPERAND@"/>
    
  </Processor>

</BlendConfiguration>

----- From the XGS processor section -----  
  
<Condition symbol="<">
  <Code>CJB   @LEFT@, @RIGHT@, @PASS@;JMP @FAIL@</Code>
  <Code>CJAE  @LEFT@, @RIGHT@, @FAIL@;JMP @PASS@</Code>
</Condition>
}}}

Next, the XML describes the various comparison operations. On the 6502, the value on the left of the comparison must be a register A, X, and Y. When the BLEND tool needs 
to make a comparison, it searches this list of instructions and selects the correct one replacing the "@RIGHT@" string with the right hand side of the comparison.

The XML then describes the various comparison operators -- the standard less-than, equal, not-equal, etc. Notice that the "<" sign is a reserved character in XML, and you
 must use the XML entity "<" instead. The XML parser built into Java will automatically replace the entity notation when it reads the file. Semicolons in the text indicate 
 separate lines of assembly, and you can see the PASS and FAIL replacement points in the text. Notice that the XML includes two different forms for each comparison block. The 
 BLEND tool will select the correct form.

Take a look at the last comparison block in the 6502 configuration -- the instructions for less-than-or-equal "<=". The condition requires testing both "Zero" and "Carry" 
at the same time. The 6502 can only test one flag at a time, and the replacement assembly includes two conditional jumps -- one for each flag. Modern processors have a rich 
set of conditional jumps that can test both at the same time. But you shouldn't have to keep up with this information while you are writing code. Simply capture the details 
here in the configuration file and let the BLEND tool keep up with it for you.

If you study the 6502 instructions carefully, you may notice that the "Carry" flag checking appears to be backwards. In fact it is! The 6502 sets the carry flag to 0 if there 
IS a borrow while a 1 means there is NO borrow. Every other processor I've seen does it the other way around. This is just more 6502 information you can code into the XML file 
and let the BLEND tool manage for you.

I have added one of the condition descriptions from the SX52 to the bottom of the listing above. The SX52 is a snazzy little CPU at the heart of 
the [XGameStation](http://www.xgamestation.com/). The processor allows you to compare-and-jump, all in one instruction as shown in the listing. These 
compact instructions make for tight assembly, but they can be confusing when you see them in an assembly listing. The BLEND tool hides the underlying 
code showing you only the easy-to-read C-like constructs.

At the bottom of the 6502 section you see a couple of "Sub" tags. These are direct text substitution templates you can add to make your own "alternate opcodes". 
In this case, the templates turn 6502 loads and stores into C-like assignment operations. You will see how these work in the next section.

# Case Study: DoubleGap 

The listing below shows the BLEND tool in action in a large 6502 program. The listing looks like standard assembly language, but if you scan through the code you will 
see there are no labels whatsoever in the left hand column! You still name your subroutines, but the BLEND tool keeps up with conditional flow labels for you. You 
need never be confused by the clutter of local labels again.

This code is a snippet from a game !DoubleGap I wrote for the Atari 2600. If you are too young to remember, the Atari 2600 was one of the first home gaming consoles 
ever made. The 2600 made a slight nostalgic comeback recently in the form of a all-in-one joystick that connect directly to the. Atari 2600 systems and games are 
popular on eBay if you want to buy back an old friend.

{{{
  LDA  #$02      ; D1 bit ON
  STA   WSYNC    ; Wait for the end of the current line
  STA  VBLANK    ; Turn the electron beam off
  STA   WSYNC    ; Wait for all ...
  STA   WSYNC    ; ... the electrons ...
  STA   WSYNC    ; ... to drain out.  
  STA  VSYNC     ; Trigger the vertical sync signal
  STA   WSYNC    ; Hold the vsync signal for ...
  STA   WSYNC    ; ... three ...
  STA   WSYNC    ; ... scanlines
  STA  HMOVE     ; Move all game objects
  LDA  #$00      ; D1 bit OFF
  STA  VSYNC     ; Release the vertical sync signal
      
  LDA  #43       ; Set timer to 43*64 = 2752 machine ...
  STA  TIM64T    ; ... cycles 2752/(228/3) = 36 scanlines

  LDA  MODE      ; What are we doing between frames?

  if(A==0) {
      JSR  GOMODE      ; Game-over processing
  } else if(A==1) {
      JSR  PLAYMODE    ; Playing-game processing
  } else {
      JSR  SELMODE     ; Selecting-game processing
  }
      
  do {
      LDA  INTIM    ; Wait for the timer to expire
  } while(A!=0);

  STA   WSYNC     ; 37th scanline
  LDA  #$00       ; Turn the ...
  STA  VBLANK     ; ... electron beam back on
}}}

You will find lots of information about Atari 2600 homebrew programming on the web (see the references at the end of this article). There are lots of freeware 
emulators (I use the Z26 emulator) on the web along with demo games, tutorials, and hardware references if you want to try making your own games.

DoubleGap is a very simple game where one or two players move left or right at the bottom of the screen trying to slip through gaps in a wall that scrolls 
down the screen. The wall scrolls faster and faster with each wave. The photo below shows the game running on my Atari 2600 system. Atari cartridges are 
simple critters. You can easily modify an Atari2600 cartridge PCB to use a re-programmable 2732 EPROM. All you have to do is glue on a 7404 inverter and 
reroute a couple of traces using wire-wrap. There are several good Atari 2600 homebrew sites on the web.

You can see the game play on [YouTube](http://www.youtube.com/watch?v=xcmxLo47WdA).

Here is the full code: [Double Gap](/Atari2600/DoubleGap/index.html)

{{{
<img src="photo1.jpg">
}}}

The code above is the section of code that runs at the end of each TV frame (60 times a second). This code signals the TV to carry the electron gun back to 
the top of the screen. It takes a relatively long time to move the gun giving the program plenty of time to process game logic. In my game there are only 
three things that can be happening between screens. Either we are waiting for the user to press start, or we are playing the game, or we are showing a brief 
"Game Over" screen before waiting for start again.

The "if" construct near the middle of the code checks the game mode and calls one of three different functions. The "do" loop at the bottom of the listing 
spins until the timer reaches zero. Then the code moves on to draw the visible TV frame. The code is clean and easy to follow with the high-level constructs sprinkled in.

The listing below shows another part of the game that reads the joystick and sets the motion register for player 1. In this snippet, I used the text 
substitution templates defined in the XML description to make the 6502 load/store instructions look like C assignments. This snippet of code shows one "if" 
statement nested inside another. The pure assembly at the bottom of the listing is the output from the BLEND tool. Which would you find easier to understand? 
I think the C-flavor is more concise and visually defined. It was certainly easier to write.

{{{
  A = SWCHA      ; Joystick switches
  A = A & 0x80   ; Player 0 left switch
  if(A==0) {     ; A==0 if joystick-left
      A = 0xF0   ; Moving-left value
  } else {
      A = SWCHA     ; Joystick
      A = A & 0x40  ; Player 0 right switch
      if(A==0) {    ; A==0 if joystick-right          
          A = 0x10  ; Moving-right value
      } else {
          A = 0     ; Not-moving value
      }
  }
  HMP0 = A    ; New movement value P0

------------------------------------------------

    LDA      SWCHA  ; Joystick switches
    AND      #128   ; Player 0 left switch
    CMP      #0     ; A==0 if joystick-left
    BEQ      FLOW_A_1_OUTPUT_TRUE
    LDA      SWCHA  ; Moving-left value
    AND      #64
    CMP      #0
    BEQ      FLOW_A_2_OUTPUT_TRUE
    LDA      #0
    JMP      FLOW_A_1_OUTPUT_END
FLOW_A_2_OUTPUT_TRUE:
    LDA      #16
    JMP      FLOW_A_1_OUTPUT_END
FLOW_A_1_OUTPUT_TRUE:
    LDA      #240
FLOW_A_1_OUTPUT_END:
    STA      HMP0
}}}

Assembling the code is a two step process. First the BLEND tool converts the C constructs to pure 6502 assembly:

java Blend GAP.ASM GAP_BLENDED.ASM
You then you turn the pure assembly into binary code with an assembler (I use the shareware TASM program). Like this:

tasm -65 --b GAP_BLENDED.ASM GAP.BIN
The resulting GAP.BIN binary can be burned into an EPROM or played in the Z26 emulator like this:

z26 GAP.BIN

# Conclusion 

Rarely does one single language fit all platforms and applications. A high-level language like C makes program flow control easy to write and easy to read 
later, but when you pick a high-level language, your code takes on all of its baggage (size and performance) whether you want it or not. C programmers 
often include assembly snippets in their C programs where speed is of the essence. Now, with the BLEND tool, assembly programmers can insert C snippets 
into their code to manage complex flow control.

As we have seen in this article, turning C flow constructs into assembly is straightforward but tedious. Adding a tool like BLEND to the process allows 
you to focus on the business logic of your program without getting bogged down in conditional jumps and local labels. The BLEND tool is easily configurable 
for your various platforms, and the Java source itself is easily modified for more advanced functionality as you need it.

In the end, there is a pleasing harmony between high-level languages and low -- between development on modern computers to create code for old computers. My 
eyes mist a bit when I see, in code, the friendship between a Java tool and a 6502 assembly program. Programming can be so romantic!
