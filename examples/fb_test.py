# https://docs.lvgl.io/8.1/examples.html
import lvgl as lv
import time

print(lv.__version__)

FONT = lv.font_montserrat_16
BG_COLOR = lv.color_hex(0x003a57)
TXT_COLOR = lv.color_hex(0xf0f0f0)

lv.init()
# Register FB display driver
# https://github.com/lvgl/lv_binding_micropython/blob/master/examples/fb_test.py
disp = lv.linux_fbdev_create()
lv.linux_fbdev_set_file(disp, "/dev/fb0")

scr = lv.scr_act()
#scr.clean()

#style_0 = lv.style_t()
#style_0.init()
#style_0.set_bg_color(BG_COLOR)
#style_0.set_text_color(TXT_COLOR)
#scr.add_style(style_0, 0)

label = lv.label_create(scr)
#label.set_style_text_font(FONT, 0)
lv.obj_set_pos(label, 20, 10)
lv.label_set_text(label, 'Hello, World!')

#lv.screen_load(scr)

start = time.time()

while True:
    stop = time.time()
    diff = int((stop * 1000) - (start * 1000))
    if diff >= 1:
        start = stop
        lv.tick_inc(diff)
        lv.task_handler()

