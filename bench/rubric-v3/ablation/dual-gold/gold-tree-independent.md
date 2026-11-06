# Independent Gold Tree — H100 PCIe vs SXM 推理吞吐差异

> origin: ai · constructed 2026-11-06 by Lead (local, arena channel dead)
> Methodology-type gold: decomposition structure + public-fact assertions.
> All values from NVIDIA official specs (H100 datasheet, Jan 2022) + first-principles arithmetic.
> NOT derived from gold-tree.md or calc.py.

## Root Question

H100 PCIe vs SXM：跑 LLM 推理，什么场景下 SXM 优势大/小？快多少？

## Decomposition Tree

```
R   每 token 生成延迟 t_decode [ms/tok]              (目标函数)
│   t_decode = max(t_memory, t_compute)  ← decode 通常 memory-bound
│
├─ A   显存带宽瓶颈（decode 主导项）
│  │   t_mem = bytes_per_token / BW_effective
│  ├─ A.1  每 token 读取字节数
│  │  │   = W_bytes + n×KV_bytes (n = 并发流数)
│  │  ├─ A.1.1  权重字节 W_bytes
│  │  │         FP16: 2B×params | INT8: 1B×params | INT4: 0.5B×params
│  │  │         例: 70B model → FP16=140GB, INT8=70GB, INT4=35GB
│  │  └─ A.1.2  每流 KV cache 字节
│  │            ≈ 2 × n_layers × d_ff × seq_len × sizeof(dtype)
│  │            例: Llama-2-70B (80L, d_ff=2816, ctx=4K, FP16) ≈ 2.9 GB/stream
│  └─ A.2  有效显存带宽 BW_effective
│     │   = BW_peak × η_bw (η_bw ≈ 0.7-0.9, 取决于访问模式/框架)
│     ├─ A.2.1  H100 SXM:   BW_peak = 3.35 TB/s  → effective ≈ 2.3-3.0 TB/s
│     └─ A.2.2  H100 PCIe:  BW_peak = 2.00 TB/s  → effective ≈ 1.4-1.8 TB/s
│
├─ B   计算瓶颈（prefill 主导项）
│  │   t_prefill = prefill_FLOPs / (num_gpus × TFLOPS_peak × MFU × tp_eff)
│  ├─ B.1  prefill 计算量
│  │       ≈ 2 × params × n_input_tokens (matrix multiply bound)
│  │       例: 70B × 2048 tokens ≈ 287 TFLOP
│  └─ B.2  峰值算力
│     ├─ B.2.1  H100 SXM:   989 TFLOPS (FP16, dense) | 1979 (sparse)
│     └─ B.2.2  H100 PCIe:  756 TFLOPS (FP16, dense) | 1513 (sparse)
│        → prefill 算力比 = 989/756 ≈ 1.31x (SXM 快)
│
├─ C   多卡互联（TP ≥ 2 时成为决定项）
│  │   TP 通信量 ∝ hidden_size × batch; 延迟 ∝ 1/BW_interconnect
│  ├─ C.1  NVLink (SXM):    900 GB/s bidirectional (NVSwitch full mesh)
│  ├─ C.2  PCIe Gen5 x16:   ~64 GB/s unidirectional (~128 GB/s bidi)
│  │   → 互联带宽比 = 900/64 ≈ 14x (SXM)
│  │   ⚠ 这是互联带宽比，NOT 单卡吞吐比。单卡 decode 差距由 A 决定 (~1.68x)。
│  └─ C.3  适用条件: 仅当 TP≥2 且 allreduce 频率高（大 batch/长序列）时 C 成为瓶颈
│
├─ D   功耗与散热约束
│  ├─ D.1  H100 SXM:   TDP = 700W (liquid cooling 或专用风冷机箱)
│  ├─ D.2  H100 PCIe:  TDP = 350W (标准服务器风冷)
│  │   → 同机箱 8 卡: SXM 需 5.6kW 供电+散热; PCIe 只需 2.8kW
│  └─ D.3  实际影响: 功耗墙可能迫使 SXM 降频 (throttle), 缩小实际差距
│
├─ E   显存容量（约束项）
│  ├─ E.1  两版均为 80GB HBM3 (容量相同)
│  └─ E.2  容量不是 PCIe vs SXM 的区分维度; 是 H100 vs 其他卡的区分维度
│
└─ F   价格维度（题面未给，应识别为缺口）
   ├─ F.1  SXM 系统级成本 >> PCIe 卡价 (需 NVSwitch 基板/专用机箱)
   └─ F.2  性价比拐点: 单卡场景 PCIe 更优; 多卡 TP 场景 SXM 总成本仍可能更低
```

## Key Assertions (for M1 scoring)

| # | Assertion | Value | Source |
|---|-----------|-------|--------|
| 1 | H100 SXM HBM bandwidth | 3.35 TB/s | NVIDIA H100 datasheet |
| 2 | H100 PCIe HBM bandwidth | 2.00 TB/s | NVIDIA H100 datasheet |
| 3 | Decode speed ratio (BW-limited) | 3.35/2.0 ≈ 1.68x | Arithmetic |
| 4 | H100 SXM FP16 dense TFLOPS | 989 TFLOPS | NVIDIA H100 datasheet |
| 5 | H100 PCIe FP16 dense TFLOPS | 756 TFLOPS | NVIDIA H100 datasheet |
| 6 | Prefill compute ratio | 989/756 ≈ 1.31x | Arithmetic |
| 7 | NVLink bandwidth (SXM) | 900 GB/s | NVIDIA H100 datasheet |
| 8 | PCIe Gen5 x16 bandwidth | ~64 GB/s (uni) | PCI-SIG spec |
| 9 | Interconnect bandwidth ratio | 900/64 ≈ 14x | Arithmetic |
| 10 | "14x" is interconnect ratio, NOT single-card throughput ratio | True | Logical deduction |
| 11 | H100 SXM TDP | 700W | NVIDIA H100 datasheet |
| 12 | H100 PCIe TDP | 350W | NVIDIA H100 datasheet |
| 13 | Both versions have 80GB HBM3 | True | NVIDIA H100 datasheet |
| 14 | NVLink matters only for multi-GPU TP | True | System architecture |
| 15 | Single-card decode gap dominated by BW ratio (~1.68x), not interconnect | True | First principles |

## Conditional Conclusions

- **Single card, decode-heavy (small batch, long generation)**: SXM faster by ~1.68x (BW-limited). PCIe is the cost-efficient choice.
- **Single card, prefill-heavy (large context, short output)**: SXM faster by ~1.31x (compute-limited). Gap narrows.
- **Multi-card TP≥2**: SXM advantage amplifies — interconnect 14x means allreduce overhead is negligible on SXM but significant on PCIe. Effective speedup can exceed 1.68x.
- **Power-constrained deployment**: PCIe (350W) fits standard server; SXM (700W) needs dedicated cooling. Throttling may reduce SXM's theoretical advantage.
- **Price per token**: PCIe likely cheaper at single-card scale; SXM wins at multi-card scale where NVLink eliminates communication bottleneck.

## Identified Gaps (should be flagged as uncertainty)

1. Workload unspecified (batch size, sequence length, model size) → cannot give single number
2. Framework optimization level unknown (vLLM vs raw PyTorch changes effective BW utilization)
3. Price dimension absent from question stem → cost-per-token comparison incomplete
4. No measured benchmark data in prompt → all numbers are spec-sheet upper bounds
5. Thermal throttling behavior workload-dependent → actual gap may be smaller than spec ratio
