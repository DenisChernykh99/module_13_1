import asyncio
import time


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for i in range(1, 6):
        delay = 1 / power
        await asyncio.sleep(delay)
        print(f'Силач {name} поднял шар #{i}')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    tasks = [
        asyncio.create_task(start_strongman('Иван', 0.8)),
        asyncio.create_task(start_strongman('Петр', 1.2)),
        asyncio.create_task(start_strongman('Алексей', 1.0))
    ]

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)


# Запускаем турнир
if __name__ == "__main__":
    asyncio.run(start_tournament())
