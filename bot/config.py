import os


# config parameters
telegram_token = str(os.environ["telegram_token"])
openai_api_key = str(os.environ["openai_api_key"])
use_chatgpt_api = bool(os.environ.get("use_chatgpt_api", True))
allowed_telegram_usernames = eval(os.environ.get("allowed_telegram_usernames")) if os.environ.get("allowed_telegram_usernames") else []
new_dialog_timeout = os.environ.get("new_dialog_timeout",600)
