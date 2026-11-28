# N28: Qwen3-27B 在 FP8 (E4M3/E5M2) 精度下的 Perplexity 增量 ΔPPL 通常小于 0.05 绝对值（相对增量 <0.5%），MM

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B 在 FP8 (E4M3/E5M2) 精度下的 Perplexity 增量 ΔPPL 通常小于 0.05 绝对值（相对增量 <0.5%），MMLU 基准测试得分下降 <1 分，被视为‘无损’或‘近无损’阈值；而 INT4 AWQ 的 ΔPPL 通常在 0.1-0.3 之间，MMLU 下降 2-5 分。

## Corrected Claim

Qwen 系列 27B 模型（如 Qwen3-27B 或 Qwen3.8-27B）在 FP8 精度下通常表现为近无损（ΔPPL < 0.05, MMLU 下降 < 1 分），而 INT4 AWQ 量化通常带来更明显的性能下降（ΔPPL 0.1-0.3, MMLU 下降 2-5 分）。

## Evidence

[质询]参考来源标题及摘要中提及的模型名称为 'Qwen3.8-27B'，而待核验事实节点指定为 'Qwen3-27B'，存在版本/型号不匹配的风险；此外，来源摘要仅涉及部署和提示词工程，未提供具体的 PPL 或 MMLU 量化损失数值，无法直接证实具体的阈值数据。 | 来源 [1][2][3] 主题相关（均为 Qwen 系列 27B 模型的 FP8 量化部署），但摘要内容未包含具体的精度损失数值（ΔPPL/MMLU drop），属于间接支持或无直接证据；鉴于 FP8 通常被视为近无损而 INT4 有损符合一般量化常识，逻辑自洽，但因缺乏直接数值证据且存在型号名称细微差异（Qwen3 vs Qwen3.8），降级处理。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=703955979b9fa5473f892e9cc833e8a83c17da81ae43d0b61ec72f10a13a0f3e', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
- {'url': 'https://blog.csdn.net/lovely_yoshino/article/details/163828474&rut=192ecaaa156b7d4665f044540bdc380324c10d7930b125ada57a1e24c2ae9caa', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 部署实践：从原理到生产 - CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/152202097&rut=c046297bef40ab48e8dc7dc73105386570c5422fdfb67e48be265d405a7f944a', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 提示词工程指南：10 个让多模态大模型发挥全部实力的技巧_丁淳凝-亚马逊云科技技术品牌专区'}
