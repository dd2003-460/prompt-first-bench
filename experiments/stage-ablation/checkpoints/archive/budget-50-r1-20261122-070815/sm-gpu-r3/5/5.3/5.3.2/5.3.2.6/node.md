# N359: Qwen3-27B 在 A100 80GB (Ampere) 上，当 Batch Size 从 1 增加到 16/32 时，BF16 精度下的总吞吐量（toke

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N126

## Claim

Qwen3-27B 在 A100 80GB (Ampere) 上，当 Batch Size 从 1 增加到 16/32 时，BF16 精度下的总吞吐量（tokens/s）及单用户延迟增加百分比，用于评估高带宽内存（HBM）在并发场景下的优势。

## Corrected Claim

Qwen3-27B 在 A100 80GB (Ampere) 上，当 Batch Size 从 1 增加到 16/32 时，BF16 精度下的总吞吐量（tokens/s）通常呈非线性增长，单用户延迟显著增加，具体数值需实测获取。

## Evidence

[质询]该陈述包含具体的经验性性能数据（吞吐量数值及延迟增加百分比），属于硬件与模型交互的经验事实，无法从第一性原理推导，且缺乏具体数值支撑，仅凭逻辑无法确定具体量级。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值）

## Search Query

Qwen3-27B vLLM A100 batch size 16 32 throughput latency
