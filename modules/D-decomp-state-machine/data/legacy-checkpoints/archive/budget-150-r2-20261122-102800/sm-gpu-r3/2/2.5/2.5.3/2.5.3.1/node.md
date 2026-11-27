# N239: N87 声称 A6000 方案‘避免多卡间 KV Cache 同步的通信开销’是错误的：TP=2 下 KV Cache 仍需分片同步，通信量与 2×4090 相

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N87

## Claim

N87 声称 A6000 方案‘避免多卡间 KV Cache 同步的通信开销’是错误的：TP=2 下 KV Cache 仍需分片同步，通信量与 2×4090 相同（参考 N130），但 A6000 的 NVLink 带宽（600GB/s）远高于 PCIe 4.0（64GB/s），通信延迟降至 0.87ms/step，开销占比仅 1.1-1.7%，显著低于 2×4090 的 11.4-21.4%。

## Corrected Claim

N87 声称 A6000 方案‘避免多卡间 KV Cache 同步的通信开销’是错误的：TP=2 下 KV Cache 仍需分片同步，通信量与 2×4090 相同（参考 N130），但 A6000 的 NVLink 带宽远高于 PCIe 4.0，通信延迟显著降低，开销占比显著低于 2×4090。

## Evidence

[质询]该陈述包含大量具体的经验性数值（如NVLink带宽600GB/s、PCIe 4.0带宽64GB/s、通信延迟0.87ms、开销占比1.1-1.7% vs 11.4-21.4%），这些具体参数和计算结果属于经验事实，无法仅从第一性原理推导得出，且当前无可用外部来源支持这些具体数值的准确性。 | 逻辑上，NVLink带宽远高于PCIe是已知事实，因此通信开销更低符合物理直觉；但具体数值（如0.87ms, 1.1-1.7%）属于经验事实，缺乏来源支持，故降级。

## Search Query

A6000 NVLink bandwidth GB/s TP=2 communication latency
