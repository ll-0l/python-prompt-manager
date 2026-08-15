prompts = [
    {
        "title": "MODU 로고 이미지 생성",
        "content": "clean futuristic wordmark logo for a productivity AI app named MODU, modern sans-serif typography, sleek and minimal design, premium tech branding, subtle neon blue and neon pink glow accents, dark navy or deep purple background, the letter U subtly styled with a check mark or completion motif, digital and youthful mood, cyberpunk-inspired but clean and readable, centered composition, high contrast, professional logo presentation, no mockup hands, no extra objects, no long slogan",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "MODU 앱 UI 이미지 생성",
        "content": "full front view of a complete smartphone displaying a virtual AI productivity planner app UI named MODU, entire phone visible from top to bottom, entire app screen visible, not cropped, centered composition, straight-on view, no hands, no people, no extra objects",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "업무용 메일 초안 작성",
        "content": "교육운영팀 담당자의 입장에서 신청자의 일정 변경 문의에 답변하는 업무용 메일 초안을 작성한다. 확인되지 않은 담당자 이름이나 정책은 임의로 생성하지 않는다.",
        "category": "텍스트 생성",
        "favorite": False
    }
]


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


def main():
    print(f"기본 프롬프트 {len(prompts)}개를 불러왔습니다.")

    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
            print("아직 준비 중인 기능입니다.")
        else:
            print("잘못된 번호입니다. 0부터 7 사이의 번호를 입력해주세요.")


if __name__ == "__main__":
    main()