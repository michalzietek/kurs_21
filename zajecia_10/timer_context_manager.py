import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        print("Otwieramy context managera")

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"Nasz context manager działał {elapsed_time} czasu")
