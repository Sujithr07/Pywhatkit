import pywhatkit

def send_message():

    num=input("Enter receiver number: ")
    print()

    message=input("Enter message: ")
    print()

    time=input("Time of delievery (in format 07,40): ")
    
    split_time=time.split(',')
    hour=int(split_time[0])
    min=int(split_time[1])

    pywhatkit.sendwhatmsg(num,message,hour,min)




