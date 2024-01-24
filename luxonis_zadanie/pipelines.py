import psycopg2
from psycopg2 import Error

class PostgresPipeline:
    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host='db',
            dbname='sreality',
            user='admin',
            password='admin'
        )
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute(
                "INSERT INTO flats (title, image_url) VALUES (%s, %s)",
                (item['title'], item['image_url'])
            )
            self.connection.commit()
            return item
        except Error as e:
            self.connection.rollback()
            spider.logger.error(f"Error processing item: {e}")
            return item  # Alebo môžete rozhodnúť o inom spracovaní chyby.
