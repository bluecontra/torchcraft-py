import re


def print_err(msg):
    raise RuntimeError(msg)


def is_empty(data):
    return data is not None and len(data) == 0


def to_str(*args):
    s = ""
    for a in args:
        if type(a) == float and a == int(a):
            r = str(int(a))
        else:
            r = str(a)
        s += r

    return s


def get_bool(b):
    if b == 'true' or b == 'TRUE' or b == 'True' or b == '1':
        return True
    else:
        return False


def get_int(args, c):
    if type(args) != list:
        print 'Error'
        return -1

    i = int(args[c])
    c += 1
    return i, c


def get_float(args, c):
    if type(args) != list:
        raise RuntimeError("Error args type" + type(args) + ", should be list.")

    i = float(args[c])
    c += 1
    return i, c


def parse_table(s):
    result = {}
    if len(s) < 2:
        return result

    s = s[1:-1]
    kvs = re.split(r',(?=[a-zA-Z])',s)
    for kv in kvs:
        if len(kv) == 0:
            continue
        pair = kv.split('=')
        if len(pair) != 2:
            continue
        result[pair[0].strip()] = pair[1].strip()
    return result


def parse_list(s):
    result = []
    if len(s) < 2:
        return result

    s = s[1:-1]
    values = s.split(',')
    for v in values:
        v = v.strip()
        if len(v) > 0:
            result.append(v)
    return result


def get_weakest(units_table):
    min_total_hp = 1E30
    weakest_uid = -1
    for uid, ut in units_table.iteritems():
        if ut is None:
            continue
        tmp_hp = ut.health + ut.shield
        if tmp_hp < min_total_hp:
            min_total_hp = tmp_hp
            weakest_uid = uid
    return weakest_uid

''' 
def get_closest(units_table, my_x, my_y):
    min_distance = 1E30
    closest_uid = -1
    for uid, ut in units_table.iteritems():
        if ut is None:
            continue
        tmp_dis = (ut.x - my_x) * (ut.x - my_x) + (ut.y - my_y) * (ut.y - my_y)
        if tmp_dis < min_distance:
            min_distance = tmp_dis
            closest_uid = uid
    return closest_uid
'''
    
def progress(nloop, battles_won, battles_game, total_battles):
    print "Loop: %5d | WinRate: %1.3f | #Wins: %4d | #Battles: %4d | #TotalBattles: %4d" % (
        nloop, battles_won / (battles_game + 1E-6), battles_won, battles_game,
        total_battles)

'''
def printClientState(client, 
    p_map_name=True, 
    p_player_id=True, 
    p_units_myself=True, 
    p_units_enemy=True,
    p_battle_won=False,
    p_waiting_for_restart=False,
    p_battle_just_ended=False,
    p_battle_frame_count=True,
    p_lag_frames=True):
    
    if p_map_name == True:
        print "map_name: " + client.state.d['map_name']
    if p_player_id == True:
        print "player_id: " + client.state.d['player_id']
    if p_battle_frame_count == True:
        print "battle_frame_count: " + client.state.d['battle_frame_count']
    if p_lag_frames == True:
        print "lag_frames: " + client.state.d['lag_frames']

    if p_units_myself == True:
        print "units_myself: "
        for k,v in client.state.d['units_myself'].items():
            # print str(k) + ' --> '
            printUnitMainInfo(v)

    if p_units_enemy == True:
        print "units_enemy: "
        for k,v in client.state.d['units_enemy'].items():
            # print str(k) + ' --> '
            printUnitMainInfo(v)

    if p_battle_won == True:
        print "battle_won: " + client.state.d['battle_won']
    if p_waiting_for_restart == True:
        print "waiting_for_restart: " + client.state.d['waiting_for_restart']
    if p_battle_just_ended == True:
        print "battle_just_ended: " + client.state.d['battle_just_ended']

def printUnitMainInfo(unit, p_cd=False, p_secInfo=False):
    s = ''
    s += to_str('uid: ' ,unit.id, ', ', 'type: ', unit.type, ', ')

    if p_secInfo == True:
        s += to_str('armor: ', unit.armor, ', ', 'shieldArmor: ', unit.shieldArmor, ', '
        , 'groundATK: ', unit.groundATK, ', '
        , 'airATK: ', unit.airATK, ', '
        , 'groundDmgType: ', unit.groundDmgType, ', '
        , 'airDmgType: ', unit.airDmgType, ', '
        , 'groundRange: ', unit.groundRange, ', '
        , 'airRange: ', unit.airRange, ', '
        , '(pixel_size_x,pixel_size_y): ', '(', unit.pixel_size_x, ',', unit.pixel_size_y, ')', ', ')
    
    s += to_str('health: ', unit.health, '/', unit.max_health, ', '
    , 'shield: ', unit.shield, '/', unit.max_shield, ', '
    , 'energy: ', unit.energy, ', ')

    s += to_str('(x,y): ', '(', unit.x, ',', unit.y, ')', ', ' 
    , '(pixel_x,pixel_y): ', '(', unit.pixel_x, ',', unit.pixel_y, ')', ', ' 
    , '(v_x,v_y): ', '(', unit.velocityX, ',', unit.velocityY, ')', ', ')

    if p_cd == True:
        s += to_str('maxCD: ', unit.maxCD, ','
        , 'groundCD: ', unit.groundCD, ','
        , 'airCD: ', unit.airCD, ','
        , 'energy: ', unit.energy, ','
        , 'energy: ', unit.energy, ',')

    print s

'''
