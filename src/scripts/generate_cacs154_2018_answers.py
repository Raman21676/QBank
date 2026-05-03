#!/usr/bin/env python3
"""Generate answer sheet for CACS154 2018 Mathematics II."""

import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

QUESTIONS_DATA = [
    {
        "title": "Group A",
        "instruction": "Attempt all the questions. [10×1 = 10]",
        "questions": [
            {
                "num": "37",
                "question": "For all rational values of n, lim(x→a) (xⁿ - aⁿ)/(x - a) is equal to",
                "marks": "1",
                "answer": """<b>Correct Answer: a) naⁿ⁻¹</b><br/>
This is a standard limit formula derived from the definition of derivative. Using L'Hôpital's Rule or binomial expansion, we obtain:<br/>
lim(x→a) (xⁿ - aⁿ)/(x - a) = naⁿ⁻¹<br/>
This result is fundamental in calculus and forms the basis for the power rule of differentiation: d/dx(xⁿ) = nxⁿ⁻¹.""",
            },
            {
                "num": "38",
                "question": "If lim(x→x₀⁺) f(x) ≠ lim(x→x₀⁻) f(x), then f(x) is said to be",
                "marks": "1",
                "answer": """<b>Correct Answer: b) An ordinary discontinuity</b><br/>
When the left-hand limit and right-hand limit exist but are not equal, the function has a <b>jump discontinuity</b> (also called ordinary discontinuity or discontinuity of the first kind). The function cannot be made continuous by redefining a single point. If the limits were equal but different from f(x₀), it would be a removable discontinuity.""",
            },
            {
                "num": "39",
                "question": "Derivative of tan⁻¹x is equal to",
                "marks": "1",
                "answer": """<b>Correct Answer: c) 1/(1+x²)</b><br/>
Let y = tan⁻¹x, then tan y = x.<br/>
Differentiating implicitly: sec²y · dy/dx = 1<br/>
Therefore: dy/dx = 1/sec²y = 1/(1 + tan²y) = <b>1/(1 + x²)</b><br/>
This is one of the standard derivatives in calculus, widely used in integration and differential equations.""",
            },
            {
                "num": "40",
                "question": "The value of lim(x→0) (eˣ - 1)/x is equal to",
                "marks": "1",
                "answer": """<b>Correct Answer: b) 1</b><br/>
This is a fundamental exponential limit. Using L'Hôpital's Rule or Taylor series expansion of eˣ:<br/>
eˣ = 1 + x + x²/2! + x³/3! + ...<br/>
So (eˣ - 1)/x = 1 + x/2! + x²/3! + ...<br/>
As x → 0, all terms with x vanish, leaving <b>1</b>.<br/>
This limit is essential for deriving the derivative of eˣ.""",
            },
            {
                "num": "41",
                "question": "The differential equation: y(d²y/dx²)² + 5(dy/dx)² + 2y = 0 is known as",
                "marks": "1",
                "answer": """<b>Correct Answer: d) First order second degree</b><br/>
Wait — correcting based on standard form analysis:<br/>
The highest order derivative is d²y/dx² (second order).<br/>
The highest power of the highest derivative is 2 (since it's squared).<br/>
Therefore, this is a <b>Second order, Second degree</b> differential equation.<br/>
<b>Correct Answer: a) Second degree second order</b><br/>
Order = highest derivative present = 2<br/>
Degree = highest power of the highest derivative = 2""",
            },
            {
                "num": "42",
                "question": "One important condition to satisfy Rolle's Theorem by a function f(x) in [a, b] is",
                "marks": "1",
                "answer": """<b>Correct Answer: c) f(a) = f(b)</b><br/>
<b>Rolle's Theorem</b> states that if a function f(x) satisfies:<br/>
1. f is continuous on the closed interval [a, b]<br/>
2. f is differentiable on the open interval (a, b)<br/>
3. <b>f(a) = f(b)</b><br/>
Then there exists at least one c in (a, b) such that f'(c) = 0.<br/>
The condition f(a) = f(b) is essential for the theorem; without it, the conclusion may fail.""",
            },
            {
                "num": "43",
                "question": "Formula for the composite trapezoidal rule is",
                "marks": "1",
                "answer": """<b>Correct Answer: a) (h/2)[y₀ + 2(y₁+y₂+...+yₙ₋₁) + yₙ]</b><br/>
The <b>Composite Trapezoidal Rule</b> approximates the definite integral by dividing the interval into n subintervals of width h and applying the trapezoid formula to each:<br/>
∫ₐᵇ f(x)dx ≈ (h/2)[y₀ + 2(y₁ + y₂ + ... + yₙ₋₁) + yₙ]<br/>
where h = (b-a)/n and yᵢ = f(xᵢ). The first and last ordinates have coefficient 1, while all intermediate ordinates have coefficient 2. The error is O(h²).""",
            },
            {
                "num": "44",
                "question": "While applying Simpson's 3/8 rule the number of sub-interval should be",
                "marks": "1",
                "answer": """<b>Correct Answer: d) Multiple of 3</b><br/>
<b>Simpson's 3/8 Rule</b> requires that the number of sub-intervals (n) be a <b>multiple of 3</b>. This is because the rule approximates the integral over three sub-intervals at a time using a cubic polynomial. The formula is:<br/>
∫ₐᵇ f(x)dx ≈ (3h/8)[y₀ + 3(y₁+y₂+y₄+y₅+...) + 2(y₃+y₆+...) + yₙ]<br/>
The pattern of coefficients is 1, 3, 3, 2, 3, 3, 2, ..., 1, which requires n to be divisible by 3.""",
            },
            {
                "num": "45",
                "question": "In Gauss Elimination method the given system of simultaneous equation is transformed into",
                "marks": "1",
                "answer": """<b>Correct Answer: d) upper triangular matrix</b><br/>
The <b>Gauss Elimination Method</b> transforms a system of linear equations into an equivalent system represented by an <b>upper triangular matrix</b> through row operations. Once in upper triangular form (where all elements below the main diagonal are zero), the system can be solved efficiently using <b>back substitution</b>, starting from the last equation and working upward.""",
            },
            {
                "num": "46",
                "question": "In Newton-Raphson method, if xₙ is an approximate solution of f(x) = 0 and f'(xₙ) ≠ 0, the next approximation is given by",
                "marks": "1",
                "answer": """<b>Correct Answer: c) xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ)</b><br/>
The <b>Newton-Raphson formula</b> is derived from Taylor series expansion and geometric interpretation (tangent line approximation):<br/>
xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ)<br/>
This iterative method converges quadratically near simple roots. The method requires an initial guess x₀ and that f'(xₙ) ≠ 0 at each iteration. It is one of the most efficient methods for finding roots of nonlinear equations.""",
            },
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5 = 30]",
        "questions": [
            {
                "num": "47",
                "question": "If a function f(x) is defined as: f(x) = 3x² + 2 if x < 1; f(x) = 2x + 3 if x > 1; f(x) = 4 if x = 1. Discuss the continuity of function at x = 1.",
                "marks": "5",
                "answer": """<b>Continuity Analysis at x = 1:</b><br/><br/>

For a function to be continuous at x = a, three conditions must be satisfied:<br/>
1. f(a) must be defined<br/>
2. lim(x→a) f(x) must exist (LHL = RHL)<br/>
3. lim(x→a) f(x) = f(a)<br/><br/>

<b>Step 1: Find f(1)</b><br/>
Given: f(1) = <b>4</b><br/><br/>

<b>Step 2: Find Left Hand Limit (LHL)</b><br/>
lim(x→1⁻) f(x) = lim(x→1⁻) (3x² + 2)<br/>
= 3(1)² + 2 = 3 + 2 = <b>5</b><br/><br/>

<b>Step 3: Find Right Hand Limit (RHL)</b><br/>
lim(x→1⁺) f(x) = lim(x→1⁺) (2x + 3)<br/>
= 2(1) + 3 = 2 + 3 = <b>5</b><br/><br/>

<b>Step 4: Check conditions</b><br/>
• LHL = RHL = 5, so lim(x→1) f(x) = <b>5</b><br/>
• f(1) = 4<br/>
• Since lim(x→1) f(x) = 5 ≠ f(1) = 4<br/><br/>

<b>Conclusion:</b><br/>
The function is <b>discontinuous at x = 1</b>.<br/><br/>

<b>Type of Discontinuity:</b><br/>
Since LHL = RHL ≠ f(1), this is a <b>removable discontinuity</b> (discontinuity of the first kind). If we redefine f(1) = 5, the function would become continuous at x = 1.<br/><br/>

<b>Graphical Interpretation:</b><br/>
The graph approaches y = 5 from both sides of x = 1, but there is a hole at (1, 5) and the actual point is at (1, 4). This single point displacement creates the discontinuity.""",
            },
            {
                "num": "48",
                "question": "Find the derivative of sin³x by using definition.",
                "marks": "5",
                "answer": """<b>Derivative of sin³x using First Principles (Definition):</b><br/><br/>

The definition of derivative is:<br/>
f'(x) = lim(h→0) [f(x+h) - f(x)]/h<br/><br/>

Let f(x) = sin³x<br/><br/>

<b>Step 1:</b> f(x+h) = sin³(x+h)<br/><br/>

<b>Step 2:</b> f(x+h) - f(x) = sin³(x+h) - sin³x<br/><br/>

Using the identity: a³ - b³ = (a-b)(a² + ab + b²)<br/>
= [sin(x+h) - sinx][sin²(x+h) + sin(x+h)sinx + sin²x]<br/><br/>

<b>Step 3:</b> Divide by h:<br/>
[f(x+h) - f(x)]/h = [(sin(x+h) - sinx)/h] · [sin²(x+h) + sin(x+h)sinx + sin²x]<br/><br/>

<b>Step 4:</b> Take limit as h → 0:<br/><br/>

First factor: lim(h→0) [sin(x+h) - sinx]/h<br/>
= lim(h→0) [2cos((2x+h)/2)sin(h/2)]/h<br/>
= lim(h→0) cos(x + h/2) · [sin(h/2)/(h/2)]<br/>
= cos(x) · 1 = <b>cos x</b><br/><br/>

Second factor: lim(h→0) [sin²(x+h) + sin(x+h)sinx + sin²x]<br/>
= sin²x + sinx·sinx + sin²x = <b>3sin²x</b><br/><br/>

<b>Step 5:</b> Multiply the limits:<br/>
f'(x) = cos x · 3sin²x = <b>3sin²x cos x</b><br/><br/>

<b>Verification using Chain Rule:</b><br/>
d/dx(sin³x) = 3sin²x · d/dx(sinx) = 3sin²x cos x ✓<br/><br/>

This confirms our result from first principles.""",
            },
            {
                "num": "13",
                "question": "Using L'Hospital's rule evaluate: lim(x→∞) (2x² + 3x + 5)/(3x² + 2)",
                "marks": "5",
                "answer": """<b>Evaluation using L'Hospital's Rule:</b><br/><br/>

Given: lim(x→∞) (2x² + 3x + 5)/(3x² + 2)<br/><br/>

<b>Step 1: Check the form</b><br/>
As x → ∞:<br/>
Numerator: 2x² + 3x + 5 → ∞<br/>
Denominator: 3x² + 2 → ∞<br/>
This is the <b>∞/∞ indeterminate form</b>, so L'Hospital's Rule applies.<br/><br/>

<b>Step 2: Apply L'Hospital's Rule (first time)</b><br/>
Differentiate numerator and denominator separately:<br/>
d/dx(2x² + 3x + 5) = 4x + 3<br/>
d/dx(3x² + 2) = 6x<br/><br/>
New limit: lim(x→∞) (4x + 3)/(6x)<br/><br/>

<b>Step 3: Check the form again</b><br/>
As x → ∞: (4x + 3)/(6x) → ∞/∞<br/>
Apply L'Hospital's Rule again.<br/><br/>

<b>Step 4: Apply L'Hospital's Rule (second time)</b><br/>
d/dx(4x + 3) = 4<br/>
d/dx(6x) = 6<br/><br/>
New limit: lim(x→∞) 4/6 = <b>2/3</b><br/><br/>

<b>Alternative Method (Direct):</b><br/>
Divide numerator and denominator by x²:<br/>
lim(x→∞) (2 + 3/x + 5/x²)/(3 + 2/x²)<br/>
= (2 + 0 + 0)/(3 + 0) = <b>2/3</b><br/><br/>

<b>Answer: 2/3</b>""",
            },
            {
                "num": "35",
                "question": "If demand function and cost function are given by P(Q) = 1-3Q and C(Q) = Q² – 2Q respectively, where Q is the quantity of the product, then find output of the factor for the maximum profit.",
                "marks": "5",
                "answer": """<b>Finding Output for Maximum Profit:</b><br/><br/>

<b>Given:</b><br/>
Demand function (Price): P(Q) = 1 - 3Q<br/>
Cost function: C(Q) = Q² - 2Q<br/><br/>

<b>Step 1: Find Revenue Function R(Q)</b><br/>
Revenue = Price × Quantity<br/>
R(Q) = P(Q) × Q = (1 - 3Q) × Q = <b>Q - 3Q²</b><br/><br/>

<b>Step 2: Find Profit Function π(Q)</b><br/>
Profit = Revenue - Cost<br/>
π(Q) = R(Q) - C(Q)<br/>
= (Q - 3Q²) - (Q² - 2Q)<br/>
= Q - 3Q² - Q² + 2Q<br/>
= <b>3Q - 4Q²</b><br/><br/>

<b>Step 3: Find Critical Points</b><br/>
For maximum profit, dπ/dQ = 0<br/>
dπ/dQ = 3 - 8Q = 0<br/>
8Q = 3<br/>
Q = <b>3/8 = 0.375</b><br/><br/>

<b>Step 4: Verify Maximum</b><br/>
d²π/dQ² = -8 < 0<br/>
Since the second derivative is negative, the profit is indeed <b>maximum</b> at Q = 3/8.<br/><br/>

<b>Step 5: Calculate Maximum Profit</b><br/>
π(3/8) = 3(3/8) - 4(3/8)²<br/>
= 9/8 - 4(9/64)<br/>
= 9/8 - 36/64<br/>
= 9/8 - 9/16<br/>
= 18/16 - 9/16<br/>
= <b>9/16 = 0.5625</b><br/><br/>

<b>Answer:</b> The output for maximum profit is <b>Q = 3/8 = 0.375 units</b>, and the maximum profit is <b>9/16 = Rs. 0.5625</b>.""",
            },
            {
                "num": "36",
                "question": "Evaluate: a) ∫ sin⁻¹x dx  b) ∫₀¹ (x² + 5) dx",
                "marks": "5",
                "answer": """<b>a) Evaluation of ∫ sin⁻¹x dx</b><br/><br/>

Using integration by parts: ∫ u dv = uv - ∫ v du<br/><br/>
Let u = sin⁻¹x, dv = dx<br/>
Then du = dx/√(1-x²), v = x<br/><br/>

∫ sin⁻¹x dx = x sin⁻¹x - ∫ x/√(1-x²) dx<br/><br/>

For the second integral, let t = 1 - x², then dt = -2x dx, so x dx = -dt/2<br/>
∫ x/√(1-x²) dx = ∫ (-1/2) t⁻¹/² dt = -1/2 · 2t¹/² = -√t = -√(1-x²)<br/><br/>

Therefore:<br/>
∫ sin⁻¹x dx = x sin⁻¹x - (-√(1-x²)) + C<br/>
= <b>x sin⁻¹x + √(1-x²) + C</b><br/><br/>

---<br/><br/>

<b>b) Evaluation of ∫₀¹ (x² + 5) dx</b><br/><br/>

∫₀¹ (x² + 5) dx = [x³/3 + 5x]₀¹<br/>
= (1³/3 + 5·1) - (0³/3 + 5·0)<br/>
= (1/3 + 5) - 0<br/>
= 1/3 + 15/3<br/>
= <b>16/3 ≈ 5.333</b><br/><br/>

<b>Answers:</b><br/>
a) <b>x sin⁻¹x + √(1-x²) + C</b><br/>
b) <b>16/3</b>""",
            },
            {
                "num": "37",
                "question": "Solve: dy/dx = (x + y)/(x - y)",
                "marks": "5",
                "answer": """<b>Solving the Differential Equation dy/dx = (x + y)/(x - y)</b><br/><br/>

This is a <b>homogeneous differential equation</b> because both numerator and denominator are homogeneous functions of degree 1.<br/><br/>

<b>Step 1: Substitution</b><br/>
Let y = vx, then dy/dx = v + x(dv/dx)<br/><br/>

<b>Step 2: Substitute into the equation</b><br/>
v + x(dv/dx) = (x + vx)/(x - vx)<br/>
v + x(dv/dx) = x(1 + v)/[x(1 - v)]<br/>
v + x(dv/dx) = (1 + v)/(1 - v)<br/><br/>

<b>Step 3: Separate variables</b><br/>
x(dv/dx) = (1 + v)/(1 - v) - v<br/>
= (1 + v - v + v²)/(1 - v)<br/>
= (1 + v²)/(1 - v)<br/><br/>

(1 - v)/(1 + v²) dv = dx/x<br/><br/>

<b>Step 4: Integrate both sides</b><br/>
∫ (1 - v)/(1 + v²) dv = ∫ dx/x<br/><br/>

Split the left side:<br/>
∫ 1/(1 + v²) dv - ∫ v/(1 + v²) dv = ln|x| + C<br/><br/>

First integral: tan⁻¹v<br/>
Second integral: Let t = 1 + v², dt = 2v dv<br/>
∫ v/(1 + v²) dv = (1/2)ln(1 + v²)<br/><br/>

So:<br/>
tan⁻¹v - (1/2)ln(1 + v²) = ln|x| + C<br/><br/>

<b>Step 5: Substitute back v = y/x</b><br/>
tan⁻¹(y/x) - (1/2)ln(1 + y²/x²) = ln|x| + C<br/><br/>
Simplify the logarithm:<br/>
(1/2)ln(1 + y²/x²) = (1/2)ln[(x² + y²)/x²] = (1/2)[ln(x² + y²) - 2ln|x|] = (1/2)ln(x² + y²) - ln|x|<br/><br/>

Substituting:<br/>
tan⁻¹(y/x) - (1/2)ln(x² + y²) + ln|x| = ln|x| + C<br/><br/>

Cancel ln|x| from both sides:<br/>
<b>tan⁻¹(y/x) - (1/2)ln(x² + y²) = C</b><br/><br/>

Or equivalently:<br/>
<b>2tan⁻¹(y/x) - ln(x² + y²) = C₁</b><br/><br/>

This is the general solution of the given differential equation.""",
            },
            {
                "num": "38",
                "question": "Examine the consistency of the system of equation and solve if possible. 3x₁ + 2x₂ + x₃ = 3; 2x₁ + x₂ + x₃ = 3; 3x₁ + 3x₂ + 2x₃ = 2",
                "marks": "5",
                "answer": """<b>Consistency Analysis and Solution:</b><br/><br/>

Given system:<br/>
3x₁ + 2x₂ + x₃ = 3  ...(1)<br/>
2x₁ + x₂ + x₃ = 3  ...(2)<br/>
3x₁ + 3x₂ + 2x₃ = 2  ...(3)<br/><br/>

<b>Step 1: Form the augmented matrix [A|B]</b><br/>
<table border='1' cellpadding='4'>
<tr><td>3</td><td>2</td><td>1</td><td>|</td><td>3</td></tr>
<tr><td>2</td><td>1</td><td>1</td><td>|</td><td>3</td></tr>
<tr><td>3</td><td>3</td><td>2</td><td>|</td><td>2</td></tr>
</table><br/><br/>

<b>Step 2: Apply row operations</b><br/><br/>

R₂ → R₂ - (2/3)R₁:<br/>
<table border='1' cellpadding='4'>
<tr><td>3</td><td>2</td><td>1</td><td>|</td><td>3</td></tr>
<tr><td>0</td><td>-1/3</td><td>1/3</td><td>|</td><td>1</td></tr>
<tr><td>3</td><td>3</td><td>2</td><td>|</td><td>2</td></tr>
</table><br/><br/>

R₃ → R₃ - R₁:<br/>
<table border='1' cellpadding='4'>
<tr><td>3</td><td>2</td><td>1</td><td>|</td><td>3</td></tr>
<tr><td>0</td><td>-1/3</td><td>1/3</td><td>|</td><td>1</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>|</td><td>-1</td></tr>
</table><br/><br/>

R₂ → -3R₂:<br/>
<table border='1' cellpadding='4'>
<tr><td>3</td><td>2</td><td>1</td><td>|</td><td>3</td></tr>
<tr><td>0</td><td>1</td><td>-1</td><td>|</td><td>-3</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>|</td><td>-1</td></tr>
</table><br/><br/>

R₃ → R₃ - R₂:<br/>
<table border='1' cellpadding='4'>
<tr><td>3</td><td>2</td><td>1</td><td>|</td><td>3</td></tr>
<tr><td>0</td><td>1</td><td>-1</td><td>|</td><td>-3</td></tr>
<tr><td>0</td><td>0</td><td>2</td><td>|</td><td>2</td></tr>
</table><br/><br/>

<b>Step 3: Back substitution</b><br/><br/>
From row 3: 2x₃ = 2, so <b>x₃ = 1</b><br/><br/>

From row 2: x₂ - x₃ = -3<br/>
x₂ - 1 = -3<br/>
<b>x₂ = -2</b><br/><br/>

From row 1: 3x₁ + 2x₂ + x₃ = 3<br/>
3x₁ + 2(-2) + 1 = 3<br/>
3x₁ - 4 + 1 = 3<br/>
3x₁ = 6<br/>
<b>x₁ = 2</b><br/><br/>

<b>Step 4: Consistency Check</b><br/>
Rank of A = 3<br/>
Rank of [A|B] = 3<br/>
Number of unknowns = 3<br/>
Since Rank(A) = Rank([A|B]) = 3, the system is <b>consistent</b> and has a <b>unique solution</b>.<br/><br/>

<b>Verification:</b><br/>
Eq (1): 3(2) + 2(-2) + 1 = 6 - 4 + 1 = 3 ✓<br/>
Eq (2): 2(2) + (-2) + 1 = 4 - 2 + 1 = 3 ✓<br/>
Eq (3): 3(2) + 3(-2) + 2(1) = 6 - 6 + 2 = 2 ✓<br/><br/>

<b>Answer: x₁ = 2, x₂ = -2, x₃ = 1</b>""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10 = 20]",
        "questions": [
            {
                "num": "39",
                "question": "Define Homogeneous equation and solve the following system of equations using Inverse Matrix Method: -2x + 2y + z = -4; -8x + 7y - 4z = -47; 9x - 8y + 5z = 55",
                "marks": "10",
                "answer": """<b>Part 1: Definition of Homogeneous Equation</b><br/><br/>

A <b>system of linear equations</b> is called <b>homogeneous</b> if all the constant terms are zero. In matrix form, AX = O, where A is the coefficient matrix, X is the column vector of variables, and O is the zero vector.<br/><br/>

For example:<br/>
2x + 3y - z = 0<br/>
x - y + 2z = 0<br/>
3x + y - z = 0<br/><br/>

<b>Properties of Homogeneous Systems:</b><br/>
• Always consistent (at least the trivial solution x = y = z = 0 exists)<br/>
• If |A| ≠ 0: only trivial solution (unique solution)<br/>
• If |A| = 0: infinitely many solutions (non-trivial solutions exist)<br/><br/>

---<br/><br/>

<b>Part 2: Solution using Inverse Matrix Method</b><br/><br/>

Given system:<br/>
-2x + 2y + z = -4<br/>
-8x + 7y - 4z = -47<br/>
9x - 8y + 5z = 55<br/><br/>

<b>Step 1: Write in matrix form AX = B</b><br/>
A = [[-2, 2, 1], [-8, 7, -4], [9, -8, 5]]<br/>
X = [x, y, z]ᵀ<br/>
B = [-4, -47, 55]ᵀ<br/><br/>

<b>Step 2: Find |A| (determinant of A)</b><br/>
|A| = -2(35 - 32) - 2(-40 + 36) + 1(64 - 63)<br/>
= -2(3) - 2(-4) + 1(1)<br/>
= -6 + 8 + 1<br/>
= <b>3</b><br/><br/>

Since |A| = 3 ≠ 0, A⁻¹ exists and the system has a unique solution.<br/><br/>

<b>Step 3: Find the Adjoint of A</b><br/><br/>

Cofactor matrix C:<br/>
C₁₁ = +(35-32) = 3, C₁₂ = -(-40+36) = 4, C₁₃ = +(64-63) = 1<br/>
C₂₁ = -(10+8) = -18, C₂₂ = +(-10-9) = -19, C₂₃ = -(-16-18) = 34<br/>
Wait, recalculating carefully:<br/><br/>

C₁₁ = +(7·5 - (-4)(-8)) = 35 - 32 = 3<br/>
C₁₂ = -((-8)·5 - (-4)·9) = -(-40 + 36) = 4<br/>
C₁₃ = +((-8)(-8) - 7·9) = 64 - 63 = 1<br/><br/>

C₂₁ = -(2·5 - 1·(-8)) = -(10 + 8) = -18<br/>
C₂₂ = +((-2)·5 - 1·9) = -10 - 9 = -19<br/>
C₂₃ = -((-2)(-8) - 2·9) = -(16 - 18) = 2<br/><br/>

C₃₁ = +(2·(-4) - 1·7) = -8 - 7 = -15<br/>
C₃₂ = -((-2)(-4) - 1·(-8)) = -(8 + 8) = -16<br/>
C₃₃ = +((-2)·7 - 2·(-8)) = -14 + 16 = 2<br/><br/>

Cofactor matrix:<br/>
[[3, 4, 1], [-18, -19, 2], [-15, -16, 2]]<br/><br/>

Adj(A) = Cᵀ =<br/>
[[3, -18, -15], [4, -19, -16], [1, 2, 2]]<br/><br/>

<b>Step 4: Find A⁻¹</b><br/>
A⁻¹ = Adj(A)/|A| = (1/3) · [[3, -18, -15], [4, -19, -16], [1, 2, 2]]<br/><br/>

<b>Step 5: Find X = A⁻¹B</b><br/><br/>
[x]   (1/3) [3  -18  -15] [-4 ]<br/>
[y] =       [4  -19  -16] [-47]<br/>
[z]         [1   2    2 ] [ 55]<br/><br/>

x = (1/3)[3(-4) + (-18)(-47) + (-15)(55)]<br/>
= (1/3)[-12 + 846 - 825]<br/>
= (1/3)[9]<br/>
= <b>3</b><br/><br/>

y = (1/3)[4(-4) + (-19)(-47) + (-16)(55)]<br/>
= (1/3)[-16 + 893 - 880]<br/>
= (1/3)[-3]<br/>
= <b>-1</b><br/><br/>

z = (1/3)[1(-4) + 2(-47) + 2(55)]<br/>
= (1/3)[-4 - 94 + 110]<br/>
= (1/3)[12]<br/>
= <b>4</b><br/><br/>

<b>Verification:</b><br/>
Eq 1: -2(3) + 2(-1) + 4 = -6 - 2 + 4 = -4 ✓<br/>
Eq 2: -8(3) + 7(-1) - 4(4) = -24 - 7 - 16 = -47 ✓<br/>
Eq 3: 9(3) - 8(-1) + 5(4) = 27 + 8 + 20 = 55 ✓<br/><br/>

<b>Answer: x = 3, y = -1, z = 4</b>""",
            },
            {
                "num": "40",
                "question": "State Rolle's Theorem and interpret it geometrically. Verify Rolle's theorem for f(x) = x² - 4 in -3 ≤ x ≤ 3",
                "marks": "10",
                "answer": """<b>Part 1: Statement of Rolle's Theorem</b><br/><br/>

<b>Rolle's Theorem:</b> If a function f(x) satisfies the following three conditions:<br/>
1. f is <b>continuous</b> on the closed interval [a, b]<br/>
2. f is <b>differentiable</b> on the open interval (a, b)<br/>
3. <b>f(a) = f(b)</b><br/>

Then there exists at least one real number <b>c ∈ (a, b)</b> such that <b>f'(c) = 0</b>.<br/><br/>

<b>Geometrical Interpretation:</b><br/>
If a curve y = f(x) is continuous between points A(a, f(a)) and B(b, f(b)), has a unique tangent at every point between A and B, and f(a) = f(b) (i.e., A and B are at the same height), then there exists at least one point C(c, f(c)) between A and B where the tangent to the curve is <b>parallel to the x-axis</b> (horizontal).<br/><br/>

In other words, somewhere between two points at the same height on a smooth curve, there must be at least one "peak" or "valley" where the slope is zero.<br/><br/>

---<br/><br/>

<b>Part 2: Verification for f(x) = x² - 4 in [-3, 3]</b><br/><br/>

<b>Step 1: Check continuity</b><br/>
f(x) = x² - 4 is a polynomial function. All polynomial functions are continuous everywhere.<br/>
Therefore, f is continuous on [-3, 3]. <b>✓ Condition 1 satisfied.</b><br/><br/>

<b>Step 2: Check differentiability</b><br/>
f'(x) = 2x exists for all real x.<br/>
Therefore, f is differentiable on (-3, 3). <b>✓ Condition 2 satisfied.</b><br/><br/>

<b>Step 3: Check f(a) = f(b)</b><br/>
f(-3) = (-3)² - 4 = 9 - 4 = 5<br/>
f(3) = (3)² - 4 = 9 - 4 = 5<br/>
Therefore, <b>f(-3) = f(3) = 5</b>. <b>✓ Condition 3 satisfied.</b><br/><br/>

<b>Step 4: Find c such that f'(c) = 0</b><br/>
f'(x) = 2x<br/>
Set f'(c) = 0:<br/>
2c = 0<br/>
c = <b>0</b><br/><br/>

<b>Step 5: Verify c ∈ (-3, 3)</b><br/>
c = 0 lies in the open interval (-3, 3). <b>✓</b><br/><br/>

<b>Step 6: Verify f'(0) = 0</b><br/>
f'(0) = 2(0) = <b>0</b> <b>✓</b><br/><br/>

<b>Conclusion:</b><br/>
Since all three conditions of Rolle's Theorem are satisfied and we found c = 0 ∈ (-3, 3) such that f'(0) = 0, <b>Rolle's Theorem is verified</b> for f(x) = x² - 4 on [-3, 3].<br/><br/>

<b>Geometrical Meaning:</b><br/>
The parabola y = x² - 4 has vertex at (0, -4). At x = 0, the tangent is horizontal (parallel to x-axis). Points (-3, 5) and (3, 5) are at the same height, and the curve smoothly descends to its minimum at (0, -4) before rising again, confirming that a horizontal tangent exists between them.""",
            },
            {
                "num": "20",
                "question": "Using Composite Trapezoidal Rule, compute ∫₀² 1/(1+x²) dx with four intervals. Find the absolute error of approximation from its actual value.",
                "marks": "10",
                "answer": """<b>Solution using Composite Trapezoidal Rule</b><br/><br/>

<b>Given:</b><br/>
∫₀² 1/(1+x²) dx, n = 4 intervals<br/><br/>

<b>Step 1: Calculate h</b><br/>
h = (b - a)/n = (2 - 0)/4 = <b>0.5</b><br/><br/>

<b>Step 2: Calculate function values</b><br/>
<table border='1' cellpadding='4'>
<tr><td>i</td><td>xᵢ</td><td>yᵢ = 1/(1+xᵢ²)</td></tr>
<tr><td>0</td><td>0.0</td><td>1.0000</td></tr>
<tr><td>1</td><td>0.5</td><td>0.8000</td></tr>
<tr><td>2</td><td>1.0</td><td>0.5000</td></tr>
<tr><td>3</td><td>1.5</td><td>0.3077</td></tr>
<tr><td>4</td><td>2.0</td><td>0.2000</td></tr>
</table><br/><br/>

<b>Step 3: Apply Composite Trapezoidal Rule</b><br/>
∫₀² f(x)dx ≈ (h/2)[y₀ + 2(y₁ + y₂ + y₃) + y₄]<br/>
= (0.5/2)[1.0000 + 2(0.8000 + 0.5000 + 0.3077) + 0.2000]<br/>
= 0.25[1.0000 + 2(1.6077) + 0.2000]<br/>
= 0.25[1.0000 + 3.2154 + 0.2000]<br/>
= 0.25[4.4154]<br/>
= <b>1.10385 ≈ 1.1039</b><br/><br/>

<b>Step 4: Find Actual Value</b><br/>
∫ 1/(1+x²) dx = tan⁻¹x<br/>
Actual value = [tan⁻¹x]₀² = tan⁻¹(2) - tan⁻¹(0)<br/>
= 1.1071487... - 0<br/>
= <b>1.1071</b> (approx)<br/><br/>

<b>Step 5: Calculate Absolute Error</b><br/>
Absolute Error = |Actual Value - Approximate Value|<br/>
= |1.1071 - 1.1039|<br/>
= <b>0.0032</b> (or more precisely, 0.0033)<br/><br/>

Using more precise values:<br/>
Actual = tan⁻¹(2) ≈ 1.1071487177940904<br/>
Approximate = 1.1038461538461537<br/>
Absolute Error ≈ <b>0.00330256</b><br/><br/>

<b>Percentage Error:</b><br/>
(0.0033/1.1071) × 100 ≈ <b>0.30%</b><br/><br/>

<b>Conclusion:</b><br/>
The Composite Trapezoidal Rule with n = 4 gives a good approximation (1.1039) with a small absolute error of approximately 0.0033. The error can be further reduced by increasing the number of intervals.""",
            },
        ]
    }
]

if __name__ == "__main__":
    generate_answer_sheet(
        subject_code="CACS154",
        subject_slug="mathematics-ii",
        subject_name="Mathematics II",
        year=2018,
        semester_slug="semester-2",
        questions_data=QUESTIONS_DATA
    )
    print("Answer sheet generation complete for CACS154 2018!")
