# N480: 长尾区域跳数 Hops_tail 量化：20% 分散用户通常需经过 3-5 跳（用户->ISP 骨干->核心网->POP->源站/缓存）。由于 BGP 路由收敛

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N161

## Claim

长尾区域跳数 Hops_tail 量化：20% 分散用户通常需经过 3-5 跳（用户->ISP 骨干->核心网->POP->源站/缓存）。由于 BGP 路由收敛及跨运营商互联点（IXP）的不确定性，长尾路径跳数波动大。取均值 3.5 跳，则 Hops_tail = 3.5。

## Corrected Claim

长尾区域跳数 Hops_tail 量化：20% 分散用户通常需经过 3-5 跳（用户->ISP 骨干->核心网->POP->源站/缓存）。由于 BGP 路由收敛及跨运营商互联点（IXP）的不确定性，长尾路径跳数波动大。取均值 3.5 跳，则 Hops_tail = 3.5。

## Evidence

先验知识/题面给定，逻辑校验通过：3-5跳符合互联网长尾路径的典型量级，取均值3.5在数学上自洽且符合网络工程常识。
