import locale

from aqt import mw
from aqt.utils import showInfo

__all__ = ["get_auto_space_flag", "get_auto_space_name", "get_plugin_menu_name",
           "get_space_name", "get_auto_space_shortcut", "get_space_shortcut",
           "set_auto_space", "mw"]

config = mw.addonManager.getConfig(__name__)
lang = mw.pm.meta.get("defaultLang", "en")


def get_plugin_name():
    plugin_name = config["plugin_name"]
    return plugin_name


def get_plugin_menu():
    plugin_menu = config["plugin_menu"]
    return plugin_menu


def get_plugin_menu_name():
    plugin_menu = get_plugin_menu()
    plugin_menu_name = plugin_menu["name"]
    return plugin_menu_name


def get_menu_actions():
    plugin_menu = get_plugin_menu()
    menu_actions = plugin_menu["actions"]
    return menu_actions


def get_auto_space():
    menu_actions = get_menu_actions()
    auto_space = menu_actions["auto_space"]
    return auto_space


def get_auto_space_flag():
    auto_space = get_auto_space()
    auto_space_flag = auto_space["flag"]
    return auto_space_flag


def get_auto_space_name():
    auto_space = get_auto_space()
    auto_space_name = auto_space["name"] if lang == "zh_CN" else auto_space["en_name"]
    return auto_space_name


def get_auto_space_shortcut():
    auto_space = get_auto_space()
    auto_space_shortcut = auto_space["shortcut"]
    return auto_space_shortcut


def get_space():
    menu_actions = get_menu_actions()
    space = menu_actions["space"]
    return space


def get_space_name():
    space = get_space()
    space_name = space["name"] if lang == "zh_CN" else space["en_name"]
    return space_name


def get_space_shortcut():
    space = get_space()
    space_shortcut = space["shortcut"]
    return space_shortcut


def _set_auto_space_flag(flag):
    auto_space = get_auto_space()
    auto_space["flag"] = flag


def _set_auto_space_name(flag):
    auto_space_flag = flag
    if auto_space_flag is True:
        auto_space_name = "卡片载入后自动帮我加上空格"
        auto_space_en_name = "Space True"
    else:
        auto_space_name = "我要自己决定什么时候要加空格"
        auto_space_en_name = "Space False"

    auto_space = get_auto_space()
    auto_space["name"] = auto_space_name
    auto_space["en_name"] = auto_space_en_name
    showInfo(("设置`%s`成功！" % auto_space_name if lang == "zh_CN" else "Set up `%s` successfully!" % auto_space_en_name))


def set_auto_space(flag):
    _set_auto_space_flag(flag)
    _set_auto_space_name(flag)
    # 保存配置到文件 .../addons21/plugin_num/meta.json
    mw.addonManager.writeConfig(__name__, config)
