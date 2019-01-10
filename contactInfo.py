class ContactInfo:
    def __init__(self, name, phone, email):
        self.n = name
        self.p = phone
        self.e = email

    def getName(self):
        return self.n

    def getPhoneNumber(self):
        return self.p

    def getEmailAddress(self):
        return self.e

    def printInfo(self):
        print('Name:\t\t{}'.format(self.n))
        print('Phone Number:\t{}'.format(self.p))
        print('Email Address:\t{}\n'.format(self.e))