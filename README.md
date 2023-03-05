# ChatGPT Telegram Bot: **Fast. No daily limits. Special chat modes**

<div align="center">
<img src="https://raw.githubusercontent.com/karfly/chatgpt_telegram_bot/main/static/header.png" align="center" style="width: 100%" />
</div>

<p align="center">
<a href="https://t.me/chatgpt_karfly_bot" alt="Run Telegram Bot shield"><img src="https://img.shields.io/badge/RUN-Telegram%20Bot-blue" /></a>
</p>

We all love [chat.openai.com](https://chat.openai.com), but... It's TERRIBLY laggy, has daily limits, and is only accessible through an archaic web interface.

This repo is ChatGPT re-created with GPT-3.5 LLM as Telegram Bot. **And it works great.**

You can deploy your own bot, or use mine: [@chatgpt_karfly_bot](https://t.me/chatgpt_karfly_bot)

## News
- *2 Mar 2023*: Added support of [ChatGPT API](https://platform.openai.com/docs/guides/chat/introduction). It's enabled by default and can be disabled with `use_chatgpt_api` option in config. Don't forget to **rebuild** you docker image (`--build`).

## Features
- Low latency replies (it usually takes about 3-5 seconds) 
- No request limits
- Code highlighting
- Special chat modes: 👩🏼‍🎓 Assistant, 👩🏼‍💻 Code Assistant, 🎬 Movie Expert. More soon
- Support of [ChatGPT API](https://platform.openai.com/docs/guides/chat/introduction)
- List of allowed Telegram users
- Track $ balance spent on OpenAI API

## Bot commands
- `/retry` – Regenerate last bot answer
- `/new` – Start new dialog
- `/mode` – Select chat mode
- `/balance` – Show balance
- `/help` – Show help

## Setup
1. Get your [OpenAI API](https://openai.com/api/) key

2. Get your Telegram bot token from [@BotFather](https://t.me/BotFather)

3. fork this repo and add some secrets (follow this turtoial https://docs.github.com/en/actions/security-guides/encrypted-secrets)


<div align="center">
<img src="https://raw.githubusercontent.com/zhangolve/chatgpt_telegram_bot/main/static/settings.png" align="center" style="width: 100%" />
</div>

The two secrets in the picture must be filled in, and the remaining fields are optional.

other secrets:

| secret name | optional value |default value|
|------|------|------|
|use_chatgpt_api | True of False | True|
|allowed_telegram_usernames | ['username_a','username_b'] | [ ](if empty, the bot is available to anyone)|
|new_dialog_timeout | number(new dialog starts after timeout (in seconds)) | 600|



## References
1. [*Build ChatGPT from GPT-3*](https://learnprompting.org/docs/applied_prompting/build_chatgpt)
