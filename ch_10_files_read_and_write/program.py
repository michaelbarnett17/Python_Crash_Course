from my_file_reader import MyFileReader
from my_file_writer import MyFileWriter

reader_1 = MyFileReader()
reader_1.print_current_directory()

reader_2 = MyFileReader("pi_digits.txt")
reader_2.process_pi()

reader_3 = MyFileReader("pi_million_digits.txt")
reader_3.process_pi_million_digits()

# pi_million_digits.txt is ignored, need to redownload it if you want next lines to run

#user_input = input("Enter your birthday MMDDYYYY: ")
#print(user_input)

#reader_4 = MyFileReader("pi_million_digits.txt")
#reader_4.process_birthday_in_pi(user_input)

writer_1 = MyFileWriter()
writer_1.print_current_directory()

writer_2 = MyFileWriter()
writer_2.write_message_to_file("hello from file writer!!!!", "my_message.txt")


# write multiple lines
contents = "hello from file writer\n"
contents += "next line goes here\n"
contents += "and next one here\n"


writer_3 = MyFileWriter()
writer_2.write_message_to_file(contents, "my_message.txt")