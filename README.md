# Library asyncio

- [Courotine](#courotine)


### Courotine
Podemos pensar em coroutine como uma função normal do python com super poderes,
ela pode pausar a sua execução e executar outras tarefas até o momento em que 
ela possa continuar a ser executada. Poder rodar outros codigos enquanto a 
função aguarda um retorno da ao nosso programa o poder da concorencia.

Para criar uma coroutine usamos a palavra reservada `async def`. Coroutine não 
são executadas quando chamadas, ao invex é retornado um objeto que será executado
mais tarde. Para rodar uma coroutine ela precisa estar em um `event loop`.

#### asyncio.run()
O `asyncio.run()` faz algumas coisas, cria um `event loop` roda a coroutina até
finalizar a tarefa, então limpa e finaliza o `event loop`.

```python
import asyncio

async def coroutine_add_one(number: int) -> int:
    return number + 1

result = asyncio.run(coroutine_add_one(1))
print(result)

>>>2
```

O real beneficio do `asyncio` é pausar a execução e deixar o `event loop` rodar
outras tarefas até que a tarefa que foi pausada já esteja pronta para continuar
a ser executada.

### Pausar uma execução `await`
Para pausar uma execução usamos a palavra reservada `await`. O `await` é usualment 
seguida por uma coroutina (mais especificament um objeto `awaitable`).

Usar `await` antes de uma coroutine irá executa-lá, também irá pausar.

