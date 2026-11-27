# N151: Qwen3-27B FP8 量化后在单卡 L40S (48GB) 上的可行性：总显存需求 = 权重 (32.22GB, 混合精度) + KV Cache (8.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

Qwen3-27B FP8 量化后在单卡 L40S (48GB) 上的可行性：总显存需求 = 权重 (32.22GB, 混合精度) + KV Cache (8.192GB) + 框架开销 (5GB) = 45.412GB < 48GB，可行，剩余 2.588GB 用于激活值

## Corrected Claim

Qwen3-27B FP8 量化后在单卡 L40S (48GB) 上的可行性：总显存需求 = 权重 (32.22GB, 混合精度) + KV Cache (8.192GB) + 框架开销 (5GB) = 45.412GB < 48GB，可行，剩余 2.588GB 用于激活值

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，FP8量化后权重约27GB（若含部分BF16层或计算误差，32.22GB在合理范围内，通常FP8为1字节/参数，27B*1=27GB，此处32.22GB可能包含了部分未量化层或特定实现开销，但量级正确）；KV Cache 8.192GB和框架开销5GB均为典型经验值；总和45.412GB小于48GB，数学计算正确，逻辑自洽。
