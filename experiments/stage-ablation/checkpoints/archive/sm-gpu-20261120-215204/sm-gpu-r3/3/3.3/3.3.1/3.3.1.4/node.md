# N256: N88 中声称的 '33.5GB/卡' 显存分配错误源于未正确应用 Tensor Parallelism 对 KV Cache 的切分逻辑；正确的 TP 策略下

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88, N89, N90

## Claim

N88 中声称的 '33.5GB/卡' 显存分配错误源于未正确应用 Tensor Parallelism 对 KV Cache 的切分逻辑；正确的 TP 策略下，KV Cache 应与权重一样均分，而非全量复制，因此单卡负载应减半。

## Corrected Claim

N88 中声称的 '33.5GB/卡' 显存分配错误源于未正确应用 Tensor Parallelism 对 KV Cache 的切分逻辑；正确的 TP 策略下，KV Cache 应与权重一样均分，而非全量复制，因此单卡负载应减半。

## Evidence

先验知识/题面给定，逻辑校验通过：在标准 Tensor Parallelism 策略下，KV Cache 确实随注意力头切分而均分，单卡负载减半符合基本原理。
