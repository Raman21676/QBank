#!/usr/bin/env python3
"""Generate answer sheet for CACS151 2021 C Programming."""

import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

# Only Group A MCQs were visible in the source PDF.
# Groups B and C appear to be missing from the extracted text.

QUESTIONS_DATA = [
    {
        "title": "Group A",
        "instruction": "Attempt all the questions. [10×1 = 10] — Note: Groups B and C were not found in the source PDF and are omitted from this answer sheet.",
        "questions": [
            {
                "num": "1",
                "question": "Among unary operation which operator represents increment?",
                "marks": "1",
                "answer": """<b>Correct Answer: b) ++</b><br/>
The <b>increment operator (++)</b> is a unary operator in C that increases the value of a variable by 1. It can be used in prefix form (++x) or postfix form (x++). The decrement operator (--) decreases a value by 1. Options -+, !+, and - - (decrement) are not correct for increment.""",
            },
            {
                "num": "2",
                "question": "If the function returns no value, then it is called……",
                "marks": "1",
                "answer": """<b>Correct Answer: d) Void function</b><br/>
A <b>void function</b> in C is a function declared with the <code>void</code> return type, meaning it does not return any value to the calling function. It performs operations but does not send back a result. Functions that return data are declared with specific data types like <code>int</code>, <code>float</code>, or <code>char</code>.""",
            },
            {
                "num": "3",
                "question": "What are the C functions used to read or write a file in Binary mode?",
                "marks": "1",
                "answer": """<b>Correct Answer: b) fread(), fwrite()</b><br/>
The <code>fread()</code> and <code>fwrite()</code> functions are used for binary file I/O in C. <code>fread()</code> reads a specified number of bytes from a binary file into memory, while <code>fwrite()</code> writes a block of data to a binary file. <code>fprintf()</code> and <code>fscanf()</code> are for text mode, and <code>getw()/putw()</code> are for reading/writing integers.""",
            },
            {
                "num": "4",
                "question": "An entire array is always passed by ……….to a called function.",
                "marks": "1",
                "answer": """<b>Correct Answer: b) call by reference</b><br/>
In C, when an array is passed to a function, what is actually passed is the <b>address of the first element</b> (a pointer). This means the array is passed by reference, not by value. Any modifications made to the array elements inside the function affect the original array in the calling function.""",
            },
            {
                "num": "5",
                "question": "What is actually passed if you pass a structure variable to a function?",
                "marks": "1",
                "answer": """<b>Correct Answer: c) Starting address of structure variable</b><br/>
When a structure variable is passed to a function, the entire structure is typically passed by value (a copy is made). However, if a pointer to the structure is passed, then the <b>starting address</b> of the structure is passed. Given the context of standard C behavior with pointers, the starting address represents the reference-passing mechanism used for efficiency with large structures.""",
            },
            {
                "num": "6",
                "question": "Choose a correct statement about C Escape Sequences.",
                "marks": "1",
                "answer": """<b>Correct Answer: d) All the above</b><br/>
All listed escape sequences are correct in C:<br/>
• <code>\\'</code> outputs a single quote<br/>
• <code>\\"</code> outputs a double quote<br/>
• <code>\\\\</code> produces one visible backslash<br/>
These are standard escape sequences defined in the C language for formatting output and handling special characters within strings and character constants.""",
            },
            {
                "num": "7",
                "question": "What is the keyword used to define a c macro?",
                "marks": "1",
                "answer": """<b>Correct Answer: c) define</b><br/>
The <code>#define</code> preprocessor directive is used to define macros in C. Macros are symbolic names for constants or code snippets that are replaced by the preprocessor before compilation. Example: <code>#define PI 3.14159</code> or <code>#define SQUARE(x) ((x)*(x))</code>. Unlike functions, macros are expanded inline.""",
            },
            {
                "num": "8",
                "question": "What is the first step in c program building process.?",
                "marks": "1",
                "answer": """<b>Correct Answer: d) Preprocessing</b><br/>
The C program building process follows this order:<br/>
1. <b>Preprocessing:</b> Handles directives like #include, #define, conditional compilation<br/>
2. <b>Compiling:</b> Translates preprocessed C code into assembly<br/>
3. <b>Assembling:</b> Converts assembly to object code (machine code)<br/>
4. <b>Linking:</b> Combines object files and libraries into executable<br/>
Therefore, preprocessing is always the first step.""",
            },
            {
                "num": "9",
                "question": "Choose a correct C statement about String functions?",
                "marks": "1",
                "answer": """<b>Correct Answer: b) strcmp(\"abc\", \"bcd\") returns a negative number</b><br/>
<code>strcmp()</code> compares strings lexicographically using ASCII values. Since 'a' (97) < 'b' (98), "abc" is less than "bcd", so it returns a negative number. Option (a) is incorrect because <code>strrev()</code> modifies in place and returns the reversed string pointer — "abcD" reversed would be "Dcba". Option (c) is wrong because "234" > "123" so <code>strcmp</code> would return positive.""",
            },
            {
                "num": "10",
                "question": "Choose a syntax for C Ternary Operator from the list.",
                "marks": "1",
                "answer": """<b>Correct Answer: a) condition? Expression1 : expression2</b><br/>
The <b>ternary operator (? :)</b> is C's conditional operator. It evaluates the condition; if true, returns Expression1, otherwise returns Expression2. Example: <code>max = (a > b) ? a : b;</code> assigns the larger of a and b to max. It is a shorthand for simple if-else statements and is right-associative.""",
            },
        ]
    }
]

if __name__ == "__main__":
    generate_answer_sheet(
        subject_code="CACS151",
        subject_slug="c-programming",
        subject_name="C Programming",
        year=2021,
        semester_slug="semester-2",
        questions_data=QUESTIONS_DATA
    )
    print("Answer sheet generation complete for CACS151 2021!")
