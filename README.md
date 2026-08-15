# Python Prompt Manager

Python 기본 문법을 활용하여 만든 **콘솔 기반 프롬프트 관리 프로그램**입니다.

생성형 AI 미션을 수행하면서 작성한 여러 프롬프트를 한곳에서 관리하기 위해 제작했습니다.

프로그램을 통해 프롬프트를 추가하고 전체 목록을 확인할 수 있으며, 카테고리별 조회, 키워드 검색, 상세 보기, 즐겨찾기 추가·해제 및 즐겨찾기 목록 확인 기능을 사용할 수 있습니다.

프롬프트 데이터는 Python의 리스트(List)와 딕셔너리(Dictionary)를 사용하여 관리합니다.

프로그램 실행 중 추가한 프롬프트와 즐겨찾기 상태는 유지되며, 프로그램을 종료하면 기본 데이터 상태로 초기화됩니다.

---

## 최종 제출 문서

과제의 전체 구현 내용, 개발 환경, Git/GitHub 사용 기록, 기능별 실행 결과 및 증빙 스크린샷은 아래 문서에서 확인할 수 있습니다.

➡️ **[SUBMISSION.md 바로가기](SUBMISSION.md)**

---

## GitHub Repository

**Repository**

https://github.com/ll-0l/python-prompt-manager

저장소 공개 범위: **Public**

---

## 개발 환경

* 운영체제: Windows
* 개발 도구: Visual Studio Code
* Python: 3.14.7
* Python 요구 버전: 3.10 이상
* Git: 2.55.0.windows.3
* 버전 관리: Git / GitHub
* 외부 Python 라이브러리: 사용하지 않음

---

## 실행 방법

### 1. 저장소 Clone

GitHub 저장소를 컴퓨터로 내려받습니다.

```bash
git clone https://github.com/ll-0l/python-prompt-manager.git
```

### 2. 프로젝트 폴더로 이동

```bash
cd python-prompt-manager
```

### 3. 프로그램 실행

Windows 환경에서는 다음 명령어를 사용할 수 있습니다.

```bash
py prompt_manager.py
```

환경에 따라 다음 명령어를 사용할 수도 있습니다.

```bash
python prompt_manager.py
```

---

## 프로그램 메뉴

