# N306: Estimated_Tokens_Lifetime 中的 Lifespan_Years 参数：消费级 GPU 的硬件物理寿命通常为 5-7 年，但软件支持（驱动

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N121

## Claim

Estimated_Tokens_Lifetime 中的 Lifespan_Years 参数：消费级 GPU 的硬件物理寿命通常为 5-7 年，但软件支持（驱动/框架兼容性）寿命通常为 3-5 年。在 TCO 计算中，建议采用保守的 3 年作为主要计算周期，或采用 5 年并引入软件过时折损因子 (Software_Depreciation_Factor = 0.5)。

## Corrected Claim

Estimated_Tokens_Lifetime 中的 Lifespan_Years 参数：消费级 GPU 的硬件物理寿命通常为 5-7 年，但软件支持（驱动/框架兼容性）寿命通常为 3-5 年。在 TCO 计算中，建议采用保守的 3 年作为主要计算周期，或采用 5 年并引入软件过时折损因子 (Software_Depreciation_Factor = 0.5)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

consumer GPU software support lifespan years LLM inference driver compatibility
