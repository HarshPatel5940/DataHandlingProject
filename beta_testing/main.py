import json


def load_raw_json_data():
    with open("beta_testing/data.json", "r") as file:
        raw_Data = json.load(file)
        return raw_Data

class beta_run:
    def __init__(self):
        self.db = load_raw_json_data()
        self.users = {}
        self.password = {}

    def setup(self):
        for n in self.db["users_db"]:
            print(n,"\t", self.db["users_db"][n])

if __name__ == "__main__":
    beta_run().setup()
