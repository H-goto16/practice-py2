class person:
    def __init__(self, name, year,country):
        self.name = name 
        self.year = year
        self.country = country
    
    def test(self):
        print(self.name + "は" + str(self.year) + "歳で" + self.country + "出身です")

if __name__ == "__main__":
    GotoHaruki = person("後藤",18,"日本")
    GotoHaruki.test()