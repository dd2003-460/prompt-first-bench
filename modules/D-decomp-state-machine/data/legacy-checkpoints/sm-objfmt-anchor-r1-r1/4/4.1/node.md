# N21: 硬件价格参数溯源矩阵：列出所有候选GPU（RTX 4090, RTX 5090, L40S, H100, A100, MI300X等）的MSRP与当前市场均价（

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

硬件价格参数溯源矩阵：列出所有候选GPU（RTX 4090, RTX 5090, L40S, H100, A100, MI300X等）的MSRP与当前市场均价（USD），标注来源为'实时电商/新闻检索'或'模型先验知识'，置信度≥0.9需双源交叉验证，否则标[待核验]

## Corrected Claim

基于实时租赁市场数据（来源[1][2][3]），RTX 4090、RTX 5090、A100、H100等主流GPU的市场活跃度和相对价格层级可被追踪，但具体的硬件MSRP与买断市场均价需另行通过电商渠道核验，当前来源仅覆盖租赁维度。

## Evidence

[质询]参考来源主要提供的是GPU租赁价格（每小时费用），而非硬件购买市场的MSRP（建议零售价）或二手/现货市场均价（一次性买断价格），存在口径混淆（租赁成本 vs 资产价值）；此外，来源中缺乏MI300X、L40S等部分候选GPU的数据，且未提供双源交叉验证以支撑≥0.9的高置信度。 | 来源[1][2][3]提供了部分GPU（4090, 5090, A100, H100）的租赁价格数据，间接反映了市场活跃度，但未直接提供MSRP或买断均价，且缺少部分型号数据，无法完全满足‘双源交叉验证’及‘完整列表’的要求，故降级为定性描述。

## Search Query

RTX 4090 price 2024 2025 market average USD, NVIDIA H100 A100 current price comparison

## Retrieval Sources

- {'url': 'https://rentgpu.link/&rut=ae5e51fc313487b527e7351ccd2ae3030d971a8bf860e028a1efd12459bc9796', 'type': 'ddg', 'title': 'Gpu 租用实时比价 - 31+平台 32+卡型每 45 分钟更新 | Gpu算力雷达'}
- {'url': 'https://blog.csdn.net/weixin_43677258/article/details/171431400&rut=ac044049857dd15da6d0286e21ba07745176c1a6dacb532ff0962c982c427945', 'type': 'ddg', 'title': '2026年11月GPU算力租赁实战指南：4090/5090/A100价格、计费方式、卡型全解析（附分子动力学GROMAC'}
- {'url': 'https://gpuprice.cn/&rut=6a8c677f89851fc32b5192de1e687eec9a05ae5de0887da049eb36fc6b8562f2', 'type': 'ddg', 'title': 'Gpu 算力比价：Rtx 4090、H100 显卡租赁价格实时对比（230 个平台） - Gpu价网'}
