# N176: 在容量受限区（K_cap=24,576）下，LFU 相比 LRU 的字节命中率增益 ΔH = H_LFU - H_LRU 的解析估计：ΔH ≈ (Σ_{i∈C_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

在容量受限区（K_cap=24,576）下，LFU 相比 LRU 的字节命中率增益 ΔH = H_LFU - H_LRU 的解析估计：ΔH ≈ (Σ_{i∈C_LFU} R_i S_i - Σ_{i∈C_LRU} R_i S_i) / TotalBytes，其中 C_LFU 保留前 24,576 个最高频率对象，C_LRU 保留最近访问的 24,576 个对象；由于热度 Pareto(β=0.9) 的极端集中性，LFU 保留的头部对象贡献约 93.7% 的请求量，而 LRU 因时间局部性可能遗漏部分高频但近期未访问的对象，ΔH 的理论上限为 H_LFU_max - H_LRU_base

## Corrected Claim

在容量受限区（K_cap=24,576）下，LFU 相比 LRU 的字节命中率增益 ΔH = H_LFU - H_LRU 的解析估计：ΔH ≈ (Σ_{i∈C_LFU} R_i S_i - Σ_{i∈C_LRU} R_i S_i) / TotalBytes，其中 C_LFU 保留前 24,576 个最高频率对象，C_LRU 保留最近访问的 24,576 个对象；由于热度 Pareto(β=0.9) 的极端集中性，LFU 保留的头部对象贡献约 93.7% 的请求量，而 LRU 因时间局部性可能遗漏部分高频但近期未访问的对象，ΔH 的理论上限为 H_LFU_max - H_LRU_base

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU vs LRU hit rate gain Pareto distribution analytical estimate
