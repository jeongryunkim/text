import os
from updown_game import UpDown_Game
from lotto_game import Lotto_Game

class Main: 
    def __init__(self):
        self.updown_file = "updown_history.txt"
        self.lotto_file = "lotto_history.txt"

        self.history_updown = self.read_updown_data()
        self.history_lotto = self.read_lotto_data()

        self.updown_game = UpDown_Game(self.history_updown)
        self.lotto_game = Lotto_Game(self.history_lotto)

    def read_updown_data(self): # UP & DOWN 게임 이력 읽기
        history = []
        if os.path.exists(self.updown_file):
            read_updown = open(self.updown_file, "r", encoding="utf-8")
            for line in read_updown:
                line = line.strip()
                if line != "":
                    data = line.split(",")
                    if len(data) == 3:
                        history.append({
                            "name": data[0],
                            "trial": int(data[1]),
                            "range": int(data[2])
                        })
            read_updown.close()
        return history

    def save_updown_data(self): # UP & DOWN 게임 이력 저장
        save_updown = open(self.updown_file, "w", encoding="utf-8")
        for item in self.history_updown:
            save_updown.write(f"{item['name']},{item['trial']},{item['range']}\n")
        save_updown.close()

    def read_lotto_data(self): # 로또 번호 이력 읽기
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

    def save_lotto_data(self): # 로또 번호 이력 저장 (중복 close 제거 수정 반영)
        save_lotto = open(self.lotto_file, "w", encoding="utf-8")
        for lotto in self.history_lotto:
            str_lotto = []
            for num in lotto:
                str_lotto.append(str(num))
            save_lotto.write(",".join(str_lotto) + "\n")
        save_lotto.close()

    def run(self): # 메인 이벤트 루프 실행
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
