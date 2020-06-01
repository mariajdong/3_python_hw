#import modules
import os
import csv
from datetime import datetime

#state abbreviation dictionary, https://gist.github.com/rogerallen/1583593
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
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
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

#define lists
e_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

#specify employee csv path
bosspath = os.path.join ("resources", "employee_data.csv")

#read employee csv file
with open (bosspath) as bossfile:
    bossreader = csv.reader (bossfile, delimiter = ',')
    
    #specify header
    bossheader = next (bossreader)

    #begin loop through rows, populate respective lists
    for row in bossreader:
        e_id.append (row[0])

        #split full name into first and last
        first_last = row[1].split (" ", 1)
        first_name.append (first_last[0])
        last_name.append (first_last[1])

        #convert DOB format
        new_dob = datetime.strptime (row[2], '%Y-%m-%d')
        dob.append (new_dob.strftime('%m/%d/%Y'))

        #hide SSN digits (other than last 4)
        full_ssn = (row[3])
        new_ssn = "***-**-" + full_ssn[-4:]
        ssn.append (new_ssn)

        #convert states to abbreviated form
        if row[4] in us_state_abbrev:
            state.append (us_state_abbrev[row[4]])

#zip lists as tuples
zip_data = zip (e_id, first_name, last_name, dob, ssn, state)

#export info to new csv file
employee_output = "resources/updated_employee_data.csv"

#write contents to csv file w/ header
with open (employee_output, 'w', newline = '') as employeefile:
    bosswriter = csv.writer (employeefile)
    bosswriter.writerow (['employee ID', 'name', 'DOB', 'SSN', 'state'])
    bosswriter.writerows (zip_data)