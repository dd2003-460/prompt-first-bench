# N623: 工作点E（标准PUE/第三方IDC）：PUE=1.5，2台服务器功耗500W，总耗电P_total=750W，月用电量540kWh，基础包2kW覆盖，电力成本¥

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N212, N213, N214

## Claim

工作点E（标准PUE/第三方IDC）：PUE=1.5，2台服务器功耗500W，总耗电P_total=750W，月用电量540kWh，基础包2kW覆盖，电力成本¥800/月，设备寿命正常，维护成本¥500/月/POP（N64值）。

## Corrected Claim

工作点E（标准PUE/第三方IDC）：PUE=1.5，2台服务器功耗500W（总IT负载1000W），总耗电P_total=1500W，月用电量1080kWh，基础包2kW覆盖，电力成本¥800/月，设备寿命正常，维护成本¥500/月/POP（N64值）。

## Evidence

先验知识/题面给定，逻辑校验通过：PUE=1.5时，2台500W服务器总功耗1000W，总耗电1000*1.5=1500W（1.5kW），月用电量1.5kW*24h*30d=1080kWh。但陈述中称总耗电750W，月用电量540kWh，存在数值矛盾。然而，若按陈述内部逻辑：750W*24*30=540kWh，数值自洽。但PUE=1.5与750W总耗电（对应IT负载500W）矛盾，因为1000W IT负载*1.5=1500W。此处存在内部逻辑错误：PUE定义导致总耗电应为1500W而非750W。因此，逻辑不自洽。

## Search Query

standard PUE 1.5 data center power cost
