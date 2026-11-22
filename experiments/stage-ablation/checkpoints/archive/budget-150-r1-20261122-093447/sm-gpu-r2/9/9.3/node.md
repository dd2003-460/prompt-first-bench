# N122: BF16 精度下显存需求 ~62.3GB (N13)，单卡消费级不可行；单卡 L40S (48GB) 不可行，需双卡 L40S (96GB) 或单卡 A100/

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

BF16 精度下显存需求 ~62.3GB (N13)，单卡消费级不可行；单卡 L40S (48GB) 不可行，需双卡 L40S (96GB) 或单卡 A100/H100 (80GB)；A100 80GB SXM 支持 NVLink 600GB/s，双卡 A100 可支撑 BF16 + 32K ctx + batch_size=2，但硬件成本 > $40,000

## Corrected Claim

BF16 精度下显存需求 ~62.3GB (N13)，单卡消费级不可行；单卡 L40S (48GB) 不可行，需双卡 L40S (96GB) 或单卡 A100/H100 (80GB)；A100 80GB SXM 支持 NVLink 600GB/s，双卡 A100 可支撑 BF16 + 32K ctx + batch_size=2，但硬件成本 > $40,000

## Evidence

先验知识/题面给定，逻辑校验通过：BF16下62.3GB显存需求确实超出单卡L40S(48GB)容量，需双卡或80GB卡；A100 80GB SXM NVLink带宽及双卡支撑32K ctx+batch=2的推理场景符合工程常识，成本估算合理。
