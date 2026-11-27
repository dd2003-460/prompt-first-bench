# N138: 性价比量化指标定义为 '每美元每秒 Token 数' (Tokens/s per $)，计算公式为：(实际测得 TPOT 倒数) / (硬件 TCO_3yr /

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比量化指标定义为 '每美元每秒 Token 数' (Tokens/s per $)，计算公式为：(实际测得 TPOT 倒数) / (硬件 TCO_3yr / 36个月)。其中 TCO_3yr 包含购置成本、3 年电费、散热摊销及预期维修成本。该指标用于横向对比不同精度和硬件组合的最终经济性。

## Corrected Claim

性价比量化指标通常定义为'每美元每秒Token数' (Tokens/s per $)，用于横向对比不同精度和硬件组合的经济性。具体计算公式和TCO构成可能因评估标准而异，常见做法包括将吞吐量（如TPOT倒数）除以总拥有成本（TCO）。

## Evidence

[质询]来源仅支持'每美元Token数'这一宏观概念，未提供具体的计算公式（如TPOT倒数除以TCO/36个月）或TCO的具体构成细节（如是否包含散热摊销、维修成本等），存在将通用概念具体化为特定公式的风险。 | 来源[1]直接支持'每美元token数'作为AI推理性价比指标的定义，但缺乏对具体计算公式和TCO构成的直接支持，属于间接支持。

## Retrieval Sources

- {'url': 'https://inferencex.semianalysis.com/zh/glossary/tokens-per-dollar&rut=21d1e7b540d9cd084c283fac646b65c62c02d55933308354a31a27e5c6f1ca9c', 'type': 'ddg', 'title': '每美元 token 数：AI 推理定义 | InferenceX by SemiAnalysis'}
- {'url': 'https://aieng-zh.cn/glossary/tokens-per-second-tps&rut=29f154050a62e07caf68c8bd72618bd105bb5c9c6231f42c5f3533822bd93e2c', 'type': 'ddg', 'title': 'Tokens per Second (TPS)：定义、示例与常见混淆'}
- {'url': 'https://inferensys.com/glossary/agentic-observability-and-telemetry/agent-performance-benchmarking/tokens-per-second-tps&rut=0b39f59b780bc66042fb457ba33b6a3f47ab17c98a18eaa9725ced431a885a07', 'type': 'ddg', 'title': 'Tokens Per Second (TPS): AI Throughput Metric Explained'}
