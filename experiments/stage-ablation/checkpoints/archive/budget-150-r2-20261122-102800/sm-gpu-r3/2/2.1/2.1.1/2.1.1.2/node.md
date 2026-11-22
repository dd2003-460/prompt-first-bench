# N210: Qwen3-27B 在 32K context 下的 KV Cache 大小计算：每层 KV Cache = 2 (K+V) * Hidden_Size (40

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75

## Claim

Qwen3-27B 在 32K context 下的 KV Cache 大小计算：每层 KV Cache = 2 (K+V) * Hidden_Size (4096) * Seq_Len (32768) * Bytes_Per_Elem (2 for BF16) * Num_Layers (48 for Qwen3-27B? 需确认层数，假设为 48) = 2 * 4096 * 32768 * 2 * 48 = 2.576 GB。若层数为 64，则 KV Cache ≈ 3.435 GB。总显存需求 = 权重 (54.36GB) + KV Cache (2.58-3.44GB) + 激活值 (~2-5GB) ≈ 59-63GB。此数值确认单卡 48GB (L40S) 和 24GB (RTX 3090/4090) 均无法容纳 BF16 全模型+KV Cache，必须量化或双卡。

## Corrected Claim

Qwen3-27B 在 32K context 下的 KV Cache 大小取决于具体层数（假设为 48 或 64 层），计算结果约为 2.58-3.44 GB。总显存需求约为 59-63GB，确认单卡 48GB 和 24GB 均无法容纳 BF16 全模型+KV Cache，必须量化或双卡。

## Evidence

[质询]Qwen3-27B 的具体架构参数（如层数、Hidden Size）属于经验事实，且当前检索无可用来源支持，无法确认层数是否为 48 或 64，导致 KV Cache 计算基于假设而非确证数据。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B KV cache size 32k context memory calculation
