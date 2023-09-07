import json
import requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

area_dict = {
    86: "北京",
    87: "天津",
    88: "河北",
    89: "山西",
    85: "内蒙古",
    84: "辽宁",
    83: "吉林",
    62: "黑龙江",
    94: "上海",
    92: "江苏",
    93: "浙江",
    95: "安徽",
    97: "福建",
    96: "江西",
    91: "山东",
    90: "河南",
    99: "湖北",
    98: "湖南",
    100: "广东",
    101: "广西",
    102: "海南",
    104: "重庆",
    103: "四川",
    105: "贵州",
    106: "云南",
    107: "西藏",
    108: "陕西",
    109: "甘肃",
    110: "青海",
    110: "宁夏",
    111: "新疆",
}


def find_key_by_value(dictionary, target_value):
    reversed_dict = {value: key for key, value in dictionary.items()}
    return reversed_dict.get(target_value)


base_url = "https://data.rmtc.org.cn/gis/listsation0_{}M.html"


# area_name = input("write your place name：")


# for num in area_dict.keys():


def main(area_name):
    all_data = {}
    # 通过传入地区名称来找到对应的地区值
    num = find_key_by_value(area_dict, area_name)
    # 生成对应的url
    url = base_url.format(num)
    # 生成对应的的地区名称
    # area_name = area_dict[num]

    # 解析html
    response = requests.get(url)
    html = response.text
    if not isinstance(html, str):
        soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
    else:
        soup = BeautifulSoup(html, "html.parser")

    # 提取需要的数据
    content = []
    for item in soup.select("li.datali"):
        name = item.select_one("div.divname").get_text(strip=True)
        value = item.select_one("span.label").text
        time = item.select_one("span.showtime").text

        content.append({"name": name, "value": value, "time": time})

    all_data = {"area": area_name, "content": content}
    with open("provent.json", "w") as f:
        json.dump(all_data, f, ensure_ascii=False)
    return all_data
