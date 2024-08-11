import multiprocessing

def calculate_pi_segment(start, end):
    pi_estimate = 0
    for i in range(start, end):
        pi_estimate += ((-1) ** i) / (2 * i + 1)
    return pi_estimate

def calculate_pi(terms, num_processes):
    segment_length = terms // num_processes
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(calculate_pi_segment, [(i * segment_length, (i + 1) * segment_length) for i in range(num_processes)])
    return sum(results) * 4

num_terms = 10000000  # 1천만 항
num_processes = 12     # 12개 스레드
pi_value = calculate_pi(num_terms, num_processes)

print(f"π의 근사값: {pi_value}")
