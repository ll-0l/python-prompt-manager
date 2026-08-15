# ==============================
# Python Prompt Manager
# ==============================


# 기본 프롬프트 데이터
prompts = [
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
        "favorite": False
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
        "favorite": False
    },
    {
        "title": "업무용 메일 초안 작성",
        "content": (
            "교육운영팀 담당자의 입장에서 신청자의 일정 변경 문의에 답변하는 "
            "업무용 메일 초안을 작성한다. 확인되지 않은 담당자 이름이나 정책은 "
            "임의로 생성하지 않는다."
        ),
        "category": "텍스트 생성",
        "favorite": False
    }
]


# ==============================
# 1. 프롬프트 추가
# ==============================

def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    # 제목 입력
    while True:
        original_title = input("제목: ").strip()

        if not original_title:
            print("제목은 비워둘 수 없습니다. 다시 입력해주세요.")
            continue

        # 이미 존재하는 제목 확인
        existing_titles = {prompt["title"] for prompt in prompts}

        title = original_title
        duplicate_number = 2

        # 같은 제목이 있으면 (2), (3)... 자동 추가
        while title in existing_titles:
            title = f"{original_title} ({duplicate_number})"
            duplicate_number += 1

        if title != original_title:
            print(f"같은 제목이 이미 있어 '{title}'로 저장합니다.")

        break

    # 내용 입력
    while True:
        content = input("내용: ").strip()

        if content:
            break

        print("내용은 비워둘 수 없습니다. 다시 입력해주세요.")

    # 기본 카테고리
    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    # 카테고리 선택
    while True:
        print("\n카테고리 선택:")

        for index, category_name in enumerate(categories, start=1):
            print(f"{index}) {category_name}")

        print("7) 직접 입력")

        category_choice = input("선택: ").strip()

        # 기본 카테고리 선택
        if category_choice in ["1", "2", "3", "4", "5", "6"]:
            category = categories[int(category_choice) - 1]
            break

        # 직접 입력
        elif category_choice == "7":
            entered_category = input("새 카테고리 이름: ").strip()

            if not entered_category:
                print("카테고리는 비워둘 수 없습니다.")
                continue

            # 현재 존재하는 카테고리를 모두 확인
            existing_categories = categories.copy()

            for prompt in prompts:
                if prompt["category"] not in existing_categories:
                    existing_categories.append(prompt["category"])

            # 대소문자를 무시하여 같은 카테고리가 있는지 검사
            matched_category = None

            for existing_category in existing_categories:
                if existing_category.lower() == entered_category.lower():
                    matched_category = existing_category
                    break

            if matched_category:
                category = matched_category
                print(f"기존 카테고리 '{category}'를 사용합니다.")
            else:
                category = entered_category

            break

        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

    # 새 프롬프트 생성
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    # 리스트에 추가
    prompts.append(new_prompt)

    print(f"\n'{title}' 프롬프트가 추가되었습니다!")


# ==============================
# 2. 프롬프트 목록
# ==============================

def show_prompt_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']}{favorite_mark}"
        )

    print(f"\n총 {len(prompts)}개의 프롬프트")


# ==============================
# 3. 카테고리별 조회
# ==============================

def show_by_category():
    print("\n=== 카테고리별 조회 ===")

    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    # 사용자가 직접 추가한 카테고리도 목록에 포함
    for prompt in prompts:
        if prompt["category"] not in categories:
            categories.append(prompt["category"])

    for index, category in enumerate(categories, start=1):
        print(f"{index}) {category}")

    choice = input("선택: ").strip()

    # 숫자가 아닌 값 처리
    if not choice.isdigit():
        print("잘못된 입력입니다. 번호를 입력해주세요.")
        return

    category_number = int(choice)

    # 범위를 벗어난 번호 처리
    if category_number < 1 or category_number > len(categories):
        print("잘못된 번호입니다.")
        return

    selected_category = categories[category_number - 1]

    # 선택한 카테고리만 필터링
    filtered_prompts = [
        prompt
        for prompt in prompts
        if prompt["category"] == selected_category
    ]

    print(f"\n[{selected_category}] 카테고리 프롬프트:")

    if not filtered_prompts:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(filtered_prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. {prompt['title']}{favorite_mark}"
        )

    print(f"\n총 {len(filtered_prompts)}개의 프롬프트")


# ==============================
# 4. 프롬프트 검색
# ==============================

def search_prompt():
    print("\n=== 프롬프트 검색 ===")

    keyword = input("검색어: ").strip()

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    results = []

    # 제목 또는 내용에 검색어가 들어있는지 확인
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

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")


# ==============================
# 5. 프롬프트 상세 보기
# ==============================

def show_prompt_detail():
    print("\n=== 프롬프트 상세 보기 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']}{favorite_mark}"
        )

    number = input("\n프롬프트 번호 입력: ").strip()

    if not number.isdigit():
        print("잘못된 입력입니다. 번호를 입력해주세요.")
        return

    prompt_number = int(number)

    if prompt_number < 1 or prompt_number > len(prompts):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    prompt = prompts[prompt_number - 1]

    favorite_text = "⭐" if prompt["favorite"] else "아니오"

    print("\n────────────────────────────")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {favorite_text}")
    print("────────────────────────────")
    print("내용:")
    print(prompt["content"])
    print("────────────────────────────")


# ==============================
# 6. 즐겨찾기 관리
# ==============================

def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']}{favorite_mark}"
        )

    number = input("\n프롬프트 번호 입력: ").strip()

    if not number.isdigit():
        print("잘못된 입력입니다. 번호를 입력해주세요.")
        return

    prompt_number = int(number)

    if prompt_number < 1 or prompt_number > len(prompts):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    prompt = prompts[prompt_number - 1]

    # True이면 False, False이면 True로 변경
    prompt["favorite"] = not prompt["favorite"]

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


# ==============================
# 7. 즐겨찾기 목록
# ==============================

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

    for index, prompt in enumerate(favorite_prompts, start=1):
        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']} ⭐"
        )

    print(f"\n총 {len(favorite_prompts)}개의 즐겨찾기")


# ==============================
# 메인 메뉴
# ==============================

def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


# ==============================
# 프로그램 실행
# ==============================

def main():
    print(f"기본 프롬프트 {len(prompts)}개를 불러왔습니다.")

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

        else:
            print(
                "잘못된 번호입니다. "
                "0부터 7 사이의 번호를 입력해주세요."
            )


# 이 파일을 직접 실행했을 때 main() 실행
if __name__ == "__main__":
    main()