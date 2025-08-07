from concurrent.futures import ThreadPoolExecutor, as_completed

def risky(n):
    if n in [2, 3, 8]:
        raise ValueError("Boom!")
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(risky, i) for i in range(10)]
    print(futures)

    for future in futures:
        try:
            print("Result:", future.result())
        except Exception as e:
            print("Error:", e)

