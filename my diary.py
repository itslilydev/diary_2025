from datetime import datetime
#Get input from user
entry = input(" What did you feel and experience today?")
#Take time
time = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
#Save to log file
with open("daily.txt","a",
          encoding="utf-8") as file:
    file.write(f"{time} - {entry}\n")
    print("Your diary has been saved.Take care")