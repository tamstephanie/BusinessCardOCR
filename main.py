import glob
from businessCardParser import BusinessCardParser

def main():
    # Get all business cards, assuming they follow that naming format
    cards = glob.glob('card*.txt')
    
    # Print contact info from the cards
    for card in cards:
        contactInfo = BusinessCardParser.getContactInfo(card)
        contactInfo.printInfo()

if __name__ == "__main__": main()