import asyncio
import threading
mutex = threading.Lock()
async def factorial(name, queue):
    f = 0
    mutex.acquire()
    try:
        number= queue.pop()
    except:
        number=0
    mutex.release()

    for i in range(1, number+1):
        print(f"Task {name}: Compute Sum({i})...")
        await asyncio.sleep(1)
        f += i
    print(f"Task {name}: Sum({number}) = {f}")
async def main(queue):
# Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A",queue),
        factorial("B",queue),
        factorial("C",queue),
        factorial("D",queue),
        factorial("E",queue)
    )
if __name__ == '__main__':
    queue=[]
    queue.append(3)
    queue.append(7)
    queue.append(4)
    queue.append(3)
    asyncio.run(main(queue))