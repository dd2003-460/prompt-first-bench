# N97: LFU 保留集合 S_LFU 的确定准则：S_LFU = {i | f_i ≥ f_threshold}，其中 f_i 为对象 i 的请求频率，f_thresh

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N32

## Claim

LFU 保留集合 S_LFU 的确定准则：S_LFU = {i | f_i ≥ f_threshold}，其中 f_i 为对象 i 的请求频率，f_threshold 为使 Σ_{i∈S_LFU} s_i ≤ 128GB 的最小频率阈值；在 β=0.9 下，f_threshold ≈ Z * (N_cache)^{β-1}，其中 Z 为归一化常数。

## Corrected Claim

LFU 保留集合 S_LFU 的确定准则：S_LFU = {i | f_i ≥ f_threshold}，其中 f_i 为对象 i 的请求频率，f_threshold 为满足容量约束 Σ_{i∈S_LFU} s_i ≤ 128GB 的最小频率阈值。具体阈值计算依赖于频率分布模型（如 Zipf 分布），在特定假设下可近似为幂律形式，但需明确模型参数。

## Evidence

[质询]公式 f_threshold ≈ Z * (N_cache)^{β-1} 缺乏明确的物理或数学推导依据，且未定义 Z 的具体计算方式或 N_cache 的确切含义（是对象总数还是缓存容量？），存在将经验拟合公式误述为通用准则的风险。 | source=knowledge，逻辑上 LFU 基于频率阈值筛选符合基本定义，但具体幂律公式属于特定模型假设，无来源支持且无法从第一性原理严格推出，故降级。
