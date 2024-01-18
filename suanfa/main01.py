def name(args):
    print("Hello World" + args)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # 每次遍历将最大的元素冒泡到末尾
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def my_bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # 在已排序部分找到合适的插入位置
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    name("你好")
    # 示例用法
    nums = [5, 2, 9, 1, 3]
    # my_bubble_sort(nums)
    insertion_sort(nums)
    print(nums)  # 输出：[1, 2, 3, 5, 9]
