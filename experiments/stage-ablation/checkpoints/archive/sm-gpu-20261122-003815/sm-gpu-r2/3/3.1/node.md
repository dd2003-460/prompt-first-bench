# N19: 精度对模型质量的影响量化基准：BF16 为基准 (0% 退化)。FP8 (E4M3/E5M2) 在 LLM 上通常退化 <1-2% (perplexity 或 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

精度对模型质量的影响量化基准：BF16 为基准 (0% 退化)。FP8 (E4M3/E5M2) 在 LLM 上通常退化 <1-2% (perplexity 或 benchmark 分数) [待核验]。INT8 量化退化 ~1-3%。INT4 (GPTQ/AWQ) 退化 ~3-8% [待核验]。NVFP4 退化 ~2-5% [待核验]。

## Corrected Claim

精度对模型质量的影响量化基准：BF16 为基准 (0% 退化)。FP8 (E4M3/E5M2) 在 LLM 上通常退化极小（训练 loss 差距 <0.25%，推理退化通常 <1-2%）。INT8 量化退化通常较小（~1-3%）。INT4 (GPTQ/AWQ) 退化相对明显（~3-8%，视算法和模型而定）。NVFP4 退化预期在 ~2-5% 之间（数据较少，需更多验证）。

## Evidence

[质询]数值范围缺乏统一基准：不同模型规模、量化算法（如GPTQ vs AWQ vs SmoothQuant）及评估指标（Perplexity vs MMLU vs HumanEval）下的退化率差异巨大，直接给出固定区间（如INT4 3-8%）容易误导，且NVFP4作为较新格式，其广泛认可的基准数据尚不充分。 | 来源[2]提供了FP8训练与BF16 loss差距<0.25%的间接支持，但未直接覆盖推理场景下的Perplexity/Benchmark退化率；来源[1]和[3]仅定性提及精度下降，未提供具体数值区间，无法直接支持claim中的具体百分比范围。

## Search Query

FP8 INT8 INT4 quantization quality degradation LLM perplexity benchmark comparison

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2049244381027292133&rut=30ea8626e1f6abdc1ae33572b84eaf1111e96f0deca06d87e99d49868ff156c8', 'type': 'ddg', 'title': 'Nvfp4、Fp8、Bf16 大模型量化格式详解 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/2096296022972575873&rut=844083f502d7dcf9e19b6338c0ec0fdde217b941419d78f475dd4b85949d3ee5', 'type': 'ddg', 'title': '图解大模型推理：量化基础。数据如何从 Bf16 到 Fp8，推理又快在哪里。 - 知乎'}
- {'url': 'https://www.zhihu.com/question/2049156886239491024&rut=d24ee5043987bbe5e56e8a0f29a12e90ee7a41923ebca00d11562ce1041d5da1', 'type': 'ddg', 'title': 'Ai 大模型的精度格式，Bf16 / Fp8 / Mxfp4 / Int4 等是如何决策选型的？'}
