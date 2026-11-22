# N400: Apple M4 Max在INT8精度、Batch=1、Seq_len=32K时的总显存占用为：模型权重27GB + KV Cache 10.7GB + 框架/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N143

## Claim

Apple M4 Max在INT8精度、Batch=1、Seq_len=32K时的总显存占用为：模型权重27GB + KV Cache 10.7GB + 框架/系统开销~10GB ≈ 47.7GB，低于可用上限96GB，显存利用率仅50%，允许提升Batch至4或Seq_len至64K而不溢出。

## Corrected Claim

Apple M4 Max在INT8精度、Batch=1、Seq_len=32K时的总显存占用为：模型权重27GB + KV Cache 10.7GB + 框架/系统开销~10GB ≈ 47.7GB，低于可用上限96GB，显存利用率仅50%，允许提升Batch至4或Seq_len至64K而不溢出。

## Evidence

先验知识/题面给定，逻辑校验通过：M4 Max 128GB 版本可用显存约 96GB，47.7GB 占用低于上限且利用率约 50%，数值量级与逻辑自洽。
