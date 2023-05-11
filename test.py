import lvgl as lv
import time

lv.init()
print('LVGL initilized')

disp = lv.sdl_window_create(480, 320)
print('disp:', disp)

group = lv.group_create()
print('group:', group)

lv.group_set_default(group)

mouse = lv.sdl_mouse_create()
print('mouse:', mouse)

keyboard = lv.sdl_keyboard_create()
print('keyboard:', keyboard)

lv.indev_set_group(keyboard, group)
print('lv_indev_set_group')


btn = lv.btn_create(lv.scr_act())
lv.obj_set_size(btn, 75, 30)
lv.obj_center(btn)

def on_click(e):
    print('clicked')

event_cb = lv.event_cb_t(on_click)

lv.obj_add_event(btn, event_cb, lv.EVENT_CLICKED, None)

start = time.time()

while True:
    stop = time.time()
    diff = int((stop * 1000) - (start * 1000))
    if diff >= 1:
        start = stop
        lv.tick_inc(diff)
        lv.task_handler()