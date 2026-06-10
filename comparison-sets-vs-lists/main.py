import time

print("=" * 60)
print("STUDENT VERIFICATION SYSTEM")
print("LINEAR SEARCH vs BINARY SEARCH vs SET SEARCH")
print("=" * 60)


student_ids = list(map(int, input("Enter Student IDs (space separated): ").split()))


search_id = int(input("Enter Student ID to verify: "))


student_set = set(student_ids)

sorted_ids = sorted(student_ids)

print("\n----- Student Database -----")
print("Student IDs (List):", student_ids)
print("Unique Student IDs (Set):", student_set)

REPEAT_COUNT = 10000




def linear_search(arr, target):
    for item in arr:
        if item == target:
            return True
    return False


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return False


start = time.perf_counter()

for _ in range(REPEAT_COUNT):
    found_linear = linear_search(student_ids, search_id)

linear_time = time.perf_counter() - start


start = time.perf_counter()

for _ in range(REPEAT_COUNT):
    found_binary = binary_search(sorted_ids, search_id)

binary_time = time.perf_counter() - start


start = time.perf_counter()

for _ in range(REPEAT_COUNT):
    found_set = search_id in student_set

set_time = time.perf_counter() - start


print("\n================ RESULTS ================\n")

print("LINEAR SEARCH")
print("Student Found :", found_linear)
print("Time Taken    :", linear_time, "seconds")
print("Complexity    : O(n)")

print("\nBINARY SEARCH")
print("Student Found :", found_binary)
print("Time Taken    :", binary_time, "seconds")
print("Complexity    : O(log n)")

print("\nSET SEARCH")
print("Student Found :", found_set)
print("Time Taken    :", set_time, "seconds")
print("Complexity    : O(1)")


times = {
    "Linear Search": linear_time,
    "Binary Search": binary_time,
    "Set Search": set_time
}

fastest = min(times, key=times.get)

print("\n=========== PERFORMANCE ANALYSIS ===========")
print("Fastest Method :", fastest)


print("\n=============== CONCLUSION ===============")
print("Linear Search checks elements one by one.")
print("Binary Search works on sorted data and reduces")
print("the search space by half in every step.")
print("Set Search uses hashing and provides the")
print("fastest membership checking.")
print("\nFor student verification systems, Set Search")
print("is generally the most efficient approach.")