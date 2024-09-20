# 用于格式化消息的工具函数
def format_message(feed_name, entry):
    return f"【{feed_name}】新文章:\n标题: {entry.title}\n链接: {entry.link}"
