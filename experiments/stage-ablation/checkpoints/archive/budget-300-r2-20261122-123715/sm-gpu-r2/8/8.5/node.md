# N111: RTX 4090 24GB 在 BF16 精度下无法直接加载 Qwen3-27B 权重 (54GB)，即使 GQA 降低 KV Cache 需求，权重本身已超显

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26, N27

## Claim

RTX 4090 24GB 在 BF16 精度下无法直接加载 Qwen3-27B 权重 (54GB)，即使 GQA 降低 KV Cache 需求，权重本身已超显存，因此 N26 中'24GB 显卡在 BF16 下即可运行'的结论不成立，需修正为量化精度下的可行性

## Corrected Claim

RTX 4090 24GB 在 BF16 精度下无法直接加载 Qwen3-27B 权重 (54GB)，即使 GQA 降低 KV Cache 需求，权重本身已超显存，因此 N26 中'24GB 显卡在 BF16 下即可运行'的结论不成立，需修正为量化精度下的可行性

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数模型在BF16下权重占用约54GB，远超24GB显存，物理上无法加载，结论自洽。
