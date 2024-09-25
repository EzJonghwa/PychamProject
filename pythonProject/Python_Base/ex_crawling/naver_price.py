from datetime import timezone

import requests
import cx_Oracle


from mylogger import make_logger
from apscheduler.schedulers.blocking import BlockingScheduler
import pytz
seoul = pytz.timezone("Asia/Seoul")
log = make_logger("naver.log","naver_price.py")
sql_merge = """

MERGE INTO stock_bbs a
USING dual
ON (a.code = :code
    and a.discussion_id = :discussionId)
WHEN MATCHED THEN
    UPDATE SET a.read_count = :readCount
             , a.good_count = :goodCount
             , a.bad_count = :badCount
             , a.comment_count = :commentCount
WHEN NOT MATCHED THEN
    INSERT (a.code, a.discussion_id, a.read_count, a.good_count, a.bad_count
          , a.comment_count, a.title, a.contents, a.create_dt)
    VALUES (:code, :discussionId, : readCount, :goodCount, :badCount, :commentCount
          , :title , :contents, to_date(:createDt,'YYYY-MM-DD HH24:MI:SS'))
"""

def get_price(code):
    price_url = f"https://polling.finance.naver.com/api/realtime/domestic/stock/{code}"
    res = requests.get(price_url)
    if res.status_code ==200:
        json_data = res.json()
        log.info("get_price 정상 요청")
        # print(json_data['datas'][0]['closePrice'].replace(',',''))
        return json_data['datas'][0]['closePrice'].replace(',','')
    else:
        log.info(f"{res.status_code} 응답으로 현재 가격 X")
def get_bbs(code):
    bbs_url = f"https://m.stock.naver.com/api/discuss/localStock/{code}?rsno=0&size=100"
    res = requests.get(bbs_url)
    arr =[]
    if res.status_code ==200:
        json_data = res.json()

        for v in json_data:
            bbs = {
                "discussionId": v['discussionId'],
                "code": v['itemCode'],
                "title": v['title'],
                "contents": v['contents'],
                "createDt": v['date'][:19],
                #  [:19] 문자열 자르기 19번째 까지
                "readCount": v['readCount'],
                "goodCount": v['goodCount'],
                "badCount": v['badCount'],
                "commentCount": v['commentCount']
                }
            print(bbs)
            arr.append(bbs)
    return arr

def current_price():
    conn = cx_Oracle.connect("member", "member", "127.0.0.1:1521/xe")
    cur = conn.cursor()
    cur.execute("SELECT *FROM STOCK WHERE USE_YN ='Y'")
    rows = cur.fetchall()
    try:
        for row in rows:
            code = row[0]
            nm = row[1]
            log.info(f"{code}:{nm}현재 가격 가져오기")
            price = get_price(code)
            cur.execute("INSERT INTO stock_price(code,price) VALUES(:1,:2)", [code,price])
            log.info(f"{code}:{price}")
            bbs_arr = get_bbs(code)
            log.info(f"{nm} 토론방 수집 시작")
            for bbs in bbs_arr:
                cur.execute(sql_merge,bbs)
            log.info(f"{nm} 토론방 수집 종료")
    except Exception as e:
        print(str(e))
        log.error(f"{e}")
        conn.rollback()
    else:
        conn.commit()
        log.info("current price 정상 저장")
    finally:
        conn.close()
        log.info("current price 완료")
if __name__ == '__main__':

    # get_price('005930')
    # get_bbs('005930')

    # log.info("start_main")
    # current_price()
    # sched = BlockingScheduler()
    # sched.add_job(current_price, 'interval', minutes=2, timezone=seoul)
    # sched.start()
    current_price()

