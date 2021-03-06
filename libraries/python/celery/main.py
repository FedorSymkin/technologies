# coding=utf-8

# http://devacademy.ru/posts/ochered-soobschenij-i-asinhronnyie-zadachi-s-pomoschyu-celery-i-rabbitmq/

from tasks import gen_prime
import time
import logging

def setup_log():
    logging.basicConfig(level=logging.DEBUG)

    fmt = "%(asctime)s [%(name)s] [%(levelname)s]: %(message)s"
    log_formatter = logging.Formatter(fmt)
    root_logger = logging.getLogger()

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)

    root_logger.handlers = []
    root_logger.addHandler(console_handler)


def main():
    log = logging.getLogger('main')
    log.info('put tasks')

    cnt = 20
    tasks = [gen_prime.delay(1000 * (c + 1)) for c in range(cnt)]
    extracted = [False for _ in range(cnt)]

    log.info('waiting tasks')
    while True:
        log.info('wait...')
        for n, task in enumerate(tasks):
            if task.ready() and not extracted[n]:
                res = task.get()
                log.info('res of task {}: {} prime nums'.format(n, len(res)))
                extracted[n] = True

        if all(extracted):
            break

        time.sleep(0.5)

    log.info('finished')


setup_log()
main()


"""
log example:

2019-04-22 09:27:18,466 [main] [INFO]: put tasks
2019-04-22 09:27:18,493 [amqp] [DEBUG]: Start from server, version: 0.9, properties: ....
2019-04-22 09:27:18,494 [amqp] [DEBUG]: using channel_id: 1
2019-04-22 09:27:18,495 [amqp] [DEBUG]: Channel open
2019-04-22 09:27:18,521 [main] [INFO]: waiting tasks
2019-04-22 09:27:18,521 [main] [INFO]: wait...
2019-04-22 09:27:19,553 [main] [INFO]: wait...
2019-04-22 09:27:19,556 [main] [INFO]: res of task 0: 168 prime nums
2019-04-22 09:27:19,559 [main] [INFO]: res of task 1: 303 prime nums
2019-04-22 09:27:19,562 [main] [INFO]: res of task 2: 430 prime nums
2019-04-22 09:27:19,565 [main] [INFO]: res of task 3: 550 prime nums
2019-04-22 09:27:20,179 [main] [INFO]: wait...
2019-04-22 09:27:20,182 [main] [INFO]: res of task 4: 669 prime nums
2019-04-22 09:27:20,185 [main] [INFO]: res of task 5: 783 prime nums
2019-04-22 09:27:20,735 [main] [INFO]: wait...
2019-04-22 09:27:21,279 [main] [INFO]: wait...
2019-04-22 09:27:21,286 [main] [INFO]: res of task 6: 900 prime nums
2019-04-22 09:27:21,837 [main] [INFO]: wait...
2019-04-22 09:27:21,857 [main] [INFO]: res of task 7: 1007 prime nums
2019-04-22 09:27:22,419 [main] [INFO]: wait...
2019-04-22 09:27:22,424 [main] [INFO]: res of task 8: 1117 prime nums
2019-04-22 09:27:22,950 [main] [INFO]: wait...
2019-04-22 09:27:22,953 [main] [INFO]: res of task 9: 1229 prime nums
2019-04-22 09:27:23,468 [main] [INFO]: wait...
2019-04-22 09:27:23,984 [main] [INFO]: wait...
2019-04-22 09:27:24,001 [main] [INFO]: res of task 10: 1335 prime nums
2019-04-22 09:27:24,533 [main] [INFO]: wait...
2019-04-22 09:27:25,064 [main] [INFO]: wait...
2019-04-22 09:27:25,066 [main] [INFO]: res of task 11: 1438 prime nums
2019-04-22 09:27:25,576 [main] [INFO]: wait...
2019-04-22 09:27:26,089 [main] [INFO]: wait...
2019-04-22 09:27:26,602 [main] [INFO]: wait...
2019-04-22 09:27:26,605 [main] [INFO]: res of task 12: 1547 prime nums
2019-04-22 09:27:27,116 [main] [INFO]: wait...
2019-04-22 09:27:27,120 [main] [INFO]: res of task 14: 1754 prime nums
2019-04-22 09:27:27,629 [main] [INFO]: wait...
2019-04-22 09:27:27,631 [main] [INFO]: res of task 13: 1652 prime nums
2019-04-22 09:27:28,139 [main] [INFO]: wait...
2019-04-22 09:27:28,647 [main] [INFO]: wait...
2019-04-22 09:27:29,157 [main] [INFO]: wait...
2019-04-22 09:27:29,160 [main] [INFO]: res of task 15: 1862 prime nums
2019-04-22 09:27:29,669 [main] [INFO]: wait...
2019-04-22 09:27:29,675 [main] [INFO]: res of task 16: 1960 prime nums
2019-04-22 09:27:30,181 [main] [INFO]: wait...
2019-04-22 09:27:30,183 [main] [INFO]: res of task 17: 2064 prime nums
2019-04-22 09:27:30,686 [main] [INFO]: wait...
2019-04-22 09:27:30,688 [main] [INFO]: res of task 18: 2158 prime nums
2019-04-22 09:27:31,190 [main] [INFO]: wait...
2019-04-22 09:27:31,198 [main] [INFO]: res of task 19: 2262 prime nums
2019-04-22 09:27:31,198 [main] [INFO]: finished
"""