import os
import shutil
from pyttsx3 import speak
directory = os.getcwd()

def create_file():
     speak("Let's create a new file")
     name = input("New File name (to create)- ")     
     path_file = os.path.join(directory, name)
     is_Exists = os.path.exists(path_file)
     if is_Exists:
          choice = input("File already exists, want to try again?(Y/N)- ")
          if choice == "y" or choice == "Y":
               create_file()
          else:
               return
     else:          
          answer = input("Want to write something in file?(Y/N)- ")    
          if answer == "Y" or answer == "y":
               speak("Let's write some content to it - ")
               file =  os.open(os.path.join(directory,name),os.O_RDWR | os.O_CREAT)
               user_writing = [] 
               while True:
                    line = input()
                    if not line: # If line is blank
                         break
                    else:
                         user_writing.append(line)
               user_writing = '\n'.join(user_writing)
               user_writing = user_writing.encode()
               os.write(file, user_writing)
               os.close(file)
               print("Your file "+name+" is successfully created and updated")
               speak("Your file "+name+" is successfully created and updated")
               print("********************************************")
          else:
               file = os.open(os.path.join(directory, name),os.O_RDWR | os.O_CREAT)
               os.close(file)                    
               print("Your file " +name+" is successfully created")
               speak("Your file " +name+" is successfully created")
               print("********************************************")

def create_folder():
     speak("Let's create a new folder")
     name = input("Folder name - ")
     if os.path.exists(os.path.join(directory, name)):
          choice = input("Folder already exists, want to try again?(Y/N)- ")
          if choice == "y" or choice == "Y":
               create_folder()
          else:
               return     
     else:
          try:
               os.mkdir(os.path.join(directory, name))
               print("Folder is created")
               speak("Folder is created")
               print("********************************************")
          except OSError as err:
               speak("Oooopps")
               print("Exception Handled : {0}", format(err))
               print("********************************************")

def delete_file():
     speak("Let's delete a file")
     name = input("Please enter the file name that you want to delete - ")
     is_Exists = os.path.exists(os.path.join(directory, name))
     if  not is_Exists:
          choice = input("File don't exist, want to try again?(Y/N)- ")
          if choice == "y" or choice == "Y":
               delete_file()
          else:
               return
     else:
          try :
               file = os.path.join(directory, name)
               os.remove(file)
               print("File is successfully deleted")
               speak("File is successfully deleted")
               print("********************************************")
          except OSError as err:
               speak("Oooopps")
               print("Exception Handled : {0}", format(err))
               print("********************************************")

def delete_folder():
     speak("Let's delete a folder")
     name = input("Please enter the folder name that you want to delete - ")
     if not os.path.exists(os.path.join(directory, name)):
          choice = input("Folder don't exist, want to try again?(Y/N)- ")
          if choice == "y" or choice == "Y":
               delete_folder()
          else:
               return
     else:
          try:
               os.rmdir(os.path.join(directory,name))
               print("Folder is successfully deleted")
               speak("Folder is successfully deleted")
               print("********************************************")
          except OSError as err:
               speak("Oooopps")
               print("Exception Handled : {0}", format(err))                    
               still_delete = input("Do you still want to delete it ? (Y/N)- ")
               if still_delete == "y" or still_delete == "Y":
                    shutil.rmtree(os.path.join(directory,name), ignore_errors=True)
                    print("Folder is successfully deleted")
                    speak("Folder is successfully deleted")
                    print("********************************************")

def rename_file_folder():
     speak("let's rename ")
     name = input("Please enter the name of file/folder that you want to rename - ")
     if not os.path.exists(os.path.join(directory, name)):
          choice = input("File/Folder don't exist, want to try again?(Y/N)- ")
          if choice == "y" or choice == "Y":
               rename_file_folder()
          else:
               return
     else:
          new_name = input("Please enter the new name that you want - ")
          try:
               os.rename(os.path.join(directory, name),new_name)
               print("Name is successfully changed from "+name+" to "+new_name)
               speak("Name is successfully changed from "+name+" to "+new_name)
               print("********************************************")
          except OSError as err:
               speak("Oooopps")
               print("Exception Handled : {0}", format(err))
               print("********************************************")

def read_file():
     speak("Let's read a file")
     name = input("Enter the name of file that you want to read - ")
     if not os.path.exists(os.path.join(directory, name)):
          choice = input("File don't exist, want to try again?(Y/N)- ")
          if choice == "y" or choice == "Y":
               read_file()
          else:
               return
     else:
          fd = os.open(os.path.join(directory, name), os.O_RDWR)
          size = os.stat(os.path.join(directory, name)).st_size
          byte = int(input("How many bytes(max = "+str(size)+")you want to read ? - "))
          if byte > size:
               print("Invalid number of bytes!!!")
          else:                    
               try:
                    read_bytes = os.read(fd, byte)
                    print(read_bytes.decode())                         
                    print("\nContent is successfully displayed")
                    speak("\nContent is successfully displayed")
                    print("********************************************")
               except OSError as err:
                    print("Exception Handled : {0}", format(err))
                    print("********************************************")

