# N346: MI300X 推理框架对 MoE 稀疏性的利用效率取决于是否实现 Expert Parallelism 或 Tensor Parallelism 下的稀疏掩码优

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N129, N130, N131

## Claim

MI300X 推理框架对 MoE 稀疏性的利用效率取决于是否实现 Expert Parallelism 或 Tensor Parallelism 下的稀疏掩码优化；当前主流框架（vLLM/SGLang）在 AMD 平台上对 MoE 的稀疏激活优化尚不成熟，实际计算量往往接近全参数加载（27.18B）而非激活参数（3.3B），导致理论 TPOT 1.25ms 难以达成，实际可能接近 10ms 量级。

## Corrected Claim

MI300X 推理框架对 MoE 稀疏性的利用效率取决于是否实现 Expert Parallelism 或 Tensor Parallelism 下的稀疏掩码优化；当前主流框架（vLLM/SGLang）在 AMD 平台上对 MoE 的稀疏激活优化若未充分实现，实际计算量可能接近全参数加载（27.18B）而非激活参数（3.3B），导致理论 TPOT 难以达成，实际延迟可能显著高于理论值。

## Evidence

[质询]该陈述包含具体的性能数值（理论 TPOT 1.25ms，实际 10ms）和特定框架在特定硬件上的成熟度判断，属于经验事实。虽然逻辑上‘未优化稀疏性导致计算量接近全参数’是合理的，但具体的延迟数值（1.25ms vs 10ms）缺乏基准测试支持，且‘尚不成熟’的定性判断可能随版本更新快速变化，存在时效性和具体数值不准确的风险。 | 先验知识/题面给定，逻辑校验通过：MoE 稀疏性优化确实依赖 Expert Parallelism 等机制，若未实现则计算量接近全参数，逻辑自洽；但具体延迟数值为经验事实，无来源支持，故降级。

## Search Query

vLLM SGLang MoE sparse activation optimization AMD MI300X
