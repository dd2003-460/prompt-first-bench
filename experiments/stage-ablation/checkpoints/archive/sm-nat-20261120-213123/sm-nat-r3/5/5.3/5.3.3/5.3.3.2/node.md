# N151: 中间过渡对象的更新失效折损 ΔH_mid_invalidate 与容量竞争折损 ΔH_mid_comp 的分解：ΔH_mid = ΔH_mid_invalida

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

中间过渡对象的更新失效折损 ΔH_mid_invalidate 与容量竞争折损 ΔH_mid_comp 的分解：ΔH_mid = ΔH_mid_invalidate + ΔH_mid_comp - ΔH_mid_overlap，其中 ΔH_mid_invalidate = P_invalidate_mid * (S_mid/S_total) * H_static_mid，ΔH_mid_comp 由 LRU 替换导致的额外未命中字节数决定。需分别量化两项以验证 '主要受限于容量竞争而非更新失效' 的断言。

## Corrected Claim

中间过渡对象的更新失效折损 ΔH_mid_invalidate 与容量竞争折损 ΔH_mid_comp 的分解：ΔH_mid = ΔH_mid_invalidate + ΔH_mid_comp - ΔH_mid_overlap，其中 ΔH_mid_invalidate = P_invalidate_mid * (S_mid/S_total) * H_static_mid，ΔH_mid_comp 由 LRU 替换导致的额外未命中字节数决定。需分别量化两项以验证 '主要受限于容量竞争而非更新失效' 的断言。

## Evidence

先验知识/题面给定，逻辑校验通过