def ask_to_repeat_file_operations():
     choice = input("Want to perform files and folders operations again?(Y/N)- ")
     if choice == "Y" or choice == "y":
          file_folder_operation()
     else:
          return

def file_folder_operation():
     print("You have following choices in Files and Folders Operations : -")
     print("*********************************************")
     print("Create new file / folder ")
     print("Delete existing file / folder")
     print("Rename existing file/folder ")
     print("Read data from existing file ")
     print("Don't Want to perform Files and Folders Operations(exit / don't perform) ")
     second_key = input("Enter your option - ")
     print("********************************************")
     second_key.lower()
     if "create" in second_key and "file" in second_key:
          create_file()
          ask_to_repeat_file_operations()
     elif "create" in second_key and "folder" in second_key:
          create_folder()
          ask_to_repeat_file_operations()
     elif "delete" in second_key and "file" in second_key:
          delete_file()
          ask_to_repeat_file_operations()
     elif "delete" in second_key and "folder" in second_key:
          delete_folder()
          ask_to_repeat_file_operations()
     elif "rename" in second_key:
          rename_file_folder()
          ask_to_repeat_file_operations()
     elif "read" in second_key and ("data" in second_key or "file" in second_key):
          read_file()
          ask_to_repeat_file_operations()
     else:
          return
                              
def open_chrome():
     speak("Let's launch our browser")
     choice = input("Do you want to open a specific site?(Y/N)")
     if choice == "y" or choice == "Y":
          site = input("Enter the site name - ")
          os.system("chrome   "+site)
     else:
          os.system("chrome")
     print("Chrome is opened")
     speak("Chrome is opened")
     print("You are ready to browse anything")
     speak("You are ready to browse anything")
     print("*****************************************************")

def open_notepad():
     speak("Let's open our text editor")
     print("Notepad is opened")
     speak("Notepad is opened")          
     print("You are ready to do your work in notepad")
     speak("You are ready to do your work in notepad")
     os.system("notepad")          
     
     print("*****************************************************")

def ask_to_repeat():
     again = input("Want to Perform Main Operations again(Y/N)- ")
     if again == "Y" or again == "y":
          main()
     else:
          return

def about_myself():
     print("--------------------------------------------------------------------------------------------")
     print("My name is Nidhi Mantri :):):)")
     speak("My name is Nidhi Mantri :):):)")
     print("B.Tech. - Indian Institute of Information Technology, Kota [2016 - 2020]")
     speak("I have done my b. tech. from Indian Institute of Information Technology, Kota  and batch is 2016 to 2020")
     print("Always passionate to learn in the field of Machine Learning and Deep Learning")
     speak("Always passionate to learn in the field of Machine Learning and Deep Learning")
     print("My Linkedin Profile - https://www.linkedin.com/in/nidhi-mantri-085456130")
     speak("This is my linkedin profile")
     print("Contact - nidhimantri.ngr@gmail.com")
     speak("Feel free to contact ")
     print("--------------------------------------------------------------------------------------------")
     
def main():
     print("******************************************************")
     print("You can perform following operations -")
     speak("You can perform following operations -")
     print("Want to work on files and folders ")
     print("Want to open Chrome ")
     print("Want to work on Notepad ")
     print("Want to know about me")
     print("Don't want to perform anything(exit) ")
     speak("Enter your requirement - ")
     key = input("Enter your requirement - ")
     key.lower()
     print("******************************************************")
     if "files" in key or "folders" in key or "file" in key or "folder" in key:
          speak("Welcome to Files and Folders Operations")
          print("Make sure files and folders you want to work on, have full permissions!!")
          file_folder_operation()               
          ask_to_repeat()
     elif ("run" in key or "launch" in key or "open" in key) and "chrome" in key:
          open_chrome()
          ask_to_repeat()
     elif ("run" in key or "launch" in key or "open" in key) and ("notepad" in key or "editor" in key):
          open_notepad()
          ask_to_repeat()
     elif  "about" in key:
          about_myself()
          ask_to_repeat()
     else:
          return

          
if  __name__ == "__main__":
     print("---------------------------------------------------------------------------------------------")
     speak("Welcome to my OS based assistant ")
     print("\t\t\tWelcome to my OS based assistant :) :)")
     print("--------------------------------------------------------------------------------------------")
     main()
     
