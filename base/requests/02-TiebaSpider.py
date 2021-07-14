import requests


class tiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_tmp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "Accept": "* / *",
            "Accept - Encoding": "gzip, deflate, br"}

    def get_url_list(self):
        url_list = []
        for i in range(100):
            url_list.append(self.url_tmp.format(i * 50))
        return url_list
        # return [self.url_tmp.format(i*50) for i in range(100)]

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.header)
        return response.content.decode()

    def save_html(self, html_str, page_num):
        file_path = "{}--第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        # 构造url地址
        url_list = self.get_url_list()

        # 发送请求，获取响应
        for url in url_list:
            html_text = self.parse_url(url)
            # 保存html页面
            self.save_html(html_text, url_list.index(url) + 1)


if __name__ == '__main__':
    tiebaSpider = tiebaSpider("李毅")
    tiebaSpider.run()
