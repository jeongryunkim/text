import random

class UpDown_Game: # UP & DOWN 게임 클래스
    def __init__(self, history):
        self.history = history # 랭킹 기록을 담을 리스트

    def input_nickname(self): # 닉네임 입력 받기
        while True:
            nickname = str(input("사용자 닉네임을 입력하세요 (8자 이내): "))
            if not nickname:
                print("닉네임을 입력해 주세요.")
            elif len(nickname) > 8:
                print("닉네임이 너무 길어요. 8자 이내로 입력해주세요.")
            else:
                return nickname

    def updown_normal_play(self, nickname): # 기본 난이도 게임
        count_updown = 0
        target_number = random.randint(1, 100)
        print(target_number)

        while True:
            print("1~100까지 숫자 중 하나를 입력해주세요.")
            user_guess = int(input("정답: "))
            count_updown += 1

            if user_guess == target_number:
                print("정답입니다!")
                print(f"시행 횟수: {count_updown}회 입니다.")

                # 성공시 기록 저장 딕셔너리 생성
                score_record = {
                    "name": nickname,
                    "trial": count_updown,
                    "range": 100
                }
                self.history.append(score_record)
                break

            elif user_guess > target_number:
                print("Down!")

            else:
                print("Up!")

    def updown_customized_play(self, nickname): # 시행횟수, 범위 조절 가능 UP & DOWN 게임
        print("\n--- 난이도 조절하기 ---")
        
        while True: # 범위 설정
            range_input = input("범위를 입력하세요.(2이상, Enter시 기본 100): ")
            if range_input == "":
                range_updown = 100
                print("범위는 1~100입니다.")
                break

            elif int(range_input) >= 2:
                range_updown = int(range_input)
                print(f"범위는 1~{range_updown}입니다.")
                break

            else:
                print("유효한 값을 입력해주세요.")

        while True: # 시행 횟수 설정
            trial_no_input = input("시행 횟수를 입력하세요.(Enter시 기본(1~100)): ")
            if trial_no_input == "":
                print("기본 난이도와 동일하게 시행 횟수 제한 없습니다.")
                trial_no = 0
                break

            elif int(trial_no_input) >= 1:
                trial_no = int(trial_no_input)
                print(f"시행 횟수는 {trial_no}입니다.")
                break

            else:
                print("유효한 값을 넣어주세요.")

        target_user = random.randint(1, range_updown)
        count_updown = 0
        print(target_user)

        while True:
            print(f"1~{range_updown}까지 숫자 중 하나를 입력해주세요.")
            x2 = int(input("정답: "))
            count_updown += 1

            if trial_no != 0 and count_updown >= trial_no and x2 != target_user:
                print("실패하셨습니다.")
                break

            elif x2 > target_user:
                print("Down!")

            elif x2 < target_user:
                print("Up!")

            elif x2 == target_user:
                print("정답입니다!")
                user_score = {}
                user_score["name"] = nickname
                user_score["trial"] = count_updown
                user_score["range"] = range_updown

                if trial_no == 0:
                    print(f"시행 횟수: {count_updown}회")
                else:
                    print(f"{trial_no}회 중 {count_updown}회 만에 성공하였습니다.")

                self.history.append(user_score)
                break

    def start_game(self): # UP & DOWN 게임 시작
        nickname = self.input_nickname()
        while True:
            print()
            print("[ Up & Down 게임 난이도 선택 ]")
            print("1. 기본 난이도 (1~100)")
            print("2. 난이도 조절하기")
            print("3. 뒤로가기")
            choice = str(input("> "))

            if choice == "1":
                self.updown_normal_play(nickname)
                break
            elif choice == "2":
                self.updown_customized_play(nickname)
                break
            elif choice == "3":
                break
            else:
                print("유효한 숫자를 입력해주세요.")

    def show_ranking(self): # UP & DOWN 게임 랭킹 보기
        print()
        print("=== Up & Down 랭킹 ===")
        if not self.history:
            print("게임 이력이 없습니다.")
            return

        sorted_ranking = sorted(self.history, key=lambda x: (x['trial'], -x['range']))
        for i, rank in enumerate(sorted_ranking, start=1):
            print(f"{i}등 \t {rank['name']} \t {rank['trial']}회 \t 1~{rank['range']}")