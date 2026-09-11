

class user_name():
    def __init__(self):
        self.users = []
        
    def user_name_input(self, number):
        for i in range(int(number)):
            user = input(f"{i+1}번째 참가자: ")
            self.users.append(user)

abc = user_name()
abc.user_name_input(3)
print(abc.users)


