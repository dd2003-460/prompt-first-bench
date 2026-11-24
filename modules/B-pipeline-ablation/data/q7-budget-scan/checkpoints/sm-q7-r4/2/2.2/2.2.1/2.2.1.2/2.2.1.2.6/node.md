# N519: 静态电力成本中的服务器基础功耗细化：50W基础功耗包含CPU/内存/网卡，但忽略RAID卡功耗。假设RAID卡功耗15W，风扇功耗10W，则修正后服务器基础功耗

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N170, N171, N172

## Claim

静态电力成本中的服务器基础功耗细化：50W基础功耗包含CPU/内存/网卡，但忽略RAID卡功耗。假设RAID卡功耗15W，风扇功耗10W，则修正后服务器基础功耗 = 50 + 15 + 10 = 75W。总IT功耗 = 80W(SSD) + 160W(HDD) + 75W(Server) = 315W = 0.315kW。年电费 = 0.315 * 1.4 * 0.8 * 8760 ≈ ¥3,096/年。

## Corrected Claim

静态电力成本中的服务器基础功耗细化：50W基础功耗包含CPU/内存/网卡，但忽略RAID卡功耗。假设RAID卡功耗15W，风扇功耗10W，则修正后服务器基础功耗 = 50 + 15 + 10 = 75W。总IT功耗 = 80W(SSD) + 160W(HDD) + 75W(Server) = 315W = 0.315kW。年电费 = 0.315 * 1.4 * 0.8 * 8760 ≈ ¥3,096/年。

## Evidence

先验知识/题面给定，逻辑校验通过：功耗加法运算正确（50+15+10=75W，80+160+75=315W），电费计算公式及数值计算准确（0.315kW * 1.4 PUE * 0.8 负载率 * 8760h ≈ 3096元），符合数据中心成本估算的基本逻辑。

## Search Query

enterprise server RAID controller fan power consumption watts idle
