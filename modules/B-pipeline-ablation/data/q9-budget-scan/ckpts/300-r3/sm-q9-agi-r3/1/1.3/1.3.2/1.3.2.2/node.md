# N149: 工作点 B（长上下文低并发）：设置 max_model_len=262144, max_num_seqs=1。单序列 KV Cache 占用为 262144 *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

工作点 B（长上下文低并发）：设置 max_model_len=262144, max_num_seqs=1。单序列 KV Cache 占用为 262144 * 128KB ≈ 32.7GB，总需求 32.7GB，低于 48.5GB 可用内存，无抢占风险。此配置支持单次超长科研推理循环，但系统处于单线程模式，无法并行处理多个假设验证任务，导致总吞吐受限。

## Corrected Claim

工作点 B（长上下文低并发）：设置 max_model_len=262144, max_num_seqs=1。单序列 KV Cache 占用为 262144 * 128KB ≈ 32.7GB，总需求 32.7GB，低于 48.5GB 可用内存，无抢占风险。此配置支持单次超长科研推理循环，但系统处于单线程模式，无法并行处理多个假设验证任务，导致总吞吐受限。

## Evidence

先验知识/题面给定，逻辑校验通过：262144 * 128KB = 32.7GB，小于48.5GB，计算无误且符合单序列KV Cache估算逻辑。
