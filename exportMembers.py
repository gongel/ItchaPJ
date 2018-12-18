import itchat as ic
ic.auto_login(hotReload=True)

for room in ic.get_chatrooms(update=True)[0:]:
    UserName=room['UserName']
    NickName=room['NickName']
    print(NickName)
    path='C:/Users/gongel/Desktop/group/'+repr(NickName)+'.txt'
    chatRoom=ic.update_chatroom(userName=UserName,detailedMember=True)
    try:
        with open(path,'a',encoding='utf-8') as f:
            i=1
            for friend in chatRoom['MemberList']:
                if friend['DisplayName']=='':
                    friend['DisplayName']='暂无备注'
                f.write(repr(i)+'.'+friend['DisplayName']+',  '+friend['NickName']+'\n')
                i+=1
    except Exception  as e:
        print(repr(e))



ic.run()
