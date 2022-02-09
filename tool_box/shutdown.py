import os
import time
import platform


def shutdown(set_time, is_everyday=False):
    if is_everyday:
        command = f'schtasks /create /tn shutdown_everyday /tr "shutdown -s -t 20" /sc daily /st {set_time}'
        os.system(command)
        print(f'已设置每日 {set_time} 关机计划')
        return f'已设置每日 {set_time} 关机计划'
    else:
        h, m, s = set_time.split(':')
        time_seconds = int(h) * 3600 + int(m) * 60 + int(s)
        print(type(time_seconds))
        now_h, now_m, now_s = time.strftime('%H:%M:%S').split(':')
        now_seconds = int(now_h) * 3600 + int(now_m) * 60 + int(now_s)
        print(type(now_seconds))
        seconds = time_seconds - now_seconds
        if seconds <= 0:
            print('关机时间超出当前时间，是否设置每天关机')
            return '关机时间超出当前时间，是否设置每天关机'
        else:
            os.system("shutdown -s -t {}".format(str(seconds)))
            print(f'已设置 {seconds} 秒后关机')
            return f'已设置 {seconds} 秒后关机'


def stop_shutdown():
    os.system('schtasks /delete /tn shutdown_everyday /f')
    os.system('shutdown -a')


if __name__ == '__main__':
    # time1 = '23:20:00'
    # shutdown(set_time=time1)
    # print(platform.platform())
    # print(platform.architecture())
    stop_shutdown()
