# Asymmetrik Programming Challenge
## Business Card OCR
We’ve created a new smartphone app that enables users to snap a photo of a business card and have the information from the card automatically extracted and added to their contact list. We need you to write the component that parses the results of the optical character recognition (OCR) component in order to extract the __name, phone number,__ and __email address__ from the processed business card image.

For the challenge, we need you to build a command line tool or graphical user interface that takes the business card text as input and outputs the Name, Phone, and Email Address of the owner of the business card. We have provided you with an interface specification [1] that we’d like you to implement, as well as a series of example test cases [2].

### Build
1. Download the files from the repository[https://github.com/tamstephanie/BusinessCardOCR]
2. Install Python 3 (the latest version)

### Run & Test
To run and test the program, you only need to run the following command:
```
python3 main.py
```

### Notes
- The business cards are input as text files, rather than terminal input due to more complex nature of multi-line input in the terminal. (Hopefully this is acceptable, since I did not think of this until later.)
- In the future, maybe instead of using regular expressions, I would consider using NLP for detection