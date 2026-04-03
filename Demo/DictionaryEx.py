print()
userDetails = {'Id' :1, 'userName': 'just me'}
print(type(userDetails))
print(userDetails)
location = dict(s= 'Samtse',t = 'Thimphu', p = 'paro')
print(location)
print(location['s'])
print(location['t'])
print(location['p'])
print(location)
userDetails['email'] = 'justme@example.com'
print(userDetails)
userDetails['userName'] = 'just_me_updated'
print(userDetails)
del location['p']
print(location)
deleted_value = userDetails.pop('email')
print(deleted_value)
del_key, del_value = userDetails.popitem()
print(f'the deleted key is{del_key} and the deleted value is {del_value}')
location.clear()
print(location)
print()