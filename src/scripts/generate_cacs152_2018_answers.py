#!/usr/bin/env python3
"""Generate answer sheet for CACS152 2018 Financial Accounting."""

import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

# Note: The source PDF only contained Group A (MCQs) and partial Group B.
# Some Group B questions and all Group C questions were not extractable.

QUESTIONS_DATA = [
    {
        "title": "Group A",
        "instruction": "Attempt all the questions. [10×1 = 10]",
        "questions": [
            {
                "num": "25",
                "question": "Which one is not an accounting process?",
                "marks": "1",
                "answer": """<b>Correct Answer: d) Preparing trial balance.</b><br/>
The accounting process includes identification, recording, and classifying financial transactions. Preparing a trial balance is part of the summarization stage, not a core accounting process itself. The main accounting processes are: identifying financial transactions, recording them in journals, classifying into ledgers, and summarizing through trial balance and financial statements.""",
            },
            {
                "num": "26",
                "question": "Which accounting concept tells us business and business man are different?",
                "marks": "1",
                "answer": """<b>Correct Answer: d) Business entity concept</b><br/>
The <b>Business Entity Concept</b> (or Separate Entity Concept) states that a business is treated as a separate legal and accounting entity from its owners. Personal transactions of the owner are not mixed with business transactions. This ensures that financial statements reflect only business activities, not personal finances of the proprietor.""",
            },
            {
                "num": "27",
                "question": "Which one is accounting package of computer software?",
                "marks": "1",
                "answer": """<b>Correct Answer: c) Tally</b><br/>
<b>Tally</b> is a popular accounting software package used for bookkeeping, inventory management, payroll, and financial reporting. SPSS and Minitab are statistical analysis software, while Excel is a general-purpose spreadsheet tool that can be used for accounting but is not a dedicated accounting package.""",
            },
            {
                "num": "28",
                "question": "An accountant prepared trial balance for ………………",
                "marks": "1",
                "answer": """<b>Correct Answer: d) Examining the arithmetical accuracy of the books of account.</b><br/>
A trial balance is prepared primarily to verify the <b>arithmetical accuracy</b> of ledger accounts. It ensures that total debits equal total credits. While it helps show balances and completes the accounting process, its fundamental purpose is to detect errors in posting, casting, and balancing of accounts.""",
            },
            {
                "num": "29",
                "question": "Who prepared the cash book?",
                "marks": "1",
                "answer": """<b>Correct Answer: c) Accountant of the business</b><br/>
The <b>cash book</b> is a special journal that records all cash receipts and cash payments. It is prepared and maintained by the accountant of the business as part of the daily bookkeeping process. It serves as both a journal and a ledger for cash transactions.""",
            },
            {
                "num": "30",
                "question": "A company is known as an artificial person because",
                "marks": "1",
                "answer": """<b>Correct Answer: c) It has rights and duties as a natural person.</b><br/>
A company is considered an <b>artificial person</b> in the eyes of law because it has a separate legal identity, can own property, enter into contracts, sue and be sued, and has rights and duties similar to a natural person. It exists independently of its shareholders and continues despite changes in ownership.""",
            },
            {
                "num": "31",
                "question": "Thapa purchased goods of Rs.60,000 from Karim on cash, which journal entry is recorded in the account book of Thapa?",
                "marks": "1",
                "answer": """<b>Correct Answer: b) Purchase A/C ……Dr Rs.60,000 To Cash Rs.60,000</b><br/>
When goods are purchased for cash, the <b>Purchase Account</b> is debited (increase in expense/purchases) and the <b>Cash Account</b> is credited (decrease in asset). Since the transaction is on cash, Karim's account is not involved — only cash goes out and purchases come in.""",
            },
            {
                "num": "32",
                "question": "The total amount of purchase book showed Rs.2,00,000 is transfer into",
                "marks": "1",
                "answer": """<b>Correct Answer: b) Debit side of purchase account</b><br/>
The purchase book (or purchases journal) records credit purchases of goods. At the end of the period, the total is transferred to the <b>debit side of the Purchase Account</b> in the ledger. This follows the rule: debit what comes in (goods purchased for resale).""",
            },
            {
                "num": "33",
                "question": "A company issued shares of Rs. 100 each, but the money is called Rs. 30 on application, Rs. 40 on allotment, and Rs.40 final call. How much money is premium per share?",
                "marks": "1",
                "answer": """<b>Correct Answer: b) Rs. 10</b><br/>
Face value of share = Rs. 100<br/>
Total called up = Rs. 30 (application) + Rs. 40 (allotment) + Rs. 40 (final call) = Rs. 110<br/>
Share premium = Total called up - Face value = Rs. 110 - Rs. 100 = <b>Rs. 10 per share</b>.<br/>
Share premium represents the excess amount received over the face value of shares.""",
            },
            {
                "num": "34",
                "question": "What is the value of closing stock under FIFO method? Purchase 3,000 @ Rs.20 per units on 1st January, Issued 500 units on 10 January, again 23 January purchase 1500 units @Rs.22 per unit. On January 30, issue 2000 units.",
                "marks": "1",
                "answer": """<b>Correct Answer: a) Rs. 43,000</b><br/>
Under <b>FIFO (First In First Out)</b>, the oldest inventory is issued first.<br/>
• Jan 1: Purchase 3,000 units @ Rs.20 = Rs.60,000<br/>
• Jan 10: Issue 500 units from first batch @ Rs.20 = Rs.10,000. Balance: 2,500 @ Rs.20 = Rs.50,000<br/>
• Jan 23: Purchase 1,500 units @ Rs.22 = Rs.33,000. Balance: 2,500 @ Rs.20 + 1,500 @ Rs.22<br/>
• Jan 30: Issue 2,000 units — first 2,000 from oldest batch @ Rs.20 = Rs.40,000<br/>
Remaining stock: 500 @ Rs.20 + 1,500 @ Rs.22 = Rs.10,000 + Rs.33,000 = <b>Rs. 43,000</b>""",
            },
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5 = 30] — Note: Some questions in this group were incomplete in the source PDF.",
        "questions": [
            {
                "num": "35",
                "question": "Define accounting. What are its functions?",
                "marks": "1+4",
                "answer": """<b>Definition of Accounting:</b><br/>
Accounting is the systematic process of identifying, recording, classifying, summarizing, interpreting, and communicating financial information about a business entity to interested users such as owners, investors, creditors, and government authorities.<br/><br/>

<b>Functions of Accounting:</b><br/>
1. <b>Identifying Financial Transactions:</b> Determining which events qualify as financial transactions that should be recorded.<br/>
2. <b>Recording:</b> Systematically documenting transactions in books of original entry (journals) in chronological order.<br/>
3. <b>Classifying:</b> Grouping similar transactions into ledger accounts under appropriate heads (assets, liabilities, income, expenses).<br/>
4. <b>Summarizing:</b> Preparing trial balance, trading account, profit and loss account, and balance sheet to present financial position.<br/>
5. <b>Analyzing and Interpreting:</b> Evaluating financial data to determine profitability, solvency, and operational efficiency through ratio analysis and trends.<br/>
6. <b>Communicating:</b> Presenting financial information to stakeholders through reports and statements for decision-making purposes.""",
            },
            {
                "num": "36",
                "question": "Following transactions relating to a business were given to you 31st November 2018. On 30th Chaitra, the cash book showed debit balance Rs. 16,000. Required: Bank reconciliation statement.",
                "marks": "5",
                "answer": """<b>Bank Reconciliation Statement as on 31st November 2018</b><br/><br/>

Given data (as visible in the source):<br/>
a. Balance as per cash book: Rs.35,000<br/>
b. Cheque issued for payment but not presented at bank: Rs.5,000<br/>
c. Cheque sent for collection at bank but not credited by the bank: Rs.15,000<br/>
d. A customer directly deposited Rs.10,000 to the bank but not recorded in cash book<br/>
e. The bank has paid electricity bill of Rs.4,000 under pre-approval from the firm but not recorded in cash book<br/><br/>

<table border='1' cellpadding='4'>
<tr><td><b>Particulars</b></td><td><b>Amount (Rs.)</b></td><td><b>Amount (Rs.)</b></td></tr>
<tr><td>Balance as per Cash Book</td><td></td><td>35,000</td></tr>
<tr><td>Add: Cheque issued but not presented</td><td>5,000</td><td></td></tr>
<tr><td>Add: Direct deposit by customer not recorded</td><td>10,000</td><td>15,000</td></tr>
<tr><td></td><td></td><td>50,000</td></tr>
<tr><td>Less: Cheque deposited but not credited</td><td>15,000</td><td></td></tr>
<tr><td>Less: Bank paid electricity bill not recorded</td><td>4,000</td><td>19,000</td></tr>
<tr><td><b>Balance as per Pass Book</b></td><td></td><td><b>31,000</b></td></tr>
</table><br/><br/>

<b>Note:</b> The reference to "Rs.16,000 debit balance" and "31st November" may contain typographical errors in the original paper (November has 30 days; Chaitra is a Nepali month). The solution above uses the reconciling items clearly listed in the question.""",
            },
            {
                "num": "13",
                "question": "The following information were provided to you by Gurung Suppliers Mahendra Pool. Prepare Sales Book. 1 Nov 2018: sales to Shrestha store — 50 bags Mansuli rice @ Rs.2,000, 30 bags Pokharali masino rice @ Rs.2,500, 70 bags Onion @ Rs.1,500. 15 Nov: sales to Bindabasini store — 30 bags potato @ Rs.1,000, 10 bags Sugar @ Rs.3,000 (Trade discount 10%)",
                "marks": "5",
                "answer": """<b>Sales Book of Gurung Suppliers</b><br/><br/>

<b>1 November 2018 — Shrestha Store, Birauta</b><br/>
<table border='1' cellpadding='4'>
<tr><td>Particulars</td><td>Qty</td><td>Rate</td><td>Amount (Rs.)</td></tr>
<tr><td>50 bags Mansuli rice</td><td>50</td><td>2,000</td><td>1,00,000</td></tr>
<tr><td>30 bags Pokharali masino rice</td><td>30</td><td>2,500</td><td>75,000</td></tr>
<tr><td>70 bags Onion</td><td>70</td><td>1,500</td><td>1,05,000</td></tr>
<tr><td colspan='3'><b>Total</b></td><td><b>2,80,000</b></td></tr>
</table><br/><br/>

<b>15 November 2018 — Bindabasini Store, Bagar</b><br/>
<table border='1' cellpadding='4'>
<tr><td>Particulars</td><td>Qty</td><td>Rate</td><td>Amount (Rs.)</td></tr>
<tr><td>30 bags Potato</td><td>30</td><td>1,000</td><td>30,000</td></tr>
<tr><td>10 bags Sugar</td><td>10</td><td>3,000</td><td>30,000</td></tr>
<tr><td colspan='3'>Gross Amount</td><td>60,000</td></tr>
<tr><td colspan='3'>Less: Trade Discount @ 10%</td><td>6,000</td></tr>
<tr><td colspan='3'><b>Net Amount</b></td><td><b>54,000</b></td></tr>
</table><br/><br/>

<b>Sales Book Summary</b><br/>
<table border='1' cellpadding='4'>
<tr><td>Date</td><td>Buyer</td><td>Amount (Rs.)</td></tr>
<tr><td>1 Nov 2018</td><td>Shrestha Store</td><td>2,80,000</td></tr>
<tr><td>15 Nov 2018</td><td>Bindabasini Store</td><td>54,000</td></tr>
<tr><td colspan='2'><b>Total Sales for the period</b></td><td><b>3,34,000</b></td></tr>
</table><br/><br/>

<b>Journal Entry:</b><br/>
Shrestha Store A/c Dr. Rs.2,80,000<br/>
Bindabasini Store A/c Dr. Rs.54,000<br/>
&nbsp;&nbsp;&nbsp;&nbsp;To Sales A/c Rs.3,34,000<br/>
(Being goods sold on credit as per Sales Book)""",
            },
        ]
    }
]

if __name__ == "__main__":
    generate_answer_sheet(
        subject_code="CACS152",
        subject_slug="financial-accounting",
        subject_name="Financial Accounting",
        year=2018,
        semester_slug="semester-2",
        questions_data=QUESTIONS_DATA
    )
    print("Answer sheet generation complete for CACS152 2018!")
