# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# res = []
# for n in range(len(l1)):
#     res.append(l1[n])
#     res.append(l2[n])

# # print(res)

# def fun(*marks):
#     total=0
#     for item in marks:
#         total = total+item
#     return total

# # print(fun())

# def x (a,b):
#     x = a+b
#     y = a*b
#     return x,y

# # print(x(10,20)[0])

# ls = [[3,4],[1,2]]
# # print(ls[1][1])


# def count_letters(string):
#     # Initialize an empty dictionary to store the counts
#     counts = {}

#     # Loop over each character in the string
#     for char in string:
#         # If the character is not already in the dictionary, add it with a count of 1
#         if char not in counts:
#             counts[char] = 1
#         # If the character is already in the dictionary, increment its count by 1
#         else:
#             counts[char] += 1

#     # Print the counts for each letter
#     # print(counts.items())
#     for char, count in counts.items():
#         print(f"{char}: {count}")

#     for x in counts.items():
#         # print(x)

# # Example usage
# my_string = "hello world"
# count_letters(my_string)


# lst1=[1,2,3,4,5,6,7,8,9]

# for i in range(0,len(lst1),2):
#     print(lst1[i])

# tup1=('jantar','mantajgfdggfghjra','sand','water','pjhfghgfjhgfjhgjhgjhgjhjgjhlace')
# temp=''
# for x in tup1:
#     if len(x)>len(temp):
#         temp=x
#     else:
#         pass
# print(temp) 
# print(len(temp))

# ls = [['sdasd','asdasd','uijhg'],['hfcghjghfg','ghcvh']]
# ls.sort()
# print(ls)

# str, flag = 'nayan',0
# for i in range(len(str)):
#     if str[i] == str[len(str)-1-i]:
#         flag=1
#     else:
#         break
# if flag==1:
#     print('palindrome')
# else:
#     print("Not palindrome")


# st = 'surajgowdaisamadman'
# count = {}
# for ind in range(len(st)):
#     if st[ind] not in count:
#         count[st[ind]]=1
#     else:
#         count[st[ind]] = count[st[ind]] +1

# for key,value in count.items():
#     print(key,'-',value)


# st = str(input("Enter a string:"))

# if st[-1]=='y':
#     new = st[0:-1]
#     new = new + 'ies'
#     print(new)
# elif st[-1]=='o' or 'ch' or 's' or 'sh' or 'x' or 'z':
#     new = st + 's'
#     print(new)  
# else:
#     new = st + 's'
#     print(new)


# def sum(n):
#     if n>1:
#         return n*sum(n-1)
#     else:
#         return n

# print(sum(3))

# ls = 'hello'

# print(ls[::-1])

# import random
# print(random.randrange(3,10))

# str1 = 'hello'
# print(str1[-1:])

# a, b, c = True, False, False
# if a or b and c:
#     print ("MSRIT")
# else:
#     print ("RNSIT")


# def print_pattern(n):
#     for i in range(1, n+1):
#         print("+ " * i)
# print_pattern(4)


# def h(m,n):
#  ans = 1
#  while (n > 0):
#     (ans,n) = (ans*m,n-2)
#  return(ans)

# print(h(6,8))


a=7
def fun(b):
    c=17
    def morefun(d):
        e=12
        print(a+b+c+d+e)
    morefun(3)
fun(5)
