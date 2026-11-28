# N35: NVLink 3.0 (V100 SXM2) 的实际有效带宽约为理论峰值 300 GB/s 的 85-90% (约 255-270 GB/s)，因存在协议开销；

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

NVLink 3.0 (V100 SXM2) 的实际有效带宽约为理论峰值 300 GB/s 的 85-90% (约 255-270 GB/s)，因存在协议开销；PCIe 3.0 x16 有效带宽约为 12.5-14 GB/s (理论 16 GB/s 减去 TLP 头尾开销)，若驱动配置错误或拓扑不当导致通信回退至 PCIe，TP 通信延迟将增加 15-20 倍，成为致命瓶颈。

## Corrected Claim

NVLink 3.0 (V100 SXM2) 的实际有效带宽约为理论峰值 300 GB/s 的 85-90% (约 255-270 GB/s)，因存在协议开销；PCIe 3.0 x16 有效带宽约为 12.5-14 GB/s (理论 16 GB/s 减去 TLP 头尾开销)，若驱动配置错误或拓扑不当导致通信回退至 PCIe，TP 通信延迟将增加 15-20 倍，成为致命瓶颈。

## Evidence

父节点级核验未通过：非正交, 不完备（子节点之间存在逻辑矛盾（NVLink vs PCIe），且严重偏离父节点主题。父节点核心讨论的是'有效带宽折扣'及'PCIe回退导致的性能灾难'，但子节点3引入了与带宽无关的计算FLOPs和算术强度分析，属于正交但无关的内容；子节点1仅提及理论值，未覆盖父节点强调的'85-90%有效带宽'这一关键约束；子节点2讨论延迟，虽相关但未涵盖父节点核心的PCIe对比场景。）

## Search Query

NVLink 3 effective bandwidth efficiency ratio PCIe 3.0 overhead percentage
