# Python Prompt Manager

Python 기본 문법을 활용하여 만든 **콘솔 기반 프롬프트 관리 프로그램**입니다.

생성형 AI 미션을 수행하면서 작성한 여러 프롬프트를 한곳에서 관리하기 위해 제작했습니다.

프로그램에서는 프롬프트 추가, 전체 목록 조회, 카테고리별 조회, 키워드 검색, 상세 보기, 즐겨찾기 추가·해제, 즐겨찾기 목록 기능을 사용할 수 있습니다.

프롬프트 데이터는 Python의 **리스트(List)** 와 **딕셔너리(Dictionary)** 를 사용하여 관리합니다.

필수 과제 범위에서는 프로그램 실행 중 추가한 프롬프트와 즐겨찾기 상태가 유지되며, 프로그램을 종료하면 기본 데이터 상태로 초기화됩니다.

---

## 최종 제출 문서

과제의 전체 구현 내용, 개발 환경, Git/GitHub 사용 기록, 실행 결과 및 증빙 자료는 아래 문서에서 확인할 수 있습니다.

➡️ **[SUBMISSION.md 바로가기](SUBMISSION.md)**

---

## GitHub Repository

https://github.com/ll-0l/python-prompt-manager

저장소 공개 범위: **Public**

---

# 개발 환경

* 운영체제: Windows
* 개발 도구: Visual Studio Code
* Python: 3.14.7
* 요구 버전: Python 3.10 이상
* Git: 2.55.0.windows.3
* 버전 관리: Git / GitHub
* 외부 Python 라이브러리: 사용하지 않음

## Python 버전 확인

```bash
py --version
```

환경에 따라 다음 명령도 사용할 수 있습니다.

```bash
python -V
```

프로젝트에서는 Python 3.14.7을 사용하여 과제 조건인 Python 3.10 이상을 충족했습니다.

![Python 버전](screenshots/01_Python_version.png)

## Git 버전 확인

```bash
git --version
```

![Git 버전](screenshots/03_Git_version.png)

## Python 기본 실행 확인

`hello.py`에 다음 코드를 작성했습니다.

```python
print("Hello")
```

실행:

```bash
py hello.py
```

![Hello 실행](screenshots/02_hello_execution.png)

---

# 실행 방법

## 1. 저장소 Clone

```bash
git clone https://github.com/ll-0l/python-prompt-manager.git
```

## 2. 프로젝트 폴더 이동

```bash
cd python-prompt-manager
```

## 3. 프로그램 실행

```bash
py prompt_manager.py
```

환경에 따라:

```bash
python prompt_manager.py
```

를 사용할 수도 있습니다.

---

# 프로그램 메뉴

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

사용자가 기능을 실행한 후 프로그램이 바로 종료되지 않고 다시 메뉴로 돌아갈 수 있도록 반복 구조로 설계했습니다.

---

# 주요 기능

## 1. 프롬프트 추가

사용자가 다음 정보를 입력하여 새로운 프롬프트를 등록합니다.

* 제목
* 내용
* 카테고리

제목 또는 내용이 비어 있으면 다시 입력하도록 요청합니다.

카테고리는 기본 목록에서 선택하거나 직접 입력할 수 있습니다.

새 프롬프트의 즐겨찾기 기본값은 `False`입니다.

---

## 2. 프롬프트 목록

저장된 모든 프롬프트를 번호와 함께 출력합니다.

표시 내용:

* 번호
* 카테고리
* 제목
* 즐겨찾기 여부 ⭐

프로그램 실행 중 새롭게 추가한 프롬프트도 목록에 유지됩니다.

---

## 3. 카테고리별 조회

카테고리를 선택하면 해당 카테고리에 속한 프롬프트만 출력합니다.

해당 카테고리에 프롬프트가 없으면 안내 메시지를 출력합니다.

---

## 4. 프롬프트 검색

검색어가 프롬프트의 **제목 또는 내용에 포함되어 있는지 확인하는 부분 문자열 검색** 방식입니다.

핵심 로직:

```python
keyword.lower() in prompt["title"].lower()
```

및

```python
keyword.lower() in prompt["content"].lower()
```

영문 검색 시 `lower()`를 사용하여 대소문자의 영향을 줄였습니다.

예를 들어 `MODU`, `modu`, `Modu`를 동일한 방식으로 검색할 수 있습니다.

현재 검색 방식은 다음 기능을 지원하지 않습니다.

* 정규표현식 검색
* 정확 일치 전용 검색
* 검색 관련도 정렬
* AND / OR 복합 검색

향후 정확 검색과 부분 검색을 선택할 수 있도록 확장할 수 있습니다.

---

## 5. 프롬프트 상세 보기

