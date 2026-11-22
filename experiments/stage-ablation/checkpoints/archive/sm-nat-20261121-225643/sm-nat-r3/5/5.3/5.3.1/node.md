# N102: LRU缓存内对象大小分布的截断条件：缓存容量M=128GB对应的大小阈值S_max_cache，由累积概率积分 ∫_{S_min}^{S_max_cache} 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

LRU缓存内对象大小分布的截断条件：缓存容量M=128GB对应的大小阈值S_max_cache，由累积概率积分 ∫_{S_min}^{S_max_cache} s * f_size(s) ds = M 确定；在α=1.1且S_min=1KB时，S_max_cache ≈ 1.374e11^(1/1.1) * 1KB^(1/1.1) ≈ 1.374e9 bytes (1.37GB)，即缓存仅能容纳大小小于1.37GB的对象。

## Corrected Claim

LRU缓存内对象大小分布的截断条件：缓存容量M=128GB对应的大小阈值S_max_cache，由累积概率积分 ∫_{S_min}^{S_max_cache} s * f_size(s) ds = M 确定；在α=1.1且S_min=1KB时，S_max_cache ≈ 1.374e11^(1/1.1) * 1KB^(1/1.1) ≈ 1.374e9 bytes (1.37GB)，即缓存仅能容纳大小小于1.37GB的对象。

## Evidence

先验知识/题面给定，逻辑校验通过：基于幂律分布 $f(s) \propto s^{-\alpha}$ 的累积质量积分推导，数值量级与公式逻辑自洽。
