# Python 프롬프트 관리 프로그램 최종 제출

## 1. 프로젝트 개요

생성형 AI 미션을 진행하면서 작성한 여러 프롬프트를 한곳에서 관리하기 위해 Python으로 콘솔 기반 프롬프트 관리 프로그램을 제작했습니다.

프로그램에서는 프롬프트를 추가하고 전체 목록을 확인할 수 있으며, 카테고리별 조회, 키워드 검색, 상세 보기, 즐겨찾기 추가·해제 및 즐겨찾기 목록 확인 기능을 제공합니다.

프롬프트 데이터는 Python의 리스트(List)와 딕셔너리(Dictionary)를 사용하여 관리하며, 프로그램 실행 중 추가한 프롬프트와 즐겨찾기 상태는 유지됩니다. 프로그램을 종료하면 데이터는 기본 상태로 초기화됩니다.

---

## 2. GitHub Repository

GitHub 저장소:

https://github.com/ll-0l/python-prompt-manager

저장소 공개 범위: **Public**

---

## 3. 개발 환경

* 운영체제: Windows
* 개발 도구: Visual Studio Code
* Python: 3.14.7
* Git: 2.55.0.windows.3
* 버전 관리: Git / GitHub
* 외부 Python 라이브러리: 사용하지 않음

---

## 4. 개발 환경 설정 확인

### 4-1. Python 버전 확인

터미널에서 Python 버전을 확인했습니다.

사용 명령어:

```bash
py --version
```

실행 결과 Python 3.14.7이 설치된 것을 확인했으며, 과제 조건인 Python 3.10 이상을 충족했습니다.

![Python 버전](screenshots/01_Python_version.png)

---

### 4-2. Python 기본 실행 확인

`hello.py` 파일을 생성하고 다음 코드를 작성했습니다.

```python
print("Hello")
```

터미널에서 다음 명령어로 실행했습니다.

```bash
py hello.py
```

정상적으로 `Hello`가 출력되는 것을 확인했습니다.

![Hello 실행](screenshots/02_hello_execution.png)

---

### 4-3. Git 버전 확인

다음 명령어로 Git 설치 상태와 버전을 확인했습니다.

```bash
git --version
```

![Git 버전](screenshots/03_Git_version.png)

---

### 4-4. Git 사용자 설정

Git 사용자 이름과 이메일을 설정하고 기본 브랜치 이름을 `main`으로 설정했습니다.

사용한 명령어:

```bash
git config --global user.name
git config --global user.email
git config --global init.defaultBranch main
```

![Git 설정](screenshots/04_Git_settings.png)

---

## 5. Git 저장소 초기화

프로젝트 폴더에서 다음 명령어를 사용하여 Git 저장소를 시작했습니다.

```bash
git init
```

파일을 Git 관리 대상으로 추가하고 첫 번째 커밋을 생성했습니다.

```bash
git add .
git commit -m "chore: initialize project"
```

![첫 Git 커밋](screenshots/05_Git_first_commit.png)

---

## 6. GitHub 원격 저장소 연결 및 Push

GitHub에 `python-prompt-manager` 저장소를 생성한 뒤 로컬 저장소와 연결했습니다.

사용한 주요 명령어:

```bash
git remote add origin https://github.com/ll-0l/python-prompt-manager.git
git remote -v
git push -u origin main
```

![Git Push](screenshots/06_Git_push.png)

GitHub 저장소에 `.gitignore`, `README.md`, `hello.py` 등의 파일이 정상적으로 업로드된 것을 확인했습니다.

![GitHub Repository](screenshots/07_GitHub_repository.png)

---

## 7. 프로그램 기능

프로그램 실행 시 다음 메뉴가 표시됩니다.

```text
=== 나만의 프롬프트 관리 ===
1. 프롬프트 추가
2. 프롬프트 목록
3. 카테고리별 조회
4. 프롬프트 검색
5. 프롬프트 상세 보기
6. 즐겨찾기 관리
7. 즐겨찾기 목록
0. 종료
```

---

### 7-1. 메인 메뉴 및 잘못된 입력 처리

사용자는 메뉴 번호를 입력하여 원하는 기능을 실행할 수 있습니다.

존재하지 않는 번호를 입력하면 오류 메시지를 출력하고 다시 메뉴로 돌아가도록 구현했습니다.

![메인 메뉴](screenshots/09_main_menu.png)

![잘못된 메뉴 입력](screenshots/10_invalid_menu_input.png)

---

### 7-2. 프롬프트 추가

