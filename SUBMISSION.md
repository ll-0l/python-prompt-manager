# Python Prompt Manager 최종 제출

## 1. 프로젝트 개요

Python 기본 문법과 Git/GitHub를 활용하여 제작한 **콘솔 기반 프롬프트 관리 프로그램**입니다.

생성형 AI 미션에서 사용한 여러 프롬프트를 한곳에서 관리할 수 있도록 구현했습니다.

필수 기능으로 다음 기능을 구현했습니다.

- 프롬프트 추가
- 전체 프롬프트 목록
- 카테고리별 조회
- 제목·내용 검색
- 프롬프트 상세 보기
- 즐겨찾기 추가 및 해제
- 즐겨찾기 목록
- 입력값 검증
- 중복 제목 처리
- 카테고리 충돌 처리

추가로 선택 보너스 과제도 모두 구현했습니다.

### 보너스 1

- JSON 파일 저장
- JSON 파일 불러오기
- 프로그램 종료 후 데이터 유지
- 카테고리별 Markdown 파일 내보내기

### 보너스 2

- 프롬프트 수정
- 프롬프트 삭제
- 상세 보기 조회수 기록
- 조회수 기준 TOP 목록

---

# 2. GitHub Repository

GitHub Repository:

https://github.com/ll-0l/python-prompt-manager

저장소 공개 범위:

**Public**

---

# 3. 개발 환경

- 운영체제: Windows
- 개발 도구: Visual Studio Code
- Python: 3.14.7
- Python 요구 버전: 3.10 이상
- Git: 2.55.0.windows.3
- 버전 관리: Git / GitHub
- 외부 Python 라이브러리: 사용하지 않음

Python 버전 확인:

```bash
py --version
```

환경에 따라:

```bash
python -V
```

Git 버전 확인:

```bash
git --version
```

---

# 4. 개발 환경 증빙

## 4-1. Python 버전

![Python 버전 확인](screenshots/01_Python_version.png)

Python 3.14.7을 사용하여 과제 요구 조건인 Python 3.10 이상을 충족했습니다.

---

## 4-2. Python 기본 실행

`hello.py` 파일에 다음 코드를 작성했습니다.

```python
print("Hello")
```

실행:

```bash
py hello.py
```

![Hello 실행](screenshots/02_hello_execution.png)

---

## 4-3. Git 버전

```bash
git --version
```

![Git 버전](screenshots/03_Git_version.png)

---

## 4-4. Git 설정

Git 사용자 이름, 이메일 및 기본 브랜치 설정을 진행했습니다.

```bash
git config --global user.name
git config --global user.email
git config --global init.defaultBranch main
```

![Git 설정](screenshots/04_Git_settings.png)

---

# 5. Git 저장소 초기화

프로젝트 폴더에서 Git 저장소를 초기화했습니다.

```bash
git init
```

변경사항 추가:

```bash
git add .
```

첫 Commit:

```bash
git commit -m "chore: initialize project"
```

![첫 Git Commit](screenshots/05_Git_first_commit.png)

---

# 6. GitHub Push

GitHub 원격 저장소를 연결했습니다.

```bash
git remote add origin https://github.com/ll-0l/python-prompt-manager.git
```

Push:

```bash
git push -u origin main
```

![Git Push](screenshots/06_Git_push.png)

GitHub에 파일이 업로드된 것을 확인했습니다.

![GitHub Repository](screenshots/07_GitHub_repository.png)

---

# 7. 프로그램 메인 메뉴

필수 기능과 보너스 기능을 포함한 최종 메뉴는 다음과 같습니다.

```text
=== 나만의 프롬프트 관리 ===
1. 프롬프트 추가
2. 프롬프트 목록
3. 카테고리별 조회
4. 프롬프트 검색
5. 프롬프트 상세 보기
6. 즐겨찾기 관리
7. 즐겨찾기 목록

--- 보너스 기능 ---
8. 프롬프트 수정
9. 프롬프트 삭제
10. 조회수 TOP 목록
11. Markdown 내보내기

0. 종료
선택:
```

