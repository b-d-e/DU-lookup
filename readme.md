# What is this?
This is a simple python script which utilises the [Durham University API](api.dur.ac.uk) to convert a list of names to a list of corresponding email addresses.

# How to use

Call from the command line with **python main.py [file of names] [file of basic auth credentials]**.

The arguments should both link to .txt files.
The members file should have a list of the names you want to lookup seperated by new lines.
The auth file should have your CIS username (e.g. abcd12) on the first line and your CIS password on the second line.

The program will store the result to a .txt file named 'emails.csv'. It will consist of a collection of emails, each separated by a new line.

If there are no corresponding names in the Durham directory, the corresponding line in emails.csv will read 'Error - No matches found'. If there are multiple people returned for the queried name the file will read 'Error - Multiple matches found'.

# API Quotas
https://api.dur.ac.uk is rate limited to a maximum of 5000 requests per hour. Please ensure your inputted list of names does not exceed 5000 lines.