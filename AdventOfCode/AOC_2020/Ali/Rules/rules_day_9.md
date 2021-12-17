<h1>--- Day 9: Encoding Error ---</h1>

# Part 1
With your neighbor happily enjoying their video game, you turn your attention to an open data port on the little screen in the seat in front of you.

Though the port is non-standard, you manage to connect it to your computer through the clever use of several paperclips. Upon connection, the port outputs a series of numbers (your puzzle input).

The data appears to be encrypted with the eXchange-Masking Addition System (XMAS) which, conveniently for you, is an old cypher with an important weakness.

XMAS starts by transmitting a **preamble** of 25 numbers. After that, each number you receive should be the sum of any two of the 25 immediately previous numbers. The two numbers will have different values, and there might be more than one such pair.

For example, suppose your preamble consists of the numbers 1 through 25 in a random order. To be valid, the next number must be the sum of two of those numbers:

-  <code>_**26**_</code> would be a **valid** next number, as it could be 1 plus <code>_**25**_</code> (or many other pairs, like <code>_**2**_</code> and <code>_**24**_</code>).
- <code>_**49**_</code> would be a **valid** next number, as it is the sum of <code>_**24**_</code> and <code>_**25**_</code>.
- <code>_**100**_</code> would not be **valid**; no two of the previous <code>_**25**_</code> numbers sum to <code>_**100**_</code>.
- <code>_**50**_</code> would also not be **valid**; although <code>_**25**_</code> appears in the previous <code>_**25**_</code> numbers, the two numbers in the pair must be different.



Suppose the 26th number is <code>_**45**_</code>, and the first number (no longer an option, as it is more than 25 numbers ago) was <code>_**20**_</code>. Now, for the next number to be valid, there needs to be some pair of numbers among <code>_**1-19**_</code>, <code>_**21-25**_</code>, or <code>_**45**_</code> that add up to it:

- 26 would still be a valid next number, as 1 and 25 are still within the previous 25 numbers.
- 65 would not be valid, as no two of the available numbers sum to it.
- 64 and 66 would both be valid, as they are the result of 19+45 and 21+45 respectively.

Here is a larger example which only considers the previous 5 numbers (and has a preamble of length 5):

    35 
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576

In this example, after the 5-number preamble, almost every number is the sum of two of the previous 5 numbers; the only number that does not follow this rule is <code>_**127**_</code>.

The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it. 

**What is the first number that does not have this property?**

<code><h3>**PART 1 Answer: ____**h3</code>

# Part 2
