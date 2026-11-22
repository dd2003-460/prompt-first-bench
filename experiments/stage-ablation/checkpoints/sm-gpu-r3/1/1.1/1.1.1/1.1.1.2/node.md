# N140: BF16 权重文件大小计算修正：若参数量为 27.1B，则 27.1e9 * 2 bytes = 54.2 GB；需验证 Qwen3-27B 是否采用混合精度训

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

BF16 权重文件大小计算修正：若参数量为 27.1B，则 27.1e9 * 2 bytes = 54.2 GB；需验证 Qwen3-27B 是否采用混合精度训练（如 Attention 部分为 FP32 或某些层为 INT8），若存在混合精度，实际权重文件大小将偏离纯 BF16 理论值

## Corrected Claim

BF16 权重文件大小计算修正：若参数量为 27.1B，则 27.1e9 * 2 bytes = 54.2 GB；需验证 Qwen3-27B 是否采用混合精度训练（如 Attention 部分为 FP32 或某些层为 INT8），若存在混合精度，实际权重文件大小将偏离纯 BF16 理论值

## Evidence

先验知识/题面给定，逻辑校验通过：27.1e9 * 2 bytes = 54.2 GB 计算正确，且关于混合精度可能影响文件大小的陈述符合工程常识。
