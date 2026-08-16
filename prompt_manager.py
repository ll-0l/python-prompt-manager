import json
from copy import deepcopy
from pathlib import Path


# ==========================================
# 파일 경로 설정
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "prompts.json"
EXPORT_DIR = BASE_DIR / "exports"


# ==========================================
# 기본 프롬프트 데이터
# ==========================================

DEFAULT_PROMPTS = [
    {
        "title": "MODU 로고 이미지 생성",
        "content": (
            "clean futuristic wordmark logo for a productivity AI app named MODU, "
            "modern sans-serif typography, sleek and minimal design, premium tech branding, "
            "subtle neon blue and neon pink glow accents, dark navy or deep purple background, "
            "the letter U subtly styled with a check mark or completion motif, "
            "digital and youthful mood, cyberpunk-inspired but clean and readable, "
            "centered composition, high contrast, professional logo presentation, "
            "no mockup hands, no extra objects, no long slogan"
        ),
        "category": "이미지 생성",
        "favorite": False,
        "view_count": 0
    },
    {
        "title": "MODU 앱 UI 이미지 생성",
        "content": (
            "full front view of a complete smartphone displaying a virtual AI productivity "
            "planner app UI named MODU, entire phone visible from top to bottom, "
            "entire app screen visible, not cropped, centered composition, "
            "straight-on view, no hands, no people, no extra objects"
        ),
        "category": "이미지 생성",
        "favorite": False,
        "view_count": 0
    },
    {
        "title": "업무용 메일 초안 작성",
        "content": (
            "교육운영팀 담당자의 입장에서 신청자의 일정 변경 문의에 답변하는 "
            "업무용 메일 초안을 작성한다. 확인되지 않은 담당자 이름이나 정책은 "
            "임의로 생성하지 않는다."
        ),
        "category": "텍스트 생성",
        "favorite": False,
        "view_count": 0
    }
]


# ==========================================
# JSON 저장
# ==========================================

def save_prompts(prompts):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(
                prompts,
                file,
                ensure_ascii=False,
                indent=4
            )

    except OSError as error:
        print(f"데이터 저장 중 오류가 발생했습니다: {error}")


# ==========================================
# JSON 불러오기
# ==========================================

def load_prompts():
    if not DATA_FILE.exists():
        prompts = deepcopy(DEFAULT_PROMPTS)
        save_prompts(prompts)

        print("저장된 데이터가 없어 기본 프롬프트를 생성했습니다.")
        return prompts

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            loaded_prompts = json.load(file)

        if not isinstance(loaded_prompts, list):
            raise ValueError("프롬프트 데이터가 리스트 형식이 아닙니다.")

        # 예전 데이터와의 호환성을 위해 필드 자동 보완
        for prompt in loaded_prompts:
            prompt.setdefault("favorite", False)
            prompt.setdefault("view_count", 0)

        print(
            f"prompts.json에서 "
            f"{len(loaded_prompts)}개의 프롬프트를 불러왔습니다."
        )

        return loaded_prompts

    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"데이터 불러오기 중 오류가 발생했습니다: {error}")
        print("기본 프롬프트 데이터로 프로그램을 시작합니다.")

        return deepcopy(DEFAULT_PROMPTS)


# 프로그램 데이터 불러오기
prompts = load_prompts()


# ==========================================
# 공통 카테고리
# ==========================================

def get_categories():
    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    for prompt in prompts:
        if prompt["category"] not in categories:
            categories.append(prompt["category"])

    return categories


# ==========================================
# 중복 제목 처리
# ==========================================

def make_unique_title(title, ignore_index=None):
    existing_titles = set()

    for index, prompt in enumerate(prompts):
        if ignore_index is not None and index == ignore_index:
            continue

        existing_titles.add(prompt["title"])

    if title not in existing_titles:
        return title

    duplicate_number = 2
    new_title = f"{title} ({duplicate_number})"

    while new_title in existing_titles:
        duplicate_number += 1
        new_title = f"{title} ({duplicate_number})"

    print(
        f"같은 제목이 이미 있어 "
        f"'{new_title}'로 저장합니다."
    )

    return new_title


