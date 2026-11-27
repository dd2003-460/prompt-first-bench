# N742: Kernel Launch Overhead 量化：每次 CUDA Kernel 启动开销约为 5-10 μs。TP=4 每层需启动 ~4-6 个通信 Kern

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N229

## Claim

Kernel Launch Overhead 量化：每次 CUDA Kernel 启动开销约为 5-10 μs。TP=4 每层需启动 ~4-6 个通信 Kernel（AllReduce 内部实现）和 ~20-30 个计算 Kernel。60 层总 Kernel 数约为 1800-2400 个。总 Kernel Launch 开销约为 $2000 \times 7.5 \mu s \approx 15 \text{ ms}$，分摊到 32K tokens 后为 0.47 μs/token，可忽略；但若 batch=1 且逐 token 生成，每 token 需启动 ~30-40 个 Kernel，开销约为 $35 \times 7.5 \mu s \approx 262.5 \mu s$，与计算时间相当，成为显著瓶颈。

## Corrected Claim

Kernel Launch Overhead 量化：每次 CUDA Kernel 启动开销约为 5-10 μs。TP=4 每层需启动 ~4-6 个通信 Kernel（AllReduce 内部实现）和 ~20-30 个计算 Kernel。60 层总 Kernel 数约为 1800-2400 个。总 Kernel Launch 开销约为 $2000 \times 7.5 \mu s \approx 15 \text{ ms}$，分摊到 32K tokens 后为 0.47 μs/token，可忽略；但若 batch=1 且逐 token 生成，每 token 需启动 ~30-40 个 Kernel，开销约为 $35 \times 7.5 \mu s \approx 262.5 \mu s$，与计算时间相当，成为显著瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过
