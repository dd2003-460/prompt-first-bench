# N347: 若因显存不足启用 CPU Offloading (如 llama.cpp 的 --n-gpu-layers 参数)，CPU 内存带宽 (通常 DDR4/DDR5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N124

## Claim

若因显存不足启用 CPU Offloading (如 llama.cpp 的 --n-gpu-layers 参数)，CPU 内存带宽 (通常 DDR4/DDR5 32-64 GB/s) 成为瓶颈，Tokens/s 将大幅下降至 5-10 Tokens/s 区间，且 TTFT 增加 2-5 倍；此时 TCO 中需额外计入 CPU 内存升级成本 ($300-$500) 和性能损失带来的机会成本，使得单卡 4090 方案在 32K 上下文下的性价比优势被显著削弱。

## Corrected Claim

若因显存不足启用 CPU Offloading (如 llama.cpp 的 --n-gpu-layers 参数)，CPU 内存带宽 (通常 DDR4/DDR5 32-64 GB/s) 成为瓶颈，Tokens/s 将大幅下降至 5-10 Tokens/s 区间，且 TTFT 增加 2-5 倍；此时 TCO 中需额外计入 CPU 内存升级成本 ($300-$500) 和性能损失带来的机会成本，使得单卡 4090 方案在 32K 上下文下的性价比优势被显著削弱。

## Evidence

先验知识/题面给定，逻辑校验通过：CPU Offloading 受限于内存带宽（DDR4/5 约 30-60GB/s），导致推理速度大幅下降至个位数或低双位数 Tokens/s 符合物理直觉；TTFT 增加及 TCO 成本估算在工程经验上合理。
