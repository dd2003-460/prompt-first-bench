# N528: NVLink 4.0 (H100) 的 P2P 通信固定启动延迟约为 2-4 µs，相比 PCIe 4.0 降低约 50-70%；在 8KB 小包通信中，NVL

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N217

## Claim

NVLink 4.0 (H100) 的 P2P 通信固定启动延迟约为 2-4 µs，相比 PCIe 4.0 降低约 50-70%；在 8KB 小包通信中，NVLink 的固定延迟占比降至 10-20%，主要瓶颈转移至带宽限制而非延迟。

## Corrected Claim

NVLink 4.0 (H100) 的 P2P 通信启动延迟显著低于 PCIe 4.0（通常降低 50% 以上）；在 8KB 小包通信中，NVLink 的延迟占比相对较小，性能瓶颈主要受带宽限制影响。

## Evidence

[质询]具体数值（2-4 µs, 50-70%, 10-20%）属于经验测量数据，缺乏公开权威基准测试的直接支持，且不同负载和驱动版本下波动较大，固定值表述过于绝对。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

NVLink 4.0 fixed latency vs PCIe 4.0 small packet overhead benchmark
