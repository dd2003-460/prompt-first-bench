# N56: NVIDIA RTX 4080 Super (16GB) 2025年零售均价为 $1,000-$1,100，其显存容量(16GB)在INT8下勉强满足27B模型

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

NVIDIA RTX 4080 Super (16GB) 2025年零售均价为 $1,000-$1,100，其显存容量(16GB)在INT8下勉强满足27B模型(13.5GB权重+1.93GB KV+1GB激活=16.43GB)但无冗余，在BF16下完全不可行，因此被排除在首选性价比列表之外，仅作为极限低价备选。

## Corrected Claim

NVIDIA RTX 4080 Super (16GB) 2025年零售均价为 $1,000-$1,100，其显存容量(16GB)在INT8下勉强满足27B模型(13.5GB权重+1.93GB KV+1GB激活=16.43GB)但无冗余，在BF16下完全不可行，因此被排除在首选性价比列表之外，仅作为极限低价备选。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型在INT8下权重约13.5GB，加上KV Cache和激活值后总显存需求约16.43GB，确实超过RTX 4080 Super的16GB显存容量，导致无法稳定运行或无冗余，逻辑自洽。