# ==========================================
# 카테고리 선택
# ==========================================

def select_category():
    categories = get_categories()

    while True:
        print("\n카테고리 선택:")

        for index, category in enumerate(categories, start=1):
            print(f"{index}) {category}")

        direct_number = len(categories) + 1
        print(f"{direct_number}) 직접 입력")

        choice = input("선택: ").strip()

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(categories):
                return categories[number - 1]

            if number == direct_number:
                entered_category = input(
                    "새 카테고리 이름: "
                ).strip()

                if not entered_category:
                    print("카테고리는 비워둘 수 없습니다.")
                    continue

                for existing_category in categories:
                    if (
                        existing_category.lower()
                        == entered_category.lower()
                    ):
                        print(
                            f"기존 카테고리 "
                            f"'{existing_category}'를 사용합니다."
                        )
                        return existing_category

                return entered_category

        print("잘못된 선택입니다. 다시 입력해주세요.")


# ==========================================
# 1. 프롬프트 추가
# ==========================================

def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    while True:
        title = input("제목: ").strip()

        if title:
            break

        print("제목은 비워둘 수 없습니다. 다시 입력해주세요.")

    title = make_unique_title(title)

    while True:
        content = input("내용: ").strip()

        if content:
            break

        print("내용은 비워둘 수 없습니다. 다시 입력해주세요.")

    category = select_category()

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "view_count": 0
    }

    prompts.append(new_prompt)

    # 보너스: JSON 영구 저장
    save_prompts(prompts)

    print(f"\n'{title}' 프롬프트가 추가되었습니다!")
    print("prompts.json에 저장되었습니다.")


# ==========================================
# 2. 프롬프트 목록
# ==========================================

def show_prompt_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']}{favorite_mark} "
            f"(조회수: {prompt['view_count']})"
        )

    print(f"\n총 {len(prompts)}개의 프롬프트")


# ==========================================
# 3. 카테고리별 조회
# ==========================================

def show_by_category():
    print("\n=== 카테고리별 조회 ===")

    categories = get_categories()

    for index, category in enumerate(categories, start=1):
        print(f"{index}) {category}")

    choice = input("선택: ").strip()

    if not choice.isdigit():
        print("잘못된 입력입니다. 번호를 입력해주세요.")
        return

    category_number = int(choice)

    if (
        category_number < 1
        or category_number > len(categories)
    ):
        print("잘못된 번호입니다.")
        return

    selected_category = categories[category_number - 1]

    filtered_prompts = [
        prompt
        for prompt in prompts
        if prompt["category"] == selected_category
    ]

    print(
        f"\n[{selected_category}] "
        "카테고리 프롬프트:"
    )

    if not filtered_prompts:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(
        filtered_prompts,
        start=1
    ):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. {prompt['title']}"
            f"{favorite_mark}"
        )

    print(
        f"\n총 {len(filtered_prompts)}개의 프롬프트"
    )


# ==========================================
# 4. 프롬프트 검색
# ==========================================

def search_prompt():
    print("\n=== 프롬프트 검색 ===")

    keyword = input("검색어: ").strip()

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    results = []

    for prompt in prompts:
        if (
            keyword.lower() in prompt["title"].lower()
            or keyword.lower() in prompt["content"].lower()
        ):
            results.append(prompt)

    if not results:
        print("\n검색 결과가 없습니다.")
        return

    print("\n검색 결과:")

    for index, prompt in enumerate(results, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']}{favorite_mark}"
        )

    print(
        f"\n{len(results)}개의 프롬프트를 찾았습니다."
    )


# ==========================================
# 5. 프롬프트 상세 보기
# 보너스: 조회수 증가
# ==========================================

