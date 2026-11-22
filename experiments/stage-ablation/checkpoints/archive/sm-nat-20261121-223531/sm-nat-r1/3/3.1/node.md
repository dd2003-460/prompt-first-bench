# N13: LFU 相对增益上限：ΔH_max = H_LFU - H_LRU ≤ ∫_{h>h_threshold} (f_H(h) - f_H_LRU(h)) * E[

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LFU 相对增益上限：ΔH_max = H_LFU - H_LRU ≤ ∫_{h>h_threshold} (f_H(h) - f_H_LRU(h)) * E[S|H=h] dh，其中 h_threshold 为 LFU 频率阈值，增益机制源于 LFU 优先保留高频对象，即使其大小较大，字节命中率提升取决于大小-热度负相关程度，最大增益 [待核验] 5-10 百分点。

## Corrected Claim

LFU 相对增益上限：ΔH_max = H_LFU - H_LRU ≤ ∫_{h>h_threshold} (f_H(h) - f_H_LRU(h)) * E[S|H=h] dh，其中 h_threshold 为 LFU 频率阈值，增益机制源于 LFU 优先保留高频对象，即使其大小较大，字节命中率提升取决于大小-热度负相关程度，最大增益 [待核验] 5-10 百分点。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU vs LRU cache hit rate improvement pareto workload correlation
