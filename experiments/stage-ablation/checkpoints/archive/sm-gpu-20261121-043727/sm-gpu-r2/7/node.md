# N35: 量化TCO中的功耗成本：RTX 4090 TDP 450W, H100 SXM TDP 700W, MI300X TDP 750W；假设电费 $0.1/kWh，

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

量化TCO中的功耗成本：RTX 4090 TDP 450W, H100 SXM TDP 700W, MI300X TDP 750W；假设电费 $0.1/kWh，计算单卡满载运行1年的电力成本差异，公式：Cost = TDP(kW) * 8760h * $0.1

## Corrected Claim

量化TCO中的功耗成本：以桌面版 RTX 4090 (TDP 450W)、H100 SXM (TDP 700W)、MI300X (TDP 750W) 为例，假设电费 $0.1/kWh，单卡满载运行1年的电力成本计算公式为 Cost = TDP(kW) * 8760h * $0.1。注意：实际功耗受版本（桌面/移动）、负载及系统配置影响，此处 TDP 为典型标称值。

## Evidence

父节点级核验未通过：有冗余（子节点1-3结构高度同质化，本质上是同一计算公式（Cost = TDP * 8760 * Price）在不同硬件参数下的实例化，存在结构性冗余；且节点4中RTX 4090的3年电费计算存在算术错误（$394.2 * 3 ≈ $1182.6，而非$1182-$1005，且区间逻辑混乱）。）

## Retrieval Sources

- {'url': 'https://blog.csdn.net/iymei4986533030/article/details/162755500&rut=d39bbec5236af6ab147d9b8c1e9bcb277fe76ebd52d743a6b586366c67c71aa3', 'type': 'ddg', 'title': 'GPU 利用率与 TCO 分析——A100 vs H100 vs 消费级 GPU 成本效益对比-CSDN博客'}
- {'url': 'https://www.stratat.com/zh/guides/rtx4090-coder&rut=280caf9b7c3314bc91c6f05c49ee4a606a20b718860b097f3e41f14667aec796', 'type': 'ddg', 'title': 'RTX 4090 运行 Coder 量化模型：性能实测与成本分析 · Strata'}
- {'url': 'https://post.smzdm.com/p/anv7wnqv/&rut=cfdffc82b946423048fdd1225b339238c71c4d289c0fcb2823898e33173cc358', 'type': 'ddg', 'title': 'Rtx 4090根本不用450w!实测功耗和电费曝光_显卡_什么值得买'}