프로그램을 실행하면 다음과 같은 메뉴가 표시됩니다.

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
선택:
```

사용자는 원하는 기능의 번호를 입력하여 프로그램을 사용할 수 있습니다.

---

# 주요 기능

## 1. 프롬프트 추가

새로운 프롬프트를 프로그램에 등록할 수 있습니다.

입력 항목:

* 제목
* 내용
* 카테고리

제목이나 내용을 입력하지 않고 Enter를 누르면 다시 입력하도록 안내합니다.

카테고리는 기본 목록에서 선택하거나 새로운 카테고리를 직접 입력할 수 있습니다.

새로운 프롬프트가 추가되면 즐겨찾기 기본값은 `False`로 저장됩니다.

---

## 2. 프롬프트 목록

현재 저장되어 있는 모든 프롬프트를 번호와 함께 출력합니다.

각 프롬프트에는 다음 내용이 표시됩니다.

* 번호
* 카테고리
* 제목
* 즐겨찾기 여부 ⭐

프로그램 실행 중 새로 추가한 프롬프트도 목록에서 확인할 수 있습니다.

---

## 3. 카테고리별 조회

카테고리 목록을 출력하고 사용자가 선택한 카테고리에 해당하는 프롬프트만 보여줍니다.

해당 카테고리에 등록된 프롬프트가 없는 경우 안내 메시지를 출력합니다.

---

## 4. 프롬프트 검색

사용자가 입력한 키워드를 기준으로 프롬프트를 검색합니다.

검색 대상:

* 프롬프트 제목
* 프롬프트 내용

검색 결과가 존재하면 해당 프롬프트 목록을 출력합니다.

검색 결과가 없으면 별도의 안내 메시지를 출력합니다.

---

## 5. 프롬프트 상세 보기

사용자가 프롬프트 번호를 입력하면 해당 프롬프트의 전체 정보를 보여줍니다.

출력 정보:

* 제목
* 카테고리
* 즐겨찾기 여부
* 프롬프트 전체 내용

존재하지 않는 번호를 입력하면 안내 메시지를 출력합니다.

---

## 6. 즐겨찾기 관리

프롬프트 번호를 입력하여 즐겨찾기를 추가하거나 해제할 수 있습니다.

즐겨찾기가 설정된 프롬프트는 목록에서 ⭐ 표시로 확인할 수 있습니다.

이미 즐겨찾기된 프롬프트를 다시 선택하면 즐겨찾기가 해제됩니다.

---

## 7. 즐겨찾기 목록

즐겨찾기로 등록된 프롬프트만 따로 모아서 출력합니다.

즐겨찾기된 프롬프트가 하나도 없는 경우 안내 메시지를 출력합니다.

---

## 8. 잘못된 입력 처리

메인 메뉴에서 존재하지 않는 번호를 입력하면 오류 안내 메시지를 출력하고 다시 메뉴를 보여줍니다.

프롬프트 번호, 카테고리 번호 등에서도 잘못된 입력을 검사하도록 구현했습니다.

---

## 9. 프로그램 종료

메인 메뉴에서 `0`을 입력하면 프로그램을 종료합니다.

프로그램 실행 중 추가된 프롬프트와 변경된 즐겨찾기 상태는 프로그램을 종료하면 초기화됩니다.

---

# 프롬프트 카테고리

프로그램에서 기본적으로 제공하는 카테고리는 다음과 같습니다.

1. 텍스트 생성
2. 이미지 생성
3. 영상 생성
4. 페르소나
5. 자동화
6. 기타

프롬프트 추가 기능에서는 사용자가 새로운 카테고리를 직접 입력할 수도 있습니다.

---

# 기본 프롬프트 데이터

프로그램 시작 시 이전 생성형 AI 미션에서 활용한 프롬프트 3개가 기본 데이터로 등록됩니다.

## 1. MODU 로고 이미지 생성

* 카테고리: 이미지 생성
* MODU 생산성 AI 앱의 로고 이미지를 생성하기 위한 프롬프트

## 2. MODU 앱 UI 이미지 생성

* 카테고리: 이미지 생성
* MODU 생산성 앱의 스마트폰 UI 이미지를 생성하기 위한 프롬프트

## 3. 업무용 메일 초안 작성

* 카테고리: 텍스트 생성
* 교육운영팀의 업무용 안내 메일 초안을 작성하기 위한 프롬프트

총 **3개의 기본 프롬프트**가 프로그램 시작 시 자동으로 등록됩니다.

---

# 데이터 구조

프롬프트 데이터는 Python의 **리스트(List)** 와 **딕셔너리(Dictionary)** 를 사용하여 관리합니다.

각 프롬프트는 다음과 같은 형태로 구성됩니다.

```python
{
    "title": "프롬프트 제목",
    "content": "프롬프트 내용",
    "category": "텍스트 생성",
    "favorite": False
}
```

여러 프롬프트는 하나의 리스트에 저장됩니다.

```python
prompts = [
    {
        "title": "프롬프트 제목",
        "content": "프롬프트 내용",
        "category": "텍스트 생성",
        "favorite": False
    }
]
```

각 프롬프트가 가지고 있는 정보:

* `title` : 프롬프트 제목
* `content` : 프롬프트 내용
* `category` : 프롬프트 카테고리
* `favorite` : 즐겨찾기 여부

---

# 함수 구조

모든 코드를 하나의 함수에 작성하지 않고 기능별로 함수를 분리했습니다.

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

각 함수가 하나의 주요 기능을 담당하도록 구성했습니다.

이를 통해 코드의 역할을 구분하고 수정 및 관리가 쉽도록 구현했습니다.

---

# Git / GitHub 활용

프로젝트는 Git을 이용하여 기능 단위로 변경 이력을 관리하고 GitHub에 업로드했습니다.

주요 기능을 완성할 때마다 별도의 커밋을 생성했습니다.

---

## Git 저장소 초기화

프로젝트 폴더에서 다음 명령어를 사용하여 Git 저장소를 시작했습니다.

```bash
git init
```

변경된 파일을 Git 관리 대상으로 추가했습니다.

```bash
git add .
```

변경사항을 커밋으로 저장했습니다.

```bash
git commit -m "chore: initialize project"
```

---

## GitHub 원격 저장소 연결

로컬 저장소와 GitHub 저장소를 연결했습니다.

```bash
git remote add origin https://github.com/ll-0l/python-prompt-manager.git
```

원격 저장소 연결 상태를 확인했습니다.

```bash
git remote -v
```

GitHub에 커밋을 업로드했습니다.

```bash
git push -u origin main
```

---

# Git 브랜치 활용

과제 요구사항에 따라 **프롬프트 목록 기능**은 `main` 브랜치에서 바로 개발하지 않고 별도의 브랜치에서 구현했습니다.

사용한 브랜치:

```text
feature/prompt-list
```

브랜치 생성 및 이동:

```bash
git checkout -b feature/prompt-list
```

`feature/prompt-list` 브랜치에서 프롬프트 목록 기능을 구현한 뒤 다음 커밋을 생성했습니다.

```text
feat: add prompt list
```

기능 구현이 완료된 후 다시 `main` 브랜치로 이동했습니다.

```bash
git checkout main
```

이후 프롬프트 목록 기능을 `main` 브랜치에 병합했습니다.

```bash
git merge --no-ff feature/prompt-list -m "merge: add prompt list feature"
```

이를 통해 브랜치를 생성하고 별도의 기능을 개발한 뒤 다시 `main` 브랜치에 병합하는 과정을 수행했습니다.

---

# 사용한 Git 명령어

이번 프로젝트에서 과제에서 요구한 다음 Git 명령어를 모두 실제로 사용했습니다.

```text
git init
git add
git commit
git push
git pull
git checkout
git clone
git merge
```

### git init

현재 폴더에서 새로운 Git 저장소를 시작합니다.

```bash
git init
```

### git add

변경된 파일을 다음 커밋에 포함할 준비 상태로 만듭니다.

```bash
git add prompt_manager.py
```

### git commit

현재 변경사항을 하나의 버전으로 기록합니다.

```bash
git commit -m "feat: add prompt search"
```

### git push

로컬 Git 저장소의 커밋을 GitHub 원격 저장소에 업로드합니다.

```bash
git push origin main
```

### git pull

GitHub 원격 저장소의 최신 내용을 로컬 저장소로 가져옵니다.

```bash
git pull origin main
```

### git checkout

다른 브랜치로 이동하거나 새로운 브랜치를 만들 때 사용합니다.

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

별도 브랜치에서 개발한 기능을 `main` 브랜치에 병합했습니다.

```bash
git merge --no-ff feature/prompt-list -m "merge: add prompt list feature"
```

---

# Git Commit 관리

프로젝트는 기능 단위로 나누어 커밋했습니다.

주요 커밋:

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

최소 10개 이상의 의미 있는 커밋을 생성하여 과제 요구사항을 충족했습니다.

---

# Git Clone 실습

과제 요구사항에 따라 공개 GitHub 저장소를 직접 Clone하여 폴더 구조와 Git 로그를 확인했습니다.

사용한 공개 저장소:

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

확인 후 원래 프로젝트 폴더로 돌아왔습니다.

---

# 프로젝트 구조

```text
python-prompt-manager/
│
├── screenshots/
│   ├── 01_Python_version.png
│   ├── 02_hello_execution.png
│   ├── 03_Git_version.png
│   ├── 04_Git_settings.png
│   ├── 05_Git_first_commit.png
│   ├── 06_Git_push.png
│   ├── 07_GitHub_repository.png
│   ├── 09_main_menu.png
│   ├── 10_invalid_menu_input.png
│   ├── 11_add_prompt.png
│   ├── 12_Git_branch.png
│   ├── 13_prompt_list.png
│   ├── 14_Git_merge.png
│   ├── 15_category_filter.png
│   ├── 16_prompt_search.png
│   ├── 17_prompt_detail.png
│   ├── 18_favorite_toggle.png
│   ├── 19_favorite_list.png
│   ├── 20_Git_clone.png
│   ├── 21_GitHub_final.png
│   └── 22_Final_Git_log.png
│
├── .gitignore
├── README.md
├── SUBMISSION.md
├── hello.py
└── prompt_manager.py
```

---

# 파일 설명

### `prompt_manager.py`

프롬프트 관리 프로그램의 메인 Python 파일입니다.

프롬프트 추가, 목록, 검색, 카테고리 조회, 상세 보기 및 즐겨찾기 기능이 구현되어 있습니다.

### `hello.py`

Python 개발 환경과 실행 방법을 확인하기 위해 작성한 연습 파일입니다.

```python
print("Hello")
```

코드를 실행하여 Python 설치 상태를 확인했습니다.

### `README.md`

프로그램 설명, 실행 방법, 주요 기능, 데이터 구조, Git/GitHub 활용 내용을 정리한 프로젝트 설명 문서입니다.

### `SUBMISSION.md`

과제의 최종 제출 문서입니다.

다음 내용을 포함합니다.

* 개발 환경
* GitHub Repository
* 기능별 구현 내용
* 프로그램 실행 결과
* Git 명령어 사용 기록
* 브랜치 생성 및 Merge 기록
* Clone 기록
* Git Commit 기록
* 과제 요구사항 체크리스트
* 프로젝트 회고
* 증빙 스크린샷

➡️ **[SUBMISSION.md 바로가기](SUBMISSION.md)**

### `.gitignore`

Git으로 관리할 필요가 없는 Python 임시 파일 등을 제외하기 위한 설정 파일입니다.

### `screenshots/`

프로젝트 개발 과정과 프로그램 실행 결과를 증빙하기 위한 이미지가 저장되어 있습니다.

---

# 프로그램 데이터 저장 방식

필수 과제 범위에서는 데이터베이스나 외부 라이브러리를 사용하지 않습니다.

프롬프트 데이터는 프로그램 실행 중 Python 리스트에 저장됩니다.

따라서 프로그램을 실행하고 있는 동안에는:

* 새로 추가한 프롬프트
* 변경한 즐겨찾기 상태

가 유지됩니다.

프로그램을 종료하고 다시 실행하면 기본 프롬프트 3개가 등록된 초기 상태로 돌아갑니다.

---

# 프로젝트를 통해 학습한 내용

이번 프로젝트를 통해 다음 내용을 직접 적용했습니다.

* VSCode에서 Python 파일 생성
* Python 파일 실행
* Python 기본 문법
* 리스트와 딕셔너리
* 조건문
* 반복문
* 함수
* 사용자 입력 처리
* 데이터 검색 및 필터링
* Git 저장소 초기화
* 기능 단위 Commit
* GitHub Push / Pull
* Git Branch 생성
* 별도 Branch 기능 개발
* Git Merge
* 공개 저장소 Clone
* Git 로그 확인
* GitHub 프로젝트 관리

---

# 실행 예시

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
선택: 2

=== 프롬프트 목록 ===
1. [이미지 생성] MODU 로고 이미지 생성
2. [이미지 생성] MODU 앱 UI 이미지 생성
3. [텍스트 생성] 업무용 메일 초안 작성

총 3개의 프롬프트
```

---

# 최종 제출

과제의 상세 구현 내용과 전체 증빙 자료는 `SUBMISSION.md`에서 확인할 수 있습니다.

➡️ **[최종 제출 문서 보기](SUBMISSION.md)**

GitHub Repository:

https://github.com/ll-0l/python-prompt-manager
