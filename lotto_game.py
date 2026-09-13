import random

class Lotto_Game: # 로또 번호 추출기 클래스
    def __init__(self, history):
        self.history = history

    def draw_lotto(self):
        print()
        print("1. 자동 추첨")
        print("2. 수동 추첨")

        choice = input("선택 : ")

        lotto = []

        if choice == "1": # 자동 추첨
            while len(lotto) < 6:
                number = random.randint(1, 45)
                if number in lotto:
                    continue
                lotto.append(number)

        elif choice == "2": # 수동 추첨
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

    def show_history(self): # 로또 번호 추출 이력 보기
        print()
        print("추출된 로또번호 이력")

        if len(self.history) == 0:
            print("로또 번호 추출 이력이 없습니다.")

        else:
            recent = self.history[-5:]
            recent.reverse()

            for i, ranking_lotto in enumerate(recent, start=0):
                print(f"{i+1}회 :", *ranking_lotto)


def read_lotto_data(filename): # 로또 번호 추출 이력 읽기
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


def save_lotto_data(filename, history): # 로또 번호 추출 이력 저장
    with open(filename, "w", encoding="utf-8") as file_save:
        for lotto in history:
            line = ""
            for i in range(len(lotto)):
                line += str(lotto[i])
                if i < len(lotto) - 1:
                    line += ","
            file_save.write(line + "\n")