# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M 
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from header_common import *
from header_scene_props import *
from header_operations import *
from header_triggers import *
from header_sounds import *
from module_constants import *
import string

####################################################################################################################
#  Each scene prop record contains the following fields:
#  1) Scene prop id: used for referencing scene props in other files. The prefix spr_ is automatically added before each scene prop id.
#  2) Scene prop flags. See header_scene_props.py for a list of available flags
#  3) Mesh name: Name of the mesh.
#  4) Physics object name:
#  5) Triggers: Simple triggers that are associated with the scene prop
####################################################################################################################

scene_props = [
  ("invalid_object",0,"question_mark","0", []),
  #("inventory",sokf_type_container|sokf_place_at_origin,"package","bobaggage", []),
  ("inventory",sokf_type_container|sokf_place_at_origin,"player_chest_sw","bo_player_chest_sw", []),
  ("empty", 0, "0", "0", []),
  ("chest_a",sokf_type_container,"chest_gothic","bochest_gothic", []),
  ("container_small_chest",sokf_type_container,"package","bobaggage", []),
  ("container_chest_b",sokf_type_container,"chest_b","bo_chest_b", []),
  ("container_chest_c",sokf_type_container,"chest_c","bo_chest_c", []),
  #SW - new player_chest and locked_player_chest
  #("player_chest",sokf_type_container,"player_chest","bo_player_chest", []),
  ("player_chest",sokf_type_container,"player_chest_sw","bo_player_chest_sw", []),
  #("locked_player_chest",0,"player_chest","bo_player_chest", []),
  ("locked_player_chest",0,"player_chest_sw","bo_player_chest_sw", []),

  #SW - new scene props

  #vehicles and mounts
  ("sw_ATST",0,"ATST_scene_prop","bo_ATST_scene_prop", []),
  ("sw_ATAT",0,"ATAT","bo_ATAT", []),  
  ("sw_dewback",0,"dewback","bo_dewback", []),
  ("sw_kaadu_a",0,"kaadu_a","bo_kaadu_a", []),
  ("sw_kaadu_b",0,"kaadu_b","bo_kaadu_b", []),  
  
  #ships/map icons
  ("sw_a_wing",0,"a_wing","bo_a_wing", []),
  ("sw_rebel_transport",0,"rebel_transport_w_landing_gear","bo_rebel_transport_w_landing_gear", []),
  ("sw_civilian_shuttle",0,"shuttle_civilian","bo_shuttle_civilian", []),  
  ("sw_freighter",0,"freighter","bo_freighter", []),  
  ("sw_hutt_cruiser",0,"Hutt_Cruiser","bo_Hutt_Cruiser", []),
  ("sw_scyk_fighter",0,"hutt_scyk_fighter","bo_hutt_scyk_fighter", []),  
  #("sw_hutt_transport",0,"hutt_transport","bo_hutt_transport", []),  
  ("sw_imperial_shuttle",0,"imperial_shuttle","bo_imperial_shuttle", []),  
  ("sw_imperial_star_destroyer",0,"Imp_ISD","bo_Imp_ISD", []),  
  ("sw_imperial_star_destroyer_interdictor",0,"Imp_ISD_Interdictor","bo_Imp_ISD_Interdictor", []),  
  ("sw_imperial_dreadnaught_frigate",0,"Imp_Dreadnaught_Frigate","bo_Imp_Dreadnaught_Frigate", []),  
  ("sw_imperial_victory_c2_frigate",0,"Imp_Victory_Class_II_Frigate","bo_Imp_Victory_Class_II_Frigate", []),  
  ("sw_imperial_trade_frigate",0,"Imp_trade_frigate","bo_Imp_trade_frigate", []),  
  ("sw_mercenary_raider",0,"mercenary_raider","bo_mercenary_raider", []),  
  ("sw_moncal_cruiser",0,"Moncal_Cruiser","bo_Moncal_Cruiser", []),  
  ("sw_corellian_gunship",0,"Cor_Gunship","bo_Cor_Gunship", []),  
  ("sw_corellian_corvette",0,"swy_corellian_corvette","bo_Cor_Gunship", []),  
  ("sw_nebulon",0,"swy_nebulon",0, []),  
  ("sw_shuttle",0,"shuttle","bo_shuttle", []),
  ("sw_asteroid_base",0,"asteroid_base","bo_asteroid_base", []),  
  ("sw_spacestation1",0,"spacestation1","bo_spacestation1", []),  
  ("sw_spacestation2",0,"spacestation1_grey","bo_spacestation2", []),  
  ("sw_spacestation3",0,"spacestation3","bo_spacestation2", []),  
  ("sw_spacestation4",0,"spacestation4","bo_spacestation4", []),  
  ("sw_spacestation5",0,"spacestation5","bo_spacestation5", []),  
 # ("sw_stormtrooper_transport",0,"stormtrooper_transport","bo_stormtrooper_transport", []),  
  ("sw_tie_fighter",0,"tie_fighter","bo_tie_fighter", []),  
  ("sw_tie_fighter_debris",0,"tie_fighter_debris","bo_tie_fighter_debris", []),  
  ("sw_CIS_star_cruiser",0,"CIS_Station","bo_CIS_Station", []),  
  ("sw_y_wing",0,"y_wing_gold","bo_y_wing_gold", []),  
  ("sw_y_wing_debris",0,"y_wing_gold_debris","bo_y_wing_gold_debris", []),  
  ("sw_z95",0,"xwing_landed2","bo_xwing_landed", []),
  ("sw_z95_debris",0,"z95_debris","bo_z95_debris", []),
  ("sw_z96",0,"z96","bo_z96", []),
  ("sw_bulk_frigate",0,"bulk_frigate","bo_bulk_frigate", []),
  
  #vector dalon scene props
  ("sw_ship_hangar_closed",0,"ship_hangar_closed","bo_ship_hangar_closed", []),
  ("sw_ship_hangar_open",0,"ship_hangar_open","bo_ship_hangar_open", []),
  ("sw_gun_turret",0,"gun_turret","bo_gun_turret", []),
  ("sw_chest1",0,"player_chest_sw","bo_player_chest_sw", []),
  ("sw_box_a",sokf_dynamic|sokf_moveable ,"box_a_sw_sp","bo_box_a_sw_sp", []),
  ("sw_box_a",sokf_moveable|sokf_dynamic,"box_a_sw_sp","bo_box_a_sw_sp", []),
  ("sw_box_a_square",sokf_moveable|sokf_dynamic,"box_a_square","bo_box_a_square", []),
  ("sw_box_a_square_blue",sokf_moveable|sokf_dynamic,"box_a_square_blue","bo_box_a_square", []),
  ("sw_box_a_square_brown",sokf_moveable|sokf_dynamic,"box_a_square_brown","bo_box_a_square", []),
  ("sw_box_a_square_red",sokf_moveable|sokf_dynamic,"box_a_square_red","bo_box_a_square", []),
  ("sw_box_a_square_yellow",sokf_moveable|sokf_dynamic,"box_a_square_yellow","bo_box_a_square", []),
  ("sw_bacta_tank",0,"bacta_tank","bo_bacta_tank", []),  
  ("sw_bacta_tank_new",0,"bacta_tank_new","bo_bacta_tank_new", []),
  ("sw_bacta_tank_new_heal",0,"bacta_tank_new","0", []),
  ("sw_antenna",0,"sw_antenna","bo_sw_antenna", []),  
  ("sw_box_b",sokf_moveable|sokf_dynamic,"sw_box_b","bo_sw_box_b", []),
  ("sw_box_c",sokf_moveable|sokf_dynamic,"sw_box_c","bo_sw_box_c", []),
  ("sw_box_d",sokf_moveable|sokf_dynamic,"sw_box_d","bo_sw_box_d", []),
  ("sw_box_e",sokf_moveable|sokf_dynamic,"sw_box_e","bo_sw_box_e", []),  
  ("sw_part_a",0,"sw_part_a","bo_sw_part_a", []),  
  ("sw_part_b",0,"sw_part_b","bo_sw_part_b", []),  
  ("sw_tower_a",0,"sw_tower_a","bo_sw_tower_a", []),  
  ("sw_tower_b",0,"sw_tower_b","bo_sw_tower_b", []),  
  ("sw_tower_c",0,"sw_tower_c","bo_sw_tower_c", []),  
  ("sw_yavin_addon",0,"yavinaddon","bo_yavinaddon", []),
  ("sw_yavin_pillar1",0,"yavinpillar1","bo_yavinpillar1", []),
  ("sw_yavin_pillar2",0,"yavinpillar2","bo_yavinpillar2", []),
  ("sw_yavin_spire",0,"yavinspire","bo_yavinspire", []),
  ("sw_yavin_statue1",0,"yavinstatue1","bo_yavinstatue1", []),
  ("sw_yavin_statue2",0,"yavinstatue2","bo_yavinstatue2", []),
  ("sw_yavin_statue3",0,"yavinstatue3","bo_yavinstatue3", []),
  ("sw_yavin_steps",0,"yavinsteps","bo_yavinsteps", []),
  ("sw_yavin_table1",0,"yavintable1","bo_yavintable1", []),
  ("sw_yavin_temple",0,"yavintempleblend","bo_yavintempleblend", []),
  ("sw_yavin_wall1",0,"yavinwall1","bo_yavinwall1", []),
  ("sw_yavin_wall2",0,"yavinwall2","bo_yavinwall2", []),
  ("sw_yavin_wall3",0,"yavinwall3","bo_yavinwall3", []),
  
## -----------> New Yavin Stuff
("sw_Yavin_Arch",0,"Yavin_Arch","bo_Yavin_Arch", []),
("sw_Yavin_Block_A",0,"Yavin_Block_A","bo_Yavin_Block_A", []),
("sw_Yavin_Bridge_Large",0,"Yavin_Bridge_Large","bo_Yavin_Bridge_Large", []),
("sw_Yavin_Bridge_Large_Broken_A",0,"Yavin_Bridge_Large_Broken_A","bo_Yavin_Bridge_Large_Broken_A", []),
("sw_Yavin_Bridge_Large_Broken_B",0,"Yavin_Bridge_Large_Broken_B","bo_Yavin_Bridge_Large_Broken_B", []),
("sw_Yavin_Bridge_Large_Cracked",0,"Yavin_Bridge_Large_Cracked","bo_Yavin_Bridge_Large_Cracked", []),
("sw_Yavin_House_1",0,"Yavin_House_1","bo_Yavin_House_1", []),
("sw_Yavin_House_2",0,"Yavin_House_2","bo_Yavin_House_2", []),
("sw_Yavin_House_3",0,"Yavin_House_3","bo_Yavin_House_3", []),
("sw_Yavin_Platform",0,"Yavin_Platform","bo_Yavin_Platform", []),
("sw_Yavin_Ramp_A",0,"Yavin_Ramp_A","bo_Yavin_Ramp_A", []),
("sw_Yavin_Ramp_B",0,"Yavin_Ramp_B","bo_Yavin_Ramp_B", []),
("sw_Yavin_Stairs",0,"Yavin_Stairs","bo_Yavin_Stairs", []),
("sw_Yavin_Statue_4",0,"Yavin_Statue_4","bo_Yavin_Statue_4", []),
("sw_Yavin_Statue_5",0,"Yavin_Statue_5","bo_Yavin_Statue_4", []),
("sw_Yavin_Statue_6",0,"Yavin_Statue_6","bo_Yavin_Statue_4", []),
("sw_Yavin_Temple_2",0,"Yavin_Temple_2","bo_Yavin_Temple_2", []),
("sw_Yavin_Tower_1",0,"Yavin_Tower_1","bo_Yavin_Tower_1", []),
("sw_Yavin_Tower_2",0,"Yavin_Tower_2","bo_Yavin_Tower_2", []),
("sw_Yavin_Wall_Big",0,"Yavin_Wall_Big","bo_Yavin_Wall_Big", []),
("sw_Yavin_Wall_Big_Broken",0,"Yavin_Wall_Big_Broken","bo_Yavin_Wall_Big_Broken", []),
("sw_Yavin_Wall_Big_Hole",0,"Yavin_Wall_Big_Hole","bo_Yavin_Wall_Big_Hole", []),
("sw_Yavin_Wall_Big_Hole_2",0,"Yavin_Wall_Big_Hole_2","bo_Yavin_Wall_Big_Hole_2", []),
("sw_Yavin_Wall_Big_Hub",0,"Yavin_Wall_Big_Hub","bo_Yavin_Wall_Big_Hub", []),
("sw_Yavin_Stairs_Large",0,"Yavin_Stairs_Large","bo_Yavin_Stairs_Large", []),
("sw_Yavin_Great_Temple",0,"Yavin_Great_Temple","bo_Yavin_Great_Temple", []),

## <---  

  ("sw_hoth_bunker",0,"hoth_bunker","bo_hoth_bunker", []),
  ("sw_shield",0,"hoth_shield","bo_hoth_shield", []),
  ("sw_hoth_trench1",0,"hoth_trench1","bo_hoth_trench1", []),
  ("sw_hoth_trench2",0,"hoth_trench2","bo_hoth_trench2", []),
  ("sw_hoth_trench3",0,"hoth_trench3","bo_hoth_trench3", []),
  ("sw_hoth_turret1",0,"hoth_turret2","bo_hoth_turret2", []),
  ("sw_hoth_turret2",0,"hoth_turret2","bo_hoth_turret2", []),
  ("sw_building_prefab1",0,"building_prefab1","bo_building_prefab1", []),
  ("sw_building_prefab2",0,"building_prefab2","bo_building_prefab2", []),
  ("sw_building_prefab_ramp1",0,"building_prefab_ramp1","bo_building_prefab_ramp1", []),
  ("sw_terminal1",0,"terminal1","bo_terminal1_2", []),
  ("sw_terminal2",0,"terminal2","bo_terminal1_2", []),
  ("sw_holocron_new_a",sokf_moveable|sokf_dynamic,"holocron_new_a","bo_holocron_new", []),
  ("sw_holocron_new_b",sokf_moveable|sokf_dynamic,"holocron_new_b","bo_holocron_new", []),
  ("sw_holocron_new_c",sokf_moveable|sokf_dynamic,"holocron_new_c","bo_holocron_new", []),
  ("sw_holocron_new_d",sokf_moveable|sokf_dynamic,"holocron_new_d","bo_holocron_new", []),
  ("sw_holocron_new_e",sokf_moveable|sokf_dynamic,"holocron_new_e","bo_holocron_new", []),
  # ("sw_holocron_old_blue",0,"holocron_blue","bo_holocron_old", []),
  # ("sw_holocron_old_green",0,"holocron_green","bo_holocron_old", []),
  # ("sw_holocron_old_red",0,"holocron_red","bo_holocron_old", []),

  ("xwing_landed",0,"xwing_landed","bo_xwing_landed", []),
  ("xwing_landed2",0,"xwing_landed2","bo_xwing_landed", []),
  ("xwing_landed3",0,"xwing_landed3","bo_xwing_landed", []),
  ("xwing_landed4",0,"xwing_landed4","bo_xwing_landed", []),
  ("xwing_landed5",0,"xwing_landed5","bo_xwing_landed", []),
 
  #bonus chests
  ("sw_bonus_chest",sokf_type_container,"box_a_square","bo_box_a_square", []),
  #("sw_bonus_chest",sokf_type_container,"player_chest_sw","bo_player_chest_sw", []),
  
  #happy stormtrooper scene props
  ("sw_endor_bunker",0,"endor_bunker_open","bo_endor_bunker", []),  
  ("sw_endor_bunker_closed",0,"endor_bunker_closed","bo_endor_bunker", []),  
  ("sw_garage_desert",0,"garage_desert","bo_garage", []),
  ("sw_garage_metal",0,"garage_metal","bo_garage", []),
  ("sw_garage_rusty",0,"garage_rusty","bo_garage", []),
  ("sw_sarlacc",0,"sarlacc","bo_sarlacc", []),  
  
  #freddex scene props
  ("sw_building_new_a",0,"building_new_a","bo_building_new_a", []),  
  ("sw_bunker_concrete",0,"bunker_concrete","bo_bunker_metal_a", []),  
  ("sw_bunker_metal_a",0,"bunker_metal_a","bo_bunker_metal_a", []),
  ("sw_bunker_metal_b",0,"bunker_metal_b","bo_bunker_metal_a", []),
  ("sw_bunker_sandstone",0,"bunker_sandstone","bo_bunker_metal_a", []),
  ("sw_wall_new_concrete",0,"wall_new_concrete","bo_wall_new_metal_a", []),
  ("sw_wall_new_glass_cubes",0,"wall_new_glass_cubes","bo_wall_new_metal_a", []),
  ("sw_wall_new_metal_a",0,"wall_new_metal_a","bo_wall_new_metal_a", []),
  ("sw_wall_new_metal_b",0,"wall_new_metal_b","bo_wall_new_metal_a", []),
  ("sw_wall_new_sandstone",0,"wall_new_sandstone","bo_wall_new_metal_a", []),  
  
  #wookiee padawan / mr sparrow scene props
  ("sw_ruin_02",0,"ruin_02","bo_ruin_02", []),  
  ("sw_ruin_03",0,"ruin_03","bo_ruin_03", []),  
  
  #geroj scene props
  ("sw_geonosian_addon_a",0,"geonosian_addon_a","bo_geonosian_addon_a", []),  
  ("sw_geonosian_gate",0,"geonosian_gate","bo_geonosian_gate", []),  
  ("sw_geonosian_hive",0,"geonosian_hive","bo_geonosian_hive", []),  
  ("sw_geonosian_house_a",0,"geonosian_house_a","bo_geonosian_house_a", []),  
  ("sw_naboo_addon_a",0,"naboo_addon_a","bo_naboo_addon_a", []),  
  ("sw_naboo_addon_b",0,"naboo_addon_b","bo_naboo_addon_b", []),  
  ("sw_naboo_altan",0,"naboo_altan","bo_naboo_altan", []),  
  ("sw_naboo_column",0,"naboo_column","bo_naboo_column", []),  
  ("sw_naboo_fountain",0,"naboo_fountain","bo_naboo_fountain", []),  
  ("sw_naboo_house_a",0,"naboo_house_a","bo_naboo_house_a", []),  
  ("sw_naboo_house_b",0,"naboo_house_b","bo_naboo_house_b", []),  
  ("sw_naboo_house_c",0,"naboo_house_c","bo_naboo_house_c", []),  
  ("sw_naboo_planter",0,"naboo_planter","bo_naboo_planter", []),  
  ("sw_naboo_tower_a",0,"naboo_tower_a","bo_naboo_tower_a", []),  
  ("sw_naboo_tower_b",0,"naboo_tower_b","bo_naboo_tower_b", []),  
  ("sw_naboo_wall",0,"naboo_wall","bo_naboo_wall", []),  
  ("sw_naboo_window_a",0,"naboo_window_a","bo_naboo_window_a", []),  
  ("sw_naboo_window_b",0,"naboo_window_b","bo_naboo_window_b", []),  
  ("sw_ryloth_tower",0,"ryloth_tower","bo_ryloth_tower", []),  
  ("sw_rock_a",0,"sw_rock_a","bo_sw_rock_a", []),  
  ("sw_rock_b",0,"sw_rock_b","bo_sw_rock_b", []),  
  ("sw_waterfall",0,"sw_waterfall","bo_sw_waterfall", []),      
  ("sw_cantina_bar",0,"sw_cantina_bar","bo_sw_cantina_bar", []),  
  ("sw_cantina_bar_with_items",0,"sw_cantina_bar_with_items","bo_sw_cantina_bar", []),    
  ("sw_table_a",0,"sw_table_a","bo_sw_table_a", []), 
  ("sw_beer_a",0,"sw_beer_a","0", []),
  ("sw_glass_a",sokf_moveable|sokf_dynamic,"sw_glass_a","0", []),
  ("sw_glass_b",sokf_moveable|sokf_dynamic,"sw_glass_b","0", []),
  ("sw_glass_c",sokf_moveable|sokf_dynamic,"sw_glass_c","0", []),
  ("sw_plate_a",0,"sw_plate_a","0", []),
  ("sw_plate_a_full",0,"sw_plate_a_full","0", []),
  ("sw_arena_sign",0,"sw_arena_arms","0", []),  
  ("sw_barrel",0,"sw_barrel","bo_sw_barrel", []),
  ("sw_holochess",0,"sw_holochess","bo_sw_holochess", []),  
  ("sw_recruiting_sign",0,"sw_recruiting_sign","bo_sw_recruiting_sign", []),
  ("sw_torch",0,"sw_torch_a","0",[]),
  ("sw_training_remote",0,"training_remote_prop","bo_training_remote_prop",[]),  
  ("sw_kashyyk_addon_a",0,"kashyyk_addon_a","bo_kashyyk_addon_a", []),
  ("sw_kashyyk_addon_b",0,"kashyyk_addon_b","bo_kashyyk_addon_b", []),
  ("sw_kashyyk_bridge",0,"kashyyk_bridge","bo_kashyyk_bridge", []),
  ("sw_kashyyk_fence_a",0,"kashyyk_fence_a","bo_kashyyk_fence_a", []),
  ("sw_kashyyk_fence_b",0,"kashyyk_fence_b","bo_kashyyk_fence_b", []),
  ("sw_kashyyk_house_a",0,"kashyyk_house_a","bo_kashyyk_house_a", []),
  ("sw_kashyyk_house_b",0,"kashyyk_house_b","bo_kashyyk_house_b", []),
  ("sw_kashyyk_platform_a",0,"kashyyk_platform_a","bo_kashyyk_platform_a", []),
  ("sw_kashyyk_platform_b",0,"kashyyk_platform_b","bo_kashyyk_platform_b", []),
  ("sw_kashyyk_platform_c",0,"kashyyk_platform_c","bo_kashyyk_platform_c", []),
  ("sw_kashyyk_stairs",0,"kashyyk_stairs","bo_kashyyk_stairs", []),
  ("sw_kashyyk_tree_a",0,"kashyyk_tree_a","bo_kashyyk_tree_a", []),
  ("sw_kashyyk_tree_b",0,"kashyyk_tree_b","bo_kashyyk_tree_b", []),
  ("sw_kashyyk_tree_top",0,"kashyyk_tree_top","0", []),
  ("sw_castle_battlement_a",0,"sw_castle_battlement_a","bo_sw_castle_battlement_a", []),
  ("sw_castle_battlement_b",0,"sw_castle_battlement_b","bo_sw_castle_battlement_b", []),
  ("sw_castle_battlement_corner_a",0,"sw_castle_battlement_corner_a","bo_sw_castle_battlement_corner_a", []),
  ("sw_castle_battlement_corner_b",0,"sw_castle_battlement_corner_b","bo_sw_castle_battlement_corner_b", []),
  ("sw_castle_battlement_stairs_a",0,"sw_castle_battlement_stairs_a","bo_sw_castle_battlement_stairs_a", []),
  ("sw_castle_battlement_stairs_b",0,"sw_castle_battlement_stairs_b","bo_sw_castle_battlement_stairs_b", []),
  ("sw_castle_gate_house_a",0,"sw_castle_gate_house_a","bo_sw_castle_gate_house_a", []),
  ("sw_castle_square_keep_a",0,"sw_castle_square_keep_a","bo_sw_castle_square_keep_a", []),
  ("sw_castle_square_keep_b",0,"sw_castle_square_keep_a","bo_sw_castle_square_keep_a", []),  
  #signs
  ("sw_sign_random_all_1",0,"sw_sign_e","bo_sw_sign_a", []),
  ("sw_sign_random_all_2",0,"sw_sign_e","bo_sw_sign_a", []),
  ("sw_sign_random_all_3",0,"sw_sign_e","bo_sw_sign_a", []),
  ("sw_sign_random_all_4",0,"sw_sign_e","bo_sw_sign_a", []),
  ("sw_sign_random_galacticempire",0,"sw_sign_a","bo_sw_sign_a", []),
  ("sw_sign_random_rebelalliance",0,"sw_sign_a","bo_sw_sign_a", []),
  ("sw_sign_random_huttcartel",0,"sw_sign_a","bo_sw_sign_a", []),
  ("sw_sign_random_townfaction_4",0,"sw_sign_a","bo_sw_sign_a", []),
  ("sw_sign_random_generic_1",0,"sw_sign_i","bo_sw_sign_a", []),
  ("sw_sign_random_generic_2",0,"sw_sign_i","bo_sw_sign_a", []),
  ("sw_sign_random_generic_3",0,"sw_sign_i","bo_sw_sign_a", []),
  ("sw_sign_random_generic_4",0,"sw_sign_i","bo_sw_sign_a", []),
  #empire
  ("sw_sign_a",0,"sw_sign_a","bo_sw_sign_a", []),
  ("sw_sign_c",0,"sw_sign_c","bo_sw_sign_a", []),
  ("sw_sign_h",0,"sw_sign_h","bo_sw_sign_a", []),
  ("sw_sign_k",0,"sw_sign_k","bo_sw_sign_a", []),
  ("sw_sign_s",0,"sw_sign_s","bo_sw_sign_a", []),
  ("sw_sign_t",0,"sw_sign_t","bo_sw_sign_a", []),
  ("sw_sign_w",0,"sw_sign_w","bo_sw_sign_a", []),
  #rebel
  ("sw_sign_b",0,"sw_sign_b","bo_sw_sign_a", []),
  ("sw_sign_d",0,"sw_sign_d","bo_sw_sign_a", []),
  ("sw_sign_f",0,"sw_sign_f","bo_sw_sign_a", []),
  ("sw_sign_g",0,"sw_sign_g","bo_sw_sign_a", []),
  ("sw_sign_u",0,"sw_sign_u","bo_sw_sign_a", []),
  ("sw_sign_x",0,"sw_sign_x","bo_sw_sign_a", []),
  #generic
  ("sw_sign_e",0,"sw_sign_e","bo_sw_sign_a", []),
  ("sw_sign_i",0,"sw_sign_i","bo_sw_sign_a", []),
  ("sw_sign_j",0,"sw_sign_j","bo_sw_sign_a", []),
  ("sw_sign_l",0,"sw_sign_l","bo_sw_sign_a", []),
  ("sw_sign_m",0,"sw_sign_m","bo_sw_sign_a", []),
  ("sw_sign_n",0,"sw_sign_n","bo_sw_sign_a", []),
  ("sw_sign_o",0,"sw_sign_o","bo_sw_sign_a", []),
  ("sw_sign_p",0,"sw_sign_p","bo_sw_sign_a", []),
  ("sw_sign_q",0,"sw_sign_q","bo_sw_sign_a", []),
  ("sw_sign_r",0,"sw_sign_r","bo_sw_sign_a", []),
  ("sw_sign_v",0,"sw_sign_v","bo_sw_sign_a", []),
  #sw_poster_random_all_1 is sw_sign_end
  ("sw_poster_random_all_1",0,"sw_poster_e","bo_sw_poster_a", []),
  ("sw_poster_random_all_2",0,"sw_poster_e","bo_sw_poster_a", []),
  ("sw_poster_random_all_3",0,"sw_poster_e","bo_sw_poster_a", []),
  ("sw_poster_random_all_4",0,"sw_poster_e","bo_sw_poster_a", []),
  ("sw_poster_random_towngalacticempire",0,"sw_poster_a","bo_sw_poster_a", []),
  ("sw_poster_random_townrebelalliance",0,"sw_poster_a","bo_sw_poster_a", []),
  ("sw_poster_random_townhuttcartel",0,"sw_poster_a","bo_sw_poster_a", []),
  ("sw_poster_random_townfaction_4",0,"sw_poster_a","bo_sw_poster_a", []),
  ("sw_poster_random_generic_1",0,"sw_poster_i","bo_sw_poster_a", []),  
  ("sw_poster_random_generic_2",0,"sw_poster_i","bo_sw_poster_a", []),  
  ("sw_poster_random_generic_3",0,"sw_poster_i","bo_sw_poster_a", []),  
  ("sw_poster_random_generic_4",0,"sw_poster_i","bo_sw_poster_a", []), 
  ("swc_junk_a",0,"swc_junk_a","bo_swc_junk_a", []),
  ("swc_junk_b",0,"swc_junk_b","bo_swc_junk_b", []),
  ("swc_junk_c",0,"swc_junk_c","bo_swc_junk_c", []),
  ("swc_shop",0,"swc_shop","bo_swc_shop", []),

  #empire
  ("sw_poster_a",0,"sw_poster_a","bo_sw_poster_a", []),
  ("sw_poster_c",0,"sw_poster_c","bo_sw_poster_a", []),
  ("sw_poster_h",0,"sw_poster_h","bo_sw_poster_a", []),
  ("sw_poster_k",0,"sw_poster_k","bo_sw_poster_a", []),
  ("sw_poster_s",0,"sw_poster_s","bo_sw_poster_a", []),
  ("sw_poster_t",0,"sw_poster_t","bo_sw_poster_a", []),
  ("sw_poster_w",0,"sw_poster_w","bo_sw_poster_a", []),
  #rebel
  ("sw_poster_b",0,"sw_poster_b","bo_sw_poster_a", []),
  ("sw_poster_d",0,"sw_poster_d","bo_sw_poster_a", []),
  ("sw_poster_f",0,"sw_poster_f","bo_sw_poster_a", []),
  ("sw_poster_g",0,"sw_poster_g","bo_sw_poster_a", []),
  ("sw_poster_u",0,"sw_poster_u","bo_sw_poster_a", []),
  ("sw_poster_x",0,"sw_poster_x","bo_sw_poster_a", []),
  #generic
  ("sw_poster_e",0,"sw_poster_e","bo_sw_poster_a", []),
  ("sw_poster_i",0,"sw_poster_i","bo_sw_poster_a", []),
  ("sw_poster_j",0,"sw_poster_j","bo_sw_poster_a", []),
  ("sw_poster_l",0,"sw_poster_l","bo_sw_poster_a", []),
  ("sw_poster_m",0,"sw_poster_m","bo_sw_poster_a", []),
  ("sw_poster_n",0,"sw_poster_n","bo_sw_poster_a", []),
  ("sw_poster_o",0,"sw_poster_o","bo_sw_poster_a", []),
  ("sw_poster_p",0,"sw_poster_p","bo_sw_poster_a", []),
  ("sw_poster_q",0,"sw_poster_q","bo_sw_poster_a", []),
  ("sw_poster_r",0,"sw_poster_r","bo_sw_poster_a", []),
  ("sw_poster_v",0,"sw_poster_v","bo_sw_poster_a", []),
  #sw_ship_bed is sw_poster_end
  ("sw_ship_bed",0,"ship_bed","bo_ship_bed", []),
  ("sw_ship_box1",sokf_moveable|sokf_dynamic,"ship_box1","bo_ship_box1", []),
  ("sw_ship_box2",sokf_moveable|sokf_dynamic,"ship_box2","bo_ship_box2", []),
  ("sw_ship_comp1",0,"ship_comp1","bo_ship_comp1", []),
  ("sw_ship_comp2",0,"ship_comp2","bo_ship_comp2", []),
  ("sw_ship_door1a",0,"ship_door1a","bo_ship_door1a", []),
  ("sw_ship_door1b",0,"ship_door1b","bo_ship_door1b", []),
  ("sw_ship_door2",0,"ship_door2","bo_ship_door2", []),
  ("sw_ship_light",0,"ship_light","bo_ship_light", []),
  ("sw_ship_part1",0,"ship_part1","bo_ship_part1", []),
  ("sw_ship_part2",0,"ship_part2","bo_ship_part2", []),
  ("sw_ship_part3",0,"ship_part3","bo_ship_part3", []),
  ("sw_ship_part4",0,"ship_part4","bo_ship_part4", []),
  ("sw_ship_part5",0,"ship_part5","bo_ship_part5", []),
  ("sw_ship_part6",0,"ship_part6","bo_ship_part6", []),
  ("sw_ship_part7",0,"ship_part7","bo_ship_part7", []),
  ("sw_ship_part8",0,"ship_part8","bo_ship_part8", []),
  ("sw_ship_part9",0,"ship_part9","bo_ship_part9", []),
  ("sw_ship_pillar",0,"ship_pillar","bo_ship_pillar", []),
  ("sw_ship_platform",0,"ship_platform","bo_ship_platform", []),
  ("sw_ship_shields",0,"ship_shields","bo_ship_shields", []),
  ("sw_ship_shields_destructible",sokf_destructible|sokf_moveable,"ship_shields","bo_ship_shields",   #spr_hit_points don't work, max of 100 ?
   [
    (ti_on_scene_prop_destroy,
    [
        (store_trigger_param_1, ":instance_no"),
        (prop_instance_get_position, pos2, ":instance_no"),
        (play_sound, "snd_dummy_destroyed"),
		(particle_system_burst, "psys_explosion_fire", pos1, 100),		#percentage_burst_strength is 100
        #(position_rotate_x, 5),			#use these if you wish to rotate it
        #(position_rotate_y, 5),
        #(position_rotate_z, 5),		
        (position_move_z, pos2, -1200),		#up/down			#move the door out of the way (underground)
		#(position_move_x, pos2, -200),		#left/right
		#(position_move_y, pos2, -200),		#forward/back
        (prop_instance_animate_to_position, ":instance_no", 2, 800), #animate to position in 8 seconds
    ]),
    (ti_on_scene_prop_hit,
    [
        (play_sound, "snd_dummy_hit"),
        (particle_system_burst, "psys_dummy_smoke", pos1, 100),		#percentage_burst_strength is 100
		#(particle_system_burst, "psys_explosion_fire", pos1, 10),		#percentage_burst_strength is 100
    ]),		
   ],
   200), 	# adding extra number which will be used for hit_points - had to manually updated process_scene_props.py to use for this
  
  ("sw_ship_wall1",0,"ship_wall1","bo_ship_wall1", []),
  ("sw_ship_wall2",0,"ship_wall2","bo_ship_wall2", []),
  ("sw_ship_wall3",0,"ship_wall3","bo_ship_wall3", []),
  ("sw_ship_wall3_destructible",sokf_destructible|sokf_moveable,"ship_wall3","bo_ship_wall3",   #spr_hit_points don't work, max of 100 ?
   [
    (ti_on_scene_prop_destroy,
    [
        (store_trigger_param_1, ":instance_no"),
        (prop_instance_get_position, pos2, ":instance_no"),
        (play_sound, "snd_dummy_destroyed"),
		(particle_system_burst, "psys_explosion_fire", pos1, 100),		#percentage_burst_strength is 100
        #(position_rotate_x, 5),			#use these if you wish to rotate it
        #(position_rotate_y, 5),
        #(position_rotate_z, 5),		
        (position_move_z, pos2, -1200),		#up/down			#move the door out of the way (underground)
		#(position_move_x, pos2, -200),		#left/right
		#(position_move_y, pos2, -200),		#forward/back
        (prop_instance_animate_to_position, ":instance_no", 2, 800), #animate to position in 8 seconds
    ]),
    (ti_on_scene_prop_hit,
    [
        (play_sound, "snd_dummy_hit"),
        (particle_system_burst, "psys_dummy_smoke", pos1, 100),		#percentage_burst_strength is 100
		#(particle_system_burst, "psys_explosion_fire", pos1, 10),		#percentage_burst_strength is 100
    ]),		
   ],
   200), 	# adding extra number which will be used for hit_points - had to manually updated process_scene_props.py to use for this  
   #other
  ("sw_ship_chest",sokf_moveable|sokf_dynamic,"ship_chest","bo_ship_chest", []),
  ("sw_ship_ventilation",0,"ship_ventilation","bo_ship_ventilation", []),
  ("sw_ship_space",0,"ship_space","bo_ship_space", []),
  ("sw_ship_keyboard",0,"ship_keyboard","bo_ship_keyboard", []),   
  #alternative concrete texture
  ("sw_concrete_part1",0,"concrete_part1","bo_ship_part1", []),
  ("sw_concrete_part2",0,"concrete_part2","bo_ship_part2", []),
  ("sw_concrete_part3",0,"concrete_part3","bo_ship_part3", []),
  ("sw_concrete_part4",0,"concrete_part4","bo_ship_part4", []),
  ("sw_concrete_part5",0,"concrete_part5","bo_ship_part5", []),
  ("sw_concrete_part6",0,"concrete_part6","bo_ship_part6", []),
  ("sw_concrete_part7",0,"concrete_part7","bo_ship_part7", []),
  ("sw_concrete_part8",0,"concrete_part8","bo_ship_part8", []),
  ("sw_concrete_part9",0,"concrete_part9","bo_ship_part9", []),
  ("sw_concrete_pillar",0,"concrete_pillar","bo_ship_pillar", []),   
  ("sw_concrete_wall1",0,"concrete_wall1","bo_ship_wall1", []),
  #bothan by geroj
  ("sw_bothan_building1",0,"bothan_building1","bo_bothan_building1", []),
  ("sw_bothan_building2",0,"bothan_building2","bo_bothan_building2", []),
  ("sw_bothan_building3",0,"bothan_building3","bo_bothan_building3", []),
  ("sw_bothan_wall1",0,"bothan_wall1","bo_bothan_wall1", []),
  ("sw_bothan_wall2",0,"bothan_wall2","bo_bothan_wall2", []),
  ("sw_bothan_road1",0,"bothan_road1","bo_bothan_road1", []),
  ("sw_bothan_road2",0,"bothan_road2","bo_bothan_road2", []),
  ("sw_palm_tree1",0,"palm1","bo_palm1", []),
  
  #SupaNinjaMan
  ("sw_kamino_bridge_connector",0,"kamino_bridge_connector","bo_kamino_bridge_connector", []),
  ("sw_kamino_bridge_end",0,"kamino_bridge_end","bo_kamino_bridge_end", []),
  ("sw_kamino_bridge_end_large_platform",0,"kamino_bridge_end_large_platform","bo_kamino_bridge_end_large_platform", []),
  ("sw_kamino_bridge_incline",0,"kamino_bridge_incline","bo_kamino_bridge_incline", []),
  ("sw_kamino_building_beam",0,"kamino_building_beam","bo_kamino_building_beam", []),
  ("sw_kamino_building_dome_a",0,"kamino_building_dome_a","bo_kamino_building_dome_a", []),
  ("sw_kamino_building_dome_b",0,"kamino_building_dome_b","bo_kamino_building_dome_b", []),
  ("sw_kamino_large_platform_1",0,"kamino_large_platform_1","bo_kamino_large_platform_1", []),
  ("sw_kamino_large_platform_2",0,"kamino_large_platform_2","bo_kamino_large_platform_2", []),
  ("sw_kamino_large_platform_3",0,"kamino_large_platform_3","bo_kamino_large_platform_3", []),
  ("sw_kamino_large_platform_4",0,"kamino_large_platform_4","bo_kamino_large_platform_4", []),
  ("sw_kamino_platform_0",0,"kamino_platform_0","bo_kamino_platform_0", []),
  ("sw_kamino_platform_1",0,"kamino_platform_1","bo_kamino_platform_1", []),
  ("sw_kamino_platform_2a",0,"kamino_platform_2a","bo_kamino_platform_2a", []),
  ("sw_kamino_platform_2b",0,"kamino_platform_2b","bo_kamino_platform_2b", []),
  ("sw_kamino_platform_3",0,"kamino_platform_3","bo_kamino_platform_3", []),
  ("sw_kamino_platform_4",0,"kamino_platform_4","bo_kamino_platform_4", []),
  ("sw_kamino_platform_beam",0,"kamino_platform_beam","bo_kamino_platform_beam", []),
  ("sw_kamino_platform_roof_a",0,"kamino_platform_roof_a","bo_kamino_platform_roof_a", []),
  ("sw_kamino_platform_roof_b",0,"kamino_platform_roof_b","bo_kamino_platform_roof_b", []),
  ("sw_kamino_platform_roof_beam",0,"kamino_platform_roof_beam","bo_kamino_platform_roof_beam", []),
  ("sw_kamino_platform_roof_c",0,"kamino_platform_roof_c","bo_kamino_platform_roof_c", []),
  
  #gangs of glasgow models
  ("appartment_grey_wall",0,"appartment_grey_wall","bo_appartment", []),
  ("appartment",0,"appartment","bo_appartment", []),
  ("appartment0",0,"appartment_grey_wall","bo_appartment", []),
  ("appartment1",0,"appartment1","bo_appartment", []),
  ("appartment2",0,"appartment2","bo_appartment", []),
  ("appartment3",0,"appartment3","bo_appartment", []),
  ("appartment4",0,"appartment4","bo_appartment", []),
  ("appartment5",0,"appartment5","bo_appartment", []),
  ("appartment6",0,"appartment6","bo_appartment", []),
  ("appartment7",0,"appartment7","bo_appartment", []),
  ("appartment8",0,"appartment8","bo_appartment", []),
  ("appartment9",0,"appartment9","bo_appartment", []),
  ("appartment10",0,"appartment10","bo_appartment", []),
  ("appartment11",0,"appartment11","bo_appartment", []),
  ("appartment12",0,"appartment12","bo_appartment", []),
  ("appartment13",0,"appartment13","bo_appartment", []),
  ("appartment14",0,"appartment14","bo_appartment", []),
  ("appartment15",0,"appartment15","bo_appartment", []),
  ("appartment16",0,"appartment16","bo_appartment", []),
  ("appartment17",0,"appartment17","bo_appartment", []),
  ("appartment18",0,"appartment18","bo_appartment", []),
  ("appartment19",0,"appartment19","bo_appartment", []),
  ("appartment20",0,"appartment20","bo_appartment", []),
  ("appartment21",0,"appartment21","bo_appartment", []),
  ("appartment22",0,"appartment22","bo_appartment", []),
  ("appartment23",0,"appartment23","bo_appartment", []),
  ("appartment24",0,"appartment24","bo_appartment", []),
  ("appartment25",0,"appartment25","bo_appartment", []),
  ("appartment26",0,"appartment26","bo_appartment", []),
  ("appartment27",0,"appartment27","bo_appartment", []),
  ("appartment28",0,"appartment28","bo_appartment", []),
  ("appartment29",0,"appartment29","bo_appartment", []),
  ("appartment30",0,"appartment30","bo_appartment", []),
  ("appartment31",0,"appartment31","bo_appartment", []),
  ("apptbridge",0,"apptbridge","bo_castle_drawbridges_open", []),  
  
  #from original star wars mod for 0.751
  #("sw_moisture_vaporator",0,"moisture_vaporator","bo_moisture_vaporator", []),  New model by Swyter
  ("sw_moisture_vaporator",0,"swy_moisturevaporator","bo_swy_moisturevaporator", []),
  ("sw_sandstone_building_a",0,"abuilding","bo_abuilding", []),
  ("sw_sandstone_building_b",0,"bbuilding","bo_bbuilding", []),
  ("sw_sandstone_building_c",0,"cbuilding","bo_cbuilding", []),
  ("sw_small_camp",0,"rebelcamp","bo_rebelcamp", []),
  ("sw_tent_a",0,"tent_a","bo_tent_a", []),
  ("sw_tent_b",0,"tent_b","bo_tent_b", []),
  ("sw_tent_c",0,"tent_c","bo_tent_c", []),

  #tyrinius models
  ("sw_microchip",sokf_moveable|sokf_dynamic,"tyr_chip","bo_tyr_chip", []),  
  ("sw_bench_white",0,"tyr_bench","bo_tyr_bench", []),  
  ("sw_bench_white_no_collision",0,"tyr_bench","0", []),  
  ("sw_chair_white",0,"tyr_chair","bo_tyr_chair", []), 
  ("sw_chair_white_no_collision",0,"tyr_chair","0", []), 
  ("sw_shelf_white",0,"tyr_shelf_1","bo_tyr_shelf_1", []),  
  ("sw_shelf_white_closed",0,"tyr_shelf_2","bo_tyr_shelf_2", []),  
  ("sw_table_white",0,"tyr_table","bo_tyr_table", []),  
  
  #takijap models
  ("sw_table_circle",sokf_moveable|sokf_dynamic,"sw_table_circle","bo_sw_table_circle", []),  
  ("sw_chair_a",0,"sw_chair_a","bo_sw_chair_a", []),
  ("sw_chair_a_no_collision",0,"sw_chair_a","0", []),  
  ("sw_bunker_a",0,"bunker_a","bo_bunker_a", []),
  ("sw_bench_a",0,"bench_a","bo_bench_a", []),
  ("sw_bench_curved_a",0,"bench_curved_a","bo_bench_curved_a", []),
  ("sw_chair_b",sokf_moveable|sokf_dynamic,"chair_b","bo_chair_b", []),
  ("sw_chair_b_no_collision",0,"chair_b","0", []),
  ("sw_office_chair_a",0,"office_chair_a","bo_office_chair_a", []),
  ("sw_office_chair_a_no_collision",0,"office_chair_a","0", []),
  ("sw_office_table_a",0,"office_table_a","bo_office_table_a", []),
  ("sw_table_light_a",0,"table_light_a","bo_table_light_a", []),
  ("sw_cantina_building",0,"cantina_bar","bo_cantina_bar", []),
  ("sw_ship_interior",0,"hangar","bo_hangar", []),
  ("sw_imperial_office_brown",0,"imperial_office_brown","bo_imperial_office_ramp", []),
  ("sw_imperial_office_green",0,"imperial_office_green","bo_imperial_office_ramp", []),
  ("sw_imperial_office_grey",0,"imperial_office_grey","bo_imperial_office_ramp", []),
  ("sw_imperial_office_red",0,"imperial_office_red","bo_imperial_office_ramp", []),
  ("sw_imperial_office_red_furnished",0,"imperial_office_red_furnished","bo_imperial_office_furnished", []),
  ("sw_sith_statue_altyr",0,"sith_statue_altyr","bo_sith_statue", []),
  ("sw_sith_statue_black_a",0,"sith_statue_black_a","bo_sith_statue", []),
  ("sw_sith_statue_black_b",0,"sith_statue_black_b","bo_sith_statue", []),
  ("sw_sith_statue_grey",0,"sith_statue_grey","bo_sith_statue", []),
  ("sw_sith_statue_red_a",0,"sith_statue_red_a","bo_sith_statue", []),
  ("sw_sith_statue_red_b",0,"sith_statue_red_b","bo_sith_statue", []),
  ("sw_sith_statue_stone",0,"sith_statue_stone","bo_sith_statue", []),
  ("sw_sith_statue_white",0,"sith_statue_white","bo_sith_statue", []),
  
  #other
  # ("sw_planet_craters",0,"sw_planet_craters","bo_planet", []),
  # ("sw_planet_farmland",0,"sw_planet_farmland","bo_planet", []),
  # ("sw_planet_gas",0,"sw_planet_gas","bo_planet", []),
  # ("sw_planet_green",0,"sw_planet_green","bo_planet", []),
  # ("sw_planet_green_water",0,"sw_planet_green_water","bo_planet", []),
  # ("sw_planet_industrial",0,"sw_planet_industrial","bo_planet", []),
  # ("sw_planet_plain",0,"sw_planet_plain","bo_planet", []),
  # ("sw_planet_snow",0,"sw_planet_snow","bo_planet", []),
  # ("sw_planet_snow_water",0,"sw_snow_water","bo_planet", []),
  
	#New Swyter planets as scene props 
  ("swy_Death_Star",0,"swy_Death_Star","bo_planet", []),
  ("swy_Planet_Coruscant",0,"swy_Planet_Coruscant","bo_planet", []),
  ("swy_Planet_Endor",0,"swy_Planet_Endor","bo_planet", []),
  ("swy_Planet_Kessel",0,"swy_Planet_Kessel","bo_planet", []),
  ("swy_Planet_RaxusPrime",0,"swy_Planet_RaxusPrime","bo_planet", []),
  ("swy_Planet_Sarapin",0,"swy_Planet_Sarapin","bo_planet", []),
  ("swy_Planet_Taris",0,"swy_Planet_Taris","bo_planet", []),
  ("swy_Planet_Tatooine",0,"swy_Planet_Tatooine","bo_planet", []),
  ("swy_Planet_forest",0,"swy_Planet_forest","bo_planet", []),
  ("swy_Planet_frozen",0,"swy_Planet_frozen","bo_planet", []),
  ("swy_Planet_geonosis",0,"swy_Planet_geonosis","bo_planet", []),
  ("swy_rePlanet_craters",0,"swy_rePlanet_craters","bo_planet", []),
  ("swy_rePlanet_earth",0,"swy_rePlanet_earth","bo_planet", []),
  ("swy_Planet_lava",0,"swy_Planet_lava","bo_planet", []),
  ("swy_rePlanet_earth",0,"swy_rePlanet_earth","bo_planet", []),
  ("swy_rePlanet_gas",0,"swy_rePlanet_gas","bo_planet", []),
  ("swy_rePlanet_ice",0,"swy_rePlanet_ice","bo_planet", []),
  ("swy_rePlanet_kashyyyk",0,"swy_rePlanet_kashyyyk","bo_planet", []),
  ("swy_rePlanet_rock",0,"swy_rePlanet_rock","bo_planet", []),
  ("swy_rePlanet_snow",0,"swy_rePlanet_snow","bo_planet", []),
  ("swy_rePlanet_water",0,"swy_rePlanet_water","bo_planet", []),
  ("swy_rePlanet_wilderness",0,"swy_rePlanet_wilderness","bo_planet", []),
  
  ("sw_skull_a",0,"sw_skull_a","0", []),
  ("sw_skull_b",0,"sw_skull_b","0", []),
  ("sw_skull_c",0,"sw_skull_c","0", []),
  ("sw_skull_d",0,"sw_skull_d","0", []),  
  ("sw_cantina_bar_door",0,"sw_cantina_bar_door","0", []),

  ("light_sun",sokf_invisible,"light_sphere","0",  [
     (ti_on_init_scene_prop,
      [
          (neg|is_currently_night),
          (store_trigger_param_1, ":prop_instance_no"),
          (set_fixed_point_multiplier, 100),
          (prop_instance_get_scale, pos5, ":prop_instance_no"),
          (position_get_scale_x, ":scale", pos5),
          (store_time_of_day,reg(12)),
          (try_begin),
            (is_between,reg(12),5,20),
            (store_mul, ":red", 5 * 200, ":scale"),
            (store_mul, ":green", 5 * 193, ":scale"),
            (store_mul, ":blue", 5 * 180, ":scale"),
          (else_try),
            (store_mul, ":red", 5 * 90, ":scale"),
            (store_mul, ":green", 5 * 115, ":scale"),
            (store_mul, ":blue", 5 * 150, ":scale"),
          (try_end),
          (val_div, ":red", 100),
          (val_div, ":green", 100),
          (val_div, ":blue", 100),
          (set_current_color,":red", ":green", ":blue"),
          (set_position_delta,0,0,0),
          (add_point_light, 0, 0),
      ]),
    ]),
  ("light",sokf_invisible,"light_sphere","0",  [
     (ti_on_init_scene_prop,
      [
          (store_trigger_param_1, ":prop_instance_no"),
          (set_fixed_point_multiplier, 100),
          (prop_instance_get_scale, pos5, ":prop_instance_no"),
          (position_get_scale_x, ":scale", pos5),
		  #SW - switching the light to be white instead of yellowish
          #(store_mul, ":red", 3 * 200, ":scale"),
          #(store_mul, ":green", 3 * 145, ":scale"),
          #(store_mul, ":blue", 3 * 45, ":scale"),
          (store_mul, ":red", 2 * 157, ":scale"),
          (store_mul, ":green", 2 * 157, ":scale"),
          (store_mul, ":blue", 2 * 167, ":scale"),
          (val_div, ":red", 100),
          (val_div, ":green", 100),
          (val_div, ":blue", 100),
          (set_current_color,":red", ":green", ":blue"),
          (set_position_delta,0,0,0),
		  #SW - disabled light flicker
          #(add_point_light, 10, 30),
		  (add_point_light, 0, 0),
      ]),
    ]),
  ("light_red",sokf_invisible,"light_sphere","0",  [
     (ti_on_init_scene_prop,
      [
          (store_trigger_param_1, ":prop_instance_no"),
          (set_fixed_point_multiplier, 100),
          (prop_instance_get_scale, pos5, ":prop_instance_no"),
          (position_get_scale_x, ":scale", pos5),
          (store_mul, ":red", 2 * 170, ":scale"),
          (store_mul, ":green", 2 * 100, ":scale"),
          (store_mul, ":blue", 2 * 30, ":scale"),
          (val_div, ":red", 100),
          (val_div, ":green", 100),
          (val_div, ":blue", 100),
          (set_current_color,":red", ":green", ":blue"),
          (set_position_delta,0,0,0),
		  #SW - should I disabled light flicker?  maybe not since its used for fires?
          (add_point_light, 20, 30),
		  #(add_point_light, 0, 0),
      ]),
    ]),
  ("light_night",sokf_invisible,"light_sphere","0",  [
     (ti_on_init_scene_prop,
      [
#          (store_time_of_day,reg(12)),
#          (neg|is_between,reg(12),5,20),
          (is_currently_night, 0),
          (store_trigger_param_1, ":prop_instance_no"),
          (set_fixed_point_multiplier, 100),
          (prop_instance_get_scale, pos5, ":prop_instance_no"),
          (position_get_scale_x, ":scale", pos5),
          (store_mul, ":red", 3 * 160, ":scale"),
          (store_mul, ":green", 3 * 145, ":scale"),
          (store_mul, ":blue", 3 * 100, ":scale"),
          (val_div, ":red", 100),
          (val_div, ":green", 100),
          (val_div, ":blue", 100),
          (set_current_color,":red", ":green", ":blue"),
          (set_position_delta,0,0,0),
          (add_point_light, 10, 30),
      ]),
    ]),
	#SW - switched the torch scene prop model
	("torch",0,"sw_torch_a","0",[]),
  # ("torch",0,"torch_a","0",
   # [
   # (ti_on_init_scene_prop,
    # [
        # (set_position_delta,0,-35,48),
        # (particle_system_add_new, "psys_torch_fire"),
        # (particle_system_add_new, "psys_torch_smoke"),
        # (particle_system_add_new, "psys_torch_fire_sparks"),

        # (play_sound, "snd_torch_loop", 0),
        
        # (set_position_delta,0,-35,56),
        # (particle_system_add_new, "psys_fire_glow_1"),
# #        (particle_system_emit, "psys_fire_glow_1",9000000),

# #second method        
        # (get_trigger_object_position, pos2),
        # (set_position_delta,0,0,0),
        # (position_move_y, pos2, -35),

        # (position_move_z, pos2, 55),
        # (particle_system_burst, "psys_fire_glow_fixed", pos2, 1),
    # ]),
   # ]),
  #SW - switched the torch_night scene prop model
  ("torch_night",0,"sw_torch_a","0",[]),   
  # ("torch_night",0,"torch_a","0",
   # [
   # (ti_on_init_scene_prop,
    # [
# #        (store_time_of_day,reg(12)),
# #        (neg|is_between,reg(12),5,20),
        # (is_currently_night, 0),
        # (set_position_delta,0,-35,48),
        # (particle_system_add_new, "psys_torch_fire"),
        # (particle_system_add_new, "psys_torch_smoke"),
        # (particle_system_add_new, "psys_torch_fire_sparks"),
        # (set_position_delta,0,-35,56),
        # (particle_system_add_new, "psys_fire_glow_1"),
        # (particle_system_emit, "psys_fire_glow_1",9000000),
        # (play_sound, "snd_torch_loop", 0),
    # ]),
   # ]),
#  ("Baggage",sokf_place_at_origin|sokf_entity_body,"package","bobaggage"),
  ("barrier_20m",sokf_invisible|sokf_type_barrier,"barrier_20m","bo_barrier_20m", []),
  ("barrier_16m",sokf_invisible|sokf_type_barrier,"barrier_16m","bo_barrier_16m", []),
  ("barrier_8m" ,sokf_invisible|sokf_type_barrier,"barrier_8m" ,"bo_barrier_8m" , []),
  ("barrier_4m" ,sokf_invisible|sokf_type_barrier,"barrier_4m" ,"bo_barrier_4m" , []),
  ("barrier_2m" ,sokf_invisible|sokf_type_barrier,"barrier_2m" ,"bo_barrier_2m" , []),
  
  ("exit_4m" ,sokf_invisible|sokf_type_barrier_leave,"barrier_4m" ,"bo_barrier_4m" , []),
  ("exit_8m" ,sokf_invisible|sokf_type_barrier_leave,"barrier_8m" ,"bo_barrier_8m" , []),
  ("exit_16m" ,sokf_invisible|sokf_type_barrier_leave,"barrier_16m" ,"bo_barrier_16m" , []),

  ("ai_limiter_2m" ,sokf_invisible|sokf_type_ai_limiter,"barrier_2m" ,"bo_barrier_2m" , []),
  ("ai_limiter_4m" ,sokf_invisible|sokf_type_ai_limiter,"barrier_4m" ,"bo_barrier_4m" , []),
  ("ai_limiter_8m" ,sokf_invisible|sokf_type_ai_limiter,"barrier_8m" ,"bo_barrier_8m" , []),
  ("ai_limiter_16m",sokf_invisible|sokf_type_ai_limiter,"barrier_16m","bo_barrier_16m", []),
  ("Shield",sokf_moveable|sokf_dynamic,"0","boshield", []),
  ("shelves",0,"shelves","boshelves", []),
  ("table_tavern",0,"table_tavern","botable_tavern", []),
  ("table_castle_a",0,"table_castle_a","bo_table_castle_a", []),
  ("chair_castle_a",0,"chair_castle_a","bo_chair_castle_a", []),

  ("pillow_a",0,"pillow_a","bo_pillow", []),
  ("pillow_b",0,"pillow_b","bo_pillow", []),
  ("pillow_c",0,"pillow_c","0", []),


  ("interior_castle_g_square_keep_b",0,"interior_castle_g_square_keep_b","bo_interior_castle_g_square_keep_b", []),



  ("carpet_with_pillows_a",0,"carpet_with_pillows_a","bo_carpet_with_pillows", []),
  ("carpet_with_pillows_b",0,"carpet_with_pillows_b","bo_carpet_with_pillows", []),
  ("table_round_a",sokf_moveable|sokf_dynamic,"table_round_a","bo_table_round_a", []),
  ("table_round_b",sokf_moveable|sokf_dynamic,"table_round_b","bo_table_round_b", []),
  ("fireplace_b",0,"fireplace_b","bo_fireplace_b", []),
  ("fireplace_c",0,"fireplace_c","bo_fireplace_c", []),
  ("sofa_a",0,"sofa_a","bo_sofa", []),
  ("sofa_b",0,"sofa_b","bo_sofa", []),
  ("ewer_a",0,"ewer_a","bo_ewer_a", []),
  ("end_table_a",0,"end_table_a","bo_end_table_a", []),


  # ("fake_houses_steppe_a",0,"fake_houses_steppe_a","0", []),
  # ("fake_houses_steppe_b",0,"fake_houses_steppe_b","0", []),
  # ("fake_houses_steppe_c",0,"fake_houses_steppe_c","0", []),

  # ("boat_destroy",0,"boat_destroy","bo_boat_destroy", []),
  # ("destroy_house_a",0,"destroy_house_a","bo_destroy_house_a", []),
  # ("destroy_house_b",0,"destroy_house_b","bo_destroy_house_b", []),
  # ("destroy_house_c",0,"destroy_house_c","bo_destroy_house_c", []),
  # ("destroy_heap",0,"destroy_heap","bo_destroy_heap", []),
  # ("destroy_castle_a",0,"destroy_castle_a","bo_destroy_castle_a", []),
  # ("destroy_castle_b",0,"destroy_castle_b","bo_destroy_castle_b", []),
  # ("destroy_castle_c",0,"destroy_castle_c","bo_destroy_castle_c", []),
  # ("destroy_castle_d",0,"destroy_castle_d","bo_destroy_castle_d", []),
  # ("destroy_windmill",0,"destroy_windmill","bo_destroy_windmill", []),
  # ("destroy_tree_a",0,"destroy_tree_a","bo_destroy_tree_a", []),
  # ("destroy_tree_b",0,"destroy_tree_b","bo_destroy_tree_b", []),  
  # ("destroy_bridge_a",0,"destroy_bridge_a","bo_destroy_bridge_a", []),  
  # ("destroy_bridge_b",0,"destroy_bridge_b","bo_destroy_bridge_b", []),  


  #SW - switched the Catapult to an ATST
  #("Catapult",0,"Catapult","bo_Catapult", []),
  ("Catapult",0,"ATST_scene_prop","bo_ATST_scene_prop", []),
  #SW - modified broom
  #("broom",0,"broom","0", []),
  ("broom", 0, "0", "0", []),
  ("garlic",sokf_moveable|sokf_dynamic,"garlic","0", []),
  ("garlic_b",sokf_moveable|sokf_dynamic,"garlic_b","0", []),

  #SW - modified destroy_a and destroy_b
  #("destroy_a",0,"destroy_a","0", []),
  #("destroy_b",0,"destroy_b","0", []),
  ("destroy_a",0,"0","0", []),     #"transparent","0", []),
  ("destroy_b",0,"0","0", []),     #"transparent","0", []),



  ("bridge_wooden",0,"bridge_wooden","bo_bridge_wooden", []),
  ("bridge_wooden_snowy",0,"bridge_wooden_snowy","bo_bridge_wooden", []),
  
  ("grave_a",0,"grave_a","bo_grave_a", []),

  
  ("village_house_e",0,"0","0", []),     #"village_house_e","bo_village_house_e", []),
  ("village_house_f",0,"0","0", []),     #"village_house_f","bo_village_house_f", []),
  ("village_house_g",0,"0","0", []),     #"village_house_g","bo_village_house_g", []),
  ("village_house_h",0,"0","0", []),     #"village_house_h","bo_village_house_h", []),
  ("village_house_i",0,"0","0", []),     #"village_house_i","bo_village_house_i", []),
  ("village_house_j",0,"0","0", []),     #"village_house_j","bo_village_house_j", []),
  ("village_wall_a",0,"0","0", []),     #"village_wall_a","bo_village_wall_a", []),
  ("village_wall_b",0,"0","0", []),     #"village_wall_b","bo_village_wall_b", []),

  ("village_snowy_house_a",0,"0","0", []),     #"village_snowy_house_a","bo_village_snowy_house_a", []),
  ("village_snowy_house_b",0,"0","0", []),     #"village_snowy_house_b","bo_village_snowy_house_b", []),
  ("village_snowy_house_c",0,"0","0", []),     #"village_snowy_house_c","bo_village_snowy_house_c", []),
  ("village_snowy_house_d",0,"0","0", []),     #"village_snowy_house_d","bo_village_snowy_house_d", []),
  ("village_snowy_house_e",0,"0","0", []),     #"village_snowy_house_e","bo_village_snowy_house_e", []),
  ("village_snowy_house_f",0,"0","0", []),     #"village_snowy_house_f","bo_village_snowy_house_f", []),



  # ("town_house_steppe_a",0,"town_house_steppe_a","bo_town_house_steppe_a", []),
  # ("town_house_steppe_b",0,"town_house_steppe_b","bo_town_house_steppe_b", []),
  # ("town_house_steppe_c",0,"town_house_steppe_c","bo_town_house_steppe_c", []),
  # ("town_house_steppe_d",0,"town_house_steppe_d","bo_town_house_steppe_d", []),
  # ("town_house_steppe_e",0,"town_house_steppe_e","bo_town_house_steppe_e", []),
  # ("town_house_steppe_f",0,"town_house_steppe_f","bo_town_house_steppe_f", []),
  # ("town_house_steppe_g",0,"town_house_steppe_g","bo_town_house_steppe_g", []),
  # ("town_house_steppe_h",0,"town_house_steppe_h","bo_town_house_steppe_h", []),
  # ("town_house_steppe_i",0,"town_house_steppe_i","bo_town_house_steppe_i", []),

  ("carpet_a",0,"carpet_a","0", []),
  ("carpet_b",0,"carpet_b","0", []),
  ("carpet_c",0,"carpet_c","0", []),
  ("carpet_d",0,"carpet_d","0", []),
  ("carpet_e",0,"carpet_e","0", []),
  ("carpet_f",0,"carpet_f","0", []),

  ("awning_a",0,"awning_a","bo_awning", []),
  ("awning_b",0,"awning_b","bo_awning", []),
  ("awning_c",0,"awning_c","bo_awning", []),
  ("awning_long",0,"awning_long","bo_awning_long", []),
  ("awning_long_b",0,"awning_long_b","bo_awning_long", []),
  ("awning_d",0,"awning_d","bo_awning_d", []),




  ("snowy_barrel_a",0,"snowy_barrel_a","bo_snowy_barrel_a", []),
  ("snowy_fence",0,"snowy_fence","bo_snowy_fence", []),
  ("snowy_wood_heap",0,"snowy_wood_heap","bo_snowy_wood_heap", []),

  ("village_snowy_stable_a",0,"0","0", []),     #"village_snowy_stable_a","bo_village_snowy_stable_a", []),


  # ("village_straw_house_a",0,"village_straw_house_a","bo_village_straw_house_a", []),
  # ("village_stable_a",0,"village_stable_a","bo_village_stable_a", []),
  ("village_shed_a",0,"0","0", []),     #"village_shed_a","bo_village_shed_a", []),
  ("village_shed_b",0,"0","0", []),     #"village_shed_b","bo_village_shed_b", []),

#  ("trunks_snowy",0,"trunks_snowy","0", []),




  ("dungeon_door_cell_a",0,"dungeon_door_cell_a","bo_dungeon_door_cell_a", []),
  ("dungeon_door_cell_b",0,"dungeon_door_cell_b","bo_dungeon_door_cell_b", []),
  ("dungeon_door_entry_a",0,"dungeon_door_entry_a","bo_dungeon_door_entry_a", []),
  ("dungeon_door_entry_b",0,"dungeon_door_entry_b","bo_dungeon_door_entry_a", []),
  ("dungeon_door_entry_c",0,"dungeon_door_entry_c","bo_dungeon_door_entry_a", []),
  ("dungeon_door_direction_a",0,"dungeon_door_direction_a","bo_dungeon_door_direction_a", []),
  ("dungeon_door_direction_b",0,"dungeon_door_direction_b","bo_dungeon_door_direction_a", []),
  ("dungeon_door_stairs_a",0,"dungeon_door_stairs_a","bo_dungeon_door_stairs_a", []),
  ("dungeon_door_stairs_b",0,"dungeon_door_stairs_b","bo_dungeon_door_stairs_a", []),
  # ("dungeon_bed_a",0,"dungeon_bed_a","0", []),
  # ("dungeon_bed_b",0,"dungeon_bed_b","bo_dungeon_bed_b", []),
  # ("torture_tool_a",0,"torture_tool_a","bo_torture_tool_a", []),
  # ("torture_tool_b",0,"torture_tool_b","0", []),
  # ("torture_tool_c",0,"torture_tool_c","bo_torture_tool_c", []),
  ("skeleton_head",0,"skeleton_head","0", []),
  ("skeleton_bone",0,"skeleton_bone","0", []),
  ("skeleton_a",0,"skeleton_a","bo_skeleton_a", []),
  ("dungeon_stairs_a",0,"dungeon_stairs_a","bo_dungeon_stairs_a", []),
  ("dungeon_stairs_b",0,"dungeon_stairs_b","bo_dungeon_stairs_a", []),
  ("dungeon_torture_room_a",0,"dungeon_torture_room_a","bo_dungeon_torture_room_a", []),
  ("dungeon_entry_a",0,"dungeon_entry_a","bo_dungeon_entry_a", []),
  ("dungeon_entry_b",0,"dungeon_entry_b","bo_dungeon_entry_b", []),
  ("dungeon_entry_c",0,"dungeon_entry_c","bo_dungeon_entry_c", []),
  ("dungeon_cell_a",0,"dungeon_cell_a","bo_dungeon_cell_a", []),
  ("dungeon_cell_b",0,"dungeon_cell_b","bo_dungeon_cell_b", []),
  ("dungeon_cell_c",0,"dungeon_cell_c","bo_dungeon_cell_c", []),
  ("dungeon_corridor_a",0,"dungeon_corridor_a","bo_dungeon_corridor_a", []),
  ("dungeon_corridor_b",0,"dungeon_corridor_b","bo_dungeon_corridor_b", []),
  ("dungeon_corridor_c",0,"dungeon_corridor_c","bo_dungeon_corridor_b", []),
  ("dungeon_corridor_d",0,"dungeon_corridor_d","bo_dungeon_corridor_b", []),
  ("dungeon_direction_a",0,"dungeon_direction_a","bo_dungeon_direction_a", []),
  ("dungeon_direction_b",0,"dungeon_direction_b","bo_dungeon_direction_a", []),
  ("dungeon_room_a",0,"dungeon_room_a","bo_dungeon_room_a", []),
  ("dungeon_tower_stairs_a",0,"dungeon_tower_stairs_a","bo_dungeon_tower_stairs_a", []),
  ("dungeon_tower_cell_a",0,"dungeon_tower_cell_a","bo_dungeon_tower_cell_a", []),
  ("tunnel_a",0,"tunnel_a","bo_tunnel_a", []),
  ("tunnel_salt",0,"tunnel_salt","bo_tunnel_salt", []),
  ("salt_a",0,"salt_a","bo_salt_a", []),

  ("tutorial_door_a",sokf_moveable,"tutorial_door_a","bo_tutorial_door_a", []),

 ("tutorial_door_b",sokf_moveable,"tutorial_door_b","bo_tutorial_door_b", []),

  ("tutorial_flag_yellow",sokf_moveable,"tutorial_flag_yellow","0", []),
  ("tutorial_flag_red",sokf_moveable,"tutorial_flag_red","0", []),
  ("tutorial_flag_blue",sokf_moveable,"tutorial_flag_blue","0", []),

  ("interior_prison_a",0,"interior_prison_a","bo_interior_prison_a", []),
  ("interior_prison_b",0,"interior_prison_b","bo_interior_prison_b", []),
  ("interior_prison_cell_a",0,"interior_prison_cell_a","bo_interior_prison_cell_a", []),

  
#  ("interior_prison_c",0,"interior_prison_c","bo_interior_prison_c", []),
  ("interior_prison_d",0,"interior_prison_d","bo_interior_prison_d", []),
  

  ("arena_archery_target_a",0,"arena_archery_target_a","bo_arena_archery_target_a", []),
  ("archery_butt_a",0,"archery_butt","bo_archery_butt", [
   (ti_on_scene_prop_hit,
    [
        (store_trigger_param_1, ":instance_no"),
        (prop_instance_get_position, pos2, ":instance_no"),
        (get_player_agent_no, ":player_agent"),
        (agent_get_position, pos3, ":player_agent"),
        (get_distance_between_positions, ":player_distance", pos3, pos2),
        (position_transform_position_to_local, pos4, pos2, pos1),
        (position_set_y, pos4, 0),
        (position_set_x, pos2, 0),
        (position_set_y, pos2, 0),
        (position_set_z, pos2, 0),
        (get_distance_between_positions, ":target_distance", pos4, pos2),
        (assign, ":point_earned", 43), #Calculating a point between 0-12
        (val_sub, ":point_earned", ":target_distance"),
        (val_mul, ":point_earned", 1299),
        (val_div, ":point_earned", 4300),
        (try_begin),
          (lt, ":point_earned", 0),
          (assign, ":point_earned", 0),
        (try_end),
        (val_div, ":player_distance", 91), #Converting to yards
        (assign, reg60, ":point_earned"),
        (assign, reg61, ":player_distance"),
        (display_message, "str_archery_target_hit"),
    ]),
  ]),
  ("archery_target_with_hit_a",0,"arena_archery_target_a","bo_arena_archery_target_a", [
   (ti_on_scene_prop_hit,
    [
        (store_trigger_param_1, ":instance_no"),
        (prop_instance_get_position, pos2, ":instance_no"),
        (get_player_agent_no, ":player_agent"),
        (agent_get_position, pos3, ":player_agent"),
        (get_distance_between_positions, ":player_distance", pos3, pos2),
        (position_transform_position_to_local, pos4, pos2, pos1),
        (position_set_y, pos4, 0),
        (position_set_x, pos2, 0),
        (position_set_y, pos2, 0),
        (position_set_z, pos2, 0),
        (get_distance_between_positions, ":target_distance", pos4, pos2),
        (assign, ":point_earned", 43), #Calculating a point between 0-12
        (val_sub, ":point_earned", ":target_distance"),
        (val_mul, ":point_earned", 1299),
        (val_div, ":point_earned", 4300),
        (try_begin),
          (lt, ":point_earned", 0),
          (assign, ":point_earned", 0),
        (try_end),
        (val_div, ":player_distance", 91), #Converting to yards
        (assign, "$g_last_archery_point_earned", ":point_earned"),
        (assign, reg60, ":point_earned"),
        (assign, reg61, ":player_distance"),
        (display_message, "str_archery_target_hit"),
    ]),
  ]),
  #SW - modified arena_archery_target_b to be imperial_stormtrooper_armor
  #("dummy_a",sokf_destructible|sokf_moveable,"arena_archery_target_b","bo_arena_archery_target_b",   [
  ("dummy_a",sokf_destructible|sokf_moveable,"imperial_stormtrooper_dummy","bo_arena_archery_target_b",   [
   (ti_on_scene_prop_destroy,
    [
        (store_trigger_param_1, ":instance_no"),
        (prop_instance_get_starting_position, pos1, ":instance_no"),
        (get_player_agent_no, ":player_agent"),
        (agent_get_position, 2, ":player_agent"),
        (assign, ":rotate_side", 80),
        (try_begin),
          (position_is_behind_position, 2, 1),
          (val_mul, ":rotate_side", -1),
        (try_end),
        (position_rotate_x, 1, ":rotate_side"),
        (prop_instance_animate_to_position, ":instance_no", 1, 70), #animate to position 1 in 0.7 second
        (val_add, "$tutorial_num_total_dummies_destroyed", 1),
        (play_sound, "snd_dummy_destroyed"),
    ]),
   (ti_on_scene_prop_hit,
    [
        (store_trigger_param_1, ":instance_no"),
        (store_trigger_param_2, ":damage"),
        (assign, reg60, ":damage"),
        (val_div, ":damage", 8),
        (prop_instance_get_position, pos2, ":instance_no"),
        (get_player_agent_no, ":player_agent"),
        (agent_get_position, pos3, ":player_agent"),
        (try_begin),
          (position_is_behind_position, pos3, pos2),
          (val_mul, ":damage", -1),
        (try_end),
        (position_rotate_x, 2, ":damage"),
        (display_message, "str_delivered_damage"),
        (prop_instance_animate_to_position, ":instance_no", 2, 30), #animate to position 1 in 0.3 second
        (play_sound, "snd_dummy_hit"),
        #(particle_system_burst, "psys_blood_hit_1", pos1, 100), #littles
        #(particle_system_burst, "psys_blood_hit_2", pos1, 1),   #Massive blood part
        #(particle_system_burst, "psys_blood_hit_3", pos1, 10),   #3-4 part of blood
        #(set_position_delta,0,0,50),
        #(prop_instance_get_position, pos2, ":instance_no"),
        (particle_system_burst, "psys_dummy_smoke", pos1, 3),
        (particle_system_burst, "psys_dummy_straw", pos1, 10),

    ]),
  ]),

  ("band_a",0,"band_a","0", []),
  #SW - modified arena_sign
  #("arena_sign",0,"arena_arms","0", []),
  ("arena_sign",0,"sw_arena_arms","0", []),
  # ("castle_h_battlement_a",0,"castle_h_battlement_a","bo_castle_h_battlement_a", []),
  # ("castle_h_battlement_b",0,"castle_h_battlement_b","bo_castle_h_battlement_b", []),
  # ("castle_h_battlement_a2",0,"castle_h_battlement_a2","bo_castle_h_battlement_a2", []),
  # ("castle_h_battlement_b2",0,"castle_h_battlement_b2","bo_castle_h_battlement_b2", []),
  # ("castle_h_corner_a",0,"castle_h_corner_a","bo_castle_h_corner_a", []),
  # ("castle_h_stairs_a",0,"castle_h_stairs_a","bo_castle_h_stairs_a", []),
  # ("castle_h_stairs_b",0,"castle_h_stairs_b","bo_castle_h_stairs_b", []),
  # ("castle_h_gatehouse_a",0,"castle_h_gatehouse_a","bo_castle_h_gatehouse_a", []),
  # ("castle_h_keep_a",0,"castle_h_keep_a","bo_castle_h_keep_a", []),
  # ("castle_h_keep_b",0,"castle_h_keep_b","bo_castle_h_keep_b", []),
  # ("castle_h_house_a",0,"castle_h_house_a","bo_castle_h_house_a", []),
  # ("castle_h_house_b",0,"castle_h_house_b","bo_castle_h_house_b", []),
  # ("castle_h_house_c",0,"castle_h_house_c","bo_castle_h_house_b", []),
  # ("castle_h_battlement_barrier",0,"castle_h_battlement_barrier","bo_castle_h_battlement_barrier", []),





  # ("castle_f_keep_a",0,"castle_f_keep_a","bo_castle_f_keep_a", []),
  # ("castle_f_battlement_a",0,"castle_f_battlement_a","bo_castle_f_battlement_a", []),
  # ("castle_f_battlement_a_destroyed",0,"castle_f_battlement_a_destroyed","bo_castle_f_battlement_a_destroyed", []),
  # ("castle_f_battlement_b",0,"castle_f_battlement_b","bo_castle_f_battlement_b", []),
  # ("castle_f_battlement_corner_a",0,"castle_f_battlement_corner_a","bo_castle_f_battlement_corner_a", []),
  # ("castle_f_battlement_corner_b",0,"castle_f_battlement_corner_b","bo_castle_f_battlement_corner_b", []),
  # ("castle_f_stairs_a",0,"castle_f_stairs_a","bo_castle_f_stairs_a", []),
  # ("castle_f_tower_a",0,"castle_f_tower_a","bo_castle_f_tower_a", []),
  # ("castle_f_wall_stairs_a",0,"castle_f_wall_stairs_a","bo_castle_f_wall_stairs_a", []),
  # ("castle_f_wall_stairs_b",0,"castle_f_wall_stairs_b","bo_castle_f_wall_stairs_b", []),
  # ("castle_f_wall_way_a",0,"castle_f_wall_way_a","bo_castle_f_wall_way_a", []),
  # ("castle_f_wall_way_b",0,"castle_f_wall_way_b","bo_castle_f_wall_way_b", []),
  # ("castle_f_gatehouse_a",0,"castle_f_gatehouse_a","bo_castle_f_gatehouse_a", []),

  # ("castle_g_battlement_a",0,"castle_g_battlement_a","bo_castle_g_battlement_a", []),
  # ("castle_g_corner_a",0,"castle_g_corner_a","bo_castle_g_corner_a", []),
  # ("castle_g_tower_a",0,"castle_g_tower_a","bo_castle_g_tower_a", []),
  # ("castle_g_gate_house",0,"castle_g_gate_house","bo_castle_g_gate_house", []),
  # ("castle_g_gate_house_door_a",0,"castle_g_gate_house_door_a","bo_castle_g_gate_house_door_a", []),
  # ("castle_g_gate_house_door_b",0,"castle_g_gate_house_door_b","bo_castle_g_gate_house_door_b", []),
  # ("castle_g_square_keep_a",0,"castle_g_square_keep_a","bo_castle_g_square_keep_a", []),


  ("mosque_a",0,"0","0", []),
  ("stone_minaret_a",0,"0","0", []),
  # ("stone_house_a",0,"stone_house_a","bo_stone_house_a", []),
  # ("stone_house_b",0,"stone_house_b","bo_stone_house_b", []),
  # ("stone_house_c",0,"stone_house_c","bo_stone_house_c", []),
  # ("stone_house_d",0,"stone_house_d","bo_stone_house_d", []),
  # ("stone_house_e",0,"stone_house_e","bo_stone_house_e", []),
  # ("stone_house_f",0,"stone_house_f","bo_stone_house_f", []),

  ("banner_pole", 0, "banner_pole", "bo_banner_pole", []),

  ("custom_banner_01",0,"custom_banner_01","0",
   [
     (ti_on_init_scene_prop,
      [
        (party_get_slot, ":leader_troop", "$g_encountered_party", slot_mainplanet_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_scene_prop_set_tableau_material, "tableau_custom_banner_default", ":leader_troop"),
        (try_end),
        ]),
     ]),
  ("custom_banner_02",0,"custom_banner_02","0",
   [
     (ti_on_init_scene_prop,
      [
        (party_get_slot, ":leader_troop", "$g_encountered_party", slot_mainplanet_lord),
        (try_begin),
          (ge, ":leader_troop", 0),
          (cur_scene_prop_set_tableau_material, "tableau_custom_banner_default", ":leader_troop"),
        (try_end),
        ]),
     ]),

  ("banner_a",0,"banner_a01","0", []),
  ("banner_b",0,"banner_a02","0", []),
  ("banner_c",0,"banner_a03","0", []),
  ("banner_d",0,"banner_a04","0", []),
  ("banner_e",0,"banner_a05","0", []),
  ("banner_f",0,"banner_a06","0", []),
  ("banner_g",0,"banner_a07","0", []),
  ("banner_h",0,"banner_a08","0", []),
  ("banner_i",0,"banner_a09","0", []),
  ("banner_j",0,"banner_a10","0", []),
  ("banner_k",0,"banner_a11","0", []),
  ("banner_l",0,"banner_a12","0", []),
  ("banner_m",0,"banner_a13","0", []),
  ("banner_n",0,"banner_a14","0", []),
  ("banner_o",0,"banner_f21","0", []),
  ("banner_p",0,"banner_a16","0", []),
  ("banner_q",0,"banner_a17","0", []),
  ("banner_r",0,"banner_a18","0", []),
  ("banner_s",0,"banner_a19","0", []),
  ("banner_t",0,"banner_a20","0", []),
  ("banner_u",0,"banner_a21","0", []),
  ("banner_ba",0,"banner_b01","0", []),
  ("banner_bb",0,"banner_b02","0", []),
  ("banner_bc",0,"banner_b03","0", []),
  ("banner_bd",0,"banner_b04","0", []),
  ("banner_be",0,"banner_b05","0", []),
  ("banner_bf",0,"banner_b06","0", []),
  ("banner_bg",0,"banner_b07","0", []),
  ("banner_bh",0,"banner_b08","0", []),
  ("banner_bi",0,"banner_b09","0", []),
  ("banner_bj",0,"banner_b10","0", []),
  ("banner_bk",0,"banner_b11","0", []),
  ("banner_bl",0,"banner_b12","0", []),
  ("banner_bm",0,"banner_b13","0", []),
  ("banner_bn",0,"banner_b14","0", []),
  ("banner_bo",0,"banner_b15","0", []),
  ("banner_bp",0,"banner_b16","0", []),
  ("banner_bq",0,"banner_b17","0", []),
  ("banner_br",0,"banner_b18","0", []),
  ("banner_bs",0,"banner_b19","0", []),
  ("banner_bt",0,"banner_b20","0", []),
  ("banner_bu",0,"banner_b21","0", []),
  ("banner_ca",0,"banner_c01","0", []),
  ("banner_cb",0,"banner_c02","0", []),
  ("banner_cc",0,"banner_c03","0", []),
  ("banner_cd",0,"banner_c04","0", []),
  ("banner_ce",0,"banner_c05","0", []),
  ("banner_cf",0,"banner_c06","0", []),
  ("banner_cg",0,"banner_c07","0", []),
  ("banner_ch",0,"banner_c08","0", []),
  ("banner_ci",0,"banner_c09","0", []),
  ("banner_cj",0,"banner_c10","0", []),
  ("banner_ck",0,"banner_c11","0", []),
  ("banner_cl",0,"banner_c12","0", []),
  ("banner_cm",0,"banner_c13","0", []),
  ("banner_cn",0,"banner_c14","0", []),
  ("banner_co",0,"banner_c15","0", []),
  ("banner_cp",0,"banner_c16","0", []),
  ("banner_cq",0,"banner_c17","0", []),
  ("banner_cr",0,"banner_c18","0", []),
  ("banner_cs",0,"banner_c19","0", []),
  ("banner_ct",0,"banner_c20","0", []),
  ("banner_cu",0,"banner_c21","0", []),
  # ("banner_da",0,"banner_d01","0", []),
  # ("banner_db",0,"banner_d02","0", []),
  # ("banner_dc",0,"banner_d03","0", []),
  # ("banner_dd",0,"banner_d04","0", []),
  # ("banner_de",0,"banner_d05","0", []),
  # ("banner_df",0,"banner_d06","0", []),
  # ("banner_dg",0,"banner_d07","0", []),
  # ("banner_dh",0,"banner_d08","0", []),
  # ("banner_di",0,"banner_d09","0", []),
  # ("banner_dj",0,"banner_d10","0", []),
  # ("banner_dk",0,"banner_d11","0", []),
  # ("banner_dl",0,"banner_d12","0", []),
  # ("banner_dm",0,"banner_d13","0", []),
  # ("banner_dn",0,"banner_d14","0", []),
  # ("banner_do",0,"banner_d15","0", []),
  # ("banner_dp",0,"banner_d16","0", []),
  # ("banner_dq",0,"banner_d17","0", []),
  # ("banner_dr",0,"banner_d18","0", []),
  # ("banner_ds",0,"banner_d19","0", []),
  # ("banner_dt",0,"banner_d20","0", []),
  # ("banner_du",0,"banner_d21","0", []),
  # ("banner_ea",0,"banner_e01","0", []),
  # ("banner_eb",0,"banner_e02","0", []),
  # ("banner_ec",0,"banner_e03","0", []),
  # ("banner_ed",0,"banner_e04","0", []),
  # ("banner_ee",0,"banner_e05","0", []),
  # ("banner_ef",0,"banner_e06","0", []),
  # ("banner_eg",0,"banner_e07","0", []),
  # ("banner_eh",0,"banner_e08","0", []),
  # ("banner_ei",0,"banner_e09","0", []),
  # ("banner_ej",0,"banner_e10","0", []),
  # ("banner_ek",0,"banner_e11","0", []),
  # ("banner_el",0,"banner_e12","0", []),
  # ("banner_em",0,"banner_e13","0", []),
  # ("banner_en",0,"banner_e14","0", []),
  # ("banner_eo",0,"banner_e15","0", []),
  # ("banner_ep",0,"banner_e16","0", []),
  # ("banner_eq",0,"banner_e17","0", []),
  # ("banner_er",0,"banner_e18","0", []),
  # ("banner_es",0,"banner_e19","0", []),
  # ("banner_et",0,"banner_e20","0", []),
  # ("banner_eu",0,"banner_e21","0", []),

  # ("banner_f01", 0, "banner_f01", "0", []),
  # ("banner_f02", 0, "banner_f02", "0", []),
  # ("banner_f03", 0, "banner_f03", "0", []),
  # ("banner_f04", 0, "banner_f04", "0", []),
  # ("banner_f05", 0, "banner_f05", "0", []),
  # ("banner_f06", 0, "banner_f06", "0", []),
  # ("banner_f07", 0, "banner_f07", "0", []),
  # ("banner_f08", 0, "banner_f08", "0", []),
  # ("banner_f09", 0, "banner_f09", "0", []),
  # ("banner_f10", 0, "banner_f10", "0", []),
  # ("banner_f11", 0, "banner_f11", "0", []),
  # ("banner_f12", 0, "banner_f12", "0", []),
  # ("banner_f13", 0, "banner_f13", "0", []),
  # ("banner_f14", 0, "banner_f14", "0", []),
  # ("banner_f15", 0, "banner_f15", "0", []),
  # ("banner_f16", 0, "banner_f16", "0", []),
  # ("banner_f17", 0, "banner_f17", "0", []),
  # ("banner_f18", 0, "banner_f18", "0", []),
  # ("banner_f19", 0, "banner_f19", "0", []),
  # ("banner_f20", 0, "banner_f20", "0", []),
  # ("banner_f21", 0, "banner_a15", "0", []),

  
  ("tavern_chair_a",0,"tavern_chair_a","bo_tavern_chair_a", []),
  ("tavern_chair_b",0,"tavern_chair_b","bo_tavern_chair_b", []),
  ("tavern_table_a",0,"tavern_table_a","bo_tavern_table_a", []),
  ("tavern_table_b",0,"tavern_table_b","bo_tavern_table_b", []),
  ("fireplace_a",0,"fireplace_a","bo_fireplace_a", []),
  #SW - modified barrel
  #("barrel",0,"barrel","bobarrel", []),
  ("barrel",sokf_moveable|sokf_dynamic,"sw_barrel","bo_sw_barrel", []),
  ("bench_tavern",0,"bench_tavern","bobench_tavern", []),
  ("bench_tavern_b",0,"bench_tavern_b","bo_bench_tavern_b", []),
  ("bowl_wood",0,"bowl_wood","0", []),
  # ("chandelier_table",0,"chandelier_table","0", []),
  # ("chandelier_tavern",0,"chandelier_tavern","0", []),
  # ("chest_gothic",0,"chest_gothic","bochest_gothic", []),
  ("chest_b",0,"chest_b","bo_chest_b", []),
  ("chest_c",0,"chest_c","bo_chest_c", []),
  ("counter_tavern",0,"counter_tavern","bocounter_tavern", []),
  ("cup",0,"cup","0", []),
  ("dish_metal",0,"dish_metal","0", []),
  # ("gothic_chair",0,"gothic_chair","bogothic_chair", []),
  # ("gothic_stool",0,"gothic_stool","bogothic_stool", []),
  ("grate",0,"grate","bograte", []),
  ("jug",0,"jug","0", []),
  ("potlamp",0,"potlamp","0", []),
  # ("weapon_rack",0,"weapon_rack","boweapon_rack", []),
  # ("weapon_rack_big",0,"weapon_rack_big","boweapon_rack_big", []),
  #SW - modified tavern_barrel 
  #("tavern_barrel",0,"barrel","bobarrel", []),  
  ("tavern_barrel",sokf_moveable|sokf_dynamic,"sw_barrel","bo_sw_barrel", []),
  ("tavern_barrel_b",0,"tavern_barrel_b","bo_tavern_barrel_b", []),
  ("merchant_sign",0,"merchant_sign","bo_tavern_sign", []),
  ("tavern_sign",0,"tavern_sign","bo_tavern_sign", []),
  ("sack",0,"sack","0", []),
  #SW - modified skull a-d
  #("skull_a",0,"skull_a","0", []),
  #("skull_b",0,"skull_b","0", []),
  #("skull_c",0,"skull_c","0", []),
  #("skull_d",0,"skull_d","0", []),
  ("skull_a",0,"sw_skull_a","0", []),
  ("skull_b",0,"sw_skull_b","0", []),
  ("skull_c",0,"sw_skull_c","0", []),
  ("skull_d",0,"sw_skull_d","0", []),  
  ("skeleton_cow",0,"skeleton_cow","0", []),
  ("cupboard_a",0,"cupboard_a","bo_cupboard_a", []),
  #SW - switched box_a
  #("box_a",0,"box_a","bo_box_a", []),
  ("box_a",0,"box_a_sw_sp","bo_box_a_sw_sp", []),
  ("bucket_a",0,"bucket_a","bo_bucket_a", []),
  ("straw_a",0,"straw_a","0", []),
  ("straw_b",0,"straw_b","0", []),
  ("straw_c",0,"straw_c","0", []),
  ("cloth_a",0,"cloth_a","0", []),
  ("cloth_b",0,"cloth_b","0", []),
  ("mat_a",0,"mat_a","0", []),
  ("mat_b",0,"mat_b","0", []),
  ("mat_c",0,"mat_c","0", []),
  ("mat_d",0,"mat_d","0", []),

  ("wood_a",0,"wood_a","bo_wood_a", []),
  ("wood_b",0,"wood_b","bo_wood_b", []),
  ("wood_heap",0,"wood_heap_a","bo_wood_heap_a", []),
  ("wood_heap_b",0,"wood_heap_b","bo_wood_heap_b", []),
  #SW - modified water_well
  #("water_well_a",0,"water_well_a","bo_water_well_a", []),
  #("water_well_a",0,"moisture_vaporator","bo_moisture_vaporator", []),
  ("water_well_a",0,"swy_moisturevaporator","bo_swy_moisturevaporator", []),
  ("net_a",0,"net_a","bo_net_a", []),
  ("net_b",0,"net_b","0", []),

  ("meat_hook",0,"meat_hook","0", []),
  ("cooking_pole",0,"cooking_pole","0", []),
  ("bowl_a",0,"bowl_a","0", []),
  ("bucket_b",0,"bucket_b","0", []),
  ("washtub_a",0,"washtub_a","bo_washtub_a", []),
  ("washtub_b",0,"washtub_b","bo_washtub_b", []),

  ("table_trunk_a",0,"table_trunk_a","bo_table_trunk_a", []),
  ("chair_trunk_a",0,"chair_trunk_a","bo_chair_trunk_a", []),
  ("chair_trunk_b",0,"chair_trunk_b","bo_chair_trunk_b", []),
  ("chair_trunk_c",0,"chair_trunk_c","bo_chair_trunk_c", []),

  ("table_trestle_long",0,"table_trestle_long","bo_table_trestle_long", []),
  ("table_trestle_small",0,"table_trestle_small","bo_table_trestle_small", []),
  ("chair_trestle",0,"chair_trestle","bo_chair_trestle", []),

  #SW - modified wheel
  #("wheel",0,"wheel","bowheel", []),
  ("wheel",0,"sw_recruiting_sign_tilted","bo_sw_recruiting_sign_tilted", []),
  ("ladder",0,"ladder","boladder", []),
  ("cart",0,"cart","bocart", []),
  ("village_stand",0,"village_stand","bovillage_stand", []),
  ("wooden_stand",0,"wooden_stand","bowooden_stand", []),
  ("table_small",0,"table_small","botable_small", []),
  ("table_small_b",0,"table_small_b","bo_table_small_b", []),
  ("small_timber_frame_house_a",0,"small_timber_frame_house_a","bo_small_timber_frame_house_a", []),
  ("timber_frame_house_b",0,"0","0", []),     #"tf_house_b","bo_tf_house_b", []),
  ("timber_frame_house_c",0,"0","0", []),     #"tf_house_c","bo_tf_house_c", []),
  ("timber_frame_extension_a",0,"0","0", []),     #"timber_frame_extension_a","bo_timber_frame_extension_a", []),
  ("timber_frame_extension_b",0,"0","0", []),     #"timber_frame_extension_b","bo_timber_frame_extension_b", []),
  ("stone_stairs_a",0,"0","0", []),     #"stone_stairs_a","bo_stone_stairs_a", []),
  ("stone_stairs_b",0,"0","0", []),     #"stone_stairs_b","bo_stone_stairs_b", []),
  ("railing_a",0,"railing_a","bo_railing_a", []),
  ("side_building_a",0,"side_building_a","bo_side_building_a", []),
  ("battlement_a",0,"0","0", []),     #"battlement_a","bo_battlement_a", []),

  ("battlement_a_destroyed",0,"0","0", []),     #"battlement_a_destroyed","bo_battlement_a_destroyed", []),


  ("round_tower_a",0,"0","0", []),     #"round_tower_a","bo_round_tower_a", []),
  ("small_round_tower_a",0,"0","0", []),     #"small_round_tower_a","bo_small_round_tower_a", []),
  ("small_round_tower_roof_a",0,"0","0", []),     #"small_round_tower_roof_a","bo_small_round_tower_roof_a", []),
  ("square_keep_a",0,"0","0", []),     #"square_keep_a","bo_square_keep_a", []),
  ("square_tower_roof_a",0,"0","0", []),     #"square_tower_roof_a","0", []),
  ("gate_house_a",0,"0","0", []),     #"gate_house_a","bo_gate_house_a", []),
  ("gate_house_b",0,"0","0", []),     #"gate_house_b","bo_gate_house_b", []),
  ("small_wall_a",0,"0","0", []),     #"small_wall_a","bo_small_wall_a", []),
  ("small_wall_b",0,"0","0", []),     #"small_wall_b","bo_small_wall_b", []),
  ("small_wall_c",0,"0","0", []),     #"small_wall_c","bo_small_wall_c", []),
  ("small_wall_c_destroy",0,"0","0", []),     #"small_wall_c_destroy","bo_small_wall_c_destroy", []),
  ("small_wall_d",0,"0","0", []),     #"small_wall_d","bo_small_wall_d", []),
  ("small_wall_e",0,"0","0", []),     #"small_wall_e","bo_small_wall_d", []),


  # ("town_house_a",0,"town_house_a","bo_town_house_a", []),
  # ("town_house_b",0,"town_house_b","bo_town_house_b", []),
  # ("town_house_c",0,"town_house_c","bo_town_house_c", []),
  # ("town_house_d",0,"town_house_d","bo_town_house_d", []),
  # ("town_house_e",0,"town_house_e","bo_town_house_e", []),
  # ("town_house_f",0,"town_house_f","bo_town_house_f", []),
  # ("town_house_g",0,"town_house_g","bo_town_house_g", []),
  # ("town_house_h",0,"town_house_h","bo_town_house_h", []),
  # ("town_house_i",0,"town_house_i","bo_town_house_i", []),
  # ("town_house_j",0,"town_house_j","bo_town_house_j", []),
  # ("town_house_l",0,"town_house_l","bo_town_house_l", []),

  # ("town_house_m",0,"town_house_m","bo_town_house_m", []),
  # ("town_house_n",0,"town_house_n","bo_town_house_n", []),
  # ("town_house_o",0,"town_house_o","bo_town_house_o", []),
  # ("town_house_p",0,"town_house_p","bo_town_house_p", []),
  # ("town_house_q",0,"town_house_q","bo_town_house_q", []),
  
  ("passage_house_a",0,"passage_house_a","bo_passage_house_a", []),
  ("passage_house_b",0,"passage_house_b","bo_passage_house_b", []),
  ("passage_house_c",0,"passage_house_c","bo_passage_house_c", []),
  ("passage_house_d",0,"passage_house_d","bo_passage_house_d", []),
  ("passage_house_c_door",0,"passage_house_c_door","bo_passage_house_c_door", []),

  # ("house_extension_a",0,"house_extension_a","bo_house_extension_a", []),
  # ("house_extension_b",0,"house_extension_b","bo_house_extension_b", []),
  # ("house_extension_c",0,"house_extension_c","bo_house_extension_a", []),#reuse 
  # ("house_extension_d",0,"house_extension_d","bo_house_extension_d", []),

  # ("house_extension_e",0,"house_extension_e","bo_house_extension_e", []),
  # ("house_extension_f",0,"house_extension_f","bo_house_extension_f", []),
  # ("house_extension_f2",0,"house_extension_f2","bo_house_extension_f", []),
  # ("house_extension_g",0,"house_extension_g","bo_house_extension_g", []),
  # ("house_extension_g2",0,"house_extension_g2","bo_house_extension_g", []),
  # ("house_extension_h",0,"house_extension_h","bo_house_extension_h", []),

  # ("house_roof_door",0,"house_roof_door","bo_house_roof_door", []),


  ("door_extension_a",0,"door_extension_a","bo_door_extension_a", []),
  ("stairs_arch_a",0,"stairs_arch_a","bo_stairs_arch_a", []),

  # ("town_house_r",0,"town_house_r","bo_town_house_r", []),
  # ("town_house_s",0,"town_house_s","bo_town_house_s", []),
  # ("town_house_t",0,"town_house_t","bo_town_house_t", []),
  # ("town_house_u",0,"town_house_u","bo_town_house_u", []),
  # ("town_house_v",0,"town_house_v","bo_town_house_v", []),
  # ("town_house_w",0,"town_house_w","bo_town_house_w", []),

  # ("town_house_y",0,"town_house_y","bo_town_house_y", []),
  # ("town_house_z",0,"town_house_z","bo_town_house_z", []),
  # ("town_house_za",0,"town_house_za","bo_town_house_za", []),
  
  ("windmill",0,"0","0",[]), 							#"windmill","bo_windmill", []),
  ("windmill_fan_turning",sokf_moveable,"0","0",[]),	#"windmill_fan_turning","bo_windmill_fan_turning", []),
  ("windmill_fan",0,"0","0",[]), 						#"windmill_fan","bo_windmill_fan", []),
  # ("fake_house_a",0,"fake_house_a","bo_fake_house_a", []),
  # ("fake_house_b",0,"fake_house_b","bo_fake_house_b", []),
  # ("fake_house_c",0,"fake_house_c","bo_fake_house_c", []),
  # ("fake_house_d",0,"fake_house_d","bo_fake_house_d", []),
  # ("fake_house_e",0,"fake_house_e","bo_fake_house_e", []),
  # ("fake_house_f",0,"fake_house_f","bo_fake_house_f", []),

  # ("fake_house_snowy_a",0,"fake_house_snowy_a","bo_fake_house_a", []),
  # ("fake_house_snowy_b",0,"fake_house_snowy_b","bo_fake_house_b", []),
  # ("fake_house_snowy_c",0,"fake_house_snowy_c","bo_fake_house_c", []),
  # ("fake_house_snowy_d",0,"fake_house_snowy_d","bo_fake_house_d", []),


  # ("fake_house_far_a",0,"fake_house_far_a","0", []),
  # ("fake_house_far_b",0,"fake_house_far_b","0", []),
  # ("fake_house_far_c",0,"fake_house_far_c","0", []),
  # ("fake_house_far_d",0,"fake_house_far_d","0", []),
  # ("fake_house_far_e",0,"fake_house_far_e","0", []),
  # ("fake_house_far_f",0,"fake_house_far_f","0", []),

  # ("fake_house_far_snowycrude_a",0,"fake_house_far_snowy_a","0", []),
  # ("fake_house_far_snowy_b",0,"fake_house_far_snowy_b","0", []),
  # ("fake_house_far_snowy_c",0,"fake_house_far_snowy_c","0", []),
  # ("fake_house_far_snowy_d",0,"fake_house_far_snowy_d","0", []),

  ("earth_wall_a",0,"earth_wall_a","bo_earth_wall_a", []),
  ("earth_wall_a2",0,"earth_wall_a2","bo_earth_wall_a2", []),
  ("earth_wall_b",0,"earth_wall_b","bo_earth_wall_b", []),
  ("earth_wall_b2",0,"earth_wall_b2","bo_earth_wall_b2", []),
  ("earth_stairs_a",0,"earth_stairs_a","bo_earth_stairs_a", []),
  ("earth_stairs_b",0,"earth_stairs_b","bo_earth_stairs_b", []),
  ("earth_tower_small_a",0,"earth_tower_small_a","bo_earth_tower_small_a", []),
  ("earth_gate_house_a",0,"earth_gate_house_a","bo_earth_gate_house_a", []),
  ("earth_gate_a",0,"earth_gate_a","bo_earth_gate_a", []),
  ("earth_square_keep_a",0,"earth_square_keep_a","bo_earth_square_keep_a", []),
  ("earth_house_a",0,"earth_house_a","bo_earth_house_a", []),
  ("earth_house_b",0,"earth_house_b","bo_earth_house_b", []),
  ("earth_house_c",0,"earth_house_c","bo_earth_house_c", []),
  ("earth_house_d",0,"earth_house_d","bo_earth_house_d", []),

  ("village_steppe_a",0,"village_steppe_a","bo_village_steppe_a", []),
  ("village_steppe_b",0,"village_steppe_b","bo_village_steppe_b", []),
  ("village_steppe_c",0,"village_steppe_c","bo_village_steppe_c", []),
  ("village_steppe_d",0,"village_steppe_d","bo_village_steppe_d", []),
  ("village_steppe_e",0,"village_steppe_e","bo_village_steppe_e", []),
  ("village_steppe_f",0,"village_steppe_f","bo_village_steppe_f", []),
  ("town_house_aa",0,"town_house_aa","bo_town_house_aa", []),
  
  
  # ("snowy_house_a",0,"snowy_house_a","bo_snowy_house_a", []),
  # ("snowy_house_b",0,"snowy_house_b","bo_snowy_house_b", []),
  # ("snowy_house_c",0,"snowy_house_c","bo_snowy_house_c", []),
  # ("snowy_house_d",0,"snowy_house_d","bo_snowy_house_d", []),
  # ("snowy_house_e",0,"snowy_house_e","bo_snowy_house_e", []),
  # ("snowy_house_f",0,"snowy_house_f","bo_snowy_house_f", []),
  # ("snowy_house_g",0,"snowy_house_g","bo_snowy_house_g", []),
  # ("snowy_house_h",0,"snowy_house_h","bo_snowy_house_h", []),
  # ("snowy_house_i",0,"snowy_house_i","bo_snowy_house_i", []),
  # ("snowy_wall_a",0,"snowy_wall_a","bo_snowy_wall_a", []),

  # ("snowy_stand",0,"snowy_stand","bo_snowy_stand", []),

  # ("snowy_heap_a",0,"snowy_heap_a","bo_snowy_heap_a", []),
  # ("snowy_trunks_a",0,"snowy_trunks_a","bo_snowy_trunks_a", []),

  # ("snowy_castle_tower_a",0,"snowy_castle_tower_a","bo_snowy_castle_tower_a", []),
  # ("snowy_castle_battlement_a",0,"snowy_castle_battlement_a","bo_snowy_castle_battlement_a", []),
  # ("snowy_castle_battlement_a_destroyed",0,"snowy_castle_battlement_a_destroyed","bo_snowy_castle_battlement_a_destroyed", []),
 
  # ("snowy_castle_battlement_b",0,"snowy_castle_battlement_b","bo_snowy_castle_battlement_b", []),
  # ("snowy_castle_battlement_corner_a",0,"snowy_castle_battlement_corner_a","bo_snowy_castle_battlement_corner_a", []),
  # ("snowy_castle_battlement_corner_b",0,"snowy_castle_battlement_corner_b","bo_snowy_castle_battlement_corner_b", []),
  # ("snowy_castle_battlement_stairs_a",0,"snowy_castle_battlement_stairs_a","bo_snowy_castle_battlement_stairs_a", []),
  # ("snowy_castle_battlement_stairs_b",0,"snowy_castle_battlement_stairs_b","bo_snowy_castle_battlement_stairs_b", []),
  # ("snowy_castle_gate_house_a",0,"snowy_castle_gate_house_a","bo_snowy_castle_gate_house_a", []),
  # ("snowy_castle_round_tower_a",0,"snowy_castle_round_tower_a","bo_snowy_castle_round_tower_a", []),
  # ("snowy_castle_square_keep_a",0,"snowy_castle_square_keep_a","bo_snowy_castle_square_keep_a", []),
  # ("snowy_castle_stairs_a",0,"snowy_castle_stairs_a","bo_snowy_castle_stairs_a", []),

  ("square_keep_b",0,"0","0", []),     #"square_keep_b","bo_square_keep_b", []),
  ("square_keep_c",0,"0","0", []),     #"square_keep_c","bo_square_keep_c", []),
  ("square_keep_d",0,"0","0", []),     #"square_keep_d","bo_square_keep_d", []),
  ("square_keep_e",0,"0","0", []),     #"square_keep_e","bo_square_keep_e", []),
  ("square_keep_f",0,"0","0", []),     #"square_keep_f","bo_square_keep_f", []),


  ("square_extension_a",0,"0","0", []),     #"square_extension_a","bo_square_extension_a", []),
  ("square_stairs_a",0,"0","0", []),     #"square_stairs_a","bo_square_stairs_a", []),

  ("castle_courtyard_house_a",0,"castle_courtyard_house_a","bo_castle_courtyard_house_a", []),
  ("castle_courtyard_house_b",0,"castle_courtyard_house_b","bo_castle_courtyard_house_b", []),
  ("castle_courtyard_house_c",0,"castle_courtyard_house_c","bo_castle_courtyard_house_c", []),
  ("castle_courtyard_a",0,"castle_courtyard_a","bo_castle_courtyard_a", []),

  ("gatehouse_b",0,"0","0", []),     #"gatehouse_b","bo_gatehouse_b", []),
  ("castle_gaillard",0,"0","0", []),     #"castle_gaillard","bo_castle_gaillard", []),
  
  # ("castle_e_battlement_a",0,"castle_e_battlement_a","bo_castle_e_battlement_a", []),
  # ("castle_e_battlement_a_destroyed",0,"castle_e_battlement_a_destroyed","bo_castle_e_battlement_a_destroyed", []),
  # ("castle_e_corner",0,"castle_e_corner","bo_castle_e_corner", []),
  # ("castle_e_stairs_a",0,"castle_e_stairs_a","bo_castle_e_stairs_a", []),
  # ("castle_e_tower",0,"castle_e_tower","bo_castle_e_tower", []),
  # ("castle_e_gate_house_a",0,"castle_e_gate_house_a","bo_castle_e_gate_house_a", []),
  # ("castle_e_keep_a",0,"castle_e_keep_a","bo_castle_e_keep_a", []),
   ("stand_thatched",0,"stand_thatched","bo_stand_thatched", []),
   ("stand_cloth",0,"stand_cloth","bo_stand_cloth", []),
  # ("castle_e_house_a",0,"castle_e_house_a","bo_castle_e_house_a", []),
  # ("castle_e_house_b",0,"castle_e_house_b","bo_castle_e_house_b", []),
  # ("castle_e_corner_b",0,"castle_e_corner_b","bo_castle_e_corner_b", []),
  

  ("arena_block_a",0,"arena_block_a","bo_arena_block_ab", []),
  ("arena_block_b",0,"arena_block_b","bo_arena_block_ab", []),
  ("arena_block_c",0,"arena_block_c","bo_arena_block_c", []),
  ("arena_block_d",0,"arena_block_d","bo_arena_block_def", []),
  ("arena_block_e",0,"arena_block_e","bo_arena_block_def", []),
  ("arena_block_f",0,"arena_block_f","bo_arena_block_def", []),
  ("arena_block_g",0,"arena_block_g","bo_arena_block_ghi", []),
  ("arena_block_h",0,"arena_block_h","bo_arena_block_ghi", []),
  ("arena_block_i",0,"arena_block_i","bo_arena_block_ghi", []),

  ("arena_block_j",0,"arena_block_j","bo_arena_block_j", []),
  ("arena_block_j_awning",0,"arena_block_j_awning","bo_arena_block_j_awning", []),



  ("arena_palisade_a",0,"arena_palisade_a","bo_arena_palisade_a", []),
  ("arena_wall_a",0,"arena_wall_a","bo_arena_wall_ab", []),
  ("arena_wall_b",0,"arena_wall_b","bo_arena_wall_ab", []),
  ("arena_barrier_a",0,"arena_barrier_a","bo_arena_barrier_a", []),
  ("arena_barrier_b",0,"arena_barrier_b","bo_arena_barrier_bc", []),
  ("arena_barrier_c",0,"arena_barrier_c","bo_arena_barrier_bc", []),
  ("arena_tower_a",0,"arena_tower_a","bo_arena_tower_abc", []),
  ("arena_tower_b",0,"arena_tower_b","bo_arena_tower_abc", []),
  ("arena_tower_c",0,"arena_tower_c","bo_arena_tower_abc", []),
  ("arena_spectator_a",0,"arena_spectator_a","0", []),
  ("arena_spectator_b",0,"arena_spectator_b","0", []),
  ("arena_spectator_c",0,"arena_spectator_c","0", []),
  ("arena_spectator_sitting_a",0,"arena_spectator_sitting_a","0", []),
  ("arena_spectator_sitting_b",0,"arena_spectator_sitting_b","0", []),
  ("arena_spectator_sitting_c",0,"arena_spectator_sitting_c","0", []),


  ("courtyard_gate_a",0,"courtyard_entry_a","bo_courtyard_entry_a", []),
  ("courtyard_gate_b",0,"courtyard_entry_b","bo_courtyard_entry_b", []),
  ("courtyard_gate_c",0,"courtyard_entry_c","bo_courtyard_entry_c", []),
  ("courtyard_gate_snowy",0,"courtyard_entry_snowy","bo_courtyard_entry_a", []),

  ("castle_tower_a",0,"castle_tower_a","bo_castle_tower_a", []),
  #SW - modified
  #("castle_battlement_a",0,"castle_battlement_a","bo_castle_battlement_a", []),
  ("castle_battlement_a",0,"sw_castle_battlement_a","bo_sw_castle_battlement_a", []),  
  #SW - modified
  #("castle_battlement_b",0,"castle_battlement_b","bo_castle_battlement_b", []),
  ("castle_battlement_b",0,"sw_castle_battlement_b","bo_sw_castle_battlement_b", []),

  ("castle_battlement_a_destroyed",0,"castle_battlement_a_destroyed","bo_castle_battlement_a_destroyed", []),
  ("castle_battlement_b_destroyed",0,"castle_battlement_b_destroyed","bo_castle_battlement_b_destroyed", []),

  #SW - modified
  #("castle_battlement_corner_a",0,"castle_battlement_corner_a","bo_castle_battlement_corner_a", []),
  #("castle_battlement_corner_b",0,"castle_battlement_corner_b","bo_castle_battlement_corner_b", []),
  #("castle_battlement_stairs_a",0,"castle_battlement_stairs_a","bo_castle_battlement_stairs_a", []),
  #("castle_battlement_stairs_b",0,"castle_battlement_stairs_b","bo_castle_battlement_stairs_b", []),
  #("castle_gate_house_a",0,"castle_gate_house_a","bo_castle_gate_house_a", []),
  #("castle_square_keep_a",0,"castle_square_keep_a","bo_castle_square_keep_a", []),
  ("castle_battlement_corner_a",0,"sw_castle_battlement_corner_a","bo_sw_castle_battlement_corner_a", []),
  ("castle_battlement_corner_b",0,"sw_castle_battlement_corner_b","bo_sw_castle_battlement_corner_b", []),
  ("castle_battlement_stairs_a",0,"sw_castle_battlement_stairs_a","bo_sw_castle_battlement_stairs_a", []),
  ("castle_battlement_stairs_b",0,"sw_castle_battlement_stairs_b","bo_sw_castle_battlement_stairs_b", []),
  ("castle_gate_house_a",0,"sw_castle_gate_house_a","bo_sw_castle_gate_house_a", []),  
  ("castle_square_keep_a",0,"sw_castle_square_keep_a","bo_sw_castle_square_keep_a", []),
  
  ("castle_round_tower_a",0,"0","0", []),     #"castle_round_tower_a","bo_castle_round_tower_a", []),
  ("castle_stairs_a",0,"0","0", []),     #"castle_stairs_a","bo_castle_stairs_a", []),

  ("castle_drawbridge_open",0,"castle_drawbridges_open","bo_castle_drawbridges_open", []),
  #SW - made the castle drawbridges destructable
  #  ("castle_drawbridge_closed",0,"castle_drawbridges_closed","bo_castle_drawbridges_closed", []),
#  ("castle_drawbridge_closed",sokf_destructible|sokf_moveable|spr_hit_points(100),"castle_drawbridges_closed","bo_castle_drawbridges_closed",   #hit_points don't work, max of 100
  ("castle_drawbridge_closed",sokf_destructible|sokf_moveable,"castle_drawbridges_closed","bo_castle_drawbridges_closed",   #spr_hit_points don't work, max of 100 ?
   [
    (ti_on_scene_prop_destroy,
    [
        (store_trigger_param_1, ":instance_no"),
        (prop_instance_get_position, pos2, ":instance_no"),
        (play_sound, "snd_dummy_destroyed"),
		(particle_system_burst, "psys_explosion_fire", pos1, 100),		#percentage_burst_strength is 100
        #(position_rotate_x, 5),			#use these if you wish to rotate it
        #(position_rotate_y, 5),
        #(position_rotate_z, 5),		
        (position_move_z, pos2, -1200),		#up/down			#move the door out of the way (underground)
		#(position_move_x, pos2, -200),		#left/right
		#(position_move_y, pos2, -200),		#forward/back
        (prop_instance_animate_to_position, ":instance_no", 2, 800), #animate to position in 8 seconds
    ]),
    (ti_on_scene_prop_hit,
    [
        (play_sound, "snd_dummy_hit"),
        (particle_system_burst, "psys_dummy_smoke", pos1, 100),		#percentage_burst_strength is 100
    ]),		
   ],
   300), 	# adding extra number which will be used for hit_points - had to manually updated process_scene_props.py to use for this
   
  ("spike_group_a",0,"spike_group_a","bo_spike_group_a", []),
  ("spike_a",0,"spike_a","bo_spike_a", []),
  ("belfry_a",sokf_moveable,"belfry_a","bo_belfry_a", []),
  ("belfry_old",0,"belfry_a","bo_belfry_a", []),
  ("belfry_platform_a",sokf_moveable,"belfry_platform_a","bo_belfry_platform_a", []),
  ("belfry_platform_b",sokf_moveable,"belfry_platform_b","bo_belfry_platform_b", []),
  ("belfry_platform_old",0,"belfry_platform_b","bo_belfry_platform_b", []),
  ("belfry_wheel",sokf_moveable,"belfry_wheel",0, []),
  ("belfry_wheel_old",0,"belfry_wheel",0, []),

  #SW - switched mangonel to an ATST
  #("mangonel",0,"mangonel","bo_mangonel", []),
  ("mangonel",0,"ATST_scene_prop","bo_ATST_scene_prop", []),
  #SW - switched trebuchet to an ATST
  #("trebuchet_old",0,"trebuchet_old","bo_trebuchet_old", []),
  #("trebuchet_new",0,"trebuchet_new","bo_trebuchet_old", []),
  ("trebuchet_old",0,"ATST_trebuchet","bo_ATST_trebuchet", []),
  ("trebuchet_new",0,"ATST_trebuchet","bo_ATST_trebuchet", []),  
  ("stone_ball",0,"stone_ball","0", []),

  ("village_house_a",0,"village_house_a","bo_village_house_a", []),
  ("village_house_b",0,"village_house_b","bo_village_house_b", []),
  ("village_house_c",0,"village_house_c","bo_village_house_c", []),
  ("village_house_d",0,"village_house_d","bo_village_house_d", []),
  ("farm_house_a",0,"farm_house_a","bo_farm_house_a", []),
  ("farm_house_b",0,"farm_house_b","bo_farm_house_b", []),
  ("farm_house_c",0,"farm_house_c","bo_farm_house_c", []),
  ("mountain_house_a",0,"mountain_house_a","bo_mountain_house_a", []),
  ("mountain_house_b",0,"mountain_house_b","bo_mountain_house_b", []),
  ("village_hut_a",0,"village_hut_a","bo_village_hut_a", []),
  ("crude_fence",0,"fence","bo_fence", []),
  ("crude_fence_small",0,"crude_fence_small","bo_crude_fence_small", []),
  ("crude_fence_small_b",0,"crude_fence_small_b","bo_crude_fence_small_b", []),
  
  ("ramp_12m",0,"ramp_12m","bo_ramp_12m", []),
  ("ramp_14m",0,"ramp_14m","bo_ramp_14m", []),

  ("siege_ladder_12m",0,"siege_leadder_12m","bo_siege_leadder_12m", []),
  ("siege_ladder_14m",0,"siege_leadder_14m","bo_siege_leadder_14m", []),

  # ("portcullis",0,"portcullis_a","bo_portcullis_a", []),
  ("bed_a",0,"bed_a","bo_bed_a", []),
  ("bed_b",0,"bed_b","bo_bed_b", []),
  ("bed_c",0,"bed_c","bo_bed_c", []),
  ("bed_d",0,"bed_d","bo_bed_d", []),
  ("bed_e",0,"bed_e","bo_bed_e", []),

  ("bed_f",0,"bed_f","bo_bed_f", []),

  ("towngate_door_left",0,"0","0",[]), 										#"door_g_left","bo_door_left", []),
  ("towngate_door_right",0,"0","0",[]), 									#"door_g_right","bo_door_right", []),
  ("towngate_rectangle_door_left",0,"0","0",[]), 							#"towngate_rectangle_door_left","bo_towngate_rectangle_door_left", []),
  ("towngate_rectangle_door_right",0,"0","0",[]), 							#"towngate_rectangle_door_right","bo_towngate_rectangle_door_right", []),
  
  ("door_screen",0,"door_screen","0", []),
  ("door_a",0,"door_a","bo_door_a", []),
  ("door_b",0,"door_b","bo_door_a", []),
  ("door_c",0,"door_c","bo_door_a", []),
  ("door_d",0,"door_d","bo_door_a", []),
  ("tavern_door_a",0,"tavern_door_a","bo_tavern_door_a", []),
  ("tavern_door_b",0,"tavern_door_b","bo_tavern_door_a", []),
  ("door_e_left",0,"door_e_left","bo_door_left", []),
  ("door_e_right",0,"door_e_right","bo_door_right", []),
  ("door_f_left",0,"door_f_left","bo_door_left", []),
  ("door_f_right",0,"door_f_right","bo_door_right", []),
  ("door_h_left",0,"door_g_left","bo_door_left", []),
  ("door_h_right",0,"door_g_right","bo_door_right", []),
  ("draw_bridge_a",0,"draw_bridge_a","bo_draw_bridge_a", []),
  ("chain_1m",0,"chain_1m","0", []),
  ("chain_2m",0,"chain_2m","0", []),
  ("chain_5m",0,"chain_5m","0", []),
  ("chain_10m",0,"chain_10m","0", []),
  ("bridge_modular_a",0,"bridge_modular_a","bo_bridge_modular_a", []),
  ("bridge_modular_b",0,"bridge_modular_b","bo_bridge_modular_b", []),
  ("church_a",0,"0","0", []),     #"church_a","bo_church_a", []),
  ("church_tower_a",0,"0","0", []),     #"church_tower_a","bo_church_tower_a", []),
  ("stone_step_a",0,"floor_stone_a","bo_floor_stone_a", []),
  ("stone_step_b",0,"stone_step_b","0", []),
  ("stone_step_c",0,"stone_step_c","0", []),
  ("stone_heap",0,"stone_heap","bo_stone_heap", []),
  ("stone_heap_b",0,"stone_heap_b","bo_stone_heap", []),

  ("panel_door_a",0,"house_door_a","bo_house_door_a", []),
  ("panel_door_b",0,"house_door_b","bo_house_door_a", []),
  #SW - switched the smoke_stain scene prop
  #("smoke_stain",0,"soot_a","0", []),
  ("smoke_stain", 0, "0", "0", []),
  ("brazier_with_fire",0,"brazier","bo_brazier",    [
   (ti_on_scene_prop_init,
    [
        (set_position_delta,0,0,85),
        (particle_system_add_new, "psys_brazier_fire_1"),
        (particle_system_add_new, "psys_fire_sparks_1"),

        (set_position_delta,0,0,100),
        (particle_system_add_new, "psys_fire_glow_1"),
        (particle_system_emit, "psys_fire_glow_1",9000000),
        #(particle_system_add_new, "psys_fire_glow_1"),
        #(set_position_delta,0,0,95),
        #(particle_system_add_new, "psys_cooking_smoke"),
    ]),
   ]),

  ("cooking_fire",0,"fire_floor","0",
   [
   (ti_on_scene_prop_init,
    [
        (set_position_delta,0,0,12),
        (particle_system_add_new, "psys_cooking_fire_1"),
        (particle_system_add_new, "psys_fire_sparks_1"),
        (particle_system_add_new, "psys_cooking_smoke"),
        (set_position_delta,0,0,50),
        (particle_system_add_new, "psys_fire_glow_1"),
        (particle_system_emit, "psys_fire_glow_1",9000000),
    ]),
   ]),
  ("cauldron_a",0,"cauldron_a","bo_cauldron_a", []),
  ("fry_pan_a",0,"fry_pan_a","0", []),
  ("tripod_cauldron_a",0,"tripod_cauldron_a","bo_tripod_cauldron_a", []),
  ("tripod_cauldron_b",0,"tripod_cauldron_b","bo_tripod_cauldron_b", []),
  ("open_stable_a",0,"open_stable_a","bo_open_stable_a", []),
  ("open_stable_b",0,"open_stable_b","bo_open_stable_b", []),
  ("plate_a",0,"plate_a","0", []),
  ("plate_b",0,"plate_b","0", []),
  ("plate_c",0,"plate_c","0", []),
  ("lettuce",0,"lettuce","0", []),
  ("hanger",0,"hanger","0", []),
  ("knife_eating",0,"knife_eating","0", []),
  ("colander",0,"colander","0", []),
  ("ladle",0,"ladle","0", []),
  ("spoon",0,"spoon","0", []),
  ("skewer",0,"skewer","0", []),
  ("grape_a",0,"grape_a","0", []),
  ("grape_b",0,"grape_b","0", []),
  ("apple_a",0,"apple_a","0", []),
  ("apple_b",0,"apple_b","0", []),
  ("maize_a",0,"maize_a","0", []),
  ("maize_b",0,"maize_b","0", []),
  ("cabbage",0,"cabbage","0", []),

  ("cabbage_b",0,"cabbage_b","0", []),
  ("bean",0,"bean","0", []),
  ("basket_a",0,"basket_a","bo_basket_a", []),
  ("feeding_trough_a",0,"feeding_trough_a","bo_feeding_trough_a", []),


  ("marrow_a",0,"marrow_a","0", []),
  ("marrow_b",0,"marrow_b","0", []),
  ("squash_plant",0,"marrow_c","0", []),


  ("cheese_a",0,"cheese_a","0", []),
  ("cheese_b",0,"cheese_b","0", []),
  ("cheese_slice_a",0,"cheese_slice_a","0", []),
  ("bread_a",0,"bread_a","0", []),
  ("bread_b",0,"bread_b","0", []),
  ("bread_slice_a",0,"bread_slice_a","0", []),
  ("fish_a",0,"fish_a","0", []),
  ("fish_roasted_a",0,"fish_roasted_a","0", []),
  ("chicken_roasted",0,"chicken_roasted","0", []),
  ("food_steam",sokf_invisible,"psys_helper","0",
   [
   (ti_on_scene_prop_init,
    [
     (set_position_delta,0,0,0),
     (particle_system_add_new, "psys_food_steam"),
    ]),
   ]),
  ########################
  ("city_smoke",sokf_invisible,"psys_helper","0",
   [
   (ti_on_scene_prop_init,
    [
     (store_time_of_day,reg(12)),
     (neg|is_between,reg(12),5,20),
     (set_position_delta,0,0,0),
     (particle_system_add_new, "psys_night_smoke_1"),
    ]),
   ]),
    ("city_fire_fly_night",sokf_invisible,"psys_helper","0",
   [
   (ti_on_scene_prop_init,
    [
     (store_time_of_day,reg(12)),
     (neg|is_between,reg(12),5,20),
     (set_position_delta,0,0,0),
     (particle_system_add_new, "psys_fire_fly_1"),
    ]),
   ]),
    ("city_fly_day",sokf_invisible,"psys_helper","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_bug_fly_1"),
    ]),
   ]),
    ("flue_smoke_tall",sokf_invisible,"psys_helper","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_flue_smoke_tall"),
    ]),
   ]),
      ("flue_smoke_short",sokf_invisible,"psys_helper","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_flue_smoke_short"),
    ]),
   ]),
      ("moon_beam",sokf_invisible,"psys_helper","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_moon_beam_1"),
     (particle_system_add_new, "psys_moon_beam_paricle_1"),
    ]),
   ]),
    ("fire_small",sokf_invisible,"psys_helper","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_fireplace_fire_small"),
    ]),
   ]),
  ("fire_big",sokf_invisible,"psys_helper","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_fireplace_fire_big"),
    ]),
   ]),
    ("battle_field_smoke",sokf_invisible,"psys_helper","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_war_smoke_tall"),
    ]),
   ]),
    ("Village_fire_big",sokf_invisible,"psys_helper","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_village_fire_big"),
     (set_position_delta,0,0,100),
     (particle_system_add_new, "psys_village_fire_smoke_big"),
    ]),
   ]),
  #########################
  ("candle_a",0,"candle_a","0",
   [
   (ti_on_scene_prop_init,
    [
     (set_position_delta,0,0,27),
     (particle_system_add_new, "psys_candle_light"),
    ]),
   ]),
  ("candle_b",0,"candle_b","0",
   [
   (ti_on_scene_prop_init,
    [
     (set_position_delta,0,0,25),
     (particle_system_add_new, "psys_candle_light"),
    ]),
   ]),
  ("candle_c",0,"candle_c","0",   [
   (ti_on_scene_prop_init,
    [
     (set_position_delta,0,0,10),
     (particle_system_add_new, "psys_candle_light_small"),
    ]),
   ]),
   #SW - modified lamp_a
  ("lamp_a",0,"sw_lamp_a","0",[]),
  #("lamp_a",0,"lamp_a","0",   [     
   # (ti_on_scene_prop_init,
    # [
     # (set_position_delta,66,0,2),
     # (particle_system_add_new, "psys_candle_light"),
    # ]),
   # ]),

   #SW - modified lamp_b
  ("lamp_b",0,"sw_lamp_a","0",[]),
  # ("lamp_b",0,"sw_lamp_a","0",   [
   # (ti_on_scene_prop_init,
    # [
     # (set_position_delta,65,0,-7),
     # (particle_system_add_new, "psys_lamp_fire"),
     # (set_position_delta,70,0,-5),
     # (particle_system_add_new, "psys_fire_glow_1"),
     # (particle_system_emit, "psys_fire_glow_1",9000000),
     # (play_sound, "snd_fire_loop", 0),
    # ]),
   # ]),

  ("hook_a",0,"hook_a","0", []),
  ("window_night",0,"window_night","0", []),
  ("fried_pig",0,"fried_pig","0", []),
  ("village_oven",0,"village_oven","bo_village_oven", []),
  ("dungeon_water_drops",sokf_invisible,"psys_helper","0",
   [
   (ti_on_scene_prop_init,
    [
     (particle_system_add_new, "psys_dungeon_water_drops"),
    ]),
   ]),
  ("shadow_circle_1",0,"shadow_circle_1","0", []),
  ("shadow_circle_2",0,"shadow_circle_2","0", []),
  ("shadow_square_1",0,"shadow_square_1","0", []),
  ("shadow_square_2",0,"shadow_square_2","0", []),
  ("wheelbarrow",0,"wheelbarrow","bo_wheelbarrow", []),
  #SW - modified gourd
  #("gourd",sokf_destructible|spr_hit_points(1),"gourd","bo_gourd",
  ("gourd",sokf_destructible|spr_hit_points(1),"training_remote_prop","bo_training_remote_prop",  
   [
     (ti_on_scene_prop_destroy,
      [
        (store_trigger_param_1, ":instance_no"),
        (val_add, "$g_last_destroyed_gourds", 1),
        (prop_instance_get_position, pos1, ":instance_no"),
        (copy_position, pos2, pos1),
        (position_set_z, pos2, -100000),
        (particle_system_burst, "psys_gourd_smoke", pos1, 2),
        (particle_system_burst, "psys_gourd_piece_1", pos1, 1),
        (particle_system_burst, "psys_gourd_piece_2", pos1, 5),
        (prop_instance_animate_to_position, ":instance_no", pos2, 1),
        (play_sound, "snd_gourd_destroyed"),
        ]),
     ]),

