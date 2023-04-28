import pandas as pd
import os

basins = pd.read_csv("/content/grdc_points_assigned.csv")

Africa_1 = basins[basins['HYBAS_ID']==1020000010]
Africa_2 = basins[basins['HYBAS_ID']==1020011530]
Africa_3 = basins[basins['HYBAS_ID']==1020018110]
Africa_4 = basins[basins['HYBAS_ID']==1020021940]
Africa_5 = basins[basins['HYBAS_ID']==1020027430]
Africa_6 = basins[basins['HYBAS_ID']==1020034170]
Africa_7 = basins[basins['HYBAS_ID']==1020035180]
Africa_8 = basins[basins['HYBAS_ID']==1020040190]
Europe_1 = basins[basins['HYBAS_ID']==2020000010]
Europe_2 = basins[basins['HYBAS_ID']==2020003440]
Europe_3 = basins[basins['HYBAS_ID']==2020018240]
Europe_4 = basins[basins['HYBAS_ID']==2020024230]
Europe_5 = basins[basins['HYBAS_ID']==2020033490]
Europe_6 = basins[basins['HYBAS_ID']==2020041390]
Europe_7 = basins[basins['HYBAS_ID']==2020057170]
Europe_8 = basins[basins['HYBAS_ID']==2020065840]
Europe_9 = basins[basins['HYBAS_ID']==2020071190]
Siberia_1 = basins[basins['HYBAS_ID']==3020000010]
Siberia_2 = basins[basins['HYBAS_ID']==3020003790]
Siberia_3 = basins[basins['HYBAS_ID']==3020005240]
Siberia_4 = basins[basins['HYBAS_ID']==3020008670]
Siberia_5 = basins[basins['HYBAS_ID']==3020009320]
Siberia_6 = basins[basins['HYBAS_ID']==3020024310]
Asia_1 = basins[basins['HYBAS_ID']==4020000010]
Asia_2 = basins[basins['HYBAS_ID']==4020006940]
Asia_3 = basins[basins['HYBAS_ID']==4020015090]
Asia_4 = basins[basins['HYBAS_ID']==4020024190]
Asia_5 = basins[basins['HYBAS_ID']==4020034510]
Asia_6 = basins[basins['HYBAS_ID']==4020050210]
Asia_7 = basins[basins['HYBAS_ID']==4020050220]
Asia_8 = basins[basins['HYBAS_ID']==4020050290]
Asia_9 = basins[basins['HYBAS_ID']==4020050470]
Australia_1 = basins[basins['HYBAS_ID']==5020000010]
Australia_2 = basins[basins['HYBAS_ID']==5020015660]
Australia_3 = basins[basins['HYBAS_ID']==5020037270]
Australia_4 = basins[basins['HYBAS_ID']==5020049720]
Australia_5 = basins[basins['HYBAS_ID']==5020054880]
Australia_6 = basins[basins['HYBAS_ID']==5020055870]
Australia_7 = basins[basins['HYBAS_ID']==5020082270]
South_America_1 = basins[basins['HYBAS_ID']==6020000010]
South_America_2= basins[basins['HYBAS_ID']==6020006540]
South_America_3 = basins[basins['HYBAS_ID']==6020008320]
South_America_4 = basins[basins['HYBAS_ID']==6020014330]
South_America_5 = basins[basins['HYBAS_ID']==6020017370]
South_America_6 = basins[basins['HYBAS_ID']==6020021870]
South_America_7 = basins[basins['HYBAS_ID']==6020029280]
North_America_1 = basins[basins['HYBAS_ID']==7020000010]
North_America_2 = basins[basins['HYBAS_ID']==7020014250]
North_America_3 = basins[basins['HYBAS_ID']==7020021430]
North_America_4 = basins[basins['HYBAS_ID']==7020024600]
North_America_5 = basins[basins['HYBAS_ID']==7020038340]
North_America_6 = basins[basins['HYBAS_ID']==7020046750]
North_America_7 = basins[basins['HYBAS_ID']==7020047840]
North_America_8 = basins[basins['HYBAS_ID']==7020065090]
Artic_1 = basins[basins['HYBAS_ID']==8020000010]
Artic_2 = basins[basins['HYBAS_ID']==8020008900]
Artic_3 = basins[basins['HYBAS_ID']==8020010700]
Artic_4 = basins[basins['HYBAS_ID']==8020020760]
Artic_5 = basins[basins['HYBAS_ID']==8020022890]
Artic_6 = basins[basins['HYBAS_ID']==8020032840]
Artic_7 = basins[basins['HYBAS_ID']==8020044560]
Greenland = basins[basins['HYBAS_ID']==9020000010]

