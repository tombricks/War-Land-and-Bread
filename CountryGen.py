countries = [
    ["YEM", "Yemen", "Yemen Arab Republic", "Yemeni", "Reformist_Socialism", "293", "204 90 62", "Middle_Eastern"],
    ["SCO", "Scotland", "Socialist People's Republic of Scotland", "Scottish", "Reformist_Socialism", "121", "127 0 55", "Western_European"],
    ["WLS", "Wales", "Socialist People's Republic of Wales", "Welsh", "Reformist_Socialism", "122", "63 202 63", "Western_European"],
    ["IRE", "Ireland", "Irish Republic", "Irish", "Reformist_Socialism", "113", "130 115 64", "Western_European"],
    ["NGL", "Northern England", "Northern England Federal Republic", "Northern English", "Reformist_Socialism", "132", "127 51 63", "Western_European"]
]

from shutil import copyfile
FileTags  = open("common/country_tags/00_countries.txt", "a+", encoding="utf8")
FileLoc   = open("localisation/countries_l_english.yml", "a+", encoding="utf8")
FileColor = open("common/countries/colors.txt", "a+", encoding="utf8")

for country in countries:
    FileTags.write(F"\n{country[0]} = \"countries/{country[7]}.txt\" ")
    FileLoc.write(F"""

 {country[0]}: "{country[1]}"
 {country[0]}_ADJ: "{country[3]}"
 {country[0]}_DEF: "{country[1]}"
 {country[0]}_Hypersocialism: "{country[2]}"
 {country[0]}_Hypersocialism_ADJ: "{country[3]}"
 {country[0]}_Hypersocialism_DEF: "The {country[2]}"
 {country[0]}_Marxism_Leninism: "{country[2]}"
 {country[0]}_Marxism_Leninism_ADJ: "{country[3]}"
 {country[0]}_Marxism_Leninism_DEF: "The {country[2]}"
 {country[0]}_New_Marxism: "{country[2]}"
 {country[0]}_New_Marxism_ADJ: "{country[3]}"
 {country[0]}_New_Marxism_DEF: "The {country[2]}"
 {country[0]}_Reformist_Socialism: "{country[2]}"
 {country[0]}_Reformist_Socialism_ADJ: "{country[3]}"
 {country[0]}_Reformist_Socialism_DEF: "The {country[2]}" """)
    FileColor.write(F"""
{country[0]} = {{
	color = rgb {{ {country[6]} }}
	color_ui = rgb {{ {country[6]} }}
}}""")

    path = F"history/countries/{country[0]} - {country[1]}.txt"
    with open(path, "w", encoding="utf8") as FileHistory:
        FileHistory.write(F"""capital = {country[5]}
set_stability = 0.6
set_war_support = 0.6

set_technology = {{
	infantry_weapons = 1
	infantry_weapons1 = 1
	tech_support = 1		
	tech_recon = 1
	tech_engineers = 1
	motorised_infantry = 1
	early_fighter = 1
	trench_warfare = 1
	fuel_silos = 1
	fuel_refining = 1
}}

set_politics = {{
	ruling_party = {country[4]}
	last_election = "1.1.1"
	election_frequency = 48
	elections_allowed = yes
}}

set_popularities = {{
	{country[4]} = 100
}}

create_country_leader = {{
	name = "Genericco"
	picture = "gfx/leaders/leader_unknown.dds"
	ideology = {country[4]}_ideology
}}""")
    copyfile("gfx/flags/ZZZ.tga", F"gfx/flags/{country[0]}.tga")
    copyfile("gfx/flags/medium/ZZZ.tga", F"gfx/flags/medium/{country[0]}.tga")
    copyfile("gfx/flags/small/ZZZ.tga", F"gfx/flags/small/{country[0]}.tga")

FileTags.seek(0)
print(FileTags.read())
FileLoc.seek(0)
print(FileLoc.read())
FileColor.seek(0)
print(FileColor.read())
