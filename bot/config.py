import os


# config parameters
telegram_token = str(os.environ["telegram_token"])
openai_api_key = str(os.environ["openai_api_key"])
use_chatgpt_api = bool(os.environ.get("use_chatgpt_api", True))
allowed_telegram_usernames_env = os.environ.get("allowed_telegram_usernames")
allowed_telegram_usernames = eval(allowed_telegram_usernames_env) if allowed_telegram_usernames_env else []
new_dialog_timeout_env = os.environ.get("new_dialog_timeout")
new_dialog_timeout = int(new_dialog_timeout_env) if new_dialog_timeout_env else 600

chatgpt_price_per_1000_tokens = 0.002
gpt_price_per_1000_tokens = 0.02
whisper_price_per_1_min = 0.006
