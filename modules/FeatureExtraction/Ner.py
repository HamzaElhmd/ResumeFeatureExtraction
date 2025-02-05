from test.TestOcr import pdf_to_text
import os
import re
from sklearn.preprocessing import LabelEncoder
import joblib

def load_cv_text(idx):
        # Get list of CV files from the 'CVs' directory
        cv_files = os.listdir('CVs')
        content = None

        # Open a CV file and read bytes content
        with open('CVs/'+cv_files[idx], "rb") as cv_file:
                content = cv_file.read()

        # Use predefine pdf_to_text function to parse PDF bytes into raw text
        return pdf_to_text(pdf_file=content, filename=cv_files[idx])


def normalize(full_name_parts):
    unique_list = []
    long_str = " ".join(full_name_parts)
    tokens = [str.upper() for str in long_str.split(" ")]

    for el in tokens:
        if len(el) > 3:
            # Check if the token is part of any existing name
            if not any(el in name for name in unique_list) and not any(name in el for name in unique_list):
                unique_list.append(el)

    return list(dict.fromkeys(unique_list))

def get_full_name(text, ner):
	# Run the pipeline and get the entities from the raw text
	entities = ner(text)
	full_name_parts = []

	idx = 0
	for entity in entities:
		if entity['entity_group'] == 'PER':
			word = entity['word']
			word = re.sub('[▁]', '', word)
			full_name_parts.append(word)

	full_name = " ".join(normalize(full_name_parts))
	print(full_name)
	return full_name

def get_email(text):
	email_rgx_err = r"([A-Za-z0-9._%+-]+[=]?)[A-Za-z0-9.-]+(\.[A-Za-z]{2,})" 
	email_rgx =  r"[A-Za-z0-9.-_]+@[a-zA-Z-]+.[a-zA-Z]+"

	email_matcher = re.compile(email_rgx)
	email_match = email_matcher.search(text)

	email_matcher_err = re.compile(email_rgx_err)
	email_match_err = email_matcher_err.search(text)

	if email_match is not None:
		result = email_match.group()
		print(result)
		return result
	elif email_match_err is not None:
		result =  email_match_err.group()
		print(result)
		return result
	else:
		print('no matches.')
		return None

def get_phone_number(text):
	phone_number_rgx = r"\+[0-9]+[0-9 ]+"
	phone_number_rgx_0 = r"0[0-9 ]+"

	phone_number_matcher = re.compile(phone_number_rgx)
	phone_number_match = phone_number_matcher.search(text)

	phone_number_matcher_0 = re.compile(phone_number_rgx_0)
	phone_number_match_0 = phone_number_matcher_0.search(text)

	if phone_number_match is not None:
		result = phone_number_match.group()
		print(result)
		return result
	elif phone_number_match_0 is not None:
		result = phone_number_match_0.group()
		print(result)
		return result
	else:
		print('no match')
		return None

def get_country(text, ner):
	entities = ner(text)
	country_parts = []

	for entity in entities:
		if entity['entity_group'] == 'LOC':
			word = entity['word']
			word = re.sub('▁','', word)
			country_parts.append(word)

	print(" ".join(normalize(country_parts)))

def get_experience(text, distilbert):
    output = distilbert(text)
    
    # Load the label encoder
    label_encoder = joblib.load('label_encoder.pkl')
    for entity in output:
        label_num = re.sub(r'LABEL_', '', entity['entity_group'])
        label = label_encoder.inverse_transform(np.array([int(label_num)]))[0] # Changed this line
        print(f"{entity['word']} ({label})")
