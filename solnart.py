import threading
import time

import tg_app
import tg_msg


while True:
    # start = time.time()
    threads = []
    for u, p in zip(tg_app.url_list, tg_app.price_list):
        t = threading.Thread(target=tg_app.parse_link, args=[u, p])
        t.daemon = True
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    result = tg_app.result
    if len(result) > 0:
        for i in result:
            for j in result[i]:
                # print(j)
                tg_msg.send_mess(j)
                time.sleep(2)
    threads.clear()
    # print(result)
    # print(len(result))
    # print(time.time() - start)

    tg_app.result.clear()
    time.sleep(10)
