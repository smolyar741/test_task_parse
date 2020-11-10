import logging
import bs4
import requests
import collections
import csv
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('wb')


ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'brand_name',
        'goods_name',
        'url',
        'image_link',
    ),
)

HEADERS = (
    'title',
    'category',
    'url',
    'image_url',
)


class Client:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
            'Accept-Language': 'ru',
        }
        self.result = []

    def load_page(self):
        url = 'https://www.wildberries.ru/catalog/sport/vidy-sporta/futbol/myachi'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('div.dtList.i-dtList.j-card-item')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        # logger.info(block)
        #logger.info('=' * 100)

        url_block = block.select_one(
            'a.ref_goods_n_p.j-open-full-product-card')
        if not url_block:
            logger.error('no url_block')
            return

        url = url_block.get('href')
        if not url:
            logger.error('no href')
            return

        name_block = block.select_one('div.dtlist-inner-brand-name')
        if not name_block:
            logger.error(f'no name_block on {url}')

        brand_name = name_block.select_one('strong.brand-name')
        if not brand_name:
            logger.error(f'no brand_name on {url}')

        brand_name = brand_name.text
        brand_name = brand_name.replace('/', '').strip()

        goods_name = name_block.select_one('span.goods-name')
        if not goods_name:
            logger.error(f'no goods_name on {url}')
            return

        goods_name = goods_name.text.strip()

        image_block = block.select_one('img.thumbnail')
        if not image_block:
            logger.error(f'no image_block on {url}')
            return

        image_link = image_block.get('src')
        if not image_link:
            logger.error('no src')
            return


        self.result.append(ParseResult(
            url=f' https://www.wildberries.ru{url}',
            brand_name=f'{brand_name}',
            goods_name=f' {goods_name}',
            image_link=f' https:{image_link}',
        ))

        logger.debug(
            '%s, %s, %s, %s',
            f'https://www.wildberries.ru{url}',
            brand_name,
            goods_name,
            f'https:{image_link}',)
        logger.debug('-' * 100)

    def save_results(self):
        path = '/Users/nikitasmolar/test_task/wildberries.csv'
        with open(path, 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(HEADERS)
            for item in self.result:
                writer.writerow(item)

        with open('wildberries.csv') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        with open('wb.json', 'w', encoding='utf-8') as f:
            json.dump(rows, f)


    def run(self):
        text = self.load_page()
        self.parse_page(text=text)
        logger.info(f'Получили {len(self.result)} карточек')
        self.save_results()

if __name__=='__main__':
        parser = Client()
        parser.run()
