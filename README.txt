This  is the technical developer test  work by Van Quang Nguyen and this is the instructions how to run my codes for this test

First, download and install the latest  version of Python from the official website or from the microsoft store.

Next, download the entire folder of Van_Quang_Nguyen_triangle_test  into your documents folder of  your computer.

Afterwards. navigate to the Van_Quang_Nguyen_triangle_test from the command prompt 

Then, run the program from  the command prompt by typing in: python main.py
it will print out these messages 
Enter 'EXIT' to close program
Enter file name:

finally, type in data_testing in order to get the result and it will create a brand new csv file.
you can open up the file directly  and it will open microsoft excel.

also, the terminal will print out this message:
Your file contains an error on line -  14  -  []
Only the first four indexes will be used.


list index out of range
Comp [0, 0, 0, 0, 0, 0, 0, 110.0, 280.0, 200.0]
Non-Comp [45.2, 110.0, 110.0, 147.0, 50.0, 125.0, 150.0, 55.0, 140.0, 100.0]


Result_File_data_testing.csv Created, Check your directory!













One of the major jobs that we do is claims reserving, which involves assessing how much money is likely to be paid in future in respect of the claims that arise from a set of insurance policies that have already been taken out. The statistical analysis of this is based around triangles of payment figures for previous claims.

A very simple example triangle might look like this (the triangle is the shaded bit):


| Incremental Claims Data | Development Year |
| --- | --- |
| 1 | 2 | 3 |
| Origin Year | 1995 | 100 | 50 | 200 |
| 1996 | 80 | 40 | ? |
| 1997 | 120 | ? | ? |



The numbers in the triangle are the amounts of payments made in respect of claims on a particular block of insurance policies.

The block of claims will be broken into origin years. For example, all claims originally happening in 1996 will go into the 1996 row of the triangle.

For each origin year grouping of claims we will see development of payments over time as settlements are made. In the example above we see that payments of 100 were made in respect or origin year 1995 during the year 1995, 50 during the year 1996 (development year 2) and 200 during 1997 (development year 3). At the end of 1997 the total of claim payments in respect of origin year 1995 is 350 = 100 + 50 + 200.

The purpose of the triangle is to try to estimate what numbers should go in the empty boxes (the ones with question marks in them) by looking at the patterns in the triangle – the numbers in the empty boxes are the amounts we expect to have to pay in the future in respect of the claims that occurred in 1996 and 1997.

To do this in practice, it is easier to spot patterns if we &#39;accumulate&#39; the data in the triangle, so that rather than showing the amount paid in any particular development year, it shows the total amount paid in all development years up to and including the one we&#39;re looking at.

The accumulated version of the above triangle is:


| Cumulative Claims Data | Development Year |
| --- | --- |
| 1 | 2 | 3 |
| Origin Year | 1995 | 100 | 150 (=100+50) | 350 (=150+200) |
| 1996 | 80 | 120 (=80+40) | ? |
| 1997 | 120 | ? | ? |



**The Problem**

You are required to create a program to read in incremental payment data from a comma-separated text file, to accumulate the data and to output the results to a different comma-separated text file. This process represents the creation of the cumulative data triangle from the incremental data triangle above.


Example Input Data

A short input file might contain the following:

Product, Origin Year, Development Year, Incremental Value
Comp, 1992, 1992, 110.0
Comp, 1992, 1993, 170.0
Comp, 1993, 1993, 200.0
Comp, 1993, 1993, 200.0
Non-Comp, 1990, 1990, 45.2
Non-Comp, 1990, 1991, 64.8
Non-Comp, 1990, 1993, 37.0
Non-Comp, 1991, 1991, 50.0
Non-Comp, 1991, 1992, 75.0
Non-Comp, 1991, 1993, 25.0
Non-Comp, 1992, 1992, 55.0
Non-Comp, 1992, 1993, 85.0
Non-Comp, 1993, 1993, 100.0

This example file contains _two_ triangles – one for a product called &#39;Comp&#39; and one for a product called &#39;Non-Comp&#39;. The first row contains column headings, and the subsequent rows contain the data, so, for example, for accidents occurring on the Non-Comp product in 1990, 45.2 was paid in 1990, 64.8 was paid in 1991 and 37 was paid in 1993.

The output file corresponding to the above input file would be:

1990, 4
Comp, 0, 0, 0, 0, 0, 0, 0, 110, 280, 200
Non-Comp, 45.2, 110, 110, 147, 50, 125, 150, 55, 140, 100

The first line gives the earliest origin year (i.e. 1990) and the number of development years (in this case ranging from 1990 through to 1993 i.e. 4).

After the first line, there is a line for each triangle. The first field in the line gives the name of the product. The subsequent fields are the accumulated triangle values.
