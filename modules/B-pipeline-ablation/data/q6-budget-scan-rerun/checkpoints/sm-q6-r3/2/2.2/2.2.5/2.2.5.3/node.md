# N200: 入向带宽对P99延迟的隐性影响：若入向带宽不足导致上传队列堆积，Origin_Upload_Latency增加，进而影响新内容缓存预热时间（Cache_Warm

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

入向带宽对P99延迟的隐性影响：若入向带宽不足导致上传队列堆积，Origin_Upload_Latency增加，进而影响新内容缓存预热时间（Cache_Warmup_Time），间接推高故障恢复期间的P99延迟；量化为Inbound_Queue_Delay = Upload_Queue_Size / Inbound_Bandwidth_Capacity

## Corrected Claim

入向带宽对P99延迟的隐性影响：若入向带宽不足导致上传队列堆积，Origin_Upload_Latency增加，进而影响新内容缓存预热时间（Cache_Warmup_Time），间接推高故障恢复期间的P99延迟；量化为Inbound_Queue_Delay = Upload_Queue_Size / Inbound_Bandwidth_Capacity

## Evidence

先验知识/题面给定，逻辑校验通过：排队论基本公式（延迟=队列长度/服务速率）及网络带宽对上传延迟的影响符合物理直觉与工程常识。
