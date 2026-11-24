# idea53 闭式 flip 方向 spot-check（2512.01644 公开数据, 确定性数学）

# origin: ai · 2026-11-25 05:58 · Lead 亲做（subagent deleg_77bff895 死于 27b 输出 token 上限, PDF 文本已 salvage 到 /tmp/arxiv2512.01644.txt）

## 目的
用已发表实测数据（arXiv 2512.01644, ICT CAS, Llama3-8B on A100 + Jetson AGX Orin）核验 idea53 闭式模型的瓶颈 flip 方向预测。

## 数据点（出处: 2512.01644 §6.2.1, PDF L848-906, 已 salvage /tmp/arxiv2512.01644.txt）
- claim 27（原文）: "FFN kernels transition from compute-bound on data-center GPUs to memory-bound on edge devices" —— FFN GEMM 在 A100 compute-bound, 在 Orin memory-bound, 机制 = cache/LPDDR 受限→数据搬运增多→AI 下降。
- 同文 Fig.9: Prefill GEMM AI≈55-100 (compute-bound), Decode AI≈1-10 (memory-bound) —— 与模型 prefill/decode 二分一致。

## 闭式代入（resist 模型 t_i = f_i/r_i, flip 条件）
2 组件简化（fp16 算力 vs bw）, f_fp16+f_bw=1: flip iff f_bw > r_bw/r_fp16 / (1 + r_bw/r_fp16)。

| 平台 | r_fp16 / r_bw | flip 阈值 f_bw | FFN GEMM 可达性 |
|---|---|---|---|
| A100 | 312 TFLOPS / 2039 GB/s (ratio 6.54) | > 0.867 | 不可达（需 bw 份额>87%）→ compute-bound |
| edge (T5000 口径) | 258 / 273 (ratio 1.06) | > 0.514 | 可达 → memory-bound |

## 判定
**方向一致（1/1 数据点, conf 0.6）**：模型预测 A100 上 FFN GEMM 不可能 flip（阈值 0.87）而 edge 上可达（阈值 0.51），与 2512.01644 实测的 compute→memory 转变方向相同。机制同构：paper 的"cache 受限→数据搬运增多" = 模型里 f_bw 在 edge 增大越过阈值。
- 限制: 单数据点、edge 端用 T5000 spec 代理 Orin（Orin FP16 dense 实际更低, 阈值只会更低, 方向不变）; 2512.01644 是 LLM inference 域, 与 idea53 的通用 workload 先验域不同——这是跨域一致性, 不是同域复现。
- 用途: 投稿时作 Related Work/讨论段的 1 个外部一致性锚点（"direction of the flip is consistent with measured LLM-inference roofline transitions (2512.01644 claim 27)"），不 claim 定量复现。

## 复现
阈值计算是 2 行代数, 无脚本依赖: thr = (rbw/r16)/(1+rbw/r16), A100=(2039/312)/(1+2039/312)=0.867, edge=(273/258)/(1+273/258)=0.514。
