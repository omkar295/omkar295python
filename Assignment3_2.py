'''2.Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56'''

def Maxi(brr):
    a=max(brr)
    print("Output: ",a)


def main():
        size=int(input("enter number of elements: "))
        arr=[]
        for i in range(size):
            no=input("enter elements: ")
            arr.append(no)
        print("list: ",arr)
        
        Maxi(arr)

        
if __name__=="__main__":
        main()
