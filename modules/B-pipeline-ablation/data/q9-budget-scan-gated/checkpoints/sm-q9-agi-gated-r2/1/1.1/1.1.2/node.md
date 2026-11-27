# N19: V100 HBM2 900GB/s带宽在处理13.5GB权重时，理论最大访存吞吐受限，单卡每秒可处理的token数受限于权重加载速率（约67 tok/s）

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

V100 HBM2 900GB/s带宽在处理13.5GB权重时，理论最大访存吞吐受限，单卡每秒可处理的token数受限于权重加载速率（约67 tok/s）

## Corrected Claim

V100 HBM2 900GB/s带宽在处理13.5GB权重时，理论最大访存吞吐受限，单卡每秒可处理的token数受限于权重加载速率（约67 tok/s）

## Evidence

先验知识/题面给定，逻辑校验通过：V100 HBM2带宽900GB/s，权重13.5GB，理论最大吞吐=900/13.5=67 tok/s，计算正确且符合内存带宽瓶颈的基本原理
