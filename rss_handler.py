import feedparser
from wecom_rss.wechat_api import send_to_wechat

# 预设 RSS 源
rss_feeds = {
    "TechCrunch": "http://feeds.feedburner.com/TechCrunch/",
}

# 存储已发送的文章链接，避免重复推送
sent_articles = set()

def check_rss_updates(feed_name, rss_url):
    feed = feedparser.parse(rss_url)
    for entry in feed.entries:
        if entry.link not in sent_articles:
            content = f"【{feed_name}】有新内容更新：\n标题: {entry.title}\n链接: {entry.link}"
            send_to_wechat(content)
            sent_articles.add(entry.link)

def run_rss_checker():
    for feed_name, rss_url in rss_feeds.items():
        check_rss_updates(feed_name, rss_url)
