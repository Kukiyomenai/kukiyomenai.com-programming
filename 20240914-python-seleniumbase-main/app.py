#app.py
from seleniumbase import SB

# ログイン時のCAPTCHA
# with SB(uc=True, incognito=True) as sb:
#     sb.uc_open_with_reconnect(
#         "https://2captcha.com/ja/demo/cloudflare-turnstile", 5
#     )
#     sb.uc_gui_click_captcha()

# 全画面表示のCAPTCHA
# with SB(uc=True, incognito=True) as sb:
#     sb.uc_open_with_reconnect(
#         "https://2captcha.com/ja/demo/cloudflare-turnstile-challenge", 5 
#     )
#     sb.uc_gui_click_captcha()