def show_prompt_detail():
    print("\n=== 프롬프트 상세 보기 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']}"
        )

    number = input("\n프롬프트 번호 입력: ").strip()

    if not number.isdigit():
        print("잘못된 입력입니다. 번호를 입력해주세요.")
        return

    prompt_number = int(number)

    if (
        prompt_number < 1
        or prompt_number > len(prompts)
    ):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    prompt = prompts[prompt_number - 1]

    # 조회수 증가
    prompt["view_count"] += 1

    # 조회수도 JSON에 저장
    save_prompts(prompts)

    favorite_text = "⭐" if prompt["favorite"] else "아니오"

    print("\n────────────────────────────")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {favorite_text}")
    print(f"조회수: {prompt['view_count']}")
    print("────────────────────────────")
    print("내용:")
    print(prompt["content"])
    print("────────────────────────────")


# ==========================================
# 6. 즐겨찾기 관리
# ==========================================

def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_prompt_list()

    number = input("\n프롬프트 번호 입력: ").strip()

    if not number.isdigit():
        print("잘못된 입력입니다. 번호를 입력해주세요.")
        return

    prompt_number = int(number)

    if (
        prompt_number < 1
        or prompt_number > len(prompts)
    ):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    prompt = prompts[prompt_number - 1]

    prompt["favorite"] = not prompt["favorite"]

    save_prompts(prompts)

    if prompt["favorite"]:
        print(
            f"\n'{prompt['title']}' 프롬프트를 "
            "즐겨찾기에 추가했습니다!"
        )
    else:
        print(
            f"\n'{prompt['title']}' 프롬프트의 "
            "즐겨찾기를 해제했습니다!"
        )


# ==========================================
# 7. 즐겨찾기 목록
# ==========================================

def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")

    favorite_prompts = [
        prompt
        for prompt in prompts
        if prompt["favorite"]
    ]

    if not favorite_prompts:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(
        favorite_prompts,
        start=1
    ):
        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']} ⭐ "
            f"(조회수: {prompt['view_count']})"
        )

    print(
        f"\n총 {len(favorite_prompts)}개의 즐겨찾기"
    )


# ==========================================
# 8. 프롬프트 수정
# ==========================================

