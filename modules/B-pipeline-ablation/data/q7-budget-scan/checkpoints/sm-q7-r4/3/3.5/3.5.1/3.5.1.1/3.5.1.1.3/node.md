# N744: 工作点 C（极低 RPO/高成本）：RPO=5 分钟，采用连续数据保护 (CDP) 或 5 分钟粒度快照。恢复数据量 = 最近 5 分钟增量 ≈ 500TB ×

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N278

## Claim

工作点 C（极低 RPO/高成本）：RPO=5 分钟，采用连续数据保护 (CDP) 或 5 分钟粒度快照。恢复数据量 = 最近 5 分钟增量 ≈ 500TB × 0.1%/hour × (5/60)h ≈ 0.04TB (40GB)。系数 k ≈ 0.00008。虽然恢复传输成本极低，但 CDP 软件许可费高达 ¥50,000/年（基于数据量计费），且备份存储需保留 24 小时连续日志（约 12TB），总年成本 ≈ ¥54,380/年，远高于工作点 B。

## Corrected Claim

工作点 C（极低 RPO/高成本）：RPO=5 分钟，采用连续数据保护 (CDP) 或 5 分钟粒度快照。恢复数据量约为 40GB。虽然恢复传输成本极低，但 CDP 软件许可费及备份存储成本通常较高，导致总年成本显著高于工作点 B（具体数值需根据实际供应商报价确定）。

## Evidence

[质询]该陈述包含大量具体的经验性参数（如CDP软件许可费¥50,000/年、备份存储成本、总年成本¥54,380/年），这些属于市场定价和商业报价，无法从第一性原理或题面条件严格推导得出，且参考来源未提供相关数据支持。 | 逻辑推导部分（恢复数据量计算）自洽，但涉及具体成本和经验参数的部分缺乏来源支持，符合经验事实排除条款，故降级。

## Search Query

Continuous Data Protection CDP software licensing cost per TB per year

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/704113264&rut=c4cbc4b8021ed6554bb0cd9139adee637ff2f10195f2fed8b7d5e68f4be38dce', 'type': 'ddg', 'title': 'Rto（恢复时间目标）和rpo（恢复点目标） - 知乎'}
