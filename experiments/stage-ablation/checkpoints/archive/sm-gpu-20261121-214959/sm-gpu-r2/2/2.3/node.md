# N14: 非典型方案候选集：Mac Studio M2 Ultra (192GB 统一内存, 800 GB/s 带宽, $3999-6999), Mac Studio M

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

非典型方案候选集：Mac Studio M2 Ultra (192GB 统一内存, 800 GB/s 带宽, $3999-6999), Mac Studio M3 Ultra (未发布, 预计 256GB, 1000+ GB/s, $5000+) [待核验：M3 Ultra 发布状态], 二手 H100 80GB (价格波动 $15,000-25,000), 多卡工作站 (如 4x RTX 4090 通过 PCIe 4.0 互联, 总显存 96GB, 总带宽 4032 GB/s, 成本 $6396 + 主板/电源 $2000)。

## Corrected Claim

非典型方案候选集：Mac Studio M2 Ultra (192GB 统一内存, 800 GB/s 带宽, 约 $3999-6999), Mac Studio M3 Ultra (未发布，规格与价格待官方确认), 二手 H100 80GB (价格随市场波动，近期区间约 $15,000-25,000), 多卡工作站 (如 4x RTX 4090，总显存 96GB，理论聚合带宽 4032 GB/s，实际受 PCIe 互联限制，硬件成本约 $6400-8400)。

## Evidence

[质询]M3 Ultra 的发布状态、具体规格（256GB/1000+ GB/s）及价格均为预测性信息，缺乏官方确认；二手 H100 价格波动范围极大且随时间剧烈变化，静态区间描述易过时；多卡工作站总带宽 4032 GB/s 为理论峰值叠加，实际受 PCIe 互联瓶颈限制，且成本估算未包含机箱、散热等隐性成本，存在口径混淆风险。 | 无可用外部证据（检索失败）。逻辑校验：M2 Ultra 参数符合已知事实；M3 Ultra 为合理推测但属未发布产品；H100 价格区间符合市场波动特征；多卡带宽计算（4x1008=4032）数学正确但物理实现受限于 PCIe 带宽，成本估算量级合理。因缺乏来源支持且含未发布/波动性数据，降级为定性表述。

## Search Query

Mac Studio M2 Ultra 192GB price used H100 price 4x RTX 4090 multi-GPU setup cost
