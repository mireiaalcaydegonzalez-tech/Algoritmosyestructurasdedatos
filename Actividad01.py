from collections import deque


# ============================================
# (a) STACK IMPLEMENTADO USANDO QUEUE
# ============================================

class StackUsingQueue:
    """
    Implementación de un Stack (Pila) usando una Queue (Cola).
    La cola es la estructura de datos subyacente.
    """

    def __init__(self):
        """Inicializa el stack con una cola vacía."""
        self.queue = deque()

    def push(self, item):
        """
        Inserta un elemento en el top del stack.

        Complejidad: O(n) donde n es el número de elementos en el stack.

        Estrategia: Agregamos el nuevo elemento al final de la cola,
        luego rotamos todos los elementos anteriores al final para que
        el nuevo elemento quede al inicio (que es nuestro "top").
        """
        # Agregar el nuevo elemento al final de la cola
        self.queue.append(item)

        # Rotar los elementos para que el último agregado quede al inicio
        # Movemos todos menos el último elemento al final
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        Extrae y retorna el elemento en el top del stack.

        Complejidad: O(1) - operación directa sobre la cola.

        Dado nuestro diseño donde el top siempre está al inicio,
        simplemente hacemos dequeue del inicio.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.queue.popleft()

    def peek(self):
        """
        Retorna el elemento en el top sin removerlo.

        Complejidad: O(1)
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.queue[0]

    def is_empty(self):
        """
        Verifica si el stack está vacío.

        Complejidad: O(1)
        """
        return len(self.queue) == 0

    def size(self):
        """
        Retorna el número de elementos en el stack.

        Complejidad: O(1)
        """
        return len(self.queue)


# ============================================
# (b) ANÁLISIS DE COMPLEJIDAD TEMPORAL
# ============================================

"""
COMPLEJIDAD TEMPORAL:

push(item): O(n)
    - append(item): O(1)
    - Loop que rota n-1 elementos: O(n)
      * Cada iteración: popleft() [O(1)] + append() [O(1)]
      * n-1 iteraciones
    - TOTAL: O(1) + O(n) = O(n)

    JUSTIFICACIÓN: Para mantener el invariante de que el "top" del stack
    está siempre al inicio de la cola (donde podemos hacer pop eficiente),
    necesitamos reorganizar todos los elementos cada vez que hacemos push.

pop(): O(1)
    - popleft(): O(1) (operación directa sobre deque)
    - TOTAL: O(1)

    JUSTIFICACIÓN: Dado que el top está siempre al inicio de la deque,
    simplemente hacemos popleft() que es una operación O(1).

TRADE-OFF:
    Este diseño sacrifica la eficiencia de push() por la eficiencia de pop().
    En un stack tradicional, ambas operaciones son O(1).
    Aquí es un trade-off donde push() es O(n) y pop() es O(1).
"""


# ============================================
# (c) VALIDADOR DE PARÉNTESIS BALANCEADOS
# ============================================

def is_balanced_parentheses(expression):
    """
    Verifica si una expresión matemática tiene paréntesis balanceados.

    Usa un Stack para hacer seguimiento de los paréntesis abiertos.

    Args:
        expression (str): La expresión matemática a validar.

    Returns:
        bool: True si está balanceada, False en caso contrario.

    Complejidad: O(n) donde n es la longitud de la expresión.
    """
    stack = StackUsingQueue()

    # Caracteres de paréntesis que nos interesan
    opening = {'(', '[', '{'}
    closing = {')', ']', '}'}
    matching = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in opening:
            # Paréntesis abierto: lo agregamos al stack
            stack.push(char)
        elif char in closing:
            # Paréntesis cerrado: verificamos que coincida con el último abierto
            if stack.is_empty():
                # No hay paréntesis abierto para cerrar
                return False

            last_opening = stack.pop()

            # Verificar que el paréntesis cerrado coincide con el abierto
            if matching[last_opening] != char:
                return False

    # Al final, el stack debe estar vacío
    # Si no lo está, hay paréntesis abiertos sin cerrar
    return stack.is_empty()


# ============================================
# PRUEBAS Y DEMOSTRACIONES
# ============================================

if __name__ == "__main__":
    # Pruebas del Stack implementado con Queue
    print("=" * 60)
    print("PRUEBAS - Stack usando Queue")
    print("=" * 60)

    stack = StackUsingQueue()
    print(f"Stack vacío: {stack.is_empty()}")  # True

    # Push de elementos
    print("\nHaciendo push de: 10, 20, 30, 40")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    print(f"Tamaño del stack: {stack.size()}")  # 4
    print(f"Top del stack (peek): {stack.peek()}")  # 40

    # Pop de elementos
    print("\nHaciendo pop...")
    print(f"pop() -> {stack.pop()}")  # 40
    print(f"pop() -> {stack.pop()}")  # 30
    print(f"Tamaño después de 2 pops: {stack.size()}")  # 2

    print("\n" + "=" * 60)
    print("PRUEBAS - Validador de Paréntesis Balanceados")
    print("=" * 60)

    test_cases = [
        ("((2+3)*(4-1))", True),
        ("((2+3)*4-1))", False),
        ("()", True),
        ("(())", True),
        ("([{}])", True),
        ("([)]", False),
        ("((())", False),
        ("())", False),
        ("2+3)*4-1", False),
        ("((2+3)*(4-1))", True),
        ("", True),
        ("2+3*4-1", True),
    ]

    print("\nEvaluando expresiones:\n")
    for expression, expected in test_cases:
        result = is_balanced_parentheses(expression)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{expression}' -> {result} (esperado: {expected})")