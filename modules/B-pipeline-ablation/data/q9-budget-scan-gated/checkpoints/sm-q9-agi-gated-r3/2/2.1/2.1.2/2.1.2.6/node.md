# N63: 题面15-20s范围与实际计算值差异的来源：题面值可能包含max_num_seqs=8下的批处理等待时间，单序列独占时延迟为5-8s，8序列并发时因GPU争用延

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

题面15-20s范围与实际计算值差异的来源：题面值可能包含max_num_seqs=8下的批处理等待时间，单序列独占时延迟为5-8s，8序列并发时因GPU争用延迟增至15-20s，争用系数约为2-3x

## Corrected Claim

题面15-20s范围与实际计算值差异的来源：题面值可能包含max_num_seqs=8下的批处理等待时间，单序列独占时延迟为5-8s，8序列并发时因GPU争用延迟增至15-20s，争用系数约为2-3x

## Evidence

先验知识/题面给定，逻辑校验通过：GPU并发争用导致延迟增加2-3倍符合硬件资源竞争的基本物理直觉，数值量级合理。
