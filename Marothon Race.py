list_for_turkish = []
new_list = []
athletes = {}
temp = {}
x = 'Y'
j = 0
while x in 'Y':
    name,surname = input('First and last name: ').split(' ') 
    country = input('Country: ') 
    hour,minute,second = eval(input('Finishing time in hours, minutes, seconds: '))
    tup1 = (name,surname)
    tup2 = (hour,minute,second)
    list = [country,tup2]  
    athletes[tup1] = list
    total = hour*60+minute+second*0.01
    if country in "Turkey" and total <180:
        list_for_turkish.append(name)
        list_for_turkish.append(surname)
    x = input('Do you want to continue Y/N ? ')
    if x in 'N' :
        number = 'N'
        print()

for key in athletes:
    list_ = athletes[key]
    temp_country = list_[0]
    temp_time = list_[1]
    temp_tup = (temp_country,)
    temp_key = key
    temp_key = temp_key + temp_tup
    temp[temp_key] = temp_time 

new_dict = dict(sorted(temp.items(), key=lambda item: item[1]))
for key in new_dict:
    new_tuple = key
    new_list.append(new_tuple)

print('Gold Medal: ', new_list[0][0],new_list[0][1],',',new_list[0][2])
print('Silver Medal: ', new_list[1][0],new_list[1][1],',',new_list[1][2])
print('Bronze Medal: ', new_list[2][0],new_list[2][1],',',new_list[2][2])
print()

max_length = len(list_for_turkish)
print('Turkish athletes running under 3 hours: ')
while j < max_length:
    print(list_for_turkish[j],list_for_turkish[j+1])
    j+=2
print()    