#SW - switched the gourd_spike to be transparent
 #("gourd_spike",0,"gourd_spike","bo_gourd_spike",[]),
 ("gourd_spike",0,"transparent","0",[]),

 ("obstacle_fence_1",0,"fence","bo_fence", []),
 ("obstacle_fallen_tree_a",0,"destroy_tree_a","bo_destroy_tree_a", []),
 ("obstacle_fallen_tree_b",0,"destroy_tree_b","bo_destroy_tree_b", []),

 #SW -new explosion scene prop from Curtain of Fire Magic Mod
   ("explosion",0,0,"asplode", [
	(ti_on_scene_prop_hit,
    [
     (particle_system_burst,"psys_torch_fire",pos1,15),
    ]),]),

#----------------------------------------------------------------------	
#SW BSG Integration
#BSG
#  ("p_viper_mk2",0,"viper_mk2","0", []),
##  ("p_viper_mk7",0,"viper_mk7","0", []),
  ("p_viper_mk7",0,"space_battle_a_wing","0", []),
#  ("p_cylon_raider",0,"cylon_raider","0", []),
#  ("p_raptor",0,"raptor","0", []),
#  ("p_combat_raptor",0,"combat_raptor","0", []),
#  ("p_cylon_heavy_raider",0,"heavy_raider","0", []),
  
