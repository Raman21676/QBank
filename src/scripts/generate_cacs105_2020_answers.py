import sys; sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS105_2020 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6\u00d75 = 30]",
        "questions": [
            {
                "num": "2",
                "question": "Define digital logic. Explain digital signal with its applications, advantages and disadvantages.",
                "marks": "1 + 4",
                "answer": """<b>Digital Logic:</b> Digital logic is the field of electronics and mathematics that deals with digital circuits and systems operating with discrete binary values (0 and 1, or LOW and HIGH). It forms the foundation of modern computers and digital systems, utilizing logic gates, Boolean algebra, and combinational/sequential circuit design.<br/>
<br/>
<b>Digital Signal:</b> A digital signal is a signal that represents data as a sequence of discrete values. It is discrete in both time and amplitude, typically switching between two voltage levels (e.g., 0V for logic 0 and +5V or +3.3V for logic 1).<br/>
<br/>
<b>Applications of Digital Signals:</b><br/>
&#8226; Computers and microprocessors<br/>
&#8226; Digital communication systems (mobile phones, internet)<br/>
&#8226; Digital audio and video processing<br/>
&#8226; Medical instruments (ECG, MRI, digital thermometers)<br/>
&#8226; Industrial control systems and robotics<br/>
&#8226; Digital measuring instruments<br/>
<br/>
<b>Advantages:</b><br/>
&#8226; <b>Noise Immunity:</b> Digital signals are less affected by noise because only two levels need to be distinguished.<br/>
&#8226; <b>Easy Storage &amp; Processing:</b> Data can be stored, retrieved, and manipulated efficiently using memory and processors.<br/>
&#8226; <b>High Accuracy:</b> Precision depends only on the number of bits used.<br/>
&#8226; <b>Programmability:</b> Digital systems can be reprogrammed for different tasks.<br/>
&#8226; <b>Error Detection &amp; Correction:</b> Techniques like parity checks and Hamming codes can detect and fix errors.<br/>
<br/>
<b>Disadvantages:</b><br/>
&#8226; <b>Quantization Error:</b> Converting analog to digital introduces small errors due to finite resolution.<br/>
&#8226; <b>Bandwidth Requirements:</b> Digital transmission may require more bandwidth than analog for the same information.<br/>
&#8226; <b>System Complexity:</b> Requires ADC/DAC converters to interface with the analog world.<br/>
&#8226; <b>Clock Synchronization:</b> Digital circuits require precise timing and clock signals.""",
            },
            {
                "num": "3",
                "question": "Define positional number system. Calculate following: a) Subtract 21 from 35 using 2's complement method. b) Convert (62.75)&#8321;&#8320; into single precision floating point format.",
                "marks": "1 + 2 + 2",
                "answer": """<b>Positional Number System:</b> A positional number system is a system in which the value of each digit depends on its position relative to the radix point. The position of each digit has a weight that is a power of the base (radix). Common examples include decimal (base 10), binary (base 2), octal (base 8), and hexadecimal (base 16). The general form is:<br/>
Value = &#931; (digit &times; base<sup>position</sup>)<br/>
<br/>
<b>a) Subtract 21 from 35 using 2's complement method:</b><br/>
Step 1: Represent both numbers in binary using sufficient bits (6 bits).<br/>
35&#8321;&#8320; = 100011&#8322;<br/>
21&#8321;&#8320; = 010101&#8322;<br/>
<br/>
Step 2: Find 2's complement of 21.<br/>
1's complement of 010101 = 101010<br/>
Add 1: 101010 + 1 = <b>101011</b> (2's complement)<br/>
<br/>
Step 3: Add 35 and 2's complement of 21.<br/>
<pre>
  100011  (35)
+ 101011  (-21 in 2's comp)
---------
 1001110
</pre>
Discard the end carry (leftmost bit). Result = <b>001110&#8322; = 14&#8321;&#8320;</b>.<br/>
Verification: 35 &#8722; 21 = <b>14</b>.<br/>
<br/>
<b>b) Convert (62.75)&#8321;&#8320; to IEEE 754 Single Precision Floating Point:</b><br/>
Step 1: Convert integer part.<br/>
62 &divide; 2 = 31 remainder 0<br/>
31 &divide; 2 = 15 remainder 1<br/>
15 &divide; 2 = 7 remainder 1<br/>
7 &divide; 2 = 3 remainder 1<br/>
3 &divide; 2 = 1 remainder 1<br/>
1 &divide; 2 = 0 remainder 1<br/>
62&#8321;&#8320; = <b>111110&#8322;</b><br/>
<br/>
Step 2: Convert fractional part.<br/>
0.75 &times; 2 = 1.50 &rarr; 1<br/>
0.50 &times; 2 = 1.00 &rarr; 1<br/>
0.75&#8321;&#8320; = <b>0.11&#8322;</b><br/>
<br/>
So, 62.75&#8321;&#8320; = <b>111110.11&#8322;</b><br/>
<br/>
Step 3: Normalize.<br/>
111110.11 = <b>1.1111011 &times; 2&#8309;</b><br/>
<br/>
Step 4: Determine fields.<br/>
&#8226; <b>Sign bit (S):</b> 0 (positive)<br/>
&#8226; <b>Exponent (E):</b> 5 + 127 = 132 = <b>10000100&#8322;</b><br/>
&#8226; <b>Mantissa (M):</b> 11110110000000000000000 (23 bits, fractional part after leading 1)<br/>
<br/>
Step 5: Final 32-bit representation.<br/>
<pre>
0 10000100 11110110000000000000000
</pre>
Hexadecimal: <b>0x427B0000</b>""",
            },
            {
                "num": "4",
                "question": "Define universal gate. Explain Universal gates with their graphical symbol, algebraic expression, truth table, and Venn diagram.",
                "marks": "1 + 4",
                "answer": """<b>Universal Gate:</b> A universal gate is a logic gate that can be used to implement any Boolean function without requiring any other type of gate. By combining only universal gates, we can construct AND, OR, and NOT operations, and therefore any digital circuit. The two universal gates are <b>NAND</b> and <b>NOR</b>.<br/>
<br/>
<b>1. NAND Gate (NOT-AND):</b><br/>
<b>Graphical Symbol:</b> An AND gate symbol with a small inversion bubble (circle) at the output.<br/>
<b>Algebraic Expression:</b> Y = (A &middot; B)'<br/>
<br/>
<b>Truth Table:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>A</b></td><td><b>B</b></td><td><b>A&middot;B</b></td><td><b>Y = (A&middot;B)'</b></td></tr>
<tr><td>0</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>1</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>0</td></tr>
</table>
<br/>
<b>Venn Diagram Description:</b> Two overlapping circles A and B. The NAND output represents the entire universal set EXCEPT the intersection region (A &#8745; B). The shaded region covers everything outside the intersection.<br/>
<br/>
<b>Implementing Basic Gates with NAND:</b><br/>
&#8226; <b>NOT:</b> Connect both inputs together: Y = (A &middot; A)' = A'<br/>
&#8226; <b>AND:</b> NAND followed by NOT (single-input NAND): Y = ((A&middot;B)')' = A&middot;B<br/>
&#8226; <b>OR:</b> Using De Morgan's theorem: Y = (A' &middot; B')' = A + B<br/>
<br/>
<b>2. NOR Gate (NOT-OR):</b><br/>
<b>Graphical Symbol:</b> An OR gate symbol with a small inversion bubble (circle) at the output.<br/>
<b>Algebraic Expression:</b> Y = (A + B)'<br/>
<br/>
<b>Truth Table:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>A</b></td><td><b>B</b></td><td><b>A+B</b></td><td><b>Y = (A+B)'</b></td></tr>
<tr><td>0</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>0</td></tr>
</table>
<br/>
<b>Venn Diagram Description:</b> Two overlapping circles A and B. The NOR output represents the region outside both circles (complement of A &#8746; B). The shaded region is only the area exterior to both A and B.<br/>
<br/>
<b>Implementing Basic Gates with NOR:</b><br/>
&#8226; <b>NOT:</b> Connect both inputs together: Y = (A + A)' = A'<br/>
&#8226; <b>OR:</b> NOR followed by NOT: Y = ((A+B)')' = A + B<br/>
&#8226; <b>AND:</b> Using De Morgan's theorem: Y = (A' + B')' = A &middot; B""",
            },
            {
                "num": "5",
                "question": "Define decoder. Explain binary to octal converter with block diagram, truth table and logic diagram.",
                "marks": "1 + 4",
                "answer": """<b>Decoder:</b> A decoder is a combinational logic circuit that converts binary information from 'n' input lines to a maximum of 2&#8319; unique output lines. Only one output is active (HIGH) at a time for each input combination. Decoders are used in memory addressing, data demultiplexing, and code conversion.<br/>
<br/>
<b>Binary to Octal Converter (3-to-8 Decoder):</b><br/>
Since octal digits range from 0 to 7 (8 states), a 3-bit binary input is required. A 3-to-8 line decoder performs this conversion.<br/>
<br/>
<b>Block Diagram:</b><br/>
<pre>
       +-------------------+
 A2 ---|                   |--- Y7 (111)
 A1 ---|   3-to-8 Decoder  |--- Y6 (110)
 A0 ---|                   |--- Y5 (101)
       |   (Binary to      |--- Y4 (100)
 E  ---|    Octal)         |--- Y3 (011)
       |                   |--- Y2 (010)
       |                   |--- Y1 (001)
       |                   |--- Y0 (000)
       +-------------------+
</pre>
Inputs: A2, A1, A0 (3-bit binary). Enable: E. Outputs: Y0&#8211;Y7 (active HIGH).<br/>
<br/>
<b>Truth Table:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>E</b></td><td><b>A2</b></td><td><b>A1</b></td><td><b>A0</b></td><td><b>Y7</b></td><td><b>Y6</b></td><td><b>Y5</b></td><td><b>Y4</b></td><td><b>Y3</b></td><td><b>Y2</b></td><td><b>Y1</b></td><td><b>Y0</b></td></tr>
<tr><td>0</td><td>X</td><td>X</td><td>X</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
</table>
<br/>
<b>Logic Diagram:</b> Each output Yi is generated by a 3-input AND gate with appropriate inputs either direct or inverted:<br/>
&#8226; Y0 = E &middot; A2' &middot; A1' &middot; A0'<br/>
&#8226; Y1 = E &middot; A2' &middot; A1' &middot; A0<br/>
&#8226; Y2 = E &middot; A2' &middot; A1 &middot; A0'<br/>
&#8226; Y3 = E &middot; A2' &middot; A1 &middot; A0<br/>
&#8226; Y4 = E &middot; A2 &middot; A1' &middot; A0'<br/>
&#8226; Y5 = E &middot; A2 &middot; A1' &middot; A0<br/>
&#8226; Y6 = E &middot; A2 &middot; A1 &middot; A0'<br/>
&#8226; Y7 = E &middot; A2 &middot; A1 &middot; A0<br/>
<br/>
Each AND gate receives the three address lines; inverters provide the complemented inputs where needed.""",
            },
            {
                "num": "6",
                "question": "Simplify the Boolean function F(w, x, y, z) = &#931;(0, 2, 4, 6, 8, 10, 12, 14) and don't care conditions d(w, x, y, z) = &#931;(1, 3, 9, 11) using K-Map method for both SOP and POS form.",
                "marks": "2.5 + 2.5",
                "answer": """<b>Given:</b><br/>
F(w, x, y, z) = &#931;(0, 2, 4, 6, 8, 10, 12, 14)<br/>
d(w, x, y, z) = &#931;(1, 3, 9, 11)<br/>
<br/>
<b>K-Map for SOP (Sum of Products):</b><br/>
Construct the 4-variable K-map with wx as rows and yz as columns:<br/>
<pre>
      yz
wx   00  01  11  10
00    1   d   d   1
01    1   0   0   1
11    1   0   0   1
10    1   d   d   1
</pre>
(1 = minterm, 0 = maxterm/remaining, d = don't care)<br/>
<br/>
<b>Observation:</b> All minterms (1s) occur where <b>z = 0</b>. The don't cares (d) all have z = 1.<br/>
Grouping all eight 1-cells together: they span all rows (w, x vary) and columns yz = 00 and 10 (y varies, z = 0). The only constant variable is <b>z = 0</b>.<br/>
<br/>
<b>Simplified SOP:</b> <b>F = z'</b><br/>
<br/>
<b>K-Map for POS (Product of Sums):</b><br/>
For POS, we group the 0-cells and treat don't cares as 0s where beneficial. The cells with z = 1 (positions 1, 3, 5, 7, 9, 11, 13, 15) can be grouped as a single block of eight by treating don't cares 1, 3, 9, 11 as zeros.<br/>
<pre>
      yz
wx   00  01  11  10
00    1   d   d   1
01    1   0   0   1
11    1   0   0   1
10    1   d   d   1
</pre>
This entire group has z = 1 for all its cells (w, x, and y vary). Therefore, the resulting sum term contains only z'.<br/>
<br/>
<b>Simplified POS:</b> <b>F = z'</b><br/>
<br/>
(Note: Both SOP and POS reduce to the same simplest expression F = z' because the function depends only on the variable z.)""",
            },
            {
                "num": "7",
                "question": "Define Multiplexer. Explain 4:1 multiplexer with its block diagram, truth table and logic diagram.",
                "marks": "1 + 4",
                "answer": """<b>Multiplexer (MUX):</b> A multiplexer is a combinational circuit that selects one of several input lines and forwards the selected input to a single output line. The selection is controlled by a set of select lines. It is also called a <b>data selector</b>. An N:1 multiplexer has N inputs, log&#8322;N select lines, and 1 output.<br/>
<br/>
<b>4:1 Multiplexer:</b><br/>
A 4:1 MUX has 4 data inputs (I&#8320;, I&#8321;, I&#8322;, I&#8323;), 2 select lines (S&#8321;, S&#8320;), and 1 output (Y).<br/>
<br/>
<b>Block Diagram:</b><br/>
<pre>
         +------------------+
 I0 ---->|                  |
 I1 ---->|     4:1 MUX      |----> Y
 I2 ---->|                  |
 I3 ---->|    S1 S0         |
         |                  |
 S1 ---->|                  |
 S0 ---->|                  |
         +------------------+
</pre>
<br/>
<b>Truth Table:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>S1</b></td><td><b>S0</b></td><td><b>Y</b></td></tr>
<tr><td>0</td><td>0</td><td>I&#8320;</td></tr>
<tr><td>0</td><td>1</td><td>I&#8321;</td></tr>
<tr><td>1</td><td>0</td><td>I&#8322;</td></tr>
<tr><td>1</td><td>1</td><td>I&#8323;</td></tr>
</table>
<br/>
<b>Logic Expression:</b><br/>
Y = S&#8321;'S&#8320;'I&#8320; + S&#8321;'S&#8320;I&#8321; + S&#8321;S&#8320;'I&#8322; + S&#8321;S&#8320;I&#8323;<br/>
<br/>
<b>Logic Diagram:</b><br/>
The circuit consists of:<br/>
&#8226; Four 3-input AND gates: each receives one data input and the appropriate select line combination (direct or inverted).<br/>
&#8226; Two NOT gates to generate S&#8321;' and S&#8320;'.<br/>
&#8226; One 4-input OR gate to combine the outputs of all four AND gates.<br/>
<br/>
<pre>
 I0 ----+----[AND]----+
        |    S1'S0'   |
 I1 ----+----[AND]----+     +-----+
        |    S1'S0    +---->|     |
 I2 ----+----[AND]----+     | OR  |----> Y
        |    S1S0'    +---->|     |
 I3 ----+----[AND]----+     +-----+
             S1S0
</pre>
(NOT gates for S1 and S0 are implied before the AND inputs.)""",
            },
            {
                "num": "8",
                "question": "Write Short Notes on (Any two): a) Parallel Adder b) PLA c) State Diagram",
                "marks": "2.5 + 2.5",
                "answer": """<b>a) Parallel Adder:</b><br/>
A parallel adder is a digital circuit that adds two multi-bit binary numbers simultaneously. Unlike a serial adder which processes one bit at a time, a parallel adder uses multiple full adders connected in cascade (ripple-carry adder) or with carry-lookahead logic.<br/>
<br/>
<b>Ripple-Carry Parallel Adder:</b><br/>
&#8226; For n-bit addition, n full adders (FAs) are required.<br/>
&#8226; The carry-out from one stage becomes the carry-in of the next (more significant) stage.<br/>
&#8226; Advantage: Simple structure.<br/>
&#8226; Disadvantage: Carry propagation delay increases with the number of bits.<br/>
<br/>
<b>4-Bit Parallel Adder Structure:</b><br/>
<pre>
 A3B3 --> FA3 --> S3
   ^C3  |
 A2B2 --> FA2 --> S2
   ^C2  |
 A1B1 --> FA1 --> S1
   ^C1  |
 A0B0 --> FA0 --> S0
        C0=Cin
</pre>
<br/>
<b>b) PLA (Programmable Logic Array):</b><br/>
A PLA is a type of programmable logic device used to implement combinational logic circuits. It consists of a programmable AND array followed by a programmable OR array. Unlike PAL (where only the AND array is programmable), both arrays in a PLA can be programmed.<br/>
<br/>
<b>Structure:</b><br/>
&#8226; <b>Input Buffer:</b> Provides true and complemented inputs.<br/>
&#8226; <b>Programmable AND Array:</b> Generates product terms (minterms) by selecting appropriate inputs.<br/>
&#8226; <b>Programmable OR Array:</b> Combines product terms to form sum-of-products expressions.<br/>
&#8226; <b>Output Stage:</b> May include flip-flops and inverters.<br/>
<br/>
<b>Advantages:</b><br/>
&#8226; High flexibility &#8212; any combinational function can be implemented.<br/>
&#8226; Multiple outputs share the same product terms.<br/>
&#8226; More efficient than ROM for many functions.<br/>
<br/>
<b>c) State Diagram:</b><br/>
A state diagram is a graphical representation of a sequential circuit that shows all possible states, transitions between states, and the inputs/outputs that cause transitions. It is a fundamental tool in the design and analysis of finite state machines (FSMs).<br/>
<br/>
<b>Components:</b><br/>
&#8226; <b>States:</b> Represented by circles (nodes), labeled with state names/values.<br/>
&#8226; <b>Transitions:</b> Directed arrows showing movement from one state to another.<br/>
&#8226; <b>Inputs/Outputs:</b> Labels on arrows (e.g., input/output).<br/>
<br/>
<b>Types:</b><br/>
&#8226; <b>Mealy Machine:</b> Output depends on both current state and input.<br/>
&#8226; <b>Moore Machine:</b> Output depends only on current state.<br/>
<br/>
State diagrams are used in designing counters, sequence detectors, and control units of digital systems.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2\u00d710 = 20]",
        "questions": [
            {
                "num": "9",
                "question": "Explain JK and T Flip-flops with their logic diagram, graphical symbol, characteristic table, characteristic equation and excitation table.",
                "marks": "5 + 5",
                "answer": """<b>1. JK Flip-Flop:</b><br/>
The JK flip-flop is a universal flip-flop that eliminates the indeterminate state of the SR flip-flop. It has two inputs J (set) and K (reset). When J=K=1, the output toggles.<br/>
<br/>
<b>Logic Diagram:</b> A JK flip-flop can be built from an SR flip-flop with feedback from outputs to inputs through AND gates, or using a master-slave configuration.<br/>
<br/>
<b>Graphical Symbol:</b><br/>
<pre>
      +-----+
  J --|     |
      |  JK |-- Q
  K --|     |
      |    Q'|
  CLK-|>    |
      +-----+
</pre>
(The triangle &gt; indicates edge-triggered clock input.)<br/>
<br/>
<b>Characteristic Table:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>J</b></td><td><b>K</b></td><td><b>Q(t)</b></td><td><b>Q(t+1)</b></td><td><b>State</b></td></tr>
<tr><td>0</td><td>0</td><td>0</td><td>0</td><td>No change</td></tr>
<tr><td>0</td><td>0</td><td>1</td><td>1</td><td>No change</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>0</td><td>Reset</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>0</td><td>Reset</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>1</td><td>Set</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>1</td><td>Set</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>1</td><td>Toggle</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>0</td><td>Toggle</td></tr>
</table>
<br/>
<b>Characteristic Equation:</b><br/>
Q(t+1) = J&middot;Q'(t) + K'&middot;Q(t)<br/>
<br/>
<b>Excitation Table:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Q(t) &rarr; Q(t+1)</b></td><td><b>J</b></td><td><b>K</b></td></tr>
<tr><td>0 &rarr; 0</td><td>0</td><td>X</td></tr>
<tr><td>0 &rarr; 1</td><td>1</td><td>X</td></tr>
<tr><td>1 &rarr; 0</td><td>X</td><td>1</td></tr>
<tr><td>1 &rarr; 1</td><td>X</td><td>0</td></tr>
</table>
(X = don't care)<br/>
<br/>
<b>2. T Flip-Flop (Toggle Flip-Flop):</b><br/>
The T flip-flop has a single input T. When T=0, the output remains unchanged; when T=1, the output toggles (complements). It is derived from a JK flip-flop by connecting J and K together.<br/>
<br/>
<b>Graphical Symbol:</b><br/>
<pre>
      +-----+
  T --|     |
      |  T  |-- Q
      |     |
  CLK-|>   Q'|
      +-----+
</pre>
<br/>
<b>Characteristic Table:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>T</b></td><td><b>Q(t)</b></td><td><b>Q(t+1)</b></td><td><b>State</b></td></tr>
<tr><td>0</td><td>0</td><td>0</td><td>No change</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>No change</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>Toggle</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>Toggle</td></tr>
</table>
<br/>
<b>Characteristic Equation:</b><br/>
Q(t+1) = T &oplus; Q(t) = T&middot;Q'(t) + T'&middot;Q(t)<br/>
<br/>
<b>Excitation Table:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Q(t) &rarr; Q(t+1)</b></td><td><b>T</b></td></tr>
<tr><td>0 &rarr; 0</td><td>0</td></tr>
<tr><td>0 &rarr; 1</td><td>1</td></tr>
<tr><td>1 &rarr; 0</td><td>1</td></tr>
<tr><td>1 &rarr; 1</td><td>0</td></tr>
</table>""",
            },
            {
                "num": "10",
                "question": "Differentiate between asynchronous and synchronous sequential circuits with example. Draw a block diagram, truth table and timing diagram to store 1001 in 4-bit SIPO register.",
                "marks": "4 + 6",
                "answer": """<b>Difference between Asynchronous and Synchronous Sequential Circuits:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Aspect</b></td><td><b>Asynchronous Sequential Circuit</b></td><td><b>Synchronous Sequential Circuit</b></td></tr>
<tr><td>Clock</td><td>No common clock; inputs change directly affect outputs after propagation delay</td><td>All flip-flops are triggered by a common clock signal</td></tr>
<tr><td>Speed</td><td>Generally faster (no clock waiting)</td><td>Slower due to clocked operation</td></tr>
<tr><td>Design</td><td>More complex to design; timing analysis is critical</td><td>Easier to design and analyze</td></tr>
<tr><td>States</td><td>Can have transient/hazard states</td><td>State changes occur only at clock edges</td></tr>
<tr><td>Reliability</td><td>More prone to race conditions and glitches</td><td>More reliable and stable</td></tr>
<tr><td>Examples</td><td>SR latch, asynchronous counters</td><td>Flip-flops, synchronous counters, registers</td></tr>
</table>
<br/>
<b>4-bit SIPO (Serial In Parallel Out) Register:</b><br/>
A SIPO register accepts data serially (one bit at a time) and outputs all bits in parallel after all bits have been shifted in.<br/>
<br/>
<b>Block Diagram:</b><br/>
<pre>
Serial        +----+    +----+    +----+    +----+
 Input   CLK->| FF0|--Q0>| FF1|--Q1>| FF2|--Q2>| FF3|--Q3
              |    |     |    |     |    |     |    |
              +----+     +----+     +----+     +----+
                ^          ^          ^          ^
               Q0         Q1         Q2         Q3
             (Parallel Outputs)
</pre>
Four D flip-flops connected in cascade. The same CLK is applied to all flip-flops.<br/>
<br/>
<b>Truth Table for Storing 1001:</b><br/>
The serial input is <b>1 &rarr; 0 &rarr; 0 &rarr; 1</b> (MSB first).<br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Clock Pulse</b></td><td><b>Serial Input</b></td><td><b>Q3</b></td><td><b>Q2</b></td><td><b>Q1</b></td><td><b>Q0</b></td><td><b>State</b></td></tr>
<tr><td>Initial</td><td>-</td><td>0</td><td>0</td><td>0</td><td>0</td><td>Reset</td></tr>
<tr><td>1st &uarr;</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>Shift in 1</td></tr>
<tr><td>2nd &uarr;</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>Shift in 0</td></tr>
<tr><td>3rd &uarr;</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>Shift in 0</td></tr>
<tr><td>4th &uarr;</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>Store 1001</td></tr>
</table>
<br/>
<b>Timing Diagram Description:</b><br/>
<pre>
CLK:  _|___|___|___|___|___
SI:   ____|___|___________|____
Q0:   _______|___________|___ (1, then 0, then 0, then 1)
Q1:   _____________|_______|___ (0, then 1, then 0, then 0)
Q2:   ___________________|___ (0, then 0, then 1, then 0)
Q3:   _________________________|____ (0, then 0, then 0, then 1)
</pre>
After the 4th clock pulse, the parallel output Q3Q2Q1Q0 = <b>1001</b>.""",
            },
            {
                "num": "11",
                "question": "Define counter. Write a procedure to design a counter circuit. Design MOD-8 up counter.",
                "marks": "1 + 2 + 7",
                "answer": """<b>Counter:</b> A counter is a sequential logic circuit that goes through a predetermined sequence of states upon the application of input pulses. Counters are used for counting events, generating timing signals, frequency division, and digital clock circuits. They are classified as asynchronous (ripple) counters and synchronous counters.<br/>
<br/>
<b>Procedure to Design a Counter Circuit:</b><br/>
1. <b>Determine the number of flip-flops (n):</b> For a MOD-N counter, find the smallest n such that 2&#8319; &ge; N.<br/>
2. <b>Draw the state diagram:</b> Show all N states and transitions between them.<br/>
3. <b>Construct the state table:</b> List present states, next states, and required flip-flop inputs.<br/>
4. <b>Choose flip-flop type:</b> Usually JK or T flip-flops.<br/>
5. <b>Determine flip-flop inputs:</b> Use excitation tables to find J, K (or T) inputs for each state transition.<br/>
6. <b>Simplify using K-maps:</b> Derive minimal Boolean expressions for each flip-flop input.<br/>
7. <b>Draw the logic diagram:</b> Connect flip-flops and required gates according to the simplified expressions.<br/>
<br/>
<b>Design of MOD-8 Up Counter:</b><br/>
A MOD-8 counter has 8 states (0 to 7), so it requires <b>n = 3</b> flip-flops (since 2&#179; = 8).<br/>
<br/>
<b>State Diagram:</b><br/>
<pre>
 000 --> 001 --> 010 --> 011 --> 100 --> 101 --> 110 --> 111 --> 000
  (0)     (1)     (2)     (3)     (4)     (5)     (6)     (7)
</pre>
<br/>
<b>State Table (using T flip-flops):</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Present State Q2Q1Q0</b></td><td><b>Next State Q2Q1Q0</b></td><td><b>T2</b></td><td><b>T1</b></td><td><b>T0</b></td></tr>
<tr><td>000</td><td>001</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>001</td><td>010</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td>010</td><td>011</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>011</td><td>100</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>100</td><td>101</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>101</td><td>110</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td>110</td><td>111</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>111</td><td>000</td><td>1</td><td>1</td><td>1</td></tr>
</table>
<br/>
<b>K-Map Simplification:</b><br/>
From the state table and T flip-flop excitation (T = Q &oplus; Q&#8314;, or T=1 when toggle needed):<br/>
&#8226; <b>T0:</b> Toggles every clock cycle &rarr; <b>T0 = 1</b><br/>
&#8226; <b>T1:</b> Toggles when Q0 = 1 &rarr; <b>T1 = Q0</b><br/>
&#8226; <b>T2:</b> Toggles when Q0 = 1 AND Q1 = 1 &rarr; <b>T2 = Q1 &middot; Q0</b><br/>
<br/>
<b>Logic Diagram:</b><br/>
<pre>
        +-------+        +-------+        +-------+
  T2 ---|  T2   |   T1 --|  T1   |   T0 --|  T0   |
  (Q1Q0)|  FF2  |        |  FF1  |        |  FF0  |
        | Q2  Q2'|        | Q1  Q1'|        | Q0  Q0'|
        +---^---+        +---^---+        +---^---+
            |                |                |
           CLK -------------+----------------+
                            |
        Q0 -----------------+-----> T1 input
        Q1 ----+            |
               |            |
               +-->[AND]---> T2 input
                    Q1&middot;Q0
</pre>
<br/>
All three T flip-flops share the same <b>CLK</b> signal (synchronous operation). T0 is permanently connected to logic 1 (Vcc). T1 is connected to Q0. T2 is driven by an AND gate with inputs Q1 and Q0.<br/>
<br/>
<b>Operation:</b> The counter increments by 1 on each clock pulse, cycling through 000 &rarr; 001 &rarr; 010 &rarr; 011 &rarr; 100 &rarr; 101 &rarr; 110 &rarr; 111 &rarr; 000. The output frequency at Q0 is half the clock, at Q1 is one-fourth, and at Q2 is one-eighth of the clock frequency.""",
            },
        ]
    }
]

if __name__ == "__main__":
    generate_answer_sheet("CACS105", "digital-logic", "Digital Logic", 2020, "semester-1", CACS105_2020)
    print("Answer sheet generation complete for CACS105!")
