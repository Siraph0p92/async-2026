# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.
import asyncio

async def greet():
    print("Hello!")

coro_object = greet()
print(f"Coroutine object: {coro_object}")

try:
    coro_object.send(None)
except StopIteration:
    print("Coroutine finished (caught StopIteration)")
