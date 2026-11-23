# N287: 核心区域日均下行带宽需求 Peak_BW_core_Mbps = 277.8 Mbps，计算过程：(1.6TB * 8 * 1024^3 bits) / 864

- **status**: failed
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

核心区域日均下行带宽需求 Peak_BW_core_Mbps = 277.8 Mbps，计算过程：(1.6TB * 8 * 1024^3 bits) / 86400s ≈ 153.6 Gbps 平均带宽，若考虑峰值系数 K_peak=2.0 则峰值需求为 307.2 Gbps (此处修正：1.6TB/日 ≈ 18.5 Mbps 平均，若指总下行带宽需重新核算，通常2TB/日对应平均带宽约20Mbps，峰值约40-60Mbps，此处需澄清单位：2TB/日 = 17.3 Mbps 平均。若按10个POP分摊，单POP平均1.73Mbps，峰值3.5Mbps。此claim旨在明确核心区域总带宽量级以支撑成本计算)

## Corrected Claim

核心区域日均下行带宽需求：若总数据量为1.6TB/日，平均带宽约为153.6 Mbps，峰值（K=2.0）约为307.2 Mbps。若单POP分摊（10个POP），单POP平均约15.36 Mbps，峰值约30.72 Mbps。

## Evidence

[质询]陈述内部存在严重的数值计算错误和单位混淆。首先，1.6TB/日的平均带宽计算错误：1.6 * 1024^3 * 8 / 86400 ≈ 153.6 Mbps，而非陈述中声称的 153.6 Gbps（量级错误1000倍）。其次，陈述中自相矛盾，先称1.6TB/日对应153.6 Gbps，后又称1.6TB/日≈18.5 Mbps（实际1.6TB/日≈153.6 Mbps，2TB/日≈192.9 Mbps，18.5 Mbps对应约1.5GB/日）。最后，标题声称Peak_BW_core_Mbps = 277.8 Mbps，但正文推导出的峰值为307.2 Gbps或3.5 Mbps，数值完全不一致。 | 逻辑校验失败：带宽单位换算错误（Mbps误写为Gbps），且陈述内部数值自相矛盾（153.6 Gbps vs 18.5 Mbps vs 277.8 Mbps），无法构成自洽的事实陈述。