프롬프트 번호를 입력하면 다음 정보를 출력합니다.

* 제목
* 카테고리
* 즐겨찾기 여부
* 프롬프트 전체 내용

숫자가 아닌 값을 입력하거나 존재하지 않는 번호를 입력하면 안내 메시지를 출력합니다.

---

## 6. 즐겨찾기 관리

프롬프트 번호를 선택하면 즐겨찾기를 추가하거나 해제합니다.

내부적으로 다음 방식으로 상태를 변경합니다.

```python
prompt["favorite"] = not prompt["favorite"]
```

따라서 `False → True`, 다시 실행하면 `True → False`로 변경됩니다.

---

## 7. 즐겨찾기 목록

`favorite` 값이 `True`인 프롬프트만 별도로 출력합니다.

즐겨찾기가 하나도 없으면 별도의 안내 메시지를 출력합니다.

---

# 기본 프롬프트 데이터

프로그램 실행 시 이전 생성형 AI 미션에서 활용한 프롬프트 3개가 기본 등록됩니다.

1. MODU 로고 이미지 생성

   * 카테고리: 이미지 생성

2. MODU 앱 UI 이미지 생성

   * 카테고리: 이미지 생성

3. 업무용 메일 초안 작성

   * 카테고리: 텍스트 생성

---

# 프롬프트 카테고리

기본 카테고리는 다음과 같습니다.

1. 텍스트 생성
2. 이미지 생성
3. 영상 생성
4. 페르소나
5. 자동화
6. 기타

프롬프트 추가 시 사용자가 새로운 카테고리를 직접 입력할 수도 있습니다.

---

# 데이터 구조

프롬프트는 Python의 리스트와 딕셔너리를 조합하여 관리합니다.

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

## 데이터 스키마

| 필드         | 자료형    | 필수 여부 | 설명         |
| ---------- | ------ | ----- | ---------- |
| `title`    | `str`  | 필수    | 프롬프트 제목    |
| `content`  | `str`  | 필수    | 프롬프트 전체 내용 |
| `category` | `str`  | 필수    | 프롬프트 분류    |
| `favorite` | `bool` | 필수    | 즐겨찾기 상태    |

제목, 내용, 카테고리는 빈 값을 허용하지 않으며 즐겨찾기의 초기값은 `False`입니다.

---

# 리스트와 딕셔너리를 선택한 이유

## 리스트(List)

여러 프롬프트를 **등록된 순서대로 저장하고 순차적으로 출력하기 쉽기 때문**에 리스트를 사용했습니다.

새로운 프롬프트를 추가할 때도:

```python
prompts.append(new_prompt)
```

처럼 간단하게 처리할 수 있습니다.

### 장점

* 입력 순서를 유지하기 쉬움
* 반복문으로 전체 데이터 조회가 쉬움
* `append()`를 이용한 데이터 추가가 간단함
* 초보자가 프로그램 흐름을 이해하기 쉬움

### 단점

검색이나 중복 확인 시 리스트 전체를 순차적으로 확인하기 때문에 데이터가 매우 많아지면 처리 시간이 증가할 수 있습니다.

---

## 딕셔너리(Dictionary)

하나의 프롬프트에는 제목, 내용, 카테고리, 즐겨찾기처럼 서로 의미가 다른 정보가 존재합니다.

딕셔너리를 사용하면 다음과 같이 키 이름으로 데이터의 의미를 명확하게 표현할 수 있습니다.

```python
prompt["title"]
prompt["content"]
prompt["category"]
prompt["favorite"]
```

### 장점

* 각 데이터의 의미가 명확함
* 필드 접근이 직관적임
* 새로운 속성을 추가하기 쉬움

### 단점

데이터 구조가 복잡해질 경우 필드 이름과 데이터 형식을 별도로 관리해야 합니다.

현재 과제 규모에서는 데이터 수가 많지 않기 때문에 **단순하고 이해하기 쉬운 리스트 + 딕셔너리 구조**를 선택했습니다.

실제 서비스 규모로 확장된다면 고유 ID와 데이터베이스를 사용하는 구조가 더 적합할 수 있습니다.

---

# 중복 제목 처리 규칙

동일한 제목의 프롬프트가 이미 존재하더라도 기존 데이터를 덮어쓰지 않습니다.

새로운 프롬프트 제목에 번호를 자동으로 추가합니다.

예:

```text
MODU 로고 이미지 생성
MODU 로고 이미지 생성 (2)
MODU 로고 이미지 생성 (3)
```

이를 통해 같은 제목을 가진 프롬프트도 기존 데이터를 삭제하지 않고 각각 별도로 관리할 수 있습니다.

목록과 상세 보기에서는 프롬프트 번호를 사용하므로 같은 이름이 존재해도 개별적으로 선택할 수 있습니다.

