async def task_1(i: int, coroutine_tracker: list):
    coroutine_tracker.append(1)

    if i == 0:
        return

    if i > 5:
        await task_2(i // 2, coroutine_tracker)
    else:
        await task_2(i - 1, coroutine_tracker)


async def task_2(i: int, coroutine_tracker: list):
    coroutine_tracker.append(2)
    
    if i == 0:
        return

    if i % 2 == 0:
        await task_1(i // 2, coroutine_tracker)
    else:
        await task_2(i - 1, coroutine_tracker)


async def coroutines_execution_order(i: int = 42) -> int:
    # Отследите порядок исполнения корутин при i = 42 и верните число, соответствующее ему.
    #
    # Когда поток управления входит в task_1 добавьте к результату цифру 1, а когда он входит в task_2,
    # добавьте цифру 2.
    #
    # Пример:
    # i = 7
    # return 12212

    coroutine_tracker = []
    await task_1(i, coroutine_tracker)

    return int(''.join(list(map(str, coroutine_tracker))))

