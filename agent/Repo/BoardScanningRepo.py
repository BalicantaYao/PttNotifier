from DataDriver.PGDataDriver import PGDataDriver


class BoardScanningRepo():

    def __init__(self):
        self.pg_driver = PGDataDriver()

    def insert(self, scanning_info):
        sql = """
            INSERT INTO subscriptions_boardscanning
            (board_name, page_number_of_last_scan, last_scan_pages_count)
            VALUES ('{0}', '{1}', '{2}');
        """.format(
            scanning_info['board_name'],
            scanning_info['page_number_of_last_scan'],
            scanning_info['last_scan_pages_count']
            )
        self.pg_driver.open_pg_connection()
        cursor = self.pg_driver.get_pg_cursor()
        self.pg_driver.execute_and_commit(sql, cursor)
        self.pg_driver.close_pg_connection()
        pass

    def get(self):
        sql = """
            SELECT * FROM subscriptions_boardscanning;
        """

        self.pg_driver.open_pg_connection()
        cursor = self.pg_driver.get_pg_cursor()
        rows = self.pg_driver.execute_and_fetchall(sql, cursor)
        self.pg_driver.close_pg_connection()
        scanning_info_list = []
        for row in rows:
            item = {
                'board_name': row[0],
                'page_number_of_last_scan': row[1],
                'last_scan_pages_count': row[2]
            }
            scanning_info_list.append(item)
        return scanning_info_list

    def update(self, id):
        pass

    def delete(self, id):
        pass
