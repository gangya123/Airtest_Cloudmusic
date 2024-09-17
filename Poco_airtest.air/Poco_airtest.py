# -*- encoding=utf8 -*-
__author__ = "ypn"

from airtest.core.api import *

auto_setup(__file__)

clear_app("com.NetEase")
start_app("com.NetEase")

sleep(5)


from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

# 通过name属性进行定位，然后点击
poco("btn_start").click()

# basic test
def basic_test():
    poco("basic").wait_for_appearance()
    poco("basic").click()

    # input
    if poco("star_single").exists():
        poco("Placeholder").click()
        text("111")
        touch([1174,607])

    # 断言是否输入成功        
    assert_equal(poco("pos_input").child("Text").get_text(), "111", "成功输入111")

    poco("btn_back").click()

# drag drop test
def drag_drop():
    poco("drag_and_drop").click()
    poco("shell").wait_for_appearance()

    # 移动星星
    stars = poco("playDragAndDrop").child("star")
    for star in stars:
        star.drag_to(poco("shell"))

    sleep(2)
    score = poco("scoreVal").get_text()
    assert_equal(score, "100", "移动全部成功，得分100！")
    poco("btn_back").click()

# list view test
def list_vieww():
    poco("list_view").click()
    bar = poco("Handle")
    for i in range(2):
        bar.swipe([0, 0.1])
    for i in range(2):
        bar.swipe("up")

    poco("Text (2)").click()
    item2 = poco("list_view_current_selected_item_name").get_text()
    assert_equal(item2, "Item 2", "成功点击 item 2")

    poco("btn_back").click()

# local positioning
def local_positioning():
    poco("local_positioning").click()


    poco(texture="icon").focus([0,0]).long_click()
    poco(texture="dec_shark").focus([0.5,0.5]).long_click()
    poco(texture="citun").focus([1,1]).long_click()

    poco("btn_back").click()

# wait UI test
def wait_UI():
    poco("wait_ui").click()

    yellow = poco("yellow")
    blue = poco("blue")
    bomb = poco("bomb")

    poco.wait_for_any([yellow, blue, bomb])

    bomb.wait_for_appearance()
    bomb.click()
    catch_count = poco("catch_count").get_text()
    assert_equal(catch_count, "1", "成功点击炸弹，得分1")

    poco("btn_back").click()


# wait UI 2
def wait_UI_2():
    poco("wait_ui2").click()

    yellow = poco("yellow")
    blue = poco("blue")
    black = poco("black")

    poco.wait_for_all([yellow, blue, black])

    poco("black").exists()

    for i in range(2):
        poco("btn_back").click()
    

basic_test()
drag_drop()
list_vieww()
local_positioning()
wait_UI()
wait_UI_2()

stop_app("com.NetEase")
