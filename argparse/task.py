import argparse

# ключ --help или -h добавляется по умолчанию

parser = argparse.ArgumentParser(prog='average',
                                 description='My frist argument parser.',
                                 epilog='Returns the arithmetic mean')
parser.add_argument('numbers',
                    metavar='N',
                    type=float,
                    nargs='*',
                    help='press some numbers')
args = parser.parse_args()
print(f'Получили экземпляр Namespace: {args=}')
print(f'У Namespace работает точечная нотация: {args.numbers =}')
print(f'Объекты внутри могуть быть любыми: {args.numbers[1] = }')

r"""
Примеры запуска в терминале:
python .\task.py 42 3.14 73
python .\task.py --help
python .\task.py Hello world!
"""

