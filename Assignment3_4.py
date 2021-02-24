'''4.Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3'''
def Search(num):
    n=input("enter element to be searched")
    print("{} occurred {} times ".format(n,num.count(n)))

            
def main():
    size=int(input("enter size of elements "))
    arr=[]
    for i in range(size):
        no=input("enter elements")
        arr.append(no)
    print("list:",arr)
    Search(arr)
    
if __name__=="__main__":
    main()
    
