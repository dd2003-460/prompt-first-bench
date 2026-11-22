# N356: 24GB 显卡运行 Qwen3-27B INT8 32K 上下文的总显存需求：Total_GB = 27 GB (Weights) + 4.0 GB (KV) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

24GB 显卡运行 Qwen3-27B INT8 32K 上下文的总显存需求：Total_GB = 27 GB (Weights) + 4.0 GB (KV) + 3.0 GB (Activation) + 1.0 GB (Framework Overhead) ≈ 35 GB，超出 24GB 上限 11 GB，确认不可行

## Corrected Claim

24GB 显卡运行 Qwen3-27B INT8 32K 上下文的总显存需求：Total_GB = 27 GB (Weights) + 4.0 GB (KV) + 3.0 GB (Activation) + 1.0 GB (Framework Overhead) ≈ 35 GB，超出 24GB 上限 11 GB，确认不可行

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型INT8权重约27GB，加上KV Cache、激活值及框架开销，总显存需求约35GB，确实超出24GB显卡上限，结论符合工程常识。
