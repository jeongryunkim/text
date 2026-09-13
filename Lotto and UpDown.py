import random
import os

class UpDown_Game:
    def __init__(self, history):
        self.history = history

    def input_nickname(self):
        while True:
            nickname = str(input("사용자 닉네임을 입력하세요 (8자 이내): "))
            if not nickname:
                print("닉네임을 입력해 주세요.")
            elif len(nickname) > 8:
                print("닉네임이 너무 길어요. 8자 이내로 입력해주세요.")
            else:
                return nickname

    def updown_normal_play(self, nickname):
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

    def updown_customized_play(self, nickname):
        print("\n--- 난이도 조절하기 ---")
        
        while True:
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

        while True:
            trial_no_input = input("시행 횟수를 입력하세요.: ")
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

    def start_game(self):
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

    def show_ranking(self):
        print()
        print("=== Up & Down 랭킹 ===")
        if not self.history:
            print("게임 이력이 없습니다.")
            return

        sorted_ranking = sorted(self.history, key=lambda x: (x['trial'], -x['range']))

        for i, rank in enumerate(sorted_ranking, start=1):
            print(f"{i}등 \t {rank['name']} \t {rank['trial']}회 \t 1~{rank['range']}")

class Lotto_Game:
    def __init__(self, history):
        self.history = history

    def draw_lotto(self):
        print()
        print("1. 자동 추첨")
        print("2. 수동 추첨")

        choice = input("선택 : ")

        lotto = []

        if choice == "1":
            while len(lotto) < 6:
                number = random.randint(1, 45)
                if number in lotto:
                    continue
                lotto.append(number)

        elif choice == "2":
            count_lotto = int(input("직접 입력할 번호 개수(0~6) : "))

            while len(lotto) < count_lotto:
                number = int(input(f"{len(lotto) + 1}번째 번호 : "))

                if number < 1 or number > 45:
                    print("1~45 사이의 번호를 입력하세요.")
                    continue

                if number in lotto:
                    print("이미 입력한 번호입니다.")
                    continue

                lotto.append(number)

            while len(lotto) < 6:
                number = random.randint(1, 45)
                if number in lotto:
                    continue
                lotto.append(number)

        else:
            print("잘못된 선택입니다.")
            return False

        lotto.sort()

        print()
        print("추천 로또 번호 :", *lotto)

        self.history.append(lotto)
        return True

    def show_history(self):
        print()
        print("추출된 로또번호 이력")

        if len(self.history) == 0:
            print("로또 번호 추출 이력이 없습니다.")

        else:
            recent = self.history[-5:]
            recent.reverse()

            for i, ranking_lotto in enumerate(recent, start=0):
                print(f"{i+1}회 :", *ranking_lotto)


def read_lotto_data(filename):
    history = []
    try:
        with open(filename, "r", encoding="utf-8") as file_read:
            lines = file_read.readlines()

        for line in lines:
            data = line.strip().split(",")
            lotto = []
            for number in data:
                if number != "":
                    lotto.append(int(number))
            if len(lotto) > 0:
                history.append(lotto)
    except FileNotFoundError:
        pass
    return history


def save_lotto_data(filename, history):
    with open(filename, "w", encoding="utf-8") as file_save:
        for lotto in history:
            line = ""
            for i in range(len(lotto)):
                line += str(lotto[i])
                if i < len(lotto) - 1:
                    line += ","
            file_save.write(line + "\n")


class GameManager:
    def __init__(self):
        self.updown_file = "updown_history.txt"
        self.lotto_file = "lotto_history.txt"

        self.history_updown = self.read_updown_data()
        self.history_lotto = self.read_lotto_data()

        self.updown_game = UpDown_Game(self.history_updown)
        self.lotto_game = Lotto_Game(self.history_lotto)

    def read_updown_data(self):
        history = []
        if os.path.exists(self.updown_file):
            f = open(self.updown_file, "r", encoding="utf-8")
            for line in f:
                line = line.strip()
                if line != "":
                    data = line.split(",")
                    if len(data) == 3:
                        history.append({
                            "name": data[0],
                            "trial": int(data[1]),
                            "range": int(data[2])
                        })
            f.close()
        return history

    def save_updown_data(self):
        f = open(self.updown_file, "w", encoding="utf-8")
        for item in self.history_updown:
            f.write(f"{item['name']},{item['trial']},{item['range']}\n")
        f.close()

    def read_lotto_data(self):
        history = []
        if os.path.exists(self.lotto_file):
            read_lotto = open(self.lotto_file, "r", encoding="utf-8")
            for line in read_lotto:
                line = line.strip()
                if line != "":
                    data = line.split(",")
                    numbers = []
                    for val in data:
                        numbers.append(int(val))
                    history.append(numbers)
            read_lotto.close()
        return history

    def save_lotto_data(self):
        save_lotto = open(self.lotto_file, "w", encoding="utf-8")
        for lotto in self.history_lotto:
            str_lotto = []
            for num in lotto:
                str_lotto.append(str(num))
            save_lotto.write(",".join(str_lotto) + "\n")
        save_lotto.close()
        save_lotto.close()

    def run(self):
        while True:
            print("\n==============================")
            print(" 1. 업앤다운 & Lotto 시작")
            print(" 2. Up & Down 랭킹 보기")
            print(" 3. 추출된 로또번호 이력 보기")
            print(" 4. 종료하기")
            print("==============================")

            menu1 = input("> ").strip()

            if menu1 == "1":
                while True:
                    print("\n[ Game Menu ]")
                    print("1. Up & Down 게임")
                    print("2. Lotto 번호 추출기")
                    print("3. 메인으로 돌아가기")
                    menu2 = input("> ").strip()

                    if menu2 == "1":
                        self.updown_game.start_game()
                        self.save_updown_data()
                    elif menu2 == "2":
                        if self.lotto_game.draw_lotto():
                            self.save_lotto_data()
                    elif menu2 == "3":
                        break
                    else:
                        print("유효한 숫자를 입력해주세요.")

            elif menu1 == "2":
                self.updown_game.show_ranking()

            elif menu1 == "3":
                self.lotto_game.show_history()

            elif menu1 == "4":
                print("\n이용해 주셔서 감사합니다.")
                break

            else:
                print("\n올바른 메뉴 번호를 입력해주세요.")


if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.run()