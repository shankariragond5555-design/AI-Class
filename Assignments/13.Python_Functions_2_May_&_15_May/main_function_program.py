
# Basic function
def greet():
    print("Hello")
greet()

# with parameter and return with positional argument
print("start")
def add_sub(a,b):
    sum=a+b
    sub=b-a
    return sum,sub

result1,result2=add_sub(10,20)
print(result1)
print(result2)
print("end")


# keyword argument

print("start")
def get_info(name,age):
    print("my name is ",name)
    print("my age is ",age)

get_info(age=25,name="Shankar")
print("end")

# default argument

print("start")
def get_info(name,age,roll_no=100):
    print("my name is ",name)
    print("my age is ",age)
    print("my roll no is ",roll_no)

get_info(age=25,name="Shankar",roll_no=40)
print("end")

# variable length positional argument

print("start")
def get_total(*args):
    result=sum(args)
    return result

result1=get_total(10,20,30,40,50)
print(result1)
print("end")

# variable length keyword argument

print("start")
def student_details(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

student_details(name="Shankar",age=25,roll_no=40)
print("end")