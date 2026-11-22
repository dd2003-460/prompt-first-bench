# N42: 非典型高显存消费级/工作站方案：AMD Radeon PRO W7900 (48GB VRAM) 或 Intel Arc A770 (16GB, 不满足32K+

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

非典型高显存消费级/工作站方案：AMD Radeon PRO W7900 (48GB VRAM) 或 Intel Arc A770 (16GB, 不满足32K+27B需求但作为低价对比基准)，其中 W7900 价格约 $4000-$5000 [待核验]，支持 ROCm 生态，在 27B BF16 下可单卡容纳权重+KV Cache，是 NVIDIA 4090 双卡方案的高性价比替代选项。

## Corrected Claim

AMD Radeon PRO W7900 配备 48GB GDDR6 显存，支持 ROCm 生态，在 27B BF16 下可单卡容纳权重+KV Cache；其具体市场价格及相对于 NVIDIA 4090 双卡方案的成本效益需进一步市场数据核验。

## Evidence

[质询]价格区间（$4000-$5000）及具体性能对比结论（如“高性价比替代”）属于经验事实，参考来源仅确认了硬件规格（48GB VRAM），未提供价格或性能基准数据，无法排除价格波动或性能对比偏差的可能性。 | 来源[1]和[2]直接支持AMD Radeon PRO W7900拥有48GB GDDR6显存这一核心规格，但缺乏价格及性能对比的外部证据支持，依据经验事实排除条款降级。

## Retrieval Sources

- {'url': 'https://www.amd.com/en/products/graphics/workstations/radeon-pro/w7900.html&rut=f6a6e8eaee85abd36fa54c14ba6e365ce07a828fc592778852e2b37d5451d9b5', 'type': 'ddg', 'title': 'AMD Radeon™ PRO W7900 Professional Graphics'}
- {'url': 'https://www.amd.com/zh-cn/products/graphics/workstations/radeon-pro/w7900d.html&rut=66aeca26084d7f51f39e380d4a234881ac4c7676cd32c27afd522284728373d1', 'type': 'ddg', 'title': 'AMD Radeon PRO W7900D 专业显卡'}
