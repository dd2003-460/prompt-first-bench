# N508: RX 7900 XTX 单卡 Decode 阶段无 PCIe 通信瓶颈，其有效带宽利用率主要受显存颗粒时序和控制器调度限制，而非总线带宽；与 N176 中提及的

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N176

## Claim

RX 7900 XTX 单卡 Decode 阶段无 PCIe 通信瓶颈，其有效带宽利用率主要受显存颗粒时序和控制器调度限制，而非总线带宽；与 N176 中提及的 PCIe 64GB/s 限制不同，单卡场景下 PCIe 仅用于数据加载，不影响逐 token 生成时的权重/KV 读取带宽。

## Corrected Claim

RX 7900 XTX 单卡 Decode 阶段无 PCIe 通信瓶颈，其有效带宽利用率主要受显存颗粒时序和控制器调度限制，而非总线带宽；与 N176 中提及的 PCIe 64GB/s 限制不同，单卡场景下 PCIe 仅用于数据加载，不影响逐 token 生成时的权重/KV 读取带宽。

## Evidence

先验知识/题面给定，逻辑校验通过：RX 7900 XTX 显存带宽（~960GB/s）远高于 PCIe 4.0 x16 带宽（~32GB/s），在单卡 Decode 阶段，权重和 KV Cache 均驻留在显存中，逐 token 生成时的瓶颈确为显存带宽而非 PCIe 总线带宽，PCIe 仅用于初始模型加载或主机-设备间少量数据交换，陈述符合硬件架构基本原理。
