import json

# Load the JSON data and extract the value to compare
json_file_path = 'C:/Users/STS546-RAGHUL S/Documents/TBS Tool/JSON_file - TBS.json'
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

value_to_compare_taxyear = json_data['submissionDetails']['taxYear']
value_to_compare_tin = json_data['returnData']['business']['tin']
original_string_tin = value_to_compare_tin.replace('-', '')
#print(original_string)
value_to_compare_Businessnamectrl = json_data['returnData']['business']['businessNm']
uppercase_string = value_to_compare_Businessnamectrl.upper()
#print(uppercase_string)
trimmed_string = uppercase_string[:4]
#print(trimmed_string)
value_to_compare_formtype = json_data['returnData']['formType']
trimmed_string_formtype = value_to_compare_formtype.strip('FORM1099')
#print(trimmed_string_formtype)
value_to_compare_Businessname = json_data['returnData']['business']['businessNm']
uppercase_string = value_to_compare_Businessname.upper()
#print(uppercase_string)
value_to_compare_address1 = json_data['returnData']["business"]['usAddress']['address1']
uppercase_string_address1 = value_to_compare_address1.upper()
#print(uppercase_string_address1)
value_to_compare_address2 = json_data['returnData']["business"]['usAddress']['city']
uppercase_string_address2 = value_to_compare_address2.upper()
#print(uppercase_string_address2)
value_to_compare_state = json_data['returnData']["business"]['usAddress']['state']
uppercase_string_state = value_to_compare_state.upper()
#print(value_to_compare_state)
value_to_compare_zipcode = json_data['returnData']["business"]['usAddress']['zipCd']
uppercase_string_zipcode = value_to_compare_zipcode.upper()
#print(value_to_compare_state)
value_to_compare_phone = json_data['returnData']["business"]['phone']
#characters_to_remove_phone = "(), -"
#trimmed_string_phone = value_to_compare_phone.strip('(')(")")(',')
#print(trimmed_string_phone)


# Read the content of the text file
text_file_path = 'C:/Users/STS546-RAGHUL S/Documents/TBS Tool/SPAN.FIRE.TEST.ORG.228.0004.txt'
with open(text_file_path, 'r') as text_file:
    text_content = text_file.read()

# Define the position from which you want to read the value
positions = [1, 752, 1503]  # Replace with the desired position
position_2 = 762
position_3 = 771
position_4 = 776
position_5 = 803
position_6 = 884
position_7 = 924
position_8 = 964
position_9 = 966
position_10 = 975
# Define the length of the value to read
value_length = 4  # Replace with the length of the value you want to read
value_length_2 = 9
value_length_3 = 4
value_length_4 = 2
value_length_5 = 16
value_length_6 = 11
value_length_7 = 8
value_length_8 = 2
value_length_9 = 5
value_length_10 = 10

# Iterate through positions and read values from the text content
#Tax Year
for position in positions:
    if position + value_length <= len(text_content):
# Read the value from the text content at the specified position
      read_value = text_content[position : position + value_length]
      print(read_value)

      if value_to_compare_taxyear == read_value:
         print(f'Is Matched')
      else:
         print(f'Is Not Matched')
         
#TIN
position=position_2
read_value_2 = text_content[position : position + value_length_2]
print(read_value_2)

if original_string_tin == read_value_2:
    print(f'Is Matched')
else:
    print(f'Is Not Matched')

#Businessname
position=position_3
read_value_3 = text_content[position : position + value_length_3]
print(read_value_3)

if trimmed_string == read_value_3:
    print(f'Is Matched')
else:
    print(f'Is Not Matched')


#formtype
position=position_4
read_value_4 = text_content[position : position + value_length_4]
text = (trimmed_string_formtype)
print(text)
if "NE" in text:
    print(f'Is Matched')
else:
    print(f'Is Not Matched')


#FirstIssuerName
position=position_5
read_value_5 = text_content[position : position + value_length_5]
print(read_value_5)

if uppercase_string == read_value_5:
    print(f'Is Matched')
else:
    print(f'Is Not Matched')


#address1
position=position_6
read_value_6 = text_content[position : position + value_length_6]
print(read_value_6)

if uppercase_string_address1 == read_value_6:
    print(f'Is Matched')
else:
    print(f'Is Not Matched')


#state
position=position_7
read_value_7 = text_content[position : position + value_length_7]
print(read_value_7)

if uppercase_string_address2 == read_value_7:
    print(f'Is Matched')
else:
    print(f'Is Not Matched')


#state
position=position_8
read_value_8 = text_content[position : position + value_length_8]
print(read_value_8)

if uppercase_string_state == read_value_8:
    print(f'Is Matched')
else:
    print(f'Is Not Matched')


#zipcode
position=position_9
read_value_9 = text_content[position : position + value_length_9]
print(read_value_9)

if uppercase_string_zipcode == read_value_9:
    print(f'Is Matched')
else:
    print(f'Is Not Matched')


#phone
position=position_10
read_value_10 = text_content[position : position + value_length_10]
print(read_value_10)

#if trimmed_string_phone == read_value_10:
#    print(f'Is Matched')
#else:
#    print(f'Is Not Matched')