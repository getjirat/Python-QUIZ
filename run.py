def ConfirmEnter(choiceA,choiceB,choiceCancel):
  answer = False
  if choiceA == '':
    print(choiceA,"Or",choiceB,"Or",choiceCancel)
    answer = input("Press KEY [ENTER] to continue.")
  else:
    answer = input(">>>")
print("Welcome to python quiz!")
ConfirmEnter("","","")
print("You can create your own question and answer in assets folder.")
ConfirmEnter("","","")
print("Do you want to continue playing?")
ConfirmEnter("Yes","No","Cancel")
if answer == 'Yes':
  print("Let the QUIZ Begin!")
  ConfirmEnter("","","")
elif answer == 'No':
  exit()
elif answer == 'Cancel':
  
