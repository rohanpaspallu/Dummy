import socket
print("For server side")
HOST=socket.gethostname()
PORT=12345
s=socket.socket()
s.bind((HOST,PORT))
s.listen(1)
conn,addr=s.accept()
print("connected by:",addr)

file_read = open("data.txt", "r")
# print(file_read)
new_list = []

for i in file_read:
    element = i.split('|')
    dummy = []
    for j in element:
        j = j.strip()
        dummy.append(j)
        # print(j)

    if(dummy[0]==''):
        continue
    # print(dummy[1])
    str = '|'.join(dummy)

    # print(str)
    new_list.append(str)
    # print(new_list)

print(new_list)


while True:
    data = conn.recv(1024)
    received = repr(data)
    received = received[:-1]
    print(received)

    received_list=[]
    received_list = received.split('|')
    # print(received_list[1])


    if received_list[1]=='1':
        count=0
        # print('in 1')
        print(new_list)
        for i in new_list:
            value = i.split("|")
            d_value = []
            count= count+1

            for j in value:
                j = j.strip()
                d_value.append(j)
            # print("dummy value: ", d_value)
            # print(d_value[0])
            # print('value of i: ',i)
            if value[0]==received_list[2]:
                reply = '|'.join(d_value)
                # print("this is reply",reply)
                conn.sendall(reply.encode())
                received_list=[]
                break

            elif count==len(new_list)-1:
                reply = 'value not found'
                # print("this is reply",reply)
                conn.sendall(reply.encode())
                received_list = []
                break


            # elif value[0]!=received_list[2] and len(new_list)-1:
            #     print('value not found')
            #     break
            # else:
            #     continue






    elif received_list[1]=='2':
        print('2')

        print(received_list)
        received_list.pop(0)
        received_list.pop(0)

        name_list=[]

        for i in new_list:
            d=[]
            print(i)
            d = i.split('|')
            name_list.append(d[0])

        # print(name_list)

        checker=0
        for i in name_list:
            # print('r',received_list[0])
            # print('i',i)
            if received_list[0]==i:
                checker=1
                break

        # print(checker)
        if checker == 1:
            reply = 'Customer already exists'
            # print("this is reply",reply)
            conn.sendall(reply.encode())
            received_list=[]
        elif checker == 0:

            # print('elements received',received_list[0])

            add = '|'.join(received_list)
            # print(add)
            new_list.append(add)

            reply = 'Customer added'
            # print("this is reply",reply)
            conn.sendall(reply.encode())
            print(new_list)
            received_list=[]







    elif received_list[1]=='3':

        print(received_list[2])

        name_list = []

        for i in new_list:
            d = []
            d = i.split('|')
            name_list.append(d[0])

        c = 0
        for i in name_list:
            # print(received_list[2])
            # print(i)
            if received_list[2] == i:
                new_list.pop(c)
                reply = 'Customer deleted'
                # print("this is reply",reply)
                conn.sendall(reply.encode())
                received_list = []
                break
            elif c==len(new_list)-1:
                reply = 'Customer does not exist'
                # print("this is reply",reply)
                conn.sendall(reply.encode())
                received_list = []
            c=c+1

        print(new_list)





    elif received_list[1]=='4':

        print(received_list)

        name_list = []

        for i in new_list:
            d = []
            d = i.split('|')
            name_list.append(d[0])

        c = 0
        for i in name_list:
            if received_list[2] == i:
                age_data=[]
                age_data = new_list[c].split('|')
                age_data[1]= received_list[3]
                new_list[c]= '|'.join(age_data)
                reply = 'Customer age changed'
                # print("this is reply",reply)
                conn.sendall(reply.encode())
                received_list = []
                break
            elif c==len(new_list)-1:
                reply = 'Customer does not exist'
                # print("this is reply",reply)
                conn.sendall(reply.encode())
                received_list = []
            c=c+1

        print(new_list)





    elif received_list[1]=='5':

        print(received_list)

        name_list = []

        for i in new_list:
            d = []
            d = i.split('|')
            name_list.append(d[0])

        c = 0
        for i in name_list:
            if received_list[2] == i:
                address_data=[]
                address_data = new_list[c].split('|')
                address_data[2]= received_list[3]
                new_list[c]= '|'.join(address_data)
                reply = 'Customer address changed'
                # print("this is reply",reply)
                conn.sendall(reply.encode())
                received_list = []
                break
            elif c==len(new_list)-1:
                reply = 'Customer does not exist'
                # print("this is reply",reply)
                conn.sendall(reply.encode())
                received_list = []
            c=c+1

        print(new_list)


    elif received_list[1]=='6':

        print(received_list)

        name_list = []

        for i in new_list:
            d = []
            d = i.split('|')
            name_list.append(d[0])

        c = 0
        for i in name_list:
            if received_list[2] == i:
                phone_data=[]
                phone_data = new_list[c].split('|')
                phone_data[3]= received_list[3]
                new_list[c]= '|'.join(phone_data)
                reply = 'Customer phone changed'
                # print("this is reply",reply)
                conn.sendall(reply.encode())
                received_list = []
                break
            elif c==len(new_list)-1:
                reply = 'Customer does not exist'
                # print("this is reply",reply)
                conn.sendall(reply.encode())
                received_list = []
            c=c+1

        print(new_list)



    elif received_list[1]=='7':
        reply = "', '".join(new_list)
        reply_new = reply+"'"
        # print("this is reply",reply)
        conn.sendall(reply_new.encode())
        received_list = []

    # elif received_list[1] == '8':
    #     reply = 'Goodbye'
    #     # print("this is reply",reply)
    #     conn.sendall(reply.encode())
    #     received_list = []

    elif received_list[1] == '8':
        reply = 'Good bye'
        # print("this is reply",reply)
        conn.sendall(reply.encode())
        conn.close()
        exit()
    # print('received',repr(data))
    # reply=input("message:")
    # conn.sendall(reply.encode())
    # if reply == 'end':
    #     break
# conn.close()