def edit_prompt():
    print("\n=== 프롬프트 수정 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_prompt_list()

    number = input("\n수정할 프롬프트 번호: ").strip()

    if not number.isdigit():
        print("잘못된 입력입니다.")
        return

    prompt_number = int(number)

    if (
        prompt_number < 1
        or prompt_number > len(prompts)
    ):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    index = prompt_number - 1
    prompt = prompts[index]

    print("\n변경하지 않을 항목은 Enter를 누르세요.")

    new_title = input(
        f"새 제목 [{prompt['title']}]: "
    ).strip()

    if new_title:
        prompt["title"] = make_unique_title(
            new_title,
            ignore_index=index
        )

    new_content = input(
        "새 내용 "
        "[현재 내용을 유지하려면 Enter]: "
    ).strip()

    if new_content:
        prompt["content"] = new_content

    change_category = input(
        "카테고리를 변경하시겠습니까? (y/n): "
    ).strip().lower()

    if change_category == "y":
        prompt["category"] = select_category()

    save_prompts(prompts)

    print(
        f"\n'{prompt['title']}' 프롬프트가 "
        "수정되었습니다!"
    )


# ==========================================
# 9. 프롬프트 삭제
# ==========================================

def delete_prompt():
    print("\n=== 프롬프트 삭제 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_prompt_list()

    number = input("\n삭제할 프롬프트 번호: ").strip()

    if not number.isdigit():
        print("잘못된 입력입니다.")
        return

    prompt_number = int(number)

    if (
        prompt_number < 1
        or prompt_number > len(prompts)
    ):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    prompt = prompts[prompt_number - 1]

    confirm = input(
        f"'{prompt['title']}'을(를) "
        "정말 삭제하시겠습니까? (y/n): "
    ).strip().lower()

    if confirm != "y":
        print("삭제를 취소했습니다.")
        return

    deleted_prompt = prompts.pop(prompt_number - 1)

    save_prompts(prompts)

    print(
        f"\n'{deleted_prompt['title']}' "
        "프롬프트를 삭제했습니다!"
    )


# ==========================================
# 10. 조회수 Top 목록
# ==========================================

def show_top_prompts():
    print("\n=== 조회수 TOP 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    sorted_prompts = sorted(
        prompts,
        key=lambda prompt: prompt["view_count"],
        reverse=True
    )

    for index, prompt in enumerate(
        sorted_prompts,
        start=1
    ):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']}{favorite_mark} "
            f"- 조회수 {prompt['view_count']}"
        )


# ==========================================
# Markdown 파일 이름 안전하게 만들기
# ==========================================

def safe_filename(text):
    invalid_characters = '<>:"/\\|?*'

    result = text

    for character in invalid_characters:
        result = result.replace(character, "_")

    result = result.replace(" ", "_")

    return result


# ==========================================
# 11. 카테고리별 Markdown 내보내기
# ==========================================

def export_markdown():
    print("\n=== Markdown 내보내기 ===")

    if not prompts:
        print("내보낼 프롬프트가 없습니다.")
        return

    EXPORT_DIR.mkdir(exist_ok=True)

    categories = get_categories()

    exported_count = 0

    for category in categories:
        category_prompts = [
            prompt
            for prompt in prompts
            if prompt["category"] == category
        ]

        if not category_prompts:
            continue

        filename = (
            safe_filename(category)
            + ".md"
        )

        file_path = EXPORT_DIR / filename

        with file_path.open(
            "w",
            encoding="utf-8"
        ) as file:
            file.write(f"# {category} 프롬프트\n\n")

            for index, prompt in enumerate(
                category_prompts,
                start=1
            ):
                favorite_text = (
                    "⭐"
                    if prompt["favorite"]
                    else "아니오"
                )

                file.write(
                    f"## {index}. {prompt['title']}\n\n"
                )
                file.write(
                    f"- 카테고리: {prompt['category']}\n"
                )
                file.write(
                    f"- 즐겨찾기: {favorite_text}\n"
                )
                file.write(
                    f"- 조회수: {prompt['view_count']}\n\n"
                )
                file.write("### 내용\n\n")
                file.write(prompt["content"])
                file.write("\n\n---\n\n")

        print(f"생성: exports/{filename}")
        exported_count += 1

    print(
        f"\n총 {exported_count}개의 "
        "Markdown 파일을 생성했습니다."
    )


# ==========================================
# 메인 메뉴
# ==========================================

def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")

    print("\n--- 보너스 기능 ---")
    print("8. 프롬프트 수정")
    print("9. 프롬프트 삭제")
    print("10. 조회수 TOP 목록")
    print("11. Markdown 내보내기")

    print("\n0. 종료")


# ==========================================
# 프로그램 실행
# ==========================================

def main():
    print(
        f"총 {len(prompts)}개의 "
        "프롬프트를 불러왔습니다."
    )

    while True:
        show_menu()

        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break

        elif choice == "1":
            add_prompt()

        elif choice == "2":
            show_prompt_list()

        elif choice == "3":
            show_by_category()

        elif choice == "4":
            search_prompt()

        elif choice == "5":
            show_prompt_detail()

        elif choice == "6":
            toggle_favorite()

        elif choice == "7":
            show_favorites()

        elif choice == "8":
            edit_prompt()

        elif choice == "9":
            delete_prompt()

        elif choice == "10":
            show_top_prompts()

        elif choice == "11":
            export_markdown()

        else:
            print(
                "잘못된 번호입니다. "
                "0부터 11 사이의 번호를 입력해주세요."
            )


if __name__ == "__main__":
    main()