class msg():
    def upper(self, message):
        self.message = message
        return self.message

# m = "123"
# m = 123
# m = msg.upper("123")
m = msg.upper(int("123"))
# m = int(input("Message: "))

def encrypt_message(message):
    # encrypted_message = ""
    upper_case_message = ""
    upper_case_message = message.upper()
    print(upper_case_message)

encrypt_message(m)

