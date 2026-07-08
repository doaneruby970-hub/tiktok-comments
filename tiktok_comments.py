import asyncio
import os
from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent, ConnectEvent, DisconnectEvent

# -------------------------------------------------------
# 【第一步】配置代理（如需代理请设置环境变量）
# 如需代理请设置环境变量 HTTP_PROXY / HTTPS_PROXY
# -------------------------------------------------------
os.environ["http_proxy"] = os.getenv("HTTP_PROXY", "")
os.environ["https_proxy"] = os.getenv("HTTP_PROXY", "")

# -------------------------------------------------------
# 【第二步】配置目标账号
# -------------------------------------------------------
# 设置环境变量 TIKTOK_TARGET_USERNAME
TARGET_USERNAME = os.getenv("TIKTOK_TARGET_USERNAME", "@tiktok")

# 创建客户端 (这里不需要再传 proxy 参数了，因为上面已经配置了全局环境)
client: TikTokLiveClient = TikTokLiveClient(unique_id=TARGET_USERNAME)


# --- 事件处理 ---

@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print(f"✅ 连接成功！账号 @{client.unique_id} 正在直播。")
    print("等待评论中... (按 Ctrl+C 结束)")
    print("-" * 30)


@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    # 打印格式： [用户昵称]: 评论内容
    print(f"[{event.user.nickname}]: {event.comment}")


@client.on(DisconnectEvent)
async def on_disconnect(event: DisconnectEvent):
    print("❌ 直播已结束或连接断开。")


# --- 主程序 ---

if __name__ == '__main__':
    print(f"正在尝试连接 @{TARGET_USERNAME} 的直播间 (使用代理: 9674)...")

    try:
        # 启动
        client.run()
    except Exception as e:
        # 错误处理
        error_msg = str(e)
        if "LiveNotFound" in error_msg or "RoomId" in error_msg:
            print(f"⚠️ 提示：账号 @{TARGET_USERNAME} 现在【没在直播】。")
        elif "SIGN_NOT_200" in error_msg or "504" in error_msg:
            print(f"❌ 网络/签名错误：代理可能不稳定，或者该账号被风控。请尝试换个大号测试。")
        else:
            print(f"❌ 发生错误: {e}")