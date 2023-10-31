import wbgapi as wb #importando la librería del banco mundial
wb.series.metadata.get('SL.UEM.TOTL.ZS')
Total_unemployment = wb.data.DataFrame('SL.UEM.TOTL.ZS', economy=['COL','ARG','CHL','BRA', 'URY', 'BOL','PER','PRY','ECU','VEN','MEX','CAN','USA','CRI'], time= range(2002,2020), labels=True).reset_index(drop=True).rename(columns={'SL.UEM.TOTL.ZS':'Unemployment'})
Total_unemployment

wb.series.metadata.get('NY.GDP.PCAP.CD')
GDP_per_capita = wb.data.DataFrame('NY.GDP.PCAP.CD', economy=['COL','ARG','CHL','BRA', 'URY', 'BOL','PER','PRY','ECU','VEN','MEX','CAN','USA','CRI'], time= range(2002,2020), labels=True).reset_index(drop=True).rename(columns={'SL.UEM.TOTL.ZS':'Unemployment'})
GDP_per_capita
wb.series.metadata.get('SP.DYN.LE00.IN')

Life_expectancy_at_birth = wb.data.DataFrame('SP.DYN.LE00.IN', economy=['COL','ARG','CHL','BRA', 'URY', 'BOL','PER','PRY','ECU','VEN','MEX','CAN','USA','CRI'], time= range(2002,2020), labels=True).reset_index(drop=True).rename(columns={'SL.UEM.TOTL.ZS':'Unemployment'})
Life_expectancy_at_birth
wb.series.metadata.get('SM.POP.NETM')

Migration= wb.data.DataFrame('SM.POP.NETM', economy=['COL','ARG','CHL','BRA', 'URY', 'BOL','PER','PRY','ECU','VEN','MEX','CAN','USA','CRI'], time= range(2002,2020), labels=True).reset_index(drop=True).rename(columns={'SL.UEM.TOTL.ZS':'Unemployment'})
Migration
wb.series.metadata.get('EG.ELC.ACCS.ZS')
Energy_access= wb.data.DataFrame('EG.ELC.ACCS.ZS', economy=['COL','ARG','CHL','BRA', 'URY', 'BOL','PER','PRY','ECU','VEN','MEX','CAN','USA','CRI'], time= range(2002,2020), labels=True).reset_index(drop=True).rename(columns={'SL.UEM.TOTL.ZS':'Unemployment'})
Energy_access
Energy_access.set_index('Country').unstack().reset_index()

Energy_access = Energy_access.set_index('Country').unstack().reset_index()
Total_unemployment.set_index('Country').unstack().reset_index()
Total_unemployment = Total_unemployment.set_index('Country').unstack().reset_index()
GDP_per_capita.set_index('Country').unstack().reset_index()

GDP_per_capita = GDP_per_capita.set_index('Country').unstack().reset_index()
Life_expectancy_at_birth.set_index('Country').unstack().reset_index()
Life_expectancy_at_birth = Life_expectancy_at_birth.set_index('Country').unstack().reset_index()
Migration.set_index('Country').unstack().reset_index()
Migration = Migration.set_index('Country').unstack().reset_index()
Migration.merge(Energy_access,on=['level_0','Country'],how='outer').merge(Life_expectancy_at_birth,on=['level_0','Country'],how='outer').merge(GDP_per_capita,on=['level_0','Country'],how='outer').merge(Total_unemployment,on=['level_0','Country'],how='outer')
Total = Migration.merge(Energy_access,on=['level_0','Country'],how='outer').merge(Life_expectancy_at_birth,on=['level_0','Country'],how='outer').merge(GDP_per_capita,on=['level_0','Country'],how='outer').merge(Total_unemployment,on=['level_0','Country'],how='outer')
Total.columns=["Years","Contry","Migration","Energy_access", "Life_expectancy","GDP_per_capita","Total_unemployment"]
