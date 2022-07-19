# README.md

* **working directory** : 내가 작업하고 있는 실제 디렉토리

* **staging area** : 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳

* **repository** : 커밋들이 저장되는 곳
* **커밋** : ~를 적어두다라는 의미와 비슷하다

---

**git status** : 깃으로 관리되고있는 파일들의 상태를 알려주는 명령어

* vscode의 터미널창에 git add README.md
* git status로 변경된 파일을 확인

---

### 새롭게 변경한 파일을 추가

1. **git init** 을 활용해 파일을 마스터로 지정해준다.

2. **git add a.txt** 를 사용하여 a.txt라는 텍스트파일 추가

3. **git commit -m "add a.txt"** 를 사용해 add a.txt라는 메시지 추가

4. 다음에 또 파일을 수정하면 **git commit -m "입력메시지"**를 통해 변경사항 기록

---

### vscode에 깃허브 계정 연동하기

1. **git config --global user.name "유저네임"**

2. **git config --global user.email "이메일주소"**

---

### git 인증 방법 

 settings =>developer settings => personal access tokens 가서 토근 발급받기

(웹으로 인증하라고 알림이 뜰시엔 초록색 버튼 누르면 인증 완료)

발급한 토큰은 다시 볼 수 없으므로 꼭 메모장 같은곳에 저장하기!

*expiration date : 토큰의 만료 기간*

권한 설정 : repo 부분만 체크(저장소 관련 권한)

---

### vscode와 git hub를 연결해서 최신화

1. **git remote add origin "깃허브 레포지토리 url"** : 어떤 원격 저장소에 깃 작업을 할건지 등록

2. **git push origin master** : 내가 지금까지 커밋한 내용(파일들) 원격 저장소에 업데이트

---

### 깃허브를 다른 pc나 파일에 복사

1. 깃허브에 있는 **https 주소를 복사**

2. **원하는 파일에 들어가서 gitbash를 킨다**

3. **git clone "복사한 https 주소 입력"** 을 입력한다.

4. **끝**

---

**commit 하기전에 꼭 pull 을 통해서 원격 레포지토리와 로컬 레포지토리의 정보를 최신화**
.