### Futures 
É um objeto que contém um valor que esperamos obter em algum ponto no futuro, 
mas não agora.

O futuro tem dois estados o primeiro quando criamos e eles ainda não tem o 
valor\resultado ele esta incompleto, o segundo quando ele já possui o valor.

```python
from asyncio import Future

my_future = Future()

print(f'Is my_future done? {my_future.done()}')

my_future.set_result(42)

print(f'Is my_future done? {my_future.done()}')
print(f'What is the result of my_future? {my_future.result()}')
```

Futures can also be used in await expressions. If we await a future, we’re saying
“pause until the future has a value set that I can work with, and once I have a value,
wake up and let me process it.”


