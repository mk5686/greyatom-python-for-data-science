# --------------
#Code starts here

#Function to read file
def read_file(path):
    file_path=path
    
    #Opening of the file located in the path in 'read' mode
    file=open(file_path,'r')
    #Reading of the first line of the file and storing it in a variable
    sentence=file.readline()
    #Closing of the file
    file.close()
    #Returning the first line of the file
    return sentence
    

#Calling the function to read file
sample_message=read_file(file_path)
message_1=read_file(file_path_1)
message_2=read_file(file_path_2)
#Printing the line of the file
print(sample_message)
print(message_1)
print(message_2)

#Function to fuse message
def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    quotient=int(message_b)//int(message_a)
    #Returning the quotient in string format
    str(quotient)
    return quotient
#Calling the function to read file  
secret_msg_1=fuse_msg(message_1,message_2)
#Calling the function to read file
message_3=read_file(file_path_3)

#Calling the function 'fuse_msg'


#Printing the secret message 

print(secret_msg_1)
print(message_3)
#Function to substitute the message
def substitute_msg(message_c):
    sub="Data Scientist"
    #If-else  
    if message_c is 'Red':
        sub ='Army General' 
      
    elif message_c is 'Green':
        sub='Data Scientist'
      
    elif message_c is 'Blue':
        sub='Marine Biologist'

    #Returning the substitute of the message
    return sub
    

#Calling the function to read file
message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
#Calling the function 'substitute_msg'
secret_msg_2=substitute_msg(message_3)
#Printing the secret message
print(secret_msg_2)
print(message_4)
print(message_5)



#Function to compare message
def compare_msg(message_d,message_e):

    #Splitting the message into a list
    a_list=message_4.split()
    b_list=message_5.split()
    
    #Splitting the message into a list
    
    
    #Comparing the elements from both the lists
    c_list = [x for x in a_list if x not in b_list]
    
    #Combining the words of a list back to a single string sentence
    final_msg=" ".join(c_list)
    
    #Returning the sentence
    return final_msg
    

#Calling the function to read file

message_6 =read_file(file_path_6)

print(message_6)
#Calling the function to read file


#Calling the function 'compare messages'
secret_msg_3=compare_msg(message_4,message_5)

#Printing the secret message
print(secret_msg_3)
#Function to filter message
def extract_msg(message_f):
    
    #Splitting the message into a list
    a_list=message_f.split()
    
    #Creating the lambda function to identify even length words
    even_word= lambda x : len(x)%2==0
    b_list=list(filter(even_word,a_list))       
    #Splitting the message into a list

    #Combining the words of a list back to a single string sentence
    final_msg=" ".join(b_list)
    #Returning the sentence
    return final_msg
    
#Calling the function to read file
secret_msg_4=extract_msg(message_6)

#Calling the function 'filter_msg'



#Printing the secret message
print(secret_msg_4)

#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message
secret_msg=" ".join(map(str,message_parts))
#secret_meg=str(secret_msg_3)+" "+str(secret_msg_1)+" "+str(secret_msg_4)+" "+str(secret_msg_2)
#secret_meg=" ".join([str(x) for x in message_parts])
#Function to write inside a file
def write_file(secret_msg,path):
    
    #Opening a file named 'secret_message' in 'write' mode
    secret_message=open(path,"a+")

    #Writing to the file
    secret_message.write(secret_msg)

    #Closing the file
    secret_message.close()

#Calling the function to write inside the file    
write_file(secret_msg,final_path)
#Printing the entire secret message
print(secret_msg)


#Code ends here


