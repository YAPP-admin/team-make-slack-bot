import properties

def divid_member(members):
        if type(members) is str:
            members = list(members)
        
        d_members = []
    
        # set을 활용한 무작위 진행
        members = set(members)
        members = list(members)
        total_member = len(members)
        
        if total_member < properties.LIMITED_NUMBER_OF_PEOPLE:
            return list(members)
        
        # limit만큼 데이터를 집어넣어서 list를 만든다.
        # list를 모으는 list를 만든다.
        # 저장된 데이터를 return한다.        
        while len(members) >= properties.LIMITED_NUMBER_OF_PEOPLE:
            temp_list = []
            for i in range(0, properties.LIMITED_NUMBER_OF_PEOPLE):
                temp_list.append(members.pop())
            # print(temp_list)
            d_members.append(temp_list)
        
        # 만약, 팀 갯수가 남은 사람 수보다 작다면, 남은 사람들로 팀을 하나 만든다.
        if len(d_members) < len(members):
            d_members.append(members)
        else:    
            for member_list in d_members:
                if len(members) <= 0: 
                    break
                member_list.append(members.pop())
        
        return d_members
    
def member_lists_to_message_lists(member_list):
    # member_list가 만약 여러 팀일 때면, user들이 들어가는 String list로 변환해주기
    # member_list에 list가 하나라면, user들이 들어가는 String 변환해서 던져주기
    result_lists = []
    user_mention_list = ""
            # 이런식으로 유저를 mention할 수 있다.
    for user_list in member_list:
        list_type = type(user_list)
        if type(user_list) is list:
            user_mention_list = ""
            for user in user_list:
                user_mention_list += '<@'+user+'> '
            result_lists.append(user_mention_list) 
            user_mention_list = ""
                
        else :
            user_mention_list += '<@'+user_list+'> '
            
    if len(user_mention_list) != 0:
        result_lists.append(user_mention_list)
    
    return result_lists