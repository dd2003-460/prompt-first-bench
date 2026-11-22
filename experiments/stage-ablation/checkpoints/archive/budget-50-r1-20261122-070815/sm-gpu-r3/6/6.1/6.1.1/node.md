# N361: 基于 config.json 确认的参数，Qwen3-27B 的 GQA 组数 G = num_attention_heads / num_key_value_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N127

## Claim

基于 config.json 确认的参数，Qwen3-27B 的 GQA 组数 G = num_attention_heads / num_key_value_heads = 32 / 4 = 8，该比例决定了 KV Cache 的压缩因子，需验证此计算是否与模型文档中描述的 'Grouped Query Attention' 配置一致。

## Corrected Claim

基于 config.json 确认的参数，Qwen3-27B 的 GQA 组数 G = num_attention_heads / num_key_value_heads = 32 / 4 = 8，该比例决定了 KV Cache 的压缩因子，需验证此计算是否与模型文档中描述的 'Grouped Query Attention' 配置一致。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 确实采用 GQA 机制，且 num_attention_heads=32, num_key_value_heads=4，计算 G=8 符合数学逻辑及模型架构常识。
