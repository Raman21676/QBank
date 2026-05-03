#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS202_2024 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "Describe the scope and limitations of Statistics.",
                "marks": "5",
                "answer": """<b>Scope of Statistics:</b><br/>
Statistics is a branch of mathematics that deals with the collection, organization, analysis, interpretation, and presentation of data. Its scope extends to almost every field of human activity:<br/><br/>

1. <b>Business and Economics:</b> Statistics is extensively used in market research, demand forecasting, quality control, production planning, sales analysis, and financial decision-making. Businesses rely on statistical data to understand consumer behavior and optimize operations.<br/><br/>

2. <b>Government and Administration:</b> Governments use statistics for planning and policy formulation. Census data, national income accounts, employment statistics, and health surveys are essential for effective governance and resource allocation.<br/><br/>

3. <b>Natural and Physical Sciences:</b> In biology, physics, chemistry, and environmental science, statistics helps in designing experiments, analyzing results, testing hypotheses, and drawing valid conclusions. Statistical methods are fundamental to modern scientific research.<br/><br/>

4. <b>Social Sciences:</b> Sociology, psychology, education, and political science use statistics to study population trends, voter behavior, educational outcomes, and social phenomena. Surveys and sampling techniques are crucial tools.<br/><br/>

5. <b>Medicine and Public Health:</b> Clinical trials, epidemiological studies, and drug efficacy testing all depend on statistical analysis. Statistics helps determine whether a treatment is effective and safe.<br/><br/>

6. <b>Engineering and Technology:</b> Quality control, reliability analysis, signal processing, and machine learning all rely heavily on statistical methods.<br/><br/>

7. <b>Agriculture:</b> Statistical designs like randomized block designs and Latin squares are used to test crop varieties, fertilizers, and irrigation methods.<br/><br/>

<b>Limitations of Statistics:</b><br/><br/>

1. <b>Deals only with aggregates, not individuals:</b> Statistics studies groups and aggregates. It cannot provide information about a single individual or unit. For example, the average marks of a class don't reveal any specific student's performance.<br/><br/>

2. <b>Requires homogeneous data:</b> Statistical methods are applicable only when data is homogeneous. Combining data from different sources or populations without proper classification can lead to misleading results.<br/><br/>

3. <b>Results are true only on average:</b> Statistical laws are not exact like mathematical laws. They hold true for large groups and on average, but may not apply to individual cases.<br/><br/>

4. <b>Can be misused:</b> Statistics can be manipulated to support false conclusions. Biased sampling, selective reporting, and improper analysis can distort reality. As the saying goes, "There are three kinds of lies: lies, damned lies, and statistics."<br/><br/>

5. <b>Limited to quantifiable phenomena:</b> Statistics cannot directly measure qualitative characteristics like honesty, beauty, intelligence, or satisfaction unless they are converted into numerical scales.<br/><br/>

6. <b>Requires specialized knowledge:</b> Proper application of statistical methods requires training and expertise. Untrained users may apply wrong techniques and draw incorrect conclusions.<br/><br/>

7. <b>Data collection limitations:</b> The accuracy of statistical conclusions depends heavily on the quality of data collection. Errors in sampling, non-response bias, and measurement errors can compromise validity.<br/><br/>

8. <b>Correlation does not imply causation:</b> Statistical relationships between variables do not necessarily indicate cause-and-effect relationships. Spurious correlations can occur between unrelated variables.""",
            },
            {
                "num": "3",
                "question": "What do you mean by statistics? The following table represents the marks of Probability and Statistics of 100 students.<br/><table border='1' cellpadding='3'><tr><td>Marks</td><td>0-10</td><td>10-20</td><td>20-30</td><td>30-40</td><td>40-50</td><td>50-60</td><td>60-70</td></tr><tr><td>No. of Students</td><td>5</td><td>12</td><td>18</td><td>25</td><td>20</td><td>14</td><td>6</td></tr></table>Find the mean, median and standard deviation of all 100 students.",
                "marks": "5",
                "answer": """<b>Meaning of Statistics:</b><br/>
Statistics is the science of collecting, organizing, presenting, analyzing, and interpreting numerical data to make informed decisions. In the singular sense, it refers to the body of methods and techniques used for data analysis. In the plural sense, it refers to the numerical facts and figures themselves (e.g., population statistics, economic statistics).<br/><br/>

<b>Given Data:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>Marks</td><td>No. of Students (f)</td><td>Midpoint (x)</td><td>fx</td><td>Cumulative f</td><td>d=(x-35)/10</td><td>fd</td><td>fd²</td></tr>
<tr><td>0-10</td><td>5</td><td>5</td><td>25</td><td>5</td><td>-3</td><td>-15</td><td>45</td></tr>
<tr><td>10-20</td><td>12</td><td>15</td><td>180</td><td>17</td><td>-2</td><td>-24</td><td>48</td></tr>
<tr><td>20-30</td><td>18</td><td>25</td><td>450</td><td>35</td><td>-1</td><td>-18</td><td>18</td></tr>
<tr><td>30-40</td><td>25</td><td>35</td><td>875</td><td>60</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>40-50</td><td>20</td><td>45</td><td>900</td><td>80</td><td>1</td><td>20</td><td>20</td></tr>
<tr><td>50-60</td><td>14</td><td>55</td><td>770</td><td>94</td><td>2</td><td>28</td><td>56</td></tr>
<tr><td>60-70</td><td>6</td><td>65</td><td>390</td><td>100</td><td>3</td><td>18</td><td>54</td></tr>
<tr><td><b>Total</b></td><td><b>N=100</b></td><td></td><td><b>Σfx=3590</b></td><td></td><td></td><td><b>Σfd=9</b></td><td><b>Σfd²=241</b></td></tr>
</table><br/>

<b>1. Mean:</b><br/>
Using direct method:<br/>
Mean = Σfx / N = 3590 / 100 = <b>35.9 marks</b><br/><br/>

Using assumed mean method (A = 35, h = 10):<br/>
Mean = A + (Σfd / N) × h = 35 + (9/100) × 10 = 35 + 0.9 = <b>35.9 marks</b><br/><br/>

<b>2. Median:</b><br/>
Median class = class where N/2 = 50th item lies<br/>
From cumulative frequency, the 50th item falls in the class <b>30-40</b> (c.f. = 60)<br/>
L = 30 (lower boundary of median class)<br/>
h = 10 (class width)<br/>
f = 25 (frequency of median class)<br/>
cf = 35 (cumulative frequency of class preceding median class)<br/><br/>

Median = L + [(N/2 - cf) / f] × h<br/>
Median = 30 + [(50 - 35) / 25] × 10<br/>
Median = 30 + (15/25) × 10<br/>
Median = 30 + 6 = <b>36 marks</b><br/><br/>

<b>3. Standard Deviation:</b><br/>
Using assumed mean method:<br/>
σ = h × √[(Σfd²/N) - (Σfd/N)²]<br/>
σ = 10 × √[(241/100) - (9/100)²]<br/>
σ = 10 × √[2.41 - 0.0081]<br/>
σ = 10 × √2.4019<br/>
σ = 10 × 1.5498 = <b>15.498 ≈ 15.50 marks</b><br/><br/>

<b>Results:</b><br/>
• Mean = <b>35.9 marks</b><br/>
• Median = <b>36 marks</b><br/>
• Standard Deviation = <b>15.50 marks</b>""",
            },
            {
                "num": "4",
                "question": "Define correlation. From the following data on marks of 10 students in the two subjects, calculate the Karl Pearson's coefficient of correlation and interpret the result:<br/><table border='1' cellpadding='3'><tr><td>Student</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>Math (X)</td><td>45</td><td>55</td><td>60</td><td>50</td><td>65</td><td>70</td><td>40</td><td>75</td><td>80</td><td>58</td></tr><tr><td>Stats (Y)</td><td>40</td><td>50</td><td>55</td><td>45</td><td>60</td><td>65</td><td>35</td><td>70</td><td>75</td><td>52</td></tr></table>",
                "marks": "5",
                "answer": """<b>Correlation:</b><br/>
Correlation is a statistical measure that indicates the extent to which two or more variables fluctuate together. It describes the degree and direction of relationship between two variables. Correlation can be:<br/>
• <b>Positive:</b> Both variables increase or decrease together<br/>
• <b>Negative:</b> One variable increases while the other decreases<br/>
• <b>Zero:</b> No linear relationship between variables<br/><br/>

<b>Karl Pearson's Coefficient of Correlation (r):</b><br/>
It measures the linear relationship between two variables X and Y. The formula is:<br/>
r = Σ[(X - X̄)(Y - Ȳ)] / √[Σ(X - X̄)² × Σ(Y - Ȳ)²]<br/>
or equivalently:<br/>
r = [NΣXY - (ΣX)(ΣY)] / √{[NΣX² - (ΣX)²][NΣY² - (ΣY)²]}<br/><br/>

<b>Calculation:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>Student</td><td>X</td><td>Y</td><td>X²</td><td>Y²</td><td>XY</td></tr>
<tr><td>1</td><td>45</td><td>40</td><td>2025</td><td>1600</td><td>1800</td></tr>
<tr><td>2</td><td>55</td><td>50</td><td>3025</td><td>2500</td><td>2750</td></tr>
<tr><td>3</td><td>60</td><td>55</td><td>3600</td><td>3025</td><td>3300</td></tr>
<tr><td>4</td><td>50</td><td>45</td><td>2500</td><td>2025</td><td>2250</td></tr>
<tr><td>5</td><td>65</td><td>60</td><td>4225</td><td>3600</td><td>3900</td></tr>
<tr><td>6</td><td>70</td><td>65</td><td>4900</td><td>4225</td><td>4550</td></tr>
<tr><td>7</td><td>40</td><td>35</td><td>1600</td><td>1225</td><td>1400</td></tr>
<tr><td>8</td><td>75</td><td>70</td><td>5625</td><td>4900</td><td>5250</td></tr>
<tr><td>9</td><td>80</td><td>75</td><td>6400</td><td>5625</td><td>6000</td></tr>
<tr><td>10</td><td>58</td><td>52</td><td>3364</td><td>2704</td><td>3016</td></tr>
<tr><td><b>Total</b></td><td><b>ΣX=598</b></td><td><b>ΣY=547</b></td><td><b>ΣX²=37264</b></td><td><b>ΣY²=31429</b></td><td><b>ΣXY=34216</b></td></tr>
</table><br/>

N = 10<br/><br/>

<b>Step 1:</b> Calculate means<br/>
X̄ = ΣX / N = 598 / 10 = <b>59.8</b><br/>
Ȳ = ΣY / N = 547 / 10 = <b>54.7</b><br/><br/>

<b>Step 2:</b> Calculate deviation method (for verification)<br/>
<table border='1' cellpadding='3'>
<tr><td>X</td><td>Y</td><td>x=X-X̄</td><td>y=Y-Ȳ</td><td>x²</td><td>y²</td><td>xy</td></tr>
<tr><td>45</td><td>40</td><td>-14.8</td><td>-14.7</td><td>219.04</td><td>216.09</td><td>217.56</td></tr>
<tr><td>55</td><td>50</td><td>-4.8</td><td>-4.7</td><td>23.04</td><td>22.09</td><td>22.56</td></tr>
<tr><td>60</td><td>55</td><td>0.2</td><td>0.3</td><td>0.04</td><td>0.09</td><td>0.06</td></tr>
<tr><td>50</td><td>45</td><td>-9.8</td><td>-9.7</td><td>96.04</td><td>94.09</td><td>95.06</td></tr>
<tr><td>65</td><td>60</td><td>5.2</td><td>5.3</td><td>27.04</td><td>28.09</td><td>27.56</td></tr>
<tr><td>70</td><td>65</td><td>10.2</td><td>10.3</td><td>104.04</td><td>106.09</td><td>105.06</td></tr>
<tr><td>40</td><td>35</td><td>-19.8</td><td>-19.7</td><td>392.04</td><td>388.09</td><td>390.06</td></tr>
<tr><td>75</td><td>70</td><td>15.2</td><td>15.3</td><td>231.04</td><td>234.09</td><td>232.56</td></tr>
<tr><td>80</td><td>75</td><td>20.2</td><td>20.3</td><td>408.04</td><td>412.09</td><td>410.06</td></tr>
<tr><td>58</td><td>52</td><td>-1.8</td><td>-2.7</td><td>3.24</td><td>7.29</td><td>4.86</td></tr>
<tr><td></td><td></td><td></td><td></td><td><b>1503.6</b></td><td><b>1508.1</b></td><td><b>1505.4</b></td></tr>
</table><br/>

<b>Step 3:</b> Apply formula<br/>
r = Σxy / √(Σx² × Σy²)<br/>
r = 1505.4 / √(1503.6 × 1508.1)<br/>
r = 1505.4 / √2,267,579.16<br/>
r = 1505.4 / 1505.85<br/>
r = <b>0.9997 ≈ 1.0</b><br/><br/>

<b>Verification using direct formula:</b><br/>
r = [10×34216 - 598×547] / √{[10×37264 - 598²][10×31429 - 547²]}<br/>
r = [342160 - 327106] / √{[372640 - 357604][314290 - 299209]}<br/>
r = 15054 / √{15036 × 15081}<br/>
r = 15054 / √226,958,316<br/>
r = 15054 / 15065.14<br/>
r = <b>0.9993 ≈ 1.0</b><br/><br/>

<b>Interpretation:</b><br/>
The Karl Pearson's correlation coefficient <b>r ≈ +1.0</b>, which indicates a <b>perfect positive correlation</b> between marks in Mathematics and Statistics. This means that students who perform well in Mathematics tend to perform equally well in Statistics, and vice versa. The two subjects are strongly linearly related.""",
            },
            {
                "num": "5",
                "question": "Define regression. The following table gives the age of the computers of a certain company and annual maintenance costs:<br/><table border='1' cellpadding='3'><tr><td>Age of computers (years) (X)</td><td>2</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>Maintenance costs (Rs. '00) (Y)</td><td>12</td><td>18</td><td>24</td><td>28</td><td>32</td><td>36</td></tr></table>Obtain the regression equation for cost related to age. Estimate the cost of maintenance for 10 years old computer. Interpret the slope.",
                "marks": "5",
                "answer": """<b>Regression:</b><br/>
Regression is a statistical technique used to determine the relationship between a dependent variable and one or more independent variables. It helps predict the value of the dependent variable based on known values of independent variables. In simple linear regression, the relationship is modeled as a straight line: Y = a + bX, where b is the slope and a is the intercept.<br/><br/>

<b>Given Data:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>Age (X)</td><td>Cost (Y)</td><td>X²</td><td>Y²</td><td>XY</td></tr>
<tr><td>2</td><td>12</td><td>4</td><td>144</td><td>24</td></tr>
<tr><td>4</td><td>18</td><td>16</td><td>324</td><td>72</td></tr>
<tr><td>5</td><td>24</td><td>25</td><td>576</td><td>120</td></tr>
<tr><td>6</td><td>28</td><td>36</td><td>784</td><td>168</td></tr>
<tr><td>7</td><td>32</td><td>49</td><td>1024</td><td>224</td></tr>
<tr><td>8</td><td>36</td><td>64</td><td>1296</td><td>288</td></tr>
<tr><td><b>ΣX=32</b></td><td><b>ΣY=150</b></td><td><b>ΣX²=194</b></td><td><b>ΣY²=4148</b></td><td><b>ΣXY=896</b></td></tr>
</table><br/>

N = 6<br/><br/>

<b>Step 1:</b> Calculate means<br/>
X̄ = ΣX / N = 32 / 6 = <b>5.333</b><br/>
Ȳ = ΣY / N = 150 / 6 = <b>25</b><br/><br/>

<b>Step 2:</b> Calculate regression coefficients<br/>
The regression equation of Y on X is: <b>Y = a + bX</b><br/>
where b (slope) = [NΣXY - (ΣX)(ΣY)] / [NΣX² - (ΣX)²]<br/>
and a (intercept) = Ȳ - bX̄<br/><br/>

b = [6×896 - 32×150] / [6×194 - 32²]<br/>
b = [5376 - 4800] / [1164 - 1024]<br/>
b = 576 / 140<br/>
b = <b>4.114</b><br/><br/>

a = 25 - (4.114 × 5.333)<br/>
a = 25 - 21.943<br/>
a = <b>3.057</b><br/><br/>

<b>Regression Equation:</b><br/>
<b>Y = 3.057 + 4.114X</b><br/><br/>

<b>Step 3:</b> Estimate cost for 10 years old computer<br/>
When X = 10:<br/>
Y = 3.057 + 4.114 × 10<br/>
Y = 3.057 + 41.14<br/>
Y = <b>44.197 ≈ Rs. 4,420</b> (since Y is in Rs. '00)<br/><br/>

<b>Interpretation of Slope (b = 4.114):</b><br/>
The slope of 4.114 indicates that for every <b>1-year increase</b> in the age of the computer, the annual maintenance cost increases by approximately <b>Rs. 411.40</b> (since Y is in hundreds). This positive slope confirms that older computers require higher maintenance costs, which is economically expected as hardware ages and components wear out.""",
            },
            {
                "num": "6",
                "question": "Define Poisson distribution. In a certain factory timing out optical lenses, there is a small chance, 1/500 for any lens to be defective. The lenses are supplied in a packet of 10 each. What is the probability that a packet will contain: (i) No defective lens, (ii) At least one defective lens, and (iii) At most two defective lenses?",
                "marks": "5",
                "answer": """<b>Poisson Distribution:</b><br/>
The Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space, provided these events occur with a known constant mean rate and independently of the time since the last event. It is used to model rare events.<br/><br/>

<b>Probability Mass Function (PMF):</b><br/>
P(X = k) = (e<sup>-λ</sup> × λ<sup>k</sup>) / k!<br/>
where λ = mean number of occurrences, k = 0, 1, 2, ...<br/><br/>

<b>Properties:</b><br/>
• Mean = λ, Variance = λ<br/>
• The events are independent<br/>
• The average rate (λ) is constant<br/>
• Two events cannot occur at exactly the same instant<br/><br/>

<b>Given:</b><br/>
Probability of defective lens, p = 1/500 = 0.002<br/>
Number of lenses in a packet, n = 10<br/>
λ = n × p = 10 × 0.002 = <b>0.02</b><br/><br/>

<b>(i) Probability of no defective lens (X = 0):</b><br/>
P(X = 0) = (e<sup>-0.02</sup> × 0.02<sup>0</sup>) / 0!<br/>
P(X = 0) = e<sup>-0.02</sup> × 1 / 1<br/>
P(X = 0) = <b>0.9802</b><br/><br/>

<b>(ii) Probability of at least one defective lens (X ≥ 1):</b><br/>
P(X ≥ 1) = 1 - P(X = 0)<br/>
P(X ≥ 1) = 1 - 0.9802<br/>
P(X ≥ 1) = <b>0.0198</b><br/><br/>

<b>(iii) Probability of at most two defective lenses (X ≤ 2):</b><br/>
P(X ≤ 2) = P(X = 0) + P(X = 1) + P(X = 2)<br/><br/>

P(X = 1) = (e<sup>-0.02</sup> × 0.02<sup>1</sup>) / 1!<br/>
P(X = 1) = 0.9802 × 0.02<br/>
P(X = 1) = <b>0.019604</b><br/><br/>

P(X = 2) = (e<sup>-0.02</sup> × 0.02<sup>2</sup>) / 2!<br/>
P(X = 2) = (0.9802 × 0.0004) / 2<br/>
P(X = 2) = 0.00039208 / 2<br/>
P(X = 2) = <b>0.000196</b><br/><br/>

P(X ≤ 2) = 0.9802 + 0.019604 + 0.000196<br/>
P(X ≤ 2) = <b>0.999999 ≈ 1.0</b><br/><br/>

<b>Summary of Results:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Condition</b></td><td><b>Probability</b></td><td><b>Percentage</b></td></tr>
<tr><td>No defective lens</td><td>0.9802</td><td>98.02%</td></tr>
<tr><td>At least one defective lens</td><td>0.0198</td><td>1.98%</td></tr>
<tr><td>At most two defective lenses</td><td>≈ 1.0000</td><td>≈ 100%</td></tr>
</table><br/>

<b>Conclusion:</b> Since the probability of a lens being defective is very small (0.002) and the packet contains only 10 lenses, it is highly likely (98.02%) that a packet will contain no defective lenses. The probability of having more than 2 defective lenses is negligible.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "Explain the different measures of central tendency and measures of dispersion with suitable examples.",
                "marks": "10",
                "answer": """<b>Measures of Central Tendency:</b><br/>
Central tendency refers to the central or typical value around which data observations tend to cluster. The main measures are:<br/><br/>

<b>1. Arithmetic Mean:</b><br/>
The sum of all observations divided by the number of observations.<br/>
Formula: X̄ = ΣX / N (for raw data) or X̄ = Σfx / N (for frequency distribution)<br/>
<b>Example:</b> Marks of 5 students: 60, 70, 80, 50, 90<br/>
Mean = (60+70+80+50+90)/5 = 350/5 = <b>70</b><br/><br/>

<b>2. Median:</b><br/>
The middle value when data is arranged in ascending or descending order.<br/>
For odd N: Median = value at (N+1)/2 position<br/>
For even N: Median = average of values at N/2 and (N/2)+1 positions<br/>
<b>Example:</b> 12, 15, 18, 22, 30 → Median = <b>18</b> (3rd value)<br/><br/>

<b>3. Mode:</b><br/>
The value that appears most frequently in a dataset.<br/>
<b>Example:</b> 5, 7, 8, 8, 9, 10, 10, 10 → Mode = <b>10</b><br/><br/>

<b>4. Geometric Mean:</b><br/>
The nth root of the product of n observations. Used for growth rates and ratios.<br/>
Formula: GM = (X₁ × X₂ × ... × X<sub>n</sub>)<sup>1/n</sup><br/><br/>

<b>5. Harmonic Mean:</b><br/>
The reciprocal of the arithmetic mean of reciprocals. Used for rates and ratios.<br/>
Formula: HM = N / Σ(1/X)<br/><br/>

<b>Measures of Dispersion:</b><br/>
Dispersion measures the spread or variability of data around the central value.<br/><br/>

<b>1. Range:</b><br/>
The difference between the maximum and minimum values.<br/>
<b>Example:</b> Data: 10, 25, 30, 45, 50 → Range = 50 - 10 = <b>40</b><br/><br/>

<b>2. Quartile Deviation (Semi-Interquartile Range):</b><br/>
QD = (Q₃ - Q₁) / 2<br/>
It measures the spread of the middle 50% of data.<br/><br/>

<b>3. Mean Deviation:</b><br/>
The average of absolute deviations from the mean or median.<br/>
Formula: MD = Σ|X - X̄| / N<br/><br/>

<b>4. Standard Deviation:</b><br/>
The square root of the average of squared deviations from the mean. It is the most widely used measure of dispersion.<br/>
Formula: σ = √[Σ(X - X̄)² / N]<br/>
<b>Example:</b> Data: 10, 20, 30, 40, 50<br/>
Mean = 30<br/>
σ = √[(400+100+0+100+400)/5] = √(1000/5) = √200 = <b>14.14</b><br/><br/>

<b>5. Variance:</b><br/>
The square of standard deviation. σ² = Σ(X - X̄)² / N<br/><br/>

<b>6. Coefficient of Variation (CV):</b><br/>
A relative measure of dispersion: CV = (σ / X̄) × 100%<br/>
Used to compare variability between datasets with different units or means.<br/><br/>

<b>Importance of Measures of Dispersion:</b><br/>
• They show how reliable the central tendency is<br/>
• They help compare variability between different datasets<br/>
• They are essential for statistical inference and quality control<br/>
• They reveal the homogeneity or heterogeneity of data""",
            },
            {
                "num": "10",
                "question": "A normal distribution has mean 50 and standard deviation 5. Find the probability that: (a) X > 55, (b) X < 45, (c) 45 < X < 55, (d) X > 60.",
                "marks": "10",
                "answer": """<b>Given:</b> Mean (μ) = 50, Standard Deviation (σ) = 5<br/>
The standard normal variate Z = (X - μ) / σ<br/><br/>

<b>(a) P(X > 55):</b><br/>
Z = (55 - 50) / 5 = 5/5 = <b>1.0</b><br/>
P(X > 55) = P(Z > 1.0) = 1 - P(Z < 1.0) = 1 - 0.8413 = <b>0.1587 or 15.87%</b><br/><br/>

<b>(b) P(X < 45):</b><br/>
Z = (45 - 50) / 5 = -5/5 = <b>-1.0</b><br/>
P(X < 45) = P(Z < -1.0) = 1 - P(Z < 1.0) = 1 - 0.8413 = <b>0.1587 or 15.87%</b><br/>
(Alternatively, by symmetry of normal distribution, P(Z < -1) = P(Z > 1) = 0.1587)<br/><br/>

<b>(c) P(45 < X < 55):</b><br/>
Z₁ = (45 - 50) / 5 = -1.0<br/>
Z₂ = (55 - 50) / 5 = 1.0<br/>
P(45 < X < 55) = P(-1.0 < Z < 1.0)<br/>
= P(Z < 1.0) - P(Z < -1.0)<br/>
= 0.8413 - 0.1587<br/>
= <b>0.6826 or 68.26%</b><br/><br/>

(Using the empirical rule: approximately 68% of data lies within 1 standard deviation of the mean)<br/><br/>

<b>(d) P(X > 60):</b><br/>
Z = (60 - 50) / 5 = 10/5 = <b>2.0</b><br/>
P(X > 60) = P(Z > 2.0) = 1 - P(Z < 2.0) = 1 - 0.9772 = <b>0.0228 or 2.28%</b><br/><br/>

<b>Summary Table:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Condition</b></td><td><b>Z-value</b></td><td><b>Probability</b></td><td><b>Percentage</b></td></tr>
<tr><td>X > 55</td><td>1.0</td><td>0.1587</td><td>15.87%</td></tr>
<tr><td>X < 45</td><td>-1.0</td><td>0.1587</td><td>15.87%</td></tr>
<tr><td>45 < X < 55</td><td>-1.0 to 1.0</td><td>0.6826</td><td>68.26%</td></tr>
<tr><td>X > 60</td><td>2.0</td><td>0.0228</td><td>2.28%</td></tr>
</table>""",
            },
            {
                "num": "11",
                "question": "Explain the different methods of sampling. A coin is tossed 10 times. Find the probability of getting: (a) exactly 6 heads, (b) at least 6 heads, (c) at most 6 heads.",
                "marks": "10",
                "answer": """<b>Methods of Sampling:</b><br/><br/>

<b>1. Simple Random Sampling:</b><br/>
Every member of the population has an equal and independent chance of being selected. Methods include lottery system, random number tables, or computer-generated random numbers. It is the most basic and unbiased sampling method.<br/><br/>

<b>2. Stratified Random Sampling:</b><br/>
The population is divided into homogeneous subgroups called strata based on certain characteristics (age, gender, income). Samples are then randomly selected from each stratum, usually in proportion to the stratum's size in the population. This ensures representation from all subgroups.<br/><br/>

<b>3. Systematic Sampling:</b><br/>
Every kth member of the population is selected after a random start, where k = N/n (population size/sample size). For example, selecting every 10th name from a list. It is easier to implement than simple random sampling but may introduce bias if there is a pattern in the population.<br/><br/>

<b>4. Cluster Sampling:</b><br/>
The population is divided into clusters (usually based on geographic location). A random sample of clusters is selected, and all members within the chosen clusters are included in the sample. It is cost-effective for large, dispersed populations but may have higher sampling error.<br/><br/>

<b>5. Multistage Sampling:</b><br/>
A combination of different sampling methods applied in stages. For example, first select clusters, then select strata within clusters, then randomly sample individuals. Commonly used in large-scale surveys and national censuses.<br/><br/>

<b>6. Convenience Sampling:</b><br/>
Samples are selected based on ease of access and availability. It is non-random and prone to bias, but quick and inexpensive. Examples include surveying people nearby or using readily available data.<br/><br/>

<b>7. Judgment/Purposive Sampling:</b><br/>
The researcher uses personal judgment to select samples that are most relevant to the study. It is subjective and non-random, used when specific expertise is required.<br/><br/>

<b>8. Quota Sampling:</b><br/>
Similar to stratified sampling but non-random. The researcher selects samples to fill predetermined quotas for different subgroups. Common in market research and opinion polling.<br/><br/>

<b>Binomial Distribution Problem:</b><br/>
Given: n = 10 tosses, p = 0.5 (probability of head), q = 0.5 (probability of tail)<br/>
P(X = k) = <sup>n</sup>C<sub>k</sub> × p<sup>k</sup> × q<sup>n-k</sup> = <sup>10</sup>C<sub>k</sub> × (0.5)<sup>k</sup> × (0.5)<sup>10-k</sup> = <sup>10</sup>C<sub>k</sub> × (0.5)<sup>10</sup><br/><br/>

<b>(a) Exactly 6 heads (X = 6):</b><br/>
P(X = 6) = <sup>10</sup>C<sub>6</sub> × (0.5)<sup>10</sup><br/>
<sup>10</sup>C<sub>6</sub> = 10! / (6! × 4!) = (10×9×8×7)/(4×3×2×1) = 210<br/>
P(X = 6) = 210 × (1/1024) = 210/1024 = <b>0.2051 or 20.51%</b><br/><br/>

<b>(b) At least 6 heads (X ≥ 6):</b><br/>
P(X ≥ 6) = P(X=6) + P(X=7) + P(X=8) + P(X=9) + P(X=10)<br/><br/>
P(X=6) = 210/1024 = 0.2051<br/>
P(X=7) = <sup>10</sup>C<sub>7</sub> × (0.5)<sup>10</sup> = 120/1024 = 0.1172<br/>
P(X=8) = <sup>10</sup>C<sub>8</sub> × (0.5)<sup>10</sup> = 45/1024 = 0.0439<br/>
P(X=9) = <sup>10</sup>C<sub>9</sub> × (0.5)<sup>10</sup> = 10/1024 = 0.0098<br/>
P(X=10) = <sup>10</sup>C<sub>10</sub> × (0.5)<sup>10</sup> = 1/1024 = 0.0010<br/><br/>
P(X ≥ 6) = (210 + 120 + 45 + 10 + 1) / 1024 = 386/1024 = <b>0.3769 or 37.69%</b><br/><br/>

<b>(c) At most 6 heads (X ≤ 6):</b><br/>
P(X ≤ 6) = P(X=0) + P(X=1) + P(X=2) + P(X=3) + P(X=4) + P(X=5) + P(X=6)<br/><br/>
Or using complementary probability:<br/>
P(X ≤ 6) = 1 - P(X > 6) = 1 - [P(X=7) + P(X=8) + P(X=9) + P(X=10)]<br/>
P(X ≤ 6) = 1 - (120 + 45 + 10 + 1)/1024<br/>
P(X ≤ 6) = 1 - 176/1024<br/>
P(X ≤ 6) = 848/1024 = <b>0.8281 or 82.81%</b><br/><br/>

Alternatively:<br/>
P(X ≤ 6) = P(X=0) + P(X=1) + P(X=2) + P(X=3) + P(X=4) + P(X=5) + P(X=6)<br/>
= (1 + 10 + 45 + 120 + 210 + 252 + 210) / 1024<br/>
= 848/1024 = <b>0.8281 or 82.81%</b>""",
            },
        ]
    }
]

if __name__ == "__main__":
    generate_answer_sheet(
        "CACS202", "probability-statistics", "Probability & Statistics",
        2024, "semester-3", CACS202_2024
    )
    print("Answer sheet generation complete for CACS202 2024!")
