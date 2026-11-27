# N109: KV Cache 精确计算：基于 N44 确认的参数，计算 BF16 下单 token KV 大小 = 2 * num_layers * num_kv_head

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

KV Cache 精确计算：基于 N44 确认的参数，计算 BF16 下单 token KV 大小 = 2 * num_layers * num_kv_heads * head_dim * 2 bytes，进而计算 32K 上下文总 KV 大小 = Token_KV_Size * 32768，并与 N31 中的 8GB 估算值对比，若偏差 >10%，需更新显存需求阈值 (N27)。

## Corrected Claim

KV Cache 精确计算：基于 N44 确认的参数，计算 BF16 下单 token KV 大小 = 2 * num_layers * num_kv_heads * head_dim * 2 bytes，进而计算 32K 上下文总 KV 大小 = Token_KV_Size * 32768，并与 N31 中的 8GB 估算值对比，若偏差 >10%，需更新显存需求阈值 (N27)。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算公式符合 Transformer 架构原理（Key/Value 各一份，BF16 为 2 字节），量级估算逻辑自洽。
