import subprocess
from datetime import datetime

time_1 = datetime.now()

# I am using linux. Only Linux. Sorry))
# Команда трассировки. Хост it-vi.ru лично мой, хотя трассировку можно запускать совершенно к любому узлу в интернетах))
cmd = '/bin/mtr -4 -o "LS DR AGJMXI NBWV" -zrc 50 it-vi.ru >> test.log'

# cmd2 = ['/bin/mtr', '-o', 'LS DR AGJMXI NBWV', '-zrc', '5', 'it-vi.ru', '>>', 'test.log']

class Mytraceroute:
    def __init__(self, cmd):
        self.time_cm_1 = datetime.now()
        print(f'\n=== Запуск менеджера контекста ==='
              f'\n=== {self.time_cm_1} ===\n')
        self.proc = subprocess.Popen(cmd, shell=True)

    def __enter__(self):
        return self.proc

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.proc.kill()
        self.time_cm_2 = datetime.now()
        print(f'\n=== Конец менеджера контекста ==='
              f'\n=== {self.time_cm_2} ===')
        print(f'\n*** Менеджер контекста выполнился за {(self.time_cm_2 - self.time_cm_1).total_seconds()} секунд. ***\n')

with Mytraceroute(cmd) as shell:
    shell.communicate()

time_2 = datetime.now()
print(f'\n>>> Полностью вся программа выполнилась за {(time_2 - time_1).total_seconds()} секунд. <<<\n'.upper())