사용자가 새로운 프롬프트의 제목, 내용, 카테고리를 입력하여 등록할 수 있습니다.

입력 항목:

* 제목
* 내용
* 카테고리
* 즐겨찾기 기본값: False

제목 또는 내용이 비어 있는 경우 다시 입력하도록 구현했습니다.

카테고리는 기본 목록에서 선택하거나 직접 입력할 수 있습니다.

![프롬프트 추가](screenshots/11_add_prompt.png)

---

### 7-3. 프롬프트 목록

저장된 모든 프롬프트를 번호와 함께 출력합니다.

각 항목에는 다음 정보가 표시됩니다.

* 번호
* 카테고리
* 제목
* 즐겨찾기 여부 ⭐

프로그램 실행 중 새롭게 추가한 프롬프트도 목록에서 유지되는 것을 확인했습니다.

![프롬프트 목록](screenshots/13_prompt_list.png)

---

### 7-4. 카테고리별 조회

카테고리 목록에서 번호를 선택하면 해당 카테고리에 속한 프롬프트만 출력합니다.

기본 카테고리는 다음과 같습니다.

1. 텍스트 생성
2. 이미지 생성
3. 영상 생성
4. 페르소나
5. 자동화
6. 기타

해당 카테고리에 프롬프트가 없는 경우 안내 메시지를 출력하도록 구현했습니다.

![카테고리별 조회](screenshots/15_category_filter.png)

---

### 7-5. 프롬프트 검색

검색어를 입력하면 프롬프트의 **제목 또는 내용**에 검색어가 포함되어 있는지 확인합니다.

예시로 `MODU`를 검색했을 때 관련 프롬프트 2개가 정상적으로 검색되는 것을 확인했습니다.

![프롬프트 검색](screenshots/16_prompt_search.png)

---

### 7-6. 프롬프트 상세 보기

프롬프트 번호를 입력하면 해당 프롬프트의 전체 정보를 출력합니다.

표시 정보:

* 제목
* 카테고리
* 즐겨찾기 여부
* 프롬프트 전체 내용

존재하지 않는 번호를 입력하면 오류 안내 메시지를 출력하도록 구현했습니다.

![프롬프트 상세 보기](screenshots/17_prompt_detail.png)

---

### 7-7. 즐겨찾기 관리

프롬프트 번호를 선택하여 즐겨찾기를 추가하거나 해제할 수 있습니다.

즐겨찾기로 설정된 프롬프트는 목록에서 ⭐ 표시가 나타납니다.

같은 프롬프트를 다시 선택하면 즐겨찾기가 해제됩니다.

![즐겨찾기 관리](screenshots/18_favorite_toggle.png)

---

### 7-8. 즐겨찾기 목록

즐겨찾기로 설정된 프롬프트만 따로 모아서 확인할 수 있습니다.

즐겨찾기가 없는 경우 별도의 안내 메시지를 출력하도록 구현했습니다.

![즐겨찾기 목록](screenshots/19_favorite_list.png)

---

## 8. 기본 프롬프트 데이터

프로그램 시작 시 이전 생성형 AI 미션에서 사용했던 프롬프트를 기본 데이터로 등록했습니다.

### 기본 프롬프트 1

* 제목: MODU 로고 이미지 생성
* 카테고리: 이미지 생성

### 기본 프롬프트 2

* 제목: MODU 앱 UI 이미지 생성
* 카테고리: 이미지 생성

### 기본 프롬프트 3

* 제목: 업무용 메일 초안 작성
* 카테고리: 텍스트 생성

총 3개의 기본 프롬프트가 프로그램 실행 시 자동으로 등록됩니다.

---

## 9. 데이터 구조

프롬프트는 리스트와 딕셔너리를 사용하여 저장했습니다.

예시:

```python
prompts = [
    {
        "title": "MODU 로고 이미지 생성",
        "content": "프롬프트 내용",
        "category": "이미지 생성",
        "favorite": False
    }
]
```

각 프롬프트는 다음 네 가지 정보를 포함합니다.

* `title`: 제목
* `content`: 프롬프트 내용
* `category`: 카테고리
* `favorite`: 즐겨찾기 여부

---

## 10. 함수 구조

모든 코드를 한 함수에 작성하지 않고 기능별로 분리했습니다.

주요 함수:

```text
add_prompt()
show_prompt_list()
show_by_category()
search_prompt()
show_prompt_detail()
toggle_favorite()
show_favorites()
show_menu()
main()
```

