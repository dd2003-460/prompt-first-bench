# N211: 工作点A（高CapEx低OpEx）：NVMe SSD阵列存储100TB温数据，扫描耗时 T_scan = 100TB / (N_drives * 3GB/s)。

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

工作点A（高CapEx低OpEx）：NVMe SSD阵列存储100TB温数据，扫描耗时 T_scan = 100TB / (N_drives * 3GB/s)。假设N_drives=10，T_scan ≈ 100,000GB / 30GB/s ≈ 3333秒 ≈ 55分钟 < SLA(2h)，隐性等待成本 C_wait = 0；主要成本为CapEx摊销，年化CapEx成本 = (100TB * ¥225/TB - 残值) / 3年 ≈ ¥7,400,000/年。

## Corrected Claim

工作点A（高CapEx低OpEx）：NVMe SSD阵列存储100TB温数据，扫描耗时 T_scan = 100TB / (N_drives * 3GB/s)。假设N_drives=10，T_scan ≈ 100,000GB / 30GB/s ≈ 3333秒 ≈ 55分钟 < SLA(2h)，隐性等待成本 C_wait = 0；主要成本为CapEx摊销，年化CapEx成本 = (100TB * ¥225/TB - 残值) / 3年 ≈ ¥7,400,000/年。

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了父节点中提到的'OpEx'部分（具体为能效/电费差异），但父节点明确指出了核心成本驱动因素是'CapEx摊销'（约740万元/年）。由于缺少关于CapEx计算逻辑、折旧政策或硬件价格假设的子节点，分解未覆盖父节点的关键方面，导致不完备。）
