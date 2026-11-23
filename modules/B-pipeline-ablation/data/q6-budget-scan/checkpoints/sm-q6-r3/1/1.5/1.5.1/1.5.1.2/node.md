# N108: 出网带宽计费单价：当前假设值为¥0.1/Mbps/小时，实际需根据IDC合同或云服务商阶梯定价调整，该参数直接决定月度成本规模。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

出网带宽计费单价：当前假设值为¥0.1/Mbps/小时，实际需根据IDC合同或云服务商阶梯定价调整，该参数直接决定月度成本规模。

## Corrected Claim

出网带宽计费单价：具体数值需根据IDC合同或云服务商阶梯定价确定（常见模式包括按带宽峰值、95计费或按流量计费），该参数直接决定月度成本规模。

## Evidence

[质询]该陈述中的具体数值（¥0.1/Mbps/小时）属于经验事实（市场定价），无法从第一性原理推导。虽然逻辑上自洽（带宽计费确实影响成本），但参考来源仅讨论了计费模式（按带宽/流量、95计费），并未提供具体的单价数值，因此无法验证该特定假设值的准确性或普遍性。 | 经验事实，逻辑自洽但缺来源支持。来源[1]和[2]确认了带宽计费的逻辑和IDC计费模式，但未提供具体单价数据，无法直接支持¥0.1/Mbps/小时这一具体数值。

## Search Query

China IDC bandwidth cost per Mbps per hour 2024

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2053451104332013653&rut=b139ab919bbe4e1dccd41c5e3e873aad50cf163a1e7db1808bef286e4d92c0f8', 'type': 'ddg', 'title': '不同带宽、流量规格下，云加速价格如何计算？ - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/2044494572210980290&rut=33d45b142647bf3049fc389ade9634b15a91b71cf7ea94b4cc8c189f53d79a66', 'type': 'ddg', 'title': 'Idc带宽95计费怎么算？一文讲清计费规则与逻辑 - 知乎'}
