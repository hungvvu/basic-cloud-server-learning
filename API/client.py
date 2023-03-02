import requests

BASE = "http://127.0.0.1:5000/"

# # call the put request
# requests.put(BASE + "student/1235", {'name':'John Doe','age':30})

# # pause before the get request
# input()

# # call the get request
# response = requests.get(BASE + 'student/123324')

# # print out the response
# print(response.json())

stop = False

while not stop:
    # print out user prompt
    print('Options:\n1. GET\
                    \n2. PUT\
                    \n3. EXIT')
    option = input()
    match option:
        case '1':
            print('Enter student ID: ', end='')
            id = input()
            response = requests.get(BASE + 'student/' + id)
            print(response.json())
        case '2':
            print('Enter student ID: ', end='')
            id = input()
            print('Enter student name: ', end='')
            name = input()
            print('Enter student age: ', end='')
            age = input()
            response = requests.put(BASE + "student/" + id, \
                                    {'name':name,'age':age})
            print(response.json())
        case '3':
            stop = True
        case _:
            print('Invalid choice')

    print('')
    
    