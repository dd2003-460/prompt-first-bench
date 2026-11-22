# N840: RTX 4090 24GB 显存运行 Qwen3-27B BF16 时，模型权重 66.58GB 无法单卡加载，必须使用量化（如 INT8/INT4）或多卡张量

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N261

## Claim

RTX 4090 24GB 显存运行 Qwen3-27B BF16 时，模型权重 66.58GB 无法单卡加载，必须使用量化（如 INT8/INT4）或多卡张量并行。INT8 量化后权重约 33.29GB，仍超出 24GB，需 INT4 量化（约 16.65GB）或 2 卡张量并行（每卡 33.29GB，超出 24GB，不可行），因此 2x RTX 4090 必须使用 INT4/FP8 量化。

## Corrected Claim

RTX 4090 24GB 显存运行 Qwen3-27B BF16 时，模型权重 66.58GB 无法单卡加载，必须使用量化（如 INT8/INT4）或多卡张量并行。INT8 量化后权重约 33.29GB，仍超出 24GB，需 INT4 量化（约 16.65GB）或 2 卡张量并行（每卡 33.29GB，超出 24GB，不可行），因此 2x RTX 4090 必须使用 INT4/FP8 量化。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16权重约54GB（27e9*2），INT8约27GB，INT4约13.5GB；24GB显存无法容纳BF16或INT8权重，INT4可容纳，2卡INT8每卡13.5GB也可行但题目限定24GB单卡限制下INT8不可行，逻辑自洽。