각 함수가 하나의 기능을 담당하도록 구성하여 코드의 가독성과 수정 편의성을 높였습니다.

---

## 11. Git 브랜치 활용

프롬프트 목록 기능은 과제 요구사항에 따라 `main` 브랜치가 아닌 별도 브랜치에서 개발했습니다.

브랜치 이름:

```text
feature/prompt-list
```

브랜치 생성 및 이동:

```bash
git checkout -b feature/prompt-list
```

![브랜치 생성](screenshots/12_Git_branch.png)

프롬프트 목록 기능을 해당 브랜치에서 구현한 뒤 다음 커밋을 생성했습니다.

```text
feat: add prompt list
```

기능 완성 후 `main` 브랜치로 돌아갔습니다.

```bash
git checkout main
```

이후 다음 명령어를 사용하여 `feature/prompt-list` 브랜치를 `main`에 병합했습니다.

```bash
git merge --no-ff feature/prompt-list -m "merge: add prompt list feature"
```

Git 그래프를 통해 브랜치가 분리되었다가 다시 `main`으로 병합된 것을 확인했습니다.

![Git Merge](screenshots/14_Git_merge.png)

---

## 12. Git Clone 실습

과제 요구사항에 따라 공개 GitHub 저장소를 `clone`하여 폴더 구조와 Git 로그를 확인했습니다.

사용한 저장소:

```text
octocat/Hello-World
```

사용 명령어:

```bash
git clone https://github.com/octocat/Hello-World.git
cd Hello-World
dir
git log --oneline --graph --all
```

확인 후 원래 프로젝트 폴더로 이동했습니다.

![Git Clone](screenshots/20_Git_clone.png)

---

## 13. 사용한 Git 명령어

이번 프로젝트에서 다음 Git 명령어를 실제로 사용했습니다.

### git init

현재 폴더에서 새로운 Git 저장소를 시작할 때 사용했습니다.

```bash
git init
```

### git add

변경된 파일을 다음 커밋 대상으로 추가할 때 사용했습니다.

```bash
git add prompt_manager.py
```

### git commit

현재 변경사항을 하나의 버전으로 저장할 때 사용했습니다.

```bash
git commit -m "feat: add prompt search"
```

### git push

로컬 저장소의 커밋을 GitHub 원격 저장소에 업로드할 때 사용했습니다.

```bash
git push origin main
```

### git pull

GitHub 원격 저장소의 최신 상태를 로컬로 가져올 때 사용했습니다.

```bash
git pull origin main
```

### git checkout

다른 브랜치로 이동하거나 새로운 브랜치를 생성할 때 사용했습니다.

```bash
git checkout -b feature/prompt-list
git checkout main
```

### git clone

공개 GitHub 저장소를 로컬 컴퓨터로 복제할 때 사용했습니다.

```bash
git clone https://github.com/octocat/Hello-World.git
```

### git merge

별도 브랜치에서 개발한 프롬프트 목록 기능을 `main` 브랜치에 병합할 때 사용했습니다.

```bash
git merge --no-ff feature/prompt-list -m "merge: add prompt list feature"
```

따라서 과제에서 요구한 Git 명령어를 모두 사용했습니다.

* git init ✅
* git add ✅
* git commit ✅
* git push ✅
* git pull ✅
* git checkout ✅
* git clone ✅
* git merge ✅

---

## 14. Git Commit 기록

프로젝트는 기능 단위로 나누어 커밋했습니다.

주요 커밋 예시는 다음과 같습니다.

```text
chore: initialize project
feat: add default prompt data
feat: add main menu
feat: add prompt creation
feat: add prompt list
merge: add prompt list feature
feat: add category filter
feat: add prompt search
feat: add prompt detail view
feat: add favorite toggle
feat: add favorite list
docs: complete README
docs: add project screenshots
```

GitHub 저장소에서 최소 10개 이상의 의미 있는 커밋이 존재하는 것을 확인했습니다.

최종 Git 그래프에서는 `feature/prompt-list` 브랜치에서 작업한 뒤 `main` 브랜치로 병합된 기록도 확인할 수 있습니다.

![최종 Git 로그](screenshots/22_Final_Git_log.png)

---

## 15. 최종 GitHub 저장소

최종 GitHub 저장소에는 다음 주요 파일과 폴더가 포함되어 있습니다.

```text
python-prompt-manager/
├── screenshots/
├── .gitignore
├── README.md
├── SUBMISSION.md
├── hello.py
└── prompt_manager.py
```