기존 필수 메뉴 실행 증빙:

![메인 메뉴](screenshots/09_main_menu.png)

보너스가 포함된 최종 메뉴:

![보너스 메뉴](screenshots/23_bonus_menu.png)

---

# 8. 잘못된 입력 처리

사용자가 존재하지 않는 메뉴 번호를 입력하더라도 프로그램이 중단되지 않고 다시 메뉴를 표시하도록 구현했습니다.

![잘못된 입력](screenshots/10_invalid_menu_input.png)

다음과 같은 입력을 검증합니다.

- 메인 메뉴의 잘못된 번호
- 빈 제목
- 빈 내용
- 빈 카테고리
- 잘못된 카테고리 번호
- 빈 검색어
- 상세 보기에서 문자 입력
- 존재하지 않는 프롬프트 번호
- 수정 기능의 번호 오류
- 삭제 기능의 번호 오류

---

# 9. 기본 프롬프트 데이터

프로그램 최초 실행 시 3개의 기본 프롬프트를 제공합니다.

## 1. MODU 로고 이미지 생성

- 카테고리: 이미지 생성

## 2. MODU 앱 UI 이미지 생성

- 카테고리: 이미지 생성

## 3. 업무용 메일 초안 작성

- 카테고리: 텍스트 생성

---

# 10. 프롬프트 추가

메뉴 `1`에서 새로운 프롬프트를 추가합니다.

입력 정보:

- 제목
- 내용
- 카테고리

데이터 구조:

```python
{
    "title": "프롬프트 제목",
    "content": "프롬프트 내용",
    "category": "텍스트 생성",
    "favorite": False,
    "view_count": 0
}
```

프롬프트 추가 후 리스트에 저장합니다.

```python
prompts.append(new_prompt)
```

보너스 구현 이후에는 추가 즉시 `prompts.json`에도 저장됩니다.

![프롬프트 추가](screenshots/11_add_prompt.png)

---

# 11. 프롬프트 목록

메뉴 `2`에서 모든 프롬프트를 확인합니다.

표시 정보:

- 번호
- 카테고리
- 제목
- 즐겨찾기 상태
- 조회수

![프롬프트 목록](screenshots/13_prompt_list.png)

---

# 12. 카테고리별 조회

메뉴 `3`에서 카테고리를 선택하면 해당 카테고리의 데이터만 출력합니다.

핵심 조건:

```python
prompt["category"] == selected_category
```

![카테고리별 조회](screenshots/15_category_filter.png)

---

# 13. 프롬프트 검색

메뉴 `4`에서 제목과 내용을 검색합니다.

핵심 로직:

```python
keyword.lower() in prompt["title"].lower()
```

```python
keyword.lower() in prompt["content"].lower()
```

부분 문자열 검색을 사용하며 영문의 경우 대소문자의 영향을 줄이기 위해 `lower()`를 사용했습니다.

![프롬프트 검색](screenshots/16_prompt_search.png)

현재 검색 방식은 다음 고급 기능은 지원하지 않습니다.

- 정규표현식
- 검색 관련도 정렬
- AND / OR 복합 검색
- 정확 일치 전용 검색

---

# 14. 프롬프트 상세 보기

메뉴 `5`에서 선택한 프롬프트의 전체 정보를 확인합니다.

출력 정보:

- 제목
- 카테고리
- 즐겨찾기 상태
- 조회수
- 전체 프롬프트 내용

![프롬프트 상세 보기](screenshots/17_prompt_detail.png)

보너스 구현 이후에는 상세 보기를 실행할 때마다 조회수가 증가합니다.

---

# 15. 즐겨찾기

메뉴 `6`에서 즐겨찾기를 추가하거나 해제합니다.

```python
prompt["favorite"] = not prompt["favorite"]
```

즉:

```text
False → True
True → False
```

방식으로 동작합니다.

