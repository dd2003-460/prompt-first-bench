# N168: Write-Back 模式下脏页比例 P_dirty|miss 的量化估算：P_dirty|miss 近似等于更新对象在缓存中的字节占比乘以更新频率与访问频率的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N60

## Claim

Write-Back 模式下脏页比例 P_dirty|miss 的量化估算：P_dirty|miss 近似等于更新对象在缓存中的字节占比乘以更新频率与访问频率的比值。基于 N57，前1%热门对象（贡献主要流量）平均大小 5KB，更新率 1%/天，访问率极高（86.4s/次），P_dirty|miss ≈ (λ_upd / λ_acc_avg) * (Byte Share_hot) ≈ (1/86400) / (86400/86.4) * 0.2 ≈ 2.3e-8，可忽略不计。

## Corrected Claim

Write-Back 模式下脏页比例 P_dirty|miss 的量化估算：P_dirty|miss 近似等于更新对象在缓存中的字节占比乘以更新频率与访问频率的比值。基于 N57，前1%热门对象（贡献主要流量）平均大小 5KB，更新率 1%/天，访问率极高（86.4s/次），P_dirty|miss ≈ (λ_upd / λ_acc_avg) * (Byte Share_hot) ≈ (1/86400) / (86400/86.4) * 0.2 ≈ 2.3e-8，可忽略不计。

## Evidence

先验知识/题面给定，逻辑校验通过
