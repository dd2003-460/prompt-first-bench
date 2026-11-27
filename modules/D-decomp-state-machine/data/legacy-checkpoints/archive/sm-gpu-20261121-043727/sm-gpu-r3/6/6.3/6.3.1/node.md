# N235: Intel Max 1550 运行 Qwen3-27B BF16 时的显存可行性判定：权重体积 (27.2B * 2 bytes = 54.4 GB) 大于 M

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

Intel Max 1550 运行 Qwen3-27B BF16 时的显存可行性判定：权重体积 (27.2B * 2 bytes = 54.4 GB) 大于 Max 1550 显存容量 (48 GB)，因此 BF16 精度下该硬件方案物理不可行，必须降级至 INT8 (27.2 GB) 或 INT4 (13.6 GB) 才能加载模型

## Corrected Claim

Intel Max 1550 运行 Qwen3-27B BF16 时的显存可行性判定：权重体积 (27.2B * 2 bytes = 54.4 GB) 大于 Max 1550 显存容量 (48 GB)，因此 BF16 精度下该硬件方案物理不可行，必须降级至 INT8 (27.2 GB) 或 INT4 (13.6 GB) 才能加载模型

## Evidence

先验知识/题面给定，逻辑校验通过：27.2B参数在BF16下占用54.4GB显存，确实超过Intel Max 1550的48GB显存容量，物理上不可行；INT8/INT4量化后的体积（27.2GB/13.6GB）在48GB范围内，逻辑自洽。
