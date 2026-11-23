# N59: TCP慢启动影响：对于大对象（>1MB），TCP慢启动可能导致传输时间增加，P99传输延迟 T_transmit_P99 = object_size / (mi

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

TCP慢启动影响：对于大对象（>1MB），TCP慢启动可能导致传输时间增加，P99传输延迟 T_transmit_P99 = object_size / (min(BW, cwnd * MSS / RTT))，其中cwnd为拥塞窗口，MSS为最大报文段（通常1460字节），初始cwnd=10，每RTT翻倍，P99传输延迟对于5MB对象在100Mbps带宽下约为50-100ms。

## Corrected Claim

TCP慢启动影响：对于大对象（>1MB），TCP慢启动可能导致传输时间增加，P99传输延迟 T_transmit_P99 = object_size / (min(BW, cwnd * MSS / RTT))，其中cwnd为拥塞窗口，MSS为最大报文段（通常1460字节），初始cwnd=10，每RTT翻倍，P99传输延迟对于5MB对象在100Mbps带宽下约为50-100ms。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1和子节点2存在严重的逻辑重叠和定义冲突。子节点1计算了慢启动耗时（~320ms），子节点2在计算总延迟时直接加上了这个耗时，且子节点2的标题'修正项'暗示其包含慢启动影响，导致两者在'慢启动对总延迟的贡献'这一核心概念上高度耦合，非正交。此外，子节点3讨论的CUBIC和TFO属于优化策略，与子节点1的基础模型（传统指数增长）在前提假设上略有不同，但未明确区分场景，造成概念边界模糊。）
