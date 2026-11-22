# N472: 基于Head Parallelism策略，每步Decode的通信延迟计算公式为：Latency_comm = Size_KV / Effective_Bandw

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N149

## Claim

基于Head Parallelism策略，每步Decode的通信延迟计算公式为：Latency_comm = Size_KV / Effective_Bandwidth。若有效带宽为 20 GB/s，传输 1.07 GB 数据所需延迟约为 53.5 ms；若有效带宽为 15 GB/s，延迟约为 71.3 ms。此延迟需与单卡计算延迟（通常 <5ms/step for 27B）对比以评估瓶颈。

## Corrected Claim

基于Head Parallelism策略，每步Decode的通信延迟计算公式为：Latency_comm = Size_KV / Effective_Bandwidth。若有效带宽为 20 GB/s，传输 1.07 GB 数据所需延迟约为 53.5 ms；若有效带宽为 15 GB/s，延迟约为 71.3 ms。此延迟需与单卡计算延迟（通常 <5ms/step for 27B）对比以评估瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：1.07GB/20GB/s=53.5ms，1.07GB/15GB/s≈71.3ms，计算准确；27B模型单步计算延迟<5ms符合工程常识，通信延迟显著高于计算延迟的结论逻辑自洽。
