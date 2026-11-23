# N15: 带宽流量计费模式对比：公有云按量付费（Pay-per-GB）vs 自建固定带宽（Leased Line）；自建每 POP 点 10Gbps 专线月费约 ¥10,

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

带宽流量计费模式对比：公有云按量付费（Pay-per-GB）vs 自建固定带宽（Leased Line）；自建每 POP 点 10Gbps 专线月费约 ¥10,000-15,000 [时效待核]，10 个 POP 总月带宽成本 = 10 * 12,500 = ¥125,000/月 = ¥1,500,000/年，远低于公有云按量付费。

## Corrected Claim

带宽流量计费模式对比：公有云按量付费（Pay-per-GB）vs 自建固定带宽（Leased Line）；自建每 POP 点 10Gbps 专线月费具体数值需根据运营商及合同确定（参考来源未提供具体价格，原陈述中¥10,000-15,000/月缺乏来源支持且可能偏低），10 个 POP 总月带宽成本取决于实际专线单价，通常自建固定带宽在长期稳定高流量场景下成本低于公有云按量付费。

## Evidence

[质询]具体数值（10Gbps专线月费¥10,000-15,000）属于经验事实，且该价格远低于当前市场主流10G专线价格（通常数万至数十万元/月），存在量级偏差或特定优惠/内部结算口径混淆的风险；参考来源仅讨论公有云ECS带宽计费模式，未提供自建专线具体价格数据。 | 来源[1][2][3]仅支持公有云按量与固定带宽的对比逻辑，未覆盖自建专线具体价格；该价格点为经验事实，逻辑自洽但缺乏直接来源支持且数值存疑，故降级。

## Search Query

China dedicated internet line 10Gbps monthly cost 2024 BGP multi-line

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1697038&rut=65834bbfe209e59e2779934eadd8871ce1e74a6ea1c0281ef19bcc50428714d5', 'type': 'ddg', 'title': '阿里云服务器固定带宽与按量付费带宽有何区别？如何选择固定带宽价格更便宜-阿里云开发者社区'}
- {'url': 'https://blog.csdn.net/2403_89345764/article/details/157213294&rut=20cfcc74fc128f796d121a1ce91b2f3c906b7468c14e59a3fd229d54c39d6865', 'type': 'ddg', 'title': '云服务器带宽怎么选？按固定带宽计费 Vs 按流量计费 哪个更划算？一文搞懂~_云服务器流量计较-csdn博客'}
- {'url': 'https://developer.aliyun.com/article/1667924&rut=079224053068aab39cdfc053aa42c64e25bbb2d71a3a0da63d0ff308870c64f5', 'type': 'ddg', 'title': '阿里云服务器公网带宽收费标准：按固定带宽和使用流量计费规则'}
