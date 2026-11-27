# N43: 缓存内对象大小分布：在热度负相关（ρ=-0.3）下，缓存内对象的大小分布偏向小值，E[s_i|Cache] < E[s_i|Total]，需计算条件期望 E[s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

缓存内对象大小分布：在热度负相关（ρ=-0.3）下，缓存内对象的大小分布偏向小值，E[s_i|Cache] < E[s_i|Total]，需计算条件期望 E[s_i | r_i > r_threshold]，其中 r_threshold 为进入缓存的热度阈值。

## Corrected Claim

缓存内对象大小分布：在热度负相关（ρ=-0.3）下，缓存内对象的大小分布偏向小值，E[s_i|Cache] < E[s_i|Total]，需计算条件期望 E[s_i | r_i > r_threshold]，其中 r_threshold 为进入缓存的热度阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：在缓存热度与大小负相关（ρ=-0.3）的设定下，高热度对象倾向于小尺寸，因此缓存内对象大小分布偏向小值，条件期望小于总体期望，逻辑自洽。

## Search Query

conditional expectation size given frequency negative correlation