![즐겨찾기 관리](screenshots/18_favorite_toggle.png)

---

# 16. 즐겨찾기 목록

메뉴 `7`에서 `favorite` 값이 `True`인 데이터만 출력합니다.

![즐겨찾기 목록](screenshots/19_favorite_list.png)

보너스 구현 이후 즐겨찾기 상태도 `prompts.json`에 저장됩니다.

---

# 17. 데이터 구조

전체 데이터는 **리스트 안에 딕셔너리를 저장하는 구조**입니다.

```python
prompts = [
    {
        "title": "MODU 로고 이미지 생성",
        "content": "프롬프트 내용",
        "category": "이미지 생성",
        "favorite": False,
        "view_count": 0
    }
]
```

## 데이터 스키마

| 필드 | 자료형 | 설명 |
|---|---|---|
| `title` | `str` | 프롬프트 제목 |
| `content` | `str` | 프롬프트 전체 내용 |
| `category` | `str` | 프롬프트 카테고리 |
| `favorite` | `bool` | 즐겨찾기 상태 |
| `view_count` | `int` | 상세 조회 횟수 |

---

# 18. 리스트와 딕셔너리를 선택한 이유

## 리스트

여러 프롬프트를 등록된 순서대로 저장하고 반복문으로 조회하기 위해 사용했습니다.

장점:

- 입력 순서를 유지하기 쉬움
- 반복문으로 전체 조회가 쉬움
- `append()`로 추가가 간단함
- 소규모 프로그램에 적합함

한계:

데이터가 매우 많아질 경우 검색과 중복 검사에서 전체 리스트를 순차적으로 확인해야 하므로 성능이 떨어질 수 있습니다.

---

## 딕셔너리

한 프롬프트에는 여러 종류의 속성이 존재하므로 딕셔너리를 사용했습니다.

```python
prompt["title"]
prompt["content"]
prompt["category"]
prompt["favorite"]
prompt["view_count"]
```

장점:

- 각 값의 의미가 명확함
- 코드의 가독성이 좋음
- 새로운 속성을 추가하기 쉬움

대규모 프로그램으로 발전할 경우 고유 ID와 SQLite 데이터베이스 등을 사용할 수 있습니다.

---

# 19. 중복 제목 처리

같은 제목이 존재할 경우 기존 데이터를 덮어쓰지 않고 자동으로 번호를 추가합니다.

```text
MODU 로고 이미지 생성
MODU 로고 이미지 생성 (2)
MODU 로고 이미지 생성 (3)
```

기존 데이터를 유지하면서 중복된 제목의 프롬프트를 별도 관리할 수 있습니다.

---

# 20. 카테고리 충돌 처리

사용자가 직접 입력한 카테고리 이름이 기존 카테고리와 같으면 새로운 중복 카테고리를 만들지 않고 기존 카테고리를 사용합니다.

영문 이름의 경우 `lower()`를 사용하여 대소문자를 무시하고 비교합니다.

---

# 21. 함수 분리

기능별로 함수를 분리했습니다.

| 함수 | 역할 |
|---|---|
| `save_prompts()` | JSON 저장 |
| `load_prompts()` | JSON 불러오기 |
| `get_categories()` | 카테고리 목록 생성 |
| `make_unique_title()` | 중복 제목 처리 |
| `select_category()` | 카테고리 선택 |
| `add_prompt()` | 프롬프트 추가 |
| `show_prompt_list()` | 전체 목록 |
| `show_by_category()` | 카테고리별 조회 |
| `search_prompt()` | 검색 |
| `show_prompt_detail()` | 상세 보기 및 조회수 증가 |
| `toggle_favorite()` | 즐겨찾기 추가·해제 |
| `show_favorites()` | 즐겨찾기 목록 |
| `edit_prompt()` | 프롬프트 수정 |
| `delete_prompt()` | 프롬프트 삭제 |
| `show_top_prompts()` | 조회수 TOP 정렬 |
| `safe_filename()` | 안전한 Markdown 파일명 생성 |
| `export_markdown()` | Markdown 내보내기 |
| `show_menu()` | 메뉴 출력 |
| `main()` | 프로그램 전체 실행 |

