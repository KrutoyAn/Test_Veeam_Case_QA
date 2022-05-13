import time
import psutil
import os
import sys
import subprocess

platform = sys.platform

path = input('input path: ')
delay = int(input('input delay: '))

if platform == 'win32':
    os.startfile(path)

    process_name = path.split('\\')[-1]
    print(process_name)
    try:
        for i in psutil.process_iter():
            if i.name() == process_name:
                with open('E:\Pythonprojects\Test_Veeam_Case_QA\Task_1\log.txt', 'a') as f:
                    while True:
                        f.write(f'CPU: {i.cpu_percent()} %\n')
                        print(f'CPU: {i.cpu_percent()} %')# The system-wide CPU utilization as a percentage

                        f.write(f'Working Set: {i.memory_full_info()[4]}\n')
                        print(f'Working Set: {i.memory_full_info()[4]}')# Return a named tuple with representing memory information about the process

                        f.write(f'Private Bytes: {i.memory_full_info()[-2]}\n')
                        print(f'Private Bytes: {i.memory_full_info()[-2]}')

                        f.write(f'handle: {i.num_handles()}\n')
                        print(f'handle: {i.num_handles()}')# The number of handles currently used by this process
                        time.sleep(delay)
    except:
        pass

else:
    subprocess.Popen(path)
    process_name = path.split('/')[-1]
    try:
        for i in psutil.process_iter():
            if i.name() == process_name:
                with open('E:\Pythonprojects\Test_Veeam_Case_QA\Task_1\log.txt', 'a') as f:
                    while True:
                        f.write(f'CPU: {i.cpu_percent()} %\n')
                        print(f'CPU: {i.cpu_percent()} %')

                        f.write(f'Resident Set Size: {i.memory_full_info()[0]}\n')
                        print(f'Resident Set Size: {i.memory_full_info()[0]}')

                        f.write(f'Virtual Memory Size: {i.memory_full_info()[1]}\n')
                        print(f'Virtual Memory Size: {i.memory_full_info()[1]}')

                        f.write(f'Descriptors: {i.num_fds()}\n')
                        print(f'Descriptors: {i.num_fds()}')# The number of file descriptors currently opened by this process
                        time.sleep(delay)
    except:
        pass