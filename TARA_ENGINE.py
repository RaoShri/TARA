

print("Welcome to TARA  analysis")

## Get asset and CIA type
asset = input("Please describe the asset under TARA \n")
print("Right, so the asset under consideration is :  " , asset)

##print data criticality table
d = { 
0 :   "Data is not important and will not affect the functioning of the system ",
1 :   "Data can affect the normal functionning of the system, but the system is not a critical component", 
2 :   "Data is critical to the normal functionning of the system, but the system is not a critical component",  
3 :   "Data can affect the normal functionning of the system, but the system is a critical component", 
4 :   "Data is user senstive / critical to the normal functionning of the system, but the system is a critical component" 
}


print("\nD Level   |         Rationale = Data Criticality ")
print("--------------------------------------------------------------------------------------------------------------------------------------------")

for k ,v in d.items():
    D = v
    print(k, "        |        ", D)

data_criticality = int(input("\nLets talk about data criticality, refer this table to understand criticality of the data in your device under analysis and feed a value you deem most appropriate\n"))

print("You have chosen a data criticality level of ", data_criticality, "for your asset under analysis\n")
dc = d[data_criticality]

##print attacker knwoledge level table
d = { 
0 :   "Information about this system and attack is publicly available and is easy to acquire",
1 :   "Some information about this system is publicly available some prior security experience is required",
2 :   "Information is confidential and protected, requires comprehensive domain experience",
}


print("\nK Level   |         Rationale = Attacker Knowledge Level needed ")
print("--------------------------------------------------------------------------------------------------------------------------------------------")

for k ,v in d.items():
    D = v
    print(k, "        |        ", D)

knowledge = int(input("\nLets talk about knowledge level of the attack, refer this table to understand the required skills of the attacker and feed a value you deem most appropriate\n"))

print("You have chosen a required knowldege level of ", knowledge, "for the attacker targetting the asset under analysis\n")

kd = d[knowledge]



##print required tool level table
d = { 
0 :   "No specific tools required to launch this attack",
1 :   "Standard tools needed and usage information of the tools are available publicly",
2 :   "Specific tools available with OEMs or licensed products with limited information on usage",
}


print("\nT Level   |         Rationale = Attacker Tools needed ")
print("--------------------------------------------------------------------------------------------------------------------------------------------")

for k ,v in d.items():
    D = v
    print(k, "        |        ", D)

tool = int(input("\nLets talk about complexity of the tools needed for the attack, refer this table to understand the tool complexity and feed a value you deem most appropriate\n"))

print("You have chosen a required knowldege level of", tool, "for the attacker targetting the asset under analysis\n")

t = d[tool]

##print attack potential table
d = { 
0 :   "Comprehensive domain knowldge and very specific tools are needed to mount the attack, so protential is very low",
1 :   "Good understanding of system and tools required, so the attack protential is low",
2 :   "The system is easy to break into with standard open source tools and knowledge, so the attack potential is considered to be high",
3 :   "Public knowledge is available about the system and no additonal tools are needed, the attack potential is very high" 
}

#Calculate attack potential for the inputs given
attacker_potential_table = ([3,2,1],[2,2,1],[1,1,0]);
attacker_potential = attacker_potential_table[tool][knowledge]

ap = d[attacker_potential]
print("For the chosen attacker knowledge and required tool levels indicate that", ap )


#print attacker controllability level table
d = { 
0 :   "Controlling the system and reverting operating state is easy",
1 :   "Controlling the system and reverting operating state is difficult but possible",
2 :   "Controlling the system and reverting operating state is impossible",
}


print("\nC Level   |         Rationale = Controllability of the device under attack")
print("--------------------------------------------------------------------------------------------------------------------------------------------")

for k ,v in d.items():
    D = v
    print(k, "        |        ", D)

controllability = int(input("\nLets talk about controllability of the system under attack, refer this table to understand the difficult in reverting system to normal operation and feed a value you deem most appropriate\n"))

print("You have chosen a controllability level of ", controllability, "for the system under attack\n")
cy = d[controllability]


##print automation level table
d = { 
0 :   "No Automation is involved in the system",
1 :   "Driver assistance -  Human is in complete control of vehicle",
2 :   "Partial Automation - Human is in control of vehicle most of the time, automated driving in certain situations",
3 :   "Conditional Auomation - Vehicle is in control of the vehicle, human override is required when conditions are not met",   
4 :   "High Automation - Vehicle is in control of the vehicle, human override is an option, but attention is needed",
5 :    "Full Automation - Human is not Involved in controlling the vehicle"
}


print("\nF Level   |         Rationale = Automation Level invovled in the component under test ")
print("--------------------------------------------------------------------------------------------------------------------------------------------")

for k ,v in d.items():
    D = v
    print(k, "        |        ", D)

automation = int(input("\nLets talk about automation invovled in the system as result of drive towards ADAS, refer this table to understand this and feed a value you deem most appropriate\n"))
print("You have chosen a automation level of", automation, "for the asset under analysis\n")
am = d[automation]

d = {
0 :   "Human is fully in control of the system during the attack",
1 :   "Human has high control over the system during the attack",
2 :   "Human has medium level of control of the system during the attack",
3 :   "Human has low level of control of the system during the attack",
4 :   "Human has no of control of the system during the attack"
}
#Calculate human factor for the input parameters
human_factor_table = ([0, 1, 4], [0, 2, 4], [1, 2, 4], [2, 3, 4], [3, 3, 4], [4, 4, 4]);
human_factor = human_factor_table[automation][controllability]

h = d[human_factor]
print("The chosen controllability and car automation levels indicate that", h )

#Calculate threat severity
threat_severity_table = ([0, 0, 0, 0], [0, 1, 1, 2], [1, 2, 2, 2], [3, 3, 3, 4], [3, 4, 4, 4]);
threat_severity = threat_severity_table[data_criticality][attacker_potential]


#threat severity table
d = {
0 :   "Very Low",
1 :   "Low",
2 :   "Moderate",
3 :   "High",
4 :   "Very High",
}
ts = d[threat_severity]
print("Based on the parameters provided, it seems that threat severity is", ts )

#Calculate threat severity
cons_threat_severity_table = ([0, 0, 0, 0, 0], [1, 1, 1, 2, 2], [2, 2, 2, 3, 3], [2, 3, 3, 4, 4], [3, 3, 4, 4, 4]);
cons_threat_severity = cons_threat_severity_table[threat_severity][human_factor]
s = d[cons_threat_severity]

print("After factoring in the human factor incontrolling the system under attack, the updated threat severity is classified as", s )

print("Summary of the analysis : \n")
print("Asset : ",  asset)
print("1.", dc )
print("2.", kd )
print("3.", t )
print("4.", ap )
print("5.", cy )
print("6.", am )
print("7.", h )
print("8. Based on the above user inputs, the threat severity of", asset, "is", ts )
print("9. After considering the human factor in the system during the attack, threat severity can be considered as", s )

