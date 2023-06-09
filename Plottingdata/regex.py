import re

# Example exported PDF data
pdf_data = """
Tue, 08:00AM-12:00PM
Wks 30-39, 41-50 (S2), 
18/07/2023 ... 5/12/2023 
[=20]
Lecture
MHS-Health Services 
MURUnits: BSBMED301_1_2023_MH_S2_2 (Interpret and apply m edical terminology appropriately)
BSBWOR301_1_2023_MH_S2_2 (Organise personal work priorities and development)
CHCCCS002_1_2023_MH_S2_2 (Assist with movement)
...
Rooms: MH.D.D5.SPEC (MH-Murdoch Campus)
Staff: Augustine,Betty
ID: 1778982
Notes: HLT33115-AA72 Cert III Health Svc Asst (Acute Care) -FT-Local-Gp1;
"""

# Define regular expressions to extract information
day_time_pattern = r"([A-Za-z]+), (\d{2}:\d{2}(?:AM|PM)-\d{2}:\d{2}(?:AM|PM))"
weeks_pattern = r"Wks (\d+(?:-\d+)?(?:, \d+(?:-\d+)?)*)(?: \((S\d+)\))?"
dates_pattern = r"(\d{2}/\d{2}/\d{4}) \.\.\. (\d{1,2}/\d{2}/\d{4})"
duration_pattern = r"\[=(\d+)\]"
lecture_pattern = r"Lecture\n(.*?)\n"
units_pattern = r"MURUnits: (.*?)\n"
rooms_pattern = r"Rooms: (.*?)\n"
staff_pattern = r"Staff: (.*?)\n"
id_pattern = r"ID: (\d+)\n"
notes_pattern = r"Notes: (.*)"

# Create an empty dictionary to store the extracted data
data_dict = {}

# Extract the information using regular expressions
day_time_match = re.search(day_time_pattern, pdf_data)
weeks_match = re.search(weeks_pattern, pdf_data)
dates_match = re.search(dates_pattern, pdf_data)
duration_match = re.search(duration_pattern, pdf_data)
lecture_match = re.search(lecture_pattern, pdf_data)
units_match = re.search(units_pattern, pdf_data)
rooms_match = re.search(rooms_pattern, pdf_data)
staff_match = re.search(staff_pattern, pdf_data)
id_match = re.search(id_pattern, pdf_data)
notes_match = re.search(notes_pattern, pdf_data)

# Store the extracted data in the dictionary
data_dict["Day"] = day_time_match.group(1) if day_time_match else None
data_dict["Time"] = day_time_match.group(2) if day_time_match else None
data_dict["Weeks"] = weeks_match.group(1) if weeks_match else None
data_dict["Semester"] = weeks_match.group(2) if weeks_match else None
data_dict["Start Date"] = dates_match.group(1) if dates_match else None
data_dict["End Date"] = dates_match.group(2) if dates_match else None
data_dict["Duration"] = duration_match.group(1) if duration_match else None
data_dict["Lecture"] = lecture_match.group(1) if lecture_match else None
data_dict["Units"] = units_match
