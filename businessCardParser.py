import re
from contactInfo import ContactInfo

# Characters to replace in phone number
chars = ['+','-','(',')',':',' ']

class BusinessCardParser:
    def getContactInfo(document):
        name, phone, email = "", "", ""

        with open(document, 'r') as card:
            info = [line.strip() for line in card]
        
        # Check lines for the necessary info
        for line in info:
            # TODO: figure out how to get name
            if():
                name = "test"
            
            # Check if phone number format, and strip to just numbers
            if(re.search("^[(]|^\d|^Phone:|^Tel:", line)):
                # Remove unecessary characters and/or strings from phone number
                for c in chars:
                    line = line.replace(c, '')
                phone = re.sub('Phone|Tel', '', line)

            # Check to see if email
            if "@" in line:
                email = line
            
        return ContactInfo(name, phone, email)