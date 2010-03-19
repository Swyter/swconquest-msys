from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_shuttle,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_civilian_cruiser,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_mercenary_fighter,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_civilian_transport,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Colonial Defenders",icon_shuttle,0,fac_commoners,merchant_personality,[(trp_farmer,5,10),(trp_civilian,5,10),(trp_peasant_woman,0,4)]),
  ("cattle_herd","Nerf Herd",icon_shuttle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  #("looters","Jawas",icon_tusken|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,12,24)]),
  ("looters","Jawas",icon_mercenary_shuttle_brown|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,8,16),(trp_looter_2,5,10),(trp_looter_3,2,4),(trp_r2series,0,1,pmf_is_prisoner),(trp_3poseries,0,1,pmf_is_prisoner)]),  
  
# Ryan END
#SW - switched Manhunters to Trandoshan Slavers
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),
#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),

  ("manhunters","Trandoshan Slavers",icon_z95,0,fac_manhunters,soldier_personality,[(trp_manhunter,25,50),(trp_wookiee,0,1,pmf_is_prisoner)]),
  ("steppe_bandits","Night Fangs Pirates",icon_mercenary_shuttle|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_steppe_bandit,5,25),(trp_steppe_bandit_female,4,8),(trp_trandoshan,1,5),(trp_twilek,1,5),(trp_twilek_female1,0,1,pmf_is_prisoner)]),
  ("forest_bandits","Blazing Claw Pirates",icon_mercenary_fighter|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit,5,25),(trp_forest_bandit_female,4,8),(trp_rodian,1,5),(trp_sullustan_1,1,5),(trp_twilek_female1,0,1,pmf_is_prisoner)]),
  ("sea_raiders","Tusken Raiders",icon_mercenary_raider_brown|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_tusken_1,10,25),(trp_tusken_2,5,10)]),  
  ("mountain_bandits","Black Sun Pirates",icon_mercenary_raider|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit_1,10,20),(trp_mountain_bandit_2,5,10),(trp_mountain_bandit_3,5,10),(trp_mountain_bandit_4,1,10),(trp_twilek_female1,0,1,pmf_is_prisoner)]),
  
#SW - new outlaw party templates with Imperial Troops (nevermind, back to regular bandits)
#  ("steppe_bandits","Imperial Scouts",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_imperial_stormtrooper_mounted,8,15),(trp_imperial_scout_trooper,10,20)]),
#  ("forest_bandits","Imperial War Party",icon_axeman|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_imperial_stormtrooper,20,30),(trp_imperial_scout_trooper,10,15),(trp_sith_apprentice,5,10),(trp_sith_master,5,10)]),
#  ("mountain_bandits","Imperial Raiders",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_imperial_trooper,5,20),(trp_imperial_recruit,5,30)]),
#  ("sea_raiders","Imperial Patrol",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_imperial_stormtrooper,5,20),(trp_imperial_trooper,5,10),(trp_imperial_scout_trooper,5,10),(trp_sith_apprentice,2,4),(trp_sith_master,2,4)]),

  ("deserters","Deserters",icon_z95|carries_goods(3),0,fac_deserters,bandit_personality,[]),
 #SW - #MF added some new templates
  ("kingdom_1_escort", "Patrol Fleet", icon_z95|carries_goods(2)|pf_show_faction|pf_default_behavior,0,fac_commoners,aggressiveness_10|courage_12, [(trp_farmer,1,1)]),
  #("independent_traders", "Trade Federation Convoy",icon_bulk_frigate|carries_goods(20)|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_b1series,15,30),(trp_b2series,5,10)]),
  ("independent_traders", "Merchant Convoy",icon_bulk_freighter|carries_goods(20)|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_b1series,1,10),(trp_oom_series_command,1,1),(trp_security_guard,10,20)]),
  #SW - removed pf_auto_remove_in_town
  #("merchant_caravan","Merchant Freighter",icon_freighter|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_hired_guard,5,25)]),
  ("merchant_caravan","Merchant Freighter",icon_freighter|carries_goods(20)|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_security_guard,15,30)]),  
  ("troublesome_bandits","Troublesome Bandits",icon_z95|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,15,55)]),
  #SW - removed pf_auto_remove_in_town
  #("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_z95|carries_goods(9)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,25,65),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),  
  ("kidnapped_girl","Kidnapped Girl",icon_shuttle|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

##  ("farmers","Farmers",icon_peasant,0,fac_innocents,merchant_personality,[(trp_farmer,11,22),(trp_peasant_woman,16,44)]),
  ("village_farmers","Colonial Farmers",icon_civilian_transport,0,fac_innocents,merchant_personality,[(trp_farmer,6,12),(trp_peasant_woman,4,8)]),
##  ("refugees","Refugees",icon_woman_b,0,fac_innocents,merchant_personality,[(trp_refugee,19,48)]),
##  ("dark_hunters","Dark Hunters",icon_gray_knight,0,fac_dark_knights,soldier_personality,[(trp_dark_knight,4,42),(trp_dark_hunter,13,25)]),

  ("spy_partners", "Unremarkable Travellers", icon_z95|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_security_guard,5,10)]),
  ("runaway_serfs","Runaway Slaves",icon_civilian_cruiser|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,10), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_z95|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_z95|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_z95|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_z95|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_z95|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_z95|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_z95|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Freighters",icon_freighter|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_security_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_bulk_freighter|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),
