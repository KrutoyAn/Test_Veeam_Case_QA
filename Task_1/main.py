import time
import psutil
import os
import sys
import subprocess

platform = sys.platform

path = input('Input path: ')
delay = int(input('Input delay: '))

if platform == 'Win-32':
    os.startfile(path)

    p_name = path.split('\\')[-1]
    print(p_name)
    try:
        for i in psutil.process_iter():
            if i.name() == p_name:
                with open('log.txt', 'a') as f:
                    while True:
                        f.write(f'CPU: {i.cpu_percent()}\n')
                        print(f'CPU: {i.cpu_percent()}')  # The system-wide CPU utilization as a percentage

                        f.write(f'Working Set: {i.memory_full_info()[4]}\n')
                        print(f'Working Set: {i.memory_full_info()[4]}') # Return a named tuple with representing memory information about the process

                        f.write(f'Private Bytes: {i.memory_full_info()[-2]}\n')
                        print(f'Privat Bytes: {i.memory_full_info()[-2]}')

                        f.write(f'Handle: {i.num_handles()}\n')
                        print(f'Hendle: {i.num_handles()}') # The number of handles currently used by this process

                        time.sleep(delay)
    except:
        pass

else:
    subprocess.Popen(path)
    p_name = path.split('/')[-1]
    try:
        for i in psutil.process_iter():
            if i.name() == p_name:
                with open('log.txt', 'a') as f:
                    while True:
                        f.write(f'CPU: {i.cpu_percent()}\n')
                        print(f'CPU: {i.cpu_percent()}')

                        f.write(f'Resident set size: {i.memory_full_info()[0]}\n')
                        print(f'Resident set size: {i.memory_full_info()[0]}')

                        f.write(f'Virtual memory size: {i.memory_full_info()[1]}\n')
                        print(f'Virtual menory size: {i.memory_full_info()[1]}')

                        f.write(f'Descriptor: {i.num_fds()}\m')
                        print(f'Descriptor: {i.num_fds}') # The number of file descriptors currently opened by this process

                        time.sleep(delay)
    except:
        pass
