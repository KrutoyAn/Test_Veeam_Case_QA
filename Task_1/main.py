import time
from datetime import datetime

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
                        now = datetime.now()
                        current_time = now.strftime("%x %H:%M:%S")

                        f.write(f'Date: {current_time}\n')
                        f.write(f'CPU: {i.cpu_percent(interval=0.0)} %\n')# The system-wide CPU utilization as a percentage
                        f.write(f'Working Set: {i.memory_full_info()[4]}\n')# Return a named tuple with representing memory information about the process (WSET)
                        f.write(f'Private Bytes: {i.memory_full_info()[-2]}\n')#Return a named tuple with representing memory information about the process (Private)
                        f.write(f'handle: {i.num_handles()}\n')# The number of handles currently used by this process
                        f.write('-' * 10)
                        f.write('\n')

                        print(f'Date: {current_time}')
                        print(f'CPU: {i.cpu_percent(interval=0.0)} %')
                        print(f'Working Set: {i.memory_full_info()[4]}')
                        print(f'Private Bytes: {i.memory_full_info()[-2]}')
                        print(f'handle: {i.num_handles()}')
                        print('-' * 10)

                        #print(i.memory_full_info()) # Get tuple
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
                        now = datetime.now()
                        current_time = now.strftime("%x %H:%M:%S")

                        f.write(f'Date: {current_time}\n')
                        f.write(f'CPU: {i.cpu_percent()} %\n')
                        f.write(f'Resident Set Size: {i.memory_full_info()[0]}\n')#Return a named tuple with representing memory information about the process (RSS)
                        f.write(f'Virtual Memory Size: {i.memory_full_info()[1]}\n')#Return a named tuple with representing memory information about the process (VMS)
                        f.write(f'Descriptors: {i.num_fds()}\n')
                        f.write('-' * 10)
                        f.write('\n')

                        print(f'Date: {current_time}')
                        print(f'CPU: {i.cpu_percent()} %')
                        print(f'Resident Set Size: {i.memory_full_info()[0]}')
                        print(f'Virtual Memory Size: {i.memory_full_info()[1]}')
                        print(f'Descriptors: {i.num_fds()}') # The number of file descriptors currently opened by this process
                        print('-' * 10)

                        time.sleep(delay)
    except:
        pass

