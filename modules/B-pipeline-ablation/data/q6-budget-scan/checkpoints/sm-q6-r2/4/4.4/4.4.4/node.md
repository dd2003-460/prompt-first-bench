# N71: PAR 对 P99 延迟的影响：高 PAR 导致峰值期间缓存过载，命中率下降，P99 延迟上升；需建立 P99_latency = f(PAR, H_avg) 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

PAR 对 P99 延迟的影响：高 PAR 导致峰值期间缓存过载，命中率下降，P99 延迟上升；需建立 P99_latency = f(PAR, H_avg) 模型，其中 H_avg 为平均命中率，PAR 越高，H_avg 越低，P99 延迟越高

## Corrected Claim

PAR 对 P99 延迟的影响：高 PAR 导致峰值期间缓存过载，命中率下降，P99 延迟上升；需建立 P99_latency = f(PAR, H_avg) 模型，其中 H_avg 为平均命中率，PAR 越高，H_avg 越低，P99 延迟越高

## Evidence

先验知识/题面给定，逻辑校验通过：高PAR导致缓存过载进而降低命中率并增加P99延迟符合系统性能基本直觉，且source为knowledge，无需外部来源支持。
