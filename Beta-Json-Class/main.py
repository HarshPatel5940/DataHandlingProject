from dataclasses import dataclass
import json


class Testing:
    def __init__(self):
        self.id = []
        self.names = []
        self.pwd = []

    @property
    def user(self):
        return self.user

    @classmethod
    def load_users_data(cls):
        with open("data.json", "r") as file:
            raw_Data = json.load(file)
            user_data = raw_Data["users_db"]
            for n in user_data:
                Testing.user[n] = user_data[n]
        print("User data loaded")

    def create_user(self):
        id1 = input("Enter user ID: ")
        name = input("Enter user name: ")
        pwd = input("Enter user password: ")

        with open("data.json", "r") as file:  # TODO: FIX THIS
            old_data = json.load(file)
            old_data["users_db"][id1] = {"name": name, "pwd": pwd, "power": "user"}
            with open("data.json", "w") as file1:
                json.dump(old_data, file1, indent=4)

        print("inserting..1")
        self.id.append(id1)
        self.names.append(name)
        self.pwd.append(pwd)
        print("User created")

    def main(self):
        while True:
            opt = input("Do you want to want to do?\n1) Load Data\n2) Create User\n3)show data (user wise)\n4) Exit")
            if opt == "1":
                Testing.load_users_data(self)
            elif opt == "2":
                Testing.create_user(self)
            elif opt == "3":
                opt2 = input("Do you want to see all users?\n1) Yes\n2) No")
                if opt2 == "1":
                    for i in self.user:
                        print(f"{i}\t{self.user[i]}")
                elif opt2 == "2":
                    id1 = input("Enter user ID: ")
                    print(f"{id1}\t{self.user[id1]}")
            elif opt == "4":
                break
            else:
                print("Invalid input")


if __name__ == "__main__":
    Testing().main()
