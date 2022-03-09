# You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalised correctly as Alison Heck.
import os

def solve(s):
    res=""
    for str in s.split(" "):
        str = str.replace(str, str.capitalize())
        print(str)
        res+=str+" "
    print(res)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()

    result = solve(s)

    #fptr.write(result + '\n')

    #fptr.close()