##  ("viper_mk2",0,"viper_mk2","0", []),
##  ("viper_mk7",0,"viper_mk7","0", []),
  ("viper_mk2",0,"space_battle_y_wing","0", []),
  ("viper_mk7",0,"space_battle_a_wing","0", []),
#  ("raptor",0,"raptor","0", []),
#  ("combat_raptor",0,"combat_raptor","0", []),
##  ("cylon_raider",0,"cylon_raider","0", []),
  #("cylon_raider",0,"space_battle_merc_ship","0", []),
  ("cylon_raider",0,"space_battle_tie_fighter","0", []),
#  ("cylon_heavy_raider",0,"heavy_raider","0", []),


#  ("galactica",0,"galactica","0", []),
#  ("pegasus",0,"pegasus","0", []),
#  ("basestar",0,"basestar","0", []),
#  ("colonial_one",0,"colonial_one","0", []),
#  ("olympic_carrier",0,"olympic_carrier","0", []),

  ("target1",sokf_invisible,"0","0", []),
  ("target2",sokf_invisible,"0","0", []),
  ("target3",sokf_invisible,"0","0", []),
  ("target4",sokf_invisible,"0","0", []),
  ("target5",sokf_invisible,"0","0", []),
  ("target6",sokf_invisible,"0","0", []),
  ("target7",sokf_invisible,"0","0", []),
  ("target8",sokf_invisible,"0","0", []),
  ("target9",sokf_invisible,"0","0", []),
  ("target_end",sokf_invisible,"0","0", []),

  ("missile",0,"laser_bolt_blue","0", []),
  ("rocket",0,"0","0", []), 
  
