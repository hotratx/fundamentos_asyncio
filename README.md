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
### Await

O real beneficio do `asyncio` é pausar a execução e deixar o `event loop` rodar
outras tarefas até que a tarefa que foi pausada já esteja pronta para continuar
a ser executada.

### Pausar uma execução `await`
Para pausar uma execução usamos a palavra reservada `await`. O `await` é usualment 
seguida por uma coroutina (mais especificament um objeto `awaitable`).

Usar `await` antes de uma coroutine irá executa-lá, ela também serve para 
pausar a função até que ela esteja pronta para continuar a ser executada.

Exemplos que não rodam de forma sequencial:

```python
import asyncio

async def add_one(number: int) -> int:
    return number + 1

async def main() -> None:
    one_plus_one = await add_one(1)     
    two_plus_one = await add_one(2)    
    print(one_plus_one)
    print(two_plus_one)

asyncio.run(main())
```
No primeiro `await` na chamada do add_one(1) o programa será pausado até o 
retorno da função add_one(1) para em seguida executar o add_one(2). O seu funcionamento
será o mesmo que uma função normal de código sequencial.

```python
import asyncio
from util import delay

async def add_one(number: int) -> int:
    return number + 1

async def hello_world_message() -> str:
    await delay(1)
    return ‘Hello World!’

async def main() -> None:
    message = await hello_world_message()      
    one_plus_one = await add_one(1)       
    print(one_plus_one)
    print(message)
asyncio.run(main())
```
O `await` antes fo hello_world_message irá pausar a coroutina até que está 
retorne um valor. O comportamento do código é sequencial.

#### Rodando as coroutines como tasks
Antes quando chamamos a coroutine diretamente nos não a colocamos 
no `event loop`. Tasks são wrappers sobre coroutines que agendam a coroutine 
para rodar no `event loop` o mais breve possível. Este agendamento e execução 
acontecem de forma não bloqueante, uma vez criada a task, nos podemos executar 
o código instantaneamente enquanto a task está em execução. Isso contrasta com 
o uso da palavra -chave Aguardar que age de maneira bloqueadora, o que 
significa que pausamos toda a coroutina até o resultado da expressão retornar.
O fato de podermos criar tarefas e agendá-las para executar instantaneamente no 
`event loop` significa que nós podemos executar multiplas tarefas no mesmo tempo.

### Criando tasks
Para criar uma `task` usamos a função `asyncio.create_task`. Quando chamamos 
está função é retornardo um objeto `tasks` instantaneamente. Depois que temos
um objeto `task` podemos colocar o `await` assim será retornado o resultado 
quando completado.

```python
import asyncio
from util import delay

async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)

asyncio.run(main())
```
Aqui criamos uma `task` que requer 3 segundos para ser executada, o print retorna 
<class '_asyncio.Task'>, que mostra que não é uma coroutine mas sim uma `task`. 

#### Rodando multiplas tasks concorentes
Se executarmos um coroutine diretamento com asyncrio.run(main()) não estamos 
colocando ela no `loop event` para ser executado, logo não podemos executar nada 
simultaneamente. Para executar coroutines simultaneamente precisamos usar as `tasks`.
As `tasks` são envolucros em torno de uma coroutine que a agendam para serem 
executadas no `loop event` o mais rápido possível. Esse programação e execução 
acontecem de maneira não bloqueante, o que significa que uma vez que criamos a 
`task` podemos executar outro código instantaneamente enquanto a `task` está em 
execução. Isso contrasta com o `await` que age de maneira bloquadora, o que 
significa que pausamos toda a coroutine até o resultado que ela aguarda retorne.

O fato de podermos criar tarefas e agendá-las para executar instantaneamente no evento
Loop significa que podemos executar várias tarefas aproximadamente ao mesmo tempo. Quando estes
As tarefas envolvem uma operação de longa duração, qualquer espera que aconteça acontecerá simultaneamente.

Uma vez chamada `asyncio.create_task(delay(3))` ela será enviada para o `loop event`
e será executada imediatamente sem bloquear o nosso thread principal, logo nosso 
codigo continua sendo executado nas linhas abaixo.


```python
import asyncio
from util import delay

async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))
    await sleep_for_three
    await sleep_again
    await sleep_once_more

asyncio.run(main())
```
A função será executada em torno de 3 segundos, pois estão sendo executadas de 
forma concorente.

### Cancelando Tasks
As `tasks` possui um método `cancel` para parar a task. O cancelamento de uma
`task` irá levantar um `CancelledError`, log devemos manipular este erro.

```python
import asyncio
from asyncio import CancelledError
from util import delay

async def main():
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0
    while not long_task.done():
        print('Task not finished, checking again in a second.')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == 5:
            long_task.cancel()
    try:
        await long_task
    except CancelledError:
        print('Our task was cancelled')

asyncio.run(main())
```

Uma vez chamado o `long_task.cancel()` a task não será cancelada imediatamente, 
ela será cancelada no momento em que ela chegar em um `await`.

