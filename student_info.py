
# Author name: Jeremiah E. Ochepo
# Code discription: Class and function and Inheritance
# Last Updated Date: 8/26/19

def horizontal_line(line_length):
    for _ in range(line_length):
        print('___', end="")
    print('__')


class Student:
    def __init__(self, firstName, middleName, lastName, age, idNumber, phoneNumber, home_address):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.age = age
        self.idNumber = idNumber
        self.phoneNumber = phoneNumber
        self.home_address = home_address

    def view_student_info(self):
        print('\nStudent Information:')
        full_name = f"{self.firstName} {self.middleName} {self.lastName}"
        output = f"Full Name: {full_name.title()}"
        output += f"\nAge: {self.age} Years"
        output += f"\nID Number: {self.idNumber.title()}"
        output += f"\nPhone Number: +1{self.phoneNumber}"
        output += f"\nE-mail Address: {self.lastName}_{self.firstName}@roberts.edu"
        output += f"\nHome Address: {self.home_address.title()}"
        return output


class StudentTranscript(Student):
    def __init__(self, firstName, middleName, lastName, age, idNumber, phoneNumber, home_address, major, crd_num, ov_gpa):
        super().__init__(firstName, middleName, lastName, age, idNumber, phoneNumber, home_address)

        self.my_major = major
        self.credit_number = crd_num
        self.overall_gpa = ov_gpa

    def view_student_transcript(self):
        horizontal_line(24)
        print('Student Transcript:')
        output = f"Major: {self.my_major}"
        output += f"\nCredit Number: {self.credit_number} Credits"
        output += f"\nOverall GPA: {self.overall_gpa} point"
        return output


def main():
    print("Enter Student Information:")
    firstName = input("First Name: ")
    middleName = input("Middle Name: ")
    lastName = input("Last Name: ")
    age = int(input("Age: "))
    idNumber = input("ID Number: ")
    phoneNumber = int(input("Phone Number: "))
    home_address = input("Home Address: ")

    print("\nEnter Academic Information:")
    my_major = input("Major: ")
    credit_number = int(input("Credit Number: "))
    overall_gpa = float(input("Overall GPA: "))

    student_info = StudentTranscript(firstName, middleName, lastName, age, idNumber, phoneNumber, home_address, my_major, credit_number, overall_gpa)

    print(student_info.view_student_info())
    print(student_info.view_student_transcript())


if __name__ == "__main__":
    main()