##@> Swyter Scene Props - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
   ("swy_city_ground",0,"swy_city_ground","bo_swy_city_ground", []),
   ("swy_city_ground2",0,"swy_city_ground2","bo_swy_city_ground", []),   
   ("swy_city_ground3",0,"swy_city_ground3","bo_swy_city_ground", []),
   ("swy_city_ground_bespin",0,"swy_city_ground_bespin","bo_swy_city_ground", []),
   ("swy_city_ground_bespin2",0,"swy_city_ground_bespin2","bo_swy_city_ground", []),
   ("swy_city_ground_hypori",0,"swy_city_ground_hypori","bo_swy_city_ground", []),
   ("swy_city_ground_hypori2",0,"swy_city_ground_hypori2","bo_swy_city_ground", []),
   ("swy_city_ground_sarapin",0,"swy_city_ground_sarapin","bo_swy_city_ground", []),
   ("swy_city_wall",0,"swy_city_wall","bo_swy_city_wall", []),
   ("swy_city_wall2",0,"swy_city_wall2","bo_swy_city_wall", []),
   ("swy_city_wall3",0,"swy_city_wall3","bo_swy_city_wall", []),
   ("swy_city_wall_bespin",0,"swy_city_wall_bespin","bo_swy_city_wall", []),
   ("swy_city_wall_bespin2",0,"swy_city_wall_bespin2","bo_swy_city_wall", []),
   ("swy_city_wall_bespin3",0,"swy_city_wall_bespin3","bo_swy_city_wall", []),
   ("swy_city_wall_bespin4",0,"swy_city_wall_bespin4","bo_swy_city_wall", []),
   ("swy_city_wall_hypori",0,"swy_city_wall_hypori","bo_swy_city_wall", []),
   ("swy_city_wall_hypori2",0,"swy_city_wall_hypori2","bo_swy_city_wall", []),
   ("swy_city_wall_sarapin",0,"swy_city_wall_sarapin","bo_swy_city_wall", []),
   
	("swy_ground_floor_imperial",0,"swy_ground_floor_imperial","bo_swy_city_ground", []),
    ("swy_city_wall_floor_imperial",0,"swy_city_wall_floor_imperial","bo_swy_city_wall", []),
	("swy_ground_floor_imperial_hangar",0,"swy_ground_floor_imperial_hangar","bo_swy_city_ground", []),
    ("swy_city_wall_floor_imperial_hangar",0,"swy_city_wall_floor_imperial_hangar","bo_swy_city_wall", []),
	("swy_ground_a",0,"swy_ground_floor_rebel","bo_swy_city_ground", []),
    ("swy_city_wall_floor_rebel",0,"swy_city_wall_floor_rebel","bo_swy_city_wall", []),
	("swy_ground_moncal_light",0,"swy_ground_moncal_light","bo_swy_city_ground", []),
    ("swy_city_wall_moncal_light",0,"swy_city_wall_moncal_light","bo_swy_city_wall", []),
    ("swy_city_wall_deathstar",0,"swy_city_wall_deathstar","bo_swy_city_wall", []),
	("swy_ground_deathstar2",0,"swy_ground_deathstar2","bo_swy_city_ground", []),
    ("swy_city_wall_deathstar2",0,"swy_city_wall_deathstar2","bo_swy_city_wall", []),
	("swy_ground_deathstar3",0,"swy_ground_deathstar3","bo_swy_city_ground", []),
    ("swy_city_wall_deathstar3",0,"swy_city_wall_deathstar3","bo_swy_city_wall", []),
   
   ("swy_palm",0,"swy_palm","bo_swy_palm", []),   
   ("swy_saleucami_rock",0,"swy_saleucami_rock","bo_swy_saleucami_rock", []),   
   ("swy_saleucami_rock2",0,"swy_saleucami_rock2","bo_swy_saleucami_rock2", []),   
   #Bespin
   ("swy_bespin_tibanna",0,"swy_bespin_tibanna",0, []),
   #Hoth
   ("swy_hoth_turret",0,"swy_hoth_turret","bo_swy_hoth_turret", []),
   ("swy_hoth_turret_cannon",0,"swy_hoth_turret_cannon","bo_swy_hoth_turret_cannon", []),
   ("swy_hoth_turret_base",0,"swy_hoth_turret_base","bo_swy_hoth_turret_base", []),
   #Death Star
   ("swy_turbolaser_battery",0,"swy_turbolaser_battery","bo_swy_turbolaser_battery", []),
   ("swy_turbolaser_base",0,"swy_turbolaser_base","bo_swy_turbolaser_base", []),   
   #Tatooine
   ("swy_moisturevaporator",0,"swy_moisturevaporator","bo_swy_moisturevaporator", []),  
  #Yavin
   ("swy_rebel_panel",0,"swy_rebel_panel","bo_swy_rebel_panel", []),  
   ("swy_rebel_panel2",0,"swy_rebel_panel2","bo_swy_rebel_panel", []),  
   ("swy_rebel_panel_orange",0,"swy_rebel_panel_orange","bo_swy_rebel_panel", []),  
   ("swy_rebel_panel_purple",0,"swy_rebel_panel_purple","bo_swy_rebel_panel", []),  
  #Dantooine
   ("swy_dant_ventilator",0,"swy_dant_ventilator",0, []),  
   ("swy_dant_base_build",0,"swy_dant_base_build",0, []),  
   ("swy_dant_dish",0,"swy_dant_dish",0, []),  
  #Energy Shields
   ("swy_deflector_shield",0,"swy_deflector_shield","bo_swy_deflector_shield",   #spr_hit_points don't work, max of 100 ?
   [
    (ti_on_scene_prop_hit,
    [
        (play_sound, "snd_deflector_shield_hit"),
        (particle_system_burst, "psys_deflector_shield_hit", pos1, 100),		#percentage_burst_strength is 100
    ]),	
    (ti_on_scene_prop_init,
    [
        (play_sound, "snd_deflector_shield"),
    ]),		
   ]),
   ("swy_deflector_shield_no_col",0,"swy_deflector_shield",0,   #spr_hit_points don't work, max of 100 ?
   [
    (ti_on_scene_prop_init,
    [
        (play_sound, "snd_deflector_shield"),
    ]),		
   ]),
   
   ("swy_deflector_shield_red",0,"swy_deflector_shield_red","bo_swy_deflector_shield",   #spr_hit_points don't work, max of 100 ?
   [
    (ti_on_scene_prop_hit,
    [
        (play_sound, "snd_deflector_shield_hit"),
        (particle_system_burst, "psys_deflector_shield_hit_red", pos1, 100),		#percentage_burst_strength is 100
    ]),	
    (ti_on_scene_prop_init,
    [
        (play_sound, "snd_deflector_shield"),
    ]),		
   ]), 
   ("swy_deflector_shield_red_no_col",0,"swy_deflector_shield_red",0,   #spr_hit_points don't work, max of 100 ?
   [
    (ti_on_scene_prop_init,
    [
        (play_sound, "snd_deflector_shield"),
    ]),	
   ]), 
   
   
    ("swy_gate.sys",0,"ship_door2","bo_ship_door2", []),
	
	#New holographic signs
    ("swy_sign_arena",0,"swy_sign_arena",0, [
	
	(ti_on_init_scene_prop,
      [
          (set_current_color, 170, 30, 30), #red
          (set_position_delta,0,0,0),
          (add_point_light, 30, 200),
      ]),]),
	("swy_sign_cantina",0,"swy_sign_cantina",0, [
	
	(ti_on_init_scene_prop,
      [
          (set_current_color, 170, 122, 30), #orange
          (set_position_delta,0,0,0),
          (add_point_light, 30, 200),
      ]),]),
	("swy_sign_shop",0,"swy_sign_shop",0, [
	
	(ti_on_init_scene_prop,
      [
          (set_current_color, 100, 30, 170), #violet
          (set_position_delta,0,0,0),
          (add_point_light, 30, 200),
      ]),]),
	("swy_sign_extra1",0,"swy_sign_extra1",0, [
	
	(ti_on_init_scene_prop,
      [
          (set_current_color, 141, 207, 30), #green
          (set_position_delta,0,0,0),
          (add_point_light, 30, 200),
      ]),]),
	("swy_sign_extra2",0,"swy_sign_extra2",0, [
	
	(ti_on_init_scene_prop,
      [
          (set_current_color, 117, 22, 142), #pinky
          (set_position_delta,0,0,0),
          (add_point_light, 30, 200),
      ]),]),
	("swy_sign_extra3",0,"swy_sign_extra3",0, [
	
	(ti_on_init_scene_prop,
      [
          (set_current_color, 191, 217, 22), #yellow
          (set_position_delta,0,0,0),
          (add_point_light, 30, 200),
      ]),]),
	
	#Glasses
	("swy_glass",0,"swy_glass",0, []),	
	("swy_glass_curved",0,"swy_glass_curved",0, []),	
	("swy_glass_rectangle",0,"swy_glass_rectangle",0, []),	
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  

