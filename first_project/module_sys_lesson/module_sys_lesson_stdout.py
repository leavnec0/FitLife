import sys

print("Введите список покупок и нажмите Enter(Ctrl+Z / Ctrl+D для завершения):")
print("(Windows: Ctrl+Z + Enter, Linux/Mac: Ctrl+D)")

purchases = sys.stdin.read()  # Читает всё до конца потока
print("\nВаш список покупок:")
print(purchases)