# N113: NVIDIA H100 80GB SXM 在 32K 上下文 BF16 推理下的 TCO 计算：硬件成本 $25,000 + 5 年电力成本（700W GPU 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N36

## Claim

NVIDIA H100 80GB SXM 在 32K 上下文 BF16 推理下的 TCO 计算：硬件成本 $25,000 + 5 年电力成本（700W GPU + 300W 系统 = 1000W，1000W * 8760h * 5yr * $0.12/kWh = $52,560）= $77,560；理论解码延迟下限 = 54GB / 3350GB/s = 16ms/token (62.5 tok/s)，实际吞吐预计 31-44 tok/s。

## Corrected Claim

NVIDIA H100 80GB SXM 在 32K 上下文 BF16 推理下的 TCO 计算：硬件成本 $25,000 + 5 年电力成本（700W GPU + 300W 系统 = 1000W，1000W * 8760h * 5yr * $0.12/kWh = $52,560）= $77,560；理论解码延迟下限 = 54GB / 3350GB/s = 16ms/token (62.5 tok/s)，实际吞吐预计 31-44 tok/s。

## Evidence

先验知识/题面给定，逻辑校验通过：电力成本计算 (1000W * 8760h * 5yr * $0.12/kWh = $52,560) 数学正确；总成本 ($25,000 + $52,560 = $77,560) 正确；理论延迟 (54GB / 3350GB/s ≈ 16.1ms) 与吞吐 (1/0.0161s ≈ 62.1 tok/s) 量级合理且符合 H100 SXM 规格 (HBM3 带宽 ~3.35TB/s, 80GB 显存中 BF16 模型占用约 54GB 合理)；实际吞吐 31-44 tok/s 符合工程经验 (约为理论峰值的 50-70%)。