GitHub 저장소에 프로그램 코드, README 및 개발 과정 증빙 자료를 업로드했습니다.

![최종 GitHub 저장소](screenshots/21_GitHub_final.png)

---

## 16. 필수 요구사항 체크리스트

### 개발 환경

* [x] VSCode 사용
* [x] VSCode Python 확장 설치
* [x] Python 3.10 이상 사용
* [x] `print("Hello")` 코드 실행
* [x] Git 버전 확인
* [x] Git 사용자 이름 설정
* [x] Git 사용자 이메일 설정
* [x] 기본 브랜치 `main` 설정
* [x] GitHub 저장소 생성 및 연동

### Git / GitHub

* [x] GitHub 새 저장소 생성
* [x] `git init` 사용
* [x] `git add` 사용
* [x] `git commit` 사용
* [x] `git push` 사용
* [x] `git pull` 사용
* [x] `git checkout` 사용
* [x] `git clone` 사용
* [x] `git merge` 사용
* [x] `.gitignore` 작성
* [x] README.md 작성
* [x] 최소 10개 이상의 의미 있는 커밋
* [x] 추가 브랜치 생성
* [x] 별도 브랜치에서 프롬프트 목록 기능 구현
* [x] `main` 브랜치로 병합

### Python 프로그램

* [x] 기본 프롬프트 최소 3개
* [x] 리스트와 딕셔너리를 이용한 데이터 관리
* [x] 메인 메뉴 출력
* [x] 메뉴 번호 입력
* [x] 잘못된 메뉴 번호 처리
* [x] 종료 기능
* [x] 프롬프트 추가
* [x] 빈 입력값 검사
* [x] 카테고리 선택
* [x] 사용자 카테고리 직접 입력
* [x] 프롬프트 전체 목록
* [x] 카테고리별 조회
* [x] 프롬프트 검색
* [x] 검색 결과 없음 처리
* [x] 프롬프트 상세 보기
* [x] 잘못된 프롬프트 번호 처리
* [x] 즐겨찾기 추가
* [x] 즐겨찾기 해제
* [x] 즐겨찾기 목록
* [x] 기능별 함수 분리
* [x] 실행 중 데이터 유지
* [x] 프로그램 종료 시 데이터 초기화

### 제출 자료

* [x] GitHub 저장소 URL
* [x] 개발 환경 설정 스크린샷
* [x] 프로그램 메뉴 스크린샷
* [x] 프롬프트 추가 결과
* [x] 프롬프트 목록 결과
* [x] 카테고리별 조회 결과
* [x] 검색 결과
* [x] 상세 보기 결과
* [x] 즐겨찾기 결과
* [x] 브랜치 생성 기록
* [x] Merge 기록
* [x] Clone 기록
* [x] `git log --oneline --graph --all` 결과

---

## 17. 프로젝트 회고

이번 프로젝트를 통해 Python 프로그램이 단순히 코드를 작성하는 것에서 끝나는 것이 아니라 사용자의 입력을 받고 데이터를 저장하고 조건에 따라 서로 다른 기능을 실행하는 구조로 동작한다는 것을 이해할 수 있었습니다.

Python의 리스트와 딕셔너리를 사용하여 여러 프롬프트 데이터를 관리했으며, 조건문과 반복문을 이용하여 메뉴와 입력 검증 기능을 구현했습니다. 또한 기능별로 함수를 분리하면서 코드의 역할을 나누는 방법을 학습했습니다.

Git에서는 프로젝트를 한 번에 저장하는 것이 아니라 기능을 하나씩 완성할 때마다 커밋하여 개발 과정을 기록했습니다. 특히 `feature/prompt-list` 브랜치를 별도로 생성하여 프롬프트 목록 기능을 구현하고, 이후 `main` 브랜치에 병합하면서 브랜치 기반 개발 방식도 경험했습니다.

GitHub를 이용하여 로컬에서 작성한 코드를 원격 저장소에 업로드하고, `push`, `pull`, `clone` 등의 명령어를 직접 사용하면서 로컬 저장소와 원격 저장소의 차이도 이해할 수 있었습니다.

최종적으로 Python으로 아이디어를 실제 동작하는 콘솔 프로그램으로 구현하고 Git과 GitHub를 활용하여 개발 이력을 관리하는 전체 과정을 경험했습니다.

---

# 최종 제출 정보

**프로젝트명:** Python Prompt Manager

**GitHub Repository:**
https://github.com/ll-0l/python-prompt-manager

**최종 제출 파일:**
`SUBMISSION.md`
