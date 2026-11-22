# N821: 4x RTX 4090 方案的真实吞吐估算：受限于 PCIe 4.0 x16 带宽 (32GB/s) 和 NVLink 缺失，TP=4 的通信开销显著。参考 v

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N254, N255, N256

## Claim

4x RTX 4090 方案的真实吞吐估算：受限于 PCIe 4.0 x16 带宽 (32GB/s) 和 NVLink 缺失，TP=4 的通信开销显著。参考 vLLM 基准，4x 4090 FP16 Qwen3-27B 单流吞吐约 35-45 tok/s，远低于 2x 4090 INT4 (74.6 tok/s) 的 2 倍线性预期。修正 N254 结论：4x 4090 并非‘性能更低’，而是‘单位成本吞吐更低’。

## Corrected Claim

4x RTX 4090 方案受限于 PCIe 4.0 带宽和 NVLink 缺失，TP=4 通信开销显著，导致其单位成本吞吐低于 2x 4090 INT4 方案的线性预期，具体吞吐数值需实测确认。

## Evidence

[质询]该陈述包含具体的经验性性能数据（35-45 tok/s, 74.6 tok/s）和硬件配置细节，属于经验事实。由于检索失败，无法验证这些具体数值的准确性，且不同硬件拓扑（如PCIe拓扑、驱动版本）可能导致显著差异，存在数值偏差风险。 | 经验事实，逻辑自洽但缺来源支持。虽然4x 4090因缺乏NVLink导致TP通信开销大、单位成本效率低这一逻辑符合硬件常识，但具体吞吐数值无法通过第一性原理推导，且无外部来源佐证。

## Search Query

vLLM 4x RTX 4090 Qwen3-27B FP16 throughput tok/s benchmark
