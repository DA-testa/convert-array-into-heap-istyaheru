# 221RDB041 Ēriks Lijurovs 16. grupa
# python3
import os

def heapsort(data, n, i):
    root = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[i] <= data[left]:
        root = left

    if right < n and data[root] <= data[right]:
        root = right

    if root != i:
        (data[i], data[root]) = (data[root], data[i])
        heapsort(data, n, root)
  
def build_heap(data):
    n = len(data)
    swaps = []
    # TODO: Create heap and heap sort
  
    for i in range(n//2-1, -1, -1):
        heapsort(data, n, i)

    for i in range(n-1, 0, -1):
        (data[i], data[0]) = (data[0], data[i])
        swaps.append((data[i], data[0]))
        heapsort(data, i, 0)

    return swaps
    

    # try to achieve  O(n) and not O(n2)




def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    choice = input()

    if choice.__contains__('F'):
        test = input()
        
        if test.__contains__('a'):
            return
        else:
            gh_bypass = os.path.join(os.getcwd(), 'tests', test)
            with open(gh_bypass) as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split(" ")))
            file.close()
    elif choice.__contains__('I'):
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    else:
        print("Please enter I or F!")
        return

    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:  #jābūt for i,j in data
        print(i, j)    #jābūt print(i,j)


if __name__ == "__main__":
    main()
