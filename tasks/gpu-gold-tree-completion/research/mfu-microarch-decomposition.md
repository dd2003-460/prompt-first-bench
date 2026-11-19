# MFU 微架构分解调研 note

> origin: ai · 2026-11-19
> 来源：Perplexity（ego-browser，2026-11-19）+ 3 篇 arXiv 论文（ID 已验证真实）
> 任务：T2（MFU 子项定义 + 数值）

## 大白话结论

D 提议的"MFU = SM 占用率 × TensorCore 利用率 × L2 命中率 × kernel 效率"这个 4 因子乘法分解**不成立**——这几个因子量纲不同、分母不同，而且 L2 命中率根本不直接折损 FLOPs（它影响的是访存时延和 HBM 流量，不是计算量）。强行相乘会得到没有物理意义的数。

更严谨的做法：MFU 先拆成"时间占比 × kernel 级 FLOPs 效率"（2 因子，这是 MFU 定义的恒等展开），然后真正落地是**按 kernel 类型分层统计**（dense GEMM / attention / norm / 通信 / launch gap），每类看 NCU 指标。

## 关键结论（带出处）

### 1. 4 因子乘法分解不成立

Perplexity 逐项评估：

| 因子 | 能否作乘法因子 | 问题 |
|---|---|---|
| SM 占用率 | 不能直接 | 衡量并发度（驻留 warp 数），不是已执行 FLOPs 比例；高占用也可能因访存等待而低吞吐 |
| TensorCore 利用率 | 接近但需精确定义 | "Tensor pipe 活跃周期占比"是时间占用，"Tensor FLOPs/峰值"是吞吐，二者不等 |
| L2 命中率修正 | 不能 | 命中率影响时延和 HBM 流量，不线性决定 FLOPs 效率；compute-bound GEMM 可以 L2 命中低却 MFU 高 |
| kernel 效率 | 可以但重复计数 | 若已含 TensorCore 利用率，再乘一次重复计入 |

出处：Perplexity + arXiv:2609.12923（"Dissecting GPU Utilization for LLM Inference on Nvidia Hopper"，明确批评把 sm__throughput 当 occupancy 的误用）

### 2. 更严谨的 2 因子分解（恒等式）

```
MFU = (T_kernel / T_step) × (ΣF_k / (T_kernel × C_peak))
      └─ GPU 有效时间占比 ─┘   └─ kernel 级 FLOPs 效率 ─┘
```

- 第一项：kernel 时间 / step 总时间（排除 launch gap、通信、CPU 空闲）
- 第二项：实际有用 FLOPs / (kernel 时间 × 峰值 FLOPs/s)
- 与 PaLM（arXiv:2204.02311）的 MFU 定义一致：分子只计模型必需 FLOPs，重计算/通信/空闲/launch gap 都压低 MFU

注意：这是恒等式（MFU 定义展开），第二项"kernel 级效率"仍是黑盒——真正落地要按 kernel 类型分层。

### 3. 真正可操作：按 kernel 类型分层

对 prefill，按 kernel 类型分层统计：dense GEMM、attention、norm/elementwise、通信、launch gap。每类看 NCU 指标。这是 gold 树 MFU 节点（N-3.1.3，B2）显式分解的落地方式。

## NCU 指标名表（标准测法）

| 子项 | NCU 指标名 | 说明 |
|---|---|---|
| 时间利用率 | `gpu__time_duration.sum`（配 Nsight Systems timeline） | kernel 时间总和 / step wall time，排除 launch gap/通信/CPU 空闲 |
| SM occupancy | `sm__warps_active.avg.pct_of_peak_sustained_active` | 活跃 warp 相对硬件上限（achieved occupancy） |
| SM/计算流水线吞吐 | `sm__throughput.avg.pct_of_peak_sustained_elapsed` | 注意：是 max over sub-pipelines，不是 occupancy |
| Tensor Core 活跃 | `DCGM_FI_PROF_PIPE_TENSOR_ACTIVE`（或 NCU Tensor pipe activity） | tensor pipe active cycles / elapsed |
| Tensor 吞吐效率 | `sm__ops_*` + `gpu__time_duration.sum` + SM clock 推算 | 不能只看 pipe active |
| L2 命中率 | `lts__t_sector_hit_rate.pct`（读：`lts__t_sector_op_read_hit_rate.pct`） | L2 sector hit rate |
| L2 带宽压力 | `lts__t_sectors.avg.pct_of_peak_sustained_elapsed` | L2 sector throughput / peak |
| HBM 利用率 | `dram__bytes.sum.per_second`（或 NCU Memory Workload Analysis DRAM throughput/SOL） | DRAM bytes/s / 峰值 HBM 带宽 |
| launch 开销 | Nsight Systems timeline gap（wall time − GPU kernel 时间） | NCU `gpu__time_duration.sum` 仅是 kernel duration |

出处：NVIDIA Nsight Compute 官方文档（docs.nvidia）

## A100/H100 prefill 典型区间