---

# 22. 메인 반복 구조

사용자가 직접 종료할 때까지 메뉴가 반복됩니다.

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

를 실행합니다.

---

# 23. 보너스 과제 1 — JSON 영속화

## JSON 저장

프롬프트 데이터를 다음 파일에 저장합니다.

```text
prompts.json
```

Python 기본 라이브러리 `json`을 사용하므로 외부 패키지는 필요하지 않습니다.

저장 대상에는 다음 정보가 포함됩니다.

```json
[
    {
        "title": "MODU 로고 이미지 생성",
        "content": "프롬프트 내용",
        "category": "이미지 생성",
        "favorite": false,
        "view_count": 2
    }
]
```

다음 작업이 발생하면 데이터를 다시 저장합니다.

- 프롬프트 추가
- 프롬프트 수정
- 프롬프트 삭제
- 즐겨찾기 변경
- 상세 조회수 증가

---

## JSON 불러오기

프로그램 시작 시 `load_prompts()`를 실행합니다.

```text
프로그램 시작
↓
prompts.json 존재 확인
↓
파일이 있으면 기존 데이터 불러오기
↓
파일이 없으면 기본 프롬프트 생성
```

프로그램을 종료한 뒤 다시 실행해도 기존 데이터가 유지됩니다.

![JSON 영속화](screenshots/24_json_persistence.png)

이 화면에서는 프로그램을 종료하고 다시 실행한 후:

```text
prompts.json에서 4개의 프롬프트를 불러왔습니다.
```

라는 메시지와 기존에 추가한 테스트 프롬프트가 그대로 남아 있는 것을 확인할 수 있습니다.

---

## JSON 오류 처리

다음 오류에 대한 예외 처리를 적용했습니다.

- 파일 읽기 오류
- JSON 형식 오류
- 잘못된 데이터 구조

JSON을 정상적으로 불러올 수 없는 경우 기본 프롬프트 데이터로 프로그램을 시작하도록 설계했습니다.

---

# 24. 보너스 과제 1 — Markdown 내보내기

메뉴 `11`을 선택하면 전체 프롬프트를 카테고리별 Markdown 파일로 내보냅니다.

예:

```text
exports/
├── 이미지_생성.md
└── 텍스트_생성.md
```

실제 프롬프트가 존재하는 카테고리의 파일만 생성합니다.

Markdown 파일에는 다음 내용이 저장됩니다.

- 제목
- 카테고리
- 즐겨찾기
- 조회수
- 프롬프트 내용

![Markdown 내보내기](screenshots/27_markdown_export.png)

---

# 25. 보너스 과제 2 — 프롬프트 수정

메뉴 `8`을 사용합니다.

수정 가능한 항목:

- 제목
- 내용
- 카테고리

변경하지 않을 항목은 Enter를 입력하여 기존 값을 유지할 수 있습니다.

![프롬프트 수정](screenshots/25_bonus_edit.png)

수정된 데이터는 `prompts.json`에 저장됩니다.

---

# 26. 보너스 과제 2 — 프롬프트 삭제

메뉴 `9`를 사용합니다.

실수로 데이터를 삭제하지 않도록 삭제 전 확인 절차를 사용합니다.

```text
정말 삭제하시겠습니까? (y/n):
```

`y`를 입력한 경우에만 삭제합니다.

![프롬프트 삭제](screenshots/28_bonus_delete.png)

삭제한 결과도 `prompts.json`에 저장됩니다.

---

# 27. 보너스 과제 2 — 조회수 기록

상세 보기 실행 시:

```python
prompt["view_count"] += 1
```

을 실행하여 조회수를 증가시킵니다.

조회수도 JSON에 저장되므로 프로그램을 종료해도 유지됩니다.

