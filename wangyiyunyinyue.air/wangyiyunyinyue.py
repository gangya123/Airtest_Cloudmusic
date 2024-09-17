# -*- encoding=utf8 -*-
__author__ = "ypn"

from airtest.core.api import *

auto_setup(__file__, devices=["android://127.0.0.1:5037/127.0.0.1:7555"])

def start_Cloudmusic():
    clear_app("com.netease.cloudmusic")
    start_app("com.netease.cloudmusic")
    touch(Template(r"tpl1726561455481.png", record_pos=(-0.004, 0.404), resolution=(720, 1280)))
    wait(Template(r"tpl1726562487258.png", record_pos=(0.0, 0.243), resolution=(720, 1280)))
    assert_exists(Template(r"tpl1726564420703.png", record_pos=(-0.011, 0.244), resolution=(720, 1280)), "成功进入网易云音乐登录页面")

    
def qq_login():
    touch(
        Template(r"tpl1726562619129.png", record_pos=(0.15, 0.761), resolution=(720, 1280)))
    
    assert_exists(Template(r"tpl1726564109535.png", record_pos=(-0.078, 0.622), resolution=(720, 1280)), "到达QQ登录页面")
    touch(Template(r"tpl1726562630149.png", record_pos=(-0.076, 0.618), resolution=(720, 1280)))
    touch(Template(r"tpl1726562636736.png", record_pos=(0.215, 0.769), resolution=(720, 1280)))
    wait(Template(r"tpl1726563279814.png", record_pos=(-0.243, -0.144), resolution=(720, 1280)))
    touch(Template(r"tpl1726563284516.png", record_pos=(-0.001, 0.531), resolution=(720, 1280)))
    wait(Template(r"tpl1726563344313.png", record_pos=(-0.006, -0.203), resolution=(720, 1280)))
    touch(Template(r"tpl1726563349191.png", record_pos=(-0.006, 0.537), resolution=(720, 1280)))
    assert_exists(Template(r"tpl1726564314390.png", record_pos=(-0.397, 0.812), resolution=(720, 1280)), "QQ登陆成功！")

    
def enter_Cloudmusic():
    sleep(5)
    wait(Template(r"tpl1726562859029.png", record_pos=(0.004, -0.676), resolution=(720, 1280)), timeout=50)
    touch(Template(r"tpl1726562863492.png", record_pos=(-0.007, 0.833), resolution=(720, 1280)))
    assert_exists(Template(r"tpl1726564373940.png", record_pos=(-0.379, -0.185), resolution=(720, 1280)), "进入到网易云音乐主页")
    
def xuezhiqian():
    touch(Template(r"tpl1726562894654.png", record_pos=(-0.147, -0.754), resolution=(720, 1280)))
    wait(Template(r"tpl1726562909751.png", record_pos=(0.412, -0.751), resolution=(720, 1280)))
    text("薛之谦")
    touch(Template(r"tpl1726562965915.png", record_pos=(0.411, -0.754), resolution=(720, 1280)))
    touch(Template(r"tpl1726562980612.png", record_pos=(-0.343, -0.326), resolution=(720, 1280)))
    sleep(3)
    assert_exists(Template(r"tpl1726565169963.png", record_pos=(-0.004, -0.132), resolution=(720, 1280)), "成功进入薛之谦个人主页！")
    touch(Template(r"tpl1726563008138.png", record_pos=(-0.254, 0.589), resolution=(720, 1280)))
    swipe(Template(r"tpl1726563056123.png", record_pos=(-0.26, 0.596), resolution=(720, 1280)), vector=[-0.0445, -0.3898])
    touch(Template(r"tpl1726563069665.png", record_pos=(-0.436, -0.16), resolution=(720, 1280)))
    assert_exists(Template(r"tpl1726564566411.png", record_pos=(0.303, 0.794), resolution=(720, 1280)), "播放热门歌曲成功")


for i in range(1):
    try:
        start_Cloudmusic()
        qq_login()
        enter_Cloudmusic()
        xuezhiqian()
        print("启动成功！")
    except:
        print("启动失败！")