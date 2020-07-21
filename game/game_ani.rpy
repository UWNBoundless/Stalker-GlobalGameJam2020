################################################################################
## 初始化
################################################################################

init offset = -1

################################################################################
## Ani
################################################################################
screen f_1_110(t, s):

    zorder 105

    if renpy.get_screen(s):

        add 'f_w' ypos 690 align(0.5, 1.0) xoffset global_xoffset at b

        timer t action Hide('f_1_110')
    
    else:
        timer 0.01 action Hide('m_s')

screen bf():

    zorder 105
    
    if renpy.get_screen('game_map_street_1'):
        add 'bf' xpos -50 ypos 0 xoffset global_xoffset

screen m_walk_slow(t, s):

    zorder 105

    if renpy.get_screen(s):
        add 'm_walk_slow' xpos 130 ypos 690 align(0.5, 1.0)

        timer t action Hide('m_walk_slow')

    else:
        timer 0.01 action Hide('m_s')

screen m_s(t, s):

    zorder 105

    if renpy.get_screen(s):

        add 'm_s' xpos 130 ypos 690 align(0.5, 1.0):
            if t < 99:
                at a

        timer t action Hide('m_s')

    else:
        timer 0.01 action Hide('m_s')

################################################################################
## 共存
################################################################################
screen chaMoveCon(cha):

    zorder 105

    if renpy.get_screen([   'game_map_street_2',
                            'game_map_cn_1',
                            'game_map_shop_1',
                            'game_map_home_1']):
        if renpy.random.randint(0, 100) >= persistent.val:
            timer 0.01 action Play('sound', 'sound/hei.mp3'), SetVariable('persistent.val', persistent.val-2), SetVariable("persistent.pleasuretimes_achievements.", persistent.pleasuretimes_achievements+1)
            add 'lovebox' xpos 130+200 ypos 400 align(0.5, 1.0)
        add cha xpos 130 ypos 690 align(0.5, 1.0)

screen f_con():

    zorder 105

    if renpy.get_screen([   'game_map_street_2',
                            'game_map_home_1']):

        if tmp_xpos != f_xpos:
            add 'f_w' xpos tmp_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset at f_w_con
            timer 4 action [SetVariable('f_xpos', tmp_xpos),
                            Hide('f_con'), Show('f_con')]
        elif abs((130+abs(global_xoffset))) >= f_xpos-350 and abs((130+abs(global_xoffset))) <= f_xpos+350:
            timer 0.01 action Return('BE1')
        elif abs((130+abs(global_xoffset))) >= f_xpos-750 and abs((130+abs(global_xoffset))) <= f_xpos+750:
            timer 0.01 action Play('sound','sound/warn.mp3'), SetVariable('persistent.f_ht_times', persistent.f_ht_times+1)
            if persistent.f_ht_times == 1 or persistent.f_ht_times == 2:
                add 'ques' xpos f_xpos-150 ypos 400 align(0.5, 1.0) xoffset global_xoffset
            elif persistent.f_ht_times ==3 or persistent.f_ht_times == 4:
                add 'red_l' xpos f_xpos-150 ypos 400 align(0.5, 1.0) xoffset global_xoffset
            elif persistent.f_ht_times == 5:
                add 'red_h' xpos f_xpos-150 ypos 400 align(0.5, 1.0) xoffset global_xoffset
            if persistent.f_ht_times == 5:
                add 'f_fin' xpos f_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset
            else:
                add 'f_ht' xpos f_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset
        else:
            add 'f_b' xpos f_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset

    elif renpy.get_screen([ 'game_map_cn_1',
                            'game_map_shop_1']):

        if tmp_xpos != f_xpos:
            add 'f_w' xpos tmp_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset at f_w_con
            timer 4 action [SetVariable('f_xpos', tmp_xpos),
                            Hide('f_con'), Show('f_con')]
        elif abs((130+abs(global_xoffset))) >= f_xpos-620 and abs((130+abs(global_xoffset))) <= f_xpos+620:
            timer 0.01 action Return('BE1')
        elif abs((130+abs(global_xoffset))) >= f_xpos-870 and abs((130+abs(global_xoffset))) <= f_xpos+870:
            timer 0.01 action Play('sound','sound/warn.mp3'), SetVariable('persistent.f_ht_times', persistent.f_ht_times+1)
            if persistent.f_ht_times == 1 or persistent.f_ht_times == 2:
                add 'ques' xpos f_xpos-150 ypos 400 align(0.5, 1.0) xoffset global_xoffset
            elif persistent.f_ht_times ==3 or persistent.f_ht_times == 4:
                add 'red_l' xpos f_xpos-150 ypos 400 align(0.5, 1.0) xoffset global_xoffset
            elif persistent.f_ht_times == 5:
                add 'red_h' xpos f_xpos-150 ypos 400 align(0.5, 1.0) xoffset global_xoffset
            if persistent.f_ht_times == 5:
                add 'f_fin' xpos f_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset
            else:
                add 'f_ht' xpos f_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset
        else:
            add 'f_b' xpos f_xpos ypos 690 align(0.5, 1.0) xoffset global_xoffset
