# N298: 峰值系数 $K_p$ 对公有云 CDN 带宽计费档位的影响：若选择按带宽峰值计费，计费带宽 $B_{bill} = Peak\ QPS * s * 8 / 10

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99, N100, N101

## Claim

峰值系数 $K_p$ 对公有云 CDN 带宽计费档位的影响：若选择按带宽峰值计费，计费带宽 $B_{bill} = Peak\ QPS * s * 8 / 10^6$ (Mbps)，其中 s 为平均对象大小。当 $K_p=3.0$ 时，$B_{bill} \approx 4855 * 3.0 * 0.5 * 8 / 1000 \approx 58$ Mbps (注：此处单位换算需精确，2TB/86400s ≈ 250KB/s ≈ 2Mbps avg, Peak ≈ 6-7Mbps，若按日峰值 4 小时集中计算则更高，需明确计费窗口)。

## Corrected Claim

峰值系数 $K_p$ 对公有云 CDN 带宽计费档位的影响：若选择按带宽峰值计费，计费带宽 $B_{bill}$ 取决于峰值 QPS、平均对象大小及计费窗口。需统一单位换算（如 1 Mbps = 10^6 bits/s），并明确峰值持续时间（如 5分钟或 1小时）以准确估算计费带宽，原陈述中数值计算存在单位错误及量级矛盾。

## Evidence

[质询]数值量级与单位换算存在严重矛盾：公式中分母为 10^6 (Mbps)，但代入数值计算时使用了 /1000，且最终结果 58 Mbps 与注释中推导的 6-7 Mbps 或 2 Mbps 平均带宽严重不符，内部逻辑不自洽。 | 先验知识/题面给定，逻辑校验失败：公式定义与代入计算过程单位不一致（10^6 vs 1000），且计算结果与注释中的物理直觉估算（2-7 Mbps）相差一个数量级，存在硬逻辑错误。

## Search Query

CDN bandwidth billing peak calculation Mbps
