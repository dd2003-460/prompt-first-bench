# N81: BF16 精度下，除权重和 KV Cache 外，激活值、CUDA Context 及框架碎片化开销约为 1-2 GB，导致实际最低显存门槛从理论 58.096

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

BF16 精度下，除权重和 KV Cache 外，激活值、CUDA Context 及框架碎片化开销约为 1-2 GB，导致实际最低显存门槛从理论 58.096 GB 上升至约 59-60 GB

## Corrected Claim

BF16 精度下，除权重和 KV Cache 外，激活值、CUDA Context 及框架碎片化开销约为 1-2 GB，导致实际最低显存门槛从理论 58.096 GB 上升至约 59-60 GB

## Evidence

先验知识/题面给定，逻辑校验通过：BF16下大模型推理中，除权重和KV Cache外的固定开销（激活值峰值、CUDA Context、框架碎片等）通常在1-2GB量级，符合工程经验与内存管理常识，数值量级合理且逻辑自洽。