##@>  Barf Scene Props
   ("barf_tower",0,"sw_taris_tower","bo_sw_taris_tower", []),
   ("barf_tower2",0,"sw_taris_tower2","bo_sw_taris_tower", []),
   ("barf_rock_1",0,"rock1","bo_rock1", []),
   ("barf_rock_2",0,"rock2","bo_rock2", []),
   ("barf_rock_3",0,"rock3","bo_rock3", []),
   ("barf_rock_4",0,"rock4","bo_rock4", []),
   ("barf_rock_5",0,"rock5","bo_rock5", []),
   ("barf_rock_6",0,"rock6","bo_rock6", []),
   ("barf_rock_7",0,"rock7","bo_rock7", []),
   ("barf_rock_8",0,"rock8","bo_rock8", []),
   ("barf_rock_9",0,"rock9","bo_rock9", []),
   ("barf_rock_10",0,"rock10","bo_rock10", []),
   ("barf_rock_11",0,"rock11","bo_rock11", []),
   ("barf_rock_12",0,"rock12","bo_rock12", []),
   ("barf_rock_13",0,"rock13","bo_rock13", []),
   ("barf_rock_14",0,"rock14","bo_rock14", []),
   ("barf_rock_15",0,"rock15","bo_rock15", []),
   ("barf_rock_16",0,"rock16","bo_rock16", []),
   ("barf_rock_17",0,"rock17","bo_rock17", []),
   ("barf_rock_18",0,"rock18","bo_rock18", []),
   ("barf_rock_19",0,"rock19","bo_rock19", []),
   ("barf_rock_20",0,"rock20","bo_rock20", []),
   ("barf_rock_21",0,"rock21","bo_rock21", []),
   ("barf_rock_22",0,"rock22","bo_rock22", []),
   ("barf_rock_23",0,"rock23","bo_rock23", []),
   ("barf_rock_24",0,"rock24","bo_rock24", []),
   
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
##@>  Yiyang Chen Props

