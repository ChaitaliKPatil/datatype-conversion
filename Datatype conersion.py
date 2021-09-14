#Q8
print('Q8: Casting Datatypes\n8+2= ',8+2)#addition of two integers gives int
print('8.2+6.8= ',8.2+6.8)#addition of two floating point numbers gives number
print('\'8\'+\'2\'= ','\'8'+'2\'\n')#Addition of two strings gives string
#Datatypes
a=input('Enter a no.')
b=input('Enter other no.')
#add the variable values together then display the combined result and its data type – to see a concatenated string value result
print('1. Add the variable values together then display the combined result and its data type – to see a concatenated string value result\n',type(a))
sum=a+b
print('Data Type sum: ',sum,type(sum))
#add the variable values together then display the combined result and its data type – to see a total integer value result
print('\n2. Add the variable values together then display the combined result and its data type – to see a total integer value result')
sum=int(a)+int(b)
print('Data Type sum: ',sum,type(sum))
#cast a variable value then display the result and its data type – to see a total float value
print('\n3. Cast a variable value then display the result and its data type – to see a total float value')
sum=float(sum)
print('Data Type sum: ',sum,type(sum))
#cast an integer representation of a variable value then display the result and its data type – to see a character string value
print('\n4. Cast an integer representation of a variable value then display the result and its data type – to see a character string value')
sum=chr(int(sum))
print('\nData Type sum: ',sum,type(sum))
print('\n\n\n\n')
