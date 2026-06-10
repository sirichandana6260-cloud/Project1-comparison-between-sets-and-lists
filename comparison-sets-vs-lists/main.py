import time

print("=" * 50)
print("STUDENT VERIFICATION SYSTEM")
print("=" * 50)


student_ids = list(map(int, input("Enter Student IDs (space separated): ").split()))


search_id = int(input("Enter Student ID to verify: "))


student_set = set(student_ids)

print("\n----- Student Database -----")
print("Student IDs (List):", student_ids)
print("Unique Student IDs (Set):", student_set)


REPEAT_COUNT = 10000


start = time.perf_counter()

for _ in range(REPEAT_COUNT):
    found_in_list = search_id in student_ids

list_time = time.perf_counter() - start


start = time.perf_counter()

for _ in range(REPEAT_COUNT):
    found_in_set = search_id in student_set

set_time = time.perf_counter() - start


print("\n----- Verification Results -----")

print("\nUsing List")
print("Student Found:", found_in_list)
print("Total Time Taken:", list_time, "seconds")
print("Time Complexity: O(n)")

print("\nUsing Set")
print("Student Found:", found_in_set)
print("Total Time Taken:", set_time, "seconds")
print("Time Complexity: O(1)")


print("\n----- Performance Analysis -----")

if set_time < list_time:
    print("Set is faster than List for student verification.")
    print("Difference:", list_time - set_time, "seconds")
elif list_time < set_time:
    print("List is faster than Set.")
    print("Difference:", set_time - list_time, "seconds")
else:
    print("Both took nearly the same time.")


print("\n----- Conclusion -----")
print("Lists allow duplicate student IDs and perform sequential searching.")
print("Sets remove duplicate student IDs and use hashing for faster searching.")
print("Therefore, Sets are generally preferred for membership checking.")