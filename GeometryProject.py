import math
import matplotlib.pyplot as plt
import time
def closest_pair(points):
    # Step 1
    p1 = min(points, key=lambda p: p[0])
    p2 = max(points, key=lambda p: p[0])
    p3 = min(points, key=lambda p: p[1])
    p4 = max(points, key=lambda p: p[1])

    # Step 2
    d1 = [(p[0] - p1[0])**2 + (p[1] - p1[1])**2 for p in points]
    d2 = [(p[0] - p2[0])**2 + (p[1] - p2[1])**2 for p in points]
    d3 = [(p[0] - p3[0])**2 + (p[1] - p3[1])**2 for p in points]
    d4 = [(p[0] - p4[0])**2 + (p[1] - p4[1])**2 for p in points]

    # Step 3
    sum_array = [11 * d1[i] + 101 * d2[i] + 1009 * d3[i] + 10007 * d4[i] for i in range(len(points))]

    # Step 4
    index = list(range(1, len(points) + 1))

    # Step 5
    merge_sort(sum_array, index)

    # Step 6
    closest_pair = find_closest_pair(points, index)

    # Step 7
    return closest_pair

def merge_sort(arr, indices):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        left_indices = indices[:mid]
        right_half = arr[mid:]
        right_indices = indices[mid:]

        merge_sort(left_half, left_indices)
        merge_sort(right_half, right_indices)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                indices[k] = left_indices[i]
                i += 1
            else:
                arr[k] = right_half[j]
                indices[k] = right_indices[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            indices[k] = left_indices[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            indices[k] = right_indices[j]
            j += 1
            k += 1

def find_closest_pair(points, index):
    closest_pair = None
    min_distance = math.inf

    for i in range(len(points) - 1):
        for j in range(i + 1, min(i + 11, len(points))):
            distance = math.sqrt((points[index[i] - 1][0] - points[index[j] - 1][0])**2 +
                                 (points[index[i] - 1][1] - points[index[j] - 1][1])**2)
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[index[i] - 1], points[index[j] - 1])

    return closest_pair

def plot_points_and_lines(points, closest_pair):
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords, label='Points', color='blue')

    if closest_pair:
        x_closest, y_closest = zip(*closest_pair)
        plt.plot(x_closest, y_closest, label='Closest Pair', color='red')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Closest Pair of Points')
    plt.legend()
    plt.show()

# Timer function
def run_with_timer(points):
    start_time = time.time()
    result = closest_pair(points)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print("The closest pair is:", result)
    print(f"Elapsed Time: {elapsed_time:.6f} seconds")

    plot_points_and_lines(points, result)


# Generating random points
import random

points_10000 = [(random.uniform(0, 1000000), random.uniform(0, 1000000)) for _ in range(50)]

run_with_timer(points_10000)