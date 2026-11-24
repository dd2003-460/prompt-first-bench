# N133: T_network 物理极限计算：T_min_phys = (2 × d_avg) / c，其中 d_avg 为用户到最近 POP 的平均物理距离（基于 N14

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

T_network 物理极限计算：T_min_phys = (2 × d_avg) / c，其中 d_avg 为用户到最近 POP 的平均物理距离（基于 N14 地理分布，核心区域 d≈100km，长尾 d≈500km），c=3×10^8 m/s；核心区域 T_min_phys ≈ 0.67ms，长尾区域 T_min_phys ≈ 3.3ms；该值仅为理论下限，实际需叠加路由开销。

## Corrected Claim

T_network 物理极限计算：T_min_phys = (2 × d_avg) / c，其中 d_avg 为用户到最近 POP 的平均物理距离（基于 N14 地理分布，核心区域 d≈100km，长尾 d≈500km），c=3×10^8 m/s；核心区域 T_min_phys ≈ 0.67ms，长尾区域 T_min_phys ≈ 3.3ms；该值仅为理论下限，实际需叠加路由开销。

## Evidence

先验知识/题面给定，逻辑校验通过：光速 c=3×10^8 m/s，核心区域 d=100km=10^5 m，T=2×10^5/3×10^8 ≈ 0.67ms；长尾区域 d=500km=5×10^5 m，T=2×5×10^5/3×10^8 ≈ 3.33ms。计算无误，量级合理。
