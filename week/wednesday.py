def max_crossing_sum(arr, left, mid, right):
    # Maximum suffix sum on left side
    total = 0
    left_max = float('-inf')
    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_max = max(left_max, total)

    # Maximum prefix sum on right side
    total = 0
    right_max = float('-inf')
    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_max = max(right_max, total)

    return left_max + right_max


def max_subarray_sum(arr, left, right):
    # Base case: only one element
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    left_sum = max_subarray_sum(arr, left, mid)
    right_sum = max_subarray_sum(arr, mid + 1, right)
    cross_sum = max_crossing_sum(arr, left, mid, right)

    return max(left_sum, right_sum, cross_sum)


# Driver code
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(max_subarray_sum(arr, 0, N - 1))

# 1
# 5
# 2 100
# 1 19
# 2 27
# 1 25
# 3 15
# output 3 142

def job_sequencing(jobs, n):
    # Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[1], reverse=True)

    # Find maximum deadline
    max_deadline = max(job[0] for job in jobs)

    # Time slots (False = free, True = occupied)
    slots = [False] * (max_deadline + 1)

    jobs_done = 0
    total_profit = 0

    for deadline, profit in jobs:
        # Try to schedule job at latest available slot
        for t in range(deadline, 0, -1):
            if not slots[t]:
                slots[t] = True
                jobs_done += 1
                total_profit += profit
                break

    return jobs_done, total_profit


# Driver code
T = int(input())
for _ in range(T):
    N = int(input())
    jobs = []

    for _ in range(N):
        D, P = map(int, input().split())
        jobs.append((D, P))

    count, profit = job_sequencing(jobs, N)
    print(count, profit)