---

# 카테고리 충돌 처리 규칙

사용자가 `직접 입력`을 선택하여 입력한 카테고리가 기존 카테고리와 동일한 경우 중복 카테고리를 새로 생성하지 않고 **기존 카테고리를 재사용**합니다.

예를 들어 이미 다음 카테고리가 존재한다고 가정합니다.

```text
이미지 생성
```

사용자가 직접 입력으로 다시:

```text
이미지 생성
```

을 입력하면 기존 `이미지 생성` 카테고리를 사용합니다.

영문 카테고리의 경우 대소문자를 무시하여 기존 이름과 비교합니다.

예:

```text
Image
image
IMAGE
```

를 같은 이름으로 판단할 수 있도록 비교합니다.

---

# 입력 검증 설계

사용자가 잘못된 값을 입력해도 프로그램이 중단되지 않도록 여러 입력 검증을 적용했습니다.

처리 대상:

* 메인 메뉴의 잘못된 번호
* 제목 빈 입력
* 내용 빈 입력
* 카테고리 잘못된 번호
* 카테고리 빈 입력
* 빈 검색어
* 검색 결과 없음
* 상세 보기의 문자 입력
* 존재하지 않는 상세 보기 번호
* 즐겨찾기의 문자 입력
* 존재하지 않는 즐겨찾기 번호

현재는 각 기능 내부에서 직접 검증하고 있습니다.

프로그램이 더 커진다면 다음과 같은 공통 입력 검증 함수를 만들어 중복을 줄일 수 있습니다.

```text
get_valid_number()
get_non_empty_input()
```

---

# 메인 반복문 설계

프로그램은 하나의 기능을 사용한 뒤 종료하지 않고 다시 메뉴로 돌아갈 수 있어야 합니다.

따라서 `main()` 함수에서 `while True`를 사용했습니다.

```python
while True:
    show_menu()
    choice = input("선택: ").strip()
```

사용자가 `0`을 입력하면:

```python
if choice == "0":
    print("프로그램을 종료합니다.")
    break
```

를 실행하여 반복을 종료합니다.

즉 사용자가 명시적으로 종료를 선택하기 전까지 프로그램을 계속 사용할 수 있는 **대화형 콘솔 프로그램 구조**입니다.

---

# 데이터 영속화 설계

현재 필수 과제에서는 프로그램 실행 중 데이터만 유지하도록 구현했습니다.

현재 흐름:

```text
프로그램 실행
↓
기본 프롬프트 3개 생성
↓
prompts 리스트에 데이터 저장
↓
프롬프트 추가 / 즐겨찾기 변경
↓
프로그램 실행 중 상태 유지
↓
프로그램 종료
↓
메모리 데이터 초기화
```

이는 과제 필수 요구사항인 **“프로그램 실행 중에는 데이터가 유지되고 종료 시 초기화”** 조건에 맞춘 설계입니다.

---

## 향후 JSON 영속화

프로그램을 종료한 후에도 프롬프트를 유지해야 한다면 Python 기본 라이브러리의 `json`을 사용할 수 있습니다.

예상 저장 파일:

```text
prompts.json
```

예상 구조:

```json
[
    {
        "title": "MODU 로고 이미지 생성",
        "content": "프롬프트 내용",
        "category": "이미지 생성",
        "favorite": true
    }
]
```

확장 흐름:

```text
프로그램 실행
↓
prompts.json 존재 여부 확인
↓
JSON 데이터 불러오기
↓
prompts 리스트 구성
↓
프롬프트 추가 / 수정 / 즐겨찾기 변경
↓
prompts.json 다시 저장
↓
다음 실행에서도 데이터 유지
```

JSON을 우선 고려하는 이유는 현재 사용 중인 리스트와 딕셔너리 구조를 자연스럽게 표현할 수 있고 별도의 외부 라이브러리가 필요하지 않기 때문입니다.

데이터의 양이 많아지고 수정·삭제·정렬·복합 검색이 중요해진다면 **SQLite**와 같은 데이터베이스 사용을 고려할 수 있습니다.

---

# 함수 구조

코드를 한 곳에 몰아서 작성하지 않고 기능별로 함수를 나눴습니다.

| 함수                     | 역할                 |
| ---------------------- | ------------------ |
| `add_prompt()`         | 프롬프트 추가 및 중복 제목 처리 |
| `show_prompt_list()`   | 전체 프롬프트 목록 출력      |
| `show_by_category()`   | 카테고리별 필터링          |
| `search_prompt()`      | 제목 또는 내용 키워드 검색    |
| `show_prompt_detail()` | 프롬프트 상세 정보 출력      |
| `toggle_favorite()`    | 즐겨찾기 추가·해제         |
| `show_favorites()`     | 즐겨찾기 목록 출력         |
| `show_menu()`          | 메인 메뉴 출력           |
| `main()`               | 전체 프로그램 실행 흐름 관리   |