| 子项 | A100 prefill | H100 prefill | 出处/限制 |
|---|---|---|---|
| dense GEMM SM utilization | 高，接近计算瓶颈 | 高，但小 batch 难填满 | ACM 跨层分析：MoE expert FFN prefill 峰值 46%，dense FFN ~90% |
| attention core SM utilization | 40–50% | 40–50% | 同一研究：即使 batch 128，attention core SM util 仅 40–50% |
| dense GEMM L2 hit rate | >75% | >75% | 同一研究 |
| L2 utilization | 30–50% | 30–50% | 同一研究 |
| TensorCore 利用率 | [待核验：无统一区间] | [待核验：无统一区间] | Perplexity 明说查不到权威跨模型跨精度统一区间，现有多为特定 kernel/模型/batch 个案 |
| 端到端 prefill MFU | [待核验：无统一区间] | [待核验：无统一区间] | PaLM 46.2% 是 TPU v4 训练 MFU，不是 GPU prefill；0.35–0.55 是大规模训练经验值 |

硬件峰值参照：H100 SXM HBM 3.35 TB/s，A100 SXM 2.0 TB/s（NVIDIA 官方）

## η_bw 分解

D 提议的"η_bw = HBM 利用率 × L2 命中 × kernel launch 开销"**不成立**：
- HBM 利用率就是 η_bw 本身，不能作自己的子项
- L2 命中率高 → 实际 HBM 流量低 → η_bw 反而低，不代表性能差
- kernel launch 开销影响"时间归一化后的带宽利用率"，不改变单 kernel 执行期的 HBM bytes/s 与峰值之比

更合理的分解：

```
η_bw = (T_mem-kernel / T_wall) × (kernel 内实测 HBM bytes/s / B_HBM,peak)
       └─ 访存 kernel 时间占比 ─┘   └─ kernel 内 HBM SOL ─┘
```

若要进一步解释"为什么 kernel 内 HBM SOL 低"，才引入：L1/L2 命中率（减少 DRAM 请求）、访存合并与 sector 效率、occupancy/latency hiding、kernel launch gap。

## 实操建议（Perplexity）

1. 不要把 4 个百分比直接相乘得 MFU；先按 wall time 分解，再对每个 kernel 算 FLOPs/s
2. 对 prefill 按 kernel 类型分层统计
3. 对 GEMM 重点看 Tensor pipe activity、sm__throughput、occupancy、L2 hit rate、DRAM throughput；但最终 MFU 必须回到"有用 FLOPs / (峰值 × step time)"
4. 报告数值务必注明：精度（FP16/BF16/FP8）、峰值定义、是否含 attention FLOPs、是否含重计算、是否含通信；否则"MFU 0.35–0.55"没有可比性

## 奠基论文（ID 已验证真实）

| arXiv ID | 标题 | 贡献 |
|---|---|---|
| 2204.02311 | PaLM: Scaling Language Modeling with Pathways | MFU/HFU 区分奠基；PaLM 540B 报告 46.2% MFU、57.8% HFU；6ND + attention FLOPs 计算口径 |
| 2609.12923 | Dissecting GPU Utilization for LLM Inference on Nvidia Hopper | 批评 sm__throughput 当 occupancy 的误用；给 SM utilization/Compute SOL/L2 fit ratio/wave efficiency 的 NCU 口径；目前最接近"MFU 微架构分解"的论文 |
| 2605.20799 | Instant GPU Efficiency Visibility at Fleet Scale | 提出 OFU = Tensor Pipe Activity × f_SM/f_SM_max；区分硬件级 FLOP 利用率与应用级 MFU |

开源：sanmati1997/gpu-utilization-vs-mfu（讨论 nvidia-smi GPU-Util、DCGM SM active/tensor active 与 MFU 差异，但不是 4 因子乘法模型实现）

## 交叉验证状态

- Perplexity 结论（4 因子不成立）：与 arXiv:2609.12923 一致（该论文明确批评 sm__throughput 误用）
- 2609.12923 abstract 第一手验证 ✓（Siavashi/Maguire/Kostic/Chiesa；8 个 counter-validated views 每个钉死 NCU counter；H100 NVL 上 profile vLLM+FA3+cuBLASLt，覆盖 cold/warm prefill + decode；重点 decode 但 prefill 有覆盖）
- TensorCore 利用率统一区间：[不存在]（Perplexity + 2609.12923 印证：查不到是因为不同模型/batch/精度差异太大，本就不存在；gold 树改用"条件化参考值"——每个值带具体模型/batch/精度出处）
- 端到端 prefill MFU 统一区间：[不存在]（同上；PaLM 46.2% 是 TPU v4 训练 MFU，不是 GPU prefill）

## 规划修正（2026-11-19）

原 T2 验收"每个子项有独立区间" → 修正为"每个子项有 NCU 测法 + 条件化参考值（带模型/batch/精度出处）"。理由：统一区间不存在（Perplexity 查不到 + 2609.12923 按 6 种 kernel role 分别给值不凑统一数），硬凑统一区间会污染 gold 树。
