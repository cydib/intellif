import functools
import os
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **keyword):
        start = time.perf_counter()
        ret = func(*args, **keyword)
        time_coast = time.perf_counter() - start
        print(f"Finish: {round(time_coast, 2)} second(s) Func: {func.__name__}()")
        return ret 

    return wrapper

@timer
def get_img(img_path):
    return [os.path.join(root, pic) for root, dirs, files in os.walk(img_path) for pic in files if
            pic.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
