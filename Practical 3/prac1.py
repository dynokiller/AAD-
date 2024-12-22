import random
import time
import matplotlib.pyplot as plt
from flask import Flask, render_template, Response
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)

def bubble_sort_algorithm(array):
    length = len(array)
    for i in range(length):
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def insertion_sort_algorithm(array):
    length = len(array)
    for i in range(1, length):
        value = array[i]
        position = i - 1
        while position >= 0 and value < array[position]:
            array[position + 1] = array[position]
            position -= 1
        array[position + 1] = value

def merge_sort_algorithm(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort_algorithm(left)
        merge_sort_algorithm(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

def time_sort_function(sort_func, array):
    start = time.time()
    sort_func(array)
    end = time.time()
    return end - start

def create_random_data(size):
    return [random.randint(1, 1000) for _ in range(size)]

@app.route('/')
def home():
    sizes = [10, 20, 100, 200, 500, 1000]
    bubble_times = []
    insertion_times = []
    merge_times = []

    for size in sizes:
        data = create_random_data(size)
        bubble_times.append(time_sort_function(bubble_sort_algorithm, data.copy()))
        insertion_times.append(time_sort_function(insertion_sort_algorithm, data.copy()))
        merge_times.append(time_sort_function(merge_sort_algorithm, data.copy()))

    plt.figure()
    plt.plot(sizes, bubble_times, label='Bubble Sort')
    plt.plot(sizes, insertion_times, label='Insertion Sort')
    plt.plot(sizes, merge_times, label='Merge Sort')
    plt.xlabel('Size of Input')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Sorting Algorithm Performance')
    plt.legend()
    plt.grid(True)

    canvas = FigureCanvas(plt.gcf())
    output = io.BytesIO()
    canvas.print_png(output)
    plt.close()

    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
