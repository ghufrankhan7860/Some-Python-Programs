# To Find Duplicate Values in a Given List
def duplicate_item_list(lst):
        """A function to count duplicate items in a list
                and returns no. of duplicate items in a dictionary"""
        dict_duplicate = {}   # In this Dictionary - key is duplicate item and value is it's count of duplicates
        count = 0   
        list_1 = []
        for item in lst:
                if item not in list_1:
                        list_1.append(item)
        print("Original List", lst)
        print("Filtered List", list_1)
        for item in list_1:
                for a in range(len(lst)):
                        if lst[a] == item:
                                count = count + 1
                                dict_duplicate["Element is "+str(item)] = "Dup. Count " + str(count - 1)       
                count = 0
        print(dict_duplicate)

if __name__ == "__main__":
        lst = eval(input("Enter a list of duplicate items "))
        print("\n Dictionary of duplicate items will be printed...")
        duplicate_item_list(lst)
