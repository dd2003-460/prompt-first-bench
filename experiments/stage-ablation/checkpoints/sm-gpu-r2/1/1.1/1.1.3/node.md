# N40: KV Cache 显存计算公式：KV_Size = 2 * L * H_kv * d * S * Bytes_Per_KV_Elem。其中 2 代表 K 和 V

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

KV Cache 显存计算公式：KV_Size = 2 * L * H_kv * d * S * Bytes_Per_KV_Elem。其中 2 代表 K 和 V，L=64, H_kv=8 (GQA), d=128, S=32768。

## Corrected Claim

KV Cache 显存计算公式：KV_Size = 2 * L * H_kv * d * S * Bytes_Per_KV_Elem。其中 2 代表 K 和 V，L=64, H_kv=8 (GQA), d=128, S=32768。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合Transformer KV Cache标准计算逻辑（2代表K/V，L为层数，H_kv为KV头数，d为头维度，S为序列长度，Bytes为数据类型大小），参数量级合理。

## Search Query

KV cache memory calculation formula LLM inference
