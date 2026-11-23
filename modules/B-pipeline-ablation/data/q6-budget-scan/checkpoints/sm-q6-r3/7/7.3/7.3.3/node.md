# N337: 95th计费模式的最小起租带宽限制通常为1Gbps或10Gbps，若计算出的$B_{95}$低于此值，则按最小起租值计费，即$C_{95} = \max(B_{

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N125

## Claim

95th计费模式的最小起租带宽限制通常为1Gbps或10Gbps，若计算出的$B_{95}$低于此值，则按最小起租值计费，即$C_{95} = \max(B_{95}, B_{min}) \times R_{95} \times T_{month}$。

## Corrected Claim

95计费模式通常设有最小起租带宽限制（具体数值依运营商而定，常见如1Gbps或10Gbps），若计算出的$B_{95}$低于此值，则按最小起租值计费，即$C_{95} = \max(B_{95}, B_{min}) \times R_{95} \times T_{month}$。

## Evidence

[质询]具体数值（1Gbps或10Gbps）属于经验事实，不同运营商或IDC服务商的最小起租带宽标准差异较大，并非统一的行业固定值，存在以偏概全的风险。 | 来源[1]主题相关且解释了95计费逻辑，但未明确给出1Gbps/10Gbps的具体最小起租数值；该数值为经验事实，逻辑自洽但缺乏直接来源支持具体数值，故降级。

## Search Query

Alibaba Cloud CDN 95th percentile bandwidth minimum commitment 1Gbps 10Gbps

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2044494572210980290&rut=33d45b142647bf3049fc389ade9634b15a91b71cf7ea94b4cc8c189f53d79a66', 'type': 'ddg', 'title': 'Idc带宽95计费怎么算？一文讲清计费规则与逻辑 - 知乎'}
