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

앞으로 평생 공부 할 것이기 때문에 개인 공부 한 것은 git hub에 커밋 

## 본 수업

## git hub

clone 처음 복제할 때만 사용

pull 변경사항의 일부를 가져올 때 사용

새로운 commit이 없다면 push 할 수 없음 

push 하기 전에 pull을 통해 변경사항이 겹쳐지지 않게 해야한다. 

## gitignore

git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는데 사용되는 텍스트 파일

이미 git의 관리는 받은 파일이나 디렉토리는 적용되지 않음

## TIL

- 매일 내가 배운 것을 마크 다운을 정리해서 문서화
- 스스로 더 나아가 어떤 학습을 했는지 기록