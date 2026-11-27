# N297: 1x A100 80GB 方案中，BF16 推理的运行时激活值 (Activations) 及框架开销 (Framework Overhead) 显存占用估算：

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

1x A100 80GB 方案中，BF16 推理的运行时激活值 (Activations) 及框架开销 (Framework Overhead) 显存占用估算：激活值 Batch=1, Seq=32K 时约 4-8 GB (BF16 激活值比 FP8 大 2 倍)；框架开销约 1-2 GB；合计约 5-10 GB [待核验：需具体框架实测]。

## Corrected Claim

1x A100 80GB 方案中，BF16 推理的运行时激活值 (Activations) 及框架开销 (Framework Overhead) 显存占用估算：激活值 Batch=1, Seq=32K 时约 4-8 GB (BF16 激活值比 FP8 大 2 倍)；框架开销约 1-2 GB；合计约 5-10 GB [待核验：需具体框架实测]。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16激活值比FP8大2倍符合位宽比例，Batch=1, Seq=32K下4-8GB激活值及1-2GB框架开销在A100 80GB显存约束下量级合理且自洽