Africa_1.to_csv("/content/basins/1020000010.csv")
Africa_2.to_csv("/content/basins/1020011530.csv")
Africa_3.to_csv("/content/basins/1020018110.csv")
Africa_4.to_csv("/content/basins/1020021940.csv")
Africa_5.to_csv("/content/basins/1020027430.csv")
Africa_6.to_csv("/content/basins/1020034170.csv")
Africa_7.to_csv("/content/basins/1020035180.csv")
Africa_8.to_csv("/content/basins/1020040190.csv")
Europe_1.to_csv("/content/basins/2020000010.csv")
Europe_2.to_csv("/content/basins/2020003440.csv")
Europe_3.to_csv("/content/basins/2020018240.csv")
Europe_4.to_csv("/content/basins/2020024230.csv")
Europe_5.to_csv("/content/basins/2020033490.csv")
Europe_6.to_csv("/content/basins/2020041390.csv")
Europe_7.to_csv("/content/basins/2020057170.csv")
Europe_8.to_csv("/content/basins/2020065840.csv")
Europe_9.to_csv("/content/basins/2020071190.csv")
Siberia_1.to_csv("/content/basins/3020000010.csv")
Siberia_2.to_csv("/content/basins/3020003790.csv")
Siberia_3.to_csv("/content/basins/3020005240.csv")
Siberia_4.to_csv("/content/basins/3020008670.csv")
Siberia_5.to_csv("/content/basins/3020009320.csv")
Siberia_6.to_csv("/content/basins/3020024310.csv")
Asia_1.to_csv("/content/basins/4020000010.csv")
Asia_2.to_csv("/content/basins/4020006940.csv")
Asia_3.to_csv("/content/basins/4020015090.csv")
Asia_4.to_csv("/content/basins/4020024190.csv")
Asia_5.to_csv("/content/basins/4020034510.csv")
Asia_6.to_csv("/content/basins/4020050210.csv")
Asia_7.to_csv("/content/basins/4020050220.csv")
Asia_8.to_csv("/content/basins/4020050290.csv")
Asia_9.to_csv("/content/basins/4020050470.csv")
Australia_1.to_csv("/content/basins/5020000010.csv")
Australia_2.to_csv("/content/basins/5020015660.csv")
Australia_3.to_csv("/content/basins/5020037270.csv")
Australia_4.to_csv("/content/basins/5020049720.csv")
Australia_5.to_csv("/content/basins/5020054880.csv")
Australia_6.to_csv("/content/basins/5020055870.csv")
Australia_7.to_csv("/content/basins/5020082270.csv")
South_America_1.to_csv("/content/basins/6020000010.csv")
South_America_2.to_csv("/content/basins/6020006540.csv")
South_America_3.to_csv("/content/basins/6020008320.csv")
South_America_4.to_csv("/content/basins/6020014330.csv")
South_America_5.to_csv("/content/basins/6020017370.csv")
South_America_6.to_csv("/content/basins/6020021870.csv")
South_America_7.to_csv("/content/basins/6020029280.csv")
North_America_1.to_csv("/content/basins/7020000010.csv")
North_America_2.to_csv("/content/basins/7020014250.csv")
North_America_3.to_csv("/content/basins/7020021430.csv")
North_America_4.to_csv("/content/basins/7020024600.csv")
North_America_5.to_csv("/content/basins/7020038340.csv")
North_America_6.to_csv("/content/basins/7020046750.csv")
North_America_7.to_csv("/content/basins/7020047840.csv")
North_America_8.to_csv("/content/basins/7020065090.csv")
Artic_1.to_csv("/content/basins/8020000010.csv")
Artic_2.to_csv("/content/basins/8020008900.csv")
Artic_3.to_csv("/content/basins/8020010700.csv")
Artic_4.to_csv("/content/basins/8020020760.csv")
Artic_5.to_csv("/content/basins/8020022890.csv")
Artic_6.to_csv("/content/basins/8020032840.csv")
Artic_7.to_csv("/content/basins/8020044560.csv")
Greenland.to_csv("/content/basins/9020000010.csv")

