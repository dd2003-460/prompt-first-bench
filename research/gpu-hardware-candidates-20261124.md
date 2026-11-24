# GPU 硬件候选集（#53 V_fine 判断输入 / #10 瓶颈判断模块）

> 来源：ChatGPT (Google grounding) 2026-11-24 查询，单源；标"推导"的为按规格关系推算非官方直列。Dense 口径。
> 用途：#53 交叉梯度实验的硬件候选集；"判断型瓶颈"的可算输入（精度算力比 × workload 构成 × 标量占比 × 带宽）。

## spec 表（Dense）

| | 5090 (Blackwell GB202) | Thor T5000 (Jetson) | 4090 (Ada AD102) | A100 80G SXM (Ampere) |
|---|---|---|---|---|
| SM | 170 | 20 (10 TPC×2 推导) | 128 | 108 |
| CUDA core | 21760 | 2560 | 16384 | 6912 |
| FP16 tensor TFLOPS | 419 | ~258 (推导) | 114 | 312 |
| FP8 TFLOPS | 838 | 517 | N/A (4090 白皮书) | 无 |
| FP4 TFLOPS | 1677 | 1035 | 无 | 无 |
| INT8 TOPS | ~838 | ~517 | 228 | 624 |
| 显存带宽 GB/s | 1792 (32G GDDR7) | 273 (128G LPDDR5X) | 1008 | 2039 |

## 关键口径纠正

- Ada FP8：专业卡 (RTX 5000 Ada) 有，4090 白皮书标 N/A。"ada 有 fp8 没有 fp4" 对专业卡成立。
- Ampere：INT8 有 (624 TOPS)，FP8 无。
- RTX Spark = 2026-05 发布 Grace CPU + Blackwell GPU 平台（6144 CUDA core / 最高 1 PFLOP FP4 / 128GB 统一内存），非独立 GPU 型号。
- Sparse 口径 = 2× Dense（NVIDIA AI TOPS 常用 2:4 稀疏），不可与 Dense 混比。

## 判断型瓶颈示例（浅层枚举给不出，深层分解才出）

1. **5090 fp16 发射砍半 + 层级多运算**：标量算子 (norm/activation, 走 CUDA core) 随层数累积；标量占 40% 时间 → 整体慢 40%。瓶颈判断 = 标量/issue-bound 占比。
2. **T5000 高精度 workload**：FP16 算力 = FP4 的 1/4 + CUDA core 弱 5090 的 8.5× + 带宽 273 GB/s 弱 6.6×。70% FP4 + 30% FP16 workload → FP16 占 63% 时间；50% FP16 → 占 78%；叠加标量/带宽 → 瓶颈比例 80%+。隐藏杀手：低精度计算够快反把带宽逼成瓶颈。
