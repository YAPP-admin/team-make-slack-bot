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
            print(temp_list)
            d_members.append(temp_list)
        
        for member_list in d_members:
            if len(members) <= 0: 
                break
            member_list.append(members.pop())
        
        return d_members