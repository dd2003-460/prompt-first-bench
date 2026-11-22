# N43: 激活值缓冲（Activation Buffer）的大小与 Batch Size (B) 和序列长度 (S) 成正比，公式约为 B * S * hidden_si

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

激活值缓冲（Activation Buffer）的大小与 Batch Size (B) 和序列长度 (S) 成正比，公式约为 B * S * hidden_size * bytes_per_element * factor，其中 factor 取决于框架实现（vLLM/llama.cpp）和算子融合程度，对于 B=1, S=32K, hidden=4096, BF16，估算约为 0.5GB-1GB。

## Corrected Claim

激活值缓冲（Activation Buffer）的大小与 Batch Size (B) 和序列长度 (S) 成正比，基础计算约为 B * S * hidden_size * bytes_per_element。对于 B=1, S=32K, hidden=4096, BF16，单层基础激活值约为 256MB，实际框架中因多层结构和算子融合，总缓冲可能在 0.5GB-1GB 量级，具体数值取决于实现细节。

## Evidence

[质询]该陈述包含具体的经验性估算数值（0.5GB-1GB）和框架特定的实现细节（vLLM/llama.cpp的factor），属于经验事实而非第一性原理可严格推导的数学恒等式。虽然量级估算在逻辑上大致合理（1 * 32768 * 4096 * 2 bytes ≈ 256MB，若考虑多层或额外缓冲可能达到0.5-1GB），但缺乏具体来源支持确切的数值范围和框架差异系数。 | 经验事实，逻辑自洽但缺来源支持。计算基础：1 * 32768 * 4096 * 2 bytes = 268,435,456 bytes ≈ 256MB。考虑到Transformer模型中激活值通常涉及多个层或中间状态，0.5GB-1GB的估算在数量级上是合理的，但具体数值依赖于未提供的框架实现细节。

## Search Query

vLLM activation memory usage estimate batch size 1 sequence length 32k
