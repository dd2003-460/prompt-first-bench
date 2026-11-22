# N103: LRU 字节命中率的理论下界 H_byte_lower 受限于字节覆盖率与头部请求集中度的乘积。在负相关 ρ=-0.3 下，驻留集合（小对象）承载了约 45% 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU 字节命中率的理论下界 H_byte_lower 受限于字节覆盖率与头部请求集中度的乘积。在负相关 ρ=-0.3 下，驻留集合（小对象）承载了约 45% 的请求量（N43 数据），但仅占约 3.5% 的字节量。因此，字节命中率下界 H_byte_lower ≈ P_req_cached * (Byte_Coverage / Req_Coverage) 的修正形式，具体数值需通过 ∑_{i∈C} (λ_i s_i) / ∑_{j=1}^{N} (λ_j s_j) 计算，初步估算该比值约为 12%-15%，显著高于请求命中率（~45%）的直觉预期偏差，因为分母中包含了大量未被缓存的大对象字节流量。

## Corrected Claim

LRU 字节命中率的理论下界 H_byte_lower 受限于字节覆盖率与头部请求集中度的乘积。在负相关 ρ=-0.3 下，驻留集合（小对象）承载了约 45% 的请求量（N43 数据），但仅占约 3.5% 的字节量。因此，字节命中率下界 H_byte_lower ≈ P_req_cached * (Byte_Coverage / Req_Coverage) 的修正形式，具体数值需通过 ∑_{i∈C} (λ_i s_i) / ∑_{j=1}^{N} (λ_j s_j) 计算，初步估算该比值约为 12%-15%，显著高于请求命中率（~45%）的直觉预期偏差，因为分母中包含了大量未被缓存的大对象字节流量。

## Evidence

检索失败: no sources from any channel (all 5 failed)
