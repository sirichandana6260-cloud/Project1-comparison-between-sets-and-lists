import time

print("=" * 50)
print("LIST VS SET SEARCH PERFORMANCE COMPARISON")
print("=" * 50)


numbers = list(map(int, input("Enter numbers (space separated): ").split()))
search_element = int(input("Enter element to search: "))


numbers_set = set(numbers)

print("\nData Structure Information")
print("--------------------------")
print("List:", numbers)
print("Set :", numbers_set)

print("\nNumber of elements in List:", len(numbers))
print("Number of elements in Set :", len(numbers_set))


start_time = time.time()

if search_element in numbers:
    found_in_list = True
else:
    found_in_list = False

list_time = time.time() - start_time


start_time = time.time()

if search_element in numbers_set:
    found_in_set = True
else:
    found_in_set = False

set_time = time.time() - start_time


print("\nSearch Results")
print("-" * 20)

print("Element Found in List :", found_in_list)
print("Time Taken by List    :", list_time, "seconds")

print("\nElement Found in Set  :", found_in_set)
print("Time Taken by Set     :", set_time, "seconds")


print("\nPerformance Analysis")
print("-" * 20)

if set_time < list_time:
    print("Set is Faster than List for searching.")
elif list_time < set_time:
    print("List is Faster than Set for searching.")
else:
    print("Both took nearly the same time.")


print("\nConclusion")
print("-" * 20)
print("List allows duplicates and maintains order.")
print("Set removes duplicates and provides faster searching using hashing.")
print("Therefore, Set is generally preferred when frequent searching is required.")