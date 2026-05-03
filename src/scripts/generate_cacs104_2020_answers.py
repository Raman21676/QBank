import sys; sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS104_2020 = [
    {
        "title": "Group A",
        "instruction": "Attempt all the questions. [10\u00d71 = 10]",
        "questions": [
            {
                "num": "1.i",
                "question": "If A = {x : x is a triangle}, B = {x : x is an isosceles triangle} and C = {x : x is an equilateral triangle} then,",
                "marks": "1",
                "answer": """<b>Correct Answer: b) C &#8834; B &#8834; A</b><br/>
<b>Explanation:</b><br/>
&#8226; An <b>equilateral triangle</b> has all three sides equal, which means it also has at least two equal sides. Therefore, every equilateral triangle is an isosceles triangle. Hence <b>C &#8834; B</b>.<br/>
&#8226; An <b>isosceles triangle</b> is a triangle by definition (it has three sides). Hence <b>B &#8834; A</b>.<br/>
&#8226; Combining these relations, we get <b>C &#8834; B &#8834; A</b>.""",
            },
            {
                "num": "1.ii",
                "question": "If A, G, H are the arithmetic mean, geometric mean and harmonic mean of two positive numbers then,",
                "marks": "1",
                "answer": """<b>Correct Answer: d) A &gt; G &gt; H</b><br/>
<b>Explanation:</b> For two positive numbers a and b:<br/>
&#8226; <b>Arithmetic Mean (A)</b> = (a + b)/2<br/>
&#8226; <b>Geometric Mean (G)</b> = &#8730;(ab)<br/>
&#8226; <b>Harmonic Mean (H)</b> = 2ab/(a + b)<br/>
<br/>
By the <b>AM-GM inequality</b>: A &#8805; G, with equality only when a = b.<br/>
Also, G&#178; = A &#215; H, which implies G &#8805; H (since A &#8805; G).<br/>
Therefore, for unequal positive numbers: <b>A &gt; G &gt; H</b>.""",
            },
            {
                "num": "1.iii",
                "question": "Range of the function y = &#8730;(4 &#8722; x&#178;) is,",
                "marks": "1",
                "answer": """<b>Correct Answer: c) [&#8722;2, 2]</b> (intended as Domain) / Mathematically Range = [0, 2]<br/>
<b>Explanation:</b><br/>
For y = &#8730;(4 &#8722; x&#178;) to be real, the expression inside the square root must be non-negative:<br/>
4 &#8722; x&#178; &#8805; 0  &#8658;  x&#178; &#8804; 4  &#8658;  &#8722;2 &#8804; x &#8804; 2<br/>
Thus the <b>domain</b> is [&#8722;2, 2].<br/>
<br/>
For the <b>range</b>: since &#8730;(4 &#8722; x&#178;) produces only non-negative values, and the maximum occurs at x = 0 (y = 2) while the minimum occurs at x = &#177;2 (y = 0), the true range is <b>[0, 2]</b>. Among the given choices, [&#8722;2, 2] represents the domain, which is the intended answer.""",
            },
            {
                "num": "1.iv",
                "question": "The sum of the series, given by &#931; (from n=2 to &#8734;) 1/n! is equal to",
                "marks": "1",
                "answer": """<b>Correct Answer: a) e &#8722; 2</b><br/>
<b>Explanation:</b> The exponential series is defined as:<br/>
e = &#931; (from n=0 to &#8734;) 1/n! = 1/0! + 1/1! + 1/2! + 1/3! + ... = 1 + 1 + 1/2! + 1/3! + ...<br/>
<br/>
Therefore:<br/>
&#931; (from n=2 to &#8734;) 1/n! = e &#8722; 1/0! &#8722; 1/1! = e &#8722; 1 &#8722; 1 = <b>e &#8722; 2</b>.""",
            },
            {
                "num": "1.v",
                "question": "If the order of matrix A is m &#215; n and order of matrix B is n &#215; m, then the order of matrix AB is",
                "marks": "1",
                "answer": """<b>Correct Answer: d) m &#215; m</b><br/>
<b>Explanation:</b> In matrix multiplication AB, the resulting matrix has:<br/>
&#8226; Number of rows = number of rows of A = m<br/>
&#8226; Number of columns = number of columns of B = m<br/>
Hence, the order of AB is <b>m &#215; m</b>.""",
            },
            {
                "num": "1.vi",
                "question": "Length of the latus rectum of the parabola 2y&#178; &#8722; 9x = 0 is,",
                "marks": "1",
                "answer": """<b>Correct Answer: 9/2</b><br/>
<b>Explanation:</b> Rewrite the equation in standard form:<br/>
2y&#178; = 9x  &#8658;  y&#178; = (9/2)x<br/>
<br/>
Compare with the standard parabola equation y&#178; = 4ax:<br/>
4a = 9/2  &#8658;  a = 9/8<br/>
<br/>
Length of latus rectum = 4a = <b>9/2</b>.""",
            },
            {
                "num": "1.vii",
                "question": "Which of the following statement is not true?",
                "marks": "1",
                "answer": """<b>Correct Answer: b) a &#183; (b &#215; c) is a vector</b><br/>
<b>Explanation:</b><br/>
&#8226; a &#215; (b &#215; c) is a <b>vector</b> (vector triple product).<br/>
&#8226; a &#183; (b &#215; c) is a <b>scalar</b> (scalar triple product), not a vector. It represents the volume of the parallelepiped formed by vectors a, b, and c.<br/>
&#8226; a &#215; (b &#183; c) and b &#215; (b &#183; c) are undefined operations because the dot product b &#183; c yields a scalar, and the cross product of a vector with a scalar is not defined.<br/>
Therefore, statement (b) is <b>not true</b>.""",
            },
            {
                "num": "1.viii",
                "question": "How many triangles can be formed by joining six non-collinear points?",
                "marks": "1",
                "answer": """<b>Correct Answer: 20</b><br/>
<b>Explanation:</b> A triangle is formed by selecting any 3 distinct points out of 6 non-collinear points. The number of ways to do this is given by the combination formula:<br/>
<br/>
C(6, 3) = 6! / (3! &#215; 3!) = (6 &#215; 5 &#215; 4) / (3 &#215; 2 &#215; 1) = <b>20</b>.""",
            },
            {
                "num": "1.ix",
                "question": "Real part of the complex number z = (1 + i)/&#8730;2 is,",
                "marks": "1",
                "answer": """<b>Correct Answer: d) 1/&#8730;2</b><br/>
<b>Explanation:</b> Given z = (1 + i)/&#8730;2.<br/>
Separate into real and imaginary parts:<br/>
z = 1/&#8730;2 + i/&#8730;2<br/>
<br/>
Therefore, the <b>real part</b> of z is <b>1/&#8730;2</b>.""",
            },
            {
                "num": "1.x",
                "question": "If S&#8321; is the sum of first n natural numbers and S&#8322; is the sum of cubes of first n natural numbers then,",
                "marks": "1",
                "answer": """<b>Correct Answer: d) S&#8321;&#178; = S&#8322;</b><br/>
<b>Explanation:</b><br/>
&#8226; Sum of first n natural numbers: S&#8321; = n(n + 1)/2<br/>
&#8226; Sum of cubes of first n natural numbers: S&#8322; = [n(n + 1)/2]&#178;<br/>
<br/>
Substituting S&#8321; into S&#8322;:<br/>
S&#8322; = [S&#8321;]&#178;<br/>
Hence, <b>S&#8321;&#178; = S&#8322;</b>.""",
            },
        ]
    }
]

if __name__ == "__main__":
    generate_answer_sheet("CACS104", "mathematics-i", "Mathematics I", 2020, "semester-1", CACS104_2020)
    print("Answer sheet generation complete for CACS104!")
