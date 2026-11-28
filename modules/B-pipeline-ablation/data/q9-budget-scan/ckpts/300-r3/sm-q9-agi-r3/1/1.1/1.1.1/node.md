# N36: vLLM 默认预留 GPU 显存的 20% (即 4x16GB * 0.2 = 12.8GB) 作为碎片安全区 (Safety Margin)，不计入 KV C

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

vLLM 默认预留 GPU 显存的 20% (即 4x16GB * 0.2 = 12.8GB) 作为碎片安全区 (Safety Margin)，不计入 KV Cache 池

## Corrected Claim

vLLM 默认预留 GPU 显存的 20% (即 4x16GB * 0.2 = 12.8GB) 作为碎片安全区 (Safety Margin)，不计入 KV Cache 池

## Evidence

先验知识/题面给定，逻辑校验通过