#Ahto [Manaan]
  ("ahto_walls",0,"ahto_walls","bo_ahto_walls", []),
  
#Bespin
  ("bespin_bridge",0,"bespin_bridge","bo_bespin_bridge", []),
  ("bespin_bridge_add",0,"bespin_bridge_add","bo_bespin_bridge_add", []),
  ("bespin_building_1",0,"bespin_building_1","bo_bespin_building_1", []),
  ("bespin_building_2",0,"bespin_building_2","bo_bespin_building_2", []),
  ("bespin_building_3",0,"bespin_building_3","bo_bespin_building_3", []),
  ("bespin_building_4",0,"bespin_building_4","bo_bespin_building_4", []),
  ("bespin_building_5",0,"bespin_building_5","bo_bespin_building_5", []),
  ("bespin_building_6",0,"bespin_building_6","bo_bespin_building_6", []),
  ("bespin_building_7",0,"bespin_building_7","bo_bespin_building_7", []),
  ("bespin_building_8",0,"bespin_building_8","bo_bespin_building_8", []),
  ("bespin_building_9",0,"bespin_building_9","bo_bespin_building_9", []),
  ("bespin_platform_1",0,"bespin_platform_1","bo_bespin_platform_1", []),
  ("bespin_platform_2",0,"bespin_platform_2","bo_bespin_platform_2", []),
  ("bespin_platform_3",0,"bespin_platform_3","bo_bespin_platform_3", []),
  ("bespin_platform_pillar_1",0,"bespin_platform_pillar_1","bo_bespin_platform_pillar_1", []),
  ("bespin_platform_pillar_2",0,"bespin_platform_pillar_2","bo_bespin_platform_pillar_2", []),

