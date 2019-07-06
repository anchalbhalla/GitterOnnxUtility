import requests 
import json

#retrieving user id
res_user = requests.get('https://api.gitter.im/v1/user/me', headers={'Authorization': 'Bearer 146f36d1f43100ba30149160c9d31e392a247451', 'Accept': 'application/json'}) 

json_user = json.loads(res_user.text)

user_id = json_user["id"] 
print("my user id: " + user_id) 


#retrieving the rooms the user is part of
res_rooms = requests.get('https://api.gitter.im/v1/user/' + user_id + '/rooms', headers={'Authorization': 'Bearer 146f36d1f43100ba30149160c9d31e392a247451', 'Accept': 'application/json'}) 
json_room = json.loads(res_rooms.text) 

#retrieving the rooms ids from the json result from the previous request and storing it in a list
count = 0 
all_room_ids = []
for i in json_room: 
	room_id = json_room[count]["id"] 
	all_room_ids.append(room_id)
	count = count+1
print (all_room_ids) 

#retrieving the number of messages in each room id 

for room_id_num in all_room_ids:
	print(room_id_num)
	res_messages = requests.get('https://api.gitter.im/v1/rooms/' + room_id_num + '/chatMessages', headers={'Authorization': 'Bearer 146f36d1f43100ba30149160c9d31e392a247451', 'Accept': 'application/json'}) 
	json_messages = json.loads(res_messages.text) 

	mess_count = 0 

	for i in json_messages: 
		mess_count = mess_count+1 

	print(mess_count)


