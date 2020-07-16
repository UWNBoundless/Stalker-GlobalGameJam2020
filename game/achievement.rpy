################################################################################
## 初始化
################################################################################

init offset = -1

################################################################################
## Achievement
################################################################################

define achievement.steam_position = "bottom right"

label achieve:
    $ achievement.Sync()

    # 卡成成就
    $ achievement.register('TruckDead_0_0', steam='ACHIEVEMENT_TruckDead_0_0')
    if not achievement.has('TruckDead_0_0') and persistent.dead_times >= 1:
        $ achievement.grant('TruckDead_0_0')

    $ achievement.register('TruckDead_0_1', steam='ACHIEVEMENT_TruckDead_0_1')
    if not achievement.has('TruckDead_0_1') and persistent.dead_times >= 5:
        $ achievement.grant('TruckDead_0_1')

    $ achievement.register('TruckDead_0_2', steam='ACHIEVEMENT_TruckDead_0_2')
    if not achievement.has('TruckDead_0_2') and persistent.dead_times >= 10:
        $ achievement.grant('TruckDead_0_2')

    $ achievement.register('TruckDead_0_3', steam='ACHIEVEMENT_TruckDead_0_3')
    if not achievement.has('TruckDead_0_3') and persistent.dead_times >= 20:
        $ achievement.grant('TruckDead_0_3')

    $ achievement.register('TruckDead_0_4', steam='ACHIEVEMENT_TruckDead_0_4')
    if not achievement.has('TruckDead_0_4') and persistent.dead_times >= 30:
        $ achievement.grant('TruckDead_0_4')
    
    return