##  ("merchant_party","Merchant",icon_mule|carries_goods(25)|pf_show_faction,0,fac_merchants,merchant_personality,[(trp_caravan_guard,12,40)]),
##  ("merchant_party_reinforcement","Merchant Party Reinforcement",icon_mule|carries_goods(25),0,fac_merchants,merchant_personality,[(trp_caravan_guard,6,20)]),

# Caravans

#SW - modified center_reinforcements
  ("center_reinforcements","Reinforcements",icon_z95|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,15),(trp_civilian,5,15),(trp_farmer,5,15)]),
  
  ("kingdom_hero_party","War Party",icon_player|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  


# Reinforcements
#  ("default_reinforcements_a","default_reinforcements_a",0,0,fac_commoners,0,[(trp_caravan_guard,1,10),(trp_watchman,3,16),(trp_farmer,9,24)]),
#  ("default_reinforcements_b","default_reinforcements_b",0,0,fac_commoners,0,[(trp_mercenary,1,7),(trp_caravan_guard,3,10),(trp_watchman,3,15)]),
#  ("default_reinforcements_c","default_reinforcements_c",0,0,fac_commoners,0,[(trp_hired_blade,1,7),(trp_mercenary,3,10),(trp_caravan_guard,3,15)]),

#SW - modified kingdom 1 reinforcements (empire = 6-13 troops)
  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_imperial_recruit,2,3),(trp_imperial_army_trooper,4,10)]),
  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_imperial_stormtrooper,6,13)]),
  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sith_hopeful,1,2),(trp_chiss_1,1,2),(trp_imperial_stormtrooper,1,2)]),

#SW - modified kingdom 2 reinforcements (rebel = 5-12 troops)
  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rebel_recruit,2,3),(trp_rebel_cadet,3,9)]),		#rebels have 1 less for min & max
  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rebel_trooper,3,8),(trp_wookiee,1,2),(trp_moncal_1,1,2)]),	#rebels have 1 less for min & max
  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_jedi_hopeful,1,2),(trp_sullustan_1,1,2),(trp_bothan,1,2)]),	#rebels are equal for this reinforcement
#SW - modified kingdom 3 reinforcements (hutt = 5-12 troops)
   ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_hutt_militia,2,3),(trp_hutt_mercenary,2,6),(trp_gamorrean,1,3),(trp_twilek_female1,0,1,pmf_is_prisoner)]),
   ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_hutt_guard,2,5),(trp_trandoshan,1,2),(trp_rodian,1,2),(trp_twilek,1,3),(trp_twilek_female1,0,1,pmf_is_prisoner)]),
   ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_mandalorian,1,1),(trp_gamorrean,1,2),(trp_hutt_skiff_guard,1,1),(trp_ig88,0,1),(trp_rancor,0,1)]),

  #SW - commented out kingdom 4 & 5 reinforcements  
  # ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_footman,2,6),(trp_nord_recruit,4,7)]),
  # ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_mercenary_crossbowman,2,4),(trp_nord_footman,4,7)]),
  # ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_warrior,3,6)]),

  # ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,2,6),(trp_rhodok_tribesman,4,7)]),
  # ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_crossbowman,2,6),(trp_rhodok_crossbowman,4,7)]),
  # ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,6)]),

