# N32: 性价比指标细化：定义 '每有效Token成本' (Cost per Effective Token) = Total_TCO_3yr / (Throughput

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比指标细化：定义 '每有效Token成本' (Cost per Effective Token) = Total_TCO_3yr / (Throughput_tokens_s * Quality_Factor * Operational_Hours)。其中 Quality_Factor 为精度损失系数（BF16=1.0, FP8=0.95, INT8=0.90, W4=0.80 [待核验]），用于修正因精度降低导致的有效产出价值，避免高吞吐但低质量的方案被高估。

## Corrected Claim

性价比指标细化：定义 '每有效Token成本' (Cost per Effective Token) = Total_TCO_3yr / (Throughput_tokens_s * Quality_Factor * Operational_Hours)。其中 Quality_Factor 为精度损失系数，用于修正因精度降低导致的有效产出价值，避免高吞吐但低质量的方案被高估。具体系数需根据特定模型、任务及量化策略通过基准测试（Benchmark）确定，而非使用固定通用值。

## Evidence

[质询]Quality_Factor 的具体数值（BF16=1.0, FP8=0.95, INT8=0.90, W4=0.80）属于经验性工程参数，且标注为[待核验]。不同模型架构、任务类型（如分类 vs 生成）及量化方法（如 GPTQ vs SmoothQuant）下，精度损失差异巨大，不存在通用的固定系数。参考来源仅讨论了“有效Token成本”的概念框架（需关注goodput/有效产出），并未提供这些具体的量化系数，因此无法验证其准确性。 | 来源[1][2][3]支持“每有效Token成本”作为评估指标的逻辑框架（即成本需除以有效产出/质量），但均未提供具体的 Quality_Factor 数值（如 FP8=0.95 等）。该数值为经验事实，缺乏来源直接支持，故降级。

## Retrieval Sources

- {'url': 'https://www.compassingai.com/concept/effective-token-cost/&rut=656291394c3f46b78bd4ae79a7668ab7b8403adac6ca693cb6872d900ab3c391', 'type': 'ddg', 'title': 'Effective Token Cost Effective Token Cost | Compassing AI 概念库'}
- {'url': 'https://www.compassingai.com/zh-hant/concept/effective-token-cost/&rut=e3811d7e08a866c7ca7733c65f9df9477efdcc450ab88cc082ae6becdf58b905', 'type': 'ddg', 'title': 'Effective Token Cost Effective Token Cost | Compassing AI 概念庫'}
- {'url': 'https://amoursec.github.io/aikg/08-benchmark-capacity/cost-model-unit-economics/&rut=ff407f43a5685a6643d30e4da42e708191e14b8c9626df7babbdedd627bf2719', 'type': 'ddg', 'title': '成本模型与单位经济性：Cost per Token、GPU Hour 与有效产出'}
