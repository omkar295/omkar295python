'''3.Write a program which accept N numbers from user and store it into List. Return Minimum
number from that List.
Input : Number of elements : 4
Input Elements : 13 5 45 7
Output : 5'''

def Mini(brr):
        print("Output: ",min(brr))


def main():
        size=int(input("enter number of elements: "))
        arr=[]
        for i in range(size):
            no=input("enter elements: ")
            arr.append(no)
        print("list: ",arr)
        
        Mini(arr)

        
if __name__=="__main__":
        main()
