import urllib.request as request

import pandas as pd
from bs4 import BeautifulSoup


def get_html_content(url):
    """
    获取网页内容
    :param url:
    :return:
    """
    html = request.urlopen(url).read()
    # pprint.pprint(html)
    return html


def analysis_list(analysis_list, save_file):
    index = (r"门类", r"大类", r"种类", r"小类", r"类别名称", r"说明")
    frame = pd.DataFrame(columns=index)

    now_men = ""
    now_da = ""
    now_zhong = ""
    for i, item in enumerate(analysis_list.find_all("tr")):
        fields = item.find_all("td")
        one_data = []
        for j, field in enumerate(fields):
            s = get_field_text(field)
            if j == 0:
                if not str_is_empty(s):
                    now_men = s.strip()
                    now_da = ""
                    now_zhong = ""
                one_data.append(now_men)
            elif j == 1:
                if not str_is_empty(s):
                    now_da = s.strip()
                    now_zhong = ""
                one_data.append(now_da)
            elif j == 2:
                if not str_is_empty(s):
                    now_zhong = s.strip()
                one_data.append(now_zhong)
            else:
                one_data.append(s.strip())

        frame.loc[i + 1] = one_data
    frame.to_excel(save_file)


def get_field_text(tag):
    b = tag.find("b")
    if b is not None:
        return b.get_text()
    else:
        return tag.get_text()


def str_is_empty(s):
    return s is None or len(s.strip()) == 0


if __name__ == '__main__':
    data_url = r"http://114.xixik.com/hangyefenlei/"
    save_file = "data.xls"
    read_data = get_html_content(data_url)
    soup = BeautifulSoup(read_data, "html.parser")

    body = soup.find("div", class_="body")
    for child_body in body.find_all("div", class_="lindBox"):
        h2 = child_body.find("h2")
        if h2 is not None and str(h2.string).startswith("国民经济行业分类与代码"):
            table_list = child_body.find("table").find("tbody")
            analysis_list(table_list, save_file)
    # analysis child_body
