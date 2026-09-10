import random
history_updown = []
history_lotto = []
user_score = {}

while True:
    print()
    print("1. 업앤다운 & Lotto")
    print("2. Up & Down 랭킹")
    print("3. 추출된 로또번호 이력(최근 5회차)")
    print("4. 종료하기")

    menu1 = (input(">"))

    if menu1 == "1":
        while True:
            print()
            print("1. Up & Down")
            print("2. Lotto 번호 추출기")
            print("3. 뒤로가기")
            menu2 = input(">")

            if menu2 == "1":
                while True:
                    nickname = input("사용자 닉네임을 입력하세요 (8자 이내):")

                    if nickname == "":
                        print("다시 입력해 주세요.")
                    elif len(nickname) > 8:
                        print("닉네임이 너무 길어요. 다시 입력해주세요.")
                    else:
                        break
                    
                print()
                print("1. 기본 난이도")
                print("2. 난이도 조절하기")
                print("3. 뒤로가기")
                menu3 = input(">")
                
                while True:
                    if menu3 == "1":
                        count_updown = 0
                        range_set = 0
                        target_normal = random.randint(1, 100)
                        print(target_normal)

                        while True:
                            print("1~100까지 숫자 중 하나를 입력해주세요.")
                            x1 = int(input("정답: "))
                            count_updown += 1
                            if x1 == target_normal:
                                print("정답입니다!")
                                print(f"시행 횟수: {count_updown}회")
                                user_score = {}
                                user_score["name"] = nickname
                                user_score["trial"] = count_updown
                                user_score["range"] = 100
                                history_updown.append(user_score)
                                break
                                    
                            elif x1 > target_normal:
                                print("Down!")
                            else:
                                print("Up!")



                        break

                    elif menu3 == "2":
                        count_updown = 0
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
                                trial_no = 10000
                                break
                            elif int(trial_no_input) >= 1:
                                trial_no = int(trial_no_input)
                                print(f"시행 횟수는 {trial_no}입니다.")
                                break

                            else:
                                print("유효한 값을 넣어주세요.")

                        target_user = random.randint(1, range_updown)
                        print(target_user)
                        
                        while True:
                            print(f"1~{range_updown}까지 숫자 중 하나를 입력해주세요.")
                            x2 = int(input("정답: "))
                            count_updown += 1
                            if count_updown >= trial_no and x2 != target_user:
                                print("실패하셨습니다")
                                break

                            elif x2 > target_user:
                                print("Down!")
                                continue

                            elif x2 < target_user:
                                print("Up!")
                                continue

                            elif x2 == target_user:
                                print("정답입니다!")
                                user_score = {}
                                user_score["name"] = nickname
                                user_score["trial"] = count_updown
                                user_score["range"] = range_updown
                                print(f"{trial_no}회 중 {count_updown}회 만에 성공하였습니다.")
                                history_updown.append(user_score)
                                break
                        break
                    elif menu3 == "3":
                        break

                    else:
                        print("유효한 숫자를 입력해주세요.")
                        break

            elif menu2 == "2":
                print()
                print("1. 자동 추첨")
                print("2. 수동 추첨")

                choice = input("선택 : ")

                lotto = []

                # -------------------------
                # 자동 추첨
                # -------------------------
                if choice == "1":

                    while len(lotto) < 6:

                        number = random.randint(1, 45)

                        if number in lotto:
                            continue

                        lotto.append(number)

                # -------------------------
                # 수동 추첨
                # -------------------------
                elif choice == "2":

                    count_lotto = int(input("직접 입력할 번호 개수(0~6) : "))

                    # 수동 입력
                    while len(lotto) < count_lotto:

                        number = int(input(f"{len(lotto) + 1}번째 번호 : "))

                        # 범위 검사
                        if number < 1 or number > 45:
                            print("1~45 사이의 번호를 입력하세요.")
                            continue

                        # 중복 검사
                        if number in lotto:
                            print("이미 입력한 번호입니다.")
                            continue

                        lotto.append(number)

                    # 부족한 번호 자동 생성
                    while len(lotto) < 6:

                        number = random.randint(1, 45)

                        if number in lotto:
                            continue

                        lotto.append(number)

                else:
                    print("잘못된 선택입니다.")
                    continue

                # 정렬
                lotto.sort()

                # 결과 출력
                print()
                print("추천 로또 번호 :", *lotto)

                # 이력 저장
                history_lotto.append(lotto)
            elif menu2 == "3":
                break
            else:  
                print("유효한 숫자를 입력해주세요.")

    elif menu1 == "2":
        print()
        print("Up & Down 랭킹")

        if len(history_updown) == 0:
            print("게임 이력이 없습니다.")

        else:
            for i in range(len(history_updown)):
                for j in range(len(history_updown)):
                    if i < j:
                        if int(history_updown[i]['trial']) > int(history_updown[j]['trial']):
                            history_updown[i], history_updown[j] = history_updown[j], history_updown[i]
                        else:          
                            continue
                    else:
                        continue

            for i in range(len(history_updown)):
                for j in range(len(history_updown)):
                    if i < j:
                        if int(history_updown[i]['trial']) == int(history_updown[j]['trial']) and int(history_updown[i]['range']) < int(history_updown[j]['range']):
                                history_updown[i], history_updown[j] = history_updown[j], history_updown[i]
                        else:
                            continue
                    else:
                        continue
        for i in range(len(history_updown)):
            print(f"{i+1}등", history_updown[i]['name'], f"{history_updown[i]['trial']}회", f"1~{history_updown[i]['range']}구간")

    elif menu1 == "3":

        print()
        print("추출된 로또번호 이력")

        if len(history_lotto) == 0:
            print("로또 번호 추출 이력이 없습니다.")

        else:
            recent = history_lotto[-5:]
            recent.reverse()

            for i, ranking_lotto in enumerate(recent, start=0):
                print(f"{i+1}회 :", *ranking_lotto)   

    elif menu1 == "4":
        print()
        print("이용해 주셔서 감사합니다.")
        break

    else:
        print()
        print("다시 입력해주세요.")

