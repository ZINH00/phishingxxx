from phishingxxx.analyzer import crawl_website

url = "https://www.daum.net"
blocked = crawl_website(url)

# 예측 수행
if blocked:
    print(f'URL: {url}, RESULT: 피싱 사이트')
else:
    print(f'URL: {url}, RESULT: 안전 사이트')
