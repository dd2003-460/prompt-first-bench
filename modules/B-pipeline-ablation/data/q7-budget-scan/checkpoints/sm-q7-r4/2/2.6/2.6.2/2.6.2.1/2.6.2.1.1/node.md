# N604: 混合架构(200TB SSD+300TB HDD)的5年TBW验证：SSD层500TB? 不，是200TB SSD。假设温数据100TB(20%)全放SSD，冷

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N205

## Claim

混合架构(200TB SSD+300TB HDD)的5年TBW验证：SSD层500TB? 不，是200TB SSD。假设温数据100TB(20%)全放SSD，冷数据100TB冗余或热点放SSD? 题目说200TB SSD。假设100TB温数据+100TB热点/缓存。SSD层年写入=200TB*365*1.5(DWF, 因缓存命中率高可能有更多写入)=109,500TB。5年=547,500TB。盘数=200/2=100块。单盘TBW=547,500/100=5,475TB。DWPD=3.0时单盘容量=2TB*3*365*5=10,950TB。安全边际充足。HDD层300TB无TBW限制，仅关注机械寿命（通常>5年）。

## Corrected Claim

混合架构(200TB SSD+300TB HDD)的5年TBW验证需基于实际数据驻留时间计算写入量。若假设温数据平均驻留时间为T天，则年写入量约为(100TB/T)*365*DWF，而非简单的200TB*365*DWF。需根据具体业务场景确定T值后重新计算单盘TBW以验证安全性。

## Evidence

[质询]SSD层年写入量的计算逻辑存在严重缺陷：将总容量(200TB)乘以天数和DWF作为年写入量，隐含假设所有SSD空间每天都被完整重写一次，这忽略了数据驻留时间（Residency Time）和实际工作负载分布。对于温数据（通常驻留数天至数周），年写入量远低于容量*365*DWF，该估算极大概率高估了写入压力，导致后续TBW验证基于错误前提。 | 逻辑校验发现核心计算公式（年写入=总容量*365*DWF）违背存储系统基本工作原理，未考虑数据驻留时间，导致写入量估算失真；虽source为knowledge，但存在可信攻击点且无法排除，故降级。

## Search Query

Hybrid storage SSD cache write amplification factor 1.5
