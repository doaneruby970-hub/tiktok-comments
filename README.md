# TikTok Comments

Monitor TikTok live room comments in real time and output them to the console.

## Features

- Connect to the live room of a specified TikTok account
- Print live room user comments in real time (nickname + comment content)
- Connection success/disconnection event notifications
- Support for HTTP/HTTPS proxy (configured via environment variables)
- Auto-detection of common error scenarios (account not live, network signature errors, etc.)

## Requirements

- Python 3.8+
- TikTokLive library

## Installation

```bash
git clone https://github.com/doaneruby970-hub/tiktok-comments.git
cd tiktok-comments
pip install TikTokLive
```

## Configuration

Configure via environment variables:

| Environment Variable | Description | Default |
|----------|------|--------|
| `TIKTOK_TARGET_USERNAME` | Target TikTok account (include @) | `@tiktok` |
| `HTTP_PROXY` | HTTP/HTTPS proxy address | Empty (direct connection) |

Example (PowerShell):

```powershell
$env:TIKTOK_TARGET_USERNAME = "@some_user"
$env:HTTP_PROXY = "http://127.0.0.1:9674"
python tiktok_comments.py
```

Example (Linux/macOS):

```bash
export TIKTOK_TARGET_USERNAME="@some_user"
export HTTP_PROXY="http://127.0.0.1:9674"
python tiktok_comments.py
```

## Usage

```bash
python tiktok_comments.py
```

After running, the script attempts to connect to the target account's live room. If the account is currently live streaming, comments are printed in real time; otherwise, a "not live" message is shown.

Press `Ctrl+C` to stop the program.

## Output Example

```
正在尝试连接 @tiktok 的直播间 (使用代理: 9674)...
✅ 连接成功！账号 @tiktok 正在直播。
等待评论中... (按 Ctrl+C 结束)
------------------------------
[user123]: 哈哈太搞笑了
[nice_guy]: 主播加油！
...
❌ 直播已结束或连接断开。
```

## Notes

- The target account must be **currently live streaming**, otherwise a "not live" message will be shown and the program will exit.
- If the network environment is restricted, configure an HTTP proxy. The proxy address is set via the `HTTP_PROXY` environment variable and is used for both HTTP and HTTPS proxies.
- If you encounter signature errors (SIGN_NOT_200 / 504), the proxy may be unstable or the account may be flagged; try testing with a different account.
- This tool is intended for learning and technical research only. Please comply with platform terms of service.
