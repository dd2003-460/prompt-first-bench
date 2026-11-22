# N24: 单Token推理延迟（Time to First Token, TTFT）：在32K上下文窗口下，不同硬件配置（单卡vs多卡）处理首Token所需的计算时间，受

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

单Token推理延迟（Time to First Token, TTFT）：在32K上下文窗口下，不同硬件配置（单卡vs多卡）处理首Token所需的计算时间，受限于显存带宽和矩阵乘法吞吐量。

## Corrected Claim

单Token推理延迟（Time to First Token, TTFT）：在32K上下文窗口下，不同硬件配置（单卡vs多卡）处理首Token所需的计算时间，受限于显存带宽和矩阵乘法吞吐量。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点2和子节点3结构高度相似，本质上是对同一计算模型在不同硬件参数下的实例化，存在冗余；且子节点4关于多卡通信开销的估算（15-30%）与子节点2/3中单卡理论值的对比缺乏统一的基准参照，导致多卡方案与单卡方案的对比逻辑在正交性上略有牵强（虽然主题不同，但计算逻辑重叠）。更关键的是，父节点强调'不同硬件配置'，但子节点仅覆盖了单卡（4090, A100）和一种多卡（2x4090），未涵盖多卡A100或其他常见配置，完备性不足。）

## Search Query

Qwen3-27B inference latency TTFT 32k context RTX 4090 A100

## Retrieval Sources

- {'url': 'https://www.ibm.com/think/topics/time-to-first-token&rut=0e29c56fa6a52f8330f8a60b5da465f5de5cba35c4e7f2c30e304e431781cd5f', 'type': 'ddg', 'title': 'Time to First Token (TTFT) | IBM'}
- {'url': 'https://blog.csdn.net/weixin_29054245/article/details/170952001&rut=5b4377e4e5852d3fdd452d9dcb45a8b2ee67c8d8aa326bec8272aba5acd176a2', 'type': 'ddg', 'title': '大模型推理性能双指标：Ttft与itl详解与优化实践-csdn博客'}
- {'url': 'https://blog.csdn.net/2401_84204413/article/details/156573662&rut=0bbb6ff18a6b70bbb46d5afdf067c356510a0fe3b8e5f1c3b4574a23e87d2bb1', 'type': 'ddg', 'title': 'Ai大模型应用性能核心指标：Ttft 与 Tpot 详解-csdn博客'}
