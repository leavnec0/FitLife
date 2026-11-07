import sys

print("Меню ресторана:")
for line in sys.stdin:
    dish = line.strip()
    print("- ", dish)