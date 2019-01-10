import re
from contactInfo import ContactInfo

# Characters to replace in phone number
chars = ['+','-','(',')',':',' ']

class BusinessCardParser:
    def getContactInfo(document):
        name, phone, email = "", "", ""

        with open(document, 'r') as card:
            info = [line.strip() for line in card]
        
        # Check business card for the necessary info
        for line in info:
            # Search card for person's name
            if not any(value in line for value in ("Software", "Engineer", "Developer", "Technologies", "Ltd", "@", ",")):
                if(re.search("^[A-Z][a-z]+(-[A-Z][a-z]+)?\s[A-Z][a-z]+", line)):
                    name = line
                    
            # Search for phone number & just get the numbers
            if(re.search("^[(]|^\d|^Phone:|^Tel:", line)):
                # Remove unecessary characters and/or strings from phone number
                for c in chars:
                    line = line.replace(c, '')
                phone = re.sub('Phone|Tel', '', line)
            
            # Search card for email address
            if "@" in line:
                email = line
            
        return ContactInfo(name, phone, email)