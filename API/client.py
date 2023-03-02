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
                    \n3. DELETE\
                    \n4. UPDATE\
                    \n5. EXIT')
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
            print('Enter student ID: ', end='')
            id = input()
            response = requests.delete(BASE + 'student/' + id)
            print(response.json())
        case '4':
            print('Enter student ID: ', end='')
            id = input()
            print('Enter a field you want to update: ', end='')
            field = input()

            response = {}
            match field:
                case 'name':
                    print('Enter name: ', end='')
                    name = input()
                    response = requests.patch(BASE + 'student/' + id,\
                                               {'name':name})
                case 'age':
                    print('Enter age: ', end='')
                    age = input()
                    response = requests.patch(BASE + 'student/' + id,\
                                               {'age':age})
                case _:
                    print('Invalid field')
                    
            print(response.json())


        case '5':
            stop = True
        case _:
            print('Invalid choice')

    print('')
    
    