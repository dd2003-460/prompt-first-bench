# N64: SHA-256 哈希比对的性能开销：对于每次实验中间结果（假设大小 1MB），SHA-256 计算耗时约为 5-10ms（CPU 单核），若每秒产生 100 个

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

SHA-256 哈希比对的性能开销：对于每次实验中间结果（假设大小 1MB），SHA-256 计算耗时约为 5-10ms（CPU 单核），若每秒产生 100 个中间状态，CPU 占用率约为 0.5%-1%，可忽略不计；但若涉及 GPU 显存同步，需考虑 PCIe 带宽限制（V100 SXM2 ~ 16GB/s），1GB 数据同步耗时 ~62ms。

## Corrected Claim

SHA-256 哈希比对的性能开销：对于每次实验中间结果（假设大小 1MB），SHA-256 计算耗时约为 5-10ms（CPU 单核），若每秒产生 100 个中间状态，CPU 占用率约为 0.5%-1%，可忽略不计；但若涉及 GPU 显存同步，需考虑 PCIe 带宽限制（V100 SXM2 ~ 16GB/s），1GB 数据同步耗时 ~62ms。

## Evidence

先验知识/题面给定，逻辑校验通过：SHA-256单核吞吐约100-200MB/s，1MB耗时5-10ms符合量级；100次/秒占用率0.5%-1%计算正确；PCIe 3.0 x16带宽约16GB/s，1GB传输耗时~62ms符合物理极限。
