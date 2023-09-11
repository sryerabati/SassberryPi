from pygame import mixer
import time
global sound, equals
import random


class Soundy:
    def __init__(self):
        mixer.init()
        self.equals = mixer.Sound('sounds/opps/equals.wav')
    def playSound(self, num):
        
        mixer.init()
        s2 = False
        s3 = False
        s4 = False
        s5 = False
        s6 = False
        negative = False
        nsound = mixer.Sound('sounds/opps/negative.wav')
        
        
        num1 = num
        
        if str(num1)[0] == '-':
            num1 = abs(num1)
            negative = True
        
        if len(str(num1)) == 1:
            sound = mixer.Sound('sounds/nums/'+str(num1)+'.wav')
        
        elif len(str(num1)) == 2:
            if (str(num1))[0] == '1':
                sound = mixer.Sound('sounds/nums/'+str(num1)+'.wav')
            elif (str(num1))[1] == '0':
                sound = mixer.Sound('sounds/nums/'+str(num1)+'.wav')
            else:
                sound = mixer.Sound('sounds/nums/'+(str(num1))[0]+'0.wav')
                sound2 = mixer.Sound('sounds/nums/'+(str(num1))[1]+'.wav')
                s2 = True
        
        elif len(str(num1)) == 3:
            if (str(num1))[1] == '0' and (str(num1))[2] == '0':
                sound = mixer.Sound('sounds/nums/'+(str(num1))[0]+'.wav')
                sound2 = mixer.Sound('sounds/nums/hundred.wav')
                s2 = True
            elif (str(num1))[1] == '0' or (str(num1))[2] == '0':
                sound = mixer.Sound('sounds/nums/'+(str(num1))[0]+'.wav')
                sound2 = mixer.Sound('sounds/nums/hundred.wav')
                if (str(num1))[1] == '0':
                    sound3 = mixer.Sound('sounds/nums/'+(str(num1))[2]+'.wav')
                else:
                    sound3 = mixer.Sound('sounds/nums/'+(str(num1))[1]+'0.wav')
                s3 = True
            else:
                if (str(num1))[1] != '1':
                    sound = mixer.Sound('sounds/nums/'+(str(num1))[0]+'.wav')
                    sound2 = mixer.Sound('sounds/nums/hundred.wav')
                    sound3 = mixer.Sound('sounds/nums/'+(str(num1))[1]+'0.wav')
                    sound4 = mixer.Sound('sounds/nums/'+(str(num1))[2]+'.wav')
                    s4 = True
                else:
                    sound = mixer.Sound('sounds/nums/'+(str(num1))[0]+'.wav')
                    sound2 = mixer.Sound('sounds/nums/hundred.wav')
                    sound3 = mixer.Sound('sounds/nums/1'+(str(num1))[2]+'.wav')
                    s3 = True
                    
                
        elif len(str(num1)) == 4:
            if (str(num1))[1] == '0' and (str(num1))[2] == '0' and (str(num1))[3] == '0':
                sound = mixer.Sound('sounds/nums/'+(str(num1))[0]+'.wav')
                sound2 = mixer.Sound('sounds/nums/thousand.wav')
                s2 = True
            elif ((str(num1))[1] == '0' and (str(num1))[2] == '0') or ((str(num1))[1] == '0' and (str(num1))[3] == '0'):
                sound = mixer.Sound('sounds/nums/'+(str(num1))[0]+'.wav')
                sound2 = mixer.Sound('sounds/nums/thousand.wav')
                if (str(num1))[2] == '0':
                    sound3 = mixer.Sound('sounds/nums/'+(str(num1))[3]+'.wav')
                else:
                    sound3 = mixer.Sound('sounds/nums/'+(str(num1))[2]+'0.wav')
                s3 = True
            elif (str(num1))[1] != '0':
                sound = mixer.Sound('sounds/nums/'+(str(num1))[0]+'.wav')
                sound2 = mixer.Sound('sounds/nums/thousand.wav')
                sound3 = mixer.Sound('sounds/nums/'+(str(num1))[1]+'.wav')
                sound4 = mixer.Sound('sounds/nums/hundred.wav')
                if (str(num1))[2] == '0' and (str(num1))[3] == '0':
                    s4 = True
                elif (str(num1))[2] == '0' or (str(num1))[3] == '0':
                    if (str(num1))[2] == '0':
                        sound5 = mixer.Sound('sounds/nums/'+(str(num1))[3]+'.wav')
                    else:
                        sound5 = mixer.Sound('sounds/nums/'+(str(num1))[2]+'0.wav')
                    s5 = True                
                else:
                    if (str(num1))[2] == '1':
                        sound = mixer.Sound('sounds/nums/'+(str(num1))[0]+'.wav')
                        sound2 = mixer.Sound('sounds/nums/thousand.wav')
                        sound3 = mixer.Sound('sounds/nums/'+(str(num1))[1]+'.wav')
                        sound4 = mixer.Sound('sounds/nums/hundred.wav')
                        sound5 = mixer.Sound('sounds/nums/1'+(str(num1))[3]+'.wav')
                        s5 = True
                    else:
                        sound = mixer.Sound('sounds/nums/'+(str(num1))[0]+'.wav')
                        sound2 = mixer.Sound('sounds/nums/thousand.wav')
                        sound3 = mixer.Sound('sounds/nums/'+(str(num1))[1]+'.wav')
                        sound4 = mixer.Sound('sounds/nums/hundred.wav')
                        sound5 = mixer.Sound('sounds/nums/'+(str(num1))[2]+'0.wav')
                        sound6 = mixer.Sound('sounds/nums/'+(str(num1))[3]+'.wav')
                        s6 = True
            else:
                if (str(num1))[2] == '1':
                    sound = mixer.Sound('sounds/nums/'+(str(num1))[0]+'.wav')
                    sound2 = mixer.Sound('sounds/nums/thousand.wav')
                    sound3 = mixer.Sound('sounds/nums/1'+(str(num1))[3]+'.wav')
                    s3 = True
                else:
                    sound = mixer.Sound('sounds/nums/'+(str(num1))[0]+'.wav')
                    sound2 = mixer.Sound('sounds/nums/thousand.wav')
                    sound3 = mixer.Sound('sounds/nums/'+(str(num1))[2]+'0.wav')
                    sound4 = mixer.Sound('sounds/nums/'+(str(num1))[3]+'.wav')
                    s4 = True
                    
        if negative == True:
            nsound.play()
            time.sleep(0.8)
        #print('playing sound 1')
        sound.play()
        if s2 == True:
            #print('playing sound 2')
            time.sleep(0.8)
            sound2.play()
        if s3 == True:
            #print('playing sound 3')
            time.sleep(0.8)
            sound2.play()
            time.sleep(0.8)
            sound3.play()
        if s4 == True:
            #print('playing sound 4')
            time.sleep(0.8)
            sound2.play()
            time.sleep(0.8)
            sound3.play()
            time.sleep(0.8)
            sound4.play()
        if s5 == True:
            #print('playing sound 5')
            time.sleep(0.8)
            sound2.play()
            time.sleep(0.8)
            sound3.play()
            time.sleep(0.8)
            sound4.play()
            time.sleep(0.8)
            sound5.play()
        if s6 == True:
            #print('playing sound 6')
            time.sleep(0.8)
            sound2.play()
            time.sleep(0.8)
            sound3.play()
            time.sleep(0.8)
            sound4.play()
            time.sleep(0.8)
            sound5.play()
            time.sleep(0.8)
            sound6.play()
            
        return num1
        

    #numba = int(input("Enter a 2 digit number >"))  

    #numba2 = int(input("Enter a 2 digit number >"))


    #opp = str(input("Choose one of the following: [ + - * / ] >"))

    def makeNoise(self, numba, opp, numba2, endnumba):
        if opp == '+':
            endnumba = numba + numba2
            sound = mixer.Sound('sounds/opps/plus.wav')
        elif opp == '-':
            endnumba = numba - numba2
            sound = mixer.Sound('sounds/opps/minus.wav')
        elif opp == '*':
            endnumba = numba * numba2
            sound = mixer.Sound('sounds/opps/times.wav')
        elif opp == '/':
            endnumba = numba / numba2
            sound = mixer.Sound('sounds/opps/divided-by.wav')



        self.playSound(numba)
        time.sleep(1)
        sound.play()
        time.sleep(1)
        self.playSound(numba2)
        time.sleep(1)
        self.equals.play()
        time.sleep(1)
        endnumba = int(endnumba)
        self.playSound(endnumba)
    def insult(self):
        randnum = random.randint(1,16)
        filename = 'sounds/insults/Insult'+str(randnum)+'.wav'
        remark = mixer.Sound(filename)
        remark.play()