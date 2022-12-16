class Name:
    def __init__(self, name):
        self.name = name

class Age:
    def __init__(self, age):
        self.age = age

class Beer(Name):
    def beer(self):
        print(f'{self.name} is drinking beer')

class Born(Age):
    def year(self):
        print(f'He was born in {2022 - self.age}')

class Both(Beer, Born):
    def __init__(self, name, age):
        Beer.__init__(self, name)
        Born.__init__(self, age)

test = Both('Loic', 20)
test.beer()
test.year()

with open('git_codes.txt', 'w', encoding='utf-8') as file:
    file.write('git init \n'
               'git remote remove origin\n'
               'git remote add origin\n'
               'git add .\n'
               'git commit -m "commentary"\n'
               'git push origin master\n'
               'git branch\n'
               'git checkout -b master1\n'
               'git branch -d master1\n'
               'git branch master2\n'
               'git chechout master 2\n'
               'git clone')