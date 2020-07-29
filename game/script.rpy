label start:

    jump startr

label startr:

    $ persistent.val = 95

    $ persistent.trash_counts = 0
    $ persistent.cn_cat_inter = 0
    $ persistent.f_ht_times = 0
    $ persistent.street_achieve = 0
    

    play music 'sound/norm.mp3'

    $ global_xoffset = 0

    call screen game_map_street_1 with Dissolve(2.0)

    jump s1

label s1:

    $ f_xpos = 1720
    $ tmp_xpos = 1720

    $ global_xoffset = -400

    call screen game_map_street_2

    $ tmp = _return

    if tmp == 'BE1':
        jump be1
    if tmp == 'BE2':
        jump be2
    if tmp == 'E1':
        jump e1
    
    jump s2

label s2:

    $ f_xpos = 1560
    $ tmp_xpos = 1560

    $ global_xoffset = 0

    call screen game_map_cn_1 with Dissolve(3.0)

    $ tmp = _return

    if tmp == 'BE1':
        jump be1
    if tmp == 'BE2':
        jump be2
    if tmp == 'E1':
        jump e1

    jump s3

label s3:

    $ f_xpos = 800
    $ tmp_xpos = 800

    $ global_xoffset = 0

    call screen game_map_shop_1 with Dissolve(3.0)

    $ tmp = _return

    if tmp == 'BE1':
        jump be1
    if tmp == 'BE2':
        jump be2
    if tmp == 'E1':
        jump e1

    jump s4

label s4:

    $ f_xpos = 760
    $ tmp_xpos = 760

    $ global_xoffset = 0
 
    call screen game_map_home_1 with Dissolve(3.0)

    $ tmp = _return

    if tmp == 'BE1':
        jump be1
    if tmp == 'BE2':
        jump be2

    if persistent.street_achieve != 0 and persistent.f_ht_times > persistent.trash_counts:
        jump ne1
    elif persistent.cn_cat_inter and persistent.f_ht_times < persistent.trash_counts:
        jump ne2
    elif persistent.street_achieve != 0 and persistent.f_ht_times < persistent.trash_counts:
        jump ne4
    elif persistent.cn_cat_inter and persistent.f_ht_times > persistent.trash_counts:
        jump ne5
    else:
        jump ne3


######################################
# ending
label ne1:
    
    $ persistent.trash_achievements += persistent.trash_counts
    $ persistent.street_achievements += 1

    scene image '/cg/e1.jpg' with Dissolve(1.0)
    pause

    jump achieve

label ne2:
    
    $ persistent.trash_achievements += persistent.trash_counts
    $ persistent.cat_achievements += 1

    scene image '/cg/e2.png' with Dissolve(1.0)
    pause

    jump achieve

label ne3:
    $ persistent.trash_achievements += persistent.trash_counts
    scene image '/cg/e3.jpg' with Dissolve(1.0)
    pause

    jump achieve

label ne4:
    
    $ persistent.trash_achievements += persistent.trash_counts
    $ persistent.street_achievements += 1
    
    scene image '/cg/e4.jpg' with Dissolve(1.0)
    pause

    jump achieve

label ne5:
    
    $ persistent.trash_achievements += persistent.trash_counts
    $ persistent.cat_achievements += 1

    scene image '/cg/e5.jpg' with Dissolve(1.0)
    pause
    return

label e1:

    $ persistent.trash_achievements += persistent.trash_counts
    $ persistent.nothing_achievements += 1

    scene image '/cg/cg_none_1.jpg' with Dissolve(0.5)
    pause 0.5
    scene image '/cg/cg_none_2.jpg' with Dissolve(0.3)
    pause 0.2
    scene image '/cg/cg_none_3.jpg' with Dissolve(0.5)
    pause 0.7
    scene image '/cg/cg_none_4.jpg' with Dissolve(0.5)
    pause

    jump achieve

label be1:

    $ persistent.trash_achievements += persistent.trash_counts
    $ persistent.caught_achievements += 1

    scene image '/cg/cg_caught_1.jpg' with Dissolve(2.0)
    pause 1.5
    scene image '/cg/cg_caught_2.jpg' with Dissolve(2.0)
    pause

    jump achieve

label be2:

    play music 'sound/car.mp3'

    $ persistent.trash_achievements += persistent.trash_counts
    $ persistent.dead_times += 1

    scene image '/cg/cg_die1.jpg' with Dissolve(2.0)
    stop music
    pause

    jump achieve