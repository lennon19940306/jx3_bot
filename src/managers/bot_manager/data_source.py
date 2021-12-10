from datetime import datetime, timedelta
from typing import Optional

from src.modules.bot_info import BotInfo
from src.modules.group_info import GroupInfo
from src.modules.plugin_info import PluginInfo
from src.modules.search_record import SearchRecord
from src.modules.token_info import TokenInfo
from src.modules.user_info import UserInfo
from src.utils.log import logger


async def bot_connect(bot_id: int) -> None:
    '''链接机器人'''
    await BotInfo.bot_connect(bot_id)


async def bot_disconnect(bot_id: int) -> None:
    '''机器人断开链接'''
    await BotInfo.bot_disconnect(bot_id)


async def clean_bot(outtime: int) -> int:
    '''清理bot数据，返回清理bot数量'''
    bot_list = await BotInfo.get_disconnect_bot()
    nowtime = datetime.now()
    count = 0
    for bot in bot_list:
        bot_id = bot.get('bot_id')
        last_left: datetime = bot.get('last_left')+timedelta(hours=outtime)
        last_left = last_left.replace(tzinfo=None)
        if nowtime > last_left:
            await _clean_bot(bot_id)
            count += 1
    return count


async def _clean_bot(bot_id: int) -> None:
    '''清理Bot数据'''
    log = f'bot（{str(bot_id)}）正在清理表：bot_info'
    logger.debug(log)
    await BotInfo.detele_bot(bot_id)
    log = f'bot（{str(bot_id)}）正在清理表group_info'
    logger.debug(log)
    await GroupInfo.detele_bot(bot_id)
    log = f'bot（{str(bot_id)}）正在清理表plugin_info'
    logger.debug(log)
    await PluginInfo.detele_bot(bot_id)
    log = f'bot（{str(bot_id)}）正在清理表user_info'
    logger.debug(log)
    await UserInfo.detele_bot(bot_id)
    log = f'bot（{str(bot_id)}）正在清理表token_info'
    logger.debug(log)
    await TokenInfo.detele_bot(bot_id)
    log = f'bot（{str(bot_id)}）正在清理表search_record'
    logger.debug(log)
    await SearchRecord.detele_bot(bot_id)
    log = f'bot（{str(bot_id)}）数据清理完毕'
    logger.debug(log)


async def set_bot_owner(bot_id: int, owner_id: int) -> Optional[bool]:
    '''
    :说明
        设置管理员

    :参数
        * bot_id：机器人QQ
        * owner_id：管理员QQ

    :返回
        * bool：成功为True，False表示管理员已存在
        * None：表示机器人记录不存在
    '''
    owner = await BotInfo.get_owner(bot_id)
    if owner is not None:
        return False
    flag = await BotInfo.set_owner(bot_id, owner_id)
    if flag:
        return True
    else:
        return None


async def clean_bot_owner(bot_id: int, owner_id: int) -> Optional[bool]:
    '''
    :说明
        清除机器人管理员

    :参数
        * bot_id：机器人QQ
        * owner_id：管理员QQ

    :返回
        * bool：成功为True，False表示当前用户不是管理员
        * None：表示机器人记录不存在
    '''
    owner = await BotInfo.get_owner(bot_id)
    if owner is None:
        return None
    if owner != owner_id:
        return False
    await BotInfo.clean_owner(bot_id)
    return True


async def get_all_bot() -> list[dict]:
    '''返回bot所有数据'''
    data = await BotInfo.get_all_bot()
    return data


async def clean_one_group(bot_id: int, group_id: int) -> None:
    '''清理一个机器人，一个群数据'''
    # 清理插件
    await PluginInfo.deltele_group(bot_id, group_id)
    # 清理用户
    await UserInfo.delete_group(bot_id, group_id)
    # 清理群信息
    await GroupInfo.delete_one(bot_id, group_id)


async def get_bot_owner(bot_id: int) -> Optional[int]:
    '''
    获取bot主人id
    '''
    owner_id = await BotInfo.get_owner(bot_id)
    return owner_id


async def get_bot_nickname(bot_id: int) -> str:
    '''获取nickname'''
    return await BotInfo.get_nickname(bot_id)
