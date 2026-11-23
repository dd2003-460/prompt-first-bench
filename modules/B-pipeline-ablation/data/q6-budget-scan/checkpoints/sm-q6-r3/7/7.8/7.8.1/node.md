# N350: 理论无门槛临界点 $K_{peak}^{theory}$ 的计算：基于等效单价相等 $C_{95}/V = C_{traffic}/V$，推导出 $K_{pea

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

理论无门槛临界点 $K_{peak}^{theory}$ 的计算：基于等效单价相等 $C_{95}/V = C_{traffic}/V$，推导出 $K_{peak}^{theory} = P_{traffic}^{eff} / (R_{95} \times 86400 / 8000)$，其中 $R_{95}$ 为 95th 带宽单价（元/Gbps/月），$P_{traffic}^{eff}$ 为流量等效单价（元/GB）。

## Corrected Claim

理论无门槛临界点 $K_{peak}^{theory}$ 的计算：基于等效单价相等 $C_{95}/V = C_{traffic}/V$，推导出 $K_{peak}^{theory} = P_{traffic}^{eff} / (R_{95} \times 86400 / 8000)$，其中 $R_{95}$ 为 95th 带宽单价（元/Gbps/月），$P_{traffic}^{eff}$ 为流量等效单价（元/GB）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合量纲分析（元/GB 除以 元/Gbps/月 再乘以时间/带宽换算系数），且 source 为 knowledge，无需外部来源支持。
