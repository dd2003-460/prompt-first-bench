# N46: Apple M3 Ultra (512GB) 整机峰值功耗约为 500W，基于 1.3 倍冗余系数计算，所需电源瓦数下限为 650W。

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

Apple M3 Ultra (512GB) 整机峰值功耗约为 500W，基于 1.3 倍冗余系数计算，所需电源瓦数下限为 650W。

## Corrected Claim

Apple M3 Ultra 整机峰值功耗的具体数值需依据官方或权威测试数据确定，若按 500W 估算，所需电源瓦数下限为 650W。

## Evidence

[质询]Apple M3 Ultra 芯片本身的 TDP 远低于 500W（通常估计在 100-200W 左右），500W 作为‘整机峰值功耗’对于 Mac Studio 等搭载该芯片的设备而言显著偏高，可能混淆了芯片功耗与整机极端负载功耗，或者该数值缺乏公开权威数据支持，属于经验性估算而非确凿事实。 | source=knowledge，逻辑上 500W * 1.3 = 650W 计算正确，但 500W 的整机峰值功耗前提缺乏可靠来源支持且与常见硬件规格直觉存在偏差，故降级。

## Search Query

Apple M3 Ultra 512GB power consumption PSU requirement
