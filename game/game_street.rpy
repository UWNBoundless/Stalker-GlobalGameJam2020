################################################################################
## 初始化
################################################################################

init offset = -10

################################################################################
## Game_street
################################################################################
screen game_map_street_1():

    zorder 100

    modal True

    # add 'bg_street_ani1' xpos -50 ypos 0 xoffset global_xoffset
    # add 'bg_street_bg' xpos -50 ypos 0 xoffset global_xoffset
    # add 'bg_street_ani2' xpos -50 ypos 0 xoffset global_xoffset
    add "bg_street_new_ani" xpos -10 xoffset global_xoffset

    timer 0.01 action Show('f_1_110', t=6, s='game_map_street_1')

    timer 2.5 action Show('bf')

    timer 6+2.6-0.5 action Show('m_s', t=1.5, s='game_map_street_1', transition=Dissolve(0.5))

    timer start_time_street+2.5-0.5 action Show('m_walk_slow', t=2.3, s='game_map_street_1')

    timer start_time_street+2.6-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.7-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.8-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+2.9-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.0-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.1-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.2-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.3-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.4-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.5-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.6-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.7-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.8-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+3.9-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.0-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.1-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.2-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.3-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.4-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    timer start_time_street+4.5-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    # timer start_time_street+4.6-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    # timer start_time_street+4.7-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    # timer start_time_street+4.8-0.5 action SetVariable('global_xoffset', global_xoffset-20)
    # timer start_time_street+4.9-0.5 action SetVariable('global_xoffset', global_xoffset-20)

    timer start_time_street+5.5 action Show('m_s', t=999, s='game_map_street_1')

    timer 0.001 action Show('bg_street_lights')

    timer start_time_street+4.1 action [SetVariable('tmp_xoffset', global_xoffset), Return()]

screen game_map_street_2():

    zorder 100

    if abs(global_xoffset) >= (3760-1280):
        timer 0.01 action [ Hide('f_con'),
                            Return('street')]

    if interact >= 5:
        timer 0.01 action [ Hide('f_con'),
                            Return('E1')]

    # add 'bg_street_ani1' xpos -50 ypos 0 xoffset global_xoffset
    # add 'bg_street_bg' xpos -50 ypos 0 xoffset global_xoffset
    # add 'bg_street_ani2' xpos -50 ypos 0 xoffset global_xoffset
    add "bg_street_new_ani" xpos -10 xoffset global_xoffset

    if persistent.street_achieve == 0:
        add 'in_street_1' xpos 0 ypos 0 xoffset global_xoffset

    if abs(global_xoffset) == 400:
        add 'm_s' xpos 130 ypos 690 align(0.5, 1.0)
    if abs(global_xoffset) == 400 and not renpy.get_screen('f_con'):
        add 'f_b' xpos 1720 ypos 690 align(0.5, 1.0) xoffset global_xoffset

    #f 主控
    timer 4.5 action [  SetVariable('tmp_xpos', 2410),
                        Show('f_con')]
    timer 11.5 action [  SetVariable('tmp_xpos', 2710),
                        Show('f_con')]
    timer 17 action [  SetVariable('tmp_xpos', 3550),
                        Show('f_con')]
    timer 25 action [  SetVariable('tmp_xpos', 4000),
                        Show('f_con')]


    ######################################################################

    timer 0.01 action Show('bg_street_lights')

    use game_buttonControll(3760-1280)

screen bg_street_lights():

    zorder 111

    if renpy.get_screen(['game_map_street_1', 'game_map_street_2']):

        add 'bg_street_lights' xpos -50 ypos 0 xoffset global_xoffset*1.15

    else:
        timer 0.01 action Hide('bg_street_lights')