#Cato Neimodia
  ("cato_neimodia_bridge_1",0,"cato_neimodia_bridge_1","bo_cato_neimodia_bridge_1", []),
  ("cato_neimodia_bridge_2",0,"cato_neimodia_bridge_2","bo_cato_neimodia_bridge_2", []),
  ("cato_neimodia_building_1",0,"cato_neimodia_building_1","bo_cato_neimodia_building_1", []),
  
#Corellia
  ("corellia_building_1",0,"corellia_building_1",0, []),
  ("corellia_building_2",0,"corellia_building_2",0, []),
  ("corellia_building_3",0,"corellia_building_3",0, []),
  ("corellia_building_4",0,"corellia_building_4",0, []),
  ("corellia_road_curve",0,"corellia_road_curve","bo_corellia_road_curve", []),
  ("corellia_road_straight",0,"corellia_road_straight","bo_corellia_road_straight", []),


#Coruscant   
  ("coruscant1",0,"coruscant1",0, []),
  ("coruscant2",0,"coruscant2",0, []),
  ("coruscant3",0,"coruscant3",0, []),
  ("coruscant4",0,"coruscant4",0, []),
  ("coruscant5",0,"coruscant5",0, []),
  ("coruscant6",0,"coruscant6",0, []),
  ("coruscant7",0,"coruscant7",0, []),
  ("coruscant8",0,"coruscant8",0, []),
  ("coruscant9",0,"coruscant9",0, []),
  ("coruscant10",0,"coruscant10",0, []),
  ("coruscant11",0,"coruscant11",0, []),
  ("coruscant12",0,"coruscant12",0, []),

  ("christophsis_buiding_1",0,"christophsis_buiding_1",0, []),
  ("christophsis_buiding_2",0,"christophsis_buiding_2",0, []),
  ("christophisis_bridge_cross",0,"christophisis_bridge_cross","bo_christophisis_bridge_cross", []),
  ("christophisis_bridge_end",0,"christophisis_bridge_end","bo_christophisis_bridge_end", []),
  ("christophisis_bridge_straight",0,"christophisis_bridge_straight","bo_christophisis_bridge_straight", []),
  ("christophisis_bridge_small",0,"christophisis_bridge_small","bo_christophisis_bridge_small", []),
  ("christophisis_bridge_small_pier",0,"christophisis_bridge_small_pier","bo_christophisis_bridge_small_pier", []),
  ("christophisis_stairs",0,"christophisis_stairs","bo_christophisis_stairs", []),

  ("christophisis_hex",0,"christophisis_hex",0, []),

  
#Felucia
  ("felucia_flower_1",0,"felucia_flower_1",0, []),
  ("felucia_flower_2",0,"felucia_flower_2",0, []),
  ("felucia_flower_3",0,"felucia_flower_3","bo_felucia_flower_3_4", []),
  ("felucia_flower_4",0,"felucia_flower_4","bo_felucia_flower_3_4", []),
  ("felucia_flower_5",0,"felucia_flower_5",0, []),
  ("felucia_flower_6",0,"felucia_flower_6",0, []),
  ("felucia_flower_7",0,"felucia_flower_7",0, []),
  ("felucia_fungus_1",0,"felucia_fungus_1","bo_felucia_fungus_1", []),
  ("felucia_fungus_2",0,"felucia_fungus_2","bo_felucia_fungus_2", []),
  ("felucia_fungus_3",0,"felucia_fungus_3","bo_felucia_fungus_3", []),
  ("felucia_fungus_4",0,"felucia_fungus_4","bo_felucia_fungus_4", []),
  ("felucia_fungus_5",0,"felucia_fungus_5","bo_felucia_fungus_5", []),
  ("felucia_fungus_6",0,"felucia_fungus_6","bo_felucia_fungus_6", []),
  
#Naboo
  ("Naboo_house_1",0,"naboo_house_1","bo_naboo_house_1", []),
  ("Naboo_house_3",0,"naboo_house_3","bo_naboo_house_3", []),
  ("Naboo_house_4",0,"naboo_house_4",0, []),
  ("naboo_house_5",0,"naboo_house_5","bo_naboo_house_5", []),

  ("Naboo_theedpalace_1",0,"naboo_theedpalace_1",0, []),
  ("Naboo_theedpalace_2",0,"naboo_theedpalace_2",0, []),
  ("Naboo_theedpalace_3",0,"naboo_theedpalace_3",0, []),
  ("Naboo_theedpalace_4",0,"naboo_theedpalace_4",0, []),
  ("Naboo_theedpalace_5",0,"naboo_theedpalace_5",0, []),
  ("Naboo_theedpalace_6",0,"naboo_theedpalace_6",0, []),
  ("Naboo_theedpalace_7",0,"naboo_theedpalace_7",0, []),
  ("Naboo_theedpalace_8",0,"naboo_theedpalace_8",0, []),
  ("Naboo_theedpalace_9",0,"naboo_theedpalace_9",0, []),

  ("Naboo_theedpalace_10",0,"naboo_theedpalace_10",0, []),
  ("Naboo_theedpalace_11",0,"naboo_theedpalace_11",0, []),
  ("Naboo_theedpalace_12",0,"naboo_theedpalace_12",0, []),
  ("Naboo_theedpalace_13",0,"naboo_theedpalace_13",0, []),
  ("Naboo_theedpalace_14",0,"naboo_theedpalace_14",0, []),
  ("Naboo_theedpalace_15",0,"naboo_theedpalace_15",0, []),
  ("Naboo_theedpalace_16",0,"naboo_theedpalace_16",0, []),
  ("Naboo_theedpalace_17",0,"naboo_theedpalace_17",0, []),
  ("Naboo_theedpalace_18",0,"naboo_theedpalace_18",0, []),
  ("Naboo_theedpalace_19",0,"naboo_theedpalace_19",0, []),
  ("Naboo_theedpalace_20",0,"naboo_theedpalace_20",0, []),
  ("Naboo_theedpalace_21",0,"naboo_theedpalace_21",0, []),

  ("Naboo_theedpalace_bridge",0,"naboo_theedpalace_bridge",0, []),
  ("Naboo_column",0,"naboo_column",0, []),
  ("naboo_arch_1",0,"naboo_arch_1",0, []),
  ("naboo_arch_2",0,"naboo_arch_2",0, []),

  ("Naboo_cantina",0,"naboo_cantina","bo_naboo_cantina", []),
  
#Mos Eisley
  ("moseisley_angle",0,"moseisley_angle","bo_moseisley_angle", []),
  ("moseisley_chair",0,"moseisley_chair","bo_moseisley_chair", []),
  ("moseisley_machine",0,"moseisley_machine","bo_moseisley_machine", []),
  ("moseisley_table",0,"moseisley_table","bo_moseisley_table", []),
  ("moseisley_bar",0,"moseisley_bar","bo_moseisley_bar", []),
  ("moseisley_bank",0,"moseisley_bank","bo_moseisley_bank", []),
  ("moseisleybottles",0,"moseisleybottles","bo_moseisleybottles", []),

  ("moseisley_building_1",0,"moseisley_building_1",0, []),
  ("moseisley_building_2",0,"moseisley_building_2",0, []),
  
#Saleucami
  ("saleucami_plant_1",0,"saleucami_plant_1","bo_saleucami_plant_1_2", []),
  ("saleucami_plant_2",0,"saleucami_plant_2","bo_saleucami_plant_1_2", []),
  ("saleucami_plant_3",0,"saleucami_plant_3","bo_saleucami_plant_3_4_5_6", []),
  ("saleucami_plant_4",0,"saleucami_plant_4","bo_saleucami_plant_3_4_5_6", []),

#Taris
  ("taris_building_a_1_hw",0,"taris_building_a_1_hw",0, []),
  ("taris_building_a_2_hw",0,"taris_building_a_2_hw",0, []),
  ("taris_building_a_3_hw",0,"taris_building_a_3_hw",0, []),
  ("taris_building_a_1_aw",0,"taris_building_a_1_aw",0, []),
  ("taris_building_a_2_aw",0,"taris_building_a_2_aw",0, []),
  ("taris_building_a_3_aw",0,"taris_building_a_3_aw",0, []),
  ("taris_building_a_1_nw",0,"taris_building_a_1_nw",0, []),
  ("taris_building_a_2_nw",0,"taris_building_a_2_nw",0, []),
  ("taris_building_a_3_nw",0,"taris_building_a_3_nw",0, []),
  ("taris_building_b_1_hw",0,"taris_building_b_1_hw",0, []),
  ("taris_building_b_2_hw",0,"taris_building_b_2_hw",0, []),
  ("taris_building_b_3_hw",0,"taris_building_b_3_hw",0, []),
  ("taris_building_b_1_aw",0,"taris_building_b_1_aw",0, []),
  ("taris_building_b_2_aw",0,"taris_building_b_2_aw",0, []),
  ("taris_building_b_3_aw",0,"taris_building_b_3_aw",0, []),
  ("taris_building_b_1_nw",0,"taris_building_b_1_nw",0, []),
  ("taris_building_b_2_nw",0,"taris_building_b_2_nw",0, []),
  ("taris_building_b_3_nw",0,"taris_building_b_3_nw",0, []),
  ("taris_building_2_bridge",0,"taris_building_2_bridge",0, []),
  ("taris_platform",0,"taris_platform",0, []),

  ("taris_cantina_door",0,"taris_cantina_door",0, []),
  ("taris_cantina_lift",0,"taris_cantina_lift",0, []),
  ("taris_cantina_table",0,"taris_cantina_table",0, []),
  
#Jabba Palace	
  ("jabba_palace_building_1",0,"jabba_palace_building_1",0, []),
  ("jabba_palace_building_2",0,"jabba_palace_building_2",0, []),
  ("jabba_palace_building_3",0,"jabba_palace_building_3",0, []),
  ("jabba_palace_building_4",0,"jabba_palace_building_4",0, []),
  ("jabba_palace_building_5",0,"jabba_palace_building_5",0, []),
  ("jabba_palace_building_6",0,"jabba_palace_building_6",0, []),

#Jabba Palace Rough reskins by RevanShan / had to retouch the normals
  ("trandoshan_building_1",0,"trandoshan_building_1",0, []),
  ("trandoshan_building_2",0,"trandoshan_building_2",0, []),
  ("trandoshan_building_3",0,"trandoshan_building_3",0, []),
  ("trandoshan_building_4",0,"trandoshan_building_4",0, []),
  ("trandoshan_building_5",0,"trandoshan_building_5",0, []),
  ("trandoshan_building_6",0,"trandoshan_building_6",0, []),

#Kashyyyk
  ("kashyyyk_house",0,"kashyyyk_house",0, []),
  ("kashyyyk_house_platform_bridge",0,"kashyyyk_house_platform_bridge",0, []),
  ("kashyyyk_house_platform_down",0,"kashyyyk_house_platform_down",0, []),
  ("kashyyyk_platform_a",0,"kashyyyk_platform_a",0, []),
  ("kashyyyk_platform_eighth_fence_addon",0,"kashyyyk_platform_eighth_fence_addon",0, []),
  ("kashyyyk_platform_eighth_fence_houseup_addon",0,"kashyyyk_platform_eighth_fence_houseup_addon",0, []),
  ("kashyyyk_platform_eighth_platform",0,"kashyyyk_platform_eighth_platform",0, []),
  ("kashyyyk_platform_house_a",0,"kashyyyk_platform_house_a",0, []),
  ("kashyyyk_platform_house_b",0,"kashyyyk_platform_house_b",0, []),
  ("kashyyyk_platform_house_bridge",0,"kashyyyk_platform_house_bridge",0, []),
  ("kashyyyk_platform_offtree_a",0,"kashyyyk_platform_offtree_a",0, []),
  ("kashyyyk_platform_sixteenth_fence",0,"kashyyyk_platform_sixteenth_fence",0, []),
  ("kashyyyk_platform_sixteenth_fence_bridge",0,"kashyyyk_platform_sixteenth_fence_bridge",0, []),
  ("kashyyyk_platform_sixteenth_platform",0,"kashyyyk_platform_sixteenth_platform",0, []),
  ("kashyyyk_platform_stringer",0,"kashyyyk_platform_stringer",0, []),
  ("kashyyyk_platform_stringer_bridge",0,"kashyyyk_platform_stringer_bridge",0, []),
  ("kashyyyk_stairs",0,"kashyyyk_stairs",0, []),
  ("kashyyyk_tree1",0,"kashyyyk_tree1",0, []),
  ("kashyyyk_tree2",0,"kashyyyk_tree2",0, []),
  ("kashyyyyk_cliff_1",0,"kashyyyyk_cliff_1",0, []),
  ("kashyyyyk_cliff_2",0,"kashyyyyk_cliff_2",0, []),
  
#Spaceviews
  ("spaceview_coruscant",0,"spaceview_coruscant",0, []),
  ("spaceview_dagobah",0,"spaceview_dagobah",0, []),
  ("spaceview_endor",0,"spaceview_endor",0, []),
  ("spaceview_geonosis",0,"spaceview_geonosis",0, []),
  ("spaceview_naboo",0,"spaceview_naboo",0, []),
  ("spaceview_taris",0,"spaceview_taris",0, []),
  ("spaceview_tatoonie",0,"spaceview_tatoonie",0, []),
  ("spaceview_yavin_iv",0,"spaceview_yavin_iv",0, []),

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
##@> Rough + Amateur Reskins from... guess who?  :P
  ("revnshn_rhenvar_addon",0,"rhenvar_addon","bo_yavinaddon", []),
  ("revnshn_rhenvar_pillar1",0,"rhenvar_pillar1","bo_yavinpillar1", []),
  ("revnshn_rhenvar_pillar2",0,"rhenvar_pillar2","bo_yavinpillar2", []),
  ("revnshn_rhenvar_spire",0,"rhenvar_spire","bo_yavinspire", []),
  ("revnshn_rhenvar_statue1",0,"rhenvar_statue1","bo_yavinstatue1", []),
  ("revnshn_rhenvar_statue2",0,"rhenvar_statue2","bo_yavinstatue2", []),
  ("revnshn_rhenvar_statue3",0,"rhenvar_statue3","bo_yavinstatue3", []),
  ("revnshn_rhenvar_steps",0,"rhenvar_steps","bo_yavinsteps", []),
  ("revnshn_rhenvar_table1",0,"rhenvar_table1","bo_yavintable1", []),
  ("revnshn_rhenvar_temple",0,"rhenvar_templeblend","bo_yavintempleblend", []),
  ("revnshn_rhenvar_wall1",0,"rhenvar_wall1","bo_yavinwall1", []),
  ("revnshn_rhenvar_wall2",0,"rhenvar_wall2","bo_yavinwall2", []),
  ("revnshn_rhenvar_wall3",0,"rhenvar_wall3","bo_yavinwall3", []),
  
  ("revnshn_ziost_addon",0,"ziost_addon","bo_yavinaddon", []),
  ("revnshn_ziost_pillar1",0,"ziost_pillar1","bo_yavinpillar1", []),
  ("revnshn_ziost_pillar2",0,"ziost_pillar2","bo_yavinpillar2", []),
  ("revnshn_ziost_spire",0,"ziost_spire","bo_yavinspire", []),
  ("revnshn_ziost_statue1",0,"ziost_statue1","bo_yavinstatue1", []),
  ("revnshn_ziost_statue2",0,"ziost_statue2","bo_yavinstatue2", []),
  ("revnshn_ziost_statue3",0,"ziost_statue3","bo_yavinstatue3", []),
  ("revnshn_ziost_steps",0,"ziost_steps","bo_yavinsteps", []),
  ("revnshn_ziost_table1",0,"ziost_table1","bo_yavintable1", []),
  ("revnshn_ziost_temple",0,"ziost_templeblend","bo_yavintempleblend", []),
  ("revnshn_ziost_wall1",0,"ziost_wall1","bo_yavinwall1", []),
  ("revnshn_ziost_wall2",0,"ziost_wall2","bo_yavinwall2", []),
  ("revnshn_ziost_wall3",0,"ziost_wall3","bo_yavinwall3", []),
  
  
  ("revnshn_dantooine_addon",0,"dantooine_addon","bo_yavinaddon", []),
  ("revnshn_dantooine_pillar1",0,"dantooine_pillar1","bo_yavinpillar1", []),
  ("revnshn_dantooine_pillar2",0,"dantooine_pillar2","bo_yavinpillar2", []),
  ("revnshn_dantooine_spire",0,"dantooine_spire","bo_yavinspire", []),
  ("revnshn_dantooine_statue1",0,"dantooine_statue1","bo_yavinstatue1", []),
  ("revnshn_dantooine_statue2",0,"dantooine_statue2","bo_yavinstatue2", []),
  ("revnshn_dantooine_statue3",0,"dantooine_statue3","bo_yavinstatue3", []),
  ("revnshn_dantooine_steps",0,"dantooine_steps","bo_yavinsteps", []),
  ("revnshn_dantooine_table1",0,"dantooine_table1","bo_yavintable1", []),
  ("revnshn_dantooine_temple",0,"dantooine_templeblend","bo_yavintempleblend", []),
  ("revnshn_dantooine_wall1",0,"dantooine_wall1","bo_yavinwall1", []),
  ("revnshn_dantooine_wall2",0,"dantooine_wall2","bo_yavinwall2", []),
  ("revnshn_dantooine_wall3",0,"dantooine_wall3","bo_yavinwall3", []),
  
  ("revnshn_korriban_1_addon",0,"korriban_1_addon","bo_yavinaddon", []),
  ("revnshn_korriban_1_pillar1",0,"korriban_1_pillar1","bo_yavinpillar1", []),
  ("revnshn_korriban_1_pillar2",0,"korriban_1_pillar2","bo_yavinpillar2", []),
  ("revnshn_korriban_1_spire",0,"korriban_1_spire","bo_yavinspire", []),
  ("revnshn_korriban_1_statue1",0,"korriban_1_statue1","bo_yavinstatue1", []),
  ("revnshn_korriban_1_statue2",0,"korriban_1_statue2","bo_yavinstatue2", []),
  ("revnshn_korriban_1_statue3",0,"korriban_1_statue3","bo_yavinstatue3", []),
  ("revnshn_korriban_1_steps",0,"korriban_1_steps","bo_yavinsteps", []),
  ("revnshn_korriban_1_table1",0,"korriban_1_table1","bo_yavintable1", []),
  ("revnshn_korriban_1_temple",0,"korriban_1_templeblend","bo_yavintempleblend", []),
  ("revnshn_korriban_1_wall1",0,"korriban_1_wall1","bo_yavinwall1", []),
  ("revnshn_korriban_1_wall2",0,"korriban_1_wall2","bo_yavinwall2", []),
  ("revnshn_korriban_1_wall3",0,"korriban_1_wall3","bo_yavinwall3", []),
  
  ("revnshn_korriban_2_addon",0,"korriban_2_addon","bo_yavinaddon", []),
  ("revnshn_korriban_2_pillar1",0,"korriban_2_pillar1","bo_yavinpillar1", []),
  ("revnshn_korriban_2_pillar2",0,"korriban_2_pillar2","bo_yavinpillar2", []),
  ("revnshn_korriban_2_spire",0,"korriban_2_spire","bo_yavinspire", []),
  ("revnshn_korriban_2_statue1",0,"korriban_2_statue1","bo_yavinstatue1", []),
  ("revnshn_korriban_2_statue2",0,"korriban_2_statue2","bo_yavinstatue2", []),
  ("revnshn_korriban_2_statue3",0,"korriban_2_statue3","bo_yavinstatue3", []),
  ("revnshn_korriban_2_steps",0,"korriban_2_steps","bo_yavinsteps", []),
  ("revnshn_korriban_2_table1",0,"korriban_2_table1","bo_yavintable1", []),
  ("revnshn_korriban_2_temple",0,"korriban_2_templeblend","bo_yavintempleblend", []),
  ("revnshn_korriban_2_wall1",0,"korriban_2_wall1","bo_yavinwall1", []),
  ("revnshn_korriban_2_wall2",0,"korriban_2_wall2","bo_yavinwall2", []),
  ("revnshn_korriban_2_wall3",0,"korriban_2_wall3","bo_yavinwall3", []),

  ("revnshn_sarapin_addon",0,"sarapin_addon","bo_yavinaddon", []),
  ("revnshn_sarapin_pillar1",0,"sarapin_pillar1","bo_yavinpillar1", []),
  ("revnshn_sarapin_pillar2",0,"sarapin_pillar2","bo_yavinpillar2", []),
  ("revnshn_sarapin_spire",0,"sarapin_spire","bo_yavinspire", []),
  ("revnshn_sarapin_statue1",0,"sarapin_statue1","bo_yavinstatue1", []),
  ("revnshn_sarapin_statue2",0,"sarapin_statue2","bo_yavinstatue2", []),
  ("revnshn_sarapin_statue3",0,"sarapin_statue3","bo_yavinstatue3", []),
  ("revnshn_sarapin_steps",0,"sarapin_steps","bo_yavinsteps", []),
  ("revnshn_sarapin_table1",0,"sarapin_table1","bo_yavintable1", []),
  ("revnshn_sarapin_temple",0,"sarapin_templeblend","bo_yavintempleblend", []),
  ("revnshn_sarapin_wall1",0,"sarapin_wall1","bo_yavinwall1", []),
  ("revnshn_sarapin_wall2",0,"sarapin_wall2","bo_yavinwall2", []),
  ("revnshn_sarapin_wall3",0,"sarapin_wall3","bo_yavinwall3", []),
  
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
##@> Skyboxes as scene props
  ("skybox_cloud_1",0,"skybox_cloud_1_prop","0", []),
  ("skybox_cloud_2",0,"skybox_cloud_2_prop","0", []),
  ("skybox_night_1",0,"skybox_night_1_prop","0", []),   
  ("skybox_sunset_1",0,"skybox_sunset_1_prop","0", []),
  ("skybox_space",0,"compass_prop","0", []),	
  ("skybox_vjun",0,"skybox_vjun","0", []),   
  ("skybox_kamino",0,"skybox_kamino","0", []),  
  ("skybox_volcanic",0,"skybox_volcanic","0", []),  
  #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## Some animated traffic stuff

   ("swc_traffic",0,"swc_traffic",0,
   [   (ti_on_scene_prop_init,[ 
###############

        (store_trigger_param_1, ":instance_no"),
        (prop_instance_get_position, pos1, ":instance_no"),
        (play_sound, "snd_dummy_destroyed"),
		(particle_system_burst, "psys_explosion_fire", pos1, 100),		#percentage_burst_strength is 100
        #(position_rotate_x, 5),			#use these if you wish to rotate it
        #(position_rotate_y, 5),
        #(position_rotate_z, 5),		
        #(position_move_z, pos2, -1200),	#up/down
		#(position_move_x, pos2, -200),		#left/right
		(position_move_y, pos1, 2000),		#forward/back
        (prop_instance_animate_to_position, ":instance_no", 1, 1000), #animate to position in10 seconds


###############
   ]),	]), 

#@Automagically added -- Start
#--spropbot.2011-07-06>>17:00:06
  ("cato_neimodia_door",0,"cato_neimodia_door","0", []),
  ("cato_neimodia_building_arch_1",0,"cato_neimodia_building_arch_1","0", []),
  ("cato_neimodia_building_arch_2",0,"cato_neimodia_building_arch_2","0", []),
  ("cato_neimodia_mountain_arch_1",0,"cato_neimodia_mountain_arch_1","0", []),
  ("cato_neimodia_building_arch_main",0,"cato_neimodia_building_arch_main","0", []),
  ("cato_neimodia_mountain_cliff",0,"cato_neimodia_mountain_cliff","0", []),
  ("cato_neimodia_platform_1",0,"cato_neimodia_platform_1","bo_cato_neimodia_platform_1", []),
  ("cato_neimodia_bridge_stump",0,"cato_neimodia_bridge_stump","bo_cato_neimodia_bridge_stump", []),
  ("cato_neimodia_door",0,"cato_neimodia_door","bo_cato_neimodia_door", []),
  ("deathstar_parts_1_doorframe",0,"deathstar_parts_1_doorframe","bo_deathstar_parts_1_doorframe", []),
  ("deathstar_parts_1_door",0,"deathstar_parts_1_door","bo_deathstar_parts_1_door", []),
  ("deathstar_parts_2_door",0,"deathstar_parts_2_door","bo_deathstar_parts_2_door", []),
  ("deathstar_parts_2_corridor",0,"deathstar_parts_2_corridor","bo_deathstar_parts_2_corridor", []),
  ("virtual_twilek_dancer_hologram",0,"virtual_twilek_dancer_hologram","bo_virtual_twilek_dancer_hologram", []),
  ("taris_statue_base_1",0,"taris_statue_base_1","bo_taris_statue_base_1", []),
  ("taris_statue_base_2",0,"taris_statue_base_2","bo_taris_statue_base_2", []),
  ("taris_statue_1",sokf_moveable|spanim_loop_linear,"taris_statue_1","bo_taris_statue_1",
[ (ti_on_scene_prop_init,[ 
		 (store_trigger_param_1, ":instance"),
		 (call_script,"script_swy_sprop_movement",":instance",y,30,10), #  <-- mov type (x,y,z), mov value, mov time
   ]),
]),
  
  ("Container_1",0,"Container_1","bo_Container_1_2_3_4", []),
  ("Container_2",0,"Container_2","bo_Container_1_2_3_4", []),
  ("Container_3",0,"Container_3","bo_Container_1_2_3_4", []),
  ("Container_4",0,"Container_4","bo_Container_1_2_3_4", []),
  ("Container_5",0,"Container_5","bo_Container_5_6_7", []),
  ("Container_6",0,"Container_6","bo_Container_5_6_7", []),
  ("Container_7",0,"Container_7","bo_Container_5_6_7", []),
  ("Container_8",0,"Container_8","bo_Container_8_9_10", []),
  ("Container_9",0,"Container_9","bo_Container_8_9_10", []),
  ("Container_10",0,"Container_10","bo_Container_8_9_10", []),

#--spropbot.2011-07-07>>16:04:53
  ("Naboo_house_2",0,"naboo_house_2","bo_naboo_house_2", []),
  ("Naboo_house_7",0,"naboo_house_7","bo_naboo_house_7", []),
  ("Naboo_house_8",0,"naboo_house_8","bo_naboo_house_7", []),
  ("Naboo_theedpalace_entrance",0,"naboo_theedpalace_entrance","bo_naboo_theedpalace_entrance", []),
  ("naboo_fence",0,"naboo_fence","0", []),
  ("naboo_statue_guard_female",0,"naboo_statue_guard_female","bo_naboo_statue_guard", []),
  ("naboo_statue_guard_male",0,"naboo_statue_guard_male","bo_naboo_statue_guard", []),

#--spropbot.2011-07-09>>15:07:50
  ("deathstar_parts_3_corridor",0,"deathstar_parts_3_corridor","bo_deathstar_parts_3_corridor", []),
  ("deathstar_parts_4_wall",0,"deathstar_parts_4_wall","bo_deathstar_parts_4_wall", []),

#--spropbot.2011-07-10>>17:42:53
  ("deathstar_parts_5_stairs",0,"deathstar_parts_5_stairs","bo_deathstar_parts_5_stairs", []),
  ("deathstar_parts_5_corridor_curve_1",0,"deathstar_parts_5_corridor_curve_1","bo_deathstar_parts_5_corridor_curve", []),
  ("deathstar_parts_5_corridor_curve_2",0,"deathstar_parts_5_corridor_curve_2","bo_deathstar_parts_5_corridor_curve", []),
  ("deathstar_parts_5_column_1",0,"deathstar_parts_5_column_1","bo_deathstar_parts_5_column", []),
  ("deathstar_parts_5_column_2",0,"deathstar_parts_5_column_2","bo_deathstar_parts_5_column", []),
  ("deathstar_parts_5_corridor_1",0,"deathstar_parts_5_corridor_1","bo_deathstar_parts_5_corridor", []),
  ("deathstar_parts_5_corridor_2",0,"deathstar_parts_5_corridor_2","bo_deathstar_parts_5_corridor", []),


("saleucami_plant_5",0,"saleucami_plant_5","bo_saleucami_plant_3_4_5_6", []),
("saleucami_plant_6",0,"saleucami_plant_6","bo_saleucami_plant_3_4_5_6", []),

("saleucami_plant_7",0,"saleucami_plant_7","bo_saleucami_plant_7_8", []),
("saleucami_plant_8",0,"saleucami_plant_8","bo_saleucami_plant_7_8", []),

#--spropbot.2011-07-16>>19:55:17
  ("naboo_theed_interior_column_1",0,"naboo_theed_interior_column_1","bo_naboo_theed_interior_column_1", []),
  ("naboo_theed_interior_window",0,"naboo_theed_interior_window","0", []),
  ("naboo_theed_interior_room_1",0,"naboo_theed_interior_room_1","bo_naboo_theed_interior_room_1", []),
  ("deathstar_hanging_bridge_1",0,"deathstar_hanging_bridge_1","bo_deathstar_hanging_bridge_1", []),
  ("deathstar_hanging_bridge_2",0,"deathstar_hanging_bridge_2","bo_deathstar_hanging_bridge_2", []),
  ("deathstar_hanger_part_1",0,"deathstar_hanger_part_1","bo_deathstar_hanger_part_1", []),
  ("Container_closed",0,"Container_closed","bo_Container_closed", []),
  ("Container_spice_1",0,"Container_spice_1","bo_Container_spice_1_2_3", []),
  ("Container_spice_2",0,"Container_spice_2","bo_Container_spice_1_2_3", []),
  ("Container_spice_3",0,"Container_spice_3","bo_Container_spice_1_2_3", []),
  ("Container_food_1",0,"Container_food_1","bo_Container_food_1_2_3", []),
  ("Container_food_2",0,"Container_food_2","bo_Container_food_1_2_3", []),
  ("Container_food_3",0,"Container_food_3","bo_Container_food_1_2_3", []),
  ("Container_metal_1",0,"Container_metal_1","bo_Container_metal_1_2_3", []),
  ("Container_metal_2",0,"Container_metal_2","bo_Container_metal_1_2_3", []),
  ("Container_metal_3",0,"Container_metal_3","bo_Container_metal_1_2_3", []),
  ("Container_death_sticks",0,"Container_death_sticks","bo_Container_death_sticks", []),
  ("Container_drink_1",0,"Container_drink_1","bo_Container_drink_1_2_3", []),
  ("Container_drink_2",0,"Container_drink_2","bo_Container_drink_1_2_3", []),
  ("Container_drink_3",0,"Container_drink_3","bo_Container_drink_1_2_3", []),
  ("Carbonite_Tibanna",0,"Carbonite_Tibanna","bo_Carbonite_Tibanna", []),
  ("terminal3",0,"terminal3","bo_terminal3_4", []),
  ("terminal4",0,"terminal4","bo_terminal3_4", []),

#--spropbot.2011-07-19>>11:17:12
  ("naboo_table_1",0,"naboo_table_1","bo_naboo_table_1", []),
  ("naboo_chair_1",0,"naboo_chair_1","bo_naboo_chair_1", []),
  ("naboo_chair_2",0,"naboo_chair_2","bo_naboo_chair_2", []),

#--spropbot.2011-07-21>>15:02:57
  ("sundari_peace_park",0,"sundari_peace_park","bo_sundari_peace_park", []),
  ("sundari_block_1",0,"sundari_block_1","0", []),

#--spropbot.2011-07-22>>22:32:12
  ("sundari_block_2",0,"sundari_block_2","0", []),
  ("sundari_block_3",0,"sundari_block_3","0", []),
  ("sundari_block_4",0,"sundari_block_4","0", []),
  ("sundari_block_5",0,"sundari_block_5","0", []),
  ("sundari_small_block_1",0,"sundari_small_block_1","0", []),
  ("sundari_small_block_2",0,"sundari_small_block_2","0", []),
  ("sundari_small_block_3",0,"sundari_small_block_3","0", []),
  ("endor_walkway",0,"endor_walkway","bo_endor_walkway", []),
  ("endor_walkway_support",0,"endor_walkway_support","bo_endor_walkway_support", []),
  ("ahto_city",0,"ahto_city","bo_ahto_city", []),
  ("Hoth_radio",0,"Hoth_radio","bo_Hoth_radio", []),
  ("Hoth_turret",0,"Hoth_turret","bo_Hoth_turret", []),
  ("Hoth_heater",0,"Hoth_heater","bo_Hoth_heater", []),
  ("Hoth_droid",0,"Hoth_droid","bo_Hoth_droid", []),
  ("Felucia_flower1",0,"Felucia_flower1","bo_Felucia_flower1", []),
  ("Hoth_floor1",0,"Hoth_floor1","bo_Hoth_floor1", []),
  ("Hoth_pillar1",0,"Hoth_pillar1","bo_Hoth_pillar", []),
  ("Hoth_pillar2",0,"Hoth_pillar2","bo_Hoth_pillar", []),

  ("endor_fac_1",0,"endor_fac_1","bo_endor_fac_1_2", []),
  ("endor_fac_2",0,"endor_fac_2","bo_endor_fac_1_2", []),

  ("Hoth_radar",0,"Hoth_radar","bo_Hoth_radar", []),
  ("Hoth_cannon",0,"Hoth_cannon","bo_Hoth_cannon", []),
  ("Hoth_battery_2",0,"Hoth_battery_2","0", []),
  ("Hoth_battery_3",0,"Hoth_battery_3","0", []),
  ("Hoth_battery_4",0,"Hoth_battery_4","0", []),

#@Automagically added -- End



#----------------------------------------------------------------------
  ("rm_end",sokf_invisible,"psys_helper","0", []),
   #add everything crashable here:(asteroids and etc.)
  ("col_end",sokf_invisible,"psys_helper","0", []),
#Highlander begin--------------------------------------
  ("scene_props_end",sokf_invisible,"psys_helper","0", []), #leave this at the last position
#Highlander end--------------------------------------
]
