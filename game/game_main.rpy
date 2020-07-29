################################################################################
## 初始化
################################################################################

init offset = -1

default persistent.caught_achievements = 0
default persistent.pleasuretimes_achievements = 0
default persistent.street_achievements = 0
default persistent.nothing_achievements = 0
default persistent.trash_achievements = 0
default persistent.cat_achievements = 0
default persistent.dead_times = 0

################################################################################
## Main
################################################################################
screen game_buttonControll(xoffset_max):

    zorder 500

    if not renpy.get_screen('game_map_street_1'):

        if abs( abs(f_xpos) - abs(global_xoffset)) > 1700:
            # timer 0.01 action [ SetVariable('persistent.dead_times', persistent.dead_times+1),
            #                     Return('BE2')]
            timer 0.01 action [ Return('BE2')]
        elif persistent.f_ht_times>5:
            # timer 0.01 action [ SetVariable('persistent.caught_times', persistent.caught_times+1),
            #                     Return('BE1')]
            timer 0.01 action [ Return('BE1')]

        # text _(str(interact)) xpos 50 ypos 0 color '#000'
        # text _(str(global_xoffset)) xpos 50 ypos 20 color '#000'
        # text _(str(persistent.trash_counts)) xpos 50 ypos 45 color '#000'
        # text _(str(tmp_xpos)) xpos 50 ypos 70 color '#000'
        # text _(str(persistent.street_achieve)) xpos 100 ypos 0 color '#000'
        # text _(str(persistent.street_achieve)) xpos 100 ypos 0 color '#000'
        # text _(str(persistent.cn_cat_inter)) xpos 100 ypos 70 color '#000'
        # text _(str(persistent.f_ht_times)) xpos 100 ypos 140 color '#000'
        # text _(str(persistent.trash_counts)) xpos 100 ypos 210 color '#000'

        imagebutton:
            keysym 'z'
            xalign 0.95 yalign 0.2
            auto 'sarr_%s'
            # if abs(global_xoffset-10) > abs(xoffset_max):
            #     action NullAction()
            # elif abs(global_xoffset-10) >= abs(xoffset_max) and abs(global_xoffset) < abs(xoffset_max):
            #     action SetVariable('global_xoffset', xoffset_max*-1)
            # else:
            if tmp_xpos != f_xpos:
                action [SetVariable('global_xoffset', global_xoffset-20),
                    Hide('chaMoveCon'),
                    Show('chaMoveCon', cha='m_walk_slow_sing')]
            else:
                action [SetVariable('global_xoffset', global_xoffset-20),
                        Hide('chaMoveCon'), Hide('f_con'),
                        Show('chaMoveCon', cha='m_walk_slow_sing'),
                        Show('f_con')]

        imagebutton:
            keysym 'x'
            xalign 0.95 yalign 0.5
            auto 'farr_%s'
            # if abs(global_xoffset-150) > abs(xoffset_max):
            #     action NullAction()
            # elif abs(global_xoffset-150) >= abs(xoffset_max) and abs(global_xoffset) < abs(xoffset_max):
            #     action SetVariable('global_xoffset', xoffset_max*-1)
            # else:
            if tmp_xpos != f_xpos:
                action [SetVariable('global_xoffset', global_xoffset-90),
                    Hide('chaMoveCon'),
                    Show('chaMoveCon', cha='m_walk_fast_sing')]
            else:
                action [SetVariable('global_xoffset', global_xoffset-90),
                    Hide('chaMoveCon'), Hide('f_con'),
                    Show('chaMoveCon', cha='m_walk_fast_sing'),
                    Show('f_con')]

        imagebutton:
            keysym 'K_SPACE'
            xalign 0.95 yalign 0.8
            auto 'inter_%s'
            if renpy.get_screen('game_map_street_2') and abs(global_xoffset)==400:
                action SetVariable('interact', interact+1)
            elif renpy.get_screen('game_map_street_2') and persistent.street_achieve == 0 and abs(global_xoffset) >= 1120 and abs(global_xoffset) <= 1390:
                # Play('sound', 'sound/en.m4a'), 
                action SetVariable('persistent.street_achieve', persistent.street_achieve+1)
            elif (renpy.get_screen('game_map_cn_1') and global_xoffset!=0 and
                    ((abs(global_xoffset)>=20 and abs(global_xoffset)<40) or 
                    (abs(global_xoffset)>=100 and abs(global_xoffset)<120) or 
                    (abs(global_xoffset)>=380 and abs(global_xoffset)<400) or
                    (abs(global_xoffset)>=560 and abs(global_xoffset)<600) or
                    (abs(global_xoffset)>=660 and abs(global_xoffset)<680) or
                    (abs(global_xoffset)>=800 and abs(global_xoffset)<860) or
                    (abs(global_xoffset)>=1140 and abs(global_xoffset)<1180) or
                    (abs(global_xoffset)>=1420 and abs(global_xoffset)<1460) or
                    (abs(global_xoffset)>=2590 and abs(global_xoffset)<2630) or
                    (abs(global_xoffset)>=2950 and abs(global_xoffset)<2990) or
                    (abs(global_xoffset)>=3440 and abs(global_xoffset)<3470) or
                    (abs(global_xoffset)>=3550 and abs(global_xoffset)<3570) or
                    (abs(global_xoffset)>=3670 and abs(global_xoffset)<3690) or
                    (abs(global_xoffset)>=3750 and abs(global_xoffset)<3790) or
                    (abs(global_xoffset)>=4070 and abs(global_xoffset)<4110) or
                    (abs(global_xoffset)>=4290 and abs(global_xoffset)<4330) or
                    (abs(global_xoffset)>=4410 and abs(global_xoffset)<4450))
                    ):
                if not m_hide:
                    action [SetVariable('m_hide', True), Hide('chaMoveCon'),
                            Show('chaMoveCon', cha='m_h')]
                    if persistent.f_ht_times>0:
                        action [SetVariable('m_hide', True), Hide('chaMoveCon'),
                                Show('chaMoveCon', cha='m_h'), SetVariable('persistent.f_ht_times', persistent.f_ht_times-1)]
                else:
                    action [SetVariable('m_hide', False), Hide('chaMoveCon'),
                            Show('chaMoveCon', cha='m_s')]
            elif (renpy.get_screen('game_map_cn_1') and global_xoffset!=0 and
                    ((abs(global_xoffset)>=2310 and abs(global_xoffset)<2890)) ):
                action SetVariable('persistent.cn_cat_inter', True) 
            elif (renpy.get_screen('game_map_shop_1') and global_xoffset!=0 and
                    ((abs(global_xoffset)>=10 and abs(global_xoffset)<=90) or
                    (abs(global_xoffset)>=340 and abs(global_xoffset)<=420) or
                    (abs(global_xoffset)>=720 and abs(global_xoffset)<=800) or
                    (abs(global_xoffset)>=1060 and abs(global_xoffset)<=1140) or
                    (abs(global_xoffset)>=2150 and abs(global_xoffset)<=2230) )
                    ):
                if not m_hide:
                    action [SetVariable('m_hide', True), Hide('chaMoveCon'),
                            Show('chaMoveCon', cha='m_h')]
                    if persistent.f_ht_times>0:
                        action [SetVariable('m_hide', True), Hide('chaMoveCon'),
                                Show('chaMoveCon', cha='m_h'), SetVariable('persistent.f_ht_times', persistent.f_ht_times-1)]
                else:
                    action [SetVariable('m_hide', False), Hide('chaMoveCon'),
                            Show('chaMoveCon', cha='m_s')]
            elif (renpy.get_screen('game_map_home_1') and global_xoffset!=0 and
                    (abs(global_xoffset)>=3240 and abs(global_xoffset)<=3420)):
                if not trash_1_solv:
                    action [SetVariable('persistent.trash_counts', persistent.trash_counts+1),
                            SetVariable('trash_1_solv', True)]
            elif (renpy.get_screen('game_map_home_1') and global_xoffset!=0 and
                    (abs(global_xoffset)>=2250 and abs(global_xoffset)<=2430)):
                if not trash_2_solv:
                    action [SetVariable('persistent.trash_counts', persistent.trash_counts+1),
                            SetVariable('trash_2_solv', True)]
            elif (renpy.get_screen('game_map_home_1') and global_xoffset!=0 and
                    (abs(global_xoffset)>=270 and abs(global_xoffset)<=450)):
                if not trash_3_solv:
                    action [SetVariable('persistent.trash_counts', persistent.trash_counts+1),
                            SetVariable('trash_3_solv', True)]
            else:
                action NullAction()

        # pad
        imagebutton:
            keysym 'pad_y_press'
            xalign 0.95 yalign 0.2
            auto 'sarr_%s'
            # if abs(global_xoffset-10) > abs(xoffset_max):
            #     action NullAction()
            # elif abs(global_xoffset-10) >= abs(xoffset_max) and abs(global_xoffset) < abs(xoffset_max):
            #     action SetVariable('global_xoffset', xoffset_max*-1)
            # else:
            if tmp_xpos != f_xpos:
                action [SetVariable('global_xoffset', global_xoffset-20),
                    Hide('chaMoveCon'),
                    Show('chaMoveCon', cha='m_walk_slow_sing')]
            else:
                action [SetVariable('global_xoffset', global_xoffset-20),
                        Hide('chaMoveCon'), Hide('f_con'),
                        Show('chaMoveCon', cha='m_walk_slow_sing'),
                        Show('f_con')]

        imagebutton:
            keysym 'pad_a_press'
            xalign 0.95 yalign 0.5
            auto 'farr_%s'
            # if abs(global_xoffset-150) > abs(xoffset_max):
            #     action NullAction()
            # elif abs(global_xoffset-150) >= abs(xoffset_max) and abs(global_xoffset) < abs(xoffset_max):
            #     action SetVariable('global_xoffset', xoffset_max*-1)
            # else:
            if tmp_xpos != f_xpos:
                action [SetVariable('global_xoffset', global_xoffset-90),
                    Hide('chaMoveCon'),
                    Show('chaMoveCon', cha='m_walk_fast_sing')]
            else:
                action [SetVariable('global_xoffset', global_xoffset-90),
                    Hide('chaMoveCon'), Hide('f_con'),
                    Show('chaMoveCon', cha='m_walk_fast_sing'),
                    Show('f_con')]

        imagebutton:
            keysym 'pad_b_press'
            xalign 0.95 yalign 0.8
            auto 'inter_%s'
            if renpy.get_screen('game_map_street_2') and abs(global_xoffset)==400:
                action SetVariable('interact', interact+1)
            elif renpy.get_screen('game_map_street_2') and persistent.street_achieve == 0 and abs(global_xoffset) >= 1120 and abs(global_xoffset) <= 1390:
                action SetVariable('persistent.street_achieve', persistent.street_achieve+1)
            elif (renpy.get_screen('game_map_cn_1') and global_xoffset!=0 and
                    ((abs(global_xoffset)>=20 and abs(global_xoffset)<40) or 
                    (abs(global_xoffset)>=100 and abs(global_xoffset)<120) or 
                    (abs(global_xoffset)>=380 and abs(global_xoffset)<400) or
                    (abs(global_xoffset)>=560 and abs(global_xoffset)<600) or
                    (abs(global_xoffset)>=660 and abs(global_xoffset)<680) or
                    (abs(global_xoffset)>=800 and abs(global_xoffset)<860) or
                    (abs(global_xoffset)>=1140 and abs(global_xoffset)<1180) or
                    (abs(global_xoffset)>=1420 and abs(global_xoffset)<1460) or
                    (abs(global_xoffset)>=2590 and abs(global_xoffset)<2630) or
                    (abs(global_xoffset)>=2950 and abs(global_xoffset)<2990) or
                    (abs(global_xoffset)>=3440 and abs(global_xoffset)<3470) or
                    (abs(global_xoffset)>=3550 and abs(global_xoffset)<3570) or
                    (abs(global_xoffset)>=3670 and abs(global_xoffset)<3690) or
                    (abs(global_xoffset)>=3750 and abs(global_xoffset)<3790) or
                    (abs(global_xoffset)>=4070 and abs(global_xoffset)<4110) or
                    (abs(global_xoffset)>=4290 and abs(global_xoffset)<4330) or
                    (abs(global_xoffset)>=4410 and abs(global_xoffset)<4450))
                    ):
                if not m_hide:
                    action [SetVariable('m_hide', True), Hide('chaMoveCon'),
                            Show('chaMoveCon', cha='m_h')]
                    if persistent.f_ht_times>0:
                        action [SetVariable('m_hide', True), Hide('chaMoveCon'),
                                Show('chaMoveCon', cha='m_h'), SetVariable('persistent.f_ht_times', persistent.f_ht_times-1)]
                else:
                    action [SetVariable('m_hide', False), Hide('chaMoveCon'),
                            Show('chaMoveCon', cha='m_s')]
            elif (renpy.get_screen('game_map_cn_1') and global_xoffset!=0 and
                    ((abs(global_xoffset)>=2310 and abs(global_xoffset)<2890)) ):
                action SetVariable('persistent.cn_cat_inter', True) 
            elif (renpy.get_screen('game_map_shop_1') and global_xoffset!=0 and
                    ((abs(global_xoffset)>=10 and abs(global_xoffset)<=90) or
                    (abs(global_xoffset)>=340 and abs(global_xoffset)<=420) or
                    (abs(global_xoffset)>=720 and abs(global_xoffset)<=800) or
                    (abs(global_xoffset)>=1060 and abs(global_xoffset)<=1140) or
                    (abs(global_xoffset)>=2150 and abs(global_xoffset)<=2230) )
                    ):
                if not m_hide:
                    action [SetVariable('m_hide', True), Hide('chaMoveCon'),
                            Show('chaMoveCon', cha='m_h')]
                    if persistent.f_ht_times>0:
                        action [SetVariable('m_hide', True), Hide('chaMoveCon'),
                                Show('chaMoveCon', cha='m_h'), SetVariable('persistent.f_ht_times', persistent.f_ht_times-1)]
                else:
                    action [SetVariable('m_hide', False), Hide('chaMoveCon'),
                            Show('chaMoveCon', cha='m_s')]
            elif (renpy.get_screen('game_map_home_1') and global_xoffset!=0 and
                    (abs(global_xoffset)>=3240 and abs(global_xoffset)<=3420)):
                if not trash_1_solv:
                    action [SetVariable('persistent.trash_counts', persistent.trash_counts+1),
                            SetVariable('trash_1_solv', True)]
            elif (renpy.get_screen('game_map_home_1') and global_xoffset!=0 and
                    (abs(global_xoffset)>=2250 and abs(global_xoffset)<=2430)):
                if not trash_2_solv:
                    action [SetVariable('persistent.trash_counts', persistent.trash_counts+1),
                            SetVariable('trash_2_solv', True)]
            elif (renpy.get_screen('game_map_home_1') and global_xoffset!=0 and
                    (abs(global_xoffset)>=270 and abs(global_xoffset)<=450)):
                if not trash_3_solv:
                    action [SetVariable('persistent.trash_counts', persistent.trash_counts+1),
                            SetVariable('trash_3_solv', True)]
            else:
                action NullAction()