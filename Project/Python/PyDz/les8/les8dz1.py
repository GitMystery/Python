def output(dataPath):
    with open(dataPath, 'r',encoding="utf-8") as f:
        for line in f:
            print(line)   
def add(dataPath):
    with open(dataPath, 'a',encoding="utf-8") as f:
        a = '\nGenry Ford FTGH +375234545657'
        f.write(a)   
def search(dataPath):
    with open(dataPath, 'r',encoding="utf-8") as f:
        N = input('Введите Имя или Фамилию: ')
        for line in f:
            if N in line:
                print(line)
def change(dataPath:str,message1:str,message2:str)->str:   
    old = message1
    new = message2
    with open(dataPath, 'r',encoding="utf-8") as f:
        data = f.read()
    with open(dataPath, 'w',encoding="utf-8") as f:
        data=data.replace(old,new)
        f.write(data)
        print('Данные заменены')
def remove(dataPath:str,message:str)->str:
    removeData=message
    with open(dataPath, 'r',encoding="utf-8") as f:
        data = f.readlines()
    with open(dataPath, 'w',encoding="utf-8") as f:
        for line in data:
            if removeData not in line.strip('\n'):
                f.write(line)
dataPath = r'C:\Users\Роман\Desktop\GIT education\Project\Python\PyDz\les8\data.txt'
output(dataPath)
# change(dataPath,input(),input())
remove(dataPath,input())