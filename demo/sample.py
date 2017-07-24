#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2017/7/24

"""
__author__ = 'HomgWu'
import threading
from eprogress import LineProgress, CircleProgress, MultiProgressManager
from sys import argv


def mock_multi_progress(progress_manager, sleep_time):
    for i in range(1, 101):
        progress_manager.update(threading.current_thread().name, i)
        time.sleep(sleep_time)


def mock_single_progress(progress_bar, sleep_time):
    for i in range(1, 101):
        progress_bar.update(i)
        time.sleep(sleep_time)


which = argv[1] if len(argv) > 0 else 1

if __name__ == '__main__':
    import time

    which = int(which)

    thread_pool = []
    if which == 1:
        # circle
        circle_progress = CircleProgress(title='circle_thread')
        circle_thread = threading.Thread(target=mock_single_progress, args=(circle_progress, 0.1))
        thread_pool.append(circle_thread)
        circle_thread.start()
    elif which == 2:
        # line
        line_progress = LineProgress(title='line thread')
        line_thread = threading.Thread(target=mock_single_progress, args=(line_progress, 0.05))
        thread_pool.append(line_thread)
        line_thread.start()
    elif which == 3:
        # multi line
        progress_manager = MultiProgressManager()

        thread1 = threading.Thread(target=mock_multi_progress, args=(progress_manager, 0.05), name=str(1001))
        thread2 = threading.Thread(target=mock_multi_progress, args=(progress_manager, 0.2), name=str(1002))
        thread3 = threading.Thread(target=mock_multi_progress, args=(progress_manager, 0.1), name=str(1003))

        thread_pool.append(thread1)
        thread_pool.append(thread2)
        thread_pool.append(thread3)

        progress_manager.put(str(1001), LineProgress(total=100, title='1 thread'))
        progress_manager.put(str(1002), LineProgress(total=100, title='2 thread'))
        progress_manager.put(str(1003), LineProgress(total=100, title='3 thread'))

        thread1.start()
        thread2.start()
        thread3.start()
    else:
        # multi line and circle
        progress_manager = MultiProgressManager()

        thread1 = threading.Thread(target=mock_multi_progress, args=(progress_manager, 0.05), name=str(1001))
        thread2 = threading.Thread(target=mock_multi_progress, args=(progress_manager, 0.2), name=str(1002))
        thread3 = threading.Thread(target=mock_multi_progress, args=(progress_manager, 0.1), name=str(1003))
        thread4 = threading.Thread(target=mock_multi_progress, args=(progress_manager, 0.1), name=str(1004))

        thread_pool.append(thread1)
        thread_pool.append(thread2)
        thread_pool.append(thread3)
        thread_pool.append(thread4)

        progress_manager.put(str(1001), LineProgress(total=100, title='1 thread'))
        progress_manager.put(str(1002), LineProgress(total=100, title='2 thread'))
        progress_manager.put(str(1003), LineProgress(total=100, title='3 thread'))
        progress_manager.put(str(1004), CircleProgress(title='4 thread'))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()

    for t in thread_pool:
        t.join()
    print('\nComplete')
