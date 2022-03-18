## 데덴찌 봇

### 구성

- dedenziBot.py -> slack_sdk를 사용하여 API를 호출하는 클래스입니다.
- properties.py -> 해당 bot에 token과 여러 잡다한 데이터들을 저장하고 있는 패키지입니다.
- divide.py -> 배열이 주어졌을 때, 제한된 인원으로 팀을 꾸려주는 로직이 담겨져 있는 패키지입니다.
- startMessage.py -> 데덴찌 봇이 채널에 모집 메시지를 전송합니다.
- makeTeamMessage.py -> emoji를 통해 반응한 사람들을 모아, divide 패키지를 통해 팀을 꾸려서 팀별 인원을 멘션하여 채널에 메시지를 전송합니다.

### properties

- 민감한 정보(token)를 저장하고 있으므로, git에 올리지 않았습니다. (회장님께 직접 드릴 예정)
- 추후에 message 패키지를 따로 빼서 구성할 예정입니다.

### 사용법

- python startMessage.py 를 호출하면, timestamp를 뱉어줍니다.
  - 나온 timestamp는 데덴찌봇이 올린 메시지에 대한 id라고 생각하시면 됩니다.
- 이를 사용하여, python makeTeamMessage.py 나온 timestamp 를 호출하시면 지금까지 emoji로 반응한 사람들을 가져와서 팀을 꾸려줍니다!

### 예외처리

- 해당하는 채널이 없으면 예외를 던집니다.
- 해당하는 timestamp(== 슬랙봇이 보낸 메시지)가 없으면 예외를 던집니다.
- target으로 하는 emoji를 고른 사람이 없으면 예외를 던집니다.
- 응답한 사람이 1명 이하일 때는 예외를 던집니다.(팀을 만들 필요가 없음)
