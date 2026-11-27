# N29: 在INT8精度下，NVIDIA RTX 4090 (24GB) 运行 Qwen3-27B 的稳态生成吞吐率（Token/s）约为 20-30，首Token延迟（

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

在INT8精度下，NVIDIA RTX 4090 (24GB) 运行 Qwen3-27B 的稳态生成吞吐率（Token/s）约为 20-30，首Token延迟（TTFT）约为 2-4s，每Token生成时间（TPOT）约为 33-50ms

## Corrected Claim

在INT8精度下，NVIDIA RTX 4090 (24GB) 运行 Qwen3-27B 的稳态生成吞吐率（Token/s）约为 20-30，首Token延迟（TTFT）约为 2-4s，每Token生成时间（TPOT）约为 33-50ms（注：参考来源针对 Qwen3.8-27B，数值需以具体模型版本实测为准）

## Evidence

[质询]参考来源标题明确提及的是 'Qwen3.8-27B'（或类似变体），而待核验事实指定为 'Qwen3-27B'。虽然参数量相同，但不同版本/微调版本的模型在量化后的实际推理性能（尤其是TTFT和TPOT）可能存在差异，且来源摘要未直接提供具体的数值区间，仅表明有实测数据，无法直接确认数值完全匹配。 | 来源[1]主题相关（RTX 4090D 24GB 部署 27B 模型），但标题模型名称与事实节点略有出入（Qwen3.8 vs Qwen3），且摘要未直接展示具体吞吐率数值，属于间接支持或需进一步验证的细节，故降级。

## Search Query

NVIDIA RTX 4090 Qwen3-27B INT8 inference throughput tokens per second TTFT TPOT

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2083555506732512359&rut=cfac76ade0bcbc3ce835d2eeb7969c8fad6071731337957cc1a252fb3f9a50d1', 'type': 'ddg', 'title': '24GB 显存榨干指南：RTX 4090D 部署 Qwen3.8-27B 全流程实测'}
