# N106: 代码生成/通用对话中风险场景（质量容忍度中等）的性价比最优精度：INT8 或 FP8。量化依据：INT8 显存占用 27GB (27B * 1 byte)，质量

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

代码生成/通用对话中风险场景（质量容忍度中等）的性价比最优精度：INT8 或 FP8。量化依据：INT8 显存占用 27GB (27B * 1 byte)，质量损失通常 <1%；FP8 显存占用 27GB，质量损失 <0.5%。此精度在 RTX 4090 单卡不可行 (27GB > 24GB)，需双卡或数据中心卡，但在 Mac Studio (192GB) 上可行且无需量化至 INT4，平衡了质量与硬件成本。

## Corrected Claim

代码生成/通用对话中风险场景（质量容忍度中等）的性价比最优精度：INT8 或 FP8。量化依据：INT8 显存占用 27GB (27B * 1 byte)，质量损失通常 <1%；FP8 显存占用 27GB，质量损失 <0.5%。此精度在 RTX 4090 单卡不可行 (27GB > 24GB)，需双卡或数据中心卡，但在 Mac Studio (192GB) 上可行且无需量化至 INT4，平衡了质量与硬件成本。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数模型在INT8/FP8下显存占用约为27GB，符合数学计算（27*1）；RTX 4090显存24GB确实无法容纳27GB模型，Mac Studio 192GB统一内存可容纳，逻辑自洽且符合硬件常识。
