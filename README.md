# 07.12 강의 노트
API를 통해 해당 기능들을 가져다 사용할 수 있다 

마크다운 = 주로 개발자들이 텍스트와 코드를 작성해 문서화 하기 위해 사용

CLI = 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식 

GUI = 그래픽을 통해서  “ 

인터페이스 = 상호작용

GUI 는 CLI에 비해  단계가 많고 성능을 상대적으로 많이 소모 

서버, 개발시스템 CLI로 조작

# 07.13 강의 노트
## 복습

- git = 분산 버전 관리 시스템

working Directory    -   Staging Area   -   Repository

                 add                 commit

master는 branch 이름

branch - 가지라는 의미 인데 실사용할 프로젝트를 테스트 하는 목적으로 사용

 git log 사용할 때 터미널창에 end가 나오는 건 단순하게 Q를 통해 나갈 수 있음 

로컬에서 git으로 저장소 설정

1. 폴더 하나에서 git init를 통해 .git 폴더 형성
2. 설정 된 폴더 에서 작업한 파일이나 폴더를 git add를 통해 staging Area로 이동
3. git commit을 통해 Repository로 이동
4. push를 통해 원격 저장소로 복제됨

 git에서 로컬에 있는 폴더를 연동 하는 방법
앞으로 평생 공부 할 것이기 때문에 개인 공부 한 것은 git hub에 커밋 

## 본 수업

## git hub

clone 처음 복제할 때만 사용

pull 변경사항의 일부를 가져올 때 사용

새로운 commit이 없다면 push 할 수 없음 

push 하기 전에 pull을 통해 변경사항이 겹쳐지지 않게 해야한다.

##명령어 활용
add.README.md 여부를 체크 하지 않았을 경우
1. 새로운 로컬 폴더 생성
2. git init 를 통해 .git 폴더를 생성하여 master 폴더로 지정되게 한다
3. touch README.md를 통해 파일 생성
4. git add README.md 를 통해  Staging Area로 보내준다
5. git commit -m "변경 내용 등등" 을 통해 커밋
6. git branch -M master(branch가 여러개가 아닐 경우 생략 가능)
7. git remote add origin(임의의 변수) url주소 를 통해 git hub의 해당 주소의 repositories와 연동
8. git push -u origin master 를 통해 해당 저장소에 업로드
체크를 했을경우
2,3번 과정은 생략 가능 


## gitignore

git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는데 사용되는 텍스트 파일

이미 git의 관리는 받은 파일이나 디렉토리는 적용되지 않음

## TIL

- 매일 내가 배운 것을 마크 다운을 정리해서 문서화
- 스스로 더 나아가 어떤 학습을 했는지 기록