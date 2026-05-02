#!/usr/bin/env python3
"""Generate answer sheet for Probability & Statistics 2020 (CAST 202)."""

import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

PROB_STATS_2020 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6 × 5 = 30]",
        "questions": [
            {
                "num": "4",
                "question": "Calculate correlation coefficient between income and expenditure in foods of certain families of Kathmandu Metropolitan from the following information:<br/><table border='1' cellpadding='3'><tr><td>Income (000 Rs)</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td>Expenditure in foods (000 Rs)</td><td>9</td><td>8</td><td>9</td><td>12</td><td>11</td></tr></table>",
                "marks": "5",
                "answer": """<b>Solution:</b> We calculate Karl Pearson's correlation coefficient.<br/><br/>
<table border='1' cellpadding='3'>
<tr><td>Income (X)</td><td>Expenditure (Y)</td><td>x=X-X̄</td><td>y=Y-Ȳ</td><td>x²</td><td>y²</td><td>xy</td></tr>
<tr><td>10</td><td>9</td><td>-2</td><td>-0.8</td><td>4</td><td>0.64</td><td>1.6</td></tr>
<tr><td>11</td><td>8</td><td>-1</td><td>-1.8</td><td>1</td><td>3.24</td><td>1.8</td></tr>
<tr><td>12</td><td>9</td><td>0</td><td>-0.8</td><td>0</td><td>0.64</td><td>0</td></tr>
<tr><td>13</td><td>12</td><td>1</td><td>2.2</td><td>1</td><td>4.84</td><td>2.2</td></tr>
<tr><td>14</td><td>11</td><td>2</td><td>1.2</td><td>4</td><td>1.44</td><td>2.4</td></tr>
<tr><td><b>ΣX=60</b></td><td><b>ΣY=49</b></td><td></td><td></td><td><b>Σx²=10</b></td><td><b>Σy²=10.8</b></td><td><b>Σxy=8</b></td></tr>
</table><br/>
X̄ = 60/5 = 12, Ȳ = 49/5 = 9.8<br/><br/>
r = Σxy / √(Σx² × Σy²) = 8 / √(10 × 10.8) = 8 / √108 = 8 / 10.392 = <b>0.77</b><br/><br/>
<b>Correlation coefficient r = 0.77</b> (strong positive correlation between income and food expenditure).""",
            },
            {
                "num": "5",
                "question": "A box contains 50 items of which 20 are defectives. If one item is selected randomly from the box, what is the probability that it is a non-defective item?",
                "marks": "5",
                "answer": """<b>Solution:</b><br/>
Total items = 50<br/>
Defective items = 20<br/>
Non-defective items = 50 - 20 = 30<br/><br/>
P(Non-defective) = Number of non-defective items / Total items<br/>
P(Non-defective) = 30/50 = <b>3/5 = 0.6 or 60%</b><br/><br/>
The probability that a randomly selected item is non-defective is <b>0.6 (60%)</b>.""",
            },
            {
                "num": "6",
                "question": "What is sampling? The standard deviation of marks in an entrance exam of BCA students is 0.5. How large a sample must be taken in order to be 95% confidence that the error of his/her estimate will not exceed 0.01.",
                "marks": "5",
                "answer": """<b>Sampling:</b><br/>
Sampling is the process of selecting a subset (sample) from a population to estimate population parameters. It is used when studying the entire population is impractical due to cost, time, or accessibility constraints.<br/><br/>
<b>Given:</b><br/>
Population standard deviation (σ) = 0.5<br/>
Confidence level = 95% → Z = 1.96<br/>
Margin of error (E) = 0.01<br/><br/>
<b>Formula for sample size:</b><br/>
n = (Z² × σ²) / E²<br/><br/>
n = (1.96² × 0.5²) / 0.01²<br/>
n = (3.8416 × 0.25) / 0.0001<br/>
n = 0.9604 / 0.0001<br/>
n = 9604<br/><br/>
<b>Required sample size = 9604 students.</b><br/><br/>
This is a very large sample because the desired margin of error (0.01) is extremely small relative to the standard deviation (0.5).""",
            },
            {
                "num": "7",
                "question": "Calculate the median and mode from following distribution:<br/><table border='1' cellpadding='3'><tr><td>Expenditure (000 Rs)</td><td>10-20</td><td>20-30</td><td>30-40</td><td>40-50</td><td>50-60</td><td>60-70</td></tr><tr><td>Number of families</td><td>7</td><td>12</td><td>15</td><td>13</td><td>8</td><td>5</td></tr></table>",
                "marks": "5",
                "answer": """<b>Solution:</b><br/><br/>
<table border='1' cellpadding='3'>
<tr><td>Expenditure</td><td>f</td><td>Cumulative f</td></tr>
<tr><td>10-20</td><td>7</td><td>7</td></tr>
<tr><td>20-30</td><td>12</td><td>19</td></tr>
<tr><td>30-40</td><td>15</td><td>34</td></tr>
<tr><td>40-50</td><td>13</td><td>47</td></tr>
<tr><td>50-60</td><td>8</td><td>55</td></tr>
<tr><td>60-70</td><td>5</td><td>60</td></tr>
</table><br/>
N = 60<br/><br/>
<b>Median:</b><br/>
Median class = class where N/2 = 30th item lies → 30-40 class<br/>
L = 30, h = 10, f = 15, cf = 19<br/>
Median = L + [(N/2 - cf)/f] × h<br/>
Median = 30 + [(30 - 19)/15] × 10<br/>
Median = 30 + (11/15) × 10 = 30 + 7.33 = <b>37.33 (000 Rs)</b><br/><br/>
<b>Mode:</b><br/>
Modal class = class with maximum frequency → 30-40 (f=15)<br/>
L = 30, h = 10, f₁ = 15, f₀ = 12, f₂ = 13<br/>
Mode = L + [(f₁ - f₀)/(2f₁ - f₀ - f₂)] × h<br/>
Mode = 30 + [(15-12)/(30-12-13)] × 10<br/>
Mode = 30 + [3/5] × 10 = 30 + 6 = <b>36 (000 Rs)</b><br/><br/>
<b>Median = Rs. 37,330 and Mode = Rs. 36,000</b>""",
            },
            {
                "num": "8",
                "question": "A test was given to three candidates taken at random from three provinces of Nepal. The scores of candidates are given below:<br/><table border='1' cellpadding='3'><tr><td>Gandaki</td><td>9</td><td>7</td><td>6</td></tr><tr><td>Lumbini</td><td>7</td><td>4</td><td>5</td></tr><tr><td>Bagmati</td><td>6</td><td>5</td><td>6</td></tr></table>Carry out one-way ANOVA.",
                "marks": "5",
                "answer": """<b>Solution:</b> One-Way ANOVA<br/><br/>
<table border='1' cellpadding='3'>
<tr><td>Gandaki</td><td>Lumbini</td><td>Bagmati</td></tr>
<tr><td>9</td><td>7</td><td>6</td></tr>
<tr><td>7</td><td>4</td><td>5</td></tr>
<tr><td>6</td><td>5</td><td>6</td></tr>
<tr><td><b>T₁=22</b></td><td><b>T₂=16</b></td><td><b>T₃=17</b></td></tr>
</table><br/>
Grand Total G = 55, N = 9, k = 3<br/><br/>
<b>Step 1: Correction Factor (CF)</b><br/>
CF = G²/N = 55²/9 = 3025/9 = 336.11<br/><br/>
<b>Step 2: Total Sum of Squares (TSS)</b><br/>
TSS = (81+49+36+49+16+25+36+25+36) - 336.11 = 353 - 336.11 = <b>16.89</b><br/><br/>
<b>Step 3: Between Groups (SSB)</b><br/>
SSB = (T₁²+T₂²+T₃²)/n - CF = (484+256+289)/3 - 336.11<br/>
= 1029/3 - 336.11 = 343 - 336.11 = <b>6.89</b><br/><br/>
<b>Step 4: Within Groups (SSW)</b><br/>
SSW = TSS - SSB = 16.89 - 6.89 = <b>10.00</b><br/><br/>
<b>ANOVA Table:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>Source</td><td>SS</td><td>df</td><td>MS</td><td>F</td></tr>
<tr><td>Between</td><td>6.89</td><td>2</td><td>3.445</td><td>2.07</td></tr>
<tr><td>Within</td><td>10.00</td><td>6</td><td>1.667</td><td></td></tr>
<tr><td>Total</td><td>16.89</td><td>8</td><td></td><td></td></tr>
</table><br/>
F-critical (2,6) at 5% = 5.14<br/><br/>
Since F = 2.07 < 5.14, the difference between provinces is <b>not statistically significant</b>. We conclude that there is no significant difference in test scores among candidates from different provinces.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2 × 10 = 20]",
        "questions": [
            {
                "num": "9",
                "question": "From the following data, determine average marks of student, standard deviation and coefficient of variation.<br/><table border='1' cellpadding='3'><tr><td>Marks</td><td>0-10</td><td>10-20</td><td>20-30</td><td>30-40</td><td>40-50</td><td>50-60</td><td>60-70</td><td>70-80</td><td>80-90</td></tr><tr><td>No. of people</td><td>54</td><td>90</td><td>86</td><td>58</td><td>62</td><td>82</td><td>78</td><td>66</td><td>70</td></tr></table>",
                "marks": "10",
                "answer": """<b>Solution:</b><br/><br/>
<table border='1' cellpadding='3'>
<tr><td>Marks</td><td>f</td><td>Mid (x)</td><td>d=(x-45)/10</td><td>fd</td><td>fd²</td></tr>
<tr><td>0-10</td><td>54</td><td>5</td><td>-4</td><td>-216</td><td>864</td></tr>
<tr><td>10-20</td><td>90</td><td>15</td><td>-3</td><td>-270</td><td>810</td></tr>
<tr><td>20-30</td><td>86</td><td>25</td><td>-2</td><td>-172</td><td>344</td></tr>
<tr><td>30-40</td><td>58</td><td>35</td><td>-1</td><td>-58</td><td>58</td></tr>
<tr><td>40-50</td><td>62</td><td>45</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>50-60</td><td>82</td><td>55</td><td>1</td><td>82</td><td>82</td></tr>
<tr><td>60-70</td><td>78</td><td>65</td><td>2</td><td>156</td><td>312</td></tr>
<tr><td>70-80</td><td>66</td><td>75</td><td>3</td><td>198</td><td>594</td></tr>
<tr><td>80-90</td><td>70</td><td>85</td><td>4</td><td>280</td><td>1120</td></tr>
<tr><td><b>Total</b></td><td><b>N=646</b></td><td></td><td></td><td><b>Σfd=0</b></td><td><b>Σfd²=4184</b></td></tr>
</table><br/>
Assumed mean A = 45, h = 10<br/><br/>
<b>Mean:</b> = A + (Σfd/N) × h = 45 + (0/646) × 10 = <b>45</b><br/><br/>
<b>Standard Deviation:</b><br/>
σ = h × √[(Σfd²/N) - (Σfd/N)²]<br/>
σ = 10 × √[(4184/646) - 0]<br/>
σ = 10 × √6.477 = 10 × 2.545 = <b>25.45</b><br/><br/>
<b>Coefficient of Variation:</b><br/>
CV = (σ/Mean) × 100 = (25.45/45) × 100 = <b>56.56%</b><br/><br/>
<b>Results:</b><br/>
• Average marks = <b>45</b><br/>
• Standard deviation = <b>25.45</b><br/>
• Coefficient of variation = <b>56.56%</b>""",
            },
            {
                "num": "10",
                "question": "In a normal distribution with mean 200 and standard deviation 20, find the probability that<br/>a) P(X>180) &nbsp;&nbsp; b) P(X<220) &nbsp;&nbsp; c) P(160&lt;X&lt;240)<br/>d) P(X>220) &nbsp;&nbsp; e) 10% values are less than what values of X?",
                "marks": "10",
                "answer": """<b>Solution:</b> Given: μ = 200, σ = 20<br/>
Z = (X - μ) / σ<br/><br/>
<b>a) P(X > 180):</b><br/>
Z = (180 - 200)/20 = -1<br/>
P(X > 180) = P(Z > -1) = P(Z < 1) = <b>0.8413 or 84.13%</b><br/><br/>
<b>b) P(X < 220):</b><br/>
Z = (220 - 200)/20 = 1<br/>
P(X < 220) = P(Z < 1) = <b>0.8413 or 84.13%</b><br/><br/>
<b>c) P(160 < X < 240):</b><br/>
Z₁ = (160-200)/20 = -2, Z₂ = (240-200)/20 = 2<br/>
P(-2 < Z < 2) = 0.9772 - 0.0228 = <b>0.9544 or 95.44%</b><br/><br/>
<b>d) P(X > 220):</b><br/>
P(X > 220) = 1 - P(X < 220) = 1 - 0.8413 = <b>0.1587 or 15.87%</b><br/><br/>
<b>e) Find X such that P(X < x) = 10%:</b><br/>
From Z-table, P(Z < -1.28) ≈ 0.10<br/>
X = μ + Z×σ = 200 + (-1.28)×20 = 200 - 25.6 = <b>174.4</b><br/><br/>
<b>10% of values are less than 174.4.</b>""",
            },
            {
                "num": "11",
                "question": "Describe simple random sampling with a suitable example. Write down the process of collecting primary data. Determine First Quartile (Q₁), 7th Decile (D₇) and 80th Percentile (P₈₀) from the following data:<br/><table border='1' cellpadding='3'><tr><td>Age in year</td><td>10</td><td>12</td><td>14</td><td>16</td><td>18</td><td>20</td><td>22</td><td>24</td><td>26</td></tr><tr><td>No. of people</td><td>7</td><td>11</td><td>21</td><td>35</td><td>27</td><td>17</td><td>11</td><td>8</td><td>5</td></tr></table>",
                "marks": "10",
                "answer": """<b>Simple Random Sampling:</b><br/>