#SW - Culture specific reinforcements
  ("kingdom_human_reinforcements_a", "kingdom_human_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_civilian,6,12)]),
  ("kingdom_human_reinforcements_b", "kingdom_human_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_civilian,3,6),(trp_militia,2,4),(trp_thug,1,2)]),
  ("kingdom_human_reinforcements_c", "kingdom_human_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_militia,2,4),(trp_thug,2,4)]),  
  ("kingdom_wookiee_reinforcements_a", "kingdom_wookiee_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_wookiee,6,12)]),
  ("kingdom_wookiee_reinforcements_b", "kingdom_wookiee_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_wookiee,3,6),(trp_wookiee_warrior,3,6)]),
  ("kingdom_wookiee_reinforcements_c", "kingdom_wookiee_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_wookiee_marksman,2,4),(trp_wookiee_berserker,2,4)]),
  ("kingdom_mandalorian_reinforcements_a", "kingdom_mandalorian_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_mandalorian,6,12)]),
  ("kingdom_mandalorian_reinforcements_b", "kingdom_mandalorian_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_mandalorian,3,6),(trp_mandalorian_soldier,3,6)]),
  ("kingdom_mandalorian_reinforcements_c", "kingdom_mandalorian_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_mandalorian_commando,2,4),(trp_mandalorian_sniper,2,4)]),  
  ("kingdom_clone_reinforcements_a", "kingdom_clone_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_clone_trooper_1,6,12)]),
  ("kingdom_clone_reinforcements_b", "kingdom_clone_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_clone_trooper_2,5,9),(trp_arc_trooper_2,1,3)]),
  ("kingdom_clone_reinforcements_c", "kingdom_clone_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_clone_trooper_3,3,6),(trp_arc_trooper_3,1,2)]),    
  ("kingdom_trandoshan_reinforcements_a", "kingdom_trandoshan_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_trandoshan,6,12)]),
  ("kingdom_trandoshan_reinforcements_b", "kingdom_trandoshan_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_trandoshan,3,6),(trp_trandoshan_warrior,3,6)]),
  ("kingdom_trandoshan_reinforcements_c", "kingdom_trandoshan_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_trandoshan_hunter,2,4),(trp_trandoshan_bounty_hunter,2,4)]),
  
##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,7),(trp_swadian_skirmisher,5,10),(trp_swadian_militia,11,26)]),
##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,5,10),(trp_swadian_infantry,5,10),(trp_swadian_crossbowman,3,8)]),
##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_knight,2,6),(trp_swadian_sergeant,2,5),(trp_swadian_sharpshooter,2,5)]),
##
##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,3,7),(trp_vaegir_skirmisher,5,10),(trp_vaegir_footman,11,26)]),
##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,4,9),(trp_vaegir_infantry,5,10),(trp_vaegir_archer,3,8)]),
##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_knight,3,7),(trp_vaegir_guard,2,5),(trp_vaegir_marksman,2,5)]),
##
##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,3,7),(trp_khergit_skirmisher,5,10),(trp_khergit_tribesman,11,26)]),
##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horse_archer,4,9),(trp_khergit_horse_archer,5,10),(trp_khergit_horseman,3,8)]),
##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer,3,7),(trp_khergit_veteran_horse_archer,2,5),(trp_khergit_horse_archer,2,5)]),
##
##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,3,7),(trp_nord_footman,5,10),(trp_nord_recruit,11,26)]),
##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_veteran,4,9),(trp_nord_warrior,5,10),(trp_nord_footman,3,8)]),
##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,3),(trp_nord_veteran,2,5),(trp_nord_warrior,2,5)]),
##
##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,3,7),(trp_rhodok_crossbowman,5,10),(trp_rhodok_tribesman,11,26)]),
##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,4,9),(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,3,8)]),
##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,7),(trp_rhodok_veteran_spearman,2,5),(trp_rhodok_veteran_crossbowman,2,5)]),
] 