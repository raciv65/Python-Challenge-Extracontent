import os
import csv
import datetime

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

DataFile=os.path.join("Resources","employee_data.csv")

EmployeeIDdata=[]
NameData=[]
DOBdata=[]
SNNdata=[]
StateData=[]

with open(DataFile, "r", encoding="UTF-8") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    headers=next(csvreader)
    for row in csvreader:
        EmployeeIDdata.append(row[0])
        NameData.append(row[1].split(" "))
        DOBdata.append(row[2].split('-'))
        SNNdata.append(row[3].split('-'))
        StateData.append(us_state_abbrev[row[4]])

FirstName=[name[0] for name in NameData]
LastName=[name[1] for name in NameData]


DOB=[]
for date in DOBdata:
    time=datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
    timeStr=time.strftime('%m/%d/%Y')
    DOB.append(timeStr)

SNN=['xxx-xx-'+str(ssn[2]) for ssn in SNNdata]

NewData=sorted(zip(EmployeeIDdata,FirstName,LastName,DOB,SNN,StateData), key=lambda x:x[0])

SaveFile=os.path.join("Analysis","Employee Data.csv")

with open(SaveFile, "w", newline='', encoding="UTF-8") as datafile:
    csvwriter=csv.writer(datafile, delimiter=',')
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SNN','State'])
    csvwriter.writerows(NewData)
