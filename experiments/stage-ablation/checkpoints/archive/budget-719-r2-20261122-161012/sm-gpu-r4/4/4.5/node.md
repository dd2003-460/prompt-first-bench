# N24: 候选集必须包含以下架构/代际/容量组合：消费级 (RTX 3090/4090/5090, 24-32GB, $1600-$2000), 数据中心 (A100/H

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5, N6

## Claim

候选集必须包含以下架构/代际/容量组合：消费级 (RTX 3090/4090/5090, 24-32GB, $1600-$2000), 数据中心 (A100/H100/MI300X, 40-80GB+, $10k-$30k), 非典型 (Mac Studio M2/M3 Ultra 512GB, $4k-$10k, 统一内存架构, 带宽 800GB/s-1.2TB/s)；遗漏 Mac 方案将导致在 32K 上下文 BF16 场景下无可行解（消费卡单卡显存不足，多卡成本激增）。

## Corrected Claim

候选集建议包含以下架构/代际/容量组合：消费级 (RTX 3090/4090, 24GB, ~$1600-$2000), 数据中心 (A100/H100, 40-80GB+, $10k-$30k), 非典型 (Mac Studio M2/M3 Ultra, 统一内存架构)；在32K上下文BF16场景下，消费级单卡显存通常不足，需考虑多卡或高内存统一架构方案。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点严格对应父节点中定义的三个互斥类别（消费级、数据中心、非典型/Mac），内容无重叠且无矛盾。虽然结构上都是‘硬件 vs 需求’的对比，但由于硬件架构（显存独立vs统一内存）、成本量级和性能瓶颈（带宽vs显存容量）存在本质差异，因此不构成冗余，而是针对不同约束条件下的独立分析维度。完备性方面，三个子节点完整覆盖了父节点要求的所有架构组合及其关键约束（显存缺口、剩余空间、带宽限制）。）

## Search Query

Mac Studio M3 Ultra 512GB LLM inference Qwen3-27B 32k context feasibility

## Retrieval Sources

- {'url': 'https://cloud.baidu.com/article/3733336&rut=8496a2d56097d3ba16175a099a4ff90fc94ccb3d94c5330e68d9a4b938b16b3b', 'type': 'ddg', 'title': '多型号显卡性能深度对比：Rtx 3090/4090与nvidia专业卡全解析'}
