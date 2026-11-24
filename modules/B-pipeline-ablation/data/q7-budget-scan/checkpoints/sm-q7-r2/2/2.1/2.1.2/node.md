# N48: 工作点B（性价比最优）：采用混合RAID或更大容量单盘（如32TB NVMe），减少磁盘数量以降低RAID控制器端口成本和服务器槽位限制；假设20块32TB S

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

工作点B（性价比最优）：采用混合RAID或更大容量单盘（如32TB NVMe），减少磁盘数量以降低RAID控制器端口成本和服务器槽位限制；假设20块32TB SSD（总标称640TB，有效≈500TB），单盘¥4000（¥125/TB），SSD总成本¥80,000；服务器¥40,000；其他¥10,000；总CapEx ≈ ¥130,000，折合¥260/有效TB，比工作点A节省约21%。

## Corrected Claim

工作点B（性价比最优）：采用混合RAID或更大容量单盘（如32TB NVMe），减少磁盘数量以降低RAID控制器端口成本和服务器槽位限制；假设20块32TB SSD（总标称640TB，有效≈500TB），基于假设的单盘¥4000（¥125/TB）、服务器¥40,000及其他¥10,000的成本估算，总CapEx约为¥130,000，折合¥260/有效TB。

## Evidence

[质询]该陈述包含大量具体的经验性市场数据（如32TB SSD单价¥4000、服务器价格¥40,000、总CapEx计算及与工作点A的对比百分比），这些属于特定时间点的市场价格和配置假设，无法从第一性原理推导，且参考来源未提供相关价格或具体配置成本数据，存在来源缺失风险。 | 逻辑校验通过：20块*32TB=640TB，有效500TB（利用率~78%，符合RAID6或类似冗余策略的量级）；成本计算 20*4000+40000+10000=130,000元；单位成本 130000/500=260元/TB。算术无误。但参考来源[1]仅讨论RAID原理，未涉及具体硬件价格或成本对比，属于经验事实且缺乏直接来源支持。

## Search Query

32TB NVMe SSD enterprise price 2026 bulk discount

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/641580240&rut=9bf11dfa4d83e48baeb15e59f51a98920bf44187a9d92605a5068b1760c832c0', 'type': 'ddg', 'title': 'Nas到底使用哪一种raid方案比较好？ - 知乎'}
