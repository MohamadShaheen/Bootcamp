from PIL import Image
import threading
from multiprocessing import cpu_count, Process
import time


def single_thread():
    image = Image.open('images/img1.jpg')
    width, height = image.size
    new_image = Image.new('RGB', (width, height))

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            reversed_pixel = tuple(255 - value for value in pixel)
            new_image.putpixel((x, y), reversed_pixel)

    new_image.save('images/reversed_image.jpg')


def process_pixels(image, new_image, width, start_y, end_y):
    for y in range(start_y, end_y):
        for x in range(width):
            pixel = image.getpixel((x, y))
            reversed_pixel = tuple(255 - value for value in pixel)
            new_image.putpixel((x, y), reversed_pixel)


def main():
    start_time = time.perf_counter()
    single_thread()
    end_time = time.perf_counter()
    total_time_single = end_time - start_time

    start_time = time.perf_counter()

    image = Image.open('images/img1.jpg')
    width, height = image.size
    new_image = Image.new('RGB', (width, height))

    num_processes = cpu_count()
    step = height // num_processes

    processes = []
    for i in range(num_processes):
        start_y = i * step
        end_y = start_y + step if i < num_processes - 1 else height
        process = Process(target=process_pixels, args=(image, new_image, width, start_y, end_y))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    new_image.save('images/reversed_image.jpg')

    end_time = time.perf_counter()
    total_time_multi = end_time - start_time

    with open('output/output.txt', 'w') as file:
        file.write(f'Total time taken using single thread is {total_time_single}\n'
                   f'Total time taken using multi thread is {total_time_multi}')


if __name__ == '__main__':
    main()
