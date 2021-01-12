import re

def get_text_from_class(soup, class_name):
    return soup.find(class_=class_name).get_text(strip=True)


def get_rate(soup):
    pattern = "Rated対象：\s*(.*)"
    result = re.match(pattern, soup)

    return result.group(1) if result else "-"


def get_date(soup):
    pattern = "(.*?)\+0900開始"
    result = re.match(pattern, soup)
    return result.group(1) if result else "開始時刻未定"
