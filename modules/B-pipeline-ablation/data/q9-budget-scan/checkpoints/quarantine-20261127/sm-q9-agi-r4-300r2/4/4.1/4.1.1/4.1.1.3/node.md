# N161: 工作点 C（高可靠性/长文本）：关闭 MTP（K=0），纯自回归生成，Throughput_eff = Base_TPS = 15 tok/s，T_local(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

工作点 C（高可靠性/长文本）：关闭 MTP（K=0），纯自回归生成，Throughput_eff = Base_TPS = 15 tok/s，T_local(10k tokens) ≈ 667s；此配置下无投机失败风险，适合对确定性要求极高的逻辑推理步骤，但速度最慢

## Corrected Claim

工作点 C（高可靠性/长文本）：关闭 MTP（K=0），纯自回归生成，Throughput_eff = Base_TPS = 15 tok/s，T_local(10k tokens) ≈ 667s；此配置下无投机失败风险，适合对确定性要求极高的逻辑推理步骤，但速度最慢

## Evidence

先验知识/题面给定，逻辑校验通过：10000 tokens / 15 tok/s ≈ 666.67s，数值量级与计算逻辑自洽；MTP K=0 对应纯自回归模式，无投机失败风险符合技术定义。

## Search Query

autonomous regression inference speed vs speculative decoding reliability long context
