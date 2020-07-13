################################################################################
## Game_screen Images 初始化
################################################################################

init offset = -1

################################################################################
## Backgrounds
################################################################################
image trash1:
    'bg/home/trash1.png'

image trash2:
    'bg/home/trash2.png'

image start_idle_EN:
    zoom 0.6
    'gui/s_n_EN.png'

image start_hover_EN:
    zoom 0.6
    'gui/s_dead_EN.png'

image start_idle_CN:
    zoom 0.6
    'gui/s_n_CN.png'

image start_hover_CN:
    zoom 0.6
    'gui/s_dead_CN.png'

image bg_templ:
    'gui/templet - bg.png'

# Street
image bg_street_bg:
    'bg/street/street.png'

image bg_street_lights:
    'bg/street/lights.png'

image bg_street_ani1-1:
    'bg/street/ani1-1.png'

image bg_street_ani1-2:
    'bg/street/ani1-2.png'

image bg_street_ani1:
    'bg_street_ani1-1'
    pause 0.5
    'bg_street_ani1-2'
    pause 0.5
    repeat

image bg_street_ani2-1:
    'bg/street/ani2-1.png'

image bg_street_ani2-2:
    'bg/street/ani2-2.png'

image bg_street_ani2:
    'bg_street_ani2-1'
    pause 0.5
    'bg_street_ani2-2'
    pause 0.5
    repeat

# CN
image bg_cn_building:
    'bg/cn/building.png'

image bg_cn_mt:
    'bg/cn/mt.png'

image bg_cn_mid:
    'bg/cn/mid.png'

image bg_cn_sky:
    'bg/cn/sky.png'

image bg_cn_tree:
    'bg/cn/tree.png'

image bg_cn_ani1:
    'bg/cn/ani1.png'

image bg_cn_ani2:
    'bg/cn/ani2.png'

image bg_cn_ani3:
    'bg/cn/ani3.png'

image bg_cn_ani:
    'bg_cn_ani1'
    pause 0.5
    'bg_cn_ani2'
    pause 0.5
    'bg_cn_ani3'
    pause 0.5
    repeat

# ST
image bg_st_shop:
    'bg/shop/shop.png'

image bg_st_label:
    'bg/shop/label.png'

image bg_st_front:
    'bg/shop/front.png'

image bg_st_ani1:
    'bg/shop/ani1.png'

image bg_st_ani2:
    'bg/shop/ani2.png'

image bg_st_ani3:
    'bg/shop/ani3.png'

image bg_st_ani:
    'bg_st_ani1'
    pause 0.5
    'bg_st_ani2'
    pause 0.5
    'bg_st_ani3'
    pause 0.5
    repeat

# home
image bg_hm_bg:
    'bg/home/bg.png'

image bg_hm_ani1:
    'bg/home/ani1.png'

image bg_hm_ani2:
    'bg/home/ani2.png'

image bg_hm_trash1:
    'bg/home/trash1.png'
image bg_hm_trash2:
    'bg/home/trash2.png'

image bg_hm_ani:
    'bg_hm_ani1'
    pause 1.0
    'bg_hm_ani2'
    pause 1.0
    repeat

################################################################################
## Gui
################################################################################
image sarr_idle:
    'gui/game_screen/sarr_idle.png'

image sarr_hover:
    'gui/game_screen/sarr_hover.png'

image farr_idle:
    'gui/game_screen/farr_idle.png'

image farr_hover:
    'gui/game_screen/farr_hover.png'

image inter_idle:
    'gui/game_screen/inter_idle.png'

image inter_hover:
    'gui/game_screen/inter_hover.png'

image ques:
    'gui/game_screen/ques.png'
image lovebox:
    'gui/game_screen/love.png'
image red_h:
    'gui/game_screen/red_h.png'
image red_l:
    'gui/game_screen/red_l.png'
image option_idle:
    zoom 0.25
    "gui/option/option.png"
################################################################################
## Temp Scene 1
################################################################################
image f_w:
    'f_s'
    pause 0.2
    'f_w1'
    pause 0.2
    'f_w2'
    pause 0.2
    'f_w1'
    repeat

