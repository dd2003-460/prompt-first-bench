# N165: 源站网络延迟 t_network_origin 取决于源站出口带宽利用率与跨域路由跳数：t_net = t_rtt_origin/2 + t_processin

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

源站网络延迟 t_network_origin 取决于源站出口带宽利用率与跨域路由跳数：t_net = t_rtt_origin/2 + t_processing_queue，其中 t_rtt_origin 为源站到边缘节点的往返时延，通常 5-20ms（同城）或 20-50ms（跨域），需通过 traceroute 实测

## Corrected Claim

源站网络延迟 t_network_origin 取决于源站出口带宽利用率与跨域路由跳数：t_net = t_rtt_origin/2 + t_processing_queue，其中 t_rtt_origin 为源站到边缘节点的往返时延，通常 5-20ms（同城）或 20-50ms（跨域），需通过 traceroute 实测

## Evidence

先验知识/题面给定，逻辑校验通过：网络延迟分解为RTT一半加排队/处理时延符合TCP/IP通信基本模型，同城5-20ms及跨域20-50ms的RTT量级符合物理光速限制与典型网络拓扑经验值，traceroute为实测标准工具。

## Search Query

origin server network latency traceroute RTT measurement
