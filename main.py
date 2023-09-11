import RPi.GPIO as GPIO
import time
import soundy

noisy = soundy.Soundy()

GPIO.setmode(GPIO.BCM)
pin1 = 1
pin2 = 2
pin3 = 3
pin4 = 4
pin5 = 5
pin6 = 6
pin7 = 7
pin8 = 8
pin9 = 9
pin0 = 0
pinPlus = "+"
pinMinus = "-"
pinMultiply = "*"
pinDivide = "÷"
pinEquals = "="

firstNum = ""
secondNum = ""


print("Please enter a number, and make sure both numbers' digits are less than or equal to 4 when added up (Ex: 22*22 or 333*3.")
print()

pins = [[pin1,21],[pin2,26],[pin3,19],[pin4,13],[pin5,6],[pin6,5],[pin7,22],[pin8,27],[pin9,17],
        [pin0,4],[pinPlus,18],[pinMinus,23],[pinMultiply,24],
        [pinDivide,25],[pinEquals,20]]

for pin in pins:
  GPIO.setup(pin[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#---------------------------------------------------------------------------------------------

#this variable decides whether it should keep adding to the 
#firstNum variable, for longer numbers like 3333, rather than ending it as
#single digit
buttonAdd = True


first1 = False
first2 = False
first3 = False



while buttonAdd:
  if GPIO.input(pins[10][1])==GPIO.HIGH and firstNum != "":
    buttonAdd = False
  
  elif GPIO.input(pins[11][1])==GPIO.HIGH and firstNum != "":
    buttonAdd = False
  elif GPIO.input(pins[12][1])==GPIO.HIGH and firstNum != "":
    buttonAdd = False
  
  elif GPIO.input(pins[13][1])==GPIO.HIGH and firstNum != "":
      buttonAdd = False
  elif GPIO.input(pins[14][1])==GPIO.HIGH and firstNum != "":
      buttonAdd = False

  if len(firstNum)>2:
      buttonAdd=False
  
  
  if GPIO.input(pins[0][1])==GPIO.HIGH:
    firstNum += "1"
    print(1,end="")
    time.sleep(.5)
  elif GPIO.input(pins[1][1])==GPIO.HIGH:
    firstNum += "2"
    print(2,end="")
    time.sleep(.5)
  elif GPIO.input(pins[2][1])==GPIO.HIGH:
    firstNum += "3"
    print(3,end="")
    time.sleep(.5)
  elif GPIO.input(pins[3][1])==GPIO.HIGH:
    firstNum += "4"
    print(4,end="")
    time.sleep(.5)
  elif GPIO.input(pins[4][1])==GPIO.HIGH:
    firstNum += "5"
    print(5,end="")
    time.sleep(.5)
  elif GPIO.input(pins[5][1])==GPIO.HIGH:
    firstNum += "6"
    print(6,end="")
    time.sleep(.5)
  elif GPIO.input(pins[6][1])==GPIO.HIGH:
    firstNum += "7"
    print(7,end="")
    time.sleep(.5)
  elif GPIO.input(pins[7][1])==GPIO.HIGH:
    firstNum += "8"
    print(8,end="")
    time.sleep(.5)
  elif GPIO.input(pins[8][1])==GPIO.HIGH:
    firstNum += "9"
    print(9,end="")
    time.sleep(.5)
  elif GPIO.input(pins[9][1])==GPIO.HIGH:
    firstNum += "0"
    print(0,end="")
    time.sleep(.5)

if len(firstNum) == 1:
    first1 = True
elif len(firstNum) == 2:
    first2 = True
elif len(firstNum) == 3:
    first3 = True
#----------------------------------------------- 2nd number
exit = True

add = False
subtract = False
multiply = False
divide = False


while exit:
  if GPIO.input(pins[10][1])==GPIO.HIGH:
    add = True
    exit = False
  elif GPIO.input(pins[11][1])==GPIO.HIGH:
    subtract = True
    exit = False
  elif GPIO.input(pins[12][1])==GPIO.HIGH:
    multiply = True
    exit = False
  elif GPIO.input(pins[13][1])==GPIO.HIGH:   
    divide = True
    exit = False


if add:
  print("+", end="")
elif subtract:
  print("-", end="")
elif multiply:
  print("*", end="")
elif divide:
  print("÷", end="")

#-------------------------------------------------------
buttonAdd = True
while buttonAdd:
  if GPIO.input(pins[14][1])==GPIO.HIGH and secondNum != "":   
    buttonAdd = False
 
  if first1 and len(secondNum)>2:
      buttonAdd = False
  if first2 and len(secondNum)>1:
      buttonAdd = False
  if first3 and len(secondNum)>0:
      buttonAdd = False
  
  if GPIO.input(pins[0][1])==GPIO.HIGH:
    secondNum += "1"
    print(1,end="")
    time.sleep(.5)
  elif GPIO.input(pins[1][1])==GPIO.HIGH:
    secondNum += "2"
    print(2,end="")
    time.sleep(.5)
  elif GPIO.input(pins[2][1])==GPIO.HIGH:
    secondNum += "3"
    print(3,end="")
    time.sleep(.5)
  elif GPIO.input(pins[3][1])==GPIO.HIGH:
    secondNum += "4"
    print(4,end="")
    time.sleep(.5)
  elif GPIO.input(pins[4][1])==GPIO.HIGH:
    secondNum += "5"
    print(5,end="")
    time.sleep(.5)
  elif GPIO.input(pins[5][1])==GPIO.HIGH:
    secondNum += "6"
    print(6,end="")
    time.sleep(.5)
  elif GPIO.input(pins[6][1])==GPIO.HIGH:
    secondNum += "7"
    print(7,end="")
    time.sleep(.5)
  elif GPIO.input(pins[7][1])==GPIO.HIGH:
    secondNum += "8"
    print(8,end="")
    time.sleep(.5)
  elif GPIO.input(pins[8][1])==GPIO.HIGH:
    secondNum += "9"
    print(9,end="")
    time.sleep(.5)
  elif GPIO.input(pins[9][1])==GPIO.HIGH:
    secondNum += "0"
    print(0,end="")
    time.sleep(.5)

x = True
while x:
    if GPIO.input(pins[14][1])==GPIO.HIGH:
        print("=", end="")
        x = False

if add:
  print(int(int(firstNum) + int(secondNum)))
  noisy.makeNoise(int(firstNum), "+", int(secondNum), int(int(firstNum) + int(secondNum)))
elif subtract:
  print(int(int(firstNum) - int(secondNum)))
  noisy.makeNoise(int(firstNum), "-", int(secondNum), int(int(firstNum) - int(secondNum)))
elif multiply:
  print(int(int(firstNum) * int(secondNum)))
  noisy.makeNoise(int(firstNum), "*", int(secondNum), int(int(firstNum) * int(secondNum)))
elif divide:
  print(int(int(firstNum) / int(secondNum)))
  noisy.makeNoise(int(firstNum), "/", int(secondNum), int(int(firstNum) / int(secondNum)))

time.sleep(1.2)
noisy.insult()
