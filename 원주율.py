
import random
import threading

def calculate_pi_part(samples, result, idx):
    inside_circle = 0
    for _ in range(samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    result[idx] = inside_circle

def calculate_pi(num_samples, num_threads):
    threads = []
    results = [0] * num_threads
    samples_per_thread = num_samples // num_threads

    for i in range(num_threads):
        thread = threading.Thread(target=calculate_pi_part, args=(samples_per_thread, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_inside_circle = sum(results)
    pi_estimate = (total_inside_circle / num_samples) * 4
    return pi_estimate

# 샘플 수와 스레드 수 설정
num_samples = 1000000000 #정확도
num_threads = 12  # i5-1240P의 코어 수에 맞춰 설정 cpu 수

pi_value = calculate_pi(num_samples, num_threads)
print("추정된 원주율 값: {pi_value}")

