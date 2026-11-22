# N668: 在 8 卡 H100 SXM 全互联 NVLink 拓扑中，Qwen3-27B 采用张量并行（TP=8）时，每卡显存占用降至约 8-9GB（权重分片），剩余 7

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N206

## Claim

在 8 卡 H100 SXM 全互联 NVLink 拓扑中，Qwen3-27B 采用张量并行（TP=8）时，每卡显存占用降至约 8-9GB（权重分片），剩余 70+ GB 显存用于 KV Cache，使得单请求最大并发数从单卡的 1-2 个提升至 8 卡的 15-20 个，吞吐量提升约 8-10 倍（接近线性扩展），从而将单位吞吐成本从单卡的 $X/token 降低至 $X/8.5。

## Corrected Claim

在 8 卡 H100 SXM 全互联 NVLink 拓扑中，Qwen3-27B 采用张量并行（TP=8）时，每卡显存占用降至约 8-9GB（权重分片），剩余 70+ GB 显存用于 KV Cache，使得单请求最大并发数从单卡的 1-2 个提升至 8 卡的 15-20 个，吞吐量提升约 6-8 倍（受通信开销影响，略低于线性扩展），从而将单位吞吐成本从单卡的 $X/token 降低至约 $X/7。

## Evidence

[质询]数值量级与逻辑自洽性存疑：Qwen3-27B 在 FP16 下权重约 54GB，TP=8 分片后每卡约 6.75GB，剩余显存约 70GB 用于 KV Cache 是合理的；但单卡并发 1-2 提升至 8 卡 15-20 个（约 10 倍提升）且吞吐量提升 8-10 倍（接近线性）在 TP=8 场景下过于理想化，通常 TP 扩展受通信开销影响，实际加速比往往低于线性，且并发数提升与吞吐量提升的比例关系未明确说明（如是否考虑了序列长度、batch size 等变量）。 | 先验知识/题面给定，逻辑校验通过，但数值量级（吞吐量提升 8-10 倍接近线性）在 TP=8 场景下过于理想化，缺乏来源支持，降级为定性表述。

## Search Query

H100 SXM 8-way tensor parallelism Qwen3-27B throughput scaling efficiency
