# N49: 用户指定研究方向关键词 (≤ 200 tokens) 的嵌入表示需与 SOTA 摘要和失败实验列表进行余弦相似度计算，若相似度 < 0.6，则提示用户补充更多背

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

用户指定研究方向关键词 (≤ 200 tokens) 的嵌入表示需与 SOTA 摘要和失败实验列表进行余弦相似度计算，若相似度 < 0.6，则提示用户补充更多背景信息，以减少因指令模糊导致的无效推理。

## Corrected Claim

用户指定研究方向关键词 (≤ 200 tokens) 的嵌入表示需与 SOTA 摘要和失败实验列表进行余弦相似度计算，若相似度 < 0.6，则提示用户补充更多背景信息，以减少因指令模糊导致的无效推理。

## Evidence

先验知识/题面给定，逻辑校验通过
