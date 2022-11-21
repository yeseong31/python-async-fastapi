import time
import asyncio


# 코루틴(coroutine) 함수
async def delivery(name, mealtime):
    print(f'{name}에게 배달 완료!')
    await asyncio.sleep(mealtime)
    print(f'{name} 식사 완료, {mealtime}시간 소요...')
    print(f'{name} 그릇 수거 완료')
    return mealtime


async def main():
    result = await asyncio.gather(
        delivery('A', 5),
        delivery('B', 3),
        delivery('C', 4),
    )
    print(result)


# 비동기 함수를 동기적으로 처리하는 방법
# async def main():
#     await delivery('A', 5)
#     await delivery('B', 3)
#     await delivery('C', 4)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
