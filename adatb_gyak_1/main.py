import random 

def general(name, n):
    with open(name, 'w') as f:
        for i in range(n):
            user_input = f"user_{random.randint(1000, 9999)}"
            salary = random.randint(30000, 100000)
            f.write(f"{i+1}. {user_input}, {salary} Ft\n")

def search(name, f_name):
    with open(f_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if name in line:
                return line.split(",")[1].strip()
    return -1

general("users.txt", 10)