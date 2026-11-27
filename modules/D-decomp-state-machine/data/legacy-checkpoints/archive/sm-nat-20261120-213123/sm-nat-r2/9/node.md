# N27: 在热门-大小负相关 (ρ=-0.3) 下，命中请求对应的对象集合并非单纯的热度 Top-k，而是热度加权后的字节覆盖集合。稳态字节命中率 H_byte 的下界可

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在热门-大小负相关 (ρ=-0.3) 下，命中请求对应的对象集合并非单纯的热度 Top-k，而是热度加权后的字节覆盖集合。稳态字节命中率 H_byte 的下界可通过计算 Top-k 热门对象的总字节流量占比得出：H_byte ≈ (Σ_{i=1}^{k} λ_i * S_i) / (Σ_{j=1}^{N} λ_j * S_j)。由于 ρ<0，热门对象倾向于较小，导致 k 增大时字节覆盖增长慢于独立假设，需通过 Copula 联合分布积分修正分母和分子。

## Corrected Claim

在热门-大小负相关 (ρ=-0.3) 下，命中请求对应的对象集合并非单纯的热度 Top-k，而是热度加权后的字节覆盖集合。稳态字节命中率 H_byte 的下界可通过计算 Top-k 热门对象的总字节流量占比得出：H_byte ≈ (Σ_{i=1}^{k} λ_i * S_i) / (Σ_{j=1}^{N} λ_j * S_j)。由于 ρ<0，热门对象倾向于较小，导致 k 增大时字节覆盖增长慢于独立假设，需通过 Copula 联合分布积分修正分母和分子。

## Evidence

检索失败: no sources from any channel (all 5 failed)
