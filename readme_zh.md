# # ChatGPT Telegram Bot Actions: 

不依赖数据库，不依赖docker 环境，只要有一个Public github repo即可创建ChatGPT Telegram Bot ,**当然这也就意味着不会保存聊天记录，所有的聊天记录都暂时保存在Github上，随着workflow重新运行，聊天记录也将销毁，如果介意可以不要使用**

# ChatGPT的功能包括：

- 低延迟回复（通常只需3-5秒）
- 无请求限制
- 代码高亮
- 特殊聊天模式：👩🏼‍🎓助理，👩🏼‍💻代码助理，🎬电影专家。更多
- 支持[ChatGPT API](https://platform.openai.com/docs/guides/chat/introduction)
- 允许的Telegram用户列表


# 启动

为了让chatgpt bot工作，您需要：

1. 从OpenAI获取API密钥。
2. 从@BotFather获取Telegram机器人令牌。
3. Fork此Repo，并添加一些Secrets（按照此教程https://docs.github.com/en/actions/security-guides/encrypted-secrets）。


<div align="center">
<img src="https://raw.githubusercontent.com/zhangolve/chatgpt_telegram_bot/main/static/settings.png" align="center" style="width: 100%" />
</div>

图片中的两个Secrets必须填写，其余字段可选。

其他Secrets：

| Secrets名称 | 可选值 | 默认值 |
|------|------|------|
|use_chatgpt_api | True 或 False | True|
|allowed_telegram_usernames | ['username_a','username_b'] | [ ]（如果为空，bot对任何人都可用）|
|new_dialog_timeout | number（新对话在超时后开始（以秒为单位）） | 600|

4. 转到存储库操作并手动触发此操作

注意：默认情况下，如果workflows 未在6小时内完成，GitHub Actions将在6小时后杀死该workflows 。由于Github Actions的限制，我已经设置了一个workflows ，每5小时重新启动一次。因此，理论上，您只需手动单击一次即可启动workflows ，然后workflows 将能够24小时工作。
