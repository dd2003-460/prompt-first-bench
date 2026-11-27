# N24: 候选集必须包含以下架构/代际/容量组合：消费级 (RTX 3090/4090/5090, 24-32GB, $1600-$2000), 数据中心 (A100/H

- **status**: degraded
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

[质询]陈述中关于Mac Studio M2/M3 Ultra的内存带宽（800GB/s-1.2TB/s）和价格区间（$4k-$10k）属于具体经验参数，且参考来源[1]仅覆盖NVIDIA消费级显卡，完全未涉及Apple Silicon或数据中心GPU，无法提供外部支持；此外，'遗漏Mac方案将导致无可行解'这一因果推断过于绝对，忽略了多卡互联（如NVLink）或量化技术等其他潜在解决方案。 | 来源[1]仅支持RTX 3090/4090的显存规格（24GB），与陈述部分一致；但Mac Studio及数据中心GPU的具体参数（带宽、价格）缺乏来源支持，且属于经验事实，逻辑自洽但缺来源直接支持。

## Search Query

Mac Studio M3 Ultra 512GB LLM inference Qwen3-27B 32k context feasibility

## Retrieval Sources

- {'url': 'https://cloud.baidu.com/article/3733336&rut=8496a2d56097d3ba16175a099a4ff90fc94ccb3d94c5330e68d9a4b938b16b3b', 'type': 'ddg', 'title': '多型号显卡性能深度对比：Rtx 3090/4090与nvidia专业卡全解析'}
