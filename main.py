# imports
import requests
import csv
import sys

def lookupMember(nameParam, auth):
    # a function to make a request to the api for a given members name
    URL = "http://api.dur.ac.uk/directory/search"
    PARAMS = {'name':nameParam}

    r = requests.get(url = URL, params = PARAMS, auth = (auth[0].rstrip(), auth[1].rstrip())) 
    data = r.json() 
    if data == []:
        return "Error - No matches found"
    if data=={'code': 'BadRequestError', 'message': 'Conditions return too many results'} or len(data) > 1:
        return "Error - Multiple matches found"
    else:
        return(data[0].get('contacts')[0].get('email'))


def main():
    # reads command line arguments
    authName = sys.argv[2]
    membersName = sys.argv[1]

    # reads files
    authFile = open(authName, "r")
    auth = authFile.readlines()
    authFile.close()

    membersFile = open(membersName, "r")
    members = membersFile.readlines()
    membersFile.close()

    # initialises variables
    emails = []
    i=1
    total = len(members)

    # iterates through members and looks up each of them
    for m in members:
        m = m.rstrip()
        print("Lookup:     "+str(i)+"/"+str(total))
        result = lookupMember(m, auth)
        emails.append(result)
        print(m+":     "+result)
        i = i+1

    # writes results to a file
    rows = zip(emails)
    with open("emails.csv", "w") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

main()