---

# 28. 보너스 과제 2 — 조회수 TOP 목록

메뉴 `10`을 사용합니다.

```python
sorted(
    prompts,
    key=lambda prompt: prompt["view_count"],
    reverse=True
)
```

를 사용하여 조회수가 높은 순으로 정렬합니다.

![조회수 TOP 목록](screenshots/26_bonus_view_count.png)

증빙 화면에서는 `MODU 로고 이미지 생성` 프롬프트의 조회수가 2로 증가하고 TOP 목록의 첫 번째에 표시되는 것을 확인할 수 있습니다.

---

# 29. Git Branch — 프롬프트 목록 기능

필수 과제에서 프롬프트 목록 기능을 별도 브랜치에서 구현했습니다.

브랜치:

```text
feature/prompt-list
```

생성:

```bash
git checkout -b feature/prompt-list
```

![브랜치 생성](screenshots/12_Git_branch.png)

기능 구현 후:

```bash
git checkout main
git merge --no-ff feature/prompt-list -m "merge: add prompt list feature"
```

로 `main`에 병합했습니다.

![Git Merge](screenshots/14_Git_merge.png)

---

# 30. Git Branch — 보너스 기능

필수 과제 사전평가 **100% / 21개 항목 PASS** 상태의 `main`을 안전하게 유지하면서 보너스 기능을 개발하기 위해 별도 브랜치를 만들었습니다.

브랜치:

```text
feature/bonus-features
```

생성:

```bash
git checkout -b feature/bonus-features
```

보너스 기능 코드를 구현하고 다음 Commit을 생성했습니다.

```text
feat: add bonus persistence and CRUD features
```

보너스 증빙을 별도 Commit으로 추가했습니다.

```text
docs: add bonus feature screenshots
```

GitHub Branches 화면에서도 다음 브랜치를 확인할 수 있습니다.

- `main`
- `feature/prompt-list`
- `feature/bonus-features`

![보너스 브랜치](screenshots/29_bonus_branch.png)

보너스 기능 전체 검증 및 문서화를 완료한 후 `main` 브랜치에 Merge하여 최종 버전을 구성합니다.

---

# 31. Git Clone 실습

공개 GitHub 저장소를 직접 Clone했습니다.

```bash
git clone https://github.com/octocat/Hello-World.git
```

이후:

```bash
cd Hello-World
dir
git log --oneline --graph --all
```

을 실행하여 폴더와 Commit 구조를 확인했습니다.

![Git Clone](screenshots/20_Git_clone.png)

---

# 32. 사용한 Git 명령어

과제에서 요구한 Git 명령어를 모두 실제로 사용했습니다.

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

## git init

새 Git 저장소를 시작합니다.

## git add

변경사항을 다음 Commit에 포함할 준비를 합니다.

## git commit

변경 내용을 하나의 버전으로 기록합니다.

## git push

로컬 Commit을 GitHub에 업로드합니다.

## git pull

GitHub의 최신 변경사항을 로컬로 가져옵니다.

## git checkout

브랜치를 생성하거나 다른 브랜치로 이동합니다.

## git clone

원격 GitHub 저장소를 로컬 컴퓨터로 복제합니다.

## git merge

별도 브랜치의 변경사항을 현재 브랜치에 병합합니다.

---

# 33. 주요 Commit 기록

