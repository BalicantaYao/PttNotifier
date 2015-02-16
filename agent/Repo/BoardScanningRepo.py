__author__ = 'tsaihung-ju'
from ..DataDriver.PGDataDriver import PGDataDriver

class BoardScanningRepo():

    def __init__(self):
        self.pg_driver = PGDataDriver()

    def insert(self, scanning_info):
        sql = """
            INSERT INTO subscriptions_boardScanning
            (notified_date, notified_time, notified_type, match_url, subscription_user_id)
            VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');
        """.format(
            notification_obj['date'], notification_obj['time'],
            notification_obj['type'], notification_obj['url'],
            notification_obj['subscription_id']
            )
        self.pg_driver.open_pg_connection()
        cursor = self.pg_driver.get_pg_cursor()
        self.pg_driver.execute_and_commit(sql, cursor)
        self.pg_driver.close_pg_connection()
        pass

    def get(self):
        pass

    def update(self, id):
        pass

    def delete(self, id):
        pass
