from anki.hooks import addHook, remHook
from aqt.qt import *  # import all of the Qt GUI library

# __all__ = ["get_auto_space_flag", "get_auto_space_name", "get_plugin_menu_name",
#            "get_space_name", "get_auto_space_shortcut", "get_space_shortcut",
#            "set_auto_space", "mw"]
from .config import *
from .utils import auto_space, once_space


def auto_space_switch(auto_space_obj):
    old_auto_space_flag = get_auto_space_flag()  # 获取旧标志
    new_auto_space_flag = not old_auto_space_flag  # 获取新标志
    set_auto_space(new_auto_space_flag)  # 更新 auto_space 配置
    if new_auto_space_flag is True:
        # 通过钩子 prepareQA，在重新加载 QA 时更新文本
        addHook("prepareQA", auto_space)
    else:
        remHook("prepareQA", auto_space)
    new_auto_space_name = get_auto_space_name()
    auto_space_obj.setText(new_auto_space_name)


def space_switch():
    if hasattr(mw, "reviewer") and \
       hasattr(mw.reviewer, "_showQuestion") and \
       hasattr(mw.reviewer, "_reps"):
        from anki.cards import Card
        real_getQA = Card._getQA
        # 通过包裹原 Card._getQA 方法，更新 QA 文本
        Card._getQA = once_space(Card._getQA)
        # 重新加载卡片到 Question 处
        mw.reviewer._showQuestion()
        Card._getQA = real_getQA


def main():
    mw.form.menuTools.addSeparator()
    menu_name = get_plugin_menu_name()
    menu_space = mw.form.menuTools.addMenu(menu_name)
    mw.form.menuTools.addSeparator()

    auto_space_name = get_auto_space_name()
    action_auto_space = QAction(auto_space_name, mw)
    menu_space.addAction(action_auto_space)

    space_name = get_space_name()
    action_space = QAction(space_name, mw)
    menu_space.addAction(action_space)

    auto_space_shortcut = get_auto_space_shortcut()
    action_auto_space.setShortcut(auto_space_shortcut)
    action_auto_space.triggered.connect(
        lambda: auto_space_switch(action_auto_space))

    space_shortcut = get_space_shortcut()
    action_space.setShortcut(space_shortcut)
    action_space.triggered.connect(space_switch)


main()
