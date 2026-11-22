# N24: 候选集必须包含以下架构/代际/容量组合：消费级 (RTX 3090/4090/5090, 24-32GB, $1600-$2000), 数据中心 (A100/H

- **status**: pending
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

父节点级核验未通过：有冗余（子节点分别对应父节点定义的三类硬件架构（消费级、数据中心、非典型），逻辑上正交且覆盖了所有关键方面，无遗漏。然而，子节点内容高度同构，均遵循“硬件显存/内存容量 vs 55GB 需求”的计算模式，且父节点已给出具体型号、容量范围和价格区间，子节点重复罗列了这些已知参数，存在信息冗余。）

## Search Query

Mac Studio M3 Ultra 512GB LLM inference Qwen3-27B 32k context feasibility

## Retrieval Sources

- {'url': 'https://cloud.baidu.com/article/3733336&rut=8496a2d56097d3ba16175a099a4ff90fc94ccb3d94c5330e68d9a4b938b16b3b', 'type': 'ddg', 'title': '多型号显卡性能深度对比：Rtx 3090/4090与nvidia专业卡全解析'}
