class Contact:
    def __init__(self,name: str, phone_number: str,email=None,address=None) -> None:
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def update_info(self,phone_number=None,email=None,address=None):
        

    def display_info(self):
        print(f"M.{self.name},who's living in {self.address}, phone number:{self.phone_number}, email: {self.email}.")
