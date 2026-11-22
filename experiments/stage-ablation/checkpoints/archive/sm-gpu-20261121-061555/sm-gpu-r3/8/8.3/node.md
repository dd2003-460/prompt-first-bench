# N125: Qwen3-27B 混合注意力架构中 Gated DeltaNet 层的线性注意力机制显存占用特性：其状态大小固定（不随 seq_len 线性增长），具体每层状

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35, N36, N37

## Claim

Qwen3-27B 混合注意力架构中 Gated DeltaNet 层的线性注意力机制显存占用特性：其状态大小固定（不随 seq_len 线性增长），具体每层状态大小约为 hidden_size * head_dim * num_states bytes，需从总 KV 预算中扣除或单独计算以修正 N38 的线性估算误差。

## Corrected Claim

Qwen3-27B 若采用混合注意力架构，其线性注意力层（如 Gated DeltaNet）的状态大小通常固定，不随 seq_len 线性增长，具体大小取决于模型超参数（如 hidden_size, head_dim 等），需从总 KV 预算中单独计算以修正线性估算误差。

## Evidence

[质询]具体数值公式（hidden_size * head_dim * num_states）及“Qwen3-27B”的具体架构细节属于经验事实，且当前检索无可用来源支持，无法确认该特定模型是否确实采用此架构及该精确的状态大小公式。 | 经验事实，逻辑自洽（线性注意力状态固定是理论特性）但缺来源支持，且具体模型参数无法验证。

## Search Query

Gated DeltaNet linear attention memory footprint per layer fixed size