Simple Random Sampling is a probability sampling method where every member of the population has an equal and independent chance of being selected. It is the most basic form of random sampling.<br/><br/>
<b>Example:</b> To select 50 students from a college of 1000 students, assign numbers 1-1000 to all students, use a random number table or computer to generate 50 random numbers between 1 and 1000, and select the students with those numbers.<br/><br/>
<b>Process of Collecting Primary Data:</b><br/>
1. <b>Define objectives:</b> Clearly state what information is needed and why.<br/>
2. <b>Determine population and sample:</b> Identify who to collect data from and select an appropriate sample.<br/>
3. <b>Choose data collection method:</b> Direct personal interview, indirect oral investigation, questionnaire, observation, or experimentation.<br/>
4. <b>Design data collection instruments:</b> Prepare questionnaires, interview schedules, or observation forms with clear, unbiased questions.<br/>
5. <b>Pre-test:</b> Conduct a pilot study to identify and correct problems.<br/>
6. <b>Collect data:</b> Administer the instrument to the sample.<br/>
7. <b>Edit and code:</b> Check for completeness, consistency, and accuracy; convert responses to codes for analysis.<br/><br/>
<b>Calculation of Q₁, D₇, and P₈₀:</b><br/><br/>
<table border='1' cellpadding='3'>
<tr><td>Age (X)</td><td>f</td><td>Cumulative f</td></tr>
<tr><td>10</td><td>7</td><td>7</td></tr>
<tr><td>12</td><td>11</td><td>18</td></tr>
<tr><td>14</td><td>21</td><td>39</td></tr>
<tr><td>16</td><td>35</td><td>74</td></tr>
<tr><td>18</td><td>27</td><td>101</td></tr>
<tr><td>20</td><td>17</td><td>118</td></tr>
<tr><td>22</td><td>11</td><td>129</td></tr>
<tr><td>24</td><td>8</td><td>137</td></tr>
<tr><td>26</td><td>5</td><td>142</td></tr>
</table><br/>
N = 142<br/><br/>
<b>First Quartile (Q₁):</b><br/>
Q₁ position = N/4 = 142/4 = 35.5th item<br/>
From cf, 35.5th item falls at age <b>16 years</b><br/><br/>
<b>7th Decile (D₇):</b><br/>
D₇ position = 7N/10 = 7×142/10 = 99.4th item<br/>
From cf, 99.4th item falls at age <b>18 years</b><br/><br/>
<b>80th Percentile (P₈₀):</b><br/>
P₈₀ position = 80N/100 = 80×142/100 = 113.6th item<br/>
From cf, 113.6th item falls at age <b>20 years</b><br/><br/>
<b>Results:</b> Q₁ = <b>16 years</b>, D₇ = <b>18 years</b>, P₈₀ = <b>20 years</b>""",
            },
        ]
    }
]

if __name__ == "__main__":
    generate_answer_sheet("CAST202", "probability-statistics", "Probability & Statistics", 2020, "semester-3", PROB_STATS_2020)
    print("✅ Probability & Statistics 2020 answer sheet generated!")
