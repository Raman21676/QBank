#!/usr/bin/env python3
"""Generate answer sheet for CACS252 Numerical Methods 2019."""

import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS252_2019 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "Why are errors important to a computational scientist? Differentiate between inherent error and round-off error.",
                "marks": "5",
                "answer": """<b>Importance of Errors in Computational Science:</b><br/>
Errors are crucial because computational scientists rely on numerical approximations to model real-world phenomena. Understanding errors helps in:<br/>
• Assessing the <b>accuracy and reliability</b> of computed results.<br/>
• Choosing appropriate <b>algorithms and step sizes</b> to keep errors within acceptable bounds.<br/>
• Avoiding <b>catastrophic cancellation</b> or accumulation of round-off errors in iterative methods.<br/>
• Validating simulation outcomes against experimental data.<br/><br/>
<b>Difference between Inherent Error and Round-off Error:</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Aspect</b></td><td><b>Inherent Error</b></td><td><b>Round-off Error</b></td></tr>
<tr><td>Source</td><td>Present in the original data or mathematical model due to measurement limitations or approximations.</td><td>Arises because computers represent numbers with finite precision (fixed number of bits).</td></tr>
<tr><td>Control</td><td>Cannot be eliminated; can only be reduced by improving data accuracy.</td><td>Can be reduced by using higher precision (double instead of float) or better algorithms.</td></tr>
<tr><td>Example</td><td>Measuring length as 10.2 cm when true value is 10.245 cm.</td><td>Representing 1/3 as 0.333333 in a 6-digit computer.</td></tr>
<tr><td>Nature</td><td>Input/data-related error.</td><td>Machine/computation-related error.</td></tr>
</table>""",
            },
            {
                "num": "3",
                "question": "Solve the equation x² - 4x - 10 = 0 using bisection method where root lies between 5 and 6.",
                "marks": "5",
                "answer": """<b>Bisection Method:</b><br/>
Given: f(x) = x² - 4x - 10<br/>
Root lies between a = 5 and b = 6.<br/><br/>
<b>Check:</b> f(5) = 25 - 20 - 10 = <b>-5</b> (negative)<br/>
f(6) = 36 - 24 - 10 = <b>+2</b> (positive)<br/>
Since f(a) × f(b) < 0, root exists in [5, 6].<br/><br/>
<b>Iterations:</b><br/>
<table border='1' cellpadding='4'>
<tr><td>Iteration</td><td>a</td><td>b</td><td>c=(a+b)/2</td><td>f(c)</td><td>Sign</td></tr>
<tr><td>1</td><td>5.0</td><td>6.0</td><td>5.5</td><td>-1.75</td><td>Negative → a = c</td></tr>
<tr><td>2</td><td>5.5</td><td>6.0</td><td>5.75</td><td>0.0625</td><td>Positive → b = c</td></tr>
<tr><td>3</td><td>5.5</td><td>5.75</td><td>5.625</td><td>-0.859</td><td>Negative → a = c</td></tr>
<tr><td>4</td><td>5.625</td><td>5.75</td><td>5.6875</td><td>-0.402</td><td>Negative → a = c</td></tr>
<tr><td>5</td><td>5.6875</td><td>5.75</td><td>5.71875</td><td>-0.170</td><td>Negative → a = c</td></tr>
</table><br/>
After 5 iterations, root ≈ <b>5.72</b><br/><br/>
<b>Exact Root:</b> Using quadratic formula:<br/>
x = (4 ± √(16 + 40)) / 2 = (4 ± √56) / 2 = (4 ± 7.483) / 2<br/>
x = 5.7417 or x = -1.7417<br/>
The positive root is <b>5.7417</b>, confirming our approximation converges correctly.""",
            },
            {
                "num": "4",
                "question": "Find f(3.5) using second order Lagrange interpolation polynomial using the data points (2, 2), (3, 6), (4, 12).",
                "marks": "5",
                "answer": """<b>Lagrange Interpolation Formula (2nd Order):</b><br/>
Given points: (x₀,y₀)=(2,2), (x₁,y₁)=(3,6), (x₂,y₂)=(4,12)<br/><br/>
P(x) = y₀ × L₀(x) + y₁ × L₁(x) + y₂ × L₂(x)<br/><br/>
Where:<br/>
L₀(x) = (x-x₁)(x-x₂) / ((x₀-x₁)(x₀-x₂))<br/>
L₁(x) = (x-x₀)(x-x₂) / ((x₁-x₀)(x₁-x₂))<br/>
L₂(x) = (x-x₀)(x-x₁) / ((x₂-x₀)(x₂-x₁))<br/><br/>
<b>For x = 3.5:</b><br/><br/>
L₀(3.5) = (3.5-3)(3.5-4) / ((2-3)(2-4)) = (0.5)(-0.5) / ((-1)(-2)) = -0.25 / 2 = <b>-0.125</b><br/><br/>
L₁(3.5) = (3.5-2)(3.5-4) / ((3-2)(3-4)) = (1.5)(-0.5) / ((1)(-1)) = -0.75 / -1 = <b>0.75</b><br/><br/>
L₂(3.5) = (3.5-2)(3.5-3) / ((4-2)(4-3)) = (1.5)(0.5) / ((2)(1)) = 0.75 / 2 = <b>0.375</b><br/><br/>
P(3.5) = 2(-0.125) + 6(0.75) + 12(0.375)<br/>
= -0.25 + 4.5 + 4.5<br/>
= <b>8.75</b><br/><br/>
<b>Therefore, f(3.5) ≈ 8.75</b>""",
            },
            {
                "num": "5",
                "question": "Evaluate the integral using Trapezoidal Rule.",
                "marks": "5",
                "answer": """<b>Note:</b> The specific function was not fully visible in the original paper. A common exam example is:<br/>
Evaluate ∫₀¹ x² dx using Trapezoidal rule with n = 4.<br/><br/>
<b>Solution:</b><br/>
h = (b - a) / n = (1 - 0) / 4 = <b>0.25</b><br/><br/>
<table border='1' cellpadding='4'>
<tr><td>x</td><td>0</td><td>0.25</td><td>0.50</td><td>0.75</td><td>1.00</td></tr>
<tr><td>y = x²</td><td>0</td><td>0.0625</td><td>0.25</td><td>0.5625</td><td>1</td></tr>
</table><br/>
Using Trapezoidal Rule:<br/>
∫ y dx ≈ (h/2) [y₀ + 2(y₁ + y₂ + y₃) + y₄]<br/>
= (0.25/2) [0 + 2(0.0625 + 0.25 + 0.5625) + 1]<br/>
= 0.125 [0 + 2(0.875) + 1]<br/>
= 0.125 [0 + 1.75 + 1]<br/>
= 0.125 × 2.75<br/>
= <b>0.34375</b><br/><br/>
<b>Exact value:</b> ∫₀¹ x² dx = [x³/3]₀¹ = 1/3 ≈ 0.3333<br/>
<b>Error:</b> 0.34375 - 0.3333 = <b>0.0104</b><br/><br/>
<b>Trapezoidal Rule Formula:</b><br/>
∫ₐᵇ f(x)dx ≈ (h/2)[y₀ + 2(y₁+y₂+...+yₙ₋₁) + yₙ] where h = (b-a)/n""",
            },
            {
                "num": "6",
                "question": "Solve the system of linear equations using Gauss-Jordan Method.",
                "marks": "5",
                "answer": """<b>Note:</b> The specific equations were not fully visible. Using a standard example:<br/>
2x + y - z = 8<br/>
-3x - y + 2z = -11<br/>
-2x + y + 2z = -3<br/><br/>
<b>Gauss-Jordan Method:</b><br/>
We form the augmented matrix and reduce it to reduced row echelon form.<br/><br/>
<b>Augmented Matrix [A|B]:</b><br/>
<table border='1' cellpadding='4'>
<tr><td>2</td><td>1</td><td>-1</td><td>8</td></tr>
<tr><td>-3</td><td>-1</td><td>2</td><td>-11</td></tr>
<tr><td>-2</td><td>1</td><td>2</td><td>-3</td></tr>
</table><br/>
<b>Step 1:</b> R1 → R1/2<br/>
<table border='1' cellpadding='4'>
<tr><td>1</td><td>0.5</td><td>-0.5</td><td>4</td></tr>
<tr><td>-3</td><td>-1</td><td>2</td><td>-11</td></tr>
<tr><td>-2</td><td>1</td><td>2</td><td>-3</td></tr>
</table><br/>
<b>Step 2:</b> R2 → R2 + 3R1, R3 → R3 + 2R1<br/>
<table border='1' cellpadding='4'>
<tr><td>1</td><td>0.5</td><td>-0.5</td><td>4</td></tr>
<tr><td>0</td><td>0.5</td><td>0.5</td><td>1</td></tr>
<tr><td>0</td><td>2</td><td>1</td><td>5</td></tr>
</table><br/>
<b>Step 3:</b> R2 → R2 × 2<br/>
<table border='1' cellpadding='4'>
<tr><td>1</td><td>0.5</td><td>-0.5</td><td>4</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>2</td></tr>
<tr><td>0</td><td>2</td><td>1</td><td>5</td></tr>
</table><br/>
<b>Step 4:</b> R1 → R1 - 0.5R2, R3 → R3 - 2R2<br/>
<table border='1' cellpadding='4'>
<tr><td>1</td><td>0</td><td>-1</td><td>3</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>2</td></tr>
<tr><td>0</td><td>0</td><td>-1</td><td>1</td></tr>
</table><br/>
<b>Step 5:</b> R3 → -R3<br/>
<table border='1' cellpadding='4'>
<tr><td>1</td><td>0</td><td>-1</td><td>3</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>2</td></tr>
<tr><td>0</td><td>0</td><td>1</td><td>-1</td></tr>
</table><br/>
<b>Step 6:</b> R1 → R1 + R3, R2 → R2 - R3<br/>
<table border='1' cellpadding='4'>
<tr><td>1</td><td>0</td><td>0</td><td>2</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>3</td></tr>
<tr><td>0</td><td>0</td><td>1</td><td>-1</td></tr>
</table><br/>
<b>Solution:</b> x = <b>2</b>, y = <b>3</b>, z = <b>-1</b>""",
            },
            {
                "num": "7",
                "question": "Find y(0.2) when y'(x) = x + y² with y(0) = 0 and h = 0.2 using Euler's method.",
                "marks": "5",
                "answer": """<b>Euler's Method:</b> yₙ₊₁ = yₙ + h × f(xₙ, yₙ)<br/><br/>
Given: f(x,y) = x + y², y(0) = 0, h = 0.2<br/>
Find y(0.2).<br/><br/>
<b>Step 1: x₀ = 0, y₀ = 0</b><br/>
f(x₀, y₀) = 0 + 0² = 0<br/>
y₁ = y₀ + h × f(x₀, y₀) = 0 + 0.2 × 0 = <b>0</b><br/><br/>
Therefore, <b>y(0.2) ≈ 0</b><br/><br/>
<b>Note:</b> Since the initial slope is zero and y₀ = 0, the first Euler step yields zero. For better accuracy, smaller step sizes or modified Euler (Heun's) method can be used.<br/><br/>
<b>Additional Step (for verification):</b><br/>
<b>Step 2: x₁ = 0.2, y₁ = 0</b><br/>
f(x₁, y₁) = 0.2 + 0² = 0.2<br/>
y₂ = 0 + 0.2 × 0.2 = <b>0.04</b><br/>
So y(0.4) ≈ 0.04""",
            },
            {
                "num": "8",
                "question": "Solve the Laplace equation in the square domain 0 < x < 3 and 0 < y < 3 with f = 0.",
                "marks": "5",
                "answer": """<b>Laplace Equation:</b> ∇²u = ∂²u/∂x² + ∂²u/∂y² = 0<br/><br/>
Domain: 0 < x < 3, 0 < y < 3 with h = 1 (assuming standard grid spacing).<br/><br/>
<b>Finite Difference Approximation:</b><br/>
Using the standard five-point formula:<br/>
u<sub>i+1,j</sub> + u<sub>i-1,j</sub> + u<sub>i,j+1</sub> + u<sub>i,j-1</sub> - 4u<sub>i,j</sub> = 0<br/><br/>
<b>Grid Points:</b><br/>
Interior points: (1,1), (2,1), (1,2), (2,2)<br/>
Boundary points: all edges where u is specified by boundary conditions.<br/><br/>
<b>Note:</b> The original question did not specify boundary values. If we assume <b>zero boundary conditions</b> (u = 0 on all boundaries), then by the maximum principle for harmonic functions, the only solution is:<br/><br/>
<b>u = 0 everywhere in the domain.</b><br/><br/>
This is because the Laplace equation with zero Dirichlet boundary conditions has the trivial solution.<br/><br/>
<b>For non-zero boundary conditions</b> (typical exam case), one would:<br/>
1. Set up equations for each interior point using the five-point formula.<br/>
2. Substitute known boundary values.<br/>
3. Solve the resulting system of linear equations (usually by iteration: Jacobi, Gauss-Seidel, or SOR).<br/><br/>
<b>Example with assumed boundary values:</b><br/>
u(0,y) = 0, u(3,y) = y, u(x,0) = 0, u(x,3) = x<br/><br/>
At (1,1): 4u₁₁ = u₂₁ + u₀₁ + u₁₂ + u₁₀ = u₂₁ + 0 + u₁₂ + 0<br/>
At (2,1): 4u₂₁ = u₃₁ + u₁₁ + u₂₂ + u₂₀ = 1 + u₁₁ + u₂₂ + 0<br/>
At (1,2): 4u₁₂ = u₂₂ + u₀₂ + u₁₃ + u₁₁ = u₂₂ + 0 + 1 + u₁₁<br/>
At (2,2): 4u₂₂ = u₃₂ + u₁₂ + u₂₃ + u₂₁ = 2 + u₁₂ + 2 + u₂₁<br/><br/>
Solving gives u₁₁ ≈ 0.25, u₂₁ ≈ 0.5, u₁₂ ≈ 0.5, u₂₂ ≈ 1.0 (approximate).<br/><br/>
<b>Conclusion:</b> The solution depends on boundary conditions; with zero boundaries, u = 0.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "Derive Newton-Raphson formula and solve an equation.",
                "marks": "10",
                "answer": """<b>Derivation of Newton-Raphson Formula:</b><br/>
Let x₀ be an initial approximation to the root r of f(x) = 0.<br/>
Let h be a small correction such that r = x₀ + h.<br/>
Using Taylor expansion about x₀:<br/>
f(x₀ + h) ≈ f(x₀) + h f'(x₀) = 0<br/>
h = -f(x₀) / f'(x₀)<br/>
Thus, the next approximation is:<br/><br/>
<b>xₙ₊₁ = xₙ - f(xₙ) / f'(xₙ)</b><br/><br/>
This is the Newton-Raphson iteration formula. It has quadratic convergence (order 2) when near the root.<br/><br/>
<b>Example:</b> Find root of f(x) = x³ - 2x - 5 = 0, starting with x₀ = 2.<br/>
f'(x) = 3x² - 2<br/><br/>
<b>Iteration 1:</b><br/>
f(2) = 8 - 4 - 5 = -1<br/>
f'(2) = 12 - 2 = 10<br/>
x₁ = 2 - (-1)/10 = 2 + 0.1 = <b>2.1</b><br/><br/>
<b>Iteration 2:</b><br/>
f(2.1) = 9.261 - 4.2 - 5 = 0.061<br/>
f'(2.1) = 13.23 - 2 = 11.23<br/>
x₂ = 2.1 - 0.061/11.23 = 2.1 - 0.00543 = <b>2.09457</b><br/><br/>
<b>Iteration 3:</b><br/>
f(2.09457) ≈ 0.00015<br/>
x₃ ≈ 2.09457 - 0.00015/f'(2.09457) ≈ <b>2.09455</b><br/><br/>
<b>Root ≈ 2.0946</b> (correct to 4 decimal places).<br/><br/>
<b>Geometric Interpretation:</b> The method approximates the curve by its tangent at xₙ and finds where the tangent crosses the x-axis.""",
            },
            {
                "num": "10",
                "question": "Explain Gaussian elimination with partial pivoting.",
                "marks": "10",
                "answer": """<b>Gaussian Elimination with Partial Pivoting:</b><br/>
Gaussian elimination transforms a system of linear equations into an upper triangular matrix, which is then solved by back substitution. <b>Partial pivoting</b> is used to improve numerical stability by reducing round-off errors.<br/><br/>
<b>Steps:</b><br/>
<b>1. Forward Elimination:</b><br/>
For each column k (pivot column):<br/>
• Find the row with the largest absolute value in column k at or below the diagonal.<br/>
• Swap this row with row k (partial pivoting).<br/>
• Eliminate all entries below the pivot using row operations: Rᵢ → Rᵢ - (aᵢₖ/aₖₖ) × Rₖ<br/><br/>
<b>2. Back Substitution:</b><br/>
Solve for variables starting from the last row upwards.<br/><br/>
<b>Example:</b><br/>
0.001x + 2y = 2<br/>
x + y = 2<br/><br/>
<b>Without pivoting:</b><br/>
Multiplier m = 1/0.001 = 1000<br/>
New R2: y - 2000y = 2 - 2000 → -1999y = -1998 → y ≈ 1<br/>
x = (2 - 2)/0.001 = 0 (inaccurate due to catastrophic cancellation)<br/><br/>
<b>With partial pivoting:</b><br/>
Swap R1 and R2 (since |1| > |0.001|):<br/>
x + y = 2<br/>
0.001x + 2y = 2<br/><br/>
Multiplier m = 0.001/1 = 0.001<br/>
New R2: 2y - 0.001y = 2 - 0.002 → 1.999y = 1.998 → y = <b>1</b><br/>
x = 2 - 1 = <b>1</b><br/><br/>
<b>Exact solution:</b> x = 1, y = 1. Partial pivoting prevents loss of significance.<br/><br/>
<b>Why Partial Pivoting is Important:</b><br/>
• Prevents division by very small numbers (which amplifies round-off errors).<br/>
• Ensures multipliers |m| ≤ 1, keeping errors bounded.<br/>
• Essential for ill-conditioned systems.""",
            },
            {
                "num": "11",
                "question": "Derive Simpson's 1/3 rule and apply it.",
                "marks": "10",
                "answer": """<b>Derivation of Simpson's 1/3 Rule:</b><br/>
We approximate f(x) by a second-degree polynomial (parabola) passing through three equally spaced points: (x₀,y₀), (x₁,y₁), (x₂,y₂).<br/><br/>
Using Newton's forward difference interpolation and integrating between x₀ and x₂ (where x₂ = x₀ + 2h):<br/><br/>
∫<sub>x₀</sub><sup>x₂</sup> f(x)dx ≈ (h/3)[y₀ + 4y₁ + y₂]<br/><br/>
For n subintervals (n must be even):<br/><br/>
<b>∫ₐᵇ f(x)dx ≈ (h/3)[y₀ + 4(y₁+y₃+...+yₙ₋₁) + 2(y₂+y₄+...+yₙ₋₂) + yₙ]</b><br/><br/>
where h = (b - a)/n.<br/><br/>
<b>Error Term:</b> E = -(b-a)h⁴f⁽⁴⁾(ξ)/180, showing it is exact for polynomials up to degree 3.<br/><br/>
<b>Application:</b> Evaluate ∫₀¹ dx/(1+x²) with n = 4.<br/><br/>
h = (1-0)/4 = 0.25<br/><br/>
<table border='1' cellpadding='4'>
<tr><td>x</td><td>0</td><td>0.25</td><td>0.50</td><td>0.75</td><td>1.00</td></tr>
<tr><td>y=1/(1+x²)</td><td>1.0000</td><td>0.9412</td><td>0.8000</td><td>0.6400</td><td>0.5000</td></tr>
</table><br/>
Result = (0.25/3)[1 + 4(0.9412 + 0.6400) + 2(0.8000) + 0.5]<br/>
= (0.08333)[1 + 4(1.5412) + 1.6 + 0.5]<br/>
= (0.08333)[1 + 6.1648 + 1.6 + 0.5]<br/>
= (0.08333)(9.2648)<br/>
= <b>0.7854</b><br/><br/>
<b>Exact value:</b> arctan(1) = π/4 ≈ 0.785398<br/>
<b>Error:</b> ≈ 0.000002 (very small).<br/><br/>
<b>Algorithm:</b><br/>
1. Start<br/>
2. Define f(x)<br/>
3. Read a, b, n (n must be even)<br/>
4. h = (b-a)/n<br/>
5. sum = f(a) + f(b)<br/>
6. For i = 1 to n-1:<br/>
   If i is even: sum += 2f(a + i·h)<br/>
   Else: sum += 4f(a + i·h)<br/>
7. Result = (h/3) × sum<br/>
8. Print Result<br/>
9. Stop""",
            },
        ]
    }
]

if __name__ == "__main__":
    print("Generating CACS252 Numerical Methods 2019 answer sheet...")
    generate_answer_sheet("CACS252", "numerical-methods", "Numerical Methods", 2019, "semester-4", CACS252_2019)
    print("✅ CACS252 2019 answer sheet generated!")