---

# Git / GitHub 활용

프로젝트는 Git을 이용하여 기능 단위로 버전을 관리했습니다.

사용한 주요 명령어:

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

---

# 주요 Git 명령어 설명

## git init

현재 폴더에서 Git 저장소를 시작합니다.

```bash
git init
```

## git add

변경된 파일을 다음 커밋 대상으로 준비합니다.

```bash
git add prompt_manager.py
```

## git commit

변경사항을 하나의 버전으로 기록합니다.

```bash
git commit -m "feat: add prompt search"
```

## git push

로컬의 커밋을 GitHub 원격 저장소에 업로드합니다.

```bash
git push origin main
```

## git pull

원격 저장소의 최신 내용을 가져옵니다.

```bash
git pull origin main
```

## git checkout

새로운 브랜치를 만들거나 다른 브랜치로 이동합니다.

```bash
git checkout -b feature/prompt-list
git checkout main
```

## git clone

공개 저장소를 로컬 컴퓨터로 복제합니다.

```bash
git clone https://github.com/octocat/Hello-World.git
```

## git merge

별도 브랜치의 변경사항을 현재 브랜치에 합칩니다.

```bash
git merge --no-ff feature/prompt-list -m "merge: add prompt list feature"
```

---

# Git 브랜치 활용

프롬프트 목록 기능은 과제 요구사항에 따라 `main` 브랜치에서 직접 개발하지 않고 별도의 브랜치에서 작업했습니다.

브랜치 이름:

```text
feature/prompt-list
```

생성:

```bash
git checkout -b feature/prompt-list
```

목록 기능 구현 후 커밋:

```text
feat: add prompt list
```

이후:

```bash
git checkout main
```

으로 `main`에 돌아왔습니다.

병합:

```bash
git merge --no-ff feature/prompt-list -m "merge: add prompt list feature"
```

## 브랜치를 분리한 이유

새로운 기능 개발 과정에서 안정적인 `main` 코드와 작업 중인 기능 코드를 분리하기 위해 사용했습니다.

브랜치 사용 기준은 다음과 같습니다.

```text
새로운 독립 기능 개발
↓
feature 브랜치 생성
↓
기능 구현 및 테스트
↓
기능 단위 commit
↓
main으로 이동
↓
검증된 기능 merge
```

이를 통해 새로운 기능을 개발하는 동안 `main`의 기존 동작 상태를 보호할 수 있습니다.

![브랜치 생성](screenshots/12_Git_branch.png)

![Git Merge](screenshots/14_Git_merge.png)

---

# Git Clone 실습

공개 저장소를 직접 Clone하여 폴더 구조와 Git 로그를 확인했습니다.

사용 저장소:

```text
octocat/Hello-World
```

실행:

```bash
git clone https://github.com/octocat/Hello-World.git
cd Hello-World
dir
git log --oneline --graph --all
```

![Git Clone](screenshots/20_Git_clone.png)

---

# 주요 Commit 기록

기능 단위로 커밋을 생성했습니다.

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
fix: handle duplicate prompt conflicts
```

10개 이상의 의미 있는 커밋을 생성했습니다.

최종 Git 기록은 다음 명령으로 확인할 수 있습니다.

```bash
git log --oneline --graph --all
```

![최종 Git 로그](screenshots/22_Final_Git_log.png)

---

# 프로젝트 구조

```text
python-prompt-manager/
│
├── screenshots/
├── .gitignore
├── README.md
├── SUBMISSION.md
├── hello.py
└── prompt_manager.py
```

---

# 향후 개선 방향

현재 프로그램은 Python 기본 문법과 Git/GitHub의 기본 흐름을 직접 학습하는 것을 목표로 구현했습니다.

향후 다음과 같은 기능을 추가할 수 있습니다.

* JSON 파일 저장 및 불러오기
* SQLite 데이터베이스 적용
* 프롬프트 수정
* 프롬프트 삭제
* 프롬프트 고유 ID
* 조회 횟수 기록
* 조회수 Top 목록
* 태그 기능
* 정확 검색 / 부분 검색 선택
* 검색 관련도 정렬
* 공통 입력 검증 함수
* GUI 프로그램
* 웹 기반 프롬프트 관리 서비스

---

# 최종 제출

과제의 상세 구현 내용과 전체 증빙 자료는 `SUBMISSION.md`에서 확인할 수 있습니다.

➡️ **[최종 제출 문서 보기](SUBMISSION.md)**

GitHub Repository:

https://github.com/ll-0l/python-prompt-manager
