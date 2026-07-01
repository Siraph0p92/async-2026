# Program 1: The First Coroutine Function
# Concept: Understanding async def and how it differs from a normal function.


import asyncio

async def greet():
    print("Hello!")

coro_object = greet()  # This creates a coroutine object but does not execute it.

print(type(coro_object))  # This will print the coroutine object representation.

coro_object.close()  # This will close the coroutine object, preventing it from being awaited or executed.