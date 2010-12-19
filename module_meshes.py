# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M 
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from header_meshes import *

####################################################################################################################
#  Each mesh record contains the following fields:
#  1) Mesh id: used for referencing meshes in other files. The prefix mesh_ is automatically added before each mesh id.
#  2) Mesh flags. See header_meshes.py for a list of available flags
#  3) Mesh resource name: Resource name of the mesh
#  4) Mesh translation on x axis: Will be done automatically when the mesh is loaded
#  5) Mesh translation on y axis: Will be done automatically when the mesh is loaded
#  6) Mesh translation on z axis: Will be done automatically when the mesh is loaded
#  7) Mesh rotation angle over x axis: Will be done automatically when the mesh is loaded
#  8) Mesh rotation angle over y axis: Will be done automatically when the mesh is loaded
#  9) Mesh rotation angle over z axis: Will be done automatically when the mesh is loaded
#  10) Mesh x scale: Will be done automatically when the mesh is loaded
#  11) Mesh y scale: Will be done automatically when the mesh is loaded
#  12) Mesh z scale: Will be done automatically when the mesh is loaded
####################################################################################################################

meshes = [
  ("pic_bandits", 0, "pic_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_mb_warrior_1", 0, "pic_mb_warrior_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_messenger", 0, "pic_messenger", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_prisoner_man", 0, "pic_prisoner_man", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_prisoner_fem", 0, "pic_prisoner_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_prisoner_wilderness", 0, "pic_prisoner_wilderness", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_siege_sighted", 0, "pic_siege_sighted", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_siege_sighted_fem", 0, "pic_siege_sighted_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_camp", 0, "pic_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_payment", 0, "pic_payment", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_escape_1", 0, "pic_escape_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_escape_1_fem", 0, "pic_escape_1_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_victory", 0, "pic_victory", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_defeat", 0, "pic_defeat", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_wounded", 0, "pic_wounded", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_wounded_fem", 0, "pic_wounded_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_steppe_bandits", 0, "pic_steppe_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_black_sun_pirates", 0, "pic_black_sun_pirates", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_sea_raiders", 0, "pic_sea_raiders", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_deserters", 0, "pic_deserters", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_blazing_claw_pirates", 0, "pic_blazing_claw_pirates", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_cattle", 0, "pic_cattle", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_looted_village", 0, "pic_looted_village", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_minorplanet_p", 0, "pic_village_p", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_minorplanet_s", 0, "pic_village_s", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_minorplanet_w", 0, "pic_village_w", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_recruits", 0, "pic_recruits", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_swadian", 0, "pic_arms_empire", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_vaegir", 0, "pic_arms_rebel", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_khergit", 0, "pic_arms_hutt", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_nord", 0, "pic_arms_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_arms_rhodok", 0, "pic_arms_rhodok", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  #SW - new background pictures
  ("pic_fullscreen_default", 0, "pic_fullscreen_default", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("pic_fullscreen_minorplanet_1", 0, "pic_fullscreen_minorplanet_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("pic_fullscreen_minorplanet_2", 0, "pic_fullscreen_minorplanet_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("pic_fullscreen_spacestation", 0, "pic_fullscreen_spacestation", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("pic_fullscreen_mainplanet_1", 0, "pic_fullscreen_mainplanet_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("pic_fullscreen_mainplanet_2", 0, "pic_fullscreen_mainplanet_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("pic_fullscreen_mainplanet_3", 0, "pic_fullscreen_mainplanet_3", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("pic_fullscreen_mainplanet_endor", 0, "pic_fullscreen_mainplanet_endor", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("pic_fullscreen_mainplanet_gamorr", 0, "pic_fullscreen_mainplanet_gamorr", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("pic_fullscreen_mainplanet_hoth", 0, "pic_fullscreen_mainplanet_hoth", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("pic_fullscreen_mainplanet_kashyyk", 0, "pic_fullscreen_mainplanet_kashyyk", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("pic_fullscreen_mainplanet_tatooine", 0, "pic_fullscreen_mainplanet_tatooine", 0, 0, 0, 0, 0, 0, 1, 1, 1), 
  ("pic_fullscreen_mainplanet_kamino", 0, "pic_fullscreen_mainplanet_kamino", 0, 0, 0, 0, 0, 0, 1, 1, 1), 
  ("pic_fullscreen_mainplanet_bespin", 0, "pic_fullscreen_mainplanet_bespin", 0, 0, 0, 0, 0, 0, 1, 1, 1), 
  
  #SW - new pictures
  ("pic_rancors", 0, "pic_rancors", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  #SW - new presentation meshes
  ("binocular_display", 0, "binocular_display", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("weapon_display", 0, "weapon_display", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("helmet_view_stormtrooper", 0, "helmet_view_stormtrooper", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("helmet_view_shadow_stormtrooper", 0, "helmet_view_shadow_stormtrooper", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("helmet_view_mandalorian", 0, "helmet_view_mandalorian", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("helmet_view_fang", 0, "helmet_view_fang", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_defiler", 0, "helmet_view_defiler", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_imperial_gunner", 0, "helmet_view_defiler", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_beak", 0, "helmet_view_beak", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_clone", 0, "helmet_view_clone", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_royal_guard", 0, "helmet_view_royal_guard", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_black_sun", 0, "helmet_view_black_sun", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_scout_trooper", 0, "helmet_view_scout_trooper", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_shadow_scout_trooper", 0, "helmet_view_shadow_scout_trooper", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_eyepiece_left", 0, "helmet_view_eyepiece_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_eyepiece_right", 0, "helmet_view_eyepiece_right", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_imperial_trooper_rebel_honor_guard", 0, "helmet_view_imperial_trooper_rebel_honor_guard", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_glasses_black", 0, "helmet_view_glasses_black", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_glasses_yellow", 0, "helmet_view_glasses_yellow", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_trandoshan", 0, "helmet_view_trandoshan", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_tusken_gas", 0, "helmet_view_tusken_gas", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_wookiee", 0, "helmet_view_wookiee", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("helmet_view_darth_vader", 0, "helmet_view_darth_vader", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  
  #SW - new health overlay meshes
  ("player_damage_25", 0, "player_damage_25", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("player_damage_50", 0, "player_damage_50", 0, 0, 0, 0, 0, 0, 1, 1, 1), 
  ("player_damage_75", 0, "player_damage_75", 0, 0, 0, 0, 0, 0, 1, 1, 1), 

##@> SWY New Class Pics for Selection Window

  ("ui_soldier", 0, "ui_soldier", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_merchant", 0, "ui_merchant", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  ("portrait_blend_out", 0, "portrait_blend_out", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("load_window", 0, "load_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("checkbox_off", render_order_plus_1, "checkbox_off", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("checkbox_on", render_order_plus_1, "checkbox_on", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("white_plane", 0, "white_plane", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("white_dot", 0, "white_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("player_dot", 0, "player_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_infantry", 0, "flag_infantry", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_archers", 0, "flag_archers", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_cavalry", 0, "flag_cavalry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("color_picker", 0, "color_picker",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("custom_map_banner_01", 0, "custom_map_banner_01",  0, 0, 0, -90, 0, 90, 1, 1, 1),
  ("custom_map_banner_02", 0, "custom_map_banner_02",  0, 0, 0, -90, 0, 90, 1, 1, 1),
  ("custom_map_banner_03", 0, "custom_map_banner_03",  0, 0, 0, -90, 0, 90, 1, 1, 1),
  ("custom_banner_01", 0, "custom_banner_01",  0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("custom_banner_02", 0, "custom_banner_02",  0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("custom_banner_bg", 0, "custom_banner_bg",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg01", 0, "custom_banner_fg01",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg02", 0, "custom_banner_fg02",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg03", 0, "custom_banner_fg03",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg04", 0, "custom_banner_fg04",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg05", 0, "custom_banner_fg05",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg06", 0, "custom_banner_fg06",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg07", 0, "custom_banner_fg07",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg08", 0, "custom_banner_fg08",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg09", 0, "custom_banner_fg09",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg10", 0, "custom_banner_fg10",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg11", 0, "custom_banner_fg11",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg12", 0, "custom_banner_fg12",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg13", 0, "custom_banner_fg13",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg14", 0, "custom_banner_fg14",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg15", 0, "custom_banner_fg15",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg16", 0, "custom_banner_fg16",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg17", 0, "custom_banner_fg17",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg18", 0, "custom_banner_fg18",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg19", 0, "custom_banner_fg19",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg20", 0, "custom_banner_fg20",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg21", 0, "custom_banner_fg21",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg22", 0, "custom_banner_fg22",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg23", 0, "custom_banner_fg23",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_01", 0, "custom_banner_charge_01",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_02", 0, "custom_banner_charge_02",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_03", 0, "custom_banner_charge_03",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_04", 0, "custom_banner_charge_04",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_05", 0, "custom_banner_charge_05",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_06", 0, "custom_banner_charge_06",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_07", 0, "custom_banner_charge_07",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_08", 0, "custom_banner_charge_08",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_09", 0, "custom_banner_charge_09",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_10", 0, "custom_banner_charge_10",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_11", 0, "custom_banner_charge_11",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_12", 0, "custom_banner_charge_12",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_13", 0, "custom_banner_charge_13",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_14", 0, "custom_banner_charge_14",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_15", 0, "custom_banner_charge_15",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_16", 0, "custom_banner_charge_16",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_17", 0, "custom_banner_charge_17",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_18", 0, "custom_banner_charge_18",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_19", 0, "custom_banner_charge_19",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_20", 0, "custom_banner_charge_20",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_21", 0, "custom_banner_charge_21",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_22", 0, "custom_banner_charge_22",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_23", 0, "custom_banner_charge_23",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_24", 0, "custom_banner_charge_24",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_25", 0, "custom_banner_charge_25",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_26", 0, "custom_banner_charge_26",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_27", 0, "custom_banner_charge_27",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_28", 0, "custom_banner_charge_28",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_29", 0, "custom_banner_charge_29",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_30", 0, "custom_banner_charge_30",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_31", 0, "custom_banner_charge_31",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_32", 0, "custom_banner_charge_32",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_33", 0, "custom_banner_charge_33",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_34", 0, "custom_banner_charge_34",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_35", 0, "custom_banner_charge_35",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_36", 0, "custom_banner_charge_36",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_37", 0, "custom_banner_charge_37",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_38", 0, "custom_banner_charge_38",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_39", 0, "custom_banner_charge_39",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_40", 0, "custom_banner_charge_40",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_41", 0, "custom_banner_charge_41",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_42", 0, "custom_banner_charge_42",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_43", 0, "custom_banner_charge_43",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_44", 0, "custom_banner_charge_44",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_45", 0, "custom_banner_charge_45",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_46", 0, "custom_banner_charge_46",  0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("tableau_mesh_custom_banner", 0, "tableau_mesh_custom_banner", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_custom_banner_square", 0, "tableau_mesh_custom_banner_square", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_custom_banner_tall", 0, "tableau_mesh_custom_banner_tall", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_custom_banner_short", 0, "tableau_mesh_custom_banner_short", 0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("tableau_mesh_shield_round_1",  0, "tableau_mesh_shield_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_2",  0, "tableau_mesh_shield_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_3",  0, "tableau_mesh_shield_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_4",  0, "tableau_mesh_shield_round_4", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_5",  0, "tableau_mesh_shield_round_5", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_1",  0, "tableau_mesh_shield_small_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_2",  0, "tableau_mesh_shield_small_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_3",  0, "tableau_mesh_shield_small_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_1",   0, "tableau_mesh_shield_kite_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_2",   0, "tableau_mesh_shield_kite_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_3",   0, "tableau_mesh_shield_kite_3",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_kite_4",   0, "tableau_mesh_shield_kite_4",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_heater_1", 0, "tableau_mesh_shield_heater_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_heater_2", 0, "tableau_mesh_shield_heater_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_pavise_1", 0, "tableau_mesh_shield_pavise_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_pavise_2", 0, "tableau_mesh_shield_pavise_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("heraldic_armor_bg", 0, "heraldic_armor_bg",  0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("tableau_mesh_heraldic_armor_a", 0, "tableau_mesh_heraldic_armor_a",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_armor_b", 0, "tableau_mesh_heraldic_armor_b",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_armor_c", 0, "tableau_mesh_heraldic_armor_c",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_armor_d", 0, "tableau_mesh_heraldic_armor_d",  0, 0, 0, 0, 0, 0, 1, 1, 1),

 #? ("outer_terrain_plain_1", 0, "outer_border_a", -90, 0, 0, 0, 0, 0, 1, 1, 1),
  ("banner_a01", 0, "banner_a01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a02", 0, "banner_a02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a03", 0, "banner_a03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a04", 0, "banner_a04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a05", 0, "banner_a05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a06", 0, "banner_a06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a07", 0, "banner_a07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a08", 0, "banner_a08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a09", 0, "banner_a09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a10", 0, "banner_a10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a11", 0, "banner_a11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a12", 0, "banner_a12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a13", 0, "banner_a13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a14", 0, "banner_a14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a15", 0, "banner_f21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a16", 0, "banner_a16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a17", 0, "banner_a17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a18", 0, "banner_a18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a19", 0, "banner_a19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a20", 0, "banner_a20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a21", 0, "banner_a21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b01", 0, "banner_b01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b02", 0, "banner_b02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b03", 0, "banner_b03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b04", 0, "banner_b04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b05", 0, "banner_b05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b06", 0, "banner_b06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b07", 0, "banner_b07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b08", 0, "banner_b08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b09", 0, "banner_b09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b10", 0, "banner_b10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b11", 0, "banner_b11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b12", 0, "banner_b12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b13", 0, "banner_b13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b14", 0, "banner_b14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b15", 0, "banner_b15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b16", 0, "banner_b16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b17", 0, "banner_b17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b18", 0, "banner_b18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b19", 0, "banner_b19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b20", 0, "banner_b20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b21", 0, "banner_b21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c01", 0, "banner_c01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c02", 0, "banner_c02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c03", 0, "banner_c03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c04", 0, "banner_c04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c05", 0, "banner_c05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c06", 0, "banner_c06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c07", 0, "banner_c07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c08", 0, "banner_c08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c09", 0, "banner_c09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c10", 0, "banner_c10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c11", 0, "banner_c11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c12", 0, "banner_c12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c13", 0, "banner_c13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c14", 0, "banner_c14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c15", 0, "banner_c15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c16", 0, "banner_c16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c17", 0, "banner_c17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c18", 0, "banner_c18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c19", 0, "banner_c19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c20", 0, "banner_c20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c21", 0, "banner_c21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d01", 0, "banner_d01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d02", 0, "banner_d02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d03", 0, "banner_d03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d04", 0, "banner_d04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d05", 0, "banner_d05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d06", 0, "banner_d06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d07", 0, "banner_d07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d08", 0, "banner_d08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d09", 0, "banner_d09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d10", 0, "banner_d10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d11", 0, "banner_d11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d12", 0, "banner_d12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d13", 0, "banner_d13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d14", 0, "banner_d14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d15", 0, "banner_d15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d16", 0, "banner_d16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d17", 0, "banner_d17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d18", 0, "banner_d18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d19", 0, "banner_d19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d20", 0, "banner_d20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d21", 0, "banner_d21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e01", 0, "banner_e01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e02", 0, "banner_e02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e03", 0, "banner_e03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e04", 0, "banner_e04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e05", 0, "banner_e05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e06", 0, "banner_e06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e07", 0, "banner_e07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e08", 0, "banner_e08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e09", 0, "banner_e09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e10", 0, "banner_e10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e11", 0, "banner_e11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e12", 0, "banner_e12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e13", 0, "banner_e13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e14", 0, "banner_e14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e15", 0, "banner_e15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e16", 0, "banner_e16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e17", 0, "banner_e17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e18", 0, "banner_e18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e19", 0, "banner_e19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e20", 0, "banner_e20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e21", 0, "banner_e21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f01", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f02", 0, "banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f03", 0, "banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f04", 0, "banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f05", 0, "banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f06", 0, "banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f07", 0, "banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f08", 0, "banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f09", 0, "banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f10", 0, "banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f11", 0, "banner_f11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f12", 0, "banner_f12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f13", 0, "banner_f13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f14", 0, "banner_f14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f15", 0, "banner_f15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f16", 0, "banner_f16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f17", 0, "banner_f17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f18", 0, "banner_f18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f19", 0, "banner_f19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f20", 0, "banner_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f21", 0, "banner_a15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  


  ("arms_a01", 0, "arms_a01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a02", 0, "arms_a02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a03", 0, "arms_a03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a04", 0, "arms_a04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a05", 0, "banner_a05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a06", 0, "arms_a06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a07", 0, "banner_a07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a08", 0, "arms_a08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a09", 0, "banner_a09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a10", 0, "banner_a10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a11", 0, "banner_a11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a12", 0, "arms_a12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a13", 0, "arms_a13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a14", 0, "banner_a14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a15", 0, "banner_f21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a16", 0, "arms_a16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a17", 0, "arms_a17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a18", 0, "arms_a18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a19", 0, "arms_a19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a20", 0, "arms_a20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a21", 0, "arms_a21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b01", 0, "arms_b01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b02", 0, "arms_b02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b03", 0, "banner_b03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b04", 0, "banner_b04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b05", 0, "arms_b05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b06", 0, "arms_b06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b07", 0, "arms_b07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b08", 0, "arms_b08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b09", 0, "arms_b09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b10", 0, "arms_b10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b11", 0, "banner_b11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b12", 0, "banner_b12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b13", 0, "banner_b13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b14", 0, "arms_b14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b15", 0, "arms_b15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b16", 0, "arms_b16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b17", 0, "banner_b17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b18", 0, "arms_b18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b19", 0, "banner_b19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b20", 0, "arms_b20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_b21", 0, "banner_b21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c01", 0, "arms_c01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c02", 0, "banner_c02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c03", 0, "banner_c03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c04", 0, "arms_c04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c05", 0, "banner_c05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c06", 0, "arms_c06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c07", 0, "arms_c07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c08", 0, "banner_c08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c09", 0, "banner_c09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c10", 0, "arms_c10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c11", 0, "banner_c11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c12", 0, "arms_c12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c13", 0, "arms_c13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c14", 0, "arms_c14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c15", 0, "banner_c15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c16", 0, "arms_c16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c17", 0, "banner_c17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c18", 0, "banner_c18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c19", 0, "arms_c19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c20", 0, "banner_c20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_c21", 0, "banner_c21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d01", 0, "banner_d01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d02", 0, "arms_d02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d03", 0, "arms_d03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d04", 0, "arms_d04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d05", 0, "banner_d05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d06", 0, "arms_d06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d07", 0, "arms_d07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d08", 0, "arms_d08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d09", 0, "arms_d09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d10", 0, "banner_d10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d11", 0, "arms_d11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d12", 0, "arms_d12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d13", 0, "arms_d13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d14", 0, "arms_d14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d15", 0, "arms_d15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d16", 0, "arms_d16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d17", 0, "arms_d17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d18", 0, "arms_d18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d19", 0, "arms_d19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d20", 0, "arms_d20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_d21", 0, "arms_d21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e01", 0, "banner_e01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e02", 0, "arms_e02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e03", 0, "banner_e03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e04", 0, "banner_e04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e05", 0, "banner_e05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e06", 0, "banner_e06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e07", 0, "banner_e07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e08", 0, "banner_e08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e09", 0, "banner_e09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e10", 0, "banner_e10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e11", 0, "banner_e11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e12", 0, "banner_e12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e13", 0, "banner_e13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e14", 0, "banner_e14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e15", 0, "banner_e15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e16", 0, "banner_e16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e17", 0, "banner_e17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e18", 0, "banner_e18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e19", 0, "banner_e19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e20", 0, "banner_e20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e21", 0, "banner_e21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("arms_f01", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f02", 0, "banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f03", 0, "banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f04", 0, "banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f05", 0, "banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f06", 0, "banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f07", 0, "banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f08", 0, "banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f09", 0, "banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f10", 0, "banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f11", 0, "banner_f11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f12", 0, "banner_f12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f13", 0, "banner_f13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f14", 0, "banner_f14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f15", 0, "banner_f15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f16", 0, "banner_f16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f17", 0, "banner_f17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f18", 0, "banner_f18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f19", 0, "banner_f19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f20", 0, "banner_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f21", 0, "banner_a15", 0, 0, 0, -90, 0, 0, 1, 1, 1),


  ("banners_default_a", 0, "banners_default_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_b", 0, "banners_default_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_c", 0, "banners_default_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_d", 0, "banners_default_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_e", 0, "banners_default_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),

#SW - FROM BLACKJACK MOD
##plus  
  ("text_bar", 0, "text_bar", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("button_used", 0, "medium_button", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("button_press_any_key", 0, "button_drop_hl", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("21_troop_portrait", 0, "blackjack_troop_portrait", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("21_button", 0, "21button", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("21_button_down", 0, "21button_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_heart_a", 0, "poker_12", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_heart_2", 0, "poker_13", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_heart_3", 0, "poker_14", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_heart_4", 0, "poker_15", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_heart_5", 0, "poker_16", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_heart_6", 0, "poker_17", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_heart_7", 0, "poker_18", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_heart_8", 0, "poker_19", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_heart_9", 0, "poker_21", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_heart_10", 0, "poker_22", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_heart_j", 0, "poker_23", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_heart_q", 0, "poker_24", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_heart_k", 0, "poker_25", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_spade_a", 0, "poker_26", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_spade_2", 0, "poker_27", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_spade_3", 0, "poker_28", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_spade_4", 0, "poker_29", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_spade_5", 0, "poker_31", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_spade_6", 0, "poker_32", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_spade_7", 0, "poker_33", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_spade_8", 0, "poker_34", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_spade_9", 0, "poker_35", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_spade_10", 0, "poker_36", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_spade_j", 0, "poker_37", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_spade_q", 0, "poker_38", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_spade_k", 0, "poker_39", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_diamond_a", 0, "poker_41", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_diamond_2", 0, "poker_42", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_diamond_3", 0, "poker_43", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_diamond_4", 0, "poker_44", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_diamond_5", 0, "poker_45", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_diamond_6", 0, "poker_46", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_diamond_7", 0, "poker_47", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_diamond_8", 0, "poker_48", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_diamond_9", 0, "poker_49", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_diamond_10", 0, "poker_51", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_diamond_j", 0, "poker_52", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_diamond_q", 0, "poker_53", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_diamond_k", 0, "poker_54", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_club_a", 0, "poker_55", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_club_2", 0, "poker_56", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_club_3", 0, "poker_57", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_club_4", 0, "poker_58", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_club_5", 0, "poker_59", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_club_6", 0, "poker_61", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_club_7", 0, "poker_62", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_club_8", 0, "poker_63", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_club_9", 0, "poker_64", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_club_10", 0, "poker_65", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_club_j", 0, "poker_66", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_club_q", 0, "poker_67", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_club_k", 0, "poker_68", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_red_joker", 0, "poker_69", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_black_joker", 0, "poker_11", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("poker_back", 0, "poker_back", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("wood_table", 0, "wood_table", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#SW - integrated companion overview  
   #### JEDEDIAH Q mesh for Companions Overview ##############################
  ("cpov", 0, "cpov", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #### JEDEDIAH Q mesh for Companions Overview END ##############################  
  ("swc_logo", 0, "warrider_logo", 0, 0, 0, 0, 0, 0, 1, 1, 1),
]
