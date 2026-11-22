# N511: RX 7900 XTX 若采用 FP8 量化（权重 27GB），超出 24GB 显存容量，必须启用 CPU Offload；假设 Offload 20GB 权重

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N177

## Claim

RX 7900 XTX 若采用 FP8 量化（权重 27GB），超出 24GB 显存容量，必须启用 CPU Offload；假设 Offload 20GB 权重至系统内存，GPU 剩余 4GB 用于 KV Cache，最大支持上下文 = 4GB / 256KB = 16,000 tokens，不满足 32K 需求，故 FP8 单卡方案不可行。

## Corrected Claim

RX 7900 XTX 若采用 FP8 量化（权重 27GB），超出 24GB 显存容量，必须启用 CPU Offload。假设 Offload 20GB 权重至系统内存，GPU 剩余 4GB 用于 KV Cache。由于 KV Cache 大小取决于具体模型架构（层数、头数等），若按典型大模型估算（例如每 token 占用 1-2MB），4GB 显存仅能支持 2K-4K tokens 上下文，远低于 32K 需求，故 FP8 单卡方案不可行。

## Evidence

[质询]KV Cache 大小计算存在严重的量级错误。对于主流大模型（如 Llama 3 70B 或同等规模），单个 token 的 KV Cache 占用通常在 1MB-2MB 左右（取决于层数、头数、head_dim 和精度），而非 256KB。即使按 256KB 计算，4GB 显存仅能支持约 16K tokens，但实际中由于 KV Cache 占用更大，支持的上下文长度会更短，或者如果模型较小，256KB 的假设可能偏低，导致结论虽方向正确但数值依据脆弱。更关键的是，'256KB/token' 这一参数缺乏通用性，不同模型差异巨大，直接作为定论依据不够严谨。 | 先验知识/题面给定，逻辑校验通过。虽然结论（FP8 单卡不可行）在工程实践中通常成立（因为 24GB 显存跑 27GB 权重确实需要 offload，且剩余显存难以支撑长上下文），但中间步骤 '4GB / 256KB = 16,000 tokens' 中的 256KB 是特定假设值，并非通用物理常数或第一性原理推导出的固定值，属于经验参数。由于 source 为 knowledge，且核心逻辑（显存不足导致 offload，剩余显存限制上下文）自洽，但具体数值依赖未明确指出的模型架构假设，故降级为 degraded 以提示数值敏感性。
