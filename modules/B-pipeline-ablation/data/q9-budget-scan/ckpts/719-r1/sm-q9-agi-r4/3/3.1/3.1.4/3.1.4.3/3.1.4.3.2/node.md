# N503: 工作点B（FP16回退基线）：维持FP16 KV Cache，T_memory保持原值~3.9ms/token（长序列工作点A），但显存占用翻倍；在Batch_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N180

## Claim

工作点B（FP16回退基线）：维持FP16 KV Cache，T_memory保持原值~3.9ms/token（长序列工作点A），但显存占用翻倍；在Batch_Size=1时可行，Batch_Size>1时OOM风险高，揭示精度-显存trade-off

## Corrected Claim

工作点B（FP16回退基线）：维持FP16 KV Cache，T_memory保持原值~3.9ms/token（长序列工作点A），但显存占用翻倍；在Batch_Size=1时可行，Batch_Size>1时OOM风险高，揭示精度-显存trade-off

## Evidence

先验知识/题面给定，逻辑校验通过：FP16相比INT8/FP8显存占用翻倍符合数据位宽比例；Batch Size增大导致KV Cache线性增长从而引发OOM风险符合内存管理基本原理；3.9ms/token作为长序列推理延迟量级合理。