################################################################################
## Ani
################################################################################
image c1:
    'cha/cat/c1.png'

image c_w_1:
    'cha/cat/c2.png'
    pause 1.0
    'cha/cat/c3.png'
    pause 1.0
    'cha/cat/c4.png'
    pause 1.0
    'cha/cat/c5.png'
    pause 1.0
    'cha/cat/c6.png'

################################################################################
## Interact
################################################################################
image in_street_1:
    'bg/street/in/1.png'
    pause 5.3
    'bg/street/in/2.png'
    pause 1.2
    'bg/street/in/3.png'
    pause 1.5
    'bg/street/in/4.png'
    pause 1.0
    'bg/street/in/5.png'
################################################################################
## LH
################################################################################
image m_s:
    'cha/m/s.png'

image m_h:
    'cha/m/hide.png'

image f_b:
    'cha/f/b.png'

image f_ht:
    'cha/f/ht.png'

# image f_fin:
#     'cha/f/fin.png'

image f_s:
    'cha/f/s.png'

image f_w1:
    'cha/f/w1.png'

image f_w2:
    'cha/f/w2.png'
################################################################################
## Walk
################################################################################
image m_walk_slow:
    'cha/m/s.png'
    pause 0.2
    'cha/m/w1.png'
    pause 0.2
    'cha/m/w2.png'
    pause 0.2
    'cha/m/w1.png'
    pause 0.2
    'cha/m/s.png'
    pause 0.2
    'cha/m/w-1.png'
    pause 0.2
    'cha/m/w-2.png'
    pause 0.2
    'cha/m/w-1.png'
    pause 0.2
    repeat

image m_walk_fast:
    'cha/m/s.png'
    pause 0.05
    'cha/m/w1.png'
    pause 0.05
    'cha/m/w2.png'
    pause 0.05
    'cha/m/w1.png'
    pause 0.05
    'cha/m/s.png'
    pause 0.05
    'cha/m/w-1.png'
    pause 0.05
    'cha/m/w-2.png'
    pause 0.05
    'cha/m/w-1.png'
    pause 0.05
    repeat

image m_walk_slow_sing:
    'cha/m/s.png'
    pause 0.12
    'cha/m/w1.png'
    pause 0.12
    'cha/m/w2.png'
    pause 0.12
    'cha/m/w1.png'
    pause 0.12
    'cha/m/s.png'

image m_walk_fast_sing:
    'cha/m/s.png'
    pause 0.06
    'cha/m/w1.png'
    pause 0.06
    'cha/m/w2.png'
    pause 0.06
    'cha/m/w1.png'
    pause 0.06
    'cha/m/s.png'
    pause 0.06
    'cha/m/w-1.png'
    pause 0.06
    'cha/m/w-2.png'
    pause 0.06
    'cha/m/w-1.png'
    pause 0.06
    'cha/m/s.png'

image cat_inter:
    'cha/cat/c1.png'
    pause 1.5
    'cha/cat/c2.png'
    pause 0.7
    'cha/cat/c3.png'
    pause 0.7
    'cha/cat/c4.png'
    pause 0.7
    'cha/cat/c5.png'
    pause 0.7
    'cha/cat/c6.png'
    pause 0.7
    'cha/cat/c6.png'
    xoffset -400

image cat_inter_yes:
    'cha/cat/c1.png'
    pause 1.5
    'cha/cat/c2.png'
    pause 0.7
    'cha/cat/c3.png'
    pause 0.7
    'cha/cat/c4.png'
    pause 0.5
    linear 1.0 alpha 0.0
    'cha/m/hold_cat.png'
    alpha 0.0
    linear 2.5 alpha 1.0
    linear 1.5 alpha 0.0

image bf:
    'bg/street/g_1.png'
    alpha 0.0
    linear 1.0 alpha 1.0
    linear 1.0 alpha 0.0
    'bg/street/g_2.png'
    linear 1.0 alpha 1.0

