from pkg.plugin.context import register, handler, BasePlugin, APIHost, EventContext
from pkg.plugin.events import * 
import requests
import logging
import mirai

# 注册插件
@register(name="setu", description="setu plugin", version="0.1", author="SkyFuture")
class Setulugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        self.logger = logging.getLogger(__name__)

    # 异步初始化
    async def initialize(self):
        pass

    def setu_url(self, url):
        resp = requests.get(
            url
        )
        return resp.url

    # 当收到个人/群聊消息时触发
    @handler(PersonNormalMessageReceived)
    @handler(GroupNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message.strip()  
        if msg == "涩图":
            image_url = "https://www.dmoe.cc/random.php"
            image_msg = mirai.Image(url=self.setu_url(image_url))
            ctx.add_return("reply", [image_msg, f"awa~"])
            ctx.prevent_default()
            return
        
    # 插件卸载时触发
    def __del__(self):
        pass
