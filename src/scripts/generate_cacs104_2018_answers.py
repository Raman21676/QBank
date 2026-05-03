#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS104_2018 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6 × 5 = 30]",
        "questions": [
            {
                "num": "11",
                "question": "32 students play basketball and 25 students play volleyball. It is found that 20 students play both the games. Find the number of students playing at least one game. Also, find total number of students if 13 students play none of these games.",
                "marks": "5",
                "answer": """<b>Solution:</b><br/>
Let B = set of basketball players, V = set of volleyball players.<br/>
Given: n(B) = 32, n(V) = 25, n(B ∩ V) = 20<br/><br/>
<b>Students playing at least one game:</b><br/>
n(B ∪ V) = n(B) + n(V) − n(B ∩ V)<br/>
n(B ∪ V) = 32 + 25 − 20 = <b>37 students</b><br/><br/>
<b>Total number of students:</b><br/>
Total = n(B ∪ V) + students playing none<br/>
Total = 37 + 13 = <b>50 students</b>"""
            },
            {
                "num": "12",
                "question": "Let f : N → N be defined by f(x) = 2x for all x ∈ N where N is the set of natural numbers. Show that f is one-one but not onto function.",
                "marks": "5",
                "answer": """<b>Solution:</b><br/>
Given: f(x) = 2x, where f : N → N<br/><br/>
<b>To prove f is one-one (injective):</b><br/>
Let f(x₁) = f(x₂)<br/>
Then 2x₁ = 2x₂<br/>
Therefore x₁ = x₂<br/>
Hence, f is one-one.<br/><br/>
<b>To prove f is not onto (surjective):</b><br/>
For f to be onto, every element in the codomain N must have a pre-image in the domain.<br/>
Consider y = 3 ∈ N (codomain).<br/>
If f(x) = 3, then 2x = 3, so x = 1.5 ∉ N.<br/>
Since 3 has no pre-image in N, f is <b>not onto</b>.<br/><br/>
Therefore, f is one-one but not onto."""
            },
            {
                "num": "13",
                "question": "If the three consecutive terms of a geometric series be increased by their middle term, then prove that the resulting terms will be in harmonic progression (H.P.).",
                "marks": "5",
                "answer": """<b>Proof:</b><br/>
Let the three consecutive terms of a G.P. be a/r, a, and ar.<br/><br/>
When each term is increased by the middle term a, the new terms are:<br/>
• First term: a/r + a = a(1 + r)/r<br/>
• Second term: a + a = 2a<br/>
• Third term: ar + a = a(r + 1)<br/><br/>
For these to be in H.P., their reciprocals must be in A.P.<br/>
Reciprocals:<br/>
• 1/[a(1+r)/r] = r/[a(1+r)]<br/>
• 1/(2a)<br/>
• 1/[a(1+r)]<br/><br/>
Check if they are in A.P.:<br/>
2 × [1/(2a)] = 1/a<br/>
r/[a(1+r)] + 1/[a(1+r)] = (r+1)/[a(1+r)] = 1/a<br/><br/>
Since 2 × (second reciprocal) = first + third, the reciprocals are in A.P.<br/>
Therefore, the resulting terms are in <b>Harmonic Progression</b>."""
            },
            {
                "num": "14",
                "question": "Find the adjoint of the matrix:<br/>A = [[1, 2, -2], [2, 2, 1], [0, 3, -1]]",
                "marks": "5",
                "answer": """<b>Solution:</b><br/>
Given matrix A = [[1, 2, -2], [2, 2, 1], [0, 3, -1]]<br/><br/>
<b>Step 1: Find the cofactor matrix.</b><br/>
C₁₁ = +(2×(-1) − 1×3) = −5<br/>
C₁₂ = −(2×(−1) − 1×0) = 2<br/>
C₁₃ = +(2×3 − 2×0) = 6<br/>
C₂₁ = −(2×(−1) − (−2)×3) = −4<br/>
C₂₂ = +(1×(−1) − (−2)×0) = −1<br/>
C₂₃ = −(1×3 − 2×0) = −3<br/>
C₃₁ = +(2×1 − (−2)×2) = 6<br/>
C₃₂ = −(1×1 − (−2)×2) = −5<br/>
C₃₃ = +(1×2 − 2×2) = −2<br/><br/>
Cofactor matrix = [[−5, 2, 6], [−4, −1, −3], [6, −5, −2]]<br/><br/>
<b>Step 2: Take the transpose to get the adjoint.</b><br/>
adj(A) = [[−5, −4, 6], [2, −1, −5], [6, −3, −2]]"""
            },
            {
                "num": "15",
                "question": "Prove that:<br/>|1  1  1|<br/>|x  y  z| = (x−y)(y−z)(z−x)<br/>|x² y² z²|",
                "marks": "5",
                "answer": """<b>Proof:</b><br/>
Let Δ = |1  1  1|<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|x  y  z|<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|x² y² z²|<br/><br/>
Apply C₂ → C₂ − C₁ and C₃ → C₃ − C₁:<br/>
Δ = |1  0  0|<br/>
&nbsp;&nbsp;&nbsp;&nbsp;|x y−x z−x|<br/>
&nbsp;&nbsp;&nbsp;&nbsp;|x² y²−x² z²−x²|<br/><br/>
Expand along R₁:<br/>
Δ = 1 × [(y−x)(z²−x²) − (z−x)(y²−x²)]<br/>
Δ = (y−x)(z−x)(z+x) − (z−x)(y−x)(y+x)<br/>
Δ = (y−x)(z−x)[(z+x) − (y+x)]<br/>
Δ = (y−x)(z−x)(z−y)<br/>
Δ = (x−y)(y−z)(z−x)<br/><br/>
Hence proved."""
            },
            {
                "num": "16",
                "question": "Find the equation of parabola with focus (−1, 2) and directrix x = 5.",
                "marks": "5",
                "answer": """<b>Solution:</b><br/>
Given: Focus S = (−1, 2), Directrix: x = 5<br/><br/>
Let P(x, y) be any point on the parabola.<br/>
By definition, SP = PM (distance from focus = perpendicular distance from directrix)<br/><br/>
SP² = (x + 1)² + (y − 2)²<br/>
PM = |x − 5|<br/>
PM² = (x − 5)²<br/><br/>
Since SP² = PM²:<br/>
(x + 1)² + (y − 2)² = (x − 5)²<br/>
x² + 2x + 1 + y² − 4y + 4 = x² − 10x + 25<br/>
2x + 1 + y² − 4y + 4 = −10x + 25<br/>
12x + y² − 4y − 20 = 0<br/><br/>
<b>Equation of parabola:</b> y² − 4y + 12x − 20 = 0<br/>
or (y − 2)² = −12(x − 2)"""
            },
            {
                "num": "17",
                "question": "Transform u = [[−1, 3], [2, 1]] and v = [[0, 1], [−1, 0]] and check whether this transformation is linear.",
                "marks": "5",
                "answer": """<b>Solution:</b><br/>
Given: u = [[−1, 3], [2, 1]] and v = [[0, 1], [−1, 0]]<br/><br/>
Wait, the question seems unclear. If the transformation is defined by T(x) = ux + v, then:<br/><br/>
<b>Check for linearity:</b><br/>
A transformation T is linear if:<br/>
1. T(x + y) = T(x) + T(y)<br/>
2. T(cx) = cT(x)<br/><br/>
If T(x) = ux + v where v ≠ 0, then:<br/>
T(0) = u(0) + v = v ≠ 0<br/><br/>
Since T(0) ≠ 0, the transformation is <b>not linear</b>.<br/><br/>
For a transformation to be linear, it must satisfy T(0) = 0. The presence of the translation vector v makes this an affine transformation, not a linear transformation."""
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2 × 10 = 20]",
        "questions": [
            {
                "num": "18",
                "question": "Define permutation and combination. Try to establish relationship between them with the help of formulae. In how many ways can the letters of the word 'LOGIC' be arranged so that i) Vowels may occupy odd position? ii) No vowels are together?",
                "marks": "10",
                "answer": """<b>Permutation:</b> An arrangement of objects in a specific order. The number of permutations of n objects taken r at a time is:<br/>
P(n, r) = n!/(n−r)!<br/><br/>
<b>Combination:</b> A selection of objects without regard to order. The number of combinations of n objects taken r at a time is:<br/>
C(n, r) = n!/[r!(n−r)!]<br/><br/>
<b>Relationship:</b> P(n, r) = C(n, r) × r!<br/><br/>
<b>Word 'LOGIC':</b><br/>
Letters: L, O, G, I, C (5 letters, vowels: O, I; consonants: L, G, C)<br/><br/>
<b>i) Vowels in odd positions:</b><br/>
Odd positions: 1, 3, 5 (3 positions)<br/>
Even positions: 2, 4 (2 positions)<br/>
Arrange 2 vowels in 3 odd positions: P(3, 2) = 3!/(3−2)! = 6 ways<br/>
Arrange 3 consonants in 3 remaining positions: 3! = 6 ways<br/>
Total ways = 6 × 6 = <b>36 ways</b><br/><br/>
<b>ii) No vowels together:</b><br/>
First arrange 3 consonants: 3! = 6 ways<br/>
This creates 4 gaps: _C_C_C_<br/>
Choose 2 gaps from 4 for vowels: C(4, 2) = 6<br/>
Arrange 2 vowels in these 2 gaps: 2! = 2<br/>
Total ways = 6 × 6 × 2 = <b>72 ways</b>"""
            },
            {
                "num": "19",
                "question": "Define scalar and vector product in three dimensional space with their geometrical interpretation and prove the formula sin(A + B) = sinAcosB + cosAsinB by using vector method.",
                "marks": "10",
                "answer": """<b>Scalar Product (Dot Product):</b><br/>
For vectors a⃗ and b⃗, a⃗ · b⃗ = |a⃗||b⃗|cos θ<br/>
<b>Geometrical interpretation:</b> The scalar product gives the product of the magnitude of one vector and the projection of the other vector onto it.<br/><br/>
<b>Vector Product (Cross Product):</b><br/>
For vectors a⃗ and b⃗, a⃗ × b⃗ = |a⃗||b⃗|sin θ n̂<br/>
where n̂ is the unit vector perpendicular to both a⃗ and b⃗.<br/>
<b>Geometrical interpretation:</b> The magnitude of the cross product equals the area of the parallelogram formed by the two vectors.<br/><br/>
<b>Proof of sin(A+B) = sinAcosB + cosAsinB:</b><br/>
Consider unit vectors in the XY-plane:<br/>
a⃗ = cosA î + sinA ĵ (making angle A with X-axis)<br/>
b⃗ = cosB î − sinB ĵ (making angle −B with X-axis)<br/><br/>
The angle between a⃗ and b⃗ is (A + B).<br/>
|a⃗ × b⃗| = |a⃗||b⃗|sin(A+B) = sin(A+B) ... (i)<br/><br/>
Also, a⃗ × b⃗ = (cosA î + sinA ĵ) × (cosB î − sinB ĵ)<br/>
= −cosAsinB(î×ĵ) + sinAcosB(ĵ×î)<br/>
= −cosAsinB(k̂) + sinAcosB(−k̂)<br/>
Wait, let me recalculate:<br/>
a⃗ × b⃗ = cosA(−sinB)(î×ĵ) + sinA(cosB)(ĵ×î)<br/>
= −cosAsinB(k̂) + sinAcosB(−k̂)<br/>
= −(cosAsinB + sinAcosB)k̂<br/><br/>
Taking magnitude: |a⃗ × b⃗| = cosAsinB + sinAcosB ... (ii)<br/><br/>
From (i) and (ii):<br/>
sin(A+B) = sinAcosB + cosAsinB<br/>
Hence proved."""
            },
            {
                "num": "20",
                "question": "Define the logarithmic function, state its properties and if f(x) = log[(1+x)/(1−x)] for −1 < x < 1, show that f(a) + f(b) = f[(a+b)/(1+ab)].",
                "marks": "10",
                "answer": """<b>Logarithmic Function:</b><br/>
The logarithmic function f(x) = logₐ(x) is the inverse of the exponential function. It is defined for x > 0 and a > 0, a ≠ 1.<br/><br/>
<b>Properties:</b><br/>
1. logₐ(mn) = logₐm + logₐn<br/>
2. logₐ(m/n) = logₐm − logₐn<br/>
3. logₐ(mⁿ) = n·logₐm<br/>
4. logₐ1 = 0<br/>
5. logₐa = 1<br/>
6. a^(logₐx) = x<br/><br/>
<b>Proof:</b><br/>
Given: f(x) = log[(1+x)/(1−x)]<br/><br/>
LHS = f(a) + f(b)<br/>
= log[(1+a)/(1−a)] + log[(1+b)/(1−b)]<br/>
= log[(1+a)(1+b)/((1−a)(1−b))]<br/>
= log[(1 + a + b + ab)/(1 − a − b + ab)]<br/><br/>
RHS = f[(a+b)/(1+ab)]<br/>
= log[(1 + (a+b)/(1+ab))/(1 − (a+b)/(1+ab))]<br/>
= log[((1+ab+a+b)/(1+ab))/((1+ab−a−b)/(1+ab))]<br/>
= log[(1 + a + b + ab)/(1 − a − b + ab)]<br/><br/>
Since LHS = RHS,<br/>
f(a) + f(b) = f[(a+b)/(1+ab)]<br/>
Hence proved."""
            },
        ]
    }
]

print("Generating CACS104 2018 answer sheet...")
generate_answer_sheet("CACS104", "mathematics-i", "Mathematics I", 2018, "semester-1", CACS104_2018)
print("✅ CACS104 2018 done!")
