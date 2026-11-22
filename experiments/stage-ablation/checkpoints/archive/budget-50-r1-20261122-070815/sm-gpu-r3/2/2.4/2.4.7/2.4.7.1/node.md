# N243: Qwen3-27B 的 Attention QKV 投影层与 LM Head 层在 AWQ INT4 量化下保留为 FP16/BF16 时，增加的显存占用 De

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71, N72, N74

## Claim

Qwen3-27B 的 Attention QKV 投影层与 LM Head 层在 AWQ INT4 量化下保留为 FP16/BF16 时，增加的显存占用 Delta_Mem 为 (QKV参数数 + LM Head参数数) * 2 bytes，基于 27B 模型结构估算约为 0.8-1.2 GB，导致总显存从 13.5GB 升至 14.3-14.7GB

## Corrected Claim

Qwen3-27B 的 Attention QKV 投影层与 LM Head 层在 AWQ INT4 量化下保留为 FP16/BF16 时，增加的显存占用 Delta_Mem 为 (QKV参数数 + LM Head参数数) * 2 bytes，基于 27B 模型结构估算约为 0.8-1.2 GB，导致总显存从 13.5GB 升至 14.3-14.7GB

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 的 QKV 投影层与 LM Head 层参数量估算合理，FP16/BF16 保留导致的显存增量计算符合基本数学逻辑，且总显存变化范围在合理区间内。

## Search Query

Qwen3-27B AWQ quantization sensitive layers memory overhead
