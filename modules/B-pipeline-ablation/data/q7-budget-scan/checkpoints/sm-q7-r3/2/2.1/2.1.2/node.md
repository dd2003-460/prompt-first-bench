# N48: 工作点B（性价比最优）：采用混合RAID或更大容量单盘（如32TB NVMe），减少磁盘数量以降低RAID控制器端口成本和服务器槽位限制；假设20块32TB S

- **status**: pending
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

父节点级核验未通过：不完备（子节点在逻辑上正交（分别处理容量、折旧、电力），且无冗余。但在完备性上存在重大缺陷：父节点的核心结论是'总CapEx ≈ ¥130,000'和'单位成本¥260/有效TB'，这属于一次性资本支出分析。子节点却引入了'5年直线折旧'和'年电力成本'，这是运营支出（OpEx）概念，与父节点的纯CapEx语境不符，导致维度不匹配。此外，子节点1指出了有效容量计算错误（应为~577TB而非500TB），但未提供修正后的CapEx单位成本计算子节点，导致无法直接验证父节点中'比工作点A节省21%'这一核心结论是否成立。）

## Search Query

32TB NVMe SSD enterprise price 2026 bulk discount

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/641580240&rut=9bf11dfa4d83e48baeb15e59f51a98920bf44187a9d92605a5068b1760c832c0', 'type': 'ddg', 'title': 'Nas到底使用哪一种raid方案比较好？ - 知乎'}
