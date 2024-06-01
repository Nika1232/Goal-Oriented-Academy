import wexpect
import time

# რთავს სხვა სკრიპტს(სადაც მდებარეობს)
child = wexpect.spawn('python C:/Users/gela/Desktop/introduction/introduction.py')

# ელოდება მეორე სკრიპტში მოცემულ რაიმე მესიჯს რის შემდეგაც აგრძელებს მოქმედებას
child.expect("what is your full name?") 

# როდესაც იპოვის, აგზავნის სახელს
child.sendline('nika tavartqiladze')

################################################
# იგივე
child.expect("what is your age?") 
child.sendline('25')
#############
child.expect(wexpect.EOF)
print(child.before)