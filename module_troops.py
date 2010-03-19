import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below...

def wp(x):
  n = 0
  r = 10 + int(x / 10)
  n |= wp_one_handed(x + random.randrange(r))
  n |= wp_two_handed(x + random.randrange(r))
  n |= wp_polearm(x + random.randrange(r))
  #n |= wp_archery(x + random.randrange(r))
  n |= wp_crossbow(x + random.randrange(r))
  n |= wp_throwing(x + random.randrange(r))
  #SW - add firearm
  n |= wp_firearm(x + random.randrange(r))
  return n

def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
  n |= wp_one_handed(x + random.randrange(r))
  n |= wp_two_handed(x + random.randrange(r))
  n |= wp_polearm(x + random.randrange(r))
  return n

#Skills
#SW - modified knows_common
#knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_tactics_1|knows_shield_1
knows_common_2 = knows_riding_2|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_2|knows_ironflesh_2|knows_power_strike_2|knows_athletics_2|knows_tactics_1|knows_shield_2
knows_common_3 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_3|knows_ironflesh_3|knows_power_strike_3|knows_athletics_3|knows_tactics_2|knows_shield_3
knows_common_4 = knows_riding_4|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_4|knows_ironflesh_4|knows_power_strike_4|knows_athletics_4|knows_tactics_2|knows_shield_4

knows_arena_1 = knows_riding_2|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_3|knows_ironflesh_2|knows_power_strike_1|knows_athletics_1|knows_tactics_1|knows_shield_2|knows_power_draw_6|knows_power_throw_5|knows_weapon_master_4
knows_arena_2 = knows_riding_2|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_4|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_tactics_3|knows_shield_3|knows_power_draw_6|knows_power_throw_5|knows_weapon_master_5
knows_arena_3 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_5|knows_ironflesh_6|knows_power_strike_5|knows_athletics_5|knows_tactics_5|knows_shield_4|knows_power_draw_6|knows_power_throw_6|knows_weapon_master_6
knows_arena_4 = knows_riding_4|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_6|knows_ironflesh_8|knows_power_strike_6|knows_athletics_7|knows_tactics_7|knows_shield_5|knows_power_draw_6|knows_power_throw_6|knows_weapon_master_6

def_attrib = str_10 | agi_8 | int_6 | cha_6
def_attrib_1 = str_12 | agi_10 | int_8 | cha_8
def_attrib_2 = str_14 | agi_12 | int_10 | cha_10
def_attrib_3 = str_16 | agi_14 | int_12 | cha_12
def_attrib_4 = str_18 | agi_16 | int_14 | cha_14

def_attrib_force_1 = str_24 | agi_18 | int_10 | cha_10
def_attrib_force_2 = str_26 | agi_22 | int_14 | cha_14
def_attrib_force_3 = str_28 | agi_26 | int_18 | cha_18
def_attrib_force_4 = str_30 | agi_30 | int_22 | cha_22

knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_horse_archery_3|knows_athletics_3|knows_weapon_master_2|knows_ironflesh_1|knows_power_strike_2|knows_riding_3|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_horse_archery_3|knows_athletics_3|knows_riding_3|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_horse_archery_3|knows_riding_3|knows_weapon_master_1|knows_athletics_3|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_30|agi_25|int_25|cha_25|level(50)

knight_attrib_1 = str_22|agi_18|int_8|cha_16|level(25)
knight_attrib_2 = str_24|agi_20|int_10|cha_18|level(30)
knight_attrib_3 = str_26|agi_22|int_12|cha_20|level(35)
knight_attrib_4 = str_28|agi_24|int_13|cha_22|level(40)
knight_attrib_5 = str_30|agi_26|int_20|cha_20|level(45)

# knight_skills_1 = knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3|knows_shield_3
# knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5|knows_shield_4
# knight_skills_3 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6|knows_shield_5
# knight_skills_4 = knows_riding_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7|knows_shield_6
# knight_skills_5 = knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9|knows_shield_7

#SW - modified knight skills for star wars knights
starwars_knight_skills_1 = knows_riding_4|knows_ironflesh_8|knows_power_strike_6|knows_athletics_6|knows_tactics_6|knows_prisoner_management_5|knows_leadership_5|knows_power_throw_6|knows_weapon_master_6|knows_shield_6|knows_horse_archery_4|knows_trainer_4
starwars_knight_skills_2 = knows_riding_5|knows_ironflesh_9|knows_power_strike_7|knows_athletics_7|knows_tactics_7|knows_prisoner_management_6|knows_leadership_6|knows_power_throw_7|knows_weapon_master_7|knows_shield_7|knows_horse_archery_5|knows_trainer_5
starwars_knight_skills_3 = knows_riding_6|knows_ironflesh_10|knows_power_strike_8|knows_athletics_8|knows_tactics_8|knows_prisoner_management_7|knows_leadership_7|knows_power_throw_8|knows_weapon_master_8|knows_shield_8|knows_horse_archery_6|knows_trainer_6
starwars_knight_skills_4 = knows_riding_7|knows_ironflesh_10|knows_power_strike_9|knows_athletics_9|knows_tactics_9|knows_prisoner_management_8|knows_leadership_8|knows_power_throw_9|knows_weapon_master_9|knows_shield_9|knows_horse_archery_7|knows_trainer_7
starwars_knight_skills_5 = knows_riding_8|knows_ironflesh_10|knows_power_strike_10|knows_athletics_10|knows_tactics_10|knows_prisoner_management_9|knows_leadership_9|knows_power_throw_10|knows_weapon_master_10|knows_shield_10|knows_horse_archery_8|knows_trainer_8

#SW - added default skills for troops
starwars_skills_1 = knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_weapon_master_4|knows_shield_2|knows_athletics_3|knows_tactics_3|knows_leadership_3|knows_trainer_1
starwars_skills_2 = knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_weapon_master_5|knows_shield_3|knows_athletics_4|knows_tactics_3|knows_leadership_3|knows_trainer_1
starwars_skills_3 = knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_tactics_4|knows_leadership_4|knows_trainer_2
starwars_skills_4 = knows_ironflesh_6|knows_power_strike_6|knows_power_throw_5|knows_weapon_master_6|knows_shield_5|knows_athletics_6|knows_tactics_4|knows_leadership_4|knows_trainer_2

starwars_skills_melee_1 = knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_4|knows_shield_5|knows_athletics_5|knows_tactics_4|knows_leadership_4|knows_trainer_2
starwars_skills_melee_2 = knows_ironflesh_6|knows_power_strike_6|knows_power_throw_5|knows_weapon_master_5|knows_shield_6|knows_athletics_6|knows_tactics_4|knows_leadership_4|knows_trainer_2
starwars_skills_melee_3 = knows_ironflesh_7|knows_power_strike_7|knows_power_throw_6|knows_weapon_master_6|knows_shield_7|knows_athletics_7|knows_tactics_5|knows_leadership_5|knows_trainer_3
starwars_skills_melee_4 = knows_ironflesh_8|knows_power_strike_8|knows_power_throw_7|knows_weapon_master_7|knows_shield_8|knows_athletics_8|knows_tactics_5|knows_leadership_5|knows_trainer_3

starwars_skills_mounted_1 = knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_weapon_master_4|knows_shield_2|knows_athletics_3|knows_riding_4|knows_horse_archery_4|knows_tactics_3|knows_leadership_3|knows_trainer_1
starwars_skills_mounted_2 = knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_weapon_master_5|knows_shield_3|knows_athletics_4|knows_riding_5|knows_horse_archery_5|knows_tactics_3|knows_leadership_3|knows_trainer_1
starwars_skills_mounted_3 = knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_5|knows_shield_4|knows_athletics_5|knows_riding_6|knows_horse_archery_6|knows_tactics_4|knows_leadership_4|knows_trainer_2
starwars_skills_mounted_4 = knows_ironflesh_6|knows_power_strike_6|knows_power_throw_5|knows_weapon_master_6|knows_shield_5|knows_athletics_6|knows_riding_8|knows_horse_archery_8|knows_tactics_4|knows_leadership_4|knows_trainer_2

starwars_skills_force_1 = knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_weapon_master_4|knows_shield_4|knows_athletics_7|knows_riding_3|knows_horse_archery_4|knows_tactics_4|knows_leadership_4|knows_trainer_2|knows_power_draw_4
starwars_skills_force_2 = knows_ironflesh_8|knows_power_strike_8|knows_power_throw_6|knows_weapon_master_5|knows_shield_5|knows_athletics_8|knows_riding_4|knows_horse_archery_4|knows_tactics_5|knows_leadership_5|knows_trainer_2|knows_power_draw_6
starwars_skills_force_3 = knows_ironflesh_9|knows_power_strike_9|knows_power_throw_7|knows_weapon_master_6|knows_shield_6|knows_athletics_9|knows_riding_5|knows_horse_archery_5|knows_tactics_6|knows_leadership_6|knows_trainer_3|knows_power_draw_8
starwars_skills_force_4 = knows_ironflesh_10|knows_power_strike_10|knows_power_throw_8|knows_weapon_master_7|knows_shield_7|knows_athletics_10|knows_riding_6|knows_horse_archery_5|knows_tactics_7|knows_leadership_7|knows_trainer_3|knows_power_draw_10

#droid attributes
droid_attrib_1 = str_3|int_8|cha_3 	# zero agility (so they move slow)
droid_attrib_2 = str_3|int_16|cha_3	# zero agility (so they move slow)

#droid skills
droid_skills_1 = knows_ironflesh_4|knows_tactics_2|knows_leadership_2|knows_trainer_2
droid_skills_2 = knows_ironflesh_6|knows_tactics_4|knows_leadership_4|knows_trainer_4

# give outlaws lower riding skills so their ships move slower on the world map
starwars_skills_outlaws_1 = knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_weapon_master_3|knows_shield_2|knows_athletics_3|knows_riding_2|knows_horse_archery_3|knows_tactics_3|knows_leadership_3|knows_trainer_1
starwars_skills_outlaws_2 = knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_weapon_master_4|knows_shield_3|knows_athletics_4|knows_riding_2|knows_horse_archery_3|knows_tactics_3|knows_leadership_3|knows_trainer_1
starwars_skills_outlaws_3 = knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_weapon_master_4|knows_shield_4|knows_athletics_5|knows_riding_3|knows_horse_archery_4|knows_tactics_4|knows_leadership_4|knows_trainer_2
starwars_skills_outlaws_4 = knows_ironflesh_6|knows_power_strike_6|knows_power_throw_5|knows_weapon_master_5|knows_shield_5|knows_athletics_6|knows_riding_3|knows_horse_archery_4|knows_tactics_4|knows_leadership_4|knows_trainer_2

# default npc skills/attrib
starwars_npc_skills = knows_ironflesh_2|knows_power_strike_1|knows_power_throw_1|knows_weapon_master_5|knows_shield_1|knows_athletics_2|knows_riding_2|knows_horse_archery_2|knows_tactics_1|knows_leadership_1|knows_trainer_1
starwars_npc_attrib = str_10 | agi_10 | int_8 | cha_8

# SW (HC) - Guarantee constants
tf_guarantee_all_armor = tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_boots

#sw_npc_jedi = sw_npc_basic|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_weapon_master_4|knows_shield_4|knows_athletics_4|knows_riding_4|knows_horse_archery_4|knows_tactics_4|knows_leadership_4
#sw_npc_warrior = sw_npc_basic|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_weapon_master_3|knows_shield_2|knows_athletics_3|knows_riding_3|knows_horse_archery_4|knows_tactics_2|knows_leadership_2
#sw_npc_tracker = sw_npc_basic|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_weapon_master_3|knows_shield_2|knows_athletics_3|knows_riding_3|knows_horse_archery_4|knows_tactics_2|knows_leadership_2
#sw_npc_merchant

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

#SW - face codes
sw_player_face = 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000		#original code from native
#sw_player_face = 	# NEW
sw_woman_face_1    = 0x0000000000000001249249480029249200000000001d24920000000000000000
sw_woman_face_2    = 0x0000000cff00700849246e480092492400000000001e49240000000000000000
sw_slave_dancer_face1 = 0x0000000000000001249249249249249200000000001d24920000000000000000
sw_slave_dancer_face2 = 0x000000003f0060085b65b6b6dbb6db6d00000000001e49240000000000000000
sw_man_face_1 = 0x0000000000000001249249249249249200000000001c924b0000000000000000
sw_man_face_2 = 0x0000000fff006287492492491c924b6d00000000001edb230000000000000000
sw_rebel_face_1 = 0x0000000000000001249249249249249200000000001d24930000000000000000
sw_rebel_face_2 = 0x0000000fff006287492492491c924b6d00000000001edb230000000000000000
sw_imperial_face_1 = 0x000000003f000001249249249249249200000000001c924b0000000000000000
sw_imperial_face_2 = 0x0000000fff005005492492491392492400000000001e49230000000000000000
sw_hutt_face_1 = 0x0000000000000001249249249249249200000000001d24930000000000000000
sw_hutt_face_2 = 0x0000000fff01034e492492491c924b6d00000000001edb230000000000000000
sw_bandit_face_1  = sw_hutt_face_1
sw_bandit_face_2  = sw_hutt_face_2
sw_sith_face_1 = 0x0000000000011000249249249249249200000000001d24530000000000000000
sw_sith_face_2 = 0x0000000fff011000492492491c92492400000000001e49230000000000000000
#alien face textures
wookiee_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
wookiee_face2 = 0x0000000fff001000000000000000000000000000000000000000000000000000
mandalorian_face1 = 0x0000000fc0007001249249249249249200000000001d24930000000000000000
mandalorian_face2 = 0x0000000fff00c185492492491c92492400000000001e49230000000000000000
twilek_female_face1 = 0x0000000000000000124924929244949200000000001c92490000000000000000
twilek_female_face2 = 0x0000000d00002000492492491b92492400000000001e49240000000000000000
twilek_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
twilek_face2 = 0x0000000aab003000000000000000000000000000000000000000000000000000
rodian_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
rodian_face2 = 0x0000000fff002000000000000000000000000000000000000000000000000000
chiss_face1 = 0x0000000000014001249249249249249200000000001d24530000000000000000
chiss_face2 = 0x0000000fff014005492492491c92492400000000001e49230000000000000000
chiss_female_face1 = 0x000000000000b001249244c80049249200000000001d24920000000000000000
chiss_female_face2 = 0x0000000cff00b00849246e480092492400000000001e49240000000000000000
weequay_face1 = 0x000000000001500c249249249249249200000000001d24930000000000000000
weequay_face2 = 0x0000000fff01600c492492491c92492400000000001e49230000000000000000
#clone_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
#clone_face2 = 0x0000000fff001000000000000000000000000000000000000000000000000000
bothan_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
bothan_face2 = 0x0000000fff000003000000000000000000000000000000000000000000000000


#single face texture only
trandoshan_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
trandoshan_face2 = 0x0000000fff001000000000000000000000000000000000000000000000000000
gamorrean_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
gamorrean_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
hutt_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
hutt_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
moncal_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
moncal_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
droid_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
droid_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
tusken_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
tusken_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
jawa_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
jawa_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
sullustan_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
sullustan_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000
geonosian_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
geonosian_face2 = 0x0000000000000000000000000000000000000000000000000000000000000000

#NAMES:
#



troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
  #SW BSG integration
  #["player","Player","Player",tf_hero|tf_unmoveable_in_party_window|tf_inactive,no_scene,reserved,fac_player_faction,
   #to release
   [],
   #for testing - don't put too many items or it may crash when starting a new game?
   #[itm_speeder_dagger,itm_dc15a,itm_combat_knife,itm_dc15s,itm_dagger,itm_vibro_blade1,itm_vibro_axe_long_2h,itm_grey_gloves,itm_imperial_stormtrooper_armor,itm_black_gloves,itm_mandalorian_crushgaunts,itm_black_boots,itm_leather_gloves],
   #[itm_droid_parts,itm_shadow_stormtrooper_helmet,itm_shadow_stormtrooper_armor,itm_shadow_stormtrooper_boots,itm_darkgrey_gloves,itm_black_gloves,itm_clone_trooper_boots,itm_clone_trooper_head,itm_combat_knife,itm_clone_trooper_helmet_blue,itm_clone_trooper_helmet_green,itm_clone_trooper_helmet_white,itm_clone_trooper_helmet_red,itm_clone_trooper_armor_blue,itm_clone_trooper_armor_green,itm_clone_trooper_armor_white,itm_clone_trooper_armor_red,itm_dc15a,itm_dc15s],
   #[itm_e11,itm_ig88_attack,itm_ig88_e11_shield,itm_ig88_dlt20a,itm_ig88_head,itm_ig88_body,itm_ig88_hands,itm_ig88_feet,itm_outfit_black,itm_luke_skywalker_outfit,itm_imperial_stormtrooper_armor,itm_right_hand_glove,itm_twilek_dagger_throwing,itm_dlt20a,itm_twilek_dagger,itm_a295,itm_t21,itm_vibro_blade1,itm_vibro_blade2,itm_vibro_blade3,itm_vibro_blade4,itm_imperial_stormtrooper_armor_officer,itm_imperial_stormtrooper_helmet,itm_imperial_stormtrooper_boots,itm_imperial_stormtrooper_gloves,itm_droid_parts,itm_imperial_uniform_black_plain,itm_imperial_trooper_armor,itm_outfit_tan,itm_outfit_grey,itm_outfit_green,itm_black_boots,itm_leather_boots],
   #[itm_laser_bolts_red,itm_laser_bolts_green,itm_dlt20a,itm_wookiee_armor1,itm_wookiee_armor2,itm_gamorrean_armor,itm_geonosian_armor,itm_lightsaber_red_double,itm_tusken_helmet,itm_tusken_armor,itm_transparent_helmet,itm_c3po_head,itm_c3po_hands,itm_c3po_body,itm_c3po_feet,itm_c3po_attack,itm_droid_parts,itm_speeder_imperial,itm_imperial_scout_trooper_armor,itm_imperial_scout_trooper_helmet,itm_imperial_scout_trooper_boots,itm_black_gloves_long,itm_laser_bolts_red,itm_scout_trooper_pistol],
   #[itm_b1series_body,itm_b1series_attack,itm_3poseries_gold,itm_3poseries_attack,itm_dc15s,itm_laser_bolts_orange,itm_a280],
   #[itm_dlt19,itm_lightsaber_blue_double,itm_lightsaber_red_double,itm_lightsaber_green,itm_imperial_stormtrooper_armor,itm_black_gloves,itm_imperial_stormtrooper_boots,itm_imperial_stormtrooper_helmet,itm_speeder_shadow,itm_shadow_scout_trooper_boots,itm_black_gloves_long,itm_shadow_scout_trooper_helmet,itm_shadow_scout_trooper_armor,itm_scout_trooper_pistol],
   #[itm_lightsaber_blue_double,itm_thermal_detonator1,itm_speeder_fc20,itm_sith_hood,itm_sith_marauder_robe,itm_black_gloves,itm_black_boots,itm_lightsaber_red,itm_lightsaber_block_red,itm_force_throw_lightsaber_red,itm_lightsaber_red_double],
   #[itm_imperial_stormtrooper_helmet,itm_imperial_stormtrooper_armor,itm_imperial_stormtrooper_boots,itm_imperial_stormtrooper_gloves,itm_lightsaber_blue_double,itm_lightsaber_red_double,itm_lightsaber_green_double,itm_lightsaber_yellow_double,itm_lightsaber_purple_double,itm_lightsaber_orange_double],
   #[itm_force_throw_lightsaber_green,itm_force_push,itm_yoda_armor,itm_yoda_lightsaber,itm_yoda_speeder,itm_imperial_uniform_green,itm_black_boots,itm_black_gloves,itm_tarkin_head,itm_lightsaber_red_1h,itm_lightsaber_block_red,itm_jabba_speeder,itm_twilek_female_helmet,itm_transparent_head,itm_transparent_body,itm_transparent_hands,itm_transparent_feet,itm_jabba_armor,itm_jabba_attack],
   #[itm_vibro_knuckler,itm_trandoshan_mask,itm_trandoshan_helmet,itm_trandoshan_armor,itm_lightsaber_red_pike,itm_black_boots,itm_black_gloves,itm_shadow_guard_robe,itm_shadow_guard_helmet,itm_baton,itm_energy_shield_oval,itm_energy_shield_green_small,itm_energy_shield_yellow_small,itm_energy_shield_green_medium,itm_energy_shield_blue_large,itm_a280,itm_a280_stun,itm_medpac_adv,itm_medpac,itm_jedi_master_robe,itm_jedi_master_hood,itm_sith_master_robe,itm_sith_hood,itm_black_boots,itm_force_lightning_ammo,itm_force_push_ammo,itm_force_power_ls_1,itm_force_power_ds_1],
   #[itm_force_knockdown,itm_force_kill,itm_force_stun,itm_dc15a,itm_force_choke,itm_rancor_body_a,itm_rancor_body_b,itm_rancor_body_c,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_rancor_attack],
   #[itm_force_throw_lightsaber_red_double,itm_force_jump,itm_force_throw_lightsaber_green_pike,itm_jetpack,itm_imperial_stormtrooper_helmet,itm_binocular,itm_a280,itm_swoop_bike,itm_e5,itm_e11,itm_senate_rifle,itm_elg3a,itm_se14r,itm_transparent_hands,itm_transparent_head,itm_transparent_feet,itm_lin_droid_armor,itm_lin_droid_armor_w_arm],
   #[itm_lightsaber_green_pike,itm_force_throw_lightsaber_green_pike,itm_jedi_master_robe,itm_lightsaber_green,itm_force_throw_lightsaber_green_merch,itm_slave_neck_chain,itm_horus_winged_cruiser,itm_lightsaber_red_reverse],
   #[itm_grey_gloves_with_bottle,itm_weequay_head_helmet_a,itm_kashyyyk_long_gun,itm_jawa_hood,itm_jawa_robe,itm_leather_gloves,itm_jawa_boots,itm_ion_beam_pistol,itm_ion_pistol],
   #[itm_darth_vader_helmet,itm_imperial_stormtrooper_helmet,itm_shadow_stormtrooper_helmet,itm_imperial_scout_trooper_helmet,itm_shadow_scout_trooper_helmet,itm_fang_helmet,itm_eyepiece_tactics,itm_eyepiece_leadership,itm_defiler_helmet,itm_imperial_gunner_helmet,itm_beak_helmet,itm_black_sun_helmet,itm_imperial_royal_guard_helmet,itm_clone_trooper_helmet_white,itm_mandalorian_crusader_helmet,itm_mandalorian_neocrusader_helmet,itm_trandoshan_mask,itm_imperial_trooper_helmet,itm_glasses_black,itm_glasses_yellow,itm_tusken_helmet,itm_wookiee_hunter_helmet],
   #[itm_droid_parts,itm_b1series_attack,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_b1series_body,itm_dc15s,itm_dc15s,itm_laser_bolts_red_rifle,itm_laser_bolts_red_rifle,itm_horus_winged_cruiser,itm_e5,itm_b2series_body,itm_b2series_blaster,itm_b2series_attack],
   #[itm_wrist_blaster],
		str_6|agi_6|int_6|cha_6,wp_one_handed(30)|wp_two_handed(30)|wp_polearm(30)|wp_crossbow(35)|wp_throwing(30)|wp_firearm(45),0,sw_player_face],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_laser_bolts_red_pistol,itm_dh17],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],
####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tutorial_maceman","Maceman","Maceman",tf_trandoshan|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_durasteel_mace,itm_arena_tunic_white],
   str_6|agi_6|level(1),wp(50),knows_common, trandoshan_face1, trandoshan_face2],
  ["tutorial_archer","Marksman","Marksman",tf_rodian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_dl44a_training,itm_laser_bolts_training_pistol,itm_arena_tunic_green,itm_leather_boots],
   str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4, rodian_face1, rodian_face2],
  ["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_lightsaber_red,itm_arena_tunic_red,itm_black_boots],
   str_6|agi_6|level(5),wp(80),knows_common, sw_sith_face_1, sw_sith_face_2],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_moncal|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_leather_boots],
   str_14|agi_9|level(9),wp(100)|wp_archery(100),knows_arena_1,moncal_face1, moncal_face2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_twilek|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_leather_boots],
   str_14|agi_11|level(14),wp(125)|wp_archery(125),knows_arena_2,twilek_face1, twilek_face2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_trandoshan|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,0,fac_commoners,
   [itm_leather_boots],
   str_14|agi_14|level(19),wp(150)|wp_archery(150),knows_arena_3,trandoshan_face1, trandoshan_face2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_leather_boots],
   str_16|agi_16|level(23),wp(175)|wp_archery(175),knows_arena_4,mandalorian_face1, mandalorian_face2],

  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_leather_boots,itm_arena_tunic_white],
   str_14|agi_9|level(9),wp(100)|wp_archery(100),knows_arena_1,sw_man_face_1, sw_man_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_twilek|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_leather_boots,itm_arena_tunic_white],
   str_14|agi_9|level(9),wp(100)|wp_archery(100),knows_arena_1,twilek_face1, twilek_face2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_weequay|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_leather_boots,itm_arena_tunic_yellow],
   str_14|agi_11|level(14),wp(125)|wp_archery(125),knows_arena_2, weequay_face1, weequay_face2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_sullustan|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_leather_boots,itm_arena_tunic_yellow],
   str_14|agi_11|level(14),wp(125)|wp_archery(125),knows_arena_2,sullustan_face1, sullustan_face2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_moncal|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_leather_boots,itm_arena_tunic_yellow],
   str_14|agi_11|level(14),wp(125)|wp_archery(125),knows_arena_2,moncal_face1, moncal_face2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_chiss|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_leather_boots,itm_arena_tunic_green],
   str_14|agi_14|level(19),wp(150)|wp_archery(150),knows_arena_3,chiss_face1, chiss_face2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_rodian|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_leather_boots,itm_arena_tunic_green],
   str_14|agi_14|level(19),wp(150)|wp_archery(150),knows_arena_3,rodian_face1, rodian_face2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_bothan|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_leather_boots,itm_arena_tunic_green],
   str_14|agi_14|level(19),wp(150)|wp_archery(150),knows_arena_3,bothan_face1, bothan_face2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_trandoshan|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_leather_boots,itm_arena_tunic_red],
   str_16|agi_16|level(23),wp(175)|wp_archery(175),knows_arena_4,trandoshan_face1, trandoshan_face2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_leather_boots,itm_arena_tunic_red],
   str_16|agi_16|level(23),wp(175)|wp_archery(175),knows_arena_4,mandalorian_face1, mandalorian_face2],

   #SW - modified cattle to nerfs and have tf_mounted flag and higher riding skill so they travel faster on the world map
  ["cattle","Nerf","Nerf Herd",tf_mounted,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),knows_common|knows_riding_8,sw_man_face_1, sw_man_face_2],


   #####################################################################################################
   #	add wp_firearm(X) to some troops?
   #SW - added Star Wars mercs

#SW - NOTE - wookiee is the troop marked as soldiers_begin   
   
#wookiee mercs (removed tf_guarantee_ranged from wookiee berserker/bacca so they will be part of the infantry group and can be given separate battle commands)
["wookiee","Wookiee","Wookiees",
	tf_wookiee|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[	itm_wookiee_bowcaster,
		itm_wookiee_bowcaster,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_melee_punch,
		itm_wookiee_shield_small,
		itm_wookiee_shield_small,
		itm_wookiee_fur
	],
	def_attrib_1|level(10),
	wp(100)|wp_firearm(105),
	starwars_skills_1,
	wookiee_face1, wookiee_face2
],
["wookiee_warrior","Wookiee Warrior","Wookiee Warriors",
	tf_wookiee|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[	itm_wookiee_bowcaster,
		itm_wookiee_bowcaster,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_wookiee_armor1,
		itm_wookiee_armor2,
		#itm_ryyk_kerarthorr,
		itm_ryyk_kerarthorr,
		itm_ryyk_kerarthorr_shield,
		itm_ryyk_kerarthorr_shield,		
		itm_wookiee_shield_small,
		itm_wookiee_shield_small,
		itm_wookiee_fur
	],
	def_attrib_2|level(16),
	wp(110)|wp_crossbow(125),
	starwars_skills_2,
	wookiee_face1, wookiee_face2
],
["wookiee_marksman","Wookiee Marksman","Wookiee Marksmen",
	tf_wookiee|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[	itm_vibro_blade1,
		itm_vibro_blade3,
		itm_wookiee_bowcaster,
		itm_wookiee_bowcaster,
		itm_wookiee_armor2,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_wookiee_shield_small,
		itm_wookiee_shield_small,
		itm_transparent_helmet,
		itm_wookiee_fur
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(140),
	starwars_skills_3,
	wookiee_face1, wookiee_face2
],
["wookiee_berserker","Wookiee Berserker","Wookiee Berserkers",
	tf_wookiee|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[	itm_ryyk_blade,
		itm_ryyk_blade,
		itm_ryyk_kerarthorr,
		#itm_ryyk_kerarthorr,
		itm_wookiee_shield_large,
		itm_wookiee_shield_large,
		#itm_ryyk_kerarthorr_shield,
		itm_ryyk_kerarthorr_shield,
		itm_wookiee_armor1,
		itm_westar,
		#itm_westar,
		itm_ddc_defender,
		#itm_ddc_defender,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,
		itm_transparent_helmet,
		itm_wookiee_fur
	],
	def_attrib_3|level(24),
	wp(135)|wp_firearm(140),
	starwars_skills_melee_3,
	wookiee_face1, wookiee_face2
],
["wookiee_sharpshooter","Wookiee Sharpshooter","Wookiee Sharpshooters",
	tf_wookiee|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[	itm_vibro_blade1,
		itm_vibro_blade3,
		itm_wookiee_bowcaster,
		itm_wookiee_bowcaster,
		itm_wookiee_armor2,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_wookiee_shield_small,
		itm_wookiee_shield_small,
		itm_transparent_helmet,
		itm_wookiee_fur
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_4,
	wookiee_face1,wookiee_face2
],
["bacca_warrior","Warrior of Bacca","Warriors of Bacca",
	tf_wookiee|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[	itm_ryyk_blade,
		itm_ryyk_blade,
		itm_ryyk_blade_chieftain,
		itm_ryyk_blade_chieftain,
		itm_wookiee_shield_large,
		itm_wookiee_shield_large,
		itm_ryyk_blade_shield,
		itm_ryyk_blade_shield,
		itm_wookiee_armor1,
		#itm_westar,
		itm_westar,
		#itm_ddc_defender,
		itm_ddc_defender,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,
		itm_transparent_helmet,
		itm_wookiee_fur
	],
	def_attrib_4|level(30),
	wp(150)|wp_firearm(160),
	starwars_skills_melee_4,
	wookiee_face1, wookiee_face2
],
   
# mandalorian mercs - keep tf_guarantee_ranged so they fall into the 'archery' group and can be given separate battle commands
["mandalorian","Mandalorian","Mandalorians",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield,
	no_scene,reserved,fac_commoners,
	[itm_mandalorian_tunic,
		itm_hide_boots,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol,
		itm_ddc_defender,
		itm_ddc_defender,		
		itm_westar,
		itm_westar,
		itm_westar_shield,
		itm_westar_shield,
		itm_energy_shield_red_small,
		itm_energy_shield_yellow_small
	],
	def_attrib_1|level(10),
	wp(100)|wp_firearm(105),
	starwars_skills_1,
	mandalorian_face1, mandalorian_face2
],
["mandalorian_soldier","Mandalorian Soldier","Mandalorian Soldiers",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[   itm_mandalorian_soldier_helmet,
		itm_mandalorian_soldier_helmet,
		itm_mandalorian_soldier_armor,
		itm_mandalorian_soldier_armor,
		itm_mandalorian_soldier_boots,
		itm_mandalorian_soldier_boots,
		itm_grey_gloves,
		itm_grey_gloves,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol,
		itm_westar,
		itm_westar,
		itm_westar_shield,
		itm_westar_shield
	],
	def_attrib_2|level(16),
	wp(110)|wp_firearm(125),
	starwars_skills_2,
	mandalorian_face1, mandalorian_face2
],
["mandalorian_commando","Mandalorian Commando","Mandalorian Commandos",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[   itm_mandalorian_commando_helmet,
		itm_mandalorian_commando_helmet,
		itm_mandalorian_commando_armor,
		itm_mandalorian_commando_armor,
		itm_mandalorian_commando_boots,
		itm_mandalorian_commando_boots,
		itm_grey_gloves,
		itm_grey_gloves,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_a295,
		itm_a295_crouch,
		itm_mandalorian_heavy_blaster,
		itm_mandalorian_heavy_blaster,
		itm_mandalorian_heavy_blaster,
		itm_westar_shield,
		itm_westar_shield
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(140),
	starwars_skills_3,
	mandalorian_face1, mandalorian_face2
],
["mandalorian_sniper","Mandalorian Sniper","Mandalorian Snipers",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[   itm_mandalorian_sniper_helmet,
		itm_mandalorian_sniper_helmet,
		itm_mandalorian_sniper_armor,
		itm_mandalorian_sniper_armor,
		itm_mandalorian_sniper_boots,
		itm_mandalorian_sniper_boots,
		itm_grey_gloves,
		itm_grey_gloves,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_dlt19,
		itm_dlt20a,
		itm_kisteer_1284,
		itm_dlt19_scope,
		itm_westar_shield,
		itm_westar_shield
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(140),
	starwars_skills_3,
	mandalorian_face1, mandalorian_face2
],
["mandalorian_crusader","Mandalorian Crusader","Mandalorian Crusaders",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[   itm_mandalorian_crusader_helmet,
		itm_mandalorian_crusader_helmet,
		itm_mandalorian_neocrusader_helmet,
		#itm_mandalorian_neocrusader_helmet,	#so they are less common
		itm_mandalorian_crusader_armor,
		itm_mandalorian_crusader_armor,
		itm_mandalorian_crusader_boots,
		itm_mandalorian_crusader_boots,
		itm_grey_gloves,
		itm_grey_gloves,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_a295,
		itm_a295_crouch,
		itm_mandalorian_heavy_blaster,
		itm_mandalorian_heavy_blaster,
		itm_mandalorian_heavy_blaster,
		itm_westar_shield,
		itm_westar_shield
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_4,
	mandalorian_face1, mandalorian_face2
],
["mandalorian_deadeye","Mandalorian Deadeye","Mandalorian Deadeyes",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[   itm_mandalorian_deadeye_helmet,
		itm_mandalorian_deadeye_helmet,
		itm_mandalorian_deadeye_armor,
		itm_mandalorian_deadeye_armor,
		itm_mandalorian_deadeye_boots,
		itm_mandalorian_deadeye_boots,
		itm_grey_gloves,
		itm_grey_gloves,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_dlt19,
		itm_dlt20a,
		itm_kisteer_1284,
		itm_dlt19_scope,
		itm_westar_shield,
		itm_westar_shield
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_4,
	mandalorian_face1, mandalorian_face2
],

#gamorrean mercs - used starwars_skills_melee_# so they have better melee fighting ability, thicker skin (ie. higher ironflesh), etc
#                -  removed tf_guarantee_ranged so they fall into the 'infantry' group and can be given separate battle command
["gamorrean","Gamorrean","Gamorreans",
	tf_gamorrean,
	no_scene,reserved,fac_commoners,
	[	
		#itm_gamorrean_armor,
		itm_gamorrean_axe_1h,
		itm_gamorrean_axe_1h,
		itm_gamorrean_axe_2h,
		itm_gamorrean_axe_2h,
		#itm_dl18,
		#itm_dl18,
		itm_throwing_axes,
		itm_throwing_axes,
		itm_gamorrean_helmet,
		itm_transparent_helmet
		#itm_laser_bolts_orange_pistol,
		#itm_laser_bolts_orange_pistol
	],
	def_attrib_1|level(10),
	wp(100)|wp_firearm(105),
	starwars_skills_melee_1,
	gamorrean_face1, gamorrean_face2
],
["gamorrean_warrior","Gamorrean Warrior","Gamorrean Warriors",
	tf_gamorrean,
	no_scene,reserved,fac_commoners,
	[	
		itm_gamorrean_armor,
		itm_gamorrean_axe_1h,
		itm_gamorrean_axe_1h,
		itm_gamorrean_axe_2h,
		itm_gamorrean_axe_2h,
		#itm_dl18,
		#itm_dl18,
		itm_throwing_axes,
		itm_throwing_axes,		
		itm_gamorrean_helmet,
		itm_transparent_helmet
		#itm_laser_bolts_orange_pistol,
		#itm_laser_bolts_orange_pistol
	],
	def_attrib_2|level(16),
	wp(110)|wp_firearm(125),
	starwars_skills_melee_2,
	gamorrean_face1, gamorrean_face2
],
["gamorrean_guard","Gamorrean Guard","Gamorrean Guards",
	tf_gamorrean|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[	itm_gamorrean_armor,
		itm_durasteel_shield_small,
		itm_durasteel_shield_small_2,
		itm_vibro_axe_medium_1h,
		itm_vibro_axe_medium_1h,
		itm_dl18,
		itm_dl18,
		itm_transparent_helmet,
		#itm_gamorrean_helmet,		
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol
	],
	def_attrib_3|level(24),
	wp(135)|wp_firearm(140),
	starwars_skills_melee_3,
	gamorrean_face1, gamorrean_face2
],
["gamorrean_palace_guard","Gamorrean Palace Guard","Gamorrean Palace Guards",
	tf_gamorrean|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[	itm_gamorrean_armor,
		itm_durasteel_shield_small,
		itm_durasteel_shield_small_2,
		itm_vibro_axe_medium_1h,
		itm_vibro_axe_medium_1h,
		itm_dl18,
		itm_dl18,
		itm_transparent_helmet,		
		#itm_gamorrean_helmet,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol
	],
	def_attrib_4|level(30),
	wp(150)|wp_firearm(160),
	starwars_skills_melee_4,
	gamorrean_face1, gamorrean_face2
],

#twilek female
["twilek_female1","Twi'lek Female","Twilek Females",
	tf_twilek_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,
	0,0,fac_commoners,
	[	
		itm_dress, 
		itm_woolen_dress, 
		itm_peasant_dress,
		itm_blue_dress, 
		itm_woolen_hose, 
		itm_blue_hose,
		#itm_lady_gloves,
		#itm_lady_gloves,
		itm_twilek_dagger,
		itm_twilek_dagger,
		itm_twilek_dagger_throwing,
		itm_twilek_dagger_throwing
		# itm_westar,
		# itm_q2,
		# itm_ddc_defender,
		# itm_laser_bolts_orange,
		# itm_laser_bolts_orange
	],
	def_attrib_1|level(10),
	wp(100)|wp_firearm(105),
	starwars_skills_melee_1,
	twilek_female_face1, twilek_female_face2
],
["twilek_female2","Twi'lek Dancer","Twilek Dancers",
	tf_twilek_female|tf_guarantee_armor|tf_guarantee_ranged,
	0,0,fac_commoners,
	[
		itm_dress_yellow,
		itm_dress_red,
		itm_dress_green,
		itm_dress_blue,
		#itm_twilek_female_helmet,
		#itm_twilek_female_helmet,
		itm_twilek_dagger,
		itm_twilek_dagger,
		#itm_twilek_dagger_throwing,		
		itm_westar,
		itm_q2,
		itm_ddc_defender,				
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol
	],
	def_attrib_2|level(16),
	wp(110)|wp_firearm(125),
	starwars_skills_melee_2,
	twilek_female_face1, twilek_female_face2
],
["twilek_female3","Twi'lek Entertainer","Twilek Entertainers",
	tf_twilek_female|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,
	0,0,fac_commoners,
	[
		itm_twilek_dagger,
		itm_twilek_dagger,
		itm_westar,
		itm_ddc_defender,
		#itm_transparent_helmet_armor,
		itm_transparent_helmet_armor,
		#itm_twilek_female_helmet_armor,
		#itm_twilek_female_helmet_armor,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol,
		itm_energy_shield_yellow_small,
		itm_energy_shield_yellow_small
	],
	def_attrib_3|level(24),
	wp(135)|wp_firearm(140),
	starwars_skills_melee_3,
	twilek_female_face1, twilek_female_face2
],

#twilek   
["twilek","Twi'lek","Twi'leks",
	tf_twilek|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[
		itm_tunic_green,
		itm_tunic_green,
		itm_leather_boots,
		itm_leather_boots,
		#itm_leather_gloves,
		#itm_leather_gloves,
		itm_twilek_dagger,
		itm_twilek_dagger,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol,
		itm_ddc_defender,
		itm_ddc_defender,
		itm_westar,
		itm_westar
	],
	def_attrib_1|level(10),
	wp(100)|wp_firearm(105),
	starwars_skills_melee_1,
	twilek_face1, twilek_face2
],
["twilek_warrior","Twi'lek Warrior","Twi'lek Warriors",
	tf_twilek|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[
		itm_light_leather,
		itm_light_leather,
		itm_light_leather_boots,
		itm_light_leather_boots,
		#itm_leather_gloves,
		#itm_leather_gloves,
		itm_twilek_dagger,
		itm_twilek_dagger,		
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_ee3,
		itm_ee3
	],
	def_attrib_2|level(16),
	wp(110)|wp_crossbow(125),
	starwars_skills_melee_2,
	twilek_face1, twilek_face2
],
["twilek_soldier","Twi'lek Soldier","Twi'lek Soldiers",
	tf_twilek|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[
		itm_light_leather,
		itm_light_leather,
		itm_light_leather_boots,
		itm_light_leather_boots,
		#itm_leather_gloves,
		#itm_leather_gloves,
		itm_vibro_axe_long_2h,
		itm_vibro_axe_long_1h,
		itm_vibro_sword3_gold,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_a295,
		itm_a295_crouch,
		itm_transparent_helmet,
		itm_energy_shield_yellow_small,
		itm_energy_shield_yellow_small
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(140),
	starwars_skills_melee_3,
	twilek_face1, twilek_face2
],
["twilek_commando","Twi'lek Commando","Twi'lek Commandos",
	tf_twilek|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[
		itm_twilek_armor,
		itm_twilek_armor,
		itm_leather_boots,
		itm_leather_boots,
		itm_leather_gloves,
		itm_leather_gloves,
		itm_vibro_axe_long_2h,
		itm_vibro_axe_long_1h,
		itm_vibro_sword3_gold,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_a295,
		itm_a295_crouch,
		itm_transparent_helmet,
		itm_energy_shield_yellow_medium,
		itm_energy_shield_yellow_medium
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_melee_4,
	twilek_face1, twilek_face2
],

#Rodian
["rodian","Rodian","Rodians",
	tf_rodian|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[	itm_tunic_yellow,
		itm_tunic_yellow,
		itm_leather_boots,
		itm_leather_boots,
		#itm_leather_gloves,
		#itm_leather_gloves,
		itm_melee_punch,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol,
		itm_dl18,
		itm_ddc_defender,
		itm_westar
	],
	def_attrib_1|level(10),
	wp(100)|wp_firearm(105),
	starwars_skills_1,
	rodian_face1, rodian_face2
],
["rodian_warrior","Rodian Warrior","Rodian Warriors",
	tf_rodian|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[
		itm_vest_closed_b,
		itm_vest_closed_b,
		itm_black_boots,
		itm_black_boots,
		#itm_black_gloves,
		#itm_black_gloves,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_ee3,
		itm_ee3
	],
	def_attrib_2|level(16),
	wp(110)|wp_crossbow(125),
	starwars_skills_2,
	rodian_face1, rodian_face2
],
["rodian_hunter","Rodian Hunter","Rodian Hunters",
	tf_rodian|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[
		itm_jacket_closed_b,
		itm_jacket_closed_b,
		itm_black_boots,
		itm_black_boots,
		#itm_black_gloves,
		#itm_black_gloves,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_rodian_ventilator,
		itm_rodian_ventilator_red,
		itm_rodian_ventilator_black,
		itm_energy_shield_green_small,
		itm_energy_shield_green_small
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(140),
	starwars_skills_3,
	rodian_face1, rodian_face2
],
["rodian_bounty_hunter","Rodian Bounty Hunter","Rodian Bounty Hunters",
	tf_rodian|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[
		itm_jacket_closed_b,
		itm_jacket_closed_b,
		itm_black_boots,
		itm_black_boots,
		itm_black_gloves,
		itm_black_gloves,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_a295,
		itm_a295_crouch,
		itm_dlt19,
		itm_dlt20a,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_rodian_ventilator,		
		itm_rodian_ventilator_red,
		itm_rodian_ventilator_black,
		itm_energy_shield_green_medium,
		itm_energy_shield_green_medium
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_4,
	rodian_face1, rodian_face2
],

#Trandoshan
["trandoshan","Trandoshan","Trandoshans",
	tf_trandoshan|tf_guarantee_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[	
		itm_trandoshan_flight_suit,
		itm_trandoshan_flight_suit,
		itm_melee_punch,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol,
		itm_trandoshan_supressor,
		itm_trandoshan_supressor,
		itm_trandoshan_skin
	],
	def_attrib_1|level(10),
	wp(100)|wp_firearm(105),
	starwars_skills_1,
	trandoshan_face1, trandoshan_face2
],
["trandoshan_warrior","Trandoshan Warrior","Trandoshan Warriors",
	tf_trandoshan|tf_guarantee_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[	
		itm_trandoshan_flight_suit,
		itm_trandoshan_flight_suit,
		itm_trandoshan_blade,
		itm_trandoshan_blade,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol,
		itm_trandoshan_supressor,
		itm_trandoshan_supressor,
		itm_trandoshan_skin
	],
	def_attrib_2|level(16),
	wp(110)|wp_firearm(125),
	starwars_skills_2,
	trandoshan_face1, trandoshan_face2
],
["trandoshan_hunter","Trandoshan Hunter","Trandoshan Hunters",
	tf_trandoshan|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[	
		itm_trandoshan_armor,
		itm_trandoshan_armor,
		itm_trandoshan_blade,
		itm_trandoshan_blade,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_trandoshan_acp_array_gun,
		itm_trandoshan_acp_array_gun,
		itm_trandoshan_stun_gun,
		itm_trandoshan_stun_gun,
		itm_energy_shield_yellow_small,
		itm_energy_shield_yellow_small,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_trandoshan_mask,
		itm_trandoshan_helmet,
		itm_trandoshan_skin
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(140),
	starwars_skills_3,
	trandoshan_face1, trandoshan_face2
],
["trandoshan_bounty_hunter","Trandoshan Bounty Hunter","Trandoshan Bounty Hunters",
	tf_trandoshan|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[	
		itm_trandoshan_armor,
		itm_trandoshan_armor,
		itm_trandoshan_blade,
		itm_trandoshan_blade,		
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_trandoshan_acp_array_gun,
		itm_trandoshan_acp_array_gun,
		itm_energy_shield_yellow_medium,
		itm_energy_shield_yellow_medium,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_trandoshan_mask,
		itm_trandoshan_helmet,
		itm_trandoshan_skin
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_4,
	trandoshan_face1, trandoshan_face2
],

#moncal
["moncal_1","Mon Calamarian","Mon Calamarians",
	tf_moncal|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[	itm_moncal_armor,
		itm_moncal_armor,
		#itm_black_gloves,
		#itm_black_gloves,		
		itm_moncal_boots,
		itm_moncal_boots,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,
		itm_ddc_defender,
		itm_ddc_defender
	],
	def_attrib_1|level(10),
	wp(100)|wp_firearm(105),
	starwars_skills_1,
	moncal_face1, moncal_face2
],
["moncal_2","Mon Calamari Warrior","Mon Calamari Warriors",
	tf_moncal|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[	itm_moncal_armor,
		itm_moncal_armor,
		#itm_black_gloves,
		#itm_black_gloves,		
		itm_moncal_boots,
		itm_moncal_boots,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,
		itm_ddc_defender,
		itm_ddc_defender
	],
	def_attrib_2|level(16),
	wp(110)|wp_firearm(125),
	starwars_skills_2,
	moncal_face1, moncal_face2
],
["moncal_3","Mon Calamari Soldier","Mon Calamari Soldiers",
	tf_moncal|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_shield,
	no_scene,reserved,fac_commoners,
	[	itm_moncal_armor_2,
		itm_moncal_armor_2,
		#itm_black_gloves,
		#itm_black_gloves,		
		itm_moncal_boots,
		itm_moncal_boots,
		itm_moncal_helmet,
		itm_moncal_helmet,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_ee3,
		itm_ee3,
		itm_energy_shield_green_small,
		itm_energy_shield_blue_small
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(140),
	starwars_skills_3,
	moncal_face1, moncal_face2
],
["moncal_4","Mon Calamari Knight","Mon Calamari Knights",
	tf_moncal|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_shield,
	no_scene,reserved,fac_commoners,
	[	
		itm_moncal_armor_2,
		itm_moncal_armor_2,
		itm_black_gloves,
		itm_black_gloves,		
		itm_moncal_boots,
		itm_moncal_boots,
		itm_moncal_helmet,
		itm_moncal_helmet,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_energy_shield_green_medium,
		itm_energy_shield_blue_medium
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_4,
	moncal_face1, moncal_face2
],

#chiss
["chiss_1","Chiss","Chiss",
	tf_chiss|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[
		itm_tunic_green,
		itm_tunic_green,
		itm_leather_boots,
		itm_leather_boots,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_red_pistol,
		itm_laser_bolts_red_pistol,
		itm_ddc_defender,
		#itm_ddc_defender,
		#itm_westar,
		itm_westar	
	],
	def_attrib_1|level(10),
	wp(100)|wp_firearm(105),
	starwars_skills_1,
	chiss_face1, chiss_face2
],
["chiss_2","Chiss Soldier","Chiss Soldiers",
	tf_chiss|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[
		itm_vest_closed_b,
		itm_vest_closed_b,
		itm_leather_boots,
		itm_leather_boots,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_ee3,
		itm_ee3	
	],
	def_attrib_2|level(16),
	wp(110)|wp_crossbow(125),
	starwars_skills_2,
	chiss_face1, chiss_face2
],
["chiss_3","Chiss Officer","Chiss Officer",
	tf_chiss|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[
		itm_jacket_closed_b,
		itm_jacket_closed_b,
		itm_leather_boots,
		itm_leather_boots,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_a295,
		itm_a295_crouch,
		itm_transparent_helmet,
		itm_energy_shield_red_small,
		itm_energy_shield_red_small
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(140),
	starwars_skills_3,
	chiss_face1, chiss_face2
],
["chiss_4","Chiss Commander","Chiss Commanders",
	tf_chiss|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_shield,
	no_scene,reserved,fac_commoners,
	[
		itm_jacket_closed_b,
		itm_jacket_closed_b,
		itm_black_boots,
		itm_black_boots,
		itm_black_gloves,
		itm_black_gloves,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_a295,
		itm_a295_crouch,
		itm_dlt19,
		itm_dlt20a,
		itm_transparent_helmet,
		itm_energy_shield_red_small,
		itm_energy_shield_red_medium
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_4,
	chiss_face1, chiss_face2
],

#geonosian
["geonosian_1","Geonosian","Geonosians",
	tf_geonosian|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[
		itm_geonosian_sonic_pistol,
		itm_geonosian_sonic_pistol,
		itm_sonic_beam_pistol,
		itm_sonic_beam_pistol,
		itm_geonosian_static_pike,
		itm_geonosian_static_pike
	],
	def_attrib_1|level(10),
	wp(100)|wp_firearm(105),
	starwars_skills_1,
	geonosian_face1, geonosian_face2
],
["geonosian_2","Geonosian Drone","Geonosian Drones",
	tf_geonosian|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[
		itm_geonosian_sonic_pistol,
		itm_geonosian_sonic_pistol,
		itm_sonic_beam_pistol,
		itm_sonic_beam_pistol,		
		itm_geonosian_static_pike,
		itm_geonosian_static_pike
	],
	def_attrib_2|level(16),
	wp(110)|wp_firearm(125),
	starwars_skills_2,
	geonosian_face1, geonosian_face2
],
["geonosian_3","Geonosian Warrior","Geonosian Warrior",
	tf_geonosian|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[
		itm_geonosian_armor,
		itm_geonosian_sonic_rifle,
		itm_geonosian_sonic_rifle,
		itm_sonic_beam_rifle,
		itm_sonic_beam_rifle,		
		itm_transparent_helmet,
		itm_geonosian_static_pike,
		itm_geonosian_static_pike
		#itm_energy_shield_yellow_medium,
		#itm_energy_shield_yellow_medium
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(140),
	starwars_skills_3,
	geonosian_face1, geonosian_face2
],
["geonosian_4","Veteran Geonosian Warrior","Veteran Geonosian Warrior",
	tf_geonosian|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[
		itm_geonosian_armor,
		itm_geonosian_sonic_rifle,
		itm_geonosian_sonic_rifle,
		itm_sonic_beam_rifle,
		itm_sonic_beam_rifle,		
		itm_transparent_helmet,
		itm_geonosian_static_pike,		
		itm_geonosian_static_pike
		#itm_energy_shield_yellow_medium,
		#itm_energy_shield_yellow_medium
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_4,
	geonosian_face1, geonosian_face2
],

#sullustan
["sullustan_1","Sullustan","Sullustans",
	tf_sullustan|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[	itm_vest_closed_a,
		itm_vest_closed_a,
		#itm_black_gloves,
		#itm_black_gloves,		
		itm_black_boots,
		itm_black_boots,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,
		itm_ddc_defender,
		itm_ddc_defender,
		#itm_westar,
		itm_westar
	],
	def_attrib_1|level(10),
	wp(100)|wp_firearm(105),
	starwars_skills_1,
	sullustan_face1, sullustan_face2
],
["sullustan_2","Sullustan Navigator","Sullustan Navigators",
	tf_sullustan|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[	itm_vest_closed_a,
		itm_vest_closed_a,
		#itm_black_gloves,
		#itm_black_gloves,		
		itm_black_boots,
		itm_black_boots,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,
		itm_ddc_defender,
		itm_ddc_defender,
		itm_westar,
		itm_westar
	],
	def_attrib_2|level(16),
	wp(110)|wp_firearm(125),
	starwars_skills_2,
	sullustan_face1, sullustan_face2
],
["sullustan_3","Sullustan Pilot","Sullustan Pilots",
	tf_sullustan|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[	itm_vest_closed_a,
		itm_vest_closed_a,
		#itm_black_gloves,
		#itm_black_gloves,		
		itm_black_boots,
		itm_black_boots,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_quicksnap_36t,
		itm_quicksnap_36t,
		itm_transparent_helmet,
		itm_energy_shield_green_small,
		itm_energy_shield_blue_small
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(140),
	starwars_skills_3,
	sullustan_face1, sullustan_face2
],
["sullustan_4","Sullustan Captain","Sullustan Captains",
	tf_sullustan|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[	itm_vest_closed_a,
		itm_vest_closed_a,
		itm_black_gloves,
		itm_black_gloves,		
		itm_black_boots,
		itm_black_boots,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_quicksnap_36t,
		itm_quicksnap_36t,
		itm_transparent_helmet,
		itm_energy_shield_green_medium,
		itm_energy_shield_blue_medium
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_4,
	sullustan_face1, sullustan_face2
],

#bothan
["bothan","Bothan","Bothans",
	tf_bothan|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[	itm_tunic_red,
		itm_tunic_red,
		#itm_leather_gloves,
		#itm_leather_gloves,		
		itm_leather_boots,
		itm_leather_boots,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,
		itm_ddc_defender,
		itm_ddc_defender,
		itm_westar,
		itm_westar
	],
	def_attrib_1|level(10),
	wp(100)|wp_firearm(105),
	starwars_skills_melee_1,
	bothan_face1, bothan_face2
],
["bothan_militia","Bothan Militia","Bothan Militia",
	tf_bothan|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[	itm_jacket_open_a,
		itm_jacket_open_a,
		#itm_leather_gloves,
		#itm_leather_gloves,		
		itm_leather_boots,
		itm_leather_boots,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,
		itm_ddc_defender,
		itm_ddc_defender,
		itm_westar,
		itm_westar
	],
	def_attrib_2|level(16),
	wp(110)|wp_firearm(125),
	starwars_skills_melee_2,
	bothan_face1, bothan_face2
],
["bothan_agent","Bothan Agent","Bothan Agents",
	tf_bothan|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[	itm_jacket_open_a,
		itm_jacket_open_a,
		#itm_leather_gloves,
		#itm_leather_gloves,		
		itm_leather_boots,
		itm_leather_boots,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,
		itm_ddc_defender,
		itm_ddc_defender,
		itm_westar,
		itm_westar
	],
	def_attrib_2|level(16),
	wp(110)|wp_firearm(125),
	starwars_skills_melee_2,
	bothan_face1, bothan_face2
],
["bothan_infantry","Bothan Infantry","Bothan Infantry",
	tf_bothan|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[	itm_republic_trooper_armor,
		itm_republic_trooper_armor,
		itm_black_gloves,
		itm_black_gloves,		
		itm_black_boots,
		itm_black_boots,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_bothan_bola_carabine,
		itm_bothan_bola_carabine,
		itm_transparent_helmet
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(140),
	starwars_skills_3,
	bothan_face1, bothan_face2
],
["bothan_spy","Bothan Spy","Bothan Spies",
	tf_bothan|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[	itm_vest_closed_a,
		itm_vest_closed_a,
		itm_black_gloves,
		itm_black_gloves,		
		itm_black_boots,
		itm_black_boots,
		itm_vibro_sword3_gold,
		itm_vibro_sword3_red,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,		
		itm_ddc_defender,
		itm_ddc_defender,
		itm_westar,
		itm_westar,
		itm_transparent_helmet,
		itm_energy_shield_green_small,
		itm_energy_shield_blue_small
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(140),
	starwars_skills_melee_3,
	bothan_face1, bothan_face2
],
["bothan_infiltrator","Bothan Infiltrator","Bothan Infiltrators",
	tf_bothan|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,reserved,fac_commoners,
	[	itm_vest_closed_a,
		itm_vest_closed_a,
		itm_black_gloves,
		itm_black_gloves,		
		itm_black_boots,
		itm_black_boots,
		itm_vibro_sword3_gold,
		itm_vibro_sword3_red,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_bothan_bola_carabine,
		itm_bothan_bola_carabine,
		itm_transparent_helmet,
		itm_energy_shield_green_medium,
		itm_energy_shield_blue_medium
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_melee_4,
	bothan_face1, bothan_face2
],

#ig88 droid merc
["ig88","IG-Series Assassin Droid","IG-Series Assassin Droids",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_shield,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_ig88_attack,
		itm_ig88_head,
		itm_ig88_body,
		itm_ig88_hands,
		itm_ig88_feet,
		itm_ig88_e11_shield,
		itm_ig88_dlt20a,
		itm_ig88_dlt20a,		#gave 2x so ther eis a chance the player could find it in the loot after a battle
		itm_laser_bolts_orange_pistol,	#have to give pistol ammo since itm_ig88_dlt20a is a pistol so it can be carried 1-handed
		itm_laser_bolts_orange_pistol	#have to give pistol ammo since itm_ig88_dlt20a is a pistol so it can be carried 1-handed
	],
	str_16|int_12|level(35),
	wp(175)|wp_crossbow(200),
	knows_ironflesh_8|knows_power_strike_6|knows_weapon_master_8|knows_shield_6|knows_tactics_5|knows_leadership_5|knows_trainer_2,
	droid_face1, droid_face2
],

#ihk droid merc
["hkseries","HK-Series Droid","HK-Series Droids",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_shield,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_hk_attack,
		itm_hk_head,
		itm_hk_body,
		itm_hk_hands,
		itm_hk_feet,
		itm_a280,
		itm_a295,
		itm_dlt19,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle
	],
	str_14|int_8|level(24),
	wp(150)|wp_crossbow(175),
	knows_ironflesh_7|knows_power_strike_5|knows_weapon_master_6|knows_shield_3|knows_tactics_4|knows_leadership_3|knows_trainer_2,
	droid_face1, droid_face2
],

#ig88 droid merc
["defiler","Defiler","Defilers",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_commoners,
	[
		itm_defiler_helmet,
		itm_defiler_helmet,
		itm_defiler_armor,
		itm_defiler_boots,
		itm_black_gloves,
		itm_black_gloves,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_a295,
		itm_a295_crouch,
		itm_a295,
		itm_a295_crouch,
		itm_mandalorian_heavy_blaster,
		itm_mandalorian_heavy_blaster
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(175),
	starwars_skills_4,
	sw_man_face_1, sw_man_face_2
],

#human merc upgrade paths

  ["farmer","Farmer","Farmers",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_baton,itm_baton,itm_pipe1,itm_pipe2,itm_melee_punch,itm_melee_punch,itm_q2,itm_ddc_defender,itm_westar,itm_laser_bolts_orange_pistol,itm_laser_bolts_yellow_pistol,itm_vibro_blade1,itm_durasteel_staff,itm_quarter_staff,itm_vibro_blade2,itm_vibro_blade3,itm_club,itm_leather_cap,itm_leather_apron,itm_linen_tunic,itm_coarse_tunic,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_a,itm_leather_gloves,itm_leather_boots,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(6),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
  ["townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_pipe1,itm_pipe2,itm_melee_punch,itm_q2,itm_ddc_defender,itm_westar,itm_laser_bolts_orange_pistol,itm_laser_bolts_yellow_pistol,itm_vibro_blade1,itm_durasteel_staff,itm_quarter_staff,itm_vibro_blade2,itm_vibro_blade3,itm_club,itm_leather_cap,itm_leather_apron,itm_linen_tunic,itm_coarse_tunic,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_a,itm_leather_gloves,itm_leather_boots,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(6),wp(60),knows_common,sw_man_face_1, sw_man_face_2],

  ["civilian","Civilian","Civilians",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
	[
		itm_baton,
		itm_pipe1,
		itm_pipe2,
		itm_melee_punch,
		itm_melee_punch,
		itm_q2,
		itm_ddc_defender,
		itm_westar,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_yellow_pistol,
		itm_jacket_closed_a,
		itm_jacket_closed_c,
		itm_jacket_open_a,
		itm_jacket_open_c,
		itm_vest_closed_a,
		itm_vest_open_a,
		itm_vest_open_b,
		itm_leather_gloves,
		itm_leather_gloves,
		itm_leather_boots,
		itm_leather_boots
	],
	def_attrib_1|level(10),
	wp(100)|wp_firearm(105),
	starwars_skills_1,	
	sw_man_face_1, sw_man_face_2
  ],

  ["militia","Militia","Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
	[
		itm_baton,
		itm_baton,
		itm_ddc_defender,
		itm_ddc_defender,
		itm_dl44a,
		itm_dl44a,
		itm_westar,
		itm_westar,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_yellow_pistol,
		itm_vest_closed_b,
		itm_vest_closed_b,		
		itm_jacket_closed_b,
		itm_jacket_closed_b,
		itm_leather_boots,
		itm_leather_boots
	],
	def_attrib_2|level(16),
	wp(110)|wp_firearm(125),
	starwars_skills_2,
   sw_man_face_1, sw_man_face_2
  ],

  ["security_guard","Security Guard","Security Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
	[
		itm_baton,
		itm_baton,
		itm_ddc_defender,
		itm_ddc_defender,
		itm_dl44a,
		itm_dl44a,
		itm_westar,
		itm_westar,
		itm_energy_shield_yellow_small,
		itm_energy_shield_yellow_small,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_yellow_pistol,
		itm_blast_armor_red,
		itm_blast_armor_black,
		itm_blast_armor_grey,
		itm_blast_armor_bluegrey,
		itm_leather_boots,
		itm_leather_boots
	],
	def_attrib_3|level(24),
	wp(135)|wp_firearm(140),
	starwars_skills_melee_3,
   sw_man_face_1, sw_man_face_2
  ],   

  ["soldier","Soldier","Soldiers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
	[
		itm_baton,
		itm_baton,
		itm_a280,
		itm_a280_crouch,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_yellow_rifle,
		itm_vest_closed_b,
		itm_vest_closed_b,		
		itm_jacket_closed_b,
		itm_jacket_closed_b,
		itm_leather_boots,
		itm_leather_boots
	],
	def_attrib_3|level(24),
	wp(135)|wp_firearm(140),
	starwars_skills_3,
   sw_man_face_1, sw_man_face_2
  ],     

  ["bodyguard","Bodyguard","Bodyguards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
	[
		itm_vibro_sword3_gold,
		itm_vibro_sword3_gold,
		itm_a280,
		itm_a280_crouch,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_yellow_rifle,		
		itm_energy_shield_yellow_medium,
		itm_energy_shield_yellow_medium,
		itm_blast_armor_red,
		itm_blast_armor_black,
		itm_blast_armor_grey,
		itm_blast_armor_bluegrey,
		itm_leather_boots,
		itm_leather_boots
	],
	def_attrib_4|level(30),
	wp(150)|wp_firearm(160),
	starwars_skills_melee_4,
   sw_man_face_1, sw_man_face_2
  ],   

  ["commando","Commando","Commandos",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
	[
		itm_baton,
		itm_baton,
		itm_a280,
		itm_a280_crouch,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_yellow_rifle,
		itm_vest_closed_b,
		itm_vest_closed_b,		
		itm_jacket_closed_b,
		itm_jacket_closed_b,
		itm_leather_boots,
		itm_leather_boots
	],
	def_attrib_4|level(30),
	wp(150)|wp_firearm(160),
	starwars_skills_4,
   sw_man_face_1, sw_man_face_2
  ],     

  ["pilot","Pilot","Pilots",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,no_scene,reserved,fac_commoners,
	[
		itm_speeder,
		itm_speeder,
		itm_speeder_hutt,
		itm_speeder_hutt,
		itm_speeder_sparrow,
		itm_speeder_dagger,
		itm_swoop_bike,
		itm_pod_racer,			
		itm_vibro_sword3_gold,
		itm_vibro_sword3_gold,
		itm_ddc_defender,
		itm_ddc_defender,
		itm_dl44a,
		itm_dl44a,
		itm_westar,
		itm_westar,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_yellow_pistol,
		itm_vest_closed_b,
		itm_vest_closed_b,		
		itm_jacket_closed_b,
		itm_jacket_closed_b,
		itm_leather_boots,
		itm_leather_boots
	],
	def_attrib_4|level(30),
	wp(150)|wp_firearm(160),
	starwars_skills_mounted_4,
   sw_man_face_1, sw_man_face_2
  ],     
  
  ["thug","Thug","Thugs",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
	[
		itm_baton,
		itm_durasteel_mace,
		itm_durasteel_bat,
		itm_vibro_blade1,
		itm_vibro_blade2,
		itm_vibro_knuckler,
		itm_combat_knife,		
		itm_ddc_defender,
		itm_ddc_defender,
		itm_dl44a,
		itm_dl44a,
		itm_westar,
		itm_westar,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_yellow_pistol,
		itm_jacket_closed_a,
		itm_jacket_closed_c,
		itm_jacket_open_a,
		itm_jacket_open_c,
		itm_vest_closed_a,
		itm_vest_open_a,
		itm_vest_open_b,
		itm_leather_gloves,
		itm_leather_gloves,
		itm_black_boots,
		itm_black_boots,
		itm_leather_boots,
		itm_leather_boots
	],
	def_attrib_2|level(16),
	wp(110)|wp_firearm(125),
	starwars_skills_melee_2,
   sw_man_face_1, sw_man_face_2
 ],

  ["goon","Goon","Goons",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
	[
		itm_baton,
		itm_durasteel_mace,
		itm_durasteel_bat,
		itm_vibro_blade1,
		itm_vibro_blade2,
		itm_vibro_knuckler,
		itm_combat_knife,		
		itm_ddc_defender,
		itm_ddc_defender,
		itm_dl44a,
		itm_dl44a,
		itm_westar,
		itm_westar,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_yellow_pistol,
		itm_jacket_closed_a,
		itm_jacket_closed_c,
		itm_jacket_open_a,
		itm_jacket_open_c,
		itm_vest_closed_a,
		itm_vest_open_a,
		itm_vest_open_b,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_mining_helmet,
		itm_pipe_helmet,
		itm_fang_helmet,
		itm_beak_helmet,
		itm_gas_mask,
		itm_leather_gloves,
		itm_leather_gloves,
		itm_black_boots,
		itm_black_boots,
		itm_leather_boots,
		itm_leather_boots
	],
	def_attrib_3|level(24),
	wp(135)|wp_firearm(140),
	starwars_skills_melee_3,
   sw_man_face_1, sw_man_face_2
 ], 

  ["biker","Biker","Bikers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,no_scene,reserved,fac_commoners,
	[
		itm_speeder,
		itm_speeder,
		itm_speeder_hutt,
		itm_speeder_hutt,
		itm_speeder_sparrow,
		itm_speeder_dagger,
		itm_swoop_bike,
		itm_pod_racer,		
		itm_durasteel_mace,
		itm_durasteel_bat,
		itm_vibro_sword3_gold,
		itm_vibro_sword3_gold,
		itm_ddc_defender,
		itm_ddc_defender,
		itm_dl44a,
		itm_dl44a,
		itm_westar,
		itm_westar,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_yellow_pistol,
		itm_jacket_closed_a,
		itm_jacket_closed_c,
		itm_jacket_open_a,
		itm_jacket_open_c,
		itm_vest_closed_a,
		itm_vest_open_a,
		itm_vest_open_b,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_mining_helmet,
		itm_pipe_helmet,
		itm_fang_helmet,
		itm_beak_helmet,
		itm_gas_mask,		
		itm_leather_gloves,
		itm_leather_gloves,
		itm_black_boots,
		itm_black_boots,
		itm_leather_boots,
		itm_leather_boots
	],
	def_attrib_3|level(24),
	wp(135)|wp_firearm(140),
	starwars_skills_mounted_3,
   sw_man_face_1, sw_man_face_2
 ],  
 
  ["assassin","Assassin","Assassins",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
	[
		itm_transparent_helmet,
		itm_transparent_helmet,	
		itm_glasses_black,
		itm_glasses_yellow,
		itm_eyepiece_tactics,
		itm_eyepiece_leadership,		
		itm_mercenary_armor,
		itm_mercenary_armor,
		itm_black_boots,
		itm_black_boots,
		itm_black_gloves,
		itm_black_gloves,		
		itm_vibro_sword3_gold,
		itm_vibro_sword3_gold,
		itm_energy_shield_yellow_medium,
		itm_energy_shield_yellow_medium,
		itm_a295,
		itm_a295_crouch,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_yellow_rifle
	],
	def_attrib_4|level(30),
	wp(150)|wp_firearm(160),
	starwars_skills_melee_4,
   sw_man_face_1, sw_man_face_2
 ], 

  ["biker_scout","Biker Scout","Biker Scouts",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,no_scene,reserved,fac_commoners,
	[
		itm_speeder,
		itm_speeder,
		itm_speeder_hutt,
		itm_speeder_hutt,
		itm_speeder_sparrow,
		itm_speeder_dagger,
		itm_swoop_bike,
		itm_pod_racer,		
		itm_vibro_sword3_gold,
		itm_vibro_sword3_gold,
		itm_energy_shield_yellow_small,
		itm_energy_shield_yellow_small,		
		itm_a280,
		itm_a280_crouch,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_yellow_rifle,		
		itm_jacket_closed_a,
		itm_jacket_closed_c,
		itm_jacket_open_a,
		itm_jacket_open_c,
		itm_vest_closed_a,
		itm_vest_open_a,
		itm_vest_open_b,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_glasses_black,
		itm_glasses_yellow,		
		itm_mining_helmet,
		itm_pipe_helmet,
		itm_fang_helmet,
		itm_beak_helmet,
		itm_gas_mask,
		itm_leather_gloves,
		itm_leather_gloves,
		itm_black_boots,
		itm_black_boots,
		itm_leather_boots,
		itm_leather_boots
	],
	def_attrib_4|level(30),
	wp(150)|wp_firearm(160),
	starwars_skills_mounted_4,
   sw_man_face_1, sw_man_face_2
 ], 
 
 
 
# ["hired_guard","Security Guard","Security Guards",
	# tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,
	# no_scene,0,fac_commoners,
	# [	
		# itm_guard_armor,
		# itm_guard_armor,
		# #itm_guard_armor_red,  	(no LOD's)
		# itm_guard_armor_red,
		# itm_energy_shield_yellow_small,
		# itm_energy_shield_blue_small,
		# itm_black_boots,
		# itm_black_boots,
		# itm_baton,
		# itm_baton,
		# itm_vibro_blade1,
		# itm_vibro_blade3,
		# itm_laser_bolts_yellow_pistol,
		# itm_laser_bolts_yellow_pistol,
		# itm_dl44a,
		# itm_dl44a,
		# itm_elg3a,
		# itm_elg3a
	# ],
	# def_attrib_2|level(16),
	# wp(110)|wp_firearm(125),
	# starwars_skills_2,
	# sw_man_face_1, sw_man_face_2
# ],
# ["hired_guardian","Security Officer","Security Officers",
	# tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_helmet,
	# no_scene,0,fac_commoners,
	# [	
		# itm_blast_armor,
		# itm_blast_armor,
		# itm_energy_shield_yellow_medium,
		# itm_energy_shield_blue_medium,
		# itm_leather_boots,
		# itm_leather_boots,
		# itm_leather_gloves,
		# itm_leather_gloves,
		# itm_vibro_blade1,
		# itm_vibro_blade3,
		# itm_laser_bolts_yellow_rifle,
		# itm_laser_bolts_yellow_rifle,
		# itm_transparent_helmet,
		# itm_transparent_helmet,
		# itm_a280,
		# itm_a280,
		# itm_a295,
		# itm_a295
	# ],
	# def_attrib_3|level(24),
	# wp(135)|wp_crossbow(140),
	# starwars_skills_3,
	# sw_man_face_1, sw_man_face_2
# ],
   
#####################################################################################################
["mercenaries_end","mercenaries_end","mercenaries_end",0,no_scene,reserved,fac_commoners, [], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
#####################################################################################################

#specialized mercs, must build village improvement to recruit

#oom_series droid
["oom_series_security","OOM Security Battle Droid","OOM Security Battle Droids",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_battle_droid_attack,
		itm_transparent_droid_head,
		itm_transparent_droid_hands,
		itm_transparent_droid_feet,		
		itm_oomseries_body,
		itm_e5,
		itm_e5,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle
	],
	str_6|int_3|cha_3|agi_3|level(1),
	wp(60)|wp_crossbow(80),
	knows_ironflesh_3|knows_tactics_2|knows_leadership_2|knows_trainer_2,
	droid_face1, droid_face2
],

["oom_series_marine","OOM Marine Battle Droid","OOM Marine Battle Droids",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_battle_droid_attack,
		itm_transparent_droid_head,
		itm_transparent_droid_hands,
		itm_transparent_droid_feet,		
		itm_oomseries_marine_body,
		itm_e5,
		itm_e5,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle
	],
	str_10|int_6|cha_3|agi_6|level(12),
	wp(140)|wp_crossbow(160),
	knows_ironflesh_6|knows_tactics_4|knows_leadership_4|knows_trainer_4,
	droid_face1, droid_face2
],

["oom_series_pilot","OOM Pilot Battle Droid","OOM Pilot Battle Droids",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_vibro_sword3_blue,
		itm_transparent_droid_head,
		itm_transparent_droid_hands,
		itm_transparent_droid_feet,		
		itm_oomseries_pilot_body,
		itm_e5,
		itm_e5,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_horus_winged_cruiser,
		itm_horus_winged_cruiser
	],
	str_10|int_6|cha_3|agi_6|level(12),
	wp(140)|wp_crossbow(160),
	knows_ironflesh_6|knows_tactics_4|knows_leadership_4|knows_trainer_4|knows_riding_5|knows_horse_archery_5,
	droid_face1, droid_face2
],

["oom_series_command","OOM Command Battle Droid","OOM Command Battle Droid",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_battle_droid_attack,
		itm_transparent_droid_head,
		itm_transparent_droid_hands,
		itm_transparent_droid_feet,		
		itm_oomseries_command_body,
		itm_e5,
		itm_e5,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle
	],
	str_16|int_9|cha_3|agi_9|level(24),
	wp(160)|wp_crossbow(180),
	knows_ironflesh_9|knows_tactics_6|knows_leadership_6|knows_trainer_6,
	droid_face1, droid_face2
],

# b1series droid
["b1series","B1-Series Battle Droid","B1-Series Battle Droids",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_battle_droid_attack,
		itm_transparent_droid_head,
		itm_transparent_droid_hands,
		itm_transparent_droid_feet,		
		itm_b1series_body,
		itm_e5,
		itm_e5,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle
	],
	str_6|int_3|cha_3|agi_3|level(1),
	wp(60)|wp_crossbow(80),
	knows_ironflesh_3|knows_tactics_2|knows_leadership_2|knows_trainer_2,
	droid_face1, droid_face2
],

["b1series_assassin","B1-Series Droid Assassin","B1-Series Droid Assassins",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_battle_droid_attack,
		itm_transparent_droid_head,
		itm_transparent_droid_hands,
		itm_transparent_droid_feet,		
		itm_b1series_body,
		itm_dlt19,
		itm_dlt19,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle
	],
	str_10|int_6|cha_3|agi_6|level(12),
	wp(140)|wp_crossbow(160),
	knows_ironflesh_6|knows_tactics_4|knows_leadership_4|knows_trainer_4,
	droid_face1, droid_face2
],

["bxseries_commando","BX-Series Droid Commando","BX-Series Droid Commandos",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_vibro_blade1,
		itm_vibro_blade2,
		itm_transparent_droid_head,
		itm_transparent_droid_hands,
		itm_transparent_droid_feet,		
		itm_bxseries_body,
		itm_e5,
		itm_e5,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle
	],
	str_16|int_9|cha_3|agi_9|level(24),
	wp(160)|wp_crossbow(180),
	knows_ironflesh_9|knows_tactics_6|knows_leadership_6|knows_trainer_6,
	droid_face1, droid_face2
],

# ["b2series","B2-Series Battle Droid","B2-Series Battle Droids",
	# tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
	# no_scene,0,fac_commoners,
	# [
		# itm_droid_parts,
		# itm_b2series_attack,
		# itm_transparent_droid_head,
		# itm_transparent_droid_hands,
		# itm_transparent_droid_feet,		
		# itm_b2series_body,
		# itm_b2series_blaster,
		# #itm_b2series_blaster,
		# itm_laser_bolts_red_pistol,
		# itm_laser_bolts_red_pistol
	# ],
	# str_12|int_8|cha_3|level(25),
	# wp(140)|wp_firearm(160),
	# knows_ironflesh_8|knows_tactics_6|knows_leadership_6|knows_trainer_4,
	# droid_face1, droid_face2
# ],

#clone troopers
["clone_trooper_1","Clone Trooper","Clone Troopers",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[
		#itm_clone_trooper_head,
		#itm_clone_trooper_head,
		itm_clone_trooper_helmet_white,
		itm_clone_trooper_helmet_white,
		itm_clone_trooper_armor_white,
		itm_clone_trooper_armor_white,	
		itm_clone_trooper_gloves_white,
		itm_clone_trooper_gloves_white,
		itm_clone_trooper_boots,
		itm_clone_trooper_boots,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_blue_rifle,
		itm_laser_bolts_blue_rifle,
		itm_dc15s,
		itm_dc15s,
		itm_dc15s,
		#itm_dc15a,
		itm_dc15a_hip
	],
	def_attrib_1|level(10),
	wp(100)|wp_crossbow(105),
	starwars_skills_1,
	mandalorian_face1, mandalorian_face2
],
["clone_trooper_2","Clone Trooper Sergeant","Clone Trooper Sergeants",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[   
		#itm_clone_trooper_head,
		#itm_clone_trooper_head,
		itm_clone_trooper_helmet_green,
		itm_clone_trooper_helmet_green,
		itm_clone_trooper_armor_green,
		itm_clone_trooper_armor_green,	
		itm_clone_trooper_gloves_green,
		itm_clone_trooper_gloves_green,
		itm_clone_trooper_boots,
		itm_clone_trooper_boots,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_blue_rifle,
		itm_laser_bolts_blue_rifle,
		itm_dc15s,
		#itm_dc15s,
		itm_dc15a,
		itm_dc15a_hip
	],
	def_attrib_2|level(16),
	wp(110)|wp_crossbow(125),
	starwars_skills_2,
	mandalorian_face1, mandalorian_face2
],
["arc_trooper_2","Arc Trooper Sergeant","Arc Trooper Sergeants",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[   
		#itm_clone_trooper_head,
		#itm_clone_trooper_head,
		itm_clone_trooper_helmet_green,
		itm_clone_trooper_helmet_green,
		itm_arc_trooper_armor_green,
		itm_arc_trooper_armor_green,	
		itm_clone_trooper_gloves_green,
		itm_clone_trooper_gloves_green,
		itm_clone_trooper_boots,
		itm_clone_trooper_boots,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_blue_rifle,
		itm_laser_bolts_blue_rifle,
		itm_dc15s,
		#itm_dc15s,
		itm_dc15a,
		itm_dc15a_hip
	],
	def_attrib_2|level(16),
	wp(110)|wp_crossbow(125),
	starwars_skills_2,
	mandalorian_face1, mandalorian_face2
],
["clone_trooper_3","Clone Trooper Lieutenant","Clone Trooper Lieutenants",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[   
		#itm_clone_trooper_head,
		#itm_clone_trooper_head,
		itm_clone_trooper_helmet_blue,
		itm_clone_trooper_helmet_blue,
		itm_clone_trooper_armor_blue,
		itm_clone_trooper_armor_blue,	
		itm_clone_trooper_gloves_blue,
		itm_clone_trooper_gloves_blue,
		itm_clone_trooper_boots,
		itm_clone_trooper_boots,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_blue_rifle,
		itm_laser_bolts_blue_rifle,
		itm_dc15s,
		#itm_dc15s,
		itm_dc15a,
		itm_dc15a_hip
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(140),
	starwars_skills_3,
	mandalorian_face1, mandalorian_face2
],
["arc_trooper_3","Arc Trooper Lieutenant","Arc Trooper Lieutenants",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[   
		#itm_clone_trooper_head,
		#itm_clone_trooper_head,
		itm_clone_trooper_helmet_blue,
		itm_clone_trooper_helmet_blue,
		itm_arc_trooper_armor_blue,
		itm_arc_trooper_armor_blue,	
		itm_clone_trooper_gloves_blue,
		itm_clone_trooper_gloves_blue,
		itm_clone_trooper_boots,
		itm_clone_trooper_boots,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_blue_rifle,
		itm_laser_bolts_blue_rifle,
		itm_dc15s,
		#itm_dc15s,
		itm_dc15a,
		itm_dc15a_hip,
		itm_dc15a_hip
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(140),
	starwars_skills_3,
	mandalorian_face1, mandalorian_face2
],
["clone_trooper_4","Clone Trooper Captain","Clone Trooper Captains",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[   
		#itm_clone_trooper_head,
		#itm_clone_trooper_head,
		itm_clone_trooper_helmet_red,
		itm_clone_trooper_helmet_red,
		itm_clone_trooper_armor_red,
		itm_clone_trooper_armor_red,	
		itm_clone_trooper_gloves_red,
		itm_clone_trooper_gloves_red,
		itm_clone_trooper_boots,
		itm_clone_trooper_boots,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_blue_rifle,
		itm_laser_bolts_blue_rifle,
		#itm_dc15s,
		#itm_dc15s,
		itm_dc15a,
		itm_dc15a_hip,
		itm_dc15a_hip
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_4,
	mandalorian_face1, mandalorian_face2
],
["arc_trooper_4","Arc Trooper Captain","Arc Trooper Captains",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[   
		#itm_clone_trooper_head,
		#itm_clone_trooper_head,
		itm_clone_trooper_helmet_red,
		itm_clone_trooper_helmet_red,
		itm_arc_trooper_armor_red,
		itm_arc_trooper_armor_red,
		itm_clone_trooper_gloves_red,
		itm_clone_trooper_gloves_red,
		itm_clone_trooper_boots,
		itm_clone_trooper_boots,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_blue_rifle,
		itm_laser_bolts_blue_rifle,
		#itm_dc15s,
		#itm_dc15s,
		itm_dc15a,
		itm_dc15a_hip,
		itm_dc15a_hip
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_4,
	mandalorian_face1, mandalorian_face2
],
["clone_trooper_5","Clone Trooper Commander","Clone Trooper Commanders",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[   
		#itm_clone_trooper_head,
		#itm_clone_trooper_head,
		itm_clone_trooper_helmet_yellow,
		itm_clone_trooper_helmet_yellow,
		itm_clone_trooper_armor_yellow,
		itm_clone_trooper_armor_yellow,	
		itm_clone_trooper_gloves_yellow,
		itm_clone_trooper_gloves_yellow,
		itm_clone_trooper_boots,
		itm_clone_trooper_boots,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_blue_rifle,
		itm_laser_bolts_blue_rifle,
		#itm_dc15s,
		#itm_dc15s,
		itm_dc15a,
		itm_dc15a_hip,
		itm_dc15a_hip
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_4,
	mandalorian_face1, mandalorian_face2
],
["arc_trooper_5","Arc Trooper Commander","Arc Trooper Commanders",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_commoners,
	[   
		#itm_clone_trooper_head,
		#itm_clone_trooper_head,
		itm_clone_trooper_helmet_yellow,
		itm_clone_trooper_helmet_yellow,
		itm_arc_trooper_armor_yellow,
		itm_arc_trooper_armor_yellow,	
		itm_clone_trooper_gloves_yellow,
		itm_clone_trooper_gloves_yellow,
		itm_clone_trooper_boots,
		itm_clone_trooper_boots,
		itm_combat_knife,
		itm_combat_knife,
		itm_laser_bolts_blue_rifle,
		itm_laser_bolts_blue_rifle,
		#itm_dc15s,
		#itm_dc15s,
		itm_dc15a,
		itm_dc15a_hip,
		itm_dc15a_hip
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(160),
	starwars_skills_4,
	mandalorian_face1, mandalorian_face2
],

# rancor
["rancor","Baby Rancor","Baby Rancors",
	tf_gamorrean|tf_guarantee_all_armor,		# used tf_gamorrean sounds  since we have a limit of races in module_skins.py
	no_scene,0,fac_commoners,
	[
		itm_rancor_body_a,
		itm_rancor_body_a,
		itm_rancor_body_a,
		itm_rancor_body_b,
		itm_rancor_body_b,		
		itm_rancor_body_c,
		itm_transparent_head,
		itm_transparent_hands,
		itm_transparent_feet,
		itm_rancor_attack
	],
	str_16|agi_8|int_3|cha_3|level(35),
	wp(175),
	knows_ironflesh_8|knows_power_strike_8|knows_weapon_master_8|knows_shield_2|knows_tactics_2|knows_leadership_2,
	sw_man_face_1, sw_man_face_2
],

######################################################################
# droids primarily used as town_walkers or prisoners

# 3poseries droid
["3poseries","3PO-Series Droid","3PO-Series Droids",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_3poseries_attack,
		itm_transparent_head,
		itm_transparent_hands,
		itm_transparent_feet,		
		itm_3poseries_gold,
		itm_3poseries_gold,
		itm_3poseries_blue,
		itm_3poseries_red,
		itm_3poseries_grey,
		itm_3poseries_grey
		#itm_q2,
		#itm_q2,
		#itm_laser_bolts_orange,
		#itm_laser_bolts_orange
	],
	droid_attrib_2|level(25),
	wp(60),
	droid_skills_2,
	droid_face1, droid_face2
],

# r2series droid
["r2series","R2-Series Droid","R2-Series Droids",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_droid_weapon_no_attack,
		itm_transparent_droid_head,
		itm_transparent_droid_hands,
		itm_transparent_droid_feet,	
		itm_r2series_blue,
		itm_r2series_green,		
		itm_r2series_orange,
		#itm_r2series_purple,
		itm_r2series_blue,
		itm_r2series_green,		
		itm_r2series_orange,
		itm_r2series_purple		
	],
	droid_attrib_2|level(25),
	wp(40),
	droid_skills_2,
	droid_face1, droid_face2
],

#power_droid
#["power_droid","EG-6 Power Droid","EG-6 Power Droids",
["power_droid","EG-Series Power Droid","EG-Series Power Droids",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_droid_weapon_no_attack,
		itm_transparent_droid_head,
		itm_transparent_droid_hands,
		itm_transparent_droid_feet,	
		#itm_power_droid_legs,
		itm_power_droid_tan,
		itm_power_droid_tan,
		itm_power_droid_grey,
		itm_power_droid_grey,
		itm_power_droid_snow
		#itm_power_droid_snow
	],
	droid_attrib_2|level(24),
	wp(40),
	droid_skills_2,
	droid_face1, droid_face2
],

#power_droid
#["power_droid","EG-6 Power Droid","EG-6 Power Droids",
["fxseries_droid","FX-Series Medical Droid","FX-Series Medical Droids",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_droid_weapon_no_attack,
		itm_transparent_droid_head,
		itm_transparent_droid_hands,
		itm_transparent_droid_feet,	
		itm_fxseries_droid_armor,
		itm_fxseries_droid_armor
	],
	droid_attrib_2|level(32),
	wp(60),
	droid_skills_2,
	droid_face1, droid_face2
],

# r2series droid
["lin_droid","LIN Droid","LIN Droids",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_droid_weapon_no_attack,
		itm_transparent_droid_head,
		itm_transparent_droid_hands,
		itm_transparent_droid_feet,	
		itm_lin_droid_armor,
		itm_lin_droid_armor,
		itm_lin_droid_armor_w_arm
	],
	droid_attrib_2|level(20),
	wp(30),
	droid_skills_2,
	droid_face1, droid_face2
],

# mse6 droid
["mse6","MSE-Series Droid","MSE-Series Droids",
	tf_droid|tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_commoners,
	[
		itm_droid_parts,
		itm_droid_weapon_no_attack,
		itm_transparent_droid_head,
		itm_transparent_droid_hands,
		itm_transparent_droid_feet,	
		itm_mse6_armor
	],
	droid_attrib_1|level(15),
	wp(20),
	droid_skills_1,
	droid_face1, droid_face2
],

###################################################################################
#SW - special culture specific troops
#human
["human_messenger","Messenger","Messengers",
	tf_mounted|tf_guarantee_all_armor|tf_guarantee_horse|tf_guarantee_ranged,
	0,0,fac_neutral,
	[itm_speeder,itm_outfit_grey,itm_black_boots,itm_black_gloves,itm_eyepiece_tactics,itm_a280,itm_laser_bolts_yellow_rifle,itm_westar_shield,itm_vibro_sword3_gold],
	def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,sw_man_face_1, sw_man_face_2
],
["human_deserter","Deserter","Deserters",
	tf_guarantee_boots|tf_guarantee_all_armor,
	0,0,fac_neutral,
	[itm_outfit_grey,itm_black_boots,itm_black_gloves,itm_westar,itm_laser_bolts_yellow_pistol,itm_combat_knife],
	def_attrib_2|level(16),wp(80),starwars_skills_2,sw_man_face_1, sw_man_face_2
],
#wookiee
["wookiee_messenger","Wookiee Messenger","Wookiee Messengers",
	tf_wookiee|tf_mounted|tf_guarantee_all_armor|tf_guarantee_horse|tf_guarantee_ranged,
	0,0,fac_neutral,
	[itm_speeder,itm_ryyk_blade,itm_wookiee_bowcaster,itm_wookiee_armor2,itm_wookiee_armor1,itm_laser_bolts_green_rifle,itm_wookiee_shield_large,itm_transparent_helmet,itm_wookiee_fur],
	def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,wookiee_face1, wookiee_face2
],
["wookiee_deserter","Wookiee Deserter","Wookiee Deserters",
	tf_wookiee|tf_guarantee_boots|tf_guarantee_armor,
	0,0,fac_neutral,
	[itm_ryyk_blade,itm_wookiee_bowcaster,itm_wookiee_armor2,itm_wookiee_armor1,itm_laser_bolts_green_rifle,itm_wookiee_shield_large,itm_transparent_helmet,itm_wookiee_fur],
	def_attrib_2|level(16),wp(80),starwars_skills_2,wookiee_face1, wookiee_face2
],
#mandalorian
["mandalorian_messenger","Mandalorian Messenger","Mandalorian Messengers",
	tf_mounted|tf_guarantee_all_armor|tf_guarantee_horse|tf_guarantee_ranged,
	0,0,fac_neutral,
	[itm_speeder_hutt,itm_mandalorian_crusader_helmet,itm_mandalorian_neocrusader_helmet,itm_mandalorian_crusader_armor,itm_mandalorian_crusader_boots,itm_grey_gloves,itm_combat_knife,itm_laser_bolts_orange_rifle,itm_mandalorian_heavy_blaster,itm_westar_shield],
	def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,mandalorian_face1, mandalorian_face2
],
["mandalorian_deserter","Mandalorian Deserter","Mandalorian Deserters",
	tf_guarantee_boots|tf_guarantee_all_armor,
	0,0,fac_neutral,
	[itm_mandalorian_crusader_helmet,itm_mandalorian_neocrusader_helmet,itm_mandalorian_crusader_armor,itm_mandalorian_crusader_boots,itm_grey_gloves,itm_combat_knife,itm_laser_bolts_orange_rifle,itm_mandalorian_heavy_blaster],
	def_attrib_2|level(16),wp(80),starwars_skills_2,mandalorian_face1, mandalorian_face2
],
#clone
["clone_messenger","Clone Messenger","Clone Messengers",
	tf_mounted|tf_guarantee_all_armor|tf_guarantee_horse|tf_guarantee_ranged,
	0,0,fac_neutral,
	[itm_speeder,itm_clone_trooper_helmet_red,itm_clone_trooper_armor_red,itm_clone_trooper_gloves_red,itm_clone_trooper_boots,itm_combat_knife,itm_laser_bolts_blue_rifle,itm_dc15a],
	def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,mandalorian_face1, mandalorian_face2
],
["clone_deserter","Clone Deserter","Clone Deserters",
	tf_guarantee_boots|tf_guarantee_all_armor,
	0,0,fac_neutral,
	[itm_clone_trooper_helmet_white,itm_clone_trooper_armor_white,itm_clone_trooper_gloves_white,itm_clone_trooper_boots,itm_combat_knife,itm_laser_bolts_blue_rifle,itm_dc15s],
	def_attrib_2|level(16),wp(80),starwars_skills_2,mandalorian_face1, mandalorian_face2
],
["trandoshan_messenger","Trandoshan Messenger","Trandoshan Messengers",
	tf_trandoshan|tf_mounted|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,
	0,0,fac_neutral,
	[itm_speeder,itm_transparent_helmet,itm_trandoshan_blade,itm_laser_bolts_orange_rifle,itm_trandoshan_acp_array_gun,itm_trandoshan_armor,itm_trandoshan_flight_suit,itm_trandoshan_skin],
	def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,wookiee_face1, wookiee_face2
],
["trandoshan_deserter","Trandoshan Deserter","Trandoshan Deserters",
	tf_trandoshan|tf_guarantee_boots|tf_guarantee_armor,
	0,0,fac_neutral,
	[itm_transparent_helmet,itm_trandoshan_blade,itm_laser_bolts_orange_rifle,itm_trandoshan_acp_array_gun,itm_trandoshan_armor,itm_trandoshan_flight_suit,itm_trandoshan_skin],
	def_attrib_2|level(16),wp(80),starwars_skills_2,wookiee_face1, wookiee_face2
],
###################################################################################

#SW BSG integration - player_inactive for BSG integration (nevermind, not used)
#  ["player_inactive","Player","Player",tf_hero|tf_unmoveable_in_party_window|tf_inactive,no_scene,reserved,fac_player_faction,	
#   [],str_4|agi_4|int_4|cha_4,wp(25)|wp_firearm(50)|wp_throwing(35),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  
["force_sensitive_recruit","Force-Sensitive","Force-Sensitives",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
	[
		itm_tunic_white,
		itm_tunic_white,
		itm_leather_boots,
		itm_leather_boots,
		itm_vibro_sword3_red,
		itm_vibro_sword3_blue,
		itm_stun_beam_pistol,
		itm_stun_beam_pistol,
		itm_q2_stun,
		itm_q2_stun,
		itm_westar_stun,
		itm_westar_stun
	],
	def_attrib_force_1|level(6),
	wp(60)|wp_archery(70),
	starwars_skills_force_1,
	sw_imperial_face_1, sw_imperial_face_2
],  
  
#================================================================================================================================	
#SW - kingdom_1 troops	
#SW - Galactic Empire Soldiers (removed tf_guarantee_ranged from sith apprentice/master/lord so they will be part of the infantry group and can be given separate battle commands)
["imperial_recruit","Imperial Recruit","Imperial Recruits",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
	[
		itm_imperial_trooper_armor,
		itm_imperial_trooper_armor,
		itm_black_boots,
		itm_black_boots,
		itm_imperial_hat_black,
		itm_imperial_hat_black,
		itm_melee_punch,
		itm_laser_bolts_red_pistol,
		itm_laser_bolts_red_pistol,
		itm_q2,
		itm_q2,
		itm_westar,
		itm_westar
	],
	def_attrib_1|level(6),
	wp(60)|wp_firearm(70),
	starwars_skills_1,
	sw_imperial_face_1,	sw_imperial_face_2
],

# ["imperial_cadet","Imperial Cadet","Imperial Cadets",
	# tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
	# no_scene,reserved,fac_neutral,
	# [
		# itm_imperial_trooper_armor,
		# itm_imperial_trooper_armor,
		# itm_black_boots,
		# itm_black_boots,
		# itm_imperial_hat_black,
		# itm_imperial_hat_black,
		# itm_melee_punch,
		# itm_laser_bolts_red,
		# itm_laser_bolts_red,
		# itm_q2,
		# itm_q2,
		# itm_westar,
		# itm_westar
	# ],
	# def_attrib_1|level(8),
	# wp(70)|wp_firearm(80),
	# starwars_skills_1,
	# sw_imperial_face_1,	sw_imperial_face_2
# ],

#SW - sith troop tree
["sith_hopeful","Sith Hopeful","Sith Hopefuls",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
	[
		itm_tunic_blue,
		itm_tunic_blue,
		itm_black_boots,
		itm_black_boots,
		itm_vibro_sword3_blue,
		itm_vibro_sword3_blue,
		itm_laser_bolts_red_pistol,
		itm_laser_bolts_red_pistol,
		itm_q2,
		itm_q2,
		itm_westar,
		itm_westar
	],
	def_attrib_force_1|level(10),
	wp(100)|wp_archery(120),
	starwars_skills_force_1,
	sw_imperial_face_1, sw_imperial_face_2
],
["sith_acolyte","Sith Acolyte","Sith Acolytes",
	tf_guarantee_boots|tf_guarantee_armor,
	no_scene,reserved,fac_neutral,
	[
		itm_sith_acolyte_outfit,
		itm_sith_acolyte_outfit,
		itm_black_boots_reinforced,
		itm_black_boots_reinforced,
		itm_vibro_sword3_blue,
		itm_vibro_sword3_blue,
		itm_force_power_ds_1,
		itm_force_power_ds_1,
		itm_force_lightning_ammo,
		itm_force_lightning_ammo
	],
	def_attrib_force_2|level(14),
	wp(130)|wp_archery(150),
	starwars_skills_force_2,
	sw_imperial_face_1,	sw_imperial_face_2
],
["sith_apprentice","Sith Apprentice","Sith Apprentices",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
	no_scene,0,fac_neutral,
	[
		itm_sith_apprentice_outfit,
		itm_sith_apprentice_outfit,
		itm_black_boots_reinforced,
		itm_black_boots_reinforced,
		itm_lightsaber_red_1h,
		itm_lightsaber_red_1h,
		itm_force_block,
		itm_force_block,
		itm_force_power_ds_2,
		itm_force_power_ds_2,
		itm_force_lightning_ammo,
		itm_force_lightning_ammo
	],
	def_attrib_force_2|level(18),
	wp(160)|wp_archery(180),
	starwars_skills_force_2,
	sw_imperial_face_1, sw_imperial_face_2
],
["sith_knight","Sith Knight","Sith Knights",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
	no_scene,0,fac_neutral,
	[   #itm_sith_hood_unique,
		#itm_sith_hood_unique,
		itm_transparent_helmet,
		itm_sith_knight_robe_unique,
		itm_sith_knight_robe_unique,
		itm_black_gloves,
		itm_black_gloves,
		itm_black_boots_reinforced,
		itm_black_boots_reinforced,
		itm_lightsaber_red_1h,
		itm_lightsaber_red_1h,
		itm_lightsaber_red,
		itm_lightsaber_red,
		itm_force_shield,
		itm_force_shield,
		itm_lightsaber_block_red,
		itm_lightsaber_block_red,
		itm_force_power_ds_3,
		itm_force_power_ds_3,
		itm_force_lightning_ammo,
		itm_force_lightning_ammo,
		itm_force_throw_lightsaber_red,
		itm_force_throw_lightsaber_red
	],
	def_attrib_force_3|level(22),
	wp(190)|wp_archery(210),
	starwars_skills_force_3,
	sw_imperial_face_1, sw_imperial_face_2
],
["sith_marauder","Sith Marauder","Sith Marauders",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,0,fac_neutral,
	[	itm_sith_hood_unique,
		itm_sith_hood_unique,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_sith_marauder_robe_unique,
		itm_sith_marauder_robe_unique,
		itm_black_gloves,
		itm_black_gloves,
		itm_black_boots_reinforced,
		itm_black_boots_reinforced,
		itm_lightsaber_red,
		itm_lightsaber_red,
		itm_force_shield,
		itm_force_shield,
		itm_force_protect,
		itm_force_protect,
		itm_lightsaber_block_red,
		itm_lightsaber_block_red,
		itm_force_power_ds_3,
		itm_force_power_ds_3,
		itm_force_lightning_ammo,
		itm_force_lightning_ammo,
		itm_force_throw_lightsaber_red,
		itm_force_throw_lightsaber_red
	],
	def_attrib_force_3|level(28),
	wp(220)|wp_archery(240),
	starwars_skills_force_3,
	sw_sith_face_1, sw_sith_face_2
],
["sith_master","Sith Master","Sith Masters",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
	no_scene,0,fac_neutral,
	[	itm_sith_hood_unique,
		itm_sith_hood_unique,
		itm_transparent_helmet,
		#itm_transparent_helmet,
		itm_sith_master_robe_unique,
		itm_sith_master_robe_unique,
		itm_black_gloves,
		itm_black_gloves,
		itm_black_boots_reinforced,
		itm_black_boots_reinforced,
		itm_lightsaber_red,
		itm_lightsaber_red,
		itm_force_protect,
		itm_force_protect,
		itm_force_power_ds_4,
		itm_force_power_ds_4,
		itm_force_lightning_ammo,
		itm_force_lightning_ammo,
		itm_force_throw_lightsaber_red,
		itm_force_throw_lightsaber_red
	],
	def_attrib_force_4|level(35),
	wp(250)|wp_archery(270),
	starwars_skills_force_4,
	sw_sith_face_1, sw_sith_face_2
],
["sith_lord","Sith Lord","Sith Lords",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
	no_scene,0,fac_neutral,
	[	itm_sith_hood_unique,
		itm_sith_hood_unique,
		#itm_transparent_helmet,
		itm_sith_master_robe_unique,
		itm_sith_master_robe_unique,
		itm_black_gloves,
		itm_black_gloves,
		itm_black_boots_reinforced,
		itm_black_boots_reinforced,
		itm_lightsaber_red,
		itm_lightsaber_red,
		itm_force_protect,
		itm_force_protect,
		itm_force_power_ds_4,
		itm_force_power_ds_4,
		itm_force_lightning_ammo,
		itm_force_lightning_ammo,
		itm_force_throw_lightsaber_red,
		itm_force_throw_lightsaber_red
	],
	def_attrib_force_4|level(42),
	wp(280)|wp_archery(300),
	starwars_skills_force_4,
	sw_sith_face_1, sw_sith_face_2
],
#SW - imperial troop tree      

["imperial_navy_trooper","Imperial Navy Trooper","Imperial Navy Troopers",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
	[
		itm_imperial_navy_trooper_armor,
		itm_imperial_navy_trooper_armor,
		itm_black_boots,
		itm_black_boots,
		itm_black_gloves_long,
		itm_black_gloves_long,
		itm_imperial_navy_trooper_helmet,
		itm_imperial_navy_trooper_helmet,
		itm_melee_punch,
		itm_laser_bolts_red_pistol,
		itm_laser_bolts_red_pistol,
		itm_dh17,
		itm_dh17
	],
	def_attrib_1|level(10),
	wp(85)|wp_firearm(95),
	starwars_skills_1,
	sw_imperial_face_1, sw_imperial_face_2
],

["imperial_army_trooper","Imperial Army Trooper","Imperial Army Troopers",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
	[
		itm_imperial_trooper_armor,
		itm_imperial_trooper_armor,
		itm_black_boots,
		itm_black_boots,
		itm_black_gloves_long,
		itm_black_gloves_long,
		itm_imperial_trooper_helmet,
		itm_imperial_trooper_helmet,
		itm_melee_punch,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_e11,
		itm_e11_hip,
		itm_ee3
	],
	def_attrib_1|level(10),
	wp(85)|wp_crossbow(95),
	starwars_skills_1,
	sw_imperial_face_1, sw_imperial_face_2
],

["imperial_gunner","Imperial Gunner","Imperial Gunners",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_neutral,
	[
		itm_imperial_uniform_black_plain,
		itm_imperial_uniform_black_plain,
		itm_black_boots,
		itm_black_boots,
		itm_black_gloves_long,
		itm_black_gloves_long,
		itm_imperial_gunner_helmet,
		itm_imperial_gunner_helmet,
		itm_baton,
		itm_baton,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_dlt19,
		itm_t21
	],
	def_attrib_2|level(16),
	wp(95)|wp_crossbow(110),
	starwars_skills_2,
	sw_imperial_face_1, sw_imperial_face_2
],

["imperial_stormtrooper","Imperial Stormtrooper","Imperial Stormtroopers",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_neutral,
	[
		itm_imperial_stormtrooper_armor,
		itm_imperial_stormtrooper_armor,
		itm_imperial_stormtrooper_helmet,
		itm_imperial_stormtrooper_helmet,
		itm_imperial_stormtrooper_boots,
		itm_imperial_stormtrooper_boots,
		itm_imperial_stormtrooper_gloves,
		itm_imperial_stormtrooper_gloves,
		itm_baton,
		itm_baton,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_e11_hip,
		itm_e11_hip,
		itm_e11
	],
	def_attrib_2|level(16),
	wp(95)|wp_crossbow(110),
	starwars_skills_2,
	sw_imperial_face_1, sw_imperial_face_2
],
["imperial_pilot","Imperial Pilot","Imperial Pilots",
	tf_mounted|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
	no_scene,0,fac_neutral,
	[
		itm_speeder_shadow,
		itm_speeder_shadow,
		itm_imperial_pilot_helmet,
		itm_imperial_pilot_helmet,
		itm_imperial_uniform_black_plain,
		itm_imperial_uniform_black_plain,
		itm_black_boots,
		itm_black_boots,
		itm_black_gloves_long,
		itm_black_gloves_long,
		itm_baton,
		itm_baton,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_e11_hip,
		itm_e11
	],
	def_attrib_2|level(16),
	wp(85)|wp_crossbow(100),
	starwars_skills_mounted_2,
	sw_imperial_face_1, sw_imperial_face_2
],
["imperial_scout_trooper","Imperial Scout Trooper","Imperial Scout Troopers",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,0,fac_neutral,
	[
		itm_imperial_scout_trooper_armor,
		itm_imperial_scout_trooper_armor,
		itm_imperial_scout_trooper_helmet,
		itm_imperial_scout_trooper_helmet,
		itm_imperial_scout_trooper_boots,
		itm_imperial_scout_trooper_boots,
		itm_black_gloves_long,
		itm_black_gloves_long,
		itm_baton,
		itm_baton,
		itm_laser_bolts_red_pistol,
		itm_laser_bolts_red_pistol,
		itm_scout_trooper_pistol,
		itm_scout_trooper_pistol
	],
	def_attrib_2|level(16),
	wp(85)|wp_firearm(100),
	starwars_skills_2,
	sw_imperial_face_1, sw_imperial_face_2
],
["imperial_gunner_veteran","Veteran Imperial Gunner","Veteran Imperial Gunners",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
	[
		itm_imperial_uniform_black_plain,
		itm_imperial_uniform_black_plain,
		itm_black_boots,
		itm_black_boots,
		itm_black_gloves_long,
		itm_black_gloves_long,
		itm_imperial_gunner_helmet,
		itm_imperial_gunner_helmet,
		itm_baton,
		itm_baton,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_dlt19,
		itm_t21
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(150),
	starwars_skills_3,
	sw_imperial_face_1, sw_imperial_face_2
],
["imperial_stormtrooper_veteran","Veteran Imperial Stormtrooper","Veteran Imperial Stormtroopers",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
	[	
		itm_imperial_stormtrooper_armor,
		itm_imperial_stormtrooper_armor,
		itm_imperial_stormtrooper_helmet,
		itm_imperial_stormtrooper_helmet,
		itm_imperial_stormtrooper_boots,
		itm_imperial_stormtrooper_boots,
		itm_imperial_stormtrooper_gloves,
		itm_imperial_stormtrooper_gloves,
		itm_baton,
		itm_baton,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_dlt19,
		itm_dlt20a,
		itm_e11_hip,
		itm_e11_hip,
		itm_e11
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(150),
	starwars_skills_3,
	sw_imperial_face_1, sw_imperial_face_2
],
["imperial_pilot_veteran","Imperial Ace Pilot","Imperial Ace Pilots",
	tf_mounted|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
	no_scene,reserved,fac_neutral,
	[
		itm_speeder_shadow,
		itm_speeder_shadow,
		itm_imperial_pilot_helmet,
		itm_imperial_pilot_helmet,
		itm_imperial_uniform_black_plain,
		itm_imperial_uniform_black_plain,
		itm_black_boots,
		itm_black_boots,
		itm_black_gloves_long,
		itm_black_gloves_long,
		itm_baton,
		itm_baton,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_e11_hip,
		itm_e11
	],
	def_attrib_3|level(24),
	wp(125)|wp_crossbow(140),
	starwars_skills_mounted_3,
	sw_imperial_face_1, sw_imperial_face_2
],
["imperial_scout_trooper_veteran","Veteran Imperial Scout Trooper","Veteran Imperial Scout Troopers",
	tf_mounted|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
	no_scene,reserved,fac_neutral,
	[
		itm_speeder_imperial,
		itm_speeder_imperial,
		itm_imperial_scout_trooper_armor,
		itm_imperial_scout_trooper_armor,
		itm_imperial_scout_trooper_helmet,
		itm_imperial_scout_trooper_helmet,
		itm_imperial_scout_trooper_boots,
		itm_imperial_scout_trooper_boots,
		itm_black_gloves_long,
		itm_black_gloves_long,
		itm_baton,
		itm_baton,
		itm_laser_bolts_red_pistol,
		itm_laser_bolts_red_pistol,
		itm_scout_trooper_pistol,
		itm_scout_trooper_pistol
	],
	def_attrib_3|level(24),
	wp(125)|wp_firearm(140),
	starwars_skills_mounted_3,
	sw_imperial_face_1, sw_imperial_face_2
],
["imperial_scout_trooper_marksman","Imperial Scout Marksman","Imperial Scout Marksmen",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
	[
		itm_imperial_scout_trooper_armor,
		itm_imperial_scout_trooper_armor,
		itm_imperial_scout_trooper_helmet,
		itm_imperial_scout_trooper_helmet,
		itm_imperial_scout_trooper_boots,
		itm_imperial_scout_trooper_boots,
		itm_black_gloves_long,
		itm_black_gloves_long,
		itm_vibro_blade1,
		itm_vibro_blade2,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_dlt19_scope,
		itm_dlt19_scope
],
	def_attrib_3|level(24),
	wp(125)|wp_crossbow(140),
	starwars_skills_3,
	sw_imperial_face_1, sw_imperial_face_2
],

["imperial_scout_trooper_captain","Imperial Scout Trooper Captain","Imperial Scout Trooper Captains",
	tf_mounted|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
	no_scene,reserved,fac_neutral,
	[
		itm_speeder_imperial,
		itm_speeder_imperial,
		itm_imperial_scout_trooper_armor,
		itm_imperial_scout_trooper_armor,
		itm_imperial_scout_trooper_helmet,
		itm_imperial_scout_trooper_helmet,
		itm_imperial_scout_trooper_boots,
		itm_imperial_scout_trooper_boots,
		itm_black_gloves_long,
		itm_black_gloves_long,
		itm_baton,
		itm_baton,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_dlt19,
		itm_dlt20a
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(170),
	starwars_skills_mounted_4,
	sw_imperial_face_1, sw_imperial_face_2
],

["imperial_scout_trooper_sniper","Imperial Scout Sniper","Imperial Scout Snipers",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
	[
		itm_imperial_scout_trooper_armor,
		itm_imperial_scout_trooper_armor,
		itm_imperial_scout_trooper_helmet,
		itm_imperial_scout_trooper_helmet,
		itm_imperial_scout_trooper_boots,
		itm_imperial_scout_trooper_boots,
		itm_black_gloves_long,
		itm_black_gloves_long,
		itm_vibro_blade1,
		itm_vibro_blade2,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_dlt19_scope,
		itm_dlt19_scope
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(170),
	starwars_skills_4,
	sw_imperial_face_1, sw_imperial_face_2
],

# ["imperial_darktrooper","Imperial Dark Trooper","Imperial Dark Troopers",
	# tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,
	# no_scene,reserved,fac_neutral,
	# [itm_imperial_stormtrooper_armor_black,
		# itm_imperial_stormtrooper_armor_black,
		# itm_imperial_stormtrooper_helmet_black,
		# itm_imperial_stormtrooper_helmet_black,
		# itm_black_boots,
		# itm_black_boots,
		# itm_black_gloves,
		# itm_black_gloves,
		# itm_vibro_sword3_gold,
		# itm_vibro_sword3_gold,
		# itm_laser_bolts_red,
		# itm_laser_bolts_red,
		# itm_dlt19,
		# itm_dlt19,
		# itm_e11,
		# itm_e11
	# ],
	# def_attrib_4|level(30),
	# wp(150)|wp_firearm(170),
	# starwars_skills_4,
	# sw_imperial_face_1, sw_imperial_face_2
# ],

["imperial_stormtrooper_officer","Imperial Stormtrooper Officer","Imperial Stormtrooper Officers",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
	[
		itm_imperial_stormtrooper_armor_officer,
		itm_imperial_stormtrooper_armor_officer,
		itm_imperial_stormtrooper_helmet,
		itm_imperial_stormtrooper_helmet,
		itm_imperial_stormtrooper_boots,
		itm_imperial_stormtrooper_boots,
		itm_imperial_stormtrooper_gloves,
		itm_imperial_stormtrooper_gloves,
		itm_baton,
		itm_baton,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_dlt19,
		itm_dlt20a,
		itm_t21,
		itm_t21
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(170),
	starwars_skills_4,
	sw_imperial_face_1, sw_imperial_face_2
],

# ["imperial_shadow_stormtrooper","Imperial Shadow Stormtrooper","Imperial Shadow Stormtrooper",
	# tf_guarantee_all_armor|tf_guarantee_ranged,
	# no_scene,reserved,fac_neutral,
	# [	
		# itm_shadow_stormtrooper_armor,
		# itm_shadow_stormtrooper_armor,
		# itm_shadow_stormtrooper_helmet,
		# itm_shadow_stormtrooper_helmet,
		# itm_shadow_stormtrooper_boots,
		# itm_shadow_stormtrooper_boots,
		# itm_shadow_stormtrooper_gloves,
		# itm_shadow_stormtrooper_gloves,
		# #itm_vibro_blade2,
		# #itm_vibro_blade4,
		# itm_melee_punch,		
		# itm_laser_bolts_red,
		# itm_laser_bolts_red,
		# itm_dlt19,
		# itm_dlt20a,
		# itm_e11,
		# itm_e11
	# ],
	# def_attrib_4|level(30),
	# wp(150)|wp_firearm(170),
	# starwars_skills_4,
	# sw_imperial_face_1, sw_imperial_face_2
# ],

["imperial_royal_guard","Imperial Royal Guard","Imperial Royal Guards",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
	[
		itm_imperial_royal_guard_boots,
		itm_imperial_royal_guard_boots,
		itm_imperial_royal_guard_gloves,
		itm_imperial_royal_guard_gloves,
		itm_imperial_royal_guard_helmet,
		itm_imperial_royal_guard_helmet,
		itm_imperial_royal_guard_robe,
		itm_imperial_royal_guard_robe,
		itm_force_pike,
		itm_force_pike,
		itm_laser_bolts_red_rifle,
		itm_laser_bolts_red_rifle,
		itm_dlt19,
		itm_dlt19
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(170),
	starwars_skills_4,
	sw_imperial_face_1, sw_imperial_face_2
],

# ["imperial_shadow_scout_trooper","Imperial Shadow Scout Trooper","Imperial Shadow Scout Trooper",
	# tf_mounted|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_horse,
	# no_scene,reserved,fac_neutral,
	# [
		# itm_speeder_shadow,
		# itm_speeder_shadow,
		# itm_shadow_scout_trooper_armor,
		# itm_shadow_scout_trooper_armor,
		# itm_shadow_scout_trooper_helmet,
		# itm_shadow_scout_trooper_helmet,
		# itm_shadow_scout_trooper_boots,
		# itm_shadow_scout_trooper_boots,
		# itm_black_gloves_long,
		# itm_black_gloves_long,
		# itm_vibro_sword3_gold,
		# itm_vibro_sword3_gold,
		# itm_laser_bolts_red,
		# itm_laser_bolts_red,
		# itm_dlt19,
		# itm_dlt20a
	# ],
	# def_attrib_4|level(35),
	# wp(175)|wp_firearm(200),
	# starwars_skills_mounted_4,
	# sw_imperial_face_1, sw_imperial_face_2
# ],

["imperial_messenger","Imperial Messenger","Imperial Messengers",
	tf_mounted|tf_guarantee_all_armor|tf_guarantee_horse|tf_guarantee_ranged,
	0,0,fac_neutral,
	[itm_speeder_imperial,itm_imperial_scout_trooper_armor,itm_imperial_scout_trooper_helmet,itm_imperial_scout_trooper_boots,itm_black_gloves,itm_laser_bolts_red_pistol,itm_scout_trooper_pistol,itm_baton],
	def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,sw_imperial_face_1, sw_imperial_face_2
],
["imperial_deserter","Imperial Deserter","Imperial Deserters",
	tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,
	0,0,fac_deserters,
	[itm_imperial_stormtrooper_armor,itm_imperial_scout_trooper_armor,itm_black_boots,itm_laser_bolts_red_pistol,itm_laser_bolts_red_pistol,itm_q2,itm_westar,itm_melee_punch],
	def_attrib_2|level(16),wp(80),starwars_skills_2,sw_imperial_face_1, sw_imperial_face_2
],

#================================================================================================================================
#SW - kingdom_2 troops
#SW - rebel alliance soldiers (removed tf_guarantee_ranged from jedi padawan/knight/master so they will be part of the infantry group and can be given separate battle commands)
["rebel_recruit","Rebel Recruit","Rebel Recruits",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
    [
		itm_rebel_technician_armor,
		itm_rebel_technician_armor,		
		itm_black_boots,
		itm_black_boots,
		itm_melee_punch,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,
		itm_q2,
		itm_q2,
		itm_westar,
		itm_westar
	],
	def_attrib_1|level(6),
	wp(60)|wp_firearm(70),
	starwars_skills_1,
	sw_rebel_face_1, sw_rebel_face_2
],
#SW - jedi upgrade tree
["jedi_hopeful","Jedi Hopeful","Jedi Hopefuls",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
	[
		itm_tunic_red,
		itm_tunic_red,
		itm_leather_boots,
		itm_leather_boots,
		itm_vibro_sword3_red,
		itm_vibro_sword3_red,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,
		itm_q2,
		itm_q2,
		itm_westar,
		itm_westar
	],
	def_attrib_force_1|level(10),
	wp(100)|wp_archery(120),
	starwars_skills_force_1,
	sw_rebel_face_1, sw_rebel_face_2
],
["jedi_initiate","Jedi Initiate","Jedi Initiates",
	tf_guarantee_boots|tf_guarantee_armor,
	no_scene,reserved,fac_neutral,
	[
		itm_jedi_initiate_robe,
		itm_jedi_initiate_robe,
		itm_leather_boots,
		itm_leather_boots,
		itm_vibro_sword3_red,
		itm_vibro_sword3_red,
		itm_force_power_ls_1,
		itm_force_power_ls_1,
		itm_force_push_ammo,
		itm_force_push_ammo
	],
	def_attrib_force_2|level(14),
	wp(130)|wp_archery(150),
	starwars_skills_force_2,
	sw_rebel_face_1, sw_rebel_face_2
],
["jedi_padawan","Jedi Padawan","Jedi Padawans",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
	no_scene,0,fac_neutral,
	[
		itm_jedi_padawan_robe,
		itm_jedi_padawan_robe,
		itm_leather_boots_reinforced,
		itm_leather_boots_reinforced,
		itm_lightsaber_blue_1h,
		itm_lightsaber_green_1h,
		itm_force_block,
		itm_force_block,		
		itm_force_power_ls_2,
		itm_force_power_ls_2,
		itm_force_push_ammo,
		itm_force_push_ammo
	],
	def_attrib_force_2|level(18),
	wp(160)|wp_archery(180),
	starwars_skills_force_2,
	sw_rebel_face_1, sw_rebel_face_2
],
["jedi_guardian","Jedi Guardian","Jedi Guardians",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
	no_scene,0,fac_neutral,
	[	#itm_jedi_knight_hood_unique,
		itm_jedi_knight_hood_unique,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_jedi_knight_robe_unique,
		itm_jedi_knight_robe_unique,
		itm_leather_gloves,
		itm_leather_gloves,
		itm_leather_boots_reinforced,
		itm_leather_boots_reinforced,
		itm_lightsaber_blue,
		itm_lightsaber_blue,		
		itm_force_block,
		itm_force_block,		
		itm_lightsaber_block_blue,
		itm_lightsaber_block_blue,		
		itm_force_throw_lightsaber_blue,
		itm_force_throw_lightsaber_blue
	],
	def_attrib_force_3|level(22),
	wp(190)|wp_archery(210),
	starwars_skills_force_3,
	sw_rebel_face_1, sw_rebel_face_2
],
["jedi_consular","Jedi Consular","Jedi Consulars",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
	no_scene,0,fac_neutral,
	[	itm_jedi_knight_hood_unique,
		itm_jedi_knight_hood_unique,
		itm_transparent_helmet,
		#itm_transparent_helmet,
		itm_jedi_knight_robe_unique,
		itm_jedi_knight_robe_unique,
		itm_leather_gloves,
		itm_leather_gloves,
		itm_leather_boots_reinforced,
		itm_leather_boots_reinforced,
		itm_lightsaber_green,
		itm_lightsaber_green,		
		itm_force_shield,
		itm_force_shield,		
		itm_force_power_ls_3,	#give 3x to increase the chance they get a ranged attack since guarantee_ranged will make them fall into the archer group
		itm_force_power_ls_3,
		itm_force_power_ls_3,
		itm_force_push_ammo,
		itm_force_push_ammo,
		itm_force_push_ammo
	],
	def_attrib_force_3|level(22),
	wp(190)|wp_archery(210),
	starwars_skills_force_3,
	sw_rebel_face_1, sw_rebel_face_2
],
["jedi_warrior_master","Jedi Warrior Master","Jedi Warrior Masters",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
	no_scene,0,fac_neutral,
	[	
		#itm_jedi_master_hood_unique,
		#itm_jedi_master_hood_unique,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_jedi_robe_a_unique,
		itm_jedi_robe_d_unique,
		itm_jedi_robe_e_unique,
		itm_jedi_robe_f_unique,
		#itm_jedi_master_robe_unique,
		#itm_jedi_master_robe_unique,
		itm_leather_gloves,
		itm_leather_gloves,
		itm_leather_boots_reinforced,
		itm_leather_boots_reinforced,
		itm_lightsaber_blue,
		itm_lightsaber_blue,
		itm_force_shield,
		itm_force_shield,		
		itm_lightsaber_block_blue,
		itm_lightsaber_block_blue,
		itm_force_throw_lightsaber_blue,
		itm_force_throw_lightsaber_blue
	],
	def_attrib_force_3|level(28),
	wp(220)|wp_archery(240),
	starwars_skills_force_3,
	sw_rebel_face_1, sw_rebel_face_2
],
["jedi_sage_master","Jedi Sage Master","Jedi Sage Masters",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
	no_scene,0,fac_neutral,
	[	
		#itm_jedi_master_hood_unique,
		#itm_jedi_master_hood_unique,
		itm_transparent_helmet,
		itm_transparent_helmet,
		#itm_jedi_master_robe_unique,
		#itm_jedi_master_robe_unique,
		itm_jedi_robe_a_unique,
		itm_jedi_robe_d_unique,
		itm_jedi_robe_e_unique,
		itm_jedi_robe_f_unique,		
		itm_leather_gloves,
		itm_leather_gloves,
		itm_leather_boots_reinforced,
		itm_leather_boots_reinforced,
		itm_lightsaber_green,
		itm_lightsaber_green,		
		itm_force_shield,
		itm_force_shield,
		itm_force_protect,
		itm_force_protect,		
		itm_force_power_ls_3,	#give 3x to increase the chance they get a ranged attack since guarantee_ranged will make them fall into the archer group
		itm_force_power_ls_3,
		itm_force_power_ls_3,
		itm_force_push_ammo,
		itm_force_push_ammo,
		itm_force_push_ammo
	],
	def_attrib_force_3|level(28),
	wp(220)|wp_archery(240),
	starwars_skills_force_3,
	sw_rebel_face_1, sw_rebel_face_2
],
["jedi_councilor","Jedi Councilor","Jedi Councilors",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_helmet,
	no_scene,0,fac_neutral,
	[	
		itm_jedi_master_hood_unique,
		itm_jedi_master_hood_unique,
		itm_jedi_master_robe_unique,
		itm_jedi_master_robe_unique,
		itm_leather_gloves,
		itm_leather_gloves,
		itm_leather_boots_reinforced,
		itm_leather_boots_reinforced,
		itm_lightsaber_blue,
		itm_lightsaber_green,
		itm_lightsaber_purple,
		itm_force_protect,
		itm_force_protect,
		itm_force_power_ls_4,
		itm_force_power_ls_4,		
		itm_force_push_ammo,
		itm_force_push_ammo,		
		itm_force_throw_lightsaber_blue,
		itm_force_throw_lightsaber_green,
		itm_force_throw_lightsaber_purple
	],
	def_attrib_force_4|level(35),
	wp(250)|wp_archery(270),
	starwars_skills_force_4,
	sw_rebel_face_1, sw_rebel_face_2
],
["jedi_grand_master","Jedi Grand Master","Jedi Grand Masters",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
	no_scene,0,fac_neutral,
	[	
		itm_jedi_master_hood_unique,
		itm_jedi_master_hood_unique,
		itm_jedi_master_robe_unique,
		itm_jedi_master_robe_unique,
		itm_leather_gloves,
		itm_leather_gloves,
		itm_leather_boots_reinforced,
		itm_leather_boots_reinforced,
		itm_lightsaber_blue,
		itm_lightsaber_green,
		itm_lightsaber_purple,
		itm_force_protect,
		itm_force_protect,
		itm_force_power_ls_4,
		itm_force_power_ls_4,		
		itm_force_push_ammo,
		itm_force_push_ammo,
		itm_force_throw_lightsaber_blue,
		itm_force_throw_lightsaber_green,
		itm_force_throw_lightsaber_purple
	],
	def_attrib_force_4|level(42),
	wp(280)|wp_archery(300),
	starwars_skills_force_4,
	sw_rebel_face_1, sw_rebel_face_2
],
#SW - rebel upgrade tree
["rebel_cadet","Rebel Cadet","Rebel Cadets",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
	no_scene,0,fac_neutral,
    [
		itm_rebel_technician_helmet,
		itm_rebel_technician_helmet,
		itm_rebel_technician_armor,
		itm_rebel_technician_armor,		
		itm_black_boots,
		itm_black_boots,
		itm_melee_punch,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,
		itm_westar,
		itm_westar
	],
    def_attrib_1|level(10),
	wp(80)|wp_firearm(90),
	starwars_skills_1,
	sw_rebel_face_1, sw_rebel_face_2
],

["rebel_trooper","Rebel Fleet Trooper","Rebel Fleet Troopers",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
	no_scene,0,fac_neutral,
    [
		itm_republic_trooper_armor,
		itm_republic_trooper_armor,
		itm_rebel_trooper_helmet,
		itm_rebel_trooper_helmet,
		itm_black_boots,
		itm_black_boots,
		itm_grey_gloves,
		itm_black_gloves,
		itm_baton,
		itm_baton,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,
		itm_dh17,
		itm_dh17
	],
    def_attrib_2|level(16),
	wp(95)|wp_firearm(110),
	starwars_skills_2,
	sw_rebel_face_1, sw_rebel_face_2
],

["rebel_scout","Rebel Scout","Rebel Scouts",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,
	no_scene,0,fac_neutral,
    [
		itm_jacket_closed_b,
		itm_vest_closed_b,
		itm_leather_boots,
		itm_leather_boots,
		itm_leather_gloves,
		#itm_leather_gloves,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_a280,
		itm_a280_crouch
	],
    def_attrib_2|level(16),
	wp(95)|wp_crossbow(110),
	starwars_skills_2,
	sw_rebel_face_1, sw_rebel_face_2
],

#["rebel_trooper_veteran","Veteran Rebel Fleet Trooper","Veteran Rebel Fleet Troopers",
["rebel_vanguard","Rebel Vanguard","Rebel Vanguards",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
    [
		itm_republic_trooper_armor,
		itm_republic_trooper_armor,
		itm_rebel_trooper_helmet,
		itm_rebel_trooper_helmet,
		itm_black_boots,
		itm_black_boots,
		itm_black_gloves,
		itm_black_gloves,		
		itm_baton,
		itm_baton,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_a280,
		itm_a280_crouch
	],
    def_attrib_3|level(24),
	wp(135)|wp_firearm(150),
	starwars_skills_3,
	sw_rebel_face_1, sw_rebel_face_2
],

["rebel_pilot","Rebel Pilot","Rebel Pilots",
	tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_horse,
	no_scene,reserved,fac_neutral,
    [
		itm_speeder_rebel,
		itm_speeder_rebel,
		itm_republic_pilot_armor,
		itm_republic_pilot_armor,
		itm_republic_pilot_helmet,
		itm_republic_pilot_helmet,
		itm_black_boots,
		itm_black_boots,
		itm_black_gloves,
		itm_black_gloves,
		itm_baton,
		itm_baton,
		itm_laser_bolts_green_pistol,
		itm_laser_bolts_green_pistol,
		itm_dh17,
		itm_dh17,
		itm_dl44a,
		itm_dl44a
	],
    def_attrib_3|level(24),
	wp(125)|wp_firearm(135),
	starwars_skills_mounted_3,
	sw_rebel_face_1, sw_rebel_face_2
],

["rebel_commando","Rebel Commando","Rebel Commandos",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,
	no_scene,reserved,fac_neutral,
	[
		itm_republic_commando_armor,
		itm_republic_commando_armor,
		itm_republic_commando_helmet,
		itm_republic_commando_helmet,
		itm_leather_boots,
		itm_leather_boots,
		itm_leather_gloves,
		itm_leather_gloves,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_a295,
		itm_a295_crouch
	],
    def_attrib_3|level(24),
	wp(135)|wp_crossbow(150),
	starwars_skills_3,
	sw_rebel_face_1, sw_rebel_face_2
],

["rebel_marksman","Rebel Marksman","Rebel Marksmen",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,
	no_scene,reserved,fac_neutral,
	[
		itm_rebel_sniper_armor,
		itm_rebel_sniper_armor,
		itm_rebel_sniper_helmet,
		itm_rebel_sniper_helmet,
		itm_leather_boots,
		itm_leather_boots,
		itm_leather_gloves,
		itm_leather_gloves,		
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_kisteer_1284,
		itm_dlt19_scope
	],
    def_attrib_3|level(24),
	wp(135)|wp_crossbow(150),
	starwars_skills_3,
	sw_rebel_face_1, sw_rebel_face_2
],

["rebel_honor_guard","Rebel Honor Guard","Rebel Honor Guards",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
    [
		itm_rebel_honor_guard_armor,
		itm_rebel_honor_guard_armor,
		itm_rebel_honor_guard_helmet,
		itm_rebel_honor_guard_helmet,
		itm_leather_boots,
		itm_leather_boots,
		itm_leather_gloves,
		itm_leather_gloves,		
		itm_force_pike,
		itm_force_pike,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_a295,
		itm_a295_crouch
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(170),
	starwars_skills_4,
	sw_rebel_face_1, sw_rebel_face_2
],

["rebel_heavy_trooper","Rebel Heavy Trooper","Rebel Heavy Troopers",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
    [
		itm_rebel_heavy_trooper_armor,
		itm_rebel_heavy_trooper_armor,
		itm_rebel_heavy_trooper_helmet,
		itm_rebel_heavy_trooper_helmet,
		itm_black_boots,
		itm_black_boots,
		itm_grey_gloves,
		itm_grey_gloves,
		itm_baton,
		itm_baton,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_t21,
		itm_t21		
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(170),
	starwars_skills_4,
	sw_rebel_face_1, sw_rebel_face_2
],

["rebel_pilot_veteran","Rebel Ace Pilot","Rebel Ace Pilots",
	tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_horse,
	no_scene,reserved,fac_neutral,
	[
		itm_speeder_rebel,
		itm_speeder_rebel,
		itm_republic_pilot_armor,
		itm_republic_pilot_armor,
		itm_republic_pilot_helmet,
		itm_republic_pilot_helmet,
		itm_black_boots,
		itm_black_boots,
		itm_black_gloves,
		itm_black_gloves,
		itm_baton,
		itm_baton,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_a295,
		itm_a295_crouch
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(135),
	starwars_skills_mounted_4,
	sw_rebel_face_1, sw_rebel_face_2
],

["rebel_commando_veteran","Veteran Rebel Commando","Veteran Rebel Commandos",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,
	no_scene,reserved,fac_neutral,
	[
		itm_republic_commando_armor,
		itm_republic_commando_armor,
		itm_republic_commando_helmet,
		itm_republic_commando_helmet,
		itm_leather_boots,
		itm_leather_boots,
		itm_leather_gloves,
		itm_leather_gloves,
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_a295,
		itm_a295_crouch
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(170),
	starwars_skills_4,
	sw_rebel_face_1, sw_rebel_face_2
],

["rebel_sniper","Rebel Sniper","Rebel Snipers",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,
	no_scene,reserved,fac_neutral,
	[
		itm_rebel_sniper_armor,
		itm_rebel_sniper_armor,
		itm_rebel_sniper_helmet,
		itm_rebel_sniper_helmet,
		itm_leather_boots,
		itm_leather_boots,
		itm_leather_gloves,
		itm_leather_gloves,		
		itm_vibro_blade1,
		itm_vibro_blade3,
		itm_laser_bolts_green_rifle,
		itm_laser_bolts_green_rifle,
		itm_kisteer_1284,
		itm_dlt19_scope
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(170),
	starwars_skills_4,
	sw_rebel_face_1, sw_rebel_face_2
],

["rebel_messenger","Rebel Messenger","Rebel Messengers",
     tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
[itm_speeder_rebel,itm_republic_pilot_armor,itm_republic_pilot_helmet,itm_black_boots,itm_black_gloves,itm_laser_bolts_green_pistol,itm_dh17,itm_baton],
def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,sw_rebel_face_1, sw_rebel_face_2],
["rebel_deserter","Rebel Deserter","Rebel Deserters",
     tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
[itm_republic_trooper_armor,itm_republic_commando_armor,itm_republic_pilot_armor,itm_black_boots,itm_laser_bolts_green_pistol,itm_laser_bolts_green_pistol,itm_q2,itm_westar,itm_melee_punch],
def_attrib_2|level(16),wp(80),starwars_skills_2,sw_rebel_face_1, sw_rebel_face_2],	

#================================================================================================================================
#SW - kingdom_3 troops
#SW - Hutt Cartel soldiers
["hutt_militia","Hutt Militia","Hutt Militias",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged,
	no_scene,reserved,fac_neutral,
	[
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,
		itm_tunic_yellow,
		itm_tunic_yellow,
		itm_hide_boots,
		itm_hide_boots,
		itm_melee_punch,		
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol,
		itm_dl18,
		itm_dl18
	],
	def_attrib_1|level(6),
	wp(60)|wp_firearm(70),
	starwars_skills_1,
	sw_hutt_face_1, sw_hutt_face_2
],
["hutt_mercenary","Hutt Mercenary","Hutt Mercenaries",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged,
	no_scene,0,fac_neutral,
	[
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,	
		itm_tunic_yellow,
		itm_tunic_yellow,
		itm_hide_boots,
		itm_hide_boots,
		itm_vibro_blade1,
		itm_vibro_blade2,
		itm_melee_punch,		
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol,
		itm_ammo_belt_pistol,
		itm_dl18,
		itm_dl18
	],
	def_attrib_1|level(10),
	wp(80)|wp_firearm(90),
	starwars_skills_1,
	sw_hutt_face_1, sw_hutt_face_2
],
["hutt_guard","Hutt Guard","Hutt Guards",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged,
	no_scene,0,fac_neutral,
	[
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,	
		itm_transparent_helmet,
		itm_klatooinian_armor,
		itm_padded_armor_white,
		itm_padded_armor_white,
		itm_hide_boots,
		itm_hide_boots,
		itm_vibro_blade1,
		itm_vibro_blade2,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol,
		itm_ammo_belt_pistol,
		itm_dl18,
		itm_dl18
	],
	def_attrib_2|level(16),
	wp(95)|wp_firearm(110),
	starwars_skills_2,
	sw_hutt_face_1, sw_hutt_face_2
],
["hutt_marksman","Hutt Marksman","Hutt Marksmen",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged,
	no_scene,0,fac_neutral,
	[
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,	
		itm_transparent_helmet,
		itm_mining_helmet,
		itm_pipe_helmet,
		itm_fang_helmet,
		itm_beak_helmet,
		itm_gas_mask,
		itm_armor_blue,
		itm_armor_brown,
		itm_armor_red,
		itm_armor_white,
		#itm_klatooinian_armor,
		itm_klatooinian_armor,
		itm_black_boots,
		itm_black_boots,
		itm_vibro_blade1,
		itm_vibro_blade2,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_ammo_belt_rifle,
		itm_a280,
		itm_a280_crouch
	],
	def_attrib_2|level(16),
	wp(95)|wp_crossbow(110),
	starwars_skills_2,
	sw_hutt_face_1, sw_hutt_face_2
],
["hutt_bounty_hunter","Hutt Bounty Hunter","Hutt Bounty Hunters",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_helmet,
	no_scene,reserved,fac_neutral,
	[	
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,	
		itm_transparent_helmet,
		itm_mining_helmet,
		itm_pipe_helmet,
		itm_fang_helmet,
		itm_beak_helmet,
		itm_gas_mask,
		itm_armor_blue,
		itm_armor_brown,
		itm_armor_red,
		itm_armor_white,
		#itm_klatooinian_armor,
		itm_klatooinian_armor,		
		itm_black_boots,
		itm_black_boots,
		itm_vibro_blade1,
		itm_vibro_blade2,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_ammo_belt_rifle,
		itm_a280,
		itm_a280_crouch
	],
	def_attrib_3|level(24),
	wp(135)|wp_crossbow(150),
	starwars_skills_3,
	sw_hutt_face_1, sw_hutt_face_2
],
["hutt_skiff_guard","Hutt Skiff Guard","Hutt Skiff Guards",
	tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_horse,
	no_scene,reserved,fac_neutral,
	[	
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,	
		itm_transparent_helmet,
		itm_skiff_guard_helmet,
		itm_skiff_guard_helmet,
		itm_skiff_guard_helmet,		
		itm_speeder,
		itm_speeder,
		itm_skiff_guard_armor_brown,
		itm_skiff_guard_armor_grey,
		itm_skiff_guard_armor_white,
		itm_hide_boots,
		itm_hide_boots,
		itm_vibro_axe_long_2h,
		itm_vibro_axe_long_2h,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol,
		itm_ammo_belt_pistol,
		itm_dl18,
		itm_dl18
	],
	def_attrib_3|level(24),
	wp(135)|wp_firearm(150),
	starwars_skills_mounted_3,
	sw_hutt_face_1, sw_hutt_face_2
],
["hutt_palace_guard","Hutt Palace Guard","Hutt Palace Guards",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_helmet,
	no_scene,reserved,fac_neutral,
	[	
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,	
		itm_transparent_helmet,
		itm_mining_helmet,
		itm_pipe_helmet,
		itm_fang_helmet,
		itm_beak_helmet,
		itm_gas_mask,
		itm_hutt_palace_guard_armor,
		itm_hutt_palace_guard_armor,
		itm_klatooinian_armor,
		itm_hide_boots,
		itm_hide_boots,
		itm_vibro_sword3_gold,
		itm_vibro_sword3_gold,
		itm_energy_shield_yellow_small,
		itm_energy_shield_red_small,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol,
		itm_ammo_belt_pistol,
		itm_dl18,
		itm_dl18
	],
	def_attrib_3|level(24),
	wp(135)|wp_firearm(150),
	starwars_skills_melee_3,
	sw_hutt_face_1, sw_hutt_face_2
],
["hutt_commando","Hutt Commando","Hutt Commandos",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_helmet,
	no_scene,reserved,fac_neutral,
	[
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,	
		itm_transparent_helmet,
		itm_mining_helmet,
		itm_pipe_helmet,
		itm_fang_helmet,
		itm_beak_helmet,
		itm_gas_mask,	
		itm_armor_blue,
		itm_armor_brown,
		itm_armor_red,
		itm_armor_white,
		#itm_klatooinian_armor,
		itm_klatooinian_armor,		
		itm_black_boots,
		itm_black_boots,
		itm_vibro_blade1,
		itm_vibro_blade2,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_ammo_belt_rifle,
		itm_a280,
		itm_a280_crouch
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(170),
	starwars_skills_4,
	sw_hutt_face_1, sw_hutt_face_2
],
["hutt_skiff_guard_captain","Hutt Skiff Guard Captain","Hutt Skiff Guard Captains",
	tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_horse,
	no_scene,reserved,fac_neutral,
	[	
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,	
		itm_skiff_guard_helmet,
		itm_skiff_guard_helmet,
		itm_skiff_guard_helmet,
		#itm_transparent_helmet,
		itm_speeder_hutt,
		itm_speeder_hutt,
		itm_skiff_guard_armor_brown,
		itm_skiff_guard_armor_grey,
		itm_skiff_guard_armor_white,
		itm_hide_boots,
		itm_hide_boots,
		itm_vibro_axe_long_2h,
		itm_vibro_axe_long_2h,
		itm_laser_bolts_orange_rifle,
		itm_laser_bolts_orange_rifle,
		itm_ammo_belt_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_a295,
		itm_a295_crouch
	],
	def_attrib_4|level(30),
	wp(150)|wp_crossbow(170),
	starwars_skills_mounted_4,
	sw_hutt_face_1, sw_hutt_face_2
],
["hutt_palace_guard_captain","Hutt Palace Guard Captain","Hutt Palace Guard Captains",
	tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_helmet,
	no_scene,reserved,fac_neutral,
	[
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,	
		itm_transparent_helmet,
		itm_mining_helmet,
		itm_pipe_helmet,
		itm_fang_helmet,
		itm_beak_helmet,
		itm_gas_mask,
		itm_hutt_palace_guard_armor,
		itm_hutt_palace_guard_armor,
		itm_klatooinian_armor,
		itm_hide_boots,
		itm_hide_boots,
		itm_vibro_sword3_gold,
		itm_vibro_sword3_gold,
		itm_energy_shield_yellow_medium,
		itm_energy_shield_yellow_medium,
		itm_energy_shield_red_medium,
		itm_laser_bolts_orange_pistol,
		itm_laser_bolts_orange_pistol,
		itm_ammo_belt_pistol,
		itm_dl44a,
		itm_dl44a
	],
	def_attrib_4|level(30),
	wp(150)|wp_firearm(170),
	starwars_skills_melee_4,
	sw_hutt_face_1, sw_hutt_face_2
],

["hutt_messenger","Hutt Messenger","Hutt Messengers",
     tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
[itm_skiff_guard_helmet,itm_speeder_hutt,itm_skiff_guard_armor_white,itm_skiff_guard_armor_brown,itm_skiff_guard_armor_grey,itm_hide_boots,itm_laser_bolts_orange_pistol,itm_dl18,itm_vibro_axe_long_2h],
def_attrib_4|agi_21|level(30),wp(150),starwars_skills_mounted_4,sw_hutt_face_1, sw_hutt_face_2],
["hutt_deserter","Hutt Deserter","Hutt Deserters",
     tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_deserters,
[itm_klatooinian_armor,itm_weequay_head_helmet_a,itm_weequay_head_helmet_b,itm_klatooinian_head_helmet_a,itm_leather_gloves,itm_black_gloves,itm_transparent_helmet,itm_mining_helmet,itm_pipe_helmet,itm_fang_helmet,itm_beak_helmet,itm_gas_mask,itm_skiff_guard_helmet,itm_skiff_guard_armor_brown,itm_skiff_guard_armor_white,itm_skiff_guard_armor_grey,itm_tunic_yellow,itm_padded_armor_white,itm_armor_blue,itm_armor_brown,itm_armor_red,itm_armor_white,itm_hutt_palace_guard_armor,itm_hide_boots,itm_laser_bolts_orange_pistol,itm_laser_bolts_orange_pistol,itm_q2,itm_westar,itm_vibro_blade1,itm_vibro_blade2],
def_attrib_4|level(16),wp(80),starwars_skills_2,sw_hutt_face_1, sw_hutt_face_2],

#================================================================================================================================   

["looter","Jawa","Jawas",
	tf_jawa|tf_guarantee_all_armor,
	0,0,fac_outlaws,
	[
		itm_jawa_hood,
		itm_jawa_robe,
		itm_jawa_boots,
		itm_leather_gloves,
		itm_leather_gloves,		
		itm_melee_punch,
		itm_ion_beam_pistol,
		itm_ion_beam_pistol,		
		itm_ion_pistol,
		itm_ion_pistol
	],
	def_attrib|level(8),
	wp(80),
	starwars_skills_outlaws_1,
	jawa_face1, jawa_face2
],
["looter_2","Jawa Scavenger","Jawa Scavengers",
	tf_jawa|tf_guarantee_all_armor,
	0,0,fac_outlaws,
	[
		itm_jawa_hood,
		itm_jawa_robe,
		itm_jawa_boots,
		itm_leather_gloves,
		itm_leather_gloves,
		itm_melee_punch,
		itm_melee_punch,		
		itm_pipe1,
		itm_pipe2,
		itm_ion_beam_pistol,
		itm_ion_beam_pistol,
		itm_ion_pistol,
		itm_ion_pistol
	],
	def_attrib|level(11),
	wp(100),
	starwars_skills_outlaws_2,
	jawa_face1, jawa_face2
],
["looter_3","Jawa Scout","Jawa Scouts",
	tf_jawa|tf_guarantee_all_armor|tf_guarantee_ranged,
	0,0,fac_outlaws,
	[
		itm_jawa_hood,
		itm_jawa_robe,
		itm_jawa_boots,
		itm_leather_gloves,
		itm_leather_gloves,
		itm_pipe1,
		itm_pipe2,
		itm_ion_beam_rifle,
		itm_ion_beam_rifle,
		itm_ion_blaster,
		itm_ion_blaster
	],
	def_attrib|level(14),
	wp(120),
	starwars_skills_outlaws_2,
	jawa_face1, jawa_face2
],

#SW - modified names of bandit, brigand, mountain, forest, sea, steppe outlaws
["bandit","Bandit","Bandits",
	tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged,
	0,0,fac_outlaws,
	[
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_mining_helmet,
		itm_pipe_helmet,
		itm_fang_helmet,
		itm_beak_helmet,
		itm_gas_mask,
		itm_glasses_black,
		itm_glasses_yellow,
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,
		itm_jacket_closed_b,
		itm_jacket_open_a,
		itm_jacket_open_b,
		itm_jacket_open_c,
		itm_mercenary_armor,
		itm_vest_closed_a,
		itm_vest_closed_b,
		itm_vest_closed_c,
		itm_armor_blue,
		itm_armor_brown,
		itm_armor_red,
		itm_armor_white,
		itm_leather_boots,
		itm_grey_boots,
		itm_black_boots,
		#itm_energy_shield_red_small,
		#itm_energy_shield_yellow_small,
		#itm_energy_shield_blue_small,
		#itm_energy_shield_red_medium,
		#itm_energy_shield_yellow_medium,
		#itm_energy_shield_blue_medium,
		itm_laser_bolts_yellow_pistol,
		itm_laser_bolts_yellow_pistol,
		itm_ammo_belt_pistol,
		itm_dl18,
		itm_dl18,
		itm_q2,
		itm_westar,
		itm_melee_punch,
		itm_melee_punch,
		itm_vibro_knuckler,
		itm_combat_knife,
		itm_vibro_blade2,
		itm_vibro_blade4
	],
	def_attrib|level(10),
	wp(90),
	starwars_skills_outlaws_2,
	sw_bandit_face_1, sw_bandit_face_2
],
["brigand","Brigand","Brigands",
	tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged,
	0,0,fac_outlaws,
	[	
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_mining_helmet,
		itm_pipe_helmet,
		itm_fang_helmet,
		itm_beak_helmet,
		itm_gas_mask,
		itm_glasses_black,
		itm_glasses_yellow,
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,
		itm_jacket_closed_b,
		itm_jacket_open_a,
		itm_jacket_open_b,
		itm_jacket_open_c,
		itm_mercenary_armor,		
		itm_vest_closed_a,
		itm_vest_closed_b,
		itm_vest_closed_c,
		itm_armor_blue,
		itm_armor_brown,
		itm_armor_red,
		itm_armor_white,
		itm_leather_boots,
		itm_grey_boots,
		itm_black_boots,
		#itm_energy_shield_red_small,
		#itm_energy_shield_yellow_small,
		#itm_energy_shield_blue_small,
		itm_laser_bolts_yellow_pistol,
		itm_laser_bolts_yellow_pistol,
		itm_ammo_belt_pistol,
		itm_dl18,
		itm_dl18,		
		itm_q2,
		itm_westar,
		itm_melee_punch,
		itm_melee_punch,
		itm_vibro_knuckler,
		itm_combat_knife,		
		itm_vibro_blade2,
		itm_vibro_blade4
	],
	def_attrib|level(11),
	wp(100),
	starwars_skills_outlaws_2,
	sw_bandit_face_1, sw_bandit_face_2
],

["mountain_bandit_1","Black Sun Thug","Black Sun Thugs",
	tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves,
	0,0,fac_outlaws,
	[	
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,
		itm_jacket_closed_b,
		itm_jacket_open_a,
		itm_jacket_open_b,
		itm_jacket_open_c,
		itm_vest_closed_a,
		itm_vest_closed_b,
		itm_vest_closed_c,
		itm_armor_blue,
		itm_armor_brown,
		itm_armor_red,
		itm_armor_white,
		itm_leather_boots,
		itm_grey_boots,
		itm_black_boots,
		itm_laser_bolts_yellow_pistol,
		itm_laser_bolts_yellow_pistol,
		itm_ammo_belt_pistol,
		itm_dl18,
		itm_dl18,
		itm_ddc_defender,
		itm_westar,
		itm_melee_punch,
		itm_pipe1,
		itm_pipe1
	],
	def_attrib|level(6),
	wp(60),
	starwars_skills_outlaws_1,
	sw_bandit_face_1, sw_bandit_face_2
],

["mountain_bandit_2","Black Sun Smuggler","Black Sun Smugglers",
	tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged,
	0,0,fac_outlaws,
	[	
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_glasses_black,
		itm_glasses_yellow,
		itm_eyepiece_tactics,
		itm_eyepiece_leadership,
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,
		itm_jacket_closed_b,
		itm_jacket_open_a,
		itm_jacket_open_b,
		itm_jacket_open_c,
		itm_vest_closed_a,
		itm_vest_closed_b,
		itm_vest_closed_c,
		itm_armor_blue,
		itm_armor_brown,
		itm_armor_red,
		itm_armor_white,
		itm_leather_boots,
		itm_grey_boots,
		itm_black_boots,
		itm_laser_bolts_yellow_pistol,
		itm_laser_bolts_yellow_pistol,
		itm_ammo_belt_pistol,
		itm_dl44a,
		itm_dl44a,		
		itm_dl18,
		itm_dl18,		
		itm_westar,
		itm_melee_punch,		
		itm_combat_knife,
		itm_vibro_knuckler,
		itm_vibro_blade2,
		itm_vibro_blade4
	],
	def_attrib|level(10),
	wp(100),
	starwars_skills_outlaws_2,
	sw_bandit_face_1, sw_bandit_face_2
],

["mountain_bandit_3","Black Sun Pirate","Black Sun Pirates",
	tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged,
	0,0,fac_outlaws,
	[	
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_mining_helmet,
		itm_pipe_helmet,
		itm_fang_helmet,
		itm_beak_helmet,
		itm_gas_mask,	
		itm_glasses_black,
		itm_glasses_yellow,
		itm_eyepiece_tactics,
		itm_eyepiece_leadership,
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,
		itm_jacket_closed_b,
		itm_jacket_open_a,
		itm_jacket_open_b,
		itm_jacket_open_c,
		itm_mercenary_armor,
		itm_vest_closed_a,
		itm_vest_closed_b,
		itm_vest_closed_c,
		itm_armor_blue,
		itm_armor_brown,
		itm_armor_red,
		itm_armor_white,
		itm_scavenger_armor,
		itm_crime_lord_armor,
		itm_leather_boots,
		itm_grey_boots,
		itm_black_boots,
		itm_energy_shield_red_small,
		itm_energy_shield_yellow_small,
		itm_energy_shield_blue_small,
		itm_laser_bolts_yellow_rifle,
		itm_laser_bolts_yellow_rifle,
		itm_ammo_belt_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_ee3,
		itm_ee3,		
		itm_kisteer_1284,
		itm_corellian_destroyer_blaster,
		itm_vibro_axe_long_1h,
		itm_combat_knife,
		itm_vibro_knuckler,
		itm_vibro_blade2,
		itm_vibro_blade4
	],
	def_attrib|level(16),
	wp(125),
	starwars_skills_outlaws_3,
	sw_bandit_face_1, sw_bandit_face_2
],

["mountain_bandit_4","Black Sun Elite","Black Sun Elites",
	tf_guarantee_all_armor|tf_guarantee_ranged,
	0,0,fac_outlaws,
	[	
		itm_black_sun_helmet,
		itm_black_sun_helmet,
		itm_black_sun_armor,
		itm_black_sun_armor,
		itm_black_boots,
		itm_black_boots,
		itm_black_gloves,
		itm_black_gloves,
		itm_energy_shield_red_small,
		itm_energy_shield_yellow_small,
		itm_energy_shield_blue_small,
		itm_laser_bolts_yellow_rifle,
		itm_laser_bolts_yellow_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_a295,
		itm_a295_crouch,
		itm_corellian_destroyer_blaster,
		itm_corellian_destroyer_blaster,
		itm_mandalorian_heavy_blaster,
		itm_mandalorian_heavy_blaster,
		itm_vibro_knuckler,
		itm_vibro_blade2,
		itm_vibro_blade4
	],
	def_attrib|level(24),
	wp(150),
	starwars_skills_outlaws_4,
	sw_bandit_face_1, sw_bandit_face_2
],

["forest_bandit","Blazing Claw Pirate","Blazing Claw Pirates",
	tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged,
	0,0,fac_outlaws,
	[
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_mining_helmet,
		itm_pipe_helmet,
		itm_fang_helmet,
		itm_beak_helmet,
		itm_gas_mask,	
		itm_glasses_black,
		itm_glasses_yellow,
		itm_eyepiece_tactics,
		itm_eyepiece_leadership,
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,
		itm_jacket_closed_b,
		itm_jacket_open_a,
		itm_jacket_open_b,
		itm_jacket_open_c,
		itm_mercenary_armor,		
		itm_vest_closed_a,
		itm_vest_closed_b,
		itm_vest_closed_c,
		itm_armor_blue,
		itm_armor_brown,
		itm_armor_red,
		itm_armor_white,
		itm_scavenger_armor,
		itm_crime_lord_armor,		
		itm_leather_boots,
		itm_grey_boots,
		itm_black_boots,
		itm_energy_shield_red_small,
		itm_energy_shield_yellow_small,
		itm_energy_shield_blue_small,
		itm_laser_bolts_yellow_rifle,
		itm_laser_bolts_yellow_rifle,
		itm_ammo_belt_rifle,
		itm_ee3,
		itm_ee3,
		itm_dc15s,
		itm_kisteer_1284,
		itm_corellian_destroyer_blaster,
		itm_melee_punch,
		itm_vibro_axe_long_1h,
		itm_vibro_knuckler,
		itm_combat_knife,
		itm_vibro_blade2,
		itm_vibro_blade4
	],
	def_attrib|level(11),
	wp(100),
	starwars_skills_outlaws_2,
	sw_bandit_face_1, sw_bandit_face_2
],
["forest_bandit_female","Blazing Claw Pirate","Blazing Claw Pirates",
	tf_female|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	0,0,fac_outlaws,
	[
		itm_female_jacket_b,
		itm_female_jacket_b,
		itm_female_jacket_c,		
		itm_female_jacket_c,		
		itm_female_leather_a,
		itm_female_leather_b,
		itm_female_leather_c,
		itm_black_boots,
		itm_energy_shield_red_small,
		itm_energy_shield_yellow_small,
		itm_energy_shield_blue_small,
		itm_laser_bolts_yellow_pistol,
		itm_laser_bolts_yellow_pistol,
		#itm_ammo_belt_pistol,
		itm_westar,
		itm_westar,
		itm_q2,
		itm_dl18,
		itm_dl18,
		itm_dl44a,
		itm_melee_punch,
		itm_vibro_knuckler,
		itm_combat_knife,
		itm_vibro_blade2,
		itm_vibro_blade4
	],
	def_attrib|level(11),
	wp(100),
	starwars_skills_outlaws_2,
	sw_woman_face_1, sw_woman_face_2
],
["steppe_bandit","Night Fangs Pirate","Night Fangs Pirates",
	tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged,
	0,0,fac_outlaws,
	[
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_transparent_helmet,
		itm_mining_helmet,
		itm_pipe_helmet,
		itm_fang_helmet,
		itm_beak_helmet,
		itm_gas_mask,	
		itm_glasses_black,
		itm_glasses_yellow,
		itm_eyepiece_tactics,
		itm_eyepiece_leadership,	
		itm_weequay_head_helmet_a,
		itm_weequay_head_helmet_b,
		itm_klatooinian_head_helmet_a,
		itm_klatooinian_head_helmet_a,
		itm_nikto_head_helmet_a,
		itm_nikto_head_helmet_b,
		itm_nikto_head_helmet_c,
		itm_leather_gloves,
		itm_black_gloves,
		itm_jacket_closed_b,
		itm_jacket_open_a,
		itm_jacket_open_b,
		itm_jacket_open_c,
		itm_mercenary_armor,		
		itm_vest_closed_a,
		itm_vest_closed_b,
		itm_vest_closed_c,
		itm_armor_blue,
		itm_armor_brown,
		itm_armor_red,
		itm_armor_white,
		itm_scavenger_armor,
		itm_crime_lord_armor,		
		itm_leather_boots,
		itm_grey_boots,
		itm_black_boots,
		itm_energy_shield_yellow_small,
		itm_energy_shield_red_small,
		itm_energy_shield_blue_small,
		itm_laser_bolts_yellow_rifle,
		itm_laser_bolts_yellow_rifle,
		itm_ammo_belt_rifle,
		itm_a280,
		itm_a280_crouch,
		itm_ee3,
		itm_ee3,		
		itm_mg15,
		itm_kisteer_1284,
		itm_corellian_destroyer_blaster,
		itm_melee_punch,
		itm_vibro_axe_long_1h,		
		itm_vibro_knuckler,
		itm_combat_knife,
		itm_vibro_blade2,
		itm_vibro_blade4
	],
	def_attrib|level(12),
	wp(110),
	starwars_skills_outlaws_2,
	sw_bandit_face_1, sw_bandit_face_2
],
["steppe_bandit_female","Night Fangs Pirate","Night Fangs Pirates",
	tf_female|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
	0,0,fac_outlaws,
	[
		itm_female_jacket_b,
		itm_female_jacket_b,
		itm_female_jacket_c,		
		itm_female_jacket_c,		
		itm_female_leather_a,
		itm_female_leather_b,
		itm_female_leather_c,
		itm_black_boots,
		itm_energy_shield_red_small,
		itm_energy_shield_yellow_small,
		itm_energy_shield_blue_small,
		itm_laser_bolts_yellow_pistol,
		itm_laser_bolts_yellow_pistol,
		#itm_ammo_belt_pistol,
		itm_westar,
		itm_westar,
		itm_q2,
		itm_dl18,
		itm_dl18,
		itm_dl44a,
		itm_melee_punch,
		itm_vibro_knuckler,
		itm_combat_knife,
		itm_vibro_blade2,
		itm_vibro_blade4
	],
	def_attrib|level(12),
	wp(110),
	starwars_skills_outlaws_2,
	sw_woman_face_1, sw_woman_face_2
],
#SW - TUSKEN RAIDERS
["tusken_1","Tusken Warrior","Tusken Warriors",
	tf_tusken|tf_guarantee_all_armor,
	0,0,fac_outlaws,
	[   
		itm_tusken_helmet,
		itm_tusken_helmet,
		itm_tusken_armor,
		itm_tusken_armor,
		itm_wrapping_boots,
		itm_wrapping_boots,	
		itm_leather_gloves,
		itm_leather_gloves,
		itm_tusken_rifle,
		#itm_tusken_rifle,
		itm_laser_bolts_yellow_rifle,
		itm_laser_bolts_yellow_rifle,		
		itm_tusken_gaffi_stick,
		itm_tusken_gaffi_stick,
		itm_tusken_gaffi_staff,
		itm_tusken_gaffi_staff
	],
	def_attrib|level(11),
	wp(100),
	starwars_skills_outlaws_2,
	tusken_face1, tusken_face2
],
["tusken_2","Tusken Raider","Tusken Raiders",
	tf_tusken|tf_guarantee_all_armor|tf_guarantee_ranged,
	0,0,fac_outlaws,
	[
		itm_tusken_helmet,
		itm_tusken_helmet,
		itm_tusken_armor,
		itm_tusken_armor,
		itm_wrapping_boots,
		itm_wrapping_boots,	
		itm_leather_gloves,
		itm_leather_gloves,	
		itm_tusken_rifle,
		itm_tusken_rifle,
		itm_laser_bolts_yellow_rifle,
		itm_laser_bolts_yellow_rifle,
		itm_tusken_gaffi_stick,
		itm_tusken_gaffi_stick,
		itm_tusken_gaffi_staff,
		itm_tusken_gaffi_staff
	],
	def_attrib|level(18),
	wp(150),
	starwars_skills_outlaws_3,
	tusken_face1, tusken_face2
],

#SW - switched to Bounty Hunters - use rodian's and trandoshan's for manhunter party?
#["manhunter","Bounty Hunter","Bounty Hunters",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_shield|tf_mounted,0,0,fac_manhunters, [itm_jacket_closed_a,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_open_a,itm_vest_open_b,itm_stun_beam,itm_a280_stun,itm_ee3_stun,itm_dl44a_stun,itm_durasteel_mace,itm_durasteel_bat,itm_energy_shield_yellow_small,itm_energy_shield_green_small,itm_energy_shield_blue_small,itm_leather_vest,itm_leather_boots], def_attrib|level(10),wp(70),starwars_skills_2,sw_bandit_face_1, sw_bandit_face_2],
["manhunter","Trandoshan Slaver","Trandoshan Slavers",tf_trandoshan|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_manhunters, [itm_baton,itm_baton,itm_trandoshan_helmet,itm_trandoshan_skin,itm_trandoshan_armor,itm_trandoshan_flight_suit,itm_jacket_closed_a,itm_jacket_closed_c,itm_mercenary_armor,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_open_a,itm_vest_open_b,itm_stun_beam_rifle,itm_a280_stun,itm_ee3_stun,itm_trandoshan_stun_gun,itm_trandoshan_stun_gun,itm_durasteel_mace,itm_durasteel_bat,itm_energy_shield_yellow_small,itm_energy_shield_yellow_small,itm_electro_staff_medium,itm_electro_staff_long], def_attrib|level(16),wp(100),starwars_skills_3,trandoshan_face1, trandoshan_face2],
##  ["deserter","Deserter","Deserters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_swadian_deserters,
##   [itm_laser_bolts_other,itm_spear,itm_fighting_pick,itm_dh17,itm_sword,itm_voulge,itm_nordic_shield,itm_round_shield,itm_kettle_hat,itm_leather_cap,itm_padded_cloth,itm_leather_armor,itm_scale_armor,itm_saddle_horse],
##   def_attrib|level(12),wp(60),knows_common,sw_bandit_face_1, sw_bandit_face_2],

#fac_slavers
##  ["slave_keeper","Slave Keeper","Slave Keepers",tf_guarantee_armor,0,0,fac_slavers,
##   [itm_cudgel,itm_club,itm_woolen_cap,itm_rawhide_coat,itm_coarse_tunic,itm_nomad_armor,itm_nordic_shield,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse],
##   def_attrib|level(10),wp(60),knows_common,sw_bandit_face_1, sw_bandit_face_2],
#SW - commented out, no longer used
#["slave_driver","Slave Driver","Slave Drivers",tf_guarantee_armor|tf_guarantee_boots|tf_mounted,0,0,fac_slavers, [itm_jacket_closed_a,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_open_a,itm_vest_open_b,itm_stun_beam,itm_q2_stun,itm_westar_stun,itm_ee3_stun,itm_dl44a_stun,itm_durasteel_mace,itm_energy_shield_yellow_small,itm_energy_shield_green_small,itm_energy_shield_blue_small,itm_nomad_boots,itm_wrapping_boots], def_attrib|level(14),wp(80),starwars_skills_1,sw_bandit_face_1, sw_bandit_face_2],
#["slave_hunter","Slave Hunter","Slave Hunters",tf_guarantee_armor|tf_guarantee_boots|tf_mounted,0,0,fac_slavers, [itm_jacket_closed_a,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_open_a,itm_vest_open_b,itm_stun_beam,itm_q2_stun,itm_westar_stun,itm_ee3_stun,itm_dl44a_stun,itm_durasteel_mace,itm_nomad_boots,itm_wrapping_boots], def_attrib|level(18),wp(90),starwars_skills_2,sw_bandit_face_1, sw_bandit_face_2],
#["slave_crusher","Slave Crusher","Slave Crushers",tf_guarantee_armor|tf_guarantee_boots|tf_mounted,0,0,fac_slavers, [itm_jacket_closed_a,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_open_a,itm_vest_open_b,itm_stun_beam,itm_dh17_stun,itm_e11_stun,itm_durasteel_mace,itm_leather_boots,itm_black_boots], def_attrib|level(22),wp(110),starwars_skills_2,sw_bandit_face_1, sw_bandit_face_2],
#["slaver_chief","Slaver Chief","Slaver Chiefs",tf_guarantee_armor|tf_guarantee_boots|tf_mounted,0,0,fac_slavers, [itm_jacket_closed_a,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_open_a,itm_vest_open_b,itm_stun_beam,itm_a280_stun,itm_durasteel_mace,itm_leather_boots,itm_black_boots], def_attrib|level(26),wp(130),starwars_skills_3,sw_bandit_face_1, sw_bandit_face_2],

#Rhodok tribal, Hunter, warrior, veteran, warchief

#  ["undead_walker","undead_walker","undead_walkers",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["undead_horseman","undead_horseman","undead_horsemen",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_undeads,
#   [], 
#   def_attrib|level(19),wp(100),knows_common,undead_face1, undead_face2],
#  ["undead_nomad","undead_nomad","undead_nomads",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
#   [], 
#   def_attrib|level(21),wp(100),knows_common|knows_riding_4,khergit_face1, khergit_face2],
#  ["undead","undead","undead",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["hell_knight","hell_knight","hell_knights",tf_undead|tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_undeads,
#   [], 
#   def_attrib|level(23),wp(100),knows_common|knows_riding_3,undead_face1, undead_face2],

#SW commented out follower_woman, hunter_woman, fighter_woman, sword_sister, refugee
#["follower_woman","Camp Follower","Camp Follower",tf_female|tf_guarantee_armor|tf_guarantee_ranged|tf_mounted,0,0,fac_commoners,[itm_laser_bolts_red,itm_q2,itm_dh17,itm_dl44a,itm_durasteel_shield_small,itm_vibro_blade1,itm_vibro_blade3,itm_dress,itm_woolen_dress, itm_wrapping_boots],def_attrib|level(5),wp(70),starwars_skills_1,sw_woman_face_1,sw_woman_face_2],
#["hunter_woman","Huntress","Huntresses",tf_female|tf_guarantee_armor|tf_guarantee_ranged|tf_mounted,0,0,fac_commoners,[itm_laser_bolts_red,itm_laser_bolts_red,itm_q2,itm_dh17,itm_dl44a,itm_energy_shield_green_small,itm_energy_shield_blue_small,itm_vibro_blade1,itm_vibro_blade3,itm_dress,itm_woolen_dress, itm_wrapping_boots],def_attrib|level(10),wp(85),starwars_skills_1,sw_woman_face_1,sw_woman_face_2],
#["fighter_woman","Camp Defender","Camp Defenders",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_mounted,0,0,fac_commoners,[itm_laser_bolts_red,itm_q2,itm_dh17,itm_dl44a,itm_energy_shield_green_small,itm_energy_shield_blue_small,itm_durasteel_shield_small,itm_vibro_blade1,itm_vibro_blade3,itm_leather_jerkin,itm_leather_vest, itm_wrapping_boots],def_attrib|level(16),wp(100),starwars_skills_2,sw_woman_face_1,sw_woman_face_2],
#["sword_sister","Sword Sister","Sword Sisters",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged|tf_mounted,0,0,fac_commoners,[itm_laser_bolts_red,itm_vibro_blade1,itm_vibro_blade3,itm_durasteel_shield_small,itm_energy_shield_green_small,itm_energy_shield_blue_small,itm_dl44a,itm_westar,itm_ee3,itm_leather_jerkin,itm_leather_vest,itm_leather_boots,itm_leather_gloves],def_attrib|level(22),wp(140),starwars_skills_2,sw_woman_face_1,sw_woman_face_2],
#["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac_commoners,[itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],def_attrib|level(1),wp(45),starwars_skills_1,sw_woman_face_1,sw_woman_face_2],
["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac_commoners,[itm_q2,itm_westar,itm_laser_bolts_orange_pistol,itm_laser_bolts_yellow_pistol,itm_knife,itm_hatchet,itm_club,itm_dress,itm_quarter_staff,itm_vibro_blade2,itm_vibro_blade3,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],def_attrib|level(1),wp(40),starwars_skills_1,sw_woman_face_1,sw_woman_face_2],

# renamed caravan master
["caravan_master","Freighter Captain","Freighter Captains",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,[itm_dl44a,itm_westar,itm_laser_bolts_green_pistol,itm_laser_bolts_red_pistol,itm_laser_bolts_yellow_pistol,itm_vest_open_b,itm_leather_boots],def_attrib|level(9),wp(100),starwars_skills_3,sw_man_face_1, sw_man_face_2],
["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_female|tf_randomize_face|tf_unmoveable_in_party_window,0,reserved,fac_commoners,[itm_dress_blue,itm_leather_boots],def_attrib|level(2),wp(50),starwars_skills_1,sw_woman_face_1, sw_woman_face_2],
#This troop is the troop marked as soldiers_end
["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_ubese_armor,itm_scavenger_armor,itm_crime_lord_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_q2,itm_dl44a,itm_civilian_cloak,itm_civilian_cloak_hood,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet,itm_jacket_closed_a,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_female_jacket_a,itm_female_jacket_b,itm_female_jacket_c,itm_female_jacket_a,itm_female_jacket_b,itm_female_jacket_c,itm_female_outfit_femconblack,itm_female_outfit_femconbrowngreen,itm_female_outfit_femcongrey,itm_female_outfit_femconorange,itm_female_outfit_femconwhite,itm_female_outfit_femconwhitebrown,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_female_dress_a,itm_female_dress_a,itm_female_dress_b,itm_female_dress_b,itm_transparent_helmet,itm_transparent_helmet,itm_black_boots,itm_leather_boots], def_attrib|level(2),wp(40),knows_common,sw_woman_face_1, sw_woman_face_2],
["town_walker_twilek","Twilek","Twileks",tf_twilek|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ubese_armor,itm_scavenger_armor,itm_crime_lord_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,twilek_face1,twilek_face2],
["town_walker_twilek_female","Twilek Female","Twilek Females",tf_twilek_female|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [], def_attrib|level(4),wp(60),knows_common,twilek_female_face1,twilek_female_face2],
["town_walker_twilek_female_slave","Twilek Slave Dancer","Twilek Slave Dancers",tf_twilek_female|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [itm_transparent_helmet,itm_slave_neck_chain], def_attrib|level(4),wp(60),knows_common,twilek_female_face1,twilek_female_face2],
["town_walker_slave_dancer","Slave Dancer","Slave Dancers",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_transparent_helmet,itm_slave_neck_chain,itm_female_leather_a,itm_female_leather_b,itm_female_leather_c,itm_female_leather_d,itm_black_boots], def_attrib|level(2),wp(40),knows_common,sw_slave_dancer_face1, sw_slave_dancer_face2],
["town_walker_chiss","Chiss","Chiss",tf_chiss|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ubese_armor,itm_scavenger_armor,itm_crime_lord_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,chiss_face1,chiss_face2],
["town_walker_chiss_female","Chiss Female","Chiss Female",tf_female|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_female_outfit_femconblack,itm_female_outfit_femconbrowngreen,itm_female_outfit_femcongrey,itm_female_outfit_femconorange,itm_female_outfit_femconwhite,itm_female_outfit_femconwhitebrown,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_white_cloak,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet,itm_black_boots,itm_leather_boots], def_attrib|level(4),wp(60),knows_common,chiss_female_face1,chiss_female_face2],
["town_walker_mandalorian","Mandalorian","Mandalorians",tf_guarantee_all_armor|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves,itm_laser_bolts_orange_rifle,itm_mandalorian_heavy_blaster,itm_mandalorian_sniper_helmet,itm_mandalorian_sniper_armor,itm_mandalorian_sniper_boots], def_attrib|level(20),wp(180),knows_common,mandalorian_face1,mandalorian_face2],
["town_walker_trandoshan","Trandoshan","Trandoshans",tf_trandoshan|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_trandoshan_flight_suit,itm_trandoshan_flight_suit,itm_trandoshan_armor,itm_trandoshan_armor,itm_trandoshan_blade,itm_trandoshan_supressor,itm_trandoshan_stun_gun,itm_trandoshan_acp_array_gun,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b], def_attrib|level(4),wp(60),knows_common,trandoshan_face1,trandoshan_face2],
["town_walker_rodian","Rodian","Rodians",tf_rodian|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ubese_armor,itm_scavenger_armor,itm_crime_lord_armor,itm_rodian_ventilator,itm_rodian_ventilator_black,itm_rodian_ventilator_red,itm_transparent_helmet,itm_transparent_helmet,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,rodian_face1,rodian_face2],
["town_walker_r2series","R2-Series Droid","R2-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_r2series_blue,itm_r2series_green,itm_r2series_orange,itm_r2series_purple,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_2,wp(60),droid_skills_2,droid_face1,droid_face2],
["town_walker_lin_droid","LIN Droid","LIN Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_lin_droid_armor,itm_lin_droid_armor,itm_lin_droid_armor_w_arm,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_2,wp(30),droid_skills_2,droid_face1,droid_face2],
["town_walker_mse6","MSE-6 Droid","MSE-6 Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_mse6_armor,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_1,wp(60),droid_skills_1,droid_face1,droid_face2],
["town_walker_3poseries","3PO-Series Droid","3PO-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_3poseries_gold,itm_3poseries_gold,itm_3poseries_blue,itm_3poseries_red,itm_3poseries_grey,itm_3poseries_grey,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_3poseries_attack], droid_attrib_2,wp(110),droid_skills_2,droid_face1,droid_face2],
["town_walker_3poseries_naked","3PO-Series Droid","3PO-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_3poseries_attack], droid_attrib_2,wp(110),droid_skills_2,droid_face1,droid_face2],
["town_walker_power_droid","Power Droid","Power Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_power_droid_tan,itm_power_droid_tan,itm_power_droid_grey,itm_power_droid_grey,itm_power_droid_snow,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_1,wp(60),droid_skills_1,droid_face1,droid_face2],
["town_walker_fxseries_droid","FX-Series Medical Droid","FX-Series Medical Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_fxseries_droid_armor,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_1,wp(60),droid_skills_1,droid_face1,droid_face2],
["town_walker_hkseries","HK-Series Droid","HK-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_hk_head,itm_hk_body,itm_hk_hands,itm_hk_feet,itm_hk_attack,itm_a280,itm_laser_bolts_orange_rifle], def_attrib_3|level(24),wp(150),starwars_skills_3,droid_face1,droid_face2],
["town_walker_sullustan","Sullustan","Sullustans",tf_sullustan|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ubese_armor,itm_scavenger_armor,itm_crime_lord_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,sullustan_face1,sullustan_face2],
["town_walker_bothan","Bothan","Bothans",tf_bothan|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ubese_armor,itm_scavenger_armor,itm_crime_lord_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,bothan_face1,bothan_face2],
["town_walker_weequay","Weequay","Weequays",tf_weequay|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_weequay_head_helmet_a,itm_weequay_head_helmet_b,itm_guard_armor,itm_guard_armor_red,itm_vibro_axe_long_2h,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,weequay_face1,weequay_face2],
["town_walker_klatooinian","Klatooinian","Klatooinians",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_klatooinian_head_helmet_a,itm_leather_gloves,itm_guard_armor,itm_guard_armor_red,itm_vibro_axe_long_2h,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common, sw_man_face_1, sw_man_face_2],
["town_walker_nikto","Nikto","Niktos",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_nikto_head_helmet_a,itm_nikto_head_helmet_b,itm_nikto_head_helmet_c,itm_leather_gloves,itm_guard_armor,itm_guard_armor_red,itm_vibro_axe_long_2h,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["town_walker_jawa","Jawa","Jawas",tf_jawa|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_jawa_hood,itm_jawa_robe,itm_jawa_boots,itm_leather_gloves,itm_ion_beam_pistol,itm_ion_pistol], def_attrib|level(4),wp(60),knows_common,jawa_face1,jawa_face2],
#["town_walker_tusken","Tusken","Tuskens",tf_tusken|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_tusken_helmet,itm_tusken_armor,itm_wrapping_boots,itm_leather_gloves,itm_laser_bolts_orange,itm_tusken_rifle,itm_tusken_gaffi_staff], def_attrib|level(4),wp(60),knows_common,tusken_face1,tusken_face2],
["town_walker_moncal","Mon Calamarian","Mon Calamarians",tf_moncal|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ubese_armor,itm_scavenger_armor,itm_crime_lord_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,moncal_face1,moncal_face2],
["town_walker_geonosian","Geonosian","geonosians",tf_geonosian|tf_randomize_face,0,0,fac_commoners, [itm_geonosian_sonic_pistol,itm_geonosian_sonic_rifle,itm_geonosian_static_pike,itm_geonosian_armor], def_attrib|level(4),wp(60),knows_common,geonosian_face1,geonosian_face2],
["town_walker_wookiee","Wookiee","Wookiees",tf_wookiee|tf_randomize_face,0,0,fac_commoners, [itm_wookiee_armor1,itm_wookiee_armor2,itm_ryyk_blade,itm_melee_punch,itm_wookiee_bowcaster,itm_laser_bolts_green_rifle], def_attrib|level(4),wp(60),knows_common,wookiee_face1,wookiee_face2],
["town_walker_wookiee_female","Wookiee Female","Wookiee Females",tf_wookiee|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_wookiee_female_head,itm_wookiee_female_body,itm_wookiee_female_hands,itm_wookiee_female_feet,itm_melee_punch], def_attrib|level(4),wp(60),knows_common,wookiee_face1,wookiee_face2],
["town_walker_gamorrean","Gamorrean","Gamorreans",tf_gamorrean|tf_randomize_face,0,0,fac_commoners, [itm_vibro_axe_medium_1h,itm_throwing_axes], def_attrib|level(4),wp(60),knows_common,gamorrean_face1,gamorrean_face2],
#new faction specific town walkers
["town_walker_empire_1","Imperial Navy Trooper","Imperial Navy Trooper",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_imperial_navy_trooper_armor,itm_imperial_navy_trooper_helmet,itm_black_boots,itm_black_gloves_long,itm_laser_bolts_red_pistol,itm_ddc_defender], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],
["town_walker_empire_2","Imperial Army Trooper","Imperial Army Trooper",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_imperial_trooper_armor,itm_imperial_trooper_helmet,itm_black_boots,itm_black_gloves_long,itm_laser_bolts_red_pistol,itm_ddc_defender], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],
["town_walker_empire_3","Imperial Stormtrooper","Imperial Stormtrooper",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_imperial_stormtrooper_armor,itm_imperial_stormtrooper_helmet,itm_imperial_stormtrooper_boots,itm_imperial_stormtrooper_gloves,itm_laser_bolts_red_rifle,itm_e11,itm_e11_hip,itm_e11_hip], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],
["town_walker_empire_4","Imperial Pilot","Imperial Pilot",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_imperial_pilot_helmet,itm_imperial_uniform_black_plain,itm_black_boots,itm_black_gloves_long,itm_laser_bolts_red_pistol,itm_ddc_defender], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],
["town_walker_empire_5","Imperial Scout Trooper","Imperial Scout Trooper",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_imperial_scout_trooper_armor,itm_imperial_scout_trooper_helmet,itm_imperial_scout_trooper_boots,itm_black_gloves_long,itm_laser_bolts_red_pistol,itm_scout_trooper_pistol], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],
["town_walker_empire_6","Imperial Officer","Imperial Officer",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_imperial_uniform_black,itm_imperial_hat_black,itm_black_boots,itm_laser_bolts_red_pistol,itm_ddc_defender], def_attrib|level(4),wp(60),knows_common,sw_imperial_face_1,sw_imperial_face_2],
["town_walker_empire_7","Sith Marauder","Sith Marauders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [itm_sith_hood_unique,itm_sith_marauder_robe_unique,itm_black_gloves,itm_black_boots_reinforced,itm_lightsaber_red,itm_force_shield,itm_force_protect,itm_lightsaber_block_red], def_attrib_force_3|level(28),wp(220)|wp_archery(240),starwars_skills_force_3,sw_sith_face_1, sw_sith_face_2],
["town_walker_empire_8","MSE-6 Droid","MSE-6 Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_mse6_armor,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_1,wp(60),droid_skills_1,droid_face1,droid_face2],
["town_walker_rebel_1","Rebel Technician","Rebel Technician",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [itm_rebel_technician_helmet,itm_rebel_technician_armor,itm_black_boots,itm_laser_bolts_green_pistol,itm_ddc_defender], def_attrib|level(4),wp(60),knows_common,sw_rebel_face_1,sw_rebel_face_2],
["town_walker_rebel_2","Rebel Trooper","Rebel Trooper",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [itm_republic_trooper_armor,itm_rebel_trooper_helmet,itm_black_boots,itm_laser_bolts_green_pistol,itm_dh17], def_attrib|level(4),wp(60),knows_common,sw_rebel_face_1,sw_rebel_face_2],
["town_walker_rebel_3","Rebel Pilot","Rebel Pilot",tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_republic_pilot_armor,itm_republic_pilot_helmet,itm_black_boots,itm_black_gloves,itm_laser_bolts_green_pistol,itm_dh17], def_attrib|level(4),wp(60),knows_common,sw_rebel_face_1,sw_rebel_face_2],
["town_walker_rebel_4","Rebel Commando","Rebel Commando",tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_republic_commando_armor,itm_republic_commando_helmet,itm_leather_boots,itm_leather_gloves,itm_laser_bolts_green_rifle,itm_a280], def_attrib|level(4),wp(60),knows_common,sw_rebel_face_1,sw_rebel_face_2],
["town_walker_rebel_5","Rebel Officer","Rebel Officer",tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_rebel_uniform_tanblue,itm_leather_boots,itm_laser_bolts_green_pistol,itm_ddc_defender], def_attrib|level(4),wp(60),knows_common,sw_rebel_face_1,sw_rebel_face_2],
["town_walker_rebel_6","Jedi Master","Jedi Masters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [itm_transparent_helmet,itm_jedi_robe_a_unique,itm_jedi_robe_d_unique,itm_jedi_robe_e_unique,itm_jedi_robe_f_unique,itm_leather_gloves,itm_leather_boots_reinforced,itm_lightsaber_blue,itm_lightsaber_green,itm_force_shield,itm_force_protect], def_attrib_force_3|level(28),wp(220)|wp_archery(240),starwars_skills_force_3,sw_rebel_face_1,sw_rebel_face_2],
["town_walker_rebel_7","Mon Calamarian","Mon Calamarians",tf_moncal|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_officer_uniform_white,itm_black_boots,itm_laser_bolts_green_pistol,itm_ddc_defender], def_attrib|level(4),wp(60),knows_common,moncal_face1,moncal_face2],
["town_walker_rebel_8","Wookiee","Wookiees",tf_wookiee|tf_randomize_face,0,0,fac_commoners, [itm_wookiee_armor1,itm_wookiee_armor2,itm_ryyk_blade,itm_melee_punch,itm_wookiee_bowcaster,itm_laser_bolts_green_rifle], def_attrib|level(4),wp(60),knows_common,wookiee_face1,wookiee_face2],
["town_walker_rebel_9","R2-Series Droid","R2-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_r2series_blue,itm_r2series_green,itm_r2series_orange,itm_r2series_purple,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_2,wp(60),droid_skills_2,droid_face1,droid_face2],
["town_walker_hutt_1","Hutt Mercenary","Hutt Mercenary",tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_armor_blue,itm_armor_brown,itm_armor_red,itm_armor_white,itm_klatooinian_armor,itm_leather_gloves,itm_black_gloves,itm_black_boots,itm_weequay_head_helmet_a,itm_weequay_head_helmet_b,itm_klatooinian_head_helmet_a,itm_klatooinian_head_helmet_a,itm_nikto_head_helmet_a,itm_nikto_head_helmet_b,itm_nikto_head_helmet_c,itm_transparent_helmet,itm_transparent_helmet,itm_mining_helmet,itm_pipe_helmet,itm_fang_helmet,itm_beak_helmet,itm_gas_mask,itm_laser_bolts_orange_pistol,itm_ddc_defender,itm_dl18,itm_dl18], def_attrib|level(4),wp(60),knows_common,sw_hutt_face_1,sw_hutt_face_2],
["town_walker_hutt_2","Hutt Skiff Guard","Hutt Skiff Guards",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_weequay_head_helmet_a,itm_weequay_head_helmet_b,itm_transparent_helmet,itm_skiff_guard_helmet,itm_skiff_guard_helmet,itm_skiff_guard_armor_brown,itm_skiff_guard_armor_grey,itm_skiff_guard_armor_white,itm_leather_boots,itm_vibro_axe_long_2h,itm_laser_bolts_orange_pistol,itm_dl18], def_attrib|level(4),wp(60),knows_common,sw_hutt_face_1,sw_hutt_face_2],
["town_walker_hutt_3","Gamorrean Guard","Gamorrean Guards",tf_gamorrean|tf_randomize_face,0,0,fac_commoners, [itm_vibro_axe_medium_1h,itm_throwing_axes], def_attrib|level(4),wp(60),knows_common,gamorrean_face1,gamorrean_face2],
["town_walker_hutt_4","Slave Dancer","Slave Dancers",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_female_dancer_outfit_a,itm_female_dancer_outfit_a,itm_female_dancer_outfit_a,itm_female_dancer_outfit_a_cloak,itm_female_dancer_boots], def_attrib|level(2),wp(40),knows_common,sw_slave_dancer_face1, sw_slave_dancer_face2],
#SW - added cantina_walkers - cantina_walker_1 marked as town_walker_end
["cantina_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_ubese_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_q2,itm_dl44a,itm_civilian_cloak,itm_civilian_cloak_hood,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet,itm_jacket_closed_a,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["cantina_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_female_jacket_a,itm_female_jacket_b,itm_female_jacket_c,itm_female_jacket_a,itm_female_jacket_b,itm_female_jacket_c,itm_female_outfit_femconblack,itm_female_outfit_femconbrowngreen,itm_female_outfit_femcongrey,itm_female_outfit_femconorange,itm_female_outfit_femconwhite,itm_female_outfit_femconwhitebrown,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_white_cloak,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet,itm_black_boots,itm_leather_boots], def_attrib|level(2),wp(40),knows_common,sw_woman_face_1, sw_woman_face_2],
#["cantina_walker_jawa","Jawa","Jawas",tf_jawa|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_jawa_hood,itm_jawa_robe,itm_jawa_boots,itm_leather_gloves,itm_ion_beam,itm_ion_pistol,itm_ion_blaster], def_attrib|level(4),wp(60),knows_common,jawa_face1,jawa_face2],
["cantina_walker_rodian","Rodian","Rodians",tf_rodian|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_rodian_ventilator,itm_rodian_ventilator_black,itm_rodian_ventilator_red,itm_transparent_helmet,itm_transparent_helmet,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,rodian_face1,rodian_face2],
["cantina_walker_moncal","Mon Calamarian","Mon Calamarians",tf_moncal|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,moncal_face1,moncal_face2],
["cantina_walker_trandoshan","Trandoshan","Trandoshans",tf_trandoshan|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_trandoshan_flight_suit,itm_trandoshan_flight_suit,itm_trandoshan_armor,itm_trandoshan_armor,itm_trandoshan_blade,itm_trandoshan_supressor,itm_trandoshan_stun_gun,itm_trandoshan_acp_array_gun,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b], def_attrib|level(4),wp(60),knows_common,trandoshan_face1,trandoshan_face2],
["cantina_walker_mandalorian","Mandalorian","Mandalorians",tf_guarantee_all_armor|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves,itm_laser_bolts_orange_rifle,itm_mandalorian_heavy_blaster,itm_mandalorian_sniper_helmet,itm_mandalorian_sniper_armor,itm_mandalorian_sniper_boots], def_attrib|level(4),wp(60),knows_common,mandalorian_face1,mandalorian_face2],
["cantina_walker_sullustan","Sullustan","Sullustans",tf_sullustan|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,sullustan_face1,sullustan_face2],
["cantina_walker_bothan","Bothan","Bothans",tf_bothan|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,bothan_face1,bothan_face2],
["cantina_walker_chiss","Chiss","Chiss",tf_chiss|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,chiss_face1,chiss_face2],
["cantina_walker_chiss_female","Chiss Female","Chiss Female",tf_female|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_female_outfit_femconblack,itm_female_outfit_femconbrowngreen,itm_female_outfit_femcongrey,itm_female_outfit_femconorange,itm_female_outfit_femconwhite,itm_female_outfit_femconwhitebrown,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_white_cloak,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet,itm_black_boots,itm_leather_boots], def_attrib|level(4),wp(60),knows_common,chiss_female_face1,chiss_female_face2],
["cantina_walker_weequay","Weequay","Weequays",tf_weequay|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_weequay_head_helmet_a,itm_weequay_head_helmet_b,itm_guard_armor,itm_guard_armor_red,itm_vibro_axe_long_2h,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,weequay_face1,weequay_face2],
["cantina_walker_klatooinian","Klatooinian","Klatooinians",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_klatooinian_head_helmet_a,itm_leather_gloves,itm_guard_armor,itm_guard_armor_red,itm_vibro_axe_long_2h,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common, sw_man_face_1, sw_man_face_2],
["cantina_walker_nikto","Nikto","Niktos",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_nikto_head_helmet_a,itm_nikto_head_helmet_b,itm_nikto_head_helmet_c,itm_leather_gloves,itm_guard_armor,itm_guard_armor_red,itm_vibro_axe_long_2h,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["cantina_walker_twilek","Twilek","Twileks",tf_twilek|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ubese_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,twilek_face1,twilek_face2],
["cantina_walker_twilek_female","Twilek Female","Twilek Females",tf_twilek_female|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [], def_attrib|level(4),wp(60),knows_common,twilek_female_face1,twilek_female_face2],
["cantina_walker_geonosian","Geonosian","geonosians",tf_geonosian|tf_randomize_face,0,0,fac_commoners, [itm_geonosian_sonic_pistol,itm_geonosian_sonic_rifle,itm_geonosian_static_pike,itm_geonosian_armor], def_attrib|level(4),wp(60),knows_common,geonosian_face1,geonosian_face2],
["cantina_walker_wookiee","Wookiee","Wookiees",tf_wookiee|tf_randomize_face,0,0,fac_commoners, [itm_wookiee_armor1,itm_wookiee_armor2,itm_ryyk_blade,itm_wookiee_bowcaster], def_attrib|level(4),wp(60),knows_common,wookiee_face1,wookiee_face2],
["cantina_walker_wookiee_female","Wookiee Female","Wookiee Females",tf_wookiee|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_wookiee_female_head,itm_wookiee_female_body,itm_wookiee_female_hands,itm_wookiee_female_feet], def_attrib|level(4),wp(60),knows_common,wookiee_face1,wookiee_face2],
["cantina_walker_gamorrean","Gamorrean","Gamorreans",tf_gamorrean|tf_randomize_face,0,0,fac_commoners, [itm_vibro_axe_medium_1h], def_attrib|level(4),wp(60),knows_common,gamorrean_face1,gamorrean_face2],
["cantina_drinker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves_with_bottle,itm_ubese_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_q2,itm_dl44a,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet,itm_jacket_closed_a,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["cantina_drinker_rodian","Rodian","Rodians",tf_rodian|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves_with_bottle,itm_rodian_ventilator,itm_rodian_ventilator_black,itm_rodian_ventilator_red,itm_transparent_helmet,itm_transparent_helmet,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,rodian_face1,rodian_face2],
["cantina_drinker_moncal","Mon Calamarian","Mon Calamarians",tf_moncal|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves_with_bottle,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,moncal_face1,moncal_face2],
["cantina_drinker_trandoshan","Trandoshan","Trandoshans",tf_trandoshan|tf_guarantee_armor|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves_with_bottle,itm_trandoshan_flight_suit,itm_trandoshan_flight_suit,itm_trandoshan_armor,itm_trandoshan_armor,itm_trandoshan_blade,itm_trandoshan_supressor,itm_trandoshan_stun_gun,itm_trandoshan_acp_array_gun,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b], def_attrib|level(4),wp(60),knows_common,trandoshan_face1,trandoshan_face2],
["cantina_drinker_sullustan","Sullustan","Sullustans",tf_sullustan|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves_with_bottle,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,sullustan_face1,sullustan_face2],
["cantina_drinker_bothan","Bothan","Bothans",tf_bothan|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves_with_bottle,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,bothan_face1,bothan_face2],
["cantina_drinker_chiss","Chiss","Chiss",tf_chiss|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves_with_bottle,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,chiss_face1,chiss_face2],
["cantina_drinker_weequay","Weequay","Weequays",tf_weequay|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves_with_bottle,itm_weequay_head_helmet_a,itm_weequay_head_helmet_b,itm_guard_armor,itm_guard_armor_red,itm_vibro_axe_long_2h,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,weequay_face1,weequay_face2],
["cantina_drinker_klatooinian","Klatooinian","Klatooinians",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves_with_bottle,itm_klatooinian_head_helmet_a,itm_guard_armor,itm_guard_armor_red,itm_vibro_axe_long_2h,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common, sw_man_face_1, sw_man_face_2],
["cantina_drinker_nikto","Nikto","Niktos",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves_with_bottle,itm_nikto_head_helmet_a,itm_nikto_head_helmet_b,itm_nikto_head_helmet_c,itm_guard_armor,itm_guard_armor_red,itm_vibro_axe_long_2h,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["cantina_drinker_twilek","Twilek","Twileks",tf_twilek|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_gloves|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves_with_bottle,itm_ubese_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,twilek_face1,twilek_face2],
#SW - renamed to colonists - village_walker_1 marked as cantina_walker_end
["village_walker_1","Colonist","Colonists",tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_ubese_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_q2,itm_dl44a,itm_civilian_cloak,itm_civilian_cloak_hood,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet,itm_jacket_closed_a,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["village_walker_2","Colonist","Colonists",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_female_jacket_a,itm_female_jacket_b,itm_female_jacket_c,itm_female_jacket_a,itm_female_jacket_b,itm_female_jacket_c,itm_female_outfit_femconblack,itm_female_outfit_femconbrowngreen,itm_female_outfit_femcongrey,itm_female_outfit_femconorange,itm_female_outfit_femconwhite,itm_female_outfit_femconwhitebrown,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_female_dress_a,itm_female_dress_a,itm_female_dress_b,itm_female_dress_b,itm_transparent_helmet,itm_transparent_helmet,itm_black_boots,itm_leather_boots], def_attrib|level(2),wp(40),knows_common,sw_woman_face_1, sw_woman_face_2],
#["village_walker_jawa","Jawa","Jawas",tf_jawa|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_jawa_hood,itm_jawa_robe,itm_jawa_boots,itm_leather_gloves,itm_ion_beam,itm_ion_pistol,itm_ion_blaster], def_attrib|level(4),wp(60),knows_common,jawa_face1,jawa_face2],
#["village_walker_tusken","Tusken","Tuskens",tf_tusken|tf_guarantee_all_armor,0,0,fac_commoners, [itm_tusken_helmet,itm_tusken_armor,itm_wrapping_boots,itm_leather_gloves,itm_laser_bolts_orange,itm_tusken_rifle,itm_tusken_gaffi_staff], def_attrib|level(4),wp(60),knows_common,tusken_face1,tusken_face2],
["village_walker_rodian","Rodian","Rodians",tf_rodian|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_rodian_ventilator,itm_rodian_ventilator_black,itm_rodian_ventilator_red,itm_transparent_helmet,itm_transparent_helmet,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,rodian_face1,rodian_face2],
["village_walker_moncal","Mon Calamarian","Mon Calamarians",tf_moncal|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,moncal_face1,moncal_face2],
["village_walker_trandoshan","Trandoshan","Trandoshans",tf_trandoshan|tf_guarantee_armor|tf_randomize_face,0,0,fac_commoners, [itm_trandoshan_flight_suit,itm_trandoshan_flight_suit,itm_trandoshan_armor,itm_trandoshan_armor,itm_trandoshan_blade,itm_trandoshan_supressor,itm_trandoshan_stun_gun,itm_trandoshan_acp_array_gun,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b], def_attrib|level(4),wp(60),knows_common,trandoshan_face1,trandoshan_face2],
["village_walker_mandalorian","Mandalorian","Mandalorians",tf_guarantee_all_armor|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves,itm_laser_bolts_orange_rifle,itm_mandalorian_heavy_blaster,itm_mandalorian_sniper_helmet,itm_mandalorian_sniper_armor,itm_mandalorian_sniper_boots], def_attrib|level(4),wp(60),knows_common,mandalorian_face1,mandalorian_face2],
["village_walker_sullustan","Sullustan","Sullustans",tf_sullustan|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,sullustan_face1,sullustan_face2],
["village_walker_bothan","Bothan","Bothans",tf_bothan|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,bothan_face1,bothan_face2],
["village_walker_chiss","Chiss","Chiss",tf_chiss|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,chiss_face1,chiss_face2],
["village_walker_chiss_female","Chiss Female","Chiss Female",tf_female|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_female_outfit_femconblack,itm_female_outfit_femconbrowngreen,itm_female_outfit_femcongrey,itm_female_outfit_femconorange,itm_female_outfit_femconwhite,itm_female_outfit_femconwhitebrown,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_white_cloak,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet,itm_black_boots,itm_leather_boots], def_attrib|level(4),wp(60),knows_common,chiss_female_face1,chiss_female_face2],
["village_walker_weequay","Weequay","Weequays",tf_weequay|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_weequay_head_helmet_a,itm_weequay_head_helmet_b,itm_guard_armor,itm_guard_armor_red,itm_vibro_axe_long_2h,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,weequay_face1,weequay_face2],
["village_walker_klatooinian","Klatooinian","Klatooinians",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_klatooinian_head_helmet_a,itm_leather_gloves,itm_guard_armor,itm_guard_armor_red,itm_vibro_axe_long_2h,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common, sw_man_face_1, sw_man_face_2],
["village_walker_nikto","Nikto","Niktos",tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_nikto_head_helmet_a,itm_nikto_head_helmet_b,itm_nikto_head_helmet_c,itm_leather_gloves,itm_guard_armor,itm_guard_armor_red,itm_vibro_axe_long_2h,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["village_walker_twilek","Twilek","Twileks",tf_twilek|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_ubese_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_laser_bolts_orange_pistol,itm_westar,itm_ddc_defender,itm_q2,itm_dl44a,itm_jacket_closed_a,itm_jacket_closed_b,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_c,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,twilek_face1,twilek_face2],
["village_walker_twilek_female","Twilek Female","Twilek Females",tf_twilek_female|tf_guarantee_armor|tf_guarantee_boots|tf_randomize_face,0,0,fac_commoners, [itm_female_outfit_femconblack,itm_female_outfit_femconbrowngreen,itm_female_outfit_femcongrey,itm_female_outfit_femconorange,itm_female_outfit_femconwhite,itm_female_outfit_femconwhitebrown,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_white_cloak,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet,itm_black_boots,itm_leather_boots], def_attrib|level(4),wp(60),knows_common,twilek_female_face1,twilek_female_face2],
["village_walker_twilek_female_slave","Twilek Slave","Twilek Slaves",tf_twilek_female|tf_guarantee_helmet|tf_randomize_face,0,0,fac_commoners, [itm_slave_neck_chain], def_attrib|level(4),wp(60),knows_common,twilek_female_face1,twilek_female_face2],
["village_walker_geonosian","Geonosian","geonosians",tf_geonosian|tf_randomize_face,0,0,fac_commoners, [itm_geonosian_sonic_pistol,itm_geonosian_sonic_rifle,itm_geonosian_static_pike,itm_geonosian_armor], def_attrib|level(4),wp(60),knows_common,geonosian_face1,geonosian_face2],
["village_walker_wookiee","Wookiee","Wookiees",tf_wookiee|tf_randomize_face,0,0,fac_commoners, [itm_wookiee_armor1,itm_wookiee_armor2,itm_ryyk_blade,itm_wookiee_bowcaster], def_attrib|level(4),wp(60),knows_common,wookiee_face1,wookiee_face2],
["village_walker_wookiee_female","Wookiee Female","Wookiee Females",tf_wookiee|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_wookiee_female_head,itm_wookiee_female_body,itm_wookiee_female_hands,itm_wookiee_female_feet], def_attrib|level(4),wp(60),knows_common,wookiee_face1,wookiee_face2],
["village_walker_gamorrean","Gamorrean","Gamorreans",tf_gamorrean|tf_randomize_face,0,0,fac_commoners, [itm_vibro_axe_medium_1h], def_attrib|level(4),wp(60),knows_common,gamorrean_face1,gamorrean_face2],
["village_walker_r2series","R2-Series Droid","R2-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_r2series_blue,itm_r2series_green,itm_r2series_orange,itm_r2series_purple,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_2,wp(60),droid_skills_2,droid_face1,droid_face2],
["village_walker_lin_droid","LIN Droid","LIN Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_lin_droid_armor,itm_lin_droid_armor,itm_lin_droid_armor_w_arm,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_2,wp(30),droid_skills_2,droid_face1,droid_face2],
["village_walker_mse6","MSE-6 Droid","MSE-6 Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_mse6_armor,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_1,wp(60),droid_skills_1,droid_face1,droid_face2],
["village_walker_3poseries","3PO-Series Droid","3PO-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_3poseries_gold,itm_3poseries_gold,itm_3poseries_blue,itm_3poseries_red,itm_3poseries_grey,itm_3poseries_grey,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_3poseries_attack], droid_attrib_2,wp(110),droid_skills_2,droid_face1,droid_face2],
["village_walker_3poseries_naked","3PO-Series Droid","3PO-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_3poseries_attack], droid_attrib_2,wp(110),droid_skills_2,droid_face1,droid_face2],
["village_walker_power_droid","Power Droid","Power Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_power_droid_tan,itm_power_droid_tan,itm_power_droid_grey,itm_power_droid_grey,itm_power_droid_snow,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_1,wp(60),droid_skills_1,droid_face1,droid_face2],
["village_walker_fxseries_droid","FX-Series Medical Droid","FX-Series Medical Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_fxseries_droid_armor,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_droid_weapon_no_attack], droid_attrib_1,wp(60),droid_skills_1,droid_face1,droid_face2],
["village_walker_hkseries","HK-Series Droid","HK-Series Droids",tf_droid|tf_guarantee_all_armor|tf_randomize_face,0,0,fac_commoners, [itm_hk_head,itm_hk_body,itm_hk_hands,itm_hk_feet], def_attrib_3|level(24),wp(150),starwars_skills_3,droid_face1,droid_face2],
["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_vibro_blade1,itm_vibro_blade2,itm_laser_bolts_orange_pistol,itm_westar,itm_q2,itm_dl44a,itm_civilian_cloak,itm_civilian_cloak_hood,itm_jacket_closed_a,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_vibro_blade1,itm_vibro_blade2,itm_laser_bolts_orange_pistol,itm_westar,itm_q2,itm_dl44a,itm_female_jacket_a,itm_female_jacket_b,itm_female_jacket_c,itm_female_outfit_femconblack,itm_female_outfit_femconbrowngreen,itm_female_outfit_femcongrey,itm_female_outfit_femconorange,itm_female_outfit_femconwhite,itm_female_outfit_femconwhitebrown,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress_yellow,itm_dress_red,itm_dress_green,itm_dress_blue,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_blue_dress,itm_white_cloak,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet,itm_black_boots,itm_leather_boots], def_attrib|level(2),wp(40),knows_common,sw_woman_face_1, sw_woman_face_2],
# Ryan END
["assassin_male","Assassin","Assassins",tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_laser_bolts_orange_rifle,itm_a295,itm_a295_crouch,itm_vibro_sword3_gold,itm_transparent_helmet,itm_ubese_armor,itm_leather_boots], def_attrib_3|level(24),wp(150),starwars_skills_3,sw_man_face_1, sw_man_face_2],
["assassin_rodian","Rodian Assassin","Rodian Assassins",tf_rodian|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_laser_bolts_orange_rifle,itm_a295,itm_a295_crouch,itm_vibro_sword3_gold,itm_rodian_ventilator,itm_rodian_ventilator_black,itm_rodian_ventilator_red,itm_transparent_helmet,itm_transparent_helmet,itm_vest_closed_b,itm_black_boots], def_attrib_3|level(24),wp(150),starwars_skills_3,rodian_face1,rodian_face2],
["assassin_trandoshan","Trandoshan Assassin","Trandoshan Assassins",tf_trandoshan|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_laser_bolts_orange_rifle,itm_trandoshan_acp_array_gun,itm_trandoshan_blade,itm_trandoshan_flight_suit,itm_trandoshan_armor,itm_transparent_helmet,itm_black_boots], def_attrib_3|level(24),wp(150),starwars_skills_3,trandoshan_face1,trandoshan_face2],
["assassin_twilek","Twilek Assassin","Twilek Assassins",tf_twilek|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_twilek_armor,itm_vibro_axe_long_2h,itm_laser_bolts_orange_rifle,itm_a295,itm_a295_crouch,itm_transparent_helmet,itm_leather_boots], def_attrib_3|level(24),wp(150),starwars_skills_3,twilek_face1,twilek_face2],
["assassin_mandalorian","Mandalorian Assassin","Mandalorian Assassins",tf_guarantee_all_armor|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_grey_gloves,itm_vibro_sword3_gold,itm_laser_bolts_orange_rifle,itm_mandalorian_heavy_blaster,itm_mandalorian_sniper_helmet,itm_mandalorian_sniper_armor,itm_mandalorian_sniper_boots], def_attrib_3|level(24),wp(150),starwars_skills_3,mandalorian_face1,mandalorian_face2],
["assassin_hkseries","HK-Series Assassin Droid","HK-Series Assassin Droids",tf_guarantee_all_armor|tf_guarantee_ranged|tf_randomize_face,0,0,fac_commoners, [itm_droid_parts,itm_hk_attack,itm_hk_head,itm_hk_body,itm_hk_hands,itm_hk_feet,itm_a280,itm_a295,itm_dlt19,itm_laser_bolts_orange_rifle,itm_laser_bolts_orange_rifle], def_attrib_3|level(24),wp(150),starwars_skills_3,droid_face1, droid_face2],

# Zendar (next troop is marked as spy_walkers_end)
["tournament_master","Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a,itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["trainer","Trainer","Trainer",tf_hero|tf_randomize_face, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a,itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero|tf_randomize_face, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_shirt,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
# Ryan BEGIN
#SW - modified Ramun_the_slave_trader
#["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero|tf_randomize_face, no_scene,reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["Ramun_the_slave_trader","Slave Trader","Slave Trader",tf_hero|tf_randomize_face, no_scene,reserved, fac_commoners,[itm_shirt,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["guide","Quick Jimmy","Quick Jimmy",tf_hero|tf_randomize_face, no_scene,0,  fac_commoners,[itm_coarse_tunic,itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1,sw_man_face_2],
# Ryan END
["Xerina","Xerina","Xerina",tf_hero|tf_female|tf_randomize_face, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_tunic_green,itm_hide_boots],def_attrib|str_15|agi_15|level(39),wp(312),knows_power_strike_5|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_athletics_8|knows_shield_3,sw_woman_face_1,sw_woman_face_2],
["Dranton","Dranton","Dranton",tf_hero|tf_randomize_face, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_tunic_green,itm_hide_boots],def_attrib|str_15|agi_14|level(42),wp(324),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,sw_man_face_1,sw_man_face_2],
["Kradus","Kradus","Kradus",tf_hero|tf_randomize_face, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_tunic_green,itm_hide_boots],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,sw_man_face_1,sw_man_face_2],
#Tutorial
["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero|tf_randomize_face, scn_training_ground|entry(2),reserved, fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a,itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],

#Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
["Galeas","Galeas","Galeas",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_shirt,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],

#Dhorak keep

["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor|tf_guarantee_boots,no_scene,reserved,fac_commoners, [itm_linen_tunic,itm_coarse_tunic,itm_shirt,itm_nomad_boots,itm_wrapping_boots], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],

["trainer_1","Trainer","Trainer",tf_hero|tf_randomize_face, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_officer_uniform_white,itm_black_boots],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["trainer_2","Trainer","Trainer",tf_hero|tf_randomize_face, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_officer_uniform_white,itm_black_boots],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["trainer_3","Trainer","Trainer",tf_hero|tf_randomize_face, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_officer_uniform_white,itm_black_boots],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["trainer_4","Trainer","Trainer",tf_hero|tf_randomize_face, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_officer_uniform_white,itm_black_boots],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["trainer_5","Trainer","Trainer",tf_hero|tf_randomize_face, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_officer_uniform_white,itm_black_boots],def_attrib|level(2),wp(20),knows_common,sw_man_face_1,sw_man_face_2],

# Ransom brokers.
["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_rich_outfit,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_rich_outfit,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_rich_outfit,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_rich_outfit,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_rich_outfit,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_rich_outfit,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_rich_outfit,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_rich_outfit,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_rich_outfit,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_rich_outfit,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],

# Tavern traveler.
["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_jacket_closed_a,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_jacket_closed_c,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_jacket_open_a,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_jacket_open_c,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_vest_closed_a,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_vest_open_a,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_vest_open_b,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_jacket_closed_a,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_jacket_closed_c,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],
["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_jacket_open_a,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],

# Tavern traveler.
#SW - switched Book_Merchant to Treasure Hunter (holocron's and possibly other rare items that give +1 to stats?)
#SW - added tavern_bookseller_#'s
["tavern_bookseller_1","Holocron Merchant","Holocron Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_rich_outfit,itm_leather_boots,itm_book_tactics,itm_book_persuasion,itm_book_leadership,itm_book_intelligence,itm_book_trade,itm_book_weapon_mastery,itm_book_engineering],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1,sw_man_face_2],
["tavern_bookseller_2","Holocron Merchant","Holocron Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_rich_outfit,itm_leather_boots,itm_book_tactics,itm_book_persuasion,itm_book_leadership,itm_book_intelligence,itm_book_trade,itm_book_weapon_mastery,itm_book_engineering],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1,sw_man_face_2],
["tavern_bookseller_3","Item Merchant","Item Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_scavenger_armor,itm_black_boots,itm_book_ironflesh_reference,itm_book_horse_archery_reference,itm_book_trade_reference,itm_book_wound_treatment_reference,itm_book_training_reference,itm_book_surgery_reference,itm_book_first_aid_reference,itm_book_tactics_reference],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_4","Item Merchant","Item Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_scavenger_armor,itm_black_boots,itm_book_ironflesh_reference,itm_book_horse_archery_reference,itm_book_trade_reference,itm_book_wound_treatment_reference,itm_book_training_reference,itm_book_surgery_reference,itm_book_first_aid_reference,itm_book_tactics_reference],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_5","Force-Sensitive Trainer","Force-Sensitive Trainers",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_jedi_robe_d,itm_leather_boots_reinforced],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_6","Force-Sensitive Trainer","Force-Sensitive Trainers",tf_hero|tf_female|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_jedi_robe_d,itm_leather_boots_reinforced],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_woman_face_1, sw_woman_face_2],
["tavern_bookseller_7","Clone Wars Era Merchant","Clone Era Merchants",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_clone_trooper_head,itm_clone_trooper_armor_mand,itm_clone_trooper_boots,itm_clone_trooper_gloves_red],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_8","Clone Wars Era Merchant","Clone Era Merchants",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_clone_trooper_head_scar,itm_clone_trooper_armor_mand,itm_clone_trooper_boots,itm_clone_trooper_gloves_red],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_9", "Illegal Weapons Merchant","Illegal Weapons Merchants",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_scavenger_armor,itm_black_boots],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_10","Illegal Weapons Merchant","Illegal Weapons Merchants",tf_hero|tf_female|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_female_jacket_c,itm_black_boots],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_woman_face_1, sw_woman_face_2],
#["tavern_bookseller_11","Droid Parts Merchant","Droid Parts Merchants",tf_hero|tf_droid|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,droid_face1, droid_face2],
#["tavern_bookseller_12","Droid Parts Merchant","Droid Parts Merchants",tf_hero|tf_droid|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,droid_face1, droid_face2],
["tavern_bookseller_11","Droid Parts Merchant","Droid Parts Merchants",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_outfit_grey,itm_black_boots],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_12","Droid Parts Merchant","Droid Parts Merchants",tf_hero|tf_female|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_female_jacket_b,itm_black_boots],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_woman_face_1, sw_woman_face_2],
["tavern_bookseller_13","Plastic Surgeon","Plastic Surgeons",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_jacket_closed_a,itm_leather_boots],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1,sw_man_face_2],
["tavern_bookseller_14","Plastic Surgeon","Plastic Surgeons",tf_hero|tf_female|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_female_jacket_a,itm_grey_boots],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_woman_face_1, sw_woman_face_2],
["tavern_bookseller_15","Force-Sensitive Merchant","Force-Sensitive Merchants",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_jedi_robe_e,itm_leather_boots_reinforced],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_man_face_1, sw_man_face_2],
["tavern_bookseller_16","Force-Sensitive Merchant","Force-Sensitive Merchants",tf_hero|tf_female|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_jedi_robe_e,itm_leather_boots_reinforced],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10,sw_woman_face_1, sw_woman_face_2],
# Tavern minstrel
["tavern_minstrel_1","Musician","Musicians",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_shirt,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,sw_man_face_1,sw_man_face_2],

#NPC system changes begin
#Companions

#SW - switched NPC's to Star Wars Characters, all now start at level 1, still need to update dialogs and some items
#SW - Borcha
["npc1","Kyle Katarn","Kyle Katarn",tf_hero|tf_unmoveable_in_party_window, 0, reserved,fac_commoners,[itm_jacket_open_a,itm_leather_boots,itm_laser_bolts_yellow_pistol,itm_dl44a,itm_vibro_blade3], str_14|agi_9|int_6|cha_5|level(6),wp(100),knows_weapon_master_4|knows_ironflesh_2|knows_athletics_3|knows_trainer_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_horse_archery_1, 0x000000003f00708136db6db6db6db6db00000000001db6db0000000000000000],
#SW - Marnid
["npc2","Rahm Kota","Rahm Kota", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_jedi_padawan_robe,itm_leather_boots,itm_lightsaber_green_1h,itm_force_power_ls_2,itm_force_push_ammo,itm_force_throw_lightsaber_green], str_16|agi_9|int_9|cha_4|level(10),wp(120)|wp_archery(140),knows_power_strike_4|knows_power_throw_4|knows_weapon_master_5|knows_inventory_management_2|knows_leadership_5|knows_shield_2|knows_trainer_2|knows_athletics_1|knows_tracking_1|knows_tactics_2|knows_power_draw_4, 0x000000000000c00e36db6db6db6db6db00000000001db6db0000000000000000],
#SW Ymira (female)
["npc3","Kyra Moryne","Kyra Moryne",tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_blue_dress,itm_blue_hose,itm_laser_bolts_yellow_pistol,itm_q2,itm_force_power_ls_1,itm_force_push_ammo],  str_12|agi_8|int_6|cha_6|level(1),wp(40)|wp_archery(40),knows_ironflesh_1|knows_weapon_master_2|knows_riding_1|knows_trade_1|knows_athletics_1|knows_power_throw_4|knows_inventory_management_1|knows_power_draw_2, sw_woman_face_1,sw_woman_face_2],
#SW - Rolf
["npc4","Dav Foss","Dav Foss",tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tunic_green,itm_leather_boots,itm_laser_bolts_yellow_pistol,itm_dl44a,itm_vibro_blade3], str_7|agi_6|int_12|cha_5|level(4),wp(65),knows_weapon_master_2|knows_riding_2|knows_horse_archery_2|knows_athletics_1|knows_spotting_3|knows_pathfinding_4|knows_engineer_1|knows_leadership_1|knows_tactics_2, sw_man_face_1,sw_man_face_2],
#SW - Baheshtur
["npc5","Trec Quizan","Trec Quizan",tf_weequay|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_shirt,itm_leather_boots,itm_vibro_blade3], str_12|agi_10|int_4|cha_5|level(3),wp(50),knows_ironflesh_3|knows_power_strike_1|knows_athletics_3|knows_trade_1|knows_trainer_1|knows_inventory_management_1|knows_first_aid_1|knows_shield_1, weequay_face1, weequay_face2],
#SW - Firentis
["npc6","Gaven Iscandar","Gaven Iscandar",tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_jacket_closed_b,itm_leather_boots,itm_laser_bolts_yellow_pistol,itm_westar,itm_vibro_blade3], str_11|agi_9|int_6|cha_9|level(4),wp(70),knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_looting_1|knows_riding_2|knows_horse_archery_1|knows_trade_2|knows_inventory_management_1|knows_weapon_master_3, sw_man_face_1,sw_man_face_2],
#SW - Deshavi (female)
["npc7","Jade Codi","Jade Codi",tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_dress_yellow,itm_laser_bolts_yellow_pistol,itm_q2,itm_vibro_blade3], str_5|agi_5|cha_13|int_10|level(2),wp(30),knows_athletics_1|knows_riding_1|knows_leadership_3|knows_weapon_master_1|knows_trade_4|knows_tactics_1, sw_woman_face_1,sw_woman_face_2],
#SW - Matheld (female)
["npc8","Dossok Snorkh","Dossok Snorkh",tf_trandoshan|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_jacket_closed_a,itm_leather_boots,itm_laser_bolts_yellow_pistol], str_5|agi_11|cha_10|int_4|level(2),wp(110),knows_ironflesh_2|knows_weapon_master_5|knows_spotting_2|knows_pathfinding_3|knows_athletics_4|knows_riding_3|knows_horse_archery_3, trandoshan_face1, trandoshan_face2],
#SW - Alayen
["npc9","Arvis Sunwright","Arvis Sunwright",tf_chiss|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_shirt,itm_leather_boots,itm_laser_bolts_yellow_pistol,itm_westar,itm_vibro_blade3], str_10|agi_12|int_8|cha_6|level(3),wp(60),knows_ironflesh_1|knows_weapon_master_2|knows_athletics_3|knows_riding_4|knows_horse_archery_2|knows_first_aid_1|knows_trade_2|knows_tactics_1|knows_leadership_2, chiss_face1, chiss_face2],
#SW - Bunduk
["npc10","Nerthak Beviin","Nerthak Beviin",tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_mandalorian_tunic,itm_leather_boots,itm_laser_bolts_yellow_rifle,itm_e11,itm_vibro_blade3], str_13|agi_10|int_8|cha_7|level(5),wp(110),knows_weapon_master_4|knows_engineer_2|knows_trade_1|knows_ironflesh_2|knows_power_strike_2|knows_tracking_1|knows_trainer_2|knows_pathfinding_1|knows_riding_2|knows_horse_archery_1|knows_leadership_3|knows_tactics_3, sw_man_face_1,sw_man_face_2],
#SW - Katrin (female)
["npc11","Luna Novar","Luna Novar",tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_blue_dress,itm_woolen_hose,itm_vibro_blade3], str_7|agi_8|int_13|cha_7|level(2),wp(80),knows_ironflesh_2|knows_power_strike_3|knows_weapon_master_1|knows_surgery_4|knows_first_aid_3|knows_wound_treatment_4|knows_trade_1|knows_engineer_1, sw_woman_face_1,sw_woman_face_2],
#SW - Jeremus
["npc12","Vaian Swogg","Vaian Swogg",tf_sullustan|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tunic_green,itm_leather_boots,itm_quarter_staff], str_11|agi_9|int_7|cha_6|level(1),wp(30),knows_ironflesh_3|knows_power_strike_3|knows_weapon_master_2|knows_trade_2|knows_tracking_2|knows_athletics_3|knows_inventory_management_3, sullustan_face1, sullustan_face2],
#SW - Nizar
["npc13","Tam Yarrow","Tam Yarrow",tf_rodian|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_shirt,itm_woolen_hose,itm_laser_bolts_yellow_pistol,itm_q2,itm_vibro_blade3], str_7|agi_9|int_8|cha_9|level(1),wp(50),knows_weapon_master_2|knows_inventory_management_3|knows_trade_4|knows_looting_2|knows_athletics_1|knows_riding_1|knows_shield_1, rodian_face1, rodian_face2],
#Lezalit
["npc14","Rath Varik","Rath Varik",tf_twilek|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tunic_white,itm_leather_boots,itm_laser_bolts_yellow_pistol,itm_westar,itm_vibro_blade3], str_10|agi_11|int_11|cha_5|level(6),wp(115),knows_ironflesh_2|knows_power_strike_2|knows_riding_2|knows_weapon_master_3|knows_horse_archery_1|knows_tracking_1|knows_pathfinding_1|knows_trainer_4|knows_leadership_2, twilek_face1, twilek_face2],
#SW - Artimenner
["npc15","Miriti Shoa","Miriti Shoa",tf_moncal|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_shirt,itm_leather_boots,itm_laser_bolts_yellow_pistol,itm_q2,itm_vibro_blade3], str_9|agi_8|int_13|cha_7|level(6),wp(70),knows_ironflesh_2|knows_power_strike_2|knows_riding_1|knows_engineer_4|knows_trainer_3|knows_tracking_1|knows_spotting_1|knows_tactics_1|knows_leadership_1|knows_weapon_master_2|knows_power_throw_2|knows_looting_1, moncal_face1, moncal_face2],
#SW - Klethi (female)
["npc16","Anela Kinse","Anela Kinse",tf_twilek_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_armor_white,itm_leather_boots,itm_laser_bolts_yellow_rifle,itm_kisteer_1284,itm_vibro_blade3], str_12|agi_13|int_9|cha_5|level(8),wp(115),knows_power_strike_3|knows_looting_2|knows_riding_2|knows_weapon_master_5|knows_athletics_4|knows_tracking_3|knows_spotting_2, twilek_female_face1, twilek_female_face2],
#NPC system changes end
#SW - new Droid NPC's
["npc17","B-2HO","B-2HO",tf_droid|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],  str_12|agi_4|int_6|cha_3|level(1),wp(25),knows_ironflesh_4|knows_weapon_master_4|knows_riding_1|knows_trade_2|knows_inventory_management_4, droid_face1, droid_face2],
["npc18","B-2KI","B-2KI",tf_droid|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[],  str_12|agi_4|int_6|cha_3|level(1),wp(25),knows_ironflesh_4|knows_weapon_master_4|knows_riding_1|knows_trade_2|knows_inventory_management_4, droid_face1, droid_face2],

["kingdom_heroes_including_player_begin", "kingdom_heroes_including_player_begin", "kingdom_heroes_including_player_begin", tf_hero|tf_randomize_face,0,reserved,fac_kingdom_1,[],lord_attrib,wp(220),knows_lord_1, sw_man_face_1,sw_man_face_2],

#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
["kingdom_1_lord",  "Emperor Palpatine",  "Kingdom 1 Lord",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_sith_hood,itm_sith_marauder_robe,itm_black_boots,itm_lightsaber_red,itm_force_protect,itm_force_power_ds_4,itm_force_lightning_ammo],lord_attrib,wp(300)|wp_archery(300),starwars_knight_skills_5|knows_power_draw_10, 0x0000000000012000249249249249249200000000001d24530000000000000000],
["kingdom_2_lord",  "Mon Mothma",  "Kingdom 2 Lord",  tf_female|tf_hero, 0,reserved,fac_kingdom_2,[itm_transparent_helmet_armor,itm_blue_dress,itm_woolen_hose,itm_laser_bolts_green_rifle,itm_a295,itm_vibro_blade1,itm_hero_shield],lord_attrib,wp(300),starwars_knight_skills_5, 0x0000000ceb00500436db49480049b6db00000000001db6db0000000000000000],
["kingdom_3_lord",  "Jabba the Hutt",  "Kingdom 3 Lord",  tf_hutt|tf_hero|tf_randomize_face, 0,reserved,  fac_kingdom_3,[itm_jabba_speeder,itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],  lord_attrib,wp(300),starwars_knight_skills_5, hutt_face1, hutt_face2],
  
#SW - commented out kingdom 4 & 5 lords
#  ["kingdom_4_lord",  "King Ragnar",  "Kingdom 4 Lord",  tf_hero, 0,reserved,  fac_kingdom_4,[itm_hunter,    itm_nobleman_outfit,    itm_leather_boots,              itm_mail_boots,                 itm_cuir_bouilli,           itm_scimitar,           itm_tab_shield_round_e,    itm_kettle_hat],            knight_attrib_5,wp(220),knight_skills_5|knows_trainer_4, 0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000, nord_face_older_2],
#  ["kingdom_5_lord",  "King Graveth",  "Kingdom 5 Lord",  tf_hero, 0,reserved,  fac_kingdom_5,[itm_warhorse,  itm_tabard,             itm_leather_boots,              itm_splinted_leather_greaves,   itm_heraldic_mail_with_tabard,           itm_lightsaber_kingdom5,         itm_tab_shield_heater_cav_b,        itm_spiked_helmet],         knight_attrib_3,wp(220),knight_skills_4|knows_trainer_5, 0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000, rhodok_face_old_2],

#    Imbrea   Belinda Ruby Qaelmas Rose    Willow 
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina  
# Dunga        Agatha     Dibus Crahask
  
#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
#Swadian civilian clothes: itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit itm_short_tunic itm_tabard

#SW - Galactic Empire Knights
# don't adjust skills much because it may lead to game in-balance?
#knight skill 5 - added tf_randomize_face to most
["knight_1_1", "Darth Vader", "knight_1_1", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_speeder_fc20,itm_darth_vader_helmet,itm_darth_vader_helmet,itm_darth_vader_armor,itm_darth_vader_armor,itm_black_boots,itm_black_gloves,itm_darth_vader_lightsaber,itm_darth_vader_lightsaber,itm_force_protect,itm_force_power_ds_4,itm_force_lightning_ammo,itm_force_throw_lightsaber_red],knight_attrib_5,wp(220)|wp_archery(220),starwars_knight_skills_5|knows_power_draw_9, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_2", "Grand Moff Tarkin", "knight_1_2", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_tarkin_head,itm_imperial_uniform_green,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_hero_shield,itm_vibro_blade4], knight_attrib_5,wp(220),starwars_knight_skills_5, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_3", "General Maximilian Veers", "knight_1_3", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_imperial_uniform_black,itm_imperial_hat_black,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_hero_shield,itm_vibro_blade4],knight_attrib_5,wp(220),starwars_knight_skills_5, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_4", "Grand General Malcor Brashin", "knight_1_4", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_imperial_uniform_black,itm_imperial_hat_black,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_large,itm_vibro_blade4], knight_attrib_5,wp(220),starwars_knight_skills_5, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_5", "Mara Jade", "knight_1_5", tf_female|tf_hero, 0, reserved,fac_kingdom_1, [itm_speeder_fc20,itm_transparent_helmet_armor,itm_sith_master_robe,itm_black_boots,itm_lightsaber_red,itm_force_protect,itm_force_power_ds_4,itm_force_lightning_ammo,itm_force_throw_lightsaber_red],knight_attrib_5,wp(220)|wp_archery(220),starwars_knight_skills_5|knows_power_draw_8, 0x000000018000500536db6d86026db6db00000000001db6db0000000000000000],
["knight_1_6", "Grand Inquisitor Malorum", "knight_1_6", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_speeder_fc20,itm_sith_hood,itm_sith_master_robe,itm_black_boots,itm_lightsaber_red,itm_force_power_ds_4,itm_force_lightning_ammo,itm_force_shield,itm_force_shield,itm_force_throw_lightsaber_red], knight_attrib_5,wp(220)|wp_archery(220),starwars_knight_skills_5|knows_power_draw_8, sw_sith_face_1, sw_sith_face_2],
["knight_1_7", "Major General Cass", "knight_1_7", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_imperial_uniform_black,itm_imperial_hat_black,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_hero_shield,itm_vibro_blade4], knight_attrib_5,wp(220),starwars_knight_skills_5, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_8", "Grand Admiral Thrawn", "knight_1_8", tf_chiss|tf_hero, 0, reserved,fac_kingdom_1, [itm_transparent_helmet_armor,itm_black_gloves,itm_officer_uniform_white,itm_black_boots,itm_vibro_blade4,itm_laser_bolts_red_rifle,itm_a280,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5, 0x0000000c3f01400436db6db6db6db6db00000000001db6db0000000000000000],
#knight skill 4 - added tf_randomize_face to most
["knight_1_9", "Inquisitor Ja'ce Yiaso", "knight_1_8", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_speeder_fc20,itm_sith_hood,itm_sith_master_robe,itm_black_boots,itm_lightsaber_red,itm_force_power_ds_4,itm_force_lightning_ammo,itm_force_protect,itm_force_throw_lightsaber_red],knight_attrib_4,wp(200)|wp_archery(200),starwars_knight_skills_4|knows_power_draw_7, sw_sith_face_1, sw_sith_face_2],
["knight_1_10", "Grand Admiral Gilad Pellaeon", "knight_1_9", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_imperial_uniform_black,itm_imperial_hat_black,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_hero_shield,itm_vibro_blade4],knight_attrib_4,wp(200),starwars_knight_skills_4, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_11", "General Rom Mohc", "knight_1_0", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_imperial_uniform_black,itm_imperial_hat_black,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_hero_shield,itm_vibro_blade4], knight_attrib_4,wp(200),starwars_knight_skills_4, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_12", "Colonel Wullf Yularen", "knight_1_1", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_imperial_uniform_black,itm_imperial_hat_black,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_hero_shield,itm_vibro_blade4], knight_attrib_4,wp(200),starwars_knight_skills_4, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_13", "Inquisitor Hydra", "knight_1_2", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_speeder_fc20,itm_sith_hood,itm_sith_master_robe,itm_black_boots,itm_lightsaber_red,itm_force_power_ds_4,itm_force_lightning_ammo,itm_force_shield,itm_force_throw_lightsaber_red],knight_attrib_4,wp(200)|wp_archery(200),starwars_knight_skills_4|knows_power_draw_7, sw_sith_face_1, sw_sith_face_2],
["knight_1_14", "Moff Jerjerrod", "knight_1_3", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_imperial_uniform_green,itm_imperial_hat_green,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_hero_shield,itm_vibro_blade4],knight_attrib_4,wp(200),starwars_knight_skills_4, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_15", "General Moradmin Bast", "knight_1_4", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_imperial_uniform_black,itm_imperial_hat_black,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_hero_shield,itm_vibro_blade4],knight_attrib_4,wp(200),starwars_knight_skills_4, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_16", "Inquisitor Onel'da", "knight_1_5", tf_hero|tf_twilek_female, 0, reserved,fac_kingdom_1, [itm_speeder_fc20,itm_transparent_helmet_armor,itm_lightsaber_red,itm_force_power_ds_4,itm_force_lightning_ammo,itm_force_shield,itm_force_throw_lightsaber_red], knight_attrib_4,wp(200)|wp_archery(200),starwars_knight_skills_4|knows_power_draw_7, 0x0000000d0000300036db6da44a6db6db00000000001db6db0000000000000000],
#knight skill 3 - added tf_randomize_face to most generic officer knights
["knight_1_17", "Grand Moff Trachta", "knight_1_6", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_imperial_uniform_green,itm_imperial_hat_green,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_hero_shield,itm_vibro_blade4], knight_attrib_3,wp(180),starwars_knight_skills_3, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_18", "Admiral Conan Antonio Motti", "knight_1_7", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_imperial_uniform_black,itm_imperial_hat_black,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_hero_shield,itm_vibro_blade4], knight_attrib_3,wp(180),starwars_knight_skills_3, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_19", "High General Cassio Tagge", "knight_1_8", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_imperial_uniform_black,itm_imperial_hat_black,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_hero_shield,itm_vibro_blade4], knight_attrib_3,wp(180),starwars_knight_skills_3, sw_imperial_face_1, sw_imperial_face_2],
["knight_1_20", "Grand Moff Argon", "knight_1_9", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_imperial_uniform_green,itm_imperial_hat_green,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_hero_shield,itm_vibro_blade4],knight_attrib_3,wp(180),starwars_knight_skills_3, sw_imperial_face_1, sw_imperial_face_2], 
["knight_1_21", "Admiral Firmus Piett", "knight_1_0", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_imperial_uniform_black,itm_imperial_hat_black,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_hero_shield,itm_vibro_blade4],knight_attrib_3,wp(180),starwars_knight_skills_3, sw_imperial_face_1, sw_imperial_face_2],  
#knight skill 2 - added tf_randomize_face to most generic officer knights
["knight_1_22", "Officer Mikin Leedine", "knight_1_2", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_23", "Officer Ratrian Oray", "knight_1_3", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_24", "Officer Beos Kutdine", "knight_1_4", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_25", "Officer Akareen Lighttrayn", "knight_1_5", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_26", "Officer Joreen Tarkdres", "knight_1_6", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_27", "Officer Kelnah Leesiri", "knight_1_7", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_28", "Officer Cedmel Krakin", "knight_1_8", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_29", "Officer Shiran Kraerre", "knight_1_9", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_30", "Officer Mobus Heldres", "knight_1_0", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_31", "Officer Jaron Ardcin", "knight_1_1", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_32", "Officer Savlif Skyhek", "knight_1_2", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_imperial_face_1, sw_imperial_face_2],   
#knight skill 1 - added tf_randomize_face to most generic officer knights
["knight_1_33", "Officer Raron Tarms", "knight_1_3", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_34", "Officer Shaka Selbaoth", "knight_1_4", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_35", "Officer Ratrian Terrray", "knight_1_5", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_36", "Officer Jaler Queldres", "knight_1_6", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_37", "Officer Zarax Nertrin", "knight_1_7", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_38", "Officer Wedra Leeonel", "knight_1_8", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_39", "Officer Nabron Faturus", "knight_1_9", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_40", "Officer Jasati Tarkkin", "knight_1_0", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_41", "Officer Lenmel Talwol", "knight_1_1", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_42", "Officer Jain Drykin", "knight_1_2", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_43", "Officer Kely Tarrak", "knight_1_3", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_44", "Officer Reric Kutlo", "knight_1_4", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
["knight_1_45", "Officer Milis Quallo", "knight_1_5", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red_rifle,itm_energy_shield_red_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# SW - switched 10 knights to be hutt cartel
# ["knight_1_46", "Officer Hasati Neldine", "knight_1_6", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_47", "Officer Elmi Nelma", "knight_1_7", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_48", "Officer Anabus Leesyn", "knight_1_8", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_49", "Officer Zalena Zarloinne", "knight_1_9", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_50", "Officer Reria Skyprin", "knight_1_0", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# added more imperial knights since they own more land then rebels3
# ["knight_1_51", "Officer Tyrkef Darkhrn", "knight_1_1", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_52", "Officer Pakric Nerprin", "knight_1_2", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_53", "Officer Ardrax Nayrus", "knight_1_3", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_54", "Officer Aeran Archran", "knight_1_4", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
# ["knight_1_55", "Officer Zalif Risik", "knight_1_5", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_1, [itm_officer_uniform_white,itm_officer_hat_white,itm_black_boots,itm_ee3,itm_laser_bolts_red,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_imperial_face_1, sw_imperial_face_2],   
 
#SW - Rebel Alliance Knights
# don't adjust skills much because it may lead to game in-balance?
#knight skill 5
["knight_2_1","Obi-Wan Kenobi","knight_2_1",tf_hero,0,reserved,fac_kingdom_2,[itm_transparent_helmet_armor,itm_force_protect,itm_force_throw_lightsaber_blue,itm_force_power_ls_4,itm_force_push_ammo,itm_jedi_master_robe,itm_leather_boots,itm_obi_wan_lightsaber,itm_obi_wan_lightsaber],knight_attrib_5,wp(220)|wp_archery(220),starwars_knight_skills_5|knows_power_draw_9,0x0000000fc00040c536db6db6d26db6db00000000001db6db0000000000000000],
["knight_2_2","Luke Skywalker","knight_2_2",tf_hero,0,reserved,fac_kingdom_2,[itm_speeder_rebel,itm_transparent_helmet_armor,itm_force_protect,itm_force_throw_lightsaber_green,itm_force_power_ls_4,itm_force_push_ammo,itm_right_hand_glove,itm_right_hand_glove,itm_luke_skywalker_outfit,itm_luke_skywalker_outfit,itm_black_boots,itm_luke_skywalker_lightsaber,itm_luke_skywalker_lightsaber],knight_attrib_5,wp(220)|wp_archery(220),starwars_knight_skills_5|knows_power_draw_8,0x000000000000000136db6db6d26db6db00000000001db6db0000000000000000],
["knight_2_3","General Jan Dodonna","knight_2_3",tf_hero|tf_randomize_face,0,reserved,fac_kingdom_2,[itm_transparent_helmet_armor,itm_a280,itm_laser_bolts_green_rifle,itm_rebel_uniform_tanblue,itm_leather_boots,itm_hero_shield,itm_vibro_blade3],knight_attrib_5,wp(220),starwars_knight_skills_5,sw_rebel_face_1, sw_rebel_face_2],
["knight_2_4","Chewbacca","knight_2_4",tf_hero|tf_wookiee|tf_randomize_face,0,reserved,fac_kingdom_2,[itm_speeder_rebel,itm_transparent_helmet_armor,itm_wookiee_armor1,itm_chewbacca_ryyk_blade,itm_chewbacca_ryyk_blade,itm_chewbacca_bowcaster,itm_chewbacca_bowcaster,itm_laser_bolts_green_rifle,itm_wookiee_shield_large],knight_attrib_5,wp(220),starwars_knight_skills_5,wookiee_face1, wookiee_face2],
["knight_2_5","Han Solo","knight_2_5",tf_hero,0,reserved,fac_kingdom_2,[itm_speeder_rebel,itm_transparent_helmet_armor,itm_han_solo_outfit,itm_han_solo_outfit,itm_black_boots,itm_laser_bolts_green_pistol,itm_han_solo_blaster,itm_han_solo_blaster,itm_vibro_sword3_gold,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5,0x0000000c7f00300136db6db6d26db6db00000000001db6db0000000000000000],
["knight_2_6","Lando Calrissian","knight_2_6",tf_hero,0,reserved,fac_kingdom_2,[itm_speeder_rebel,itm_transparent_helmet_armor,itm_shirt_blue,itm_black_boots,itm_laser_bolts_green_rifle,itm_a280,itm_vibro_sword3_gold,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5,0x0000000a7f010104249249249249249200000000001d24930000000000000000],
["knight_2_7","Leia Organa","knight_2_7",tf_female|tf_hero,0,reserved,fac_kingdom_2,[itm_transparent_helmet_armor,itm_princess_leia_blaster,itm_princess_leia_blaster,itm_princess_leia_outfit,itm_princess_leia_outfit,itm_woolen_hose,itm_laser_bolts_green_pistol,itm_hero_shield,itm_vibro_blade3],knight_attrib_5,wp(220),starwars_knight_skills_5,0x00000001bf00000836db6d86026db6db00000000001db6db0000000000000000],
["knight_2_8","Yoda","knight_2_8",tf_hero|tf_randomize_face,0,reserved,fac_kingdom_2,[itm_yoda_armor,itm_yoda_speeder,itm_yoda_lightsaber,itm_transparent_head,itm_transparent_hands,itm_transparent_feet,itm_force_protect,itm_force_throw_lightsaber_green,itm_force_power_ls_4,itm_force_push_ammo],knight_attrib_5,wp(220)|wp_archery(220),starwars_knight_skills_5|knows_power_draw_10,sw_rebel_face_1, sw_rebel_face_2],
["knight_2_9","Admiral Ackbar","knight_2_9",tf_hero|tf_moncal|tf_randomize_face,0,reserved,fac_kingdom_2,[itm_transparent_helmet_armor,itm_black_gloves,itm_officer_uniform_white,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_green_rifle,itm_a280,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5,moncal_face1, moncal_face2],
#knight skill 4
["knight_2_10","General Carlist Rieekan","knight_2_0",tf_hero|tf_randomize_face,0,reserved,fac_kingdom_2,[itm_transparent_helmet_armor,itm_rebel_uniform_tanblue,itm_leather_boots,itm_a280,itm_laser_bolts_green_rifle,itm_vibro_blade1,itm_hero_shield],knight_attrib_4,wp(200),starwars_knight_skills_4,sw_rebel_face_1, sw_rebel_face_2],
["knight_2_11","General Crix Madine","knight_2_1",tf_hero|tf_randomize_face,0,reserved,fac_kingdom_2,[itm_transparent_helmet_armor,itm_rebel_uniform_tanblue,itm_leather_boots,itm_a280,itm_laser_bolts_green_rifle,itm_vibro_blade1,itm_hero_shield],knight_attrib_4,wp(200),starwars_knight_skills_4,sw_rebel_face_1, sw_rebel_face_2],
["knight_2_12","General Pharl McQuarrie","knight_2_2",tf_hero|tf_randomize_face,0,reserved,fac_kingdom_2,[itm_transparent_helmet_armor,itm_rebel_uniform_tanblue,itm_leather_boots,itm_a280,itm_laser_bolts_green_rifle,itm_vibro_blade1,itm_hero_shield],knight_attrib_4,wp(200),starwars_knight_skills_4,sw_rebel_face_1, sw_rebel_face_2],
["knight_2_13","Major Bren Derlin","knight_2_3",tf_hero|tf_randomize_face,0,reserved,fac_kingdom_2,[itm_transparent_helmet_armor,itm_rebel_uniform_tanblue,itm_leather_boots,itm_a280,itm_laser_bolts_green_rifle,itm_vibro_blade1,itm_hero_shield],knight_attrib_4,wp(200),starwars_knight_skills_4,sw_rebel_face_1, sw_rebel_face_2],
["knight_2_14","Captain Yutani","knight_2_4",tf_hero|tf_randomize_face,0,reserved,fac_kingdom_2,[itm_transparent_helmet_armor,itm_rebel_uniform_tanblue,itm_leather_boots,itm_a280,itm_laser_bolts_green_rifle,itm_vibro_blade1,itm_hero_shield],knight_attrib_4,wp(200),starwars_knight_skills_4,sw_rebel_face_1, sw_rebel_face_2],
["knight_2_15","Lieutenant Greeve","knight_2_5",tf_hero|tf_randomize_face,0,reserved,fac_kingdom_2,[itm_transparent_helmet_armor,itm_rebel_uniform_tanblue,itm_leather_boots,itm_a280,itm_laser_bolts_green_rifle,itm_vibro_blade1,itm_hero_shield],knight_attrib_4,wp(200),starwars_knight_skills_4,sw_rebel_face_1, sw_rebel_face_2],
["knight_2_16","Corran Horn","knight_2_6",tf_hero,0,reserved,fac_kingdom_2,[itm_speeder_rebel,itm_transparent_helmet_armor,itm_republic_pilot_armor,itm_black_boots,itm_black_gloves,itm_laser_bolts_green_pistol,itm_dh17,itm_hero_shield,itm_vibro_sword3_gold],knight_attrib_4,wp(200),starwars_knight_skills_4,0x000000003f00500536db6db6db6db6db00000000001db6db0000000000000000],
["knight_2_17","Wes Janson","knight_2_7",tf_hero|tf_randomize_face,0,reserved,fac_kingdom_2,[itm_speeder_rebel,itm_transparent_helmet_armor,itm_republic_pilot_armor,itm_black_boots,itm_black_gloves,itm_laser_bolts_green_pistol,itm_dh17,itm_hero_shield,itm_vibro_sword3_gold],knight_attrib_4,wp(200),starwars_knight_skills_4,sw_man_face_1,sw_man_face_2],
["knight_2_18","Wedge Antilles","knight_2_8",tf_hero,0,reserved,fac_kingdom_2,[itm_speeder_rebel,itm_transparent_helmet_armor,itm_republic_pilot_armor,itm_black_boots,itm_black_gloves,itm_laser_bolts_green_pistol,itm_dh17,itm_hero_shield,itm_vibro_sword3_gold],knight_attrib_4,wp(200),starwars_knight_skills_4, 0x000000003f00400636db6db6db6db6db00000000001db6db0000000000000000],
#knight skill 3 - added tf_randomize_face to most generic commander knights
["knight_2_19","Arvel Crynyd","knight_2_9",tf_hero|tf_randomize_face,0,reserved,fac_kingdom_2,[itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_a280,itm_laser_bolts_green_rifle,itm_vibro_blade1,itm_hero_shield],knight_attrib_3,wp(180),starwars_knight_skills_3,sw_rebel_face_1, sw_rebel_face_2],
["knight_2_20","Nik Sant","knight_2_0",tf_hero,0,reserved,fac_kingdom_2,[itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_a280,itm_laser_bolts_green_rifle,itm_vibro_blade1,itm_hero_shield],knight_attrib_3,wp(180),starwars_knight_skills_3,0x0000000fc000124526d46d34db6dc95c00000000001db8d30000000000000000],
["knight_2_21", "Derek Klivian", "knight_2_1", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_hero_shield,itm_vibro_blade4],knight_attrib_3,wp(180),starwars_knight_skills_3, sw_rebel_face_1, sw_rebel_face_2],   
#use energy shields below this point
["knight_2_22", "Commander Elte Tuntrin", "knight_2_2", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_energy_shield_green_small,itm_vibro_blade4],knight_attrib_3,wp(180),starwars_knight_skills_3, sw_rebel_face_1, sw_rebel_face_2],   
["knight_2_23", "Commander Shiy Facken", "knight_2_3", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_energy_shield_green_small,itm_vibro_blade4],knight_attrib_3,wp(180),starwars_knight_skills_3, sw_rebel_face_1, sw_rebel_face_2],   
["knight_2_24", "Commander Jomi Torwalker", "knight_2_4", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_energy_shield_green_small,itm_vibro_blade4],knight_attrib_3,wp(180),starwars_knight_skills_3, sw_rebel_face_1, sw_rebel_face_2],   
["knight_2_25", "Commander Shay Kracin", "knight_2_5", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_energy_shield_green_small,itm_vibro_blade4],knight_attrib_3,wp(180),starwars_knight_skills_3, sw_rebel_face_1, sw_rebel_face_2],   
#knight skill 2 - added tf_randomize_face to most generic commander knights
["knight_2_26", "Commander Dakan Talik", "knight_2_6", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_energy_shield_green_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
["knight_2_27", "Commander Celnia Terrles", "knight_2_7", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_energy_shield_green_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
["knight_2_28", "Commander Jeran Ardtrin", "knight_2_8", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_energy_shield_green_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
["knight_2_29", "Commander Corsati Berles", "knight_2_9", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_energy_shield_green_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
["knight_2_30", "Commander Shin Lightrus", "knight_2_0", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_energy_shield_green_small,itm_vibro_blade4],knight_attrib_2,wp(160),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
#knight skill 1 - added tf_randomize_face to most generic commander knights
["knight_2_31", "Commander Janah Talik", "knight_2_1", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_energy_shield_green_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
["knight_2_32", "Commander Lerek Terrtrayn", "knight_2_2", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_energy_shield_green_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
["knight_2_33", "Commander Rhyin Quellan", "knight_2_3", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_energy_shield_green_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
["knight_2_34", "Commander Ardlena Sanhek", "knight_2_4", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_energy_shield_green_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
["knight_2_35", "Commander Pakric Cynekin", "knight_2_5", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_transparent_helmet,itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green_rifle,itm_energy_shield_green_small,itm_vibro_blade4],knight_attrib_1,wp(140),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   

# SW - commented out since imperials should have more knights since they own more land/castles, also moved some knights to the hutt cartel
# ["knight_2_36", "Commander Mios Darkker", "knight_2_6", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_2,wp(130),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_37", "Commander Wein Lorkin", "knight_2_7", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_2,wp(130),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_38", "Commander Tenke Krahek", "knight_2_8", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_2,wp(130),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_39", "Commander Akalla Sanlan", "knight_2_9", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_2,wp(130),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_40", "Commander Marric Terrel", "knight_2_0", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_2,wp(130),starwars_knight_skills_2, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_41", "Commander Karkin Lorwol", "knight_2_1", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_42", "Commander Melkef Wolfsiri", "knight_2_2", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_43", "Commander Kelcus Torilles", "knight_2_3", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_44", "Commander Marbus Krahrn", "knight_2_4", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_45", "Commander Jagent Loin", "knight_2_5", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_46", "Commander X", "knight_2_6", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_47", "Commander X", "knight_2_7", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_48", "Commander X", "knight_2_8", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_49", "Commander X", "knight_2_9", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   
# ["knight_2_50", "Commander X", "knight_2_0", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_2, [itm_rebel_uniform_green,itm_leather_boots,itm_ee3,itm_laser_bolts_green,itm_energy_shield_yellow_small,itm_vibro_blade4],knight_attrib_1,wp(120),starwars_knight_skills_1, sw_rebel_face_1, sw_rebel_face_2],   

#SW - Hutt Cartel Knights
# don't adjust skills much because it may lead to game in-balance?
#knight skill 5
["knight_3_1", "Boba Fett", "knight_3_1", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_speeder_hutt,itm_grey_gloves,itm_grey_gloves,itm_boba_fett_armor,itm_boba_fett_armor,itm_boba_fett_boots,itm_boba_fett_boots,itm_boba_fett_helmet,itm_boba_fett_helmet,itm_boba_fett_blaster,itm_boba_fett_blaster,itm_laser_bolts_orange_rifle,itm_laser_bolts_orange_rifle,itm_vibro_sword3_gold,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5, mandalorian_face1, mandalorian_face2],
["knight_3_2", "Bib Fortuna", "knight_3_2", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_twilek_male_head_bib,itm_hutt_palace_guard_armor,itm_grey_boots,itm_grey_gloves,itm_dl18,itm_laser_bolts_orange_pistol,itm_twilek_dagger,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5, sw_hutt_face_1, sw_hutt_face_2],
["knight_3_3", "Queequeg", "knight_3_3", tf_hero|tf_weequay|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_transparent_helmet,itm_speeder_hutt,itm_skiff_guard_armor_brown,itm_skiff_guard_armor_grey,itm_skiff_guard_armor_white,itm_hide_boots,itm_vibro_axe_long_2h,itm_laser_bolts_orange_rifle,itm_ee3,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5, weequay_face1, weequay_face2], 
["knight_3_4", "Weequay", "knight_3_4", tf_hero|tf_weequay|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_transparent_helmet,itm_speeder_hutt,itm_skiff_guard_armor_brown,itm_skiff_guard_armor_grey,itm_skiff_guard_armor_white,itm_hide_boots,itm_weequay_vibro_axe,itm_weequay_vibro_axe,itm_laser_bolts_orange_rifle,itm_ee3,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5, weequay_face1, weequay_face2], 
["knight_3_5", "Bossk", "knight_3_5", tf_hero|tf_trandoshan|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_speeder_hutt,itm_transparent_helmet,itm_trandoshan_flight_suit,itm_leather_boots,itm_a280,itm_laser_bolts_orange_rifle,itm_vibro_sword3_gold,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5, trandoshan_face1, trandoshan_face2],  
["knight_3_6", "Dengar", "knight_3_6", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_speeder_hutt,itm_dengar_armor,itm_dengar_armor,itm_dengar_helmet,itm_dengar_helmet,itm_dengar_boots,itm_dengar_boots,itm_dengar_gloves,itm_dengar_gloves,itm_dlt19_scope,itm_dlt19_scope,itm_westar_shield,itm_westar_shield,itm_vibro_sword3_gold,itm_laser_bolts_orange_rifle,itm_laser_bolts_orange_rifle],knight_attrib_5,wp(220),starwars_knight_skills_5, mandalorian_face1, mandalorian_face2], 
["knight_3_7", "Zuckuss", "knight_3_7", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_speeder_hutt,itm_transparent_helmet,itm_padded_armor_white,itm_leather_boots,itm_a280,itm_laser_bolts_orange_rifle,itm_vibro_sword3_gold,itm_hero_shield],knight_attrib_5,wp(220),starwars_knight_skills_5, sw_hutt_face_1, sw_hutt_face_2], 
#knight skill 4
["knight_3_8", "Barada", "knight_3_8", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_klatooinian_head_helmet_a,itm_armor_red,itm_leather_boots,itm_leather_gloves,itm_pipe1,itm_laser_bolts_orange_rifle,itm_ee3,itm_hero_shield],knight_attrib_4,wp(200),starwars_knight_skills_4, weequay_face1, weequay_face2], 
["knight_3_9", "Greedo", "knight_3_9", tf_hero|tf_rodian|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_speeder_hutt,itm_transparent_helmet,itm_padded_armor_white,itm_leather_boots,itm_leather_gloves,itm_a280,itm_laser_bolts_orange_rifle,itm_vibro_sword3_gold,itm_hero_shield],knight_attrib_4,wp(200),starwars_knight_skills_4, rodian_face1, rodian_face2], 
["knight_3_10", "Xob", "knight_3_0", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_4,wp(200),starwars_knight_skills_4, gamorrean_face1, gamorrean_face2], 
["knight_3_11", "Ortugg", "knight_3_1", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_4,wp(200),starwars_knight_skills_4, gamorrean_face1, gamorrean_face2], 
["knight_3_12", "Gartogg", "knight_3_2", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_4,wp(200),starwars_knight_skills_4, gamorrean_face1, gamorrean_face2], 
["knight_3_13", "Jubnuk", "knight_3_3", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_4,wp(200),starwars_knight_skills_4, sw_hutt_face_1, gamorrean_face1, gamorrean_face2], 
["knight_3_14", "Rogua", "knight_3_4", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_4,wp(200),starwars_knight_skills_4, gamorrean_face1, gamorrean_face2], 
#knight skill 3
["knight_3_15", "Thok", "knight_3_5", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_3,wp(180),starwars_knight_skills_3, gamorrean_face1, gamorrean_face2], 
["knight_3_16", "Thug", "knight_3_6", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_3,wp(180),starwars_knight_skills_3, gamorrean_face1, gamorrean_face2], 
["knight_3_17", "Warlug", "knight_3_7", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_3,wp(180),starwars_knight_skills_3, gamorrean_face1, gamorrean_face2], 
["knight_3_18", "Tront", "knight_3_8", tf_hero|tf_gamorrean|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_transparent_helmet,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_a280,itm_laser_bolts_orange_rifle,itm_durasteel_shield_small],knight_attrib_3,wp(180),starwars_knight_skills_3, gamorrean_face1, gamorrean_face2], 
["knight_3_19", "Malakili", "knight_3_9", tf_hero, 0, reserved,fac_kingdom_3, [itm_rancor_keeper_armor,itm_rancor_keeper_hat,itm_wrapping_boots,itm_dl18,itm_laser_bolts_orange_pistol,itm_tusken_gaffi_stick,itm_energy_shield_yellow_small],knight_attrib_3,wp(180),starwars_knight_skills_3, 0x0000000b6100500736db6db6db6db6db00000000001db6db0000000000000000], 
["knight_3_20", "Nizuc Bek", "knight_3_0", tf_hero|tf_randomize_face, 0, reserved,fac_kingdom_3, [itm_transparent_helmet,itm_padded_armor_white,itm_leather_boots,itm_dl18,itm_laser_bolts_orange_pistol,itm_vibro_blade1,itm_hero_shield],knight_attrib_3,wp(180),starwars_knight_skills_3, sw_hutt_face_1, sw_hutt_face_2], 
 
#knight skill 4
# etc... 
#SW - deleted kingdom 4 knights, for later use for Independants?
#SW -deleted kingdom 5 knights, for later use for Smugglers Alliance?

#Own kingdom start------------------------------
  ["reserved_knight_1", "Commander Pechnak", "knight_6_1", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],     knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_2", "Commander Daynad", "knight_6_2", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral,  [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],     knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_3", "Commander Joayah", "knight_6_3", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral,  [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_4", "Commander Marlund", "knight_6_4", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_5", "Commander Taarl", "knight_6_5", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral,   [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium], knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_6", "Commander Euscarl", "knight_6_6", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_7", "Commander Sigmar", "knight_6_7", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral,  [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],     knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_8", "Commander Talesqe", "knight_6_8", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_9", "Commander Aels", "knight_6_9", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral,    [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],   knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_10", "Commander Raurqe", "knight_6_0", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],  knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_11", "Commander Bragamus", "knight_6_1", tf_hero|tf_randomize_face, 0, reserved, fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],     knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_12", "Commander Ramin", "knight_6_2", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],     knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_13", "Commander Shulk", "knight_6_3", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_14", "Commander Putar", "knight_6_4", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_15", "Commander Reichad", "knight_6_5", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium], knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_16", "Commander Walcheas", "knight_6_6", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_17", "Commander Rulkh", "knight_6_7", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],     knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_18", "Commander Ramar", "knight_6_8", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],    knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_19", "Commander Caldaran", "knight_6_9", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],   knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
  ["reserved_knight_20", "Commander Brabas", "knight_6_0", tf_hero|tf_randomize_face, 0, reserved,  fac_neutral, [itm_transparent_helmet,itm_jacket_closed_b,itm_jacket_closed_b,itm_black_boots,itm_black_boots,itm_vibro_blade1,itm_vibro_blade3,itm_laser_bolts_yellow_rifle,itm_laser_bolts_yellow_rifle,itm_a295,itm_energy_shield_yellow_medium,itm_energy_shield_yellow_medium],  knight_attrib_4,wp(200),starwars_knight_skills_4, sw_man_face_1,sw_man_face_2],
#Own kingdom end------------------------------

#SW - commented out kingdom # pretenders
#  ["kingdom_1_pretender",  "Lady Isolla of Suno",       "Kingdom 1 Lord",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_1,[itm_charger,   itm_rich_outfit,  itm_blue_hose,      itm_iron_greaves,         itm_mail_shirt,      itm_sword_medieval_c_small,      itm_tab_shield_small_round_c,       itm_bascinet],          lord_attrib,wp(220),knows_lord_1, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
#claims pre-salic descent

#  ["kingdom_2_pretender",  "Prince Valdym the Bastard", "Kingdom 2 Lord",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_2,[itm_hunter,    itm_courtly_outfit,      itm_leather_boots,              itm_mail_chausses,              itm_lamellar_cuirass,       itm_military_pick,      itm_tab_shield_heater_b,      itm_flat_topped_helmet],    lord_attrib,wp(220),knows_lord_1, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, vaegir_face_middle_2],
#had his patrimony falsified

#  ["kingdom_3_pretender",  "Dustum Khan",               "Kingdom 3 Lord",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_3,[itm_courser,   itm_nomad_robe,             itm_leather_boots,              itm_splinted_greaves,           itm_khergit_guard_armor,         itm_vibro_blade3,              itm_tab_shield_small_round_c,       itm_segmented_helmet],      lord_attrib,wp(220),knows_lord_1, 0x000000065504310b30d556b51238f66100000000001c256d0000000000000000, khergit_face_middle_2],
#of the family

#  ["kingdom_4_pretender",  "Lethwin Far-Seeker",   "Kingdom 4 Lord",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_4,[itm_hunter,    itm_tabard,    itm_leather_boots,              itm_mail_boots,                 itm_brigandine_a,           itm_sword_medieval_c,           itm_tab_shield_heater_cav_a,    itm_kettle_hat],            lord_attrib,wp(220),knows_lord_1, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
#dispossessed and wronged

#  ["kingdom_5_pretender",  "Lord Kastor of Veluca",  "Kingdom 5 Lord",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_5,[itm_warhorse,  itm_nobleman_outfit,             itm_leather_boots,              itm_splinted_leather_greaves,   itm_mail_hauberk,           itm_sword_medieval_c,         itm_tab_shield_heater_d,        itm_spiked_helmet],         lord_attrib,wp(220),knows_lord_1, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
#republican

##  ["kingdom_1_lord_a", "Kingdom 1 Lord A", "Kingdom 1 Lord A", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_b", "Kingdom 1 Lord B", "Kingdom 1 Lord B", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_c", "Kingdom 1 Lord C", "Kingdom 1 Lord C", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_d", "Kingdom 1 Lord D", "Kingdom 1 Lord D", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_e", "Kingdom 1 Lord E", "Kingdom 1 Lord E", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_f", "Kingdom 1 Lord F", "Kingdom 1 Lord F", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_g", "Kingdom 1 Lord G", "Kingdom 1 Lord G", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_h", "Kingdom 1 Lord H", "Kingdom 1 Lord H", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_i", "Kingdom 1 Lord I", "Kingdom 1 Lord I", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_j", "Kingdom 1 Lord J", "Kingdom 1 Lord J", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_k", "Kingdom 1 Lord K", "Kingdom 1 Lord K", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_l", "Kingdom 1 Lord L", "Kingdom 1 Lord L", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_m", "Kingdom 1 Lord M", "Kingdom 1 Lord M", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_n", "Kingdom 1 Lord N", "Kingdom 1 Lord N", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],



#  ["town_1_ruler_a", "King Harlaus",  "King Harlaus",  tf_hero, scn_town_1_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_courtly_outfit,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010908101e36db44b75b6dd],
#  ["town_2_ruler_a", "Duke Taugard",  "Duke Taugard",  tf_hero, scn_town_2_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_courtly_outfit,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000310401e06db86375f6da],
#  ["town_3_ruler_a", "Count Grimar",  "Count Grimar",  tf_hero, scn_town_3_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004430301e46136eb75bc0a],
#  ["town_4_ruler_a", "Count Haxalye", "Count Haxalye", tf_hero, scn_town_4_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010918701e77136e905bc0e
#  ["town_5_ruler_a", "Count Belicha", "Count Belicha", tf_hero, scn_town_5_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000421c801e7713729c5b8ce],
#  ["town_6_ruler_a", "Count Nourbis", "Count Nourbis", tf_hero, scn_town_6_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c640501e371b72bcdb724],
#  ["town_7_ruler_a", "Count Rhudolg", "Count Rhudolg", tf_hero, scn_town_7_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c710201fa51b7286db721],
 
#  ["town_8_ruler_b", "King Yaroglek", "King_yaroglek", tf_hero, scn_town_8_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000128801f294ca6d66d555],
#  ["town_9_ruler_b", "Count Aolbrug", "Count_Aolbrug", tf_hero, scn_town_9_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004234401f26a271c8d38ea],
#  ["town_10_ruler_b","Count Rasevas", "Count_Rasevas", tf_hero, scn_town_10_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000001032c201f38e269372471c],
#  ["town_11_ruler_b","Count Leomir",  "Count_Leomir",  tf_hero, scn_town_11_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c538001f55148936d3895],
#  ["town_12_ruler_b","Count Haelbrad","Count_Haelbrad",tf_hero, scn_town_12_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000410c701f38598ac8aaaab],
#  ["town_13_ruler_b","Count Mira",    "Count_Mira",    tf_hero, scn_town_13_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004204401f390c515555594],
#  ["town_14_ruler_b","Count Camechaw","Count_Camechaw",tf_hero, scn_town_14_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],

##  ["kingdom_2_lord_a", "Kingdom 2 Lord A", "Kingdom 2 Lord A", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_b", "Kingdom 2 Lord B", "Kingdom 2 Lord B", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_c", "Kingdom 2 Lord C", "Kingdom 2 Lord C", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_d", "Kingdom 2 Lord D", "Kingdom 2 Lord D", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_e", "Kingdom 2 Lord E", "Kingdom 2 Lord E", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_f", "Kingdom 2 Lord F", "Kingdom 2 Lord F", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_g", "Kingdom 2 Lord G", "Kingdom 2 Lord G", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_h", "Kingdom 2 Lord H", "Kingdom 2 Lord H", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_i", "Kingdom 2 Lord I", "Kingdom 2 Lord I", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_j", "Kingdom 2 Lord J", "Kingdom 2 Lord J", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_k", "Kingdom 2 Lord K", "Kingdom 2 Lord K", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_l", "Kingdom 2 Lord L", "Kingdom 2 Lord L", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_m", "Kingdom 2 Lord M", "Kingdom 2 Lord M", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_n", "Kingdom 2 Lord N", "Kingdom 2 Lord N", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],



#Royal family members
#SW - commented out kingdom # wives, daughters
#  ["knight_1_1_wife","Lady Anna","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
#  ["knight_2_1_wife","Lady Junitha","knight_2_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
#  ["knight_3_1_wife","Lady Borge","knight_3_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_nomad_vest,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
#  ["knight_4_1_wife","Lady Jadeth","knight_4_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress , itm_wimple_with_veil,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
#  ["knight_5_1_wife","Lady Brina","knight_5_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],

#  ["knight_1_2_wife","Lady Nelda","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
#   ["knight_2_2_wife","Lady Katia","knight_2_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
#  ["knight_3_2_wife","Lady Tuan","knight_3_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_nomad_vest,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
#  ["knight_4_2_wife","Lady Miar","knight_4_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress , itm_wimple_with_veil,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
#  ["knight_5_2_wife","Lady Aliena","knight_5_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],

#  ["knight_1_1_daughter","Lady Bela","knight_1_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_lady_dress_blue,    itm_turret_hat_blue,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
#  ["knight_2_1_daughter","Lady Seomis","knight_2_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_peasant_dress ,   itm_wimple_with_veil,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
#  ["knight_3_1_daughter","Lady Chedina","knight_3_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_nomad_robe ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
#  ["knight_4_1_daughter","Lady Dria","knight_4_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
#  ["knight_5_1_daughter","Lady Aneth","knight_5_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,   itm_wimple_with_veil,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],

#  ["knight_1_2_daughter","Lady Elina","knight_1_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_lady_dress_blue,    itm_turret_hat_blue,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
#  ["knight_2_2_daughter","Lady Drina","knight_2_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_peasant_dress ,   itm_wimple_with_veil,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
#  ["knight_3_2_daughter","Lady Ayasu","knight_3_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_nomad_robe ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
#  ["knight_4_2_daughter","Lady Glunde","knight_4_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
#  ["knight_5_2_daughter","Lady Reada","knight_5_1_daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,   itm_wimple_with_veil,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],

#  ["kingdom_11_lord_daughter","kingdom_11_lord_daughter","kingdom_11_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008300701c08d34a450ce43],
#  ["kingdom_13_lord_daughter","kingdom_13_lord_daughter","kingdom_13_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008000401db10a45b41d6d8],
##  ["kingdom_1_lady_a","kingdom_1_lady_a","kingdom_1_lady_a",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],
##  ["kingdom_1_lady_b","kingdom_1_lady_b","kingdom_1_lady_b",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000101c3ae68e0e944ac],
##  ["kingdom_2_lady_a","Kingdom 2 Lady a","Kingdom 2 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008100501d8ad93708e4694],
##  ["kingdom_2_lady_b","Kingdom 2 Lady b","Kingdom 2 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000401d8ad93708e4694],
##  ["kingdom_3_lady_a","Kingdom 3 Lady a","Kingdom 3 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_3, [               itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500301d8ad93708e4694],
##
##  ["kingdom_3_lady_b","Kingdom 3 Lady b","Kingdom 3 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_3,  [                         itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100601d8b08d76d14a24],
##  ["kingdom_4_lady_a","Kingdom 4 Lady a","Kingdom 4 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500601d8ad93708e4694],
##  ["kingdom_4_lady_b","Kingdom 4 Lady b","Kingdom 4 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],

["heroes_end", "heroes end", "heroes end", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_speeder,itm_shirt,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_kingdom_1,[itm_courser,            itm_fighting_axe,       itm_leather_jerkin,         itm_leather_boots,          itm_straw_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008200201e54c137a940c91],
##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_kingdom_2,[itm_saddle_horse,       itm_arming_sword,       itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000000601db6db6db6db6db],
##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_kingdom_3,[itm_courser,            itm_nordic_sword,       itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008100701db6db6db6db6db],
##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_kingdom_4,[itm_saddle_horse,       itm_falchion,           itm_light_leather,          itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401e54c137a945c91],
##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_kingdom_5,[itm_saddle_horse,       itm_sword,              itm_ragged_outfit,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008038001e54c135a945c91],
##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_kingdom_1,[itm_saddle_horse,      itm_scimitar,           itm_leather_jerkin,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000248e01e54c1b5a945c91],
##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_kingdom_2,[itm_hunter,            itm_arming_sword,       itm_padded_leather,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004200601c98ad39c97557a],
##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_kingdom_3,[itm_saddle_horse,      itm_nordic_sword,       itm_light_leather,          itm_leather_boots,          itm_woolen_hood],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001095ce01d6aad3a497557a],
##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_kingdom_4,[itm_saddle_horse,      itm_sword,              itm_padded_leather,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010519601ec26ae99898697],
##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000884c401f6837d3294e28a],
##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c450501e289dd2c692694],
##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_falchion,           itm_leather_jerkin,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c660a01e5af3cb2763401],
##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[itm_sumpter_horse,      itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001001d601ec912a89e4d534],
##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[itm_courser,            itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004335601ea2c04a8b6a394],
##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_padded_leather,         itm_woolen_hose,            itm_fur_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008358e01dbf27b6436089d],
##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c300101db0b9921494add],
##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008740f01e945c360976a0a],
##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008020c01fc2db3b4c97685],
##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_falchion,           itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008118301f02af91892725b],
##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_courser,            itm_arming_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401f6837d27688212],

  
#Seneschals
#SW - renamed Seneschal to Administrator ?
#SW - town_1 = Mandalore, give mandalorian armor/tunic
["town_1_seneschal", "Planet Administrator", "Town 1 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_mandalorian_deadeye_armor,itm_mandalorian_deadeye_boots,itm_grey_gloves], def_attrib|level(2),wp(20),knows_common, mandalorian_face1, mandalorian_face2],
["town_2_seneschal", "Planet Administrator", "Town 2 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["town_3_seneschal", "Planet Administrator", "Town 3 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["town_4_seneschal", "Planet Administrator", "Town 4 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["town_5_seneschal", "Planet Administrator", "Town 5 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["town_6_seneschal", "Planet Administrator", "Town 6 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["town_7_seneschal", "Planet Administrator", "Town 7 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
#SW- town_8 = geonosian
["town_8_seneschal", "Planet Administrator", "Town 8 Administrator", tf_hero|tf_geonosian|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_geonosian_armor],   def_attrib|level(2),wp(20),knows_common, geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor
["town_9_seneschal", "Planet Administrator", "Town 9 Administrator", tf_hero|tf_moncal|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_officer_uniform_white,itm_moncal_armor,itm_moncal_armor_2,itm_black_boots], def_attrib|level(2),wp(20),knows_common, moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["town_10_seneschal", "Planet Administrator", "Town 10 Administrator", tf_hero|tf_randomize_face|tf_wookiee|tf_is_merchant, 0,reserved,  fac_neutral,[],     def_attrib|level(2),wp(20),knows_common, wookiee_face1, wookiee_face2],
["town_11_seneschal", "Planet Administrator", "Town 11 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["town_12_seneschal", "Planet Administrator", "Town 12 Administrator", tf_hero|tf_randomize_face|tf_gamorrean|tf_is_merchant, 0,reserved,  fac_neutral,[], def_attrib|level(2),wp(20),knows_common, gamorrean_face1],
["town_13_seneschal", "Planet Administrator", "Town 13 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["town_14_seneschal", "Planet Administrator", "Town 14 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["town_15_seneschal", "Planet Administrator", "Town 14 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["town_16_seneschal", "Planet Administrator", "Town 14 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
#SW - town 17 = Ryloth, give twilek armor
["town_17_seneschal", "Planet Administrator", "Town 14 Administrator", tf_hero|tf_twilek|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_red_gambeson,itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, twilek_face1, twilek_face2],
#give hutt armor
["town_18_seneschal", "Planet Administrator", "Town 14 Administrator", tf_hero|tf_hutt|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],     def_attrib|level(2),wp(20),knows_common, hutt_face1, hutt_face2],
#SW - town 19, give bothan armor
["town_19_seneschal", "Planet Administrator", "Town 19 Administrator", tf_hero|tf_bothan|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, bothan_face1, bothan_face2],
["town_20_seneschal", "Planet Administrator", "Town 20 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["town_21_seneschal", "Planet Administrator", "Town 21 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],     def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],

["castle_1_seneschal", "Planet Administrator", "Castle 1 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],    def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_2_seneschal", "Planet Administrator", "Castle 2 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_3_seneschal", "Planet Administrator", "Castle 3 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_4_seneschal", "Planet Administrator", "Castle 4 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_5_seneschal", "Planet Administrator", "Castle 5 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],    def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_6_seneschal", "Planet Administrator", "Castle 6 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_7_seneschal", "Planet Administrator", "Castle 7 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_8_seneschal", "Planet Administrator", "Castle 8 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],    def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_9_seneschal", "Planet Administrator", "Castle 9 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_10_seneschal", "Planet Administrator", "Castle 10 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_11_seneschal", "Planet Administrator", "Castle 11 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_12_seneschal", "Planet Administrator", "Castle 2 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_13_seneschal", "Planet Administrator", "Castle 3 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_14_seneschal", "Planet Administrator", "Castle 4 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_15_seneschal", "Planet Administrator", "Castle 5 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots],    def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_16_seneschal", "Planet Administrator", "Castle 6 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_17_seneschal", "Planet Administrator", "Castle 7 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_18_seneschal", "Planet Administrator", "Castle 8 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots],    def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_19_seneschal", "Planet Administrator", "Castle 9 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_20_seneschal", "Planet Administrator", "Castle 20 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_21_seneschal", "Planet Administrator", "Castle 11 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_22_seneschal", "Planet Administrator", "Castle 2 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_23_seneschal", "Planet Administrator", "Castle 3 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_24_seneschal", "Planet Administrator", "Castle 4 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_25_seneschal", "Planet Administrator", "Castle 5 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],    def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_26_seneschal", "Planet Administrator", "Castle 6 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_27_seneschal", "Planet Administrator", "Castle 7 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_28_seneschal", "Planet Administrator", "Castle 8 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],    def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_29_seneschal", "Planet Administrator", "Castle 9 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_30_seneschal", "Planet Administrator", "Castle 20 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_31_seneschal", "Planet Administrator", "Castle 11 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_32_seneschal", "Planet Administrator", "Castle 2 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_33_seneschal", "Planet Administrator", "Castle 3 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_34_seneschal", "Planet Administrator", "Castle 4 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_35_seneschal", "Planet Administrator", "Castle 5 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],    def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_36_seneschal", "Planet Administrator", "Castle 6 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_37_seneschal", "Planet Administrator", "Castle 7 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_38_seneschal", "Planet Administrator", "Castle 8 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],    def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_39_seneschal", "Planet Administrator", "Castle 9 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],
["castle_40_seneschal", "Planet Administrator", "Castle 20 Administrator", tf_hero|tf_randomize_face|tf_is_merchant, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common, sw_man_face_1, sw_man_face_2],

#Arena Masters
#SW - town_1 = Mandalore, give mandalorian armor/tunic
["town_1_arena_master", "Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[itm_mandalorian_crusader_armor,itm_mandalorian_crusader_boots,itm_grey_gloves],    def_attrib|level(2),wp(20),knows_common,mandalorian_face1, mandalorian_face2],
["town_2_arena_master", "Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a],   def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["town_3_arena_master", "Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["town_4_arena_master", "Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["town_5_arena_master", "Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a],   def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["town_6_arena_master", "Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a], def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["town_7_arena_master", "Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a],   def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
#SW- town_8 = geonosian
["town_8_arena_master", "Arena Master","Tournament Master",tf_hero|tf_geonosian|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_geonosian_armor,itm_geonosian_sonic_rifle,itm_sonic_beam_rifle],    def_attrib|level(2),wp(20),knows_common,geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor
["town_9_arena_master", "Arena Master","Tournament Master",tf_hero|tf_moncal|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_officer_uniform_white,itm_moncal_armor,itm_moncal_armor_2,itm_black_boots], def_attrib|level(2),wp(20),knows_common,moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["town_10_arena_master","Arena Master","Tournament Master",tf_hero|tf_wookiee|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_wookiee_armor2],   def_attrib|level(2),wp(20),knows_common,wookiee_face1, wookiee_face2],
["town_11_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["town_12_arena_master","Arena Master","Tournament Master",tf_hero|tf_gamorrean|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[],    def_attrib|level(2),wp(20),knows_common, gamorrean_face1, gamorrean_face2],
["town_13_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a],   def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["town_14_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["town_15_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["town_16_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
#SW - town 17 = Ryloth, give twilek armor
["town_17_arena_master","Arena Master","Tournament Master",tf_hero|tf_twilek|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,twilek_face1, twilek_face2],
["town_18_arena_master","Arena Master","Tournament Master",tf_hero|tf_hutt|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],    def_attrib|level(2),wp(20),knows_common,hutt_face1, hutt_face2],
#SW - town 19, bothan
["town_19_arena_master","Arena Master","Tournament Master",tf_hero|tf_bothan|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a],    def_attrib|level(2),wp(20),knows_common, bothan_face1, bothan_face2],
["town_20_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],
["town_21_arena_master","Arena Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_vest_closed_a,itm_black_boots,itm_dl44a],    def_attrib|level(2),wp(20),knows_common,sw_man_face_1, sw_man_face_2],

# Underground 

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_leather_boots       ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,    itm_turret_hat_ruby     ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_apron,      itm_hide_boots          ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[itm_red_gambeson,       itm_blue_hose           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_woolen_dress,       itm_woolen_hood         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
##  
##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_jacket,     itm_leather_boots       ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_blue_dress,        itm_wimple_with_veil    ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[itm_blue_gambeson,     itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_woolen_dress,      itm_turret_hat_ruby     ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
  #arena_masters_end = zendar_armorer

#SW - town_1 = Mandalore, give mandalorian armor/tunic  
["town_1_armorer","Armorer",  "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_mandalorian_sniper_armor,itm_mandalorian_sniper_boots,itm_grey_gloves,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, mandalorian_face1, mandalorian_face2],
["town_2_armorer","Armorer",  "Armorer",  tf_hero|tf_randomize_face|		  tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_green,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_3_armorer","Armorer",  "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_white,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_4_armorer","Armorer",  "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_blue,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_5_armorer","Armorer",  "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_red,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_6_armorer","Armorer",  "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_green,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_7_armorer","Armorer",  "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_white,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW- town_8 = geonosian
["town_8_armorer","Armorer",  "Armorer",  tf_hero|tf_geonosian|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor
["town_9_armorer","Armorer",  "Armorer",  tf_hero|tf_moncal|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_officer_uniform_white,itm_moncal_armor,itm_moncal_armor_2,itm_black_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["town_10_armorer","Armorer", "Armorer",  tf_hero|tf_wookiee|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_wookiee_armor1,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, wookiee_face1, wookiee_face2],
["town_11_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_blue,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["town_12_armorer","Armorer", "Armorer",  tf_hero|tf_gamorrean|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, gamorrean_face1, gamorrean_face2],
["town_13_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_red,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_14_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_yellow,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_15_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_green,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_16_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_white,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW - town 17 = Ryloth, give twilek armor
["town_17_armorer","Armorer", "Armorer",  tf_hero|tf_twilek|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_blue,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, twilek_face1, twilek_face2],
#SW - town 18 = Nal Hutta, give jabba armor
["town_18_armorer","Armorer", "Armorer",  tf_hero|tf_hutt|tf_trandoshan|tf_randomize_face|	      tf_is_merchant, 0, 0, fac_commoners,[itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],def_attrib|level(12),wp(80),knows_inventory_management_10, hutt_face1, hutt_face2],
#SW - town 19, bothan
["town_19_armorer","Armorer", "Armorer",  tf_hero|tf_bothan|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_blue,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, bothan_face1, bothan_face2],
["town_20_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_red,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_21_armorer","Armorer", "Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_yellow,itm_leather_boots,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],

# Weapon merchants
#SW - town_1 = Mandalore, give mandalorian armor/tunic (also switched from female to male)
["town_1_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_mandalorian_deadeye_armor,itm_mandalorian_deadeye_boots,itm_grey_gloves,itm_vibro_blade1,itm_mandalorian_heavy_blaster,itm_laser_bolts_yellow_rifle],def_attrib|level(12),wp(80),knows_inventory_management_10, mandalorian_face1, mandalorian_face2],
["town_2_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_green,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_3_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_white,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_4_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_blue,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_5_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_red,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_6_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_yellow,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_7_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_green,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW- town_8 = geonosian
["town_8_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_geonosian|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_geonosian_armor,itm_geonosian_sonic_rifle,itm_sonic_beam_rifle],def_attrib|level(12),wp(80),knows_inventory_management_10, geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor
["town_9_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_moncal|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_officer_uniform_white,itm_moncal_armor,itm_moncal_armor_2,itm_black_boots,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["town_10_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_wookiee|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_wookiee_armor2,itm_wookiee_bowcaster,itm_laser_bolts_yellow_rifle,itm_vibro_blade1],def_attrib|level(12),wp(80),knows_inventory_management_10, wookiee_face1, wookiee_face2],
["town_11_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_white,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["town_12_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_gamorrean|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_vibro_axe_medium_1h],def_attrib|level(12),wp(80),knows_inventory_management_10, gamorrean_face1, gamorrean_face2],
["town_13_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_blue,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_14_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_red,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_15_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_yellow,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_16_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_green,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW - town 17 = Ryloth, give twilek armor
["town_17_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_twilek|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_white,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, twilek_face1, twilek_face2],
#SW - town 18 = Nal Hutta, give jabba armor
["town_18_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_hutt|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],def_attrib|level(12),wp(80),knows_inventory_management_10, hutt_face1, hutt_face2],
#town 19, bothan
["town_19_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_bothan|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_blue,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, bothan_face1, bothan_face2],
["town_20_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_red,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_21_weaponsmith","Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_tunic_yellow,itm_leather_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_ddc_defender],def_attrib|level(12),wp(80),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],

#Tavern keepers
#SW - updated Tavern_Keeper to Bartender
#SW - town_1 = Mandalore, give mandalorian armor/tunic
["town_1_tavernkeeper", "Bartender","Bartender",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_mandalorian_tunic,itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mandalorian_face1, mandalorian_face2],
["town_2_tavernkeeper", "Bartender","Bartender",tf_hero|tf_randomize_face|tf_female,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_female_dress_a, itm_leather_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["town_3_tavernkeeper", "Bartender","Bartender",tf_hero|tf_randomize_face|tf_female, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_female_dress_b, itm_leather_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["town_4_tavernkeeper", "Bartender","Bartender",tf_hero|tf_randomize_face|tf_female,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_female_dress_a, itm_leather_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["town_5_tavernkeeper", "Bartender","Bartender",tf_hero|tf_randomize_face|tf_female,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_female_dress_b, itm_leather_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["town_6_tavernkeeper", "Bartender","Bartender",tf_hero|tf_randomize_face|tf_female, scn_town_6_tavern|entry(9),0,   fac_commoners,[itm_female_dress_a, itm_leather_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["town_7_tavernkeeper", "Bartender","Bartender",tf_hero|tf_randomize_face|tf_female, scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_female_dress_b, itm_leather_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
#SW- town_8 = geonosian
["town_8_tavernkeeper", "Bartender","Bartender",tf_hero|tf_geonosian|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[],def_attrib|level(2),wp(20),knows_common, geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor (removed tf_female)
["town_9_tavernkeeper", "Bartender","Bartender",tf_hero|tf_moncal|tf_randomize_face, scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_officer_uniform_white,itm_moncal_armor,itm_moncal_armor_2,itm_black_boots],def_attrib|level(2),wp(20),knows_common, moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["town_10_tavernkeeper","Bartender","Bartender",tf_hero|tf_wookiee|tf_randomize_face, scn_town_10_tavern|entry(9),0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common, wookiee_face1, wookiee_face2],
["town_11_tavernkeeper","Bartender","Bartender",tf_hero|tf_randomize_face|tf_female, scn_town_11_tavern|entry(9),0,  fac_commoners,[itm_female_dress_a, itm_leather_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["town_12_tavernkeeper","Bartender","Bartender",tf_hero|tf_gamorrean|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[],def_attrib|level(2),wp(20),knows_common, gamorrean_face1, gamorrean_face2],
["town_13_tavernkeeper","Bartender","Bartender",tf_hero|tf_randomize_face|tf_female, scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_female_dress_b, itm_leather_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["town_14_tavernkeeper","Bartender","Bartender",tf_hero|tf_randomize_face|tf_female,           scn_town_14_tavern|entry(9),0,  fac_commoners,[itm_female_dress_a, itm_leather_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["town_15_tavernkeeper","Bartender","Bartender",tf_hero|tf_randomize_face|tf_female, scn_town_15_tavern|entry(9),0,  fac_commoners,[itm_female_dress_b, itm_leather_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["town_16_tavernkeeper","Bartender","Bartender",tf_hero|tf_randomize_face|tf_female,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_female_dress_a, itm_leather_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
#SW - town 17 = Ryloth, give twilek armor
["town_17_tavernkeeper","Bartender","Bartender",tf_hero|tf_randomize_face|tf_twilek_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,itm_hide_boots],def_attrib|level(2),wp(20),knows_common, twilek_female_face1, twilek_female_face2],
#SW - town 18 - give jaba armor
["town_18_tavernkeeper","Bartender","Bartender",tf_hero|tf_hutt|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],def_attrib|level(2),wp(20),knows_common, hutt_face1, hutt_face2],
#SW - town 19, bothan
["town_19_tavernkeeper","Bartender","Bartender",tf_hero|tf_bothan|tf_randomize_face,           scn_town_19_tavern|entry(9),0,  fac_commoners,[itm_tunic_green, itm_leather_boots],def_attrib|level(2),wp(20),knows_common, bothan_face1, bothan_face2],
["town_20_tavernkeeper","Bartender","Bartender",tf_hero|tf_randomize_face|tf_female,           scn_town_20_tavern|entry(9),0,  fac_commoners,[itm_female_dress_b, itm_leather_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],
["town_21_tavernkeeper","Bartender","Bartender",tf_hero|tf_randomize_face|tf_female,           scn_town_21_tavern|entry(9),0,  fac_commoners,[itm_female_dress_a, itm_leather_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_common, sw_woman_face_1, sw_woman_face_2],

#Goods Merchants
#SW - town_1 = Mandalore, give mandalorian armor/tunic
["town_1_merchant", "Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_mandalorian_tunic,itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, mandalorian_face1, mandalorian_face2],
["town_2_merchant", "Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_female_jacket_a, itm_black_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["town_3_merchant", "Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_female_jacket_b, itm_black_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["town_4_merchant", "Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_female_jacket_c, itm_black_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["town_5_merchant", "Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_female_jacket_a, itm_black_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["town_6_merchant", "Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_female_jacket_b, itm_black_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["town_7_merchant", "Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_female_jacket_c, itm_black_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
#SW- town_8 = geonosian
["town_8_merchant", "Merchant","Merchant",          tf_hero|tf_geonosian|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_geonosian_armor],def_attrib|level(2),wp(20),knows_inventory_management_10, geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor
["town_9_merchant", "Merchant","Merchant",          tf_hero|tf_moncal|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_officer_uniform_white,itm_moncal_armor,itm_moncal_armor_2,itm_black_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["town_10_merchant","Merchant","Merchant",          tf_hero|tf_randomize_face|tf_wookiee|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_wookiee_armor1],def_attrib|level(2),wp(20),knows_inventory_management_10, wookiee_face1, wookiee_face2],
["town_11_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_female_jacket_a, itm_black_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["town_12_merchant","Merchant","Merchant",tf_gamorrean|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [],def_attrib|level(2),wp(20),knows_inventory_management_10, gamorrean_face1, gamorrean_face2],
["town_13_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_female_jacket_b, itm_black_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["town_14_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_female_jacket_c, itm_black_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["town_15_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_female_jacket_a, itm_black_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["town_16_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_female_jacket_b, itm_black_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
#SW - town 17 = Ryloth, give twilek armor
["town_17_merchant","Merchant","Merchant",tf_twilek_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_dress,itm_leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, twilek_female_face1, twilek_female_face2],
#town 18, hutt
["town_18_merchant","Merchant","Merchant",          tf_hero|tf_hutt|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],def_attrib|level(2),wp(20),knows_inventory_management_10, hutt_face1, hutt_face2],
#SW - town 19, bothan
["town_19_merchant","Merchant","Merchant",tf_bothan|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_tunic_yellow, itm_leather_boots ],def_attrib|level(2),wp(20),knows_inventory_management_10, bothan_face1, bothan_face2],
["town_20_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_female_jacket_c, itm_black_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],
["town_21_merchant","Merchant","Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_female_jacket_a, itm_black_boots, itm_vibro_blade1, itm_q2, itm_laser_bolts_yellow_pistol],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_woman_face_1, sw_woman_face_2],

["salt_mine_merchant","Barezan","Barezan",                tf_hero|tf_randomize_face|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_leather_apron, itm_leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],

# Horse Merchants
#SW - renamed to Transportation Merchant ?
#SW - town_1 = Mandalore, give mandalorian armor/tunic (also removed female flag)
["town_1_horse_merchant","Transportation Merchant","Town 1 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,    0, 0, fac_commoners,[itm_mandalorian_tunic,itm_hide_boots],   def_attrib|level(2),wp(20),knows_inventory_management_10, mandalorian_face1, mandalorian_face2],
["town_2_horse_merchant","Transportation Merchant","Town 2 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_tunic_green, itm_leather_boots, itm_vibro_blade1],                      def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_3_horse_merchant","Transportation Merchant","Town 3 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_tunic_white, itm_leather_boots, itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_4_horse_merchant","Transportation Merchant","Town 4 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_tunic_blue, itm_leather_boots, itm_vibro_blade1],                       def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_5_horse_merchant","Transportation Merchant","Town 5 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,    0, 0, fac_commoners,[itm_tunic_red, itm_leather_boots, itm_vibro_blade1],   def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_6_horse_merchant","Transportation Merchant","Town 6 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_tunic_yellow, itm_leather_boots, itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_7_horse_merchant","Transportation Merchant","Town 7 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_tunic_green, itm_leather_boots, itm_vibro_blade1],                     def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW- town_8 = geonosian
["town_8_horse_merchant","Transportation Merchant","Town 8 Transportation Merchant",tf_hero|tf_geonosian|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_geonosian_armor,itm_geonosian_static_pike],                        def_attrib|level(5),wp(20),knows_inventory_management_10, geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor
["town_9_horse_merchant","Transportation Merchant","Town 9 Transportation Merchant",tf_hero|tf_moncal|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_officer_uniform_white,itm_moncal_armor,itm_moncal_armor_2,itm_black_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["town_10_horse_merchant","Transportation Merchant","Town 10 Transportation Merchant",tf_hero|tf_wookiee|tf_randomize_face|tf_is_merchant,  0, 0, fac_commoners,[itm_wookiee_armor2],     def_attrib|level(5),wp(20),knows_inventory_management_10, wookiee_face1, wookiee_face2],
["town_11_horse_merchant","Transportation Merchant","Town 11 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_tunic_white, itm_leather_boots, itm_vibro_blade1],                     def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["town_12_horse_merchant","Transportation Merchant","Town 12 Transportation Merchant",tf_hero|tf_gamorrean|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[],                        def_attrib|level(5),wp(20),knows_inventory_management_10, gamorrean_face1, gamorrean_face2],
["town_13_horse_merchant","Transportation Merchant","Town 13 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_tunic_blue, itm_leather_boots, itm_vibro_blade1],                       def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_14_horse_merchant","Transportation Merchant","Town 14 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,  0, 0, fac_commoners,[itm_tunic_red, itm_leather_boots, itm_vibro_blade1],     def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_15_horse_merchant","Transportation Merchant","Town 15 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_tunic_yellow, itm_leather_boots, itm_vibro_blade1],                     def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_16_horse_merchant","Transportation Merchant","Town 16 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_tunic_green, itm_leather_boots, itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
#SW - town 17 = Ryloth, give twilek armor
["town_17_horse_merchant","Transportation Merchant","Town 17 Transportation Merchant",tf_hero|tf_twilek|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, twilek_face1, twilek_face2],
#SW - town 18, give hutt armor
["town_18_horse_merchant","Transportation Merchant","Town 18 Transportation Merchant",tf_hero|tf_hutt|tf_randomize_face|tf_is_merchant,  0, 0, fac_commoners,[itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],     def_attrib|level(5),wp(20),knows_inventory_management_10, hutt_face1, hutt_face2],
#SW - town 19 - bothan
["town_19_horse_merchant","Transportation Merchant","Town 19 Transportation Merchant",tf_hero|tf_bothan|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_tunic_green,      itm_leather_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, bothan_face1, bothan_face2],
["town_20_horse_merchant","Transportation Merchant","Town 20 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_tunic_white, itm_leather_boots, itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["town_21_horse_merchant","Transportation Merchant","Town 21 Transportation Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_tunic_blue, itm_leather_boots, itm_vibro_blade1],                        def_attrib|level(5),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],

#Town Mayors    #itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit
#SW - town_1 = Mandalore, give mandalorian armor/tunic
["town_1_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_mandalorian_crusader_armor,itm_mandalorian_crusader_boots,itm_grey_gloves], def_attrib|level(2),wp(20),knows_common, mandalorian_face1, mandalorian_face2],
["town_2_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["town_3_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["town_4_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots],     def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["town_5_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["town_6_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["town_7_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
#SW- town_8 = geonosian
["town_8_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_geonosian|tf_randomize_face, 0,reserved,  fac_neutral,[itm_geonosian_armor,itm_geonosian_sonic_pistol,itm_sonic_beam_pistol],   def_attrib|level(2),wp(20),knows_common,  geonosian_face1, geonosian_face2],
#SW - town_9 = Mon Cal, give mon calamari armor
["town_9_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_moncal|tf_randomize_face, 0,reserved,  fac_neutral,[itm_officer_uniform_white,itm_moncal_armor,itm_moncal_armor_2,itm_black_boots], def_attrib|level(2),wp(20),knows_common,  moncal_face1, moncal_face2],
#SW - town_10 = Kashyyyk, give wookiee armor
["town_10_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_wookiee|tf_randomize_face, 0,reserved,  fac_neutral,[itm_wookiee_armor1],     def_attrib|level(2),wp(20),knows_common,  wookiee_face1, wookiee_face2],
["town_11_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
#SW - town_12 = Gamorr, give gamorrean armor
["town_12_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_gamorrean|tf_randomize_face, 0,reserved,  fac_neutral,[], def_attrib|level(2),wp(20),knows_common,  gamorrean_face1, gamorrean_face2],
["town_13_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["town_14_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots],     def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["town_15_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_red_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["town_16_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
#SW - town 17 = Ryloth, give twilek armor
["town_17_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_twilek|tf_randomize_face, 0,reserved,  fac_neutral,[itm_gambeson,itm_leather_boots],   def_attrib|level(2),wp(20),knows_common,  twilek_face1, twilek_face2],
#SW - town_18 = Nal Hutta, give jabba armor
["town_18_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_hutt|tf_randomize_face, 0,reserved,  fac_neutral,[itm_transparent_head,itm_transparent_hands,itm_jabba_armor,itm_transparent_feet,itm_jabba_attack],     def_attrib|level(2),wp(20),knows_common,  hutt_face1, hutt_face2],
#SW - town 19, bothan
["town_19_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_bothan|tf_randomize_face, 0,reserved,  fac_neutral,[itm_blue_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  bothan_face1, bothan_face2],
["town_20_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],
["town_21_mayor", "Planet_Administrator", "Planet_Administrator", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_lobot_headgear,itm_blue_gambeson,itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  sw_man_face_1, sw_man_face_2],


#Village stores
["village_1_elder", "Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_2_elder", "Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_3_elder", "Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_4_elder", "Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_5_elder", "Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_6_elder", "Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_7_elder", "Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_8_elder", "Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_9_elder", "Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_10_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_11_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_12_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_13_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_14_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_15_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_16_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_17_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_18_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_19_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_20_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_21_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_22_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_23_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_24_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_closed_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_25_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_26_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_27_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_28_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_29_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_30_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_31_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_32_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_33_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_34_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_35_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_36_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_37_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_38_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_39_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_40_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_41_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_42_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_43_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_44_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_45_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_46_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_47_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_48_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_jacket_open_c,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_49_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_50_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_51_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_52_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_53_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_54_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_55_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_56_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_57_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_58_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_59_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_60_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_closed_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_q2,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_61_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_62_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_63_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_64_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_65_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_66_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_67_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_68_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_69_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_70_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_71_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_72_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_a,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_westar,itm_eyepiece_leadership],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_73_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_74_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_75_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_76_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_77_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_78_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_79_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_80_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_81_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_82_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_83_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_84_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_85_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_86_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_87_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_88_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_89_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
["village_90_elder","Planet_Administrator", "village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_vest_open_b,itm_leather_boots,itm_laser_bolts_orange_pistol,itm_dl44a,itm_eyepiece_tactics],def_attrib|level(2),wp(20),knows_inventory_management_10, sw_man_face_1, sw_man_face_2],
# Place extra merchants before this point
["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

# Chests
["zendar_chest","Zendar Chest","Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
#SW - modified tutorial_chests
["tutorial_chest_1","Melee Weapons Chest","Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["tutorial_chest_2","Ranged Weapons Chest","Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
#SW - added Star Wars items to bonus chests
# bonus_chest_1 = town_13 (Rivacheg)
["bonus_chest_1","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_darth_vader_helmet,itm_darth_vader_armor,itm_darth_vader_lightsaber,itm_obi_wan_lightsaber,itm_luke_skywalker_lightsaber,itm_chewbacca_bowcaster,itm_han_solo_outfit,itm_han_solo_blaster,itm_princess_leia_outfit,itm_boba_fett_armor,itm_boba_fett_helmet,itm_boba_fett_boots,itm_boba_fett_blaster,itm_twilek_male_head_bib,itm_weequay_vibro_axe],def_attrib|level(18),wp(60),knows_common, 0],
# bonus_chest_2 = town_5 (Jelkala)
["bonus_chest_2","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_darth_vader_helmet,itm_darth_vader_armor,itm_darth_vader_lightsaber,itm_obi_wan_lightsaber,itm_luke_skywalker_lightsaber,itm_chewbacca_bowcaster,itm_han_solo_outfit,itm_han_solo_blaster,itm_princess_leia_outfit,itm_boba_fett_armor,itm_boba_fett_helmet,itm_boba_fett_boots,itm_boba_fett_blaster,itm_twilek_male_head_bib,itm_weequay_vibro_axe],def_attrib|level(18),wp(60),knows_common, 0],
# bonus_chest_3 = town_2 (Tihr)
["bonus_chest_3","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_darth_vader_helmet,itm_darth_vader_armor,itm_darth_vader_lightsaber,itm_obi_wan_lightsaber,itm_luke_skywalker_lightsaber,itm_chewbacca_bowcaster,itm_han_solo_outfit,itm_han_solo_blaster,itm_princess_leia_outfit,itm_boba_fett_armor,itm_boba_fett_helmet,itm_boba_fett_boots,itm_boba_fett_blaster,itm_twilek_male_head_bib,itm_weequay_vibro_axe],def_attrib|level(18),wp(60),knows_common, 0],

#town specific bonus chests
["bonus_chest_town_1","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_boba_fett_armor,itm_boba_fett_helmet,itm_boba_fett_boots,itm_boba_fett_blaster],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_2","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_3","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_4","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_han_solo_outfit,itm_han_solo_blaster],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_5","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_6","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_7","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_8","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_9","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_10","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_chewbacca_bowcaster,itm_chewbacca_ryyk_blade],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_11","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_12","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_13","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_princess_leia_outfit,itm_princess_leia_blaster,itm_luke_skywalker_outfit,itm_luke_skywalker_lightsaber,itm_anakin_skywalker_lightsaber],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_14","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_rancor_keeper_armor,itm_dengar_armor,itm_dengar_helmet,itm_dengar_boots,itm_dengar_gloves,itm_weequay_vibro_axe,itm_obi_wan_lightsaber],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_15","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_16","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_darth_vader_lightsaber,itm_darth_vader_helmet,itm_darth_vader_armor],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_17","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_18","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_19","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_20","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_town_21","Bonus Chest","Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_protein_pack,itm_carbohydrate_pack],def_attrib|level(18),wp(60),knows_common, 0],
	
# These are used as arrays in the scripts.
["temp_array_a","temp_array_a","temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["temp_array_b","temp_array_b","temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["temp_array_c","temp_array_c","temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

["stack_selection_amounts","stack_selection_amounts","stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["stack_selection_ids","stack_selection_ids","stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["notification_menu_types","notification_menu_types","notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["notification_menu_var1","notification_menu_var1","notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["notification_menu_var2","notification_menu_var2","notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["banner_background_color_array","banner_background_color_array","banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

#SW BSG integration
["viper_a","viper_a","viper_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_b","viper_c","viper_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_c","viper_b","viper_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_d","viper_d","viper_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_e","viper_e","viper_e",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_f","viper_f","viper_f",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_g","viper_g","viper_g",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_h","viper_h","viper_h",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["viper_end","viper_end","viper_end",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

["cylon_a","cylon_a","cylon_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_b","cylon_c","cylon_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_c","cylon_b","cylon_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_d","cylon_d","cylon_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_e","cylon_e","cylon_e",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_f","cylon_f","cylon_f",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_g","cylon_g","cylon_g",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_h","cylon_h","cylon_h",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["cylon_end","cylon_end","cylon_end",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],  
  
##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
##   [itm_laser_bolts_green,itm_nomad_sabre,itm_scimitar,itm_winged_mace,itm_lance,itm_ee3,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_nomad_shield,itm_steppe_horse,itm_warhorse],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],


# Add Extra Quest NPCs below this point  

["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners, [itm_q2,itm_ddc_defender,itm_westar,itm_laser_bolts_orange_pistol,itm_laser_bolts_yellow_pistol,itm_cleaver,itm_durasteel_staff,itm_quarter_staff,itm_vibro_blade2,itm_vibro_blade3,itm_club,itm_leather_cap,itm_leather_apron,itm_linen_tunic,itm_coarse_tunic,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_a,itm_leather_gloves,itm_leather_boots,itm_nomad_boots,itm_wrapping_boots], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["trainee_peasant","Peasant","Peasants",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners, [itm_q2,itm_ddc_defender,itm_westar,itm_laser_bolts_orange_pistol,itm_laser_bolts_yellow_pistol,itm_cleaver,itm_durasteel_staff,itm_quarter_staff,itm_vibro_blade2,itm_vibro_blade3,itm_club,itm_leather_cap,itm_leather_apron,itm_linen_tunic,itm_coarse_tunic,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_a,itm_leather_gloves,itm_leather_boots,itm_nomad_boots,itm_wrapping_boots], def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners, [itm_ubese_armor,itm_scavenger_armor,itm_crime_lord_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_vibro_sword3_gold,itm_laser_bolts_orange_pistol,itm_westar,itm_q2,itm_dl44a,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet,itm_jacket_closed_a,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,mandalorian_face1, mandalorian_face2],
["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral, [itm_ubese_armor,itm_scavenger_armor,itm_crime_lord_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_vibro_sword3_gold,itm_laser_bolts_orange_pistol,itm_westar,itm_q2,itm_dl44a,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet,itm_jacket_closed_a,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|agi_11|level(20),wp(130),knows_common,mandalorian_face1, mandalorian_face2],
["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral, [itm_ubese_armor,itm_scavenger_armor,itm_crime_lord_armor,itm_guard_armor,itm_guard_armor_red,itm_tunic_blue,itm_tunic_red,itm_tunic_yellow,itm_vibro_sword3_gold,itm_laser_bolts_orange_pistol,itm_westar,itm_q2,itm_dl44a,itm_transparent_helmet,itm_transparent_helmet,itm_transparent_helmet,itm_jacket_closed_a,itm_jacket_closed_c,itm_jacket_open_a,itm_jacket_open_c,itm_vest_closed_a,itm_vest_open_a,itm_vest_open_b,itm_black_boots], def_attrib|agi_11|level(10),wp(130),knows_common,mandalorian_face1, mandalorian_face2],
["bounty_target_1a","CIS Officer","CIS Officers",tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_black_boots,itm_black_gloves,itm_officer_uniform_white,itm_vibro_sword3_gold,itm_energy_shield_yellow_small,itm_laser_bolts_yellow_rifle,itm_a295], def_attrib_3|level(26),wp(180),starwars_skills_3, sw_imperial_face_1, sw_imperial_face_2],
["bounty_target_1b","CIS Officer","CIS Officers",tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_black_boots,itm_black_gloves,itm_outfit_grey,itm_vibro_sword3_gold,itm_energy_shield_yellow_small,itm_laser_bolts_yellow_rifle,itm_a295], def_attrib_3|level(26),wp(180),starwars_skills_3, sw_imperial_face_1, sw_imperial_face_2],
["bounty_target_2a","Farmer","Farmers",tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_vibro_blade1,itm_q2,itm_ddc_defender,itm_laser_bolts_yellow_pistol,itm_coarse_tunic,itm_jacket_open_c,itm_vest_open_a,itm_leather_gloves,itm_leather_boots], def_attrib_2|level(20),wp(150),starwars_skills_2 ,sw_man_face_1, sw_man_face_2],
["bounty_target_2b","Farmer","Farmers",tf_twilek|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_vibro_blade1,itm_q2,itm_ddc_defender,itm_laser_bolts_yellow_pistol,itm_linen_tunic,itm_vest_closed_a,itm_leather_gloves,itm_leather_boots], def_attrib_2|level(20),wp(150),starwars_skills_2 ,twilek_face1, twilek_face2],
["bounty_target_3a","Target","Targets",tf_bothan|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_vest_closed_a,itm_black_boots,itm_vibro_sword3_red,itm_laser_bolts_green_rifle,itm_bothan_bola_carabine,itm_energy_shield_green_medium], def_attrib_4|level(30),wp(220),starwars_skills_4, bothan_face1, bothan_face2],
["bounty_target_3b","Target","Targets",tf_gamorrean|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_durasteel_shield_small,itm_gamorrean_armor,itm_vibro_axe_medium_1h,itm_throwing_axes], def_attrib_4|level(30),wp(220),starwars_skills_4, gamorrean_face1, gamorrean_face2],
["bounty_target_3c","Target","Targets",tf_chiss|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_guard_armor,itm_guard_armor_red,itm_officer_uniform_white,itm_black_boots,itm_vibro_sword3_gold,itm_energy_shield_red_medium,itm_laser_bolts_red_rifle,itm_a295], def_attrib_4|level(30),wp(220),starwars_skills_4, chiss_face1, chiss_face2],
["bounty_target_3d","Target","Targets",tf_moncal|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_black_boots,itm_guard_armor,itm_moncal_armor,itm_moncal_armor_2,itm_a295,itm_laser_bolts_green_rifle,itm_vibro_sword3_gold,itm_energy_shield_green_medium], def_attrib_4|level(30),wp(220),starwars_skills_4, moncal_face1, moncal_face1],
["bounty_target_4a","Pirate","Pirates",tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_leather_boots,itm_laser_bolts_yellow_rifle,itm_a295,itm_vibro_sword3_gold,itm_crime_lord_armor,itm_guard_armor,itm_westar_shield,itm_energy_shield_yellow_small], def_attrib_3|level(26),wp(180),starwars_skills_3, mandalorian_face1, mandalorian_face2],
["bounty_target_4b","Pirate","Pirates",tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_transparent_helmet_armor,itm_leather_boots,itm_laser_bolts_yellow_rifle,itm_a295,itm_vibro_sword3_gold,itm_ubese_armor,itm_scavenger_armor,itm_westar_shield,itm_energy_shield_yellow_small], def_attrib_3|level(26),wp(180),starwars_skills_3, sw_rebel_face_1, sw_rebel_face_2],
["bounty_target_5a","Bountyhunter","Bountyhunters",tf_randomize_face|tf_guarantee_all_armor|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_mandalorian_deadeye_helmet,itm_mandalorian_deadeye_armor,itm_mandalorian_deadeye_boots,itm_grey_gloves,itm_vibro_sword3_gold,itm_laser_bolts_red_rifle,itm_mandalorian_heavy_blaster,itm_westar_shield], def_attrib_4|level(30),wp(220),starwars_skills_4, mandalorian_face1, mandalorian_face2],
["bounty_target_5b","Bountyhunter","Bountyhunters",tf_trandoshan|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_trandoshan_armor,itm_trandoshan_flight_suit,itm_trandoshan_blade,itm_laser_bolts_orange_rifle,itm_trandoshan_acp_array_gun,itm_energy_shield_yellow_medium,itm_westar_shield,itm_transparent_helmet_armor], def_attrib_4|level(30),wp(220),starwars_skills_4, trandoshan_face1, trandoshan_face2],
["bounty_target_5c","Bountyhunter","Bountyhunters",tf_rodian|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_jacket_closed_b,itm_black_boots,itm_black_gloves,itm_vibro_sword3_gold,itm_laser_bolts_orange_rifle,itm_a295,itm_transparent_helmet_armor,itm_energy_shield_green_medium,itm_westar_shield], def_attrib_4|level(30),wp(220),starwars_skills_4, rodian_face1, rodian_face2],
["bounty_target_6a","Smuggler","Smugglers",tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_vibro_blade1,itm_dl44a,itm_laser_bolts_green_pistol,itm_westar_shield,itm_energy_shield_yellow_small,itm_transparent_helmet_armor,itm_vest_closed_a,itm_vest_open_b,itm_han_solo_outfit,itm_black_boots], def_attrib_3|level(26),wp(180),starwars_skills_3, sw_imperial_face_1, sw_imperial_face_2],
["bounty_target_6b","Smuggler","Smugglers",tf_wookiee|tf_randomize_face|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_commoners, [itm_wookiee_armor1,itm_wookiee_armor2,itm_transparent_helmet_armor,itm_ryyk_blade,itm_ryyk_blade_chieftain,itm_wookiee_shield_small,itm_wookiee_bowcaster,itm_laser_bolts_green_rifle], def_attrib|str_24|agi_25|level(26),wp(180), def_attrib_3|level(26),wp(180),starwars_skills_3, wookiee_face1, wookiee_face2],
##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,sw_man_face_1, sw_man_face_2],
##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,sw_man_face_1, sw_man_face_2],
##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
##   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
##   def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],
##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
##   [itm_sword,itm_leather_jacket,itm_hide_boots, itm_saddle_horse, itm_leather_jacket, itm_leather_cap],
##   def_attrib|level(9),wp(100),knows_common,swadian_face1, swadian_face2],
##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
##   [itm_knife,itm_dagger,itm_dlt19,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
##   def_attrib|level(3),wp(45),knows_common,sw_woman_face_1,sw_woman_face_2],


#SW - modified quick_battle_6_player which is then used in the Quick Battle (this is also bounty_targets_end)
["quick_battle_player", "Player", "Player", tf_hero, 0, reserved,  fac_player_faction, [itm_transparent_helmet,itm_leather_boots,itm_quick_battle_armor, itm_leather_gloves, itm_lightsaber_yellow, itm_a280,  itm_stun_beam_rifle, itm_energy_shield_yellow_medium],    knight_attrib_5,wp(250),starwars_knight_skills_5, sw_player_face],
["quick_battle_player_mounted", "Player", "Player", tf_hero, 0, reserved,  fac_player_faction, [itm_transparent_helmet,itm_leather_boots,itm_quick_battle_armor, itm_leather_gloves, itm_lightsaber_yellow, itm_a280,  itm_stun_beam_rifle, itm_energy_shield_yellow_medium, itm_practice_speeder],knight_attrib_5,wp(250),starwars_knight_skills_5, sw_player_face],
["quick_battle_farmer","Farmer","Farmers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_baton,itm_baton,itm_pipe1,itm_pipe2,itm_melee_punch,itm_melee_punch,itm_vibro_blade1,itm_vibro_blade2,itm_q2,itm_q2,itm_dl44a,itm_ddc_defender,itm_westar,itm_laser_bolts_yellow_pistol,itm_leather_apron,itm_linen_tunic,itm_coarse_tunic,itm_jacket_open_c,itm_vest_closed_a,itm_vest_closed_b,itm_vest_closed_a,itm_leather_gloves,itm_leather_boots,itm_outfit_tan,itm_outfit_grey,itm_outfit_green],
   def_attrib|level(4),wp(60),knows_common,sw_man_face_1, sw_man_face_2],

# START OF CUSTOM BATTLE TROOPS  
#########################################
# Custom Battle Troops
#########################################

["custom_battle_fac_store","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["custom_battle_fac_1_troops","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["custom_battle_fac_2_troops","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["custom_battle_fac_3_troops","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["custom_battle_fac_4_troops","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["custom_battle_fac_5_troops","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["custom_battle_fac_6_troops","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
["custom_battle_spawn_store","Bleh","Bleh",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],   

# END OF CUSTOM BATTLE TROOPS

#Player history array
["log_array_entry_type",            "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_entry_time",            "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_actor",                 "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_center_object",         "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_center_object_lord",    "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_center_object_faction", "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_troop_object",          "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_troop_object_faction",  "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
["log_array_faction_object",        "Local Merchant","Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],

#Highlander begin--------------------------------------
	#particle arrays
  ["pjct_active",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_x",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_y",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_z",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_x_velocity",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_y_velocity",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_z_velocity",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_emit_time",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],

  ["pjct_source_agent",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_damage",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_bounce_effect",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_explosive",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_explosion_countdown",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_explosion_area",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_explosion_damage",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_explode_on_ground_hit",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_particle_system",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
  ["pjct_particle_system_magnitude",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],

  ["pjct_attach_scene_prop",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],

  ["pjct_check_collision",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
	#instance arrays
  ["instance_attached_to",            "_","_",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, sw_man_face_1, sw_man_face_2],
#Highlander end--------------------------------------
]


#Troop upgrade declarations

#SW - commented out old merc upgrade paths

#upgrade(troops,"farmer", "watchman")
#upgrade(troops,"townsman","watchman")
#upgrade2(troops,"watchman","caravan_guard","mercenary_crossbowman")
#upgrade2(troops,"caravan_guard","mercenary_swordsman","mercenary_horseman")
#upgrade(troops,"mercenary_swordsman","hired_blade")
#upgrade(troops,"mercenary_horseman","mercenary_cavalry")

#SW - added star wars upgrade paths

#human mercs
upgrade(troops,"farmer", "civilian")
upgrade(troops,"townsman","civilian")
upgrade2(troops,"civilian","militia","thug")
upgrade2(troops,"militia","security_guard","soldier")
upgrade(troops,"security_guard", "bodyguard")
upgrade2(troops,"soldier","commando","pilot")
upgrade2(troops,"thug","goon","biker")
upgrade(troops,"goon", "assassin")
upgrade(troops,"biker", "biker_scout")

#force_sensitive
upgrade2(troops,"force_sensitive_recruit","sith_hopeful","jedi_hopeful")
# imperial
#upgrade2(troops,"imperial_recruit","imperial_cadet","sith_hopeful")
#upgrade(troops,"imperial_recruit","imperial_cadet")
upgrade2(troops,"imperial_recruit","imperial_navy_trooper","imperial_army_trooper")
upgrade2(troops,"imperial_navy_trooper","imperial_pilot","imperial_gunner")
upgrade(troops,"imperial_pilot","imperial_pilot_veteran")
upgrade(troops,"imperial_gunner","imperial_gunner_veteran")
upgrade2(troops,"imperial_army_trooper","imperial_stormtrooper","imperial_scout_trooper")
upgrade2(troops,"imperial_scout_trooper","imperial_scout_trooper_veteran","imperial_scout_trooper_marksman")
upgrade(troops,"imperial_scout_trooper_marksman","imperial_scout_trooper_sniper")
upgrade(troops,"imperial_scout_trooper_veteran","imperial_scout_trooper_captain")
upgrade(troops,"imperial_stormtrooper","imperial_stormtrooper_veteran")
upgrade2(troops,"imperial_stormtrooper_veteran","imperial_stormtrooper_officer","imperial_royal_guard")
upgrade(troops,"sith_hopeful","sith_acolyte")
upgrade(troops,"sith_acolyte","sith_apprentice")
upgrade(troops,"sith_apprentice","sith_knight")
upgrade(troops,"sith_knight","sith_marauder")
upgrade(troops,"sith_marauder","sith_master")
upgrade(troops,"sith_master","sith_lord")

# rebel
#upgrade2(troops,"rebel_recruit","rebel_cadet","jedi_hopeful")
upgrade(troops,"rebel_recruit","rebel_cadet")
upgrade2(troops,"rebel_cadet","rebel_trooper","rebel_scout")
upgrade2(troops,"rebel_trooper","rebel_vanguard","rebel_pilot")
upgrade(troops,"rebel_pilot","rebel_pilot_veteran")
upgrade2(troops,"rebel_vanguard","rebel_heavy_trooper","rebel_honor_guard")
upgrade2(troops,"rebel_scout","rebel_commando","rebel_marksman")
upgrade(troops,"rebel_commando","rebel_commando_veteran")
upgrade(troops,"rebel_marksman","rebel_sniper")
upgrade(troops,"jedi_hopeful","jedi_initiate")
upgrade(troops,"jedi_initiate","jedi_padawan")
upgrade2(troops,"jedi_padawan","jedi_guardian","jedi_consular")
upgrade(troops,"jedi_guardian","jedi_warrior_master")
upgrade(troops,"jedi_consular","jedi_sage_master")
upgrade(troops,"jedi_warrior_master","jedi_councilor")
upgrade(troops,"jedi_sage_master","jedi_councilor")
upgrade(troops,"jedi_councilor","jedi_grand_master")

#hutt
upgrade(troops,"hutt_militia","hutt_mercenary")
upgrade2(troops,"hutt_mercenary","hutt_marksman","hutt_guard")
upgrade(troops,"hutt_marksman","hutt_bounty_hunter")
upgrade(troops,"hutt_bounty_hunter","hutt_commando")
upgrade2(troops,"hutt_guard","hutt_skiff_guard","hutt_palace_guard")
upgrade(troops,"hutt_skiff_guard","hutt_skiff_guard_captain")
upgrade(troops,"hutt_palace_guard","hutt_palace_guard_captain")

#wookiee mercs
upgrade(troops,"wookiee","wookiee_warrior")
upgrade2(troops,"wookiee_warrior","wookiee_marksman","wookiee_berserker")
upgrade(troops,"wookiee_marksman","wookiee_sharpshooter")
upgrade(troops,"wookiee_berserker","bacca_warrior")
#mandalorian mercs
upgrade(troops,"mandalorian","mandalorian_soldier")
upgrade2(troops,"mandalorian_soldier","mandalorian_commando","mandalorian_sniper")
upgrade(troops,"mandalorian_commando","mandalorian_crusader")
upgrade(troops,"mandalorian_sniper","mandalorian_deadeye")
#clone trooper
upgrade2(troops,"clone_trooper_1","clone_trooper_2","arc_trooper_2")
upgrade(troops,"clone_trooper_2","clone_trooper_3")
upgrade(troops,"clone_trooper_3","clone_trooper_4")
upgrade(troops,"clone_trooper_4","clone_trooper_5")
upgrade(troops,"arc_trooper_2","arc_trooper_3")
upgrade(troops,"arc_trooper_3","arc_trooper_4")
upgrade(troops,"arc_trooper_4","arc_trooper_5")
#twilek female
upgrade(troops,"twilek_female1","twilek_female2")
upgrade(troops,"twilek_female2","twilek_female3")
#sullustan male
upgrade(troops,"chiss_1","chiss_2")
upgrade(troops,"chiss_2","chiss_3")
upgrade(troops,"chiss_3","chiss_4")
#sullustan male
upgrade(troops,"sullustan_1","sullustan_2")
upgrade(troops,"sullustan_2","sullustan_3")
upgrade(troops,"sullustan_3","sullustan_4")
#geonosian male
upgrade(troops,"geonosian_1","geonosian_2")
upgrade(troops,"geonosian_2","geonosian_3")
upgrade(troops,"geonosian_3","geonosian_4")
#twilek male
upgrade(troops,"twilek","twilek_warrior")
upgrade(troops,"twilek_warrior","twilek_soldier")
upgrade(troops,"twilek_soldier","twilek_commando")
#rodian
upgrade(troops,"rodian","rodian_warrior")
upgrade(troops,"rodian_warrior","rodian_hunter")
upgrade(troops,"rodian_hunter","rodian_bounty_hunter")
#trandoshan
upgrade(troops,"trandoshan","trandoshan_warrior")
upgrade(troops,"trandoshan_warrior","trandoshan_hunter")
upgrade(troops,"trandoshan_hunter","trandoshan_bounty_hunter")
#mon cal
upgrade(troops,"moncal_1","moncal_2")
upgrade(troops,"moncal_2","moncal_3")
upgrade(troops,"moncal_3","moncal_4")
#bothan
upgrade2(troops,"bothan","bothan_agent","bothan_militia")
upgrade(troops,"bothan_militia","bothan_infantry")
upgrade(troops,"bothan_agent","bothan_spy")
upgrade(troops,"bothan_spy","bothan_infiltrator")
#gamorrean
upgrade(troops,"gamorrean","gamorrean_warrior")
upgrade(troops,"gamorrean_warrior","gamorrean_guard")
upgrade(troops,"gamorrean_guard","gamorrean_palace_guard")

#SW - looter doesn't need to upgrade to other bandits since they are jawa's
#upgrade2(troops,"looter","mountain_bandit", "forest_bandit")

#black sun
upgrade(troops,"mountain_bandit_1","mountain_bandit_2")
upgrade(troops,"mountain_bandit_2","mountain_bandit_3")
upgrade(troops,"mountain_bandit_3","mountain_bandit_4")
#jawa
upgrade(troops,"looter","looter_2")
upgrade(troops,"looter_2","looter_3")

#SW - tusken upgrade path
upgrade(troops,"tusken_1","tusken_2")

# SW - upgrade doesn't make sense, possible defect?
#upgrade2(troops,"bandit","brigand","mercenary_swordsman")
upgrade(troops,"bandit","brigand")

#droids
#b1series
upgrade(troops,"b1series","b1series_assassin")
upgrade(troops,"b1series_assassin","bxseries_commando")
#oom_series
upgrade2(troops,"oom_series_security","oom_series_marine","oom_series_pilot")
upgrade(troops,"oom_series_marine","oom_series_command")

#SW - manhunter switched to trandoshan slavers, currently with no upgrade path
#upgrade(troops,"manhunter","slave_driver")
#upgrade(troops,"slave_driver","slave_hunter")
#upgrade(troops,"slave_hunter","slave_crusher")
#upgrade(troops,"slave_crusher","slaver_chief")

#upgrade(troops,"forest_bandit","mercenary_crossbowman")

#upgrade(troops,"refugee","follower_woman")
#upgrade(troops,"peasant_woman","follower_woman")

#upgrade(troops,"follower_woman","hunter_woman")
#upgrade(troops,"hunter_woman","fighter_woman")
#upgrade(troops,"fighter_woman","sword_sister")