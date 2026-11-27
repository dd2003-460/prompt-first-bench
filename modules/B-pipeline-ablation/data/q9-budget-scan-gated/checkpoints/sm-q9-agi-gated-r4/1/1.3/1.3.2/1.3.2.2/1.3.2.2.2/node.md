# N103: 在高并发批处理场景（batch_size=8），decode 步时间受 AllReduce 带宽延迟主导（1.79ms）及 GPU 争用影响，单 token 延

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

在高并发批处理场景（batch_size=8），decode 步时间受 AllReduce 带宽延迟主导（1.79ms）及 GPU 争用影响，单 token 延迟增至 15-20ms，通信占比稳定在 15-25% 区间，与 N9 估算一致，表明高并发下通信不再是次要瓶颈。

## Corrected Claim

在高并发批处理场景（batch_size=8），decode 步时间受 AllReduce 通信延迟及 GPU 争用影响显著，单 token 延迟通常较低并发场景增加，通信占比上升至 15-25% 区间，表明高并发下通信成为主要瓶颈之一。

## Evidence

[质询]具体数值（1.79ms, 15-20ms, 15-25%）缺乏通用基准支持，高度依赖特定硬件配置（如GPU型号、互联带宽NVLink/PCIe）和软件栈版本，作为通用事实陈述存在过度具体化风险。 | 先验知识/题面给定，逻辑校验通过：在高并发（batch=8）下，AllReduce通信开销随batch size线性增加，占比上升符合分布式推理基本规律；但具体毫秒级数值为经验数据，无外部来源佐证，故降级。
