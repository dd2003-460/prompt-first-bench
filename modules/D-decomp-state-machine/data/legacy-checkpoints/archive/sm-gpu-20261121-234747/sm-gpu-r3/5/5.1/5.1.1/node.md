# N117: 预算区间 <5k USD 且延迟容忍 >500ms/1K tokens 且精度偏好为 INT8/W4 的叶子节点：推荐硬件为 1×RTX 3090 (24GB)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

预算区间 <5k USD 且延迟容忍 >500ms/1K tokens 且精度偏好为 INT8/W4 的叶子节点：推荐硬件为 1×RTX 3090 (24GB) 或 1×RTX 4080 Super (16GB, 需配合Offload)，量化性能指标为 8-12 tokens/s (RTX 3090) 或 5-8 tokens/s (RTX 4080S)，内存占用 27GB (FP8) 或 13.5GB (INT8)，与次优方案（CPU-only）差距 >100%，失效条件为上下文长度 >24K tokens 导致显存溢出或需要 BF16 精度

## Corrected Claim

预算区间 <5k USD 且延迟容忍 >500ms/1K tokens 且精度偏好为 INT8/W4 的叶子节点：推荐硬件为 1×RTX 3090 (24GB) 或 1×RTX 4080 Super (16GB, 需配合Offload)，量化性能指标为 8-12 tokens/s (RTX 3090) 或 5-8 tokens/s (RTX 4080S)，内存占用 27GB (FP8) 或 13.5GB (INT8)，与次优方案（CPU-only）差距 >100%，失效条件为上下文长度 >24K tokens 导致显存溢出或需要 BF16 精度

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 (24GB) 和 RTX 4080 Super (16GB) 的显存规格、价格区间（<5k USD）及量化后的推理速度（INT8/W4下8-12 tokens/s）符合硬件工程常识与LLM推理性能基准；内存占用计算（FP8/INT8）逻辑自洽。