기능 단위로 Commit을 생성했습니다.

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
docs: address design feedback in README
docs: address pre-evaluation feedback
feat: add bonus persistence and CRUD features
docs: add bonus feature screenshots
docs: add bonus branch screenshot
docs: update README for bonus features
```

10개 이상의 의미 있는 Commit 요구사항을 충분히 충족했습니다.

기존 필수 버전의 Git 그래프:

![최종 Git 로그](screenshots/22_Final_Git_log.png)

---

# 34. 보너스 증빙 목록

| 파일 | 증빙 내용 |
|---|---|
| `23_bonus_menu.png` | 최종 보너스 메뉴 |
| `24_json_persistence.png` | JSON 저장 및 재실행 후 불러오기 |
| `25_bonus_edit.png` | 프롬프트 수정 |
| `26_bonus_view_count.png` | 조회수 기록 및 TOP 정렬 |
| `27_markdown_export.png` | 카테고리별 Markdown 내보내기 |
| `28_bonus_delete.png` | 프롬프트 삭제 |
| `29_bonus_branch.png` | 보너스 기능 별도 Branch |

---

# 35. 최종 프로젝트 구조

```text
python-prompt-manager/
│
├── exports/
│   ├── 이미지_생성.md
│   └── 텍스트_생성.md
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
│   ├── 22_Final_Git_log.png
│   ├── 23_bonus_menu.png
│   ├── 24_json_persistence.png
│   ├── 25_bonus_edit.png
│   ├── 26_bonus_view_count.png
│   ├── 27_markdown_export.png
│   ├── 28_bonus_delete.png
│   └── 29_bonus_branch.png
│
├── .gitignore
├── README.md
├── SUBMISSION.md
├── hello.py
├── prompt_manager.py
└── prompts.json
```

`exports/`의 파일은 현재 등록된 프롬프트 카테고리에 따라 달라질 수 있습니다.

---

# 36. 데이터 저장 흐름

최종 보너스 버전에서는 다음 흐름으로 데이터를 관리합니다.

```text
프로그램 시작
↓
prompts.json 확인
↓
기존 JSON 데이터 불러오기
↓
프롬프트 관리
↓
추가 / 수정 / 삭제
즐겨찾기 변경
상세 조회
↓
prompts.json 자동 저장
↓
프로그램 종료
↓
다음 실행에서도 데이터 유지
```

초기 필수 버전에서는 실행 중 메모리에서만 데이터를 관리했지만, 보너스 과제를 통해 JSON 영속화 기능을 실제로 구현했습니다.

---

# 37. 필수 과제 체크리스트

## 개발 환경

- [x] Visual Studio Code 사용
- [x] Python 3.10 이상
- [x] Python 버전 확인
- [x] `print("Hello")` 실행
- [x] Git 버전 확인
- [x] Git 사용자 설정
- [x] 기본 브랜치 `main`

## 프로그램

- [x] 콘솔 메뉴
- [x] 번호 입력
- [x] 종료 기능
- [x] 기본 프롬프트 3개 이상
- [x] 리스트 사용
- [x] 딕셔너리 사용
- [x] 제목 필드
- [x] 내용 필드
- [x] 카테고리 필드
- [x] 즐겨찾기 필드
- [x] 프롬프트 추가
- [x] 빈 입력 처리
- [x] 전체 목록
- [x] 카테고리별 조회
- [x] 제목 검색
- [x] 내용 검색
- [x] 상세 보기
- [x] 즐겨찾기 추가·해제
- [x] 즐겨찾기 목록
- [x] 기능별 함수 분리
- [x] 잘못된 입력 처리
- [x] 중복 제목 처리
- [x] 카테고리 충돌 처리

## Git / GitHub

- [x] `git init`
- [x] `git add`
- [x] `git commit`
- [x] `git push`
- [x] `git pull`
- [x] `git checkout`
- [x] `git clone`
- [x] `git merge`
- [x] 10개 이상 의미 있는 Commit
- [x] 추가 Branch 생성
- [x] `feature/prompt-list`
- [x] Branch에서 목록 기능 구현
- [x] `main` Merge
- [x] Public Repository

---

# 38. 보너스 과제 체크리스트

## 보너스 1 — 프롬프트 영속화 및 내보내기

- [x] `prompts.json` 저장
- [x] `prompts.json` 불러오기
- [x] 프로그램 종료 후 데이터 유지
- [x] 재실행 시 기존 데이터 복원
- [x] 카테고리별 Markdown 파일 내보내기
- [x] `exports/` 폴더 자동 생성

## 보너스 2 — CRUD 및 사용 기록

- [x] 프롬프트 수정
- [x] 프롬프트 삭제
- [x] 삭제 확인 절차
- [x] 상세 보기 조회수 기록
- [x] 조회수 JSON 저장
- [x] 조회수 TOP 목록
- [x] 조회수 내림차순 정렬

## 보너스 Git 관리

- [x] `feature/bonus-features` 생성
- [x] 보너스 기능을 별도 Branch에서 개발
- [x] GitHub에 보너스 Branch Push
- [x] 보너스 실행 증빙 추가
- [x] README에 보너스 기능 문서화
- [x] SUBMISSION에 보너스 기능 문서화

---

# 39. AI 사전평가 반영

필수 과제 구현 후 AI 사전평가에서 처음에는 86%를 받았습니다.

보완이 필요했던 주요 항목은 다음과 같았습니다.

- 리스트와 딕셔너리 선택 근거
- 데이터 영속화 설계
- 중복 제목 및 카테고리 충돌 처리

해당 내용을 코드와 문서에 보완한 뒤 다시 평가하여:

```text
100%
21 / 21 항목 PASS
```

결과를 확인했습니다.

이후 선택 과제인 보너스 기능까지 추가하여 JSON 영속화를 설계 수준이 아니라 실제 코드로 구현했습니다.

---

# 40. 향후 개선 방향

현재 프로그램은 JSON 기반 영속화까지 구현했습니다.

더 큰 프로그램으로 확장할 경우 다음 기능을 고려할 수 있습니다.

- SQLite 데이터베이스
- 각 프롬프트 고유 ID
- 생성 날짜
- 수정 날짜
- 태그
- 삭제 복구
- 백업 파일
- 검색 조건 조합
- 정확 검색 / 부분 검색 선택
- 조회수 TOP 개수 선택
- GUI
- 웹 서비스

데이터가 많아질 경우:

```text
JSON
↓
고유 ID 추가
↓
SQLite 테이블 설계
↓
기존 JSON 데이터 이전
↓
DB 기반 CRUD / 검색
```

방식으로 확장할 수 있습니다.

---

# 41. 프로젝트 회고

프로젝트 시작 시에는 Python 파일을 직접 실행하는 과정부터 시작했습니다.

`print("Hello")`를 실행한 후 리스트, 딕셔너리, 조건문, 반복문, 함수와 사용자 입력을 차례대로 적용하여 콘솔 기반 프로그램을 완성했습니다.

Git에서는 기능을 하나씩 완성할 때마다 Commit을 생성했고, 프롬프트 목록 기능은 `feature/prompt-list` 브랜치에서 별도로 개발한 뒤 `main`에 Merge했습니다.

필수 과제를 완성한 후 AI 사전평가 결과를 기반으로 데이터 구조 선택 이유, 영속화 설계, 중복 데이터 처리 등의 설명을 보완하여 21개 평가 항목 전체 PASS를 확인했습니다.

이후 보너스 과제를 수행할 때는 이미 검증된 `main` 브랜치를 바로 수정하지 않고 `feature/bonus-features` 브랜치를 새로 생성했습니다.

보너스 기능으로 JSON 저장·불러오기, Markdown 내보내기, 수정·삭제, 조회수 기록 및 TOP 목록을 실제로 구현했습니다.

이를 통해 단순한 Python 콘솔 프로그램 작성뿐 아니라 Git Branch를 이용해 안정된 버전을 보호하면서 새로운 기능을 개발하는 흐름까지 직접 경험할 수 있었습니다.

---

# 42. 최종 제출 정보

**프로젝트명:** Python Prompt Manager

**GitHub Repository:**  
https://github.com/ll-0l/python-prompt-manager

**최종 제출 파일:**  
`SUBMISSION.md`

**필수 과제:** 완료

**AI 사전평가:** 100% / 21개 항목 PASS

**보너스 과제 1:** 완료

**보너스 과제 2:** 완료