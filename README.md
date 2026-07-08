# TikTok Comments

实时监控 TikTok 直播间评论并输出到控制台。

## 功能特性

- 连接到指定 TikTok 账号的直播间
- 实时打印直播间用户评论（昵称 + 评论内容）
- 连接成功/断开事件提示
- 支持 HTTP/HTTPS 代理（通过环境变量配置）
- 自动检测常见错误场景（账号未开播、网络签名错误等）

## 环境要求

- Python 3.8+
- TikTokLive 库

## 安装

```bash
git clone https://github.com/your-username/tiktok-comments.git
cd tiktok-comments
pip install TikTokLive
```

## 配置

通过环境变量进行配置：

| 环境变量 | 说明 | 默认值 |
|----------|------|--------|
| `TIKTOK_TARGET_USERNAME` | 目标 TikTok 账号（含 @） | `@tiktok` |
| `HTTP_PROXY` | HTTP/HTTPS 代理地址 | 空（直连） |

示例（PowerShell）：

```powershell
$env:TIKTOK_TARGET_USERNAME = "@some_user"
$env:HTTP_PROXY = "http://127.0.0.1:9674"
python tiktok_comments.py
```

示例（Linux/macOS）：

```bash
export TIKTOK_TARGET_USERNAME="@some_user"
export HTTP_PROXY="http://127.0.0.1:9674"
python tiktok_comments.py
```

## 使用方式

```bash
python tiktok_comments.py
```

运行后会尝试连接目标账号的直播间。如果该账号正在直播，将实时打印评论；否则提示未开播。

按 `Ctrl+C` 停止程序。

## 输出示例

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

## 注意事项

- 目标账号必须**正在直播**，否则会提示未开播并退出。
- 如果网络环境受限，请配置 HTTP 代理。代理地址通过 `HTTP_PROXY` 环境变量设置，会被同时用作 HTTP 和 HTTPS 代理。
- 如遇到签名错误（SIGN_NOT_200 / 504），可能是代理不稳定或账号被风控，建议更换大号测试。
- 本工具仅用于学习和技术研究，请遵守平台使用条款。
