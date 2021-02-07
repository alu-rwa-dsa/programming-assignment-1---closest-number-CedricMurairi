

def closestNumbers(arr):
    arr.sort()
    checked = dict()
    
    for i in range(len(arr) - 1):
        diff = abs(arr[i+1] - arr[i])
        if diff in checked:
            checked[diff].append(arr[i])
            checked[diff].append(arr[i+1])
        else:
            checked[diff] = [arr[i], arr[i+1]]

    return checked[min(checked.keys())]

def main():
    arr = [5, 4, 3, 2]
    # arr = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]

    print(closestNumbers(arr))

if __name__ == "__main__":
    main()
