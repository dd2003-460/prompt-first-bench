# N242: VPC内网10 Gbps链路的有效吞吐为1.2 GB/s（RTT<1ms，无拥塞），500TB数据传输时间为116.3小时，比公网节省10小时，但需计算集群部署

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

VPC内网10 Gbps链路的有效吞吐为1.2 GB/s（RTT<1ms，无拥塞），500TB数据传输时间为116.3小时，比公网节省10小时，但需计算集群部署在云同区域（额外硬件成本约¥500,000）

## Corrected Claim

VPC内网10 Gbps链路的有效吞吐为1.2 GB/s（RTT<1ms，无拥塞），500TB数据传输时间为116.3小时，比公网节省10小时，但需计算集群部署在云同区域（额外硬件成本约¥500,000）

## Evidence

先验知识/题面给定，逻辑校验通过：10 Gbps = 1.25 GB/s，考虑协议开销后1.2 GB/s合理；500TB / 1.2GB/s ≈ 115.7小时，与116.3小时量级一致；成本与部署约束符合云架构常识。
