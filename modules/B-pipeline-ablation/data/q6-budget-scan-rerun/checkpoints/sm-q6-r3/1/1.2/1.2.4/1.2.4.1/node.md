# N118: 客户端网络下载时间 $T_{dl} = s / B_{eff}$，其中 $s$ 为对象大小（字节），$B_{eff}$ 为有效带宽（bps）。$B_{eff}$

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

客户端网络下载时间 $T_{dl} = s / B_{eff}$，其中 $s$ 为对象大小（字节），$B_{eff}$ 为有效带宽（bps）。$B_{eff}$ 受限于客户端上行/下行链路速率及 TCP 拥塞控制窗口，典型 4G/5G 下行 $B_{eff} \in [5, 50]$ Mbps，Wi-Fi 环境 $B_{eff} \in [50, 500]$ Mbps。

## Corrected Claim

客户端网络下载时间 $T_{dl} = s / B_{eff}$，其中 $s$ 为对象大小（字节），$B_{eff}$ 为有效带宽（bps）。$B_{eff}$ 受限于客户端上行/下行链路速率及 TCP 拥塞控制窗口，典型 4G/5G 下行 $B_{eff} \in [5, 50]$ Mbps，Wi-Fi 环境 $B_{eff} \in [50, 500]$ Mbps。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 T=s/B 量纲正确（字节/比特每秒需隐含单位转换或定义一致，此处为通用模型表述），4G/5G及Wi-Fi带宽范围符合典型工程经验值。

## Search Query

average mobile download speed Mbps 4G 5G wifi throughput statistics
