def calculate_sums(n, heights):
    stack = [(0, float('inf'))]  # Initialize stack with a sentinel value
    total_sum = 0
    results = []

    for height in heights:
        reduce_sum = 0
        width = 1

        while stack[-1][1] <= height:
            prev_width, prev_height = stack.pop()
            reduce_sum += prev_width * prev_height
            width += prev_width

        total_sum += width * height - reduce_sum
        stack.append((width, height))
        results.append(total_sum + 1)

    return results

def main():
    n = int(input())
    heights = list(map(int, input().split()))
    results = calculate_sums(n, heights)
    print(" ".join(map(str, results)))

if __name__ == "__main__":
    main()