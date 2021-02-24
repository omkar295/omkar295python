'''1.Write a program which accept N numbers from user and store it into List. Return addition of all
elements from that List.
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130'''

def  Add(brr):
       sum=0
       for i in range(len(brr)):
            sum=sum+brr[i]
       print("output: ",sum)
       
       
    
def main():
       size=int(input("enter number of elements"))
       arr=[]
       for i in range(size):
            n=int(input("enter elements"))
            arr.append(n)
       print("list :",arr)
       
       Add(arr)
    
if __name__=="__main__":
    main()
