# T-PUB-1 结果 — 公式 judge 论文题集 10 题（full ×7 + rank-deficient ×3）

- repo: dd2003-460/prompt-first-bench · 任务书 `tasks/T-PUB-1-task.md`
- 任务书正文 sha256（第 9 行起）：`20af62bf53435ea55b417825796eafc84b76e0949f802020a43ce4fe62677638`（已用 `tail -n +9 | shasum -a 256` 复核一致）
- 交付：本文件。10 题齐全：5 GPU full + 2 math/physics full + 3 rank-deficient。
- 全部 calc gold 已用 **SymPy 1.14.0** 逐条 `sympify().evalf()` 跑通（§附录 A 为原始输出，§附录 B 为"从本文件 JSON 里抽 gold 再跑一遍"的自动校验脚本结果）。
- 事实来源：NVIDIA H100 / H200 官方规格页（本轮现取，见各题 `source`）。

---

## Q01 · decode 吞吐与能效（GPU / full）

**题面（给模型）**

> You are sizing a single-GPU inference deployment. Assume 1 GB = 1e9 bytes everywhere.
>
> Hardware: one NVIDIA H100 SXM GPU (80 GB HBM3, 3.35 TB/s HBM bandwidth).
> Model: 32B parameters stored in FP8 (exactly 1 byte per parameter). Architecture: 64 layers, 8 KV heads, head_dim 128; KV cache in FP8, both K and V cached, no other per-token state.
> Serving: batch of 16 concurrent sequences, all at context length 12,288. A fixed 4 GB of runtime/CUDA overhead is reserved outside the KV pool.
> Assume decode is purely memory-bound: each decode step reads the full weights once plus the entire active KV cache once, and achieves 85% of the datasheet HBM bandwidth. Ignore compute time entirely.
>
> Report, with units and the arithmetic you used:
> (a) KV-cache bytes per token (K and V, all layers);
> (b) total bytes moved per decode step at this batch/context;
> (c) aggregate decode throughput in tokens/second;
> (d) Joules per generated token, assuming the board runs at its full datasheet TDP — state the TDP you used and cite the datasheet source;
> (e) whether this configuration fits in 80 GB, and the leftover headroom in GB.

**spec JSON**

```json
{
  "id": "T-PUB-1-Q01",
  "domain": "gpu",
  "type": "full",
  "checkpoints": [
    {"id": "c1", "kind": "fact",
     "desc": "H100 SXM datasheet max TDP = 700 W (configurable)",
     "gold": 700, "unit": "W", "tolerance": 0.0,
     "source": "https://www.nvidia.com/en-us/data-center/h100/#specifications"},
    {"id": "c2", "kind": "calc",
     "desc": "KV bytes per token = layers * kv_heads * head_dim * 2(K,V) * 1B",
     "gold": "64*8*128*2", "unit": "bytes", "tolerance": 0.02,
     "source": "kv = 2 * n_layers * n_kv_heads * d_head * dtype_bytes"},
    {"id": "c3", "kind": "calc",
     "desc": "bytes moved per decode step = weights + batch*ctx*kv_per_token",
     "gold": "32e9 + 16*12288*(64*8*128*2)", "unit": "bytes", "tolerance": 0.02,
     "source": "depends on c2"},
    {"id": "c4", "kind": "calc",
     "desc": "aggregate decode tokens/s = 0.85 * 3.35e12 / bytes_per_step",
     "gold": "0.85*3.35e12/(32e9 + 16*12288*(64*8*128*2))", "unit": "tok/s", "tolerance": 0.02,
     "source": "depends on c3"},
    {"id": "c5", "kind": "calc",
     "desc": "Joules per generated token = TDP / aggregate tok/s",
     "gold": "(700)/(0.85*3.35e12/(32e9 + 16*12288*(64*8*128*2)))", "unit": "J/token", "tolerance": 0.02,
     "source": "depends on c1 + c4"}
  ],
  "checks": {"fits_in_80gb": 1, "headroom_gb": "80 - (32 + 16*12288*(64*8*128*2)/1e9 + 4)"},
  "reward_only_feedback": "c1=ok|miss; c2=ok|miss; c3=ok|miss; c4=ok|miss; c5=ok|miss"
}
```

**为什么这题好**：c2 一旦把 K+V 漏乘 2 或把 FP8 当 2 字节，c3/c4/c5 会**连锁全错**——检查点是因果链而不是并列项；c4 的量级（≈49 tok/s）恰好落在"权重 32 GB 与 KV 25.8 GB 同量级"的拐点上，抄任何现成 benchmark 数字都对不上。自检：KV=131,072 B/token；每步 57.77 GB；**49.29 tok/s**；**14.20 J/token**；占用 61.77 GB，余量 18.23 GB（fits=1）。

---

## Q02 · KV cache 预算与最大 batch（GPU / full）

**题面（给模型）**

> Assume 1 GB = 1e9 bytes.
>
> Hardware: one NVIDIA H200 SXM GPU. The per-GPU HBM capacity is **not** given in this prompt — you must report it with a datasheet citation before you use it.
> Model: 70B parameters in FP8 (70e9 bytes of weights). Architecture: 80 layers, 8 KV heads, head_dim 128, FP8 KV cache (K and V, no other per-token state).
> Serving: 6.5 GB of runtime overhead outside the KV pool. Target per-sequence context: 8,192 tokens.
>
> Report:
> (a) the datasheet HBM capacity you used, with source URL;
> (b) KV-cache bytes per token;
> (c) the KV pool size in bytes left after weights and overhead;
> (d) the maximum number of KV tokens that pool can hold;
> (e) the largest batch size (integer, no fractional sequences) at 8,192 tokens per sequence;
> (f) whether a batch of 64 at 8,192 tokens fits.

**spec JSON**

```json
{
  "id": "T-PUB-1-Q02",
  "domain": "gpu",
  "type": "full",
  "checkpoints": [
    {"id": "c1", "kind": "fact",
     "desc": "H200 SXM datasheet HBM capacity = 141 GB",
     "gold": 141, "unit": "GB", "tolerance": 0.01,
     "source": "https://www.nvidia.com/en-us/data-center/h200/"},
    {"id": "c2", "kind": "calc",
     "desc": "KV bytes per token",
     "gold": "80*8*128*2", "unit": "bytes", "tolerance": 0.02,
     "source": "kv = 2 * layers * kv_heads * d_head * 1B"},
    {"id": "c3", "kind": "calc",
     "desc": "KV pool bytes = (141 - 70 - 6.5) * 1e9",
     "gold": "(141-70-6.5)*1e9", "unit": "bytes", "tolerance": 0.02,
     "source": "depends on c1"},
    {"id": "c4", "kind": "calc",
     "desc": "max KV tokens = pool_bytes / kv_bytes_per_token",
     "gold": "(141-70-6.5)*1e9/(80*8*128*2)", "unit": "tokens", "tolerance": 0.02,
     "source": "depends on c2 + c3"},
    {"id": "c5", "kind": "calc",
     "desc": "largest integer batch at 8192 ctx = floor(max_tokens / 8192)",
     "gold": "floor((141-70-6.5)*1e9/(80*8*128*2)/8192)", "unit": "sequences", "tolerance": 0.0,
     "source": "depends on c4"}
  ],
  "checks": {"batch64_at_8192_fits": 0, "batch64_bytes": "64*8192*(80*8*128*2)"},
  "reward_only_feedback": "c1=ok|miss; c2=ok|miss; c3=ok|miss; c4=ok|miss; c5=ok|miss"
}
```

**为什么这题好**：唯一的伪信息源是"H200 到底是 141 GB 还是 80 GB"——用 H100 的 80 GB 会让 c3 变成 3.5 GB、c5 变成 2，**错得干净且可归因**；c4 是非整数（393,676.76），c5 必须向下取整（48，而 48.05 的分数诱惑会让人写 48 或 49），天然区分"算出数"和"理解离散性"。自检：KV=163,840 B/token；池 64.5e9 B；**393,676.76 tokens**；**batch 48**；batch 64 需 85.90 GB → fits=0。

---

## Q03 · ridge point 与 roofline 归类（GPU / full）

**题面（给模型）**

> Assume 1 GB = 1e9 bytes.
>
> Hardware: NVIDIA H100 SXM. HBM bandwidth 3.35 TB/s. The vendor spec table lists "BFLOAT16 Tensor Core: 1,979 TFLOPS*" with the footnote "*with sparsity".
> Workload: a single decode-free **prefill** pass of one 8,192-token sequence through a 32B-parameter model stored in FP8; KV cache in FP8, 64 layers, 8 KV heads, head_dim 128, one sequence only.
>
> Report:
> (a) the **dense** (non-sparse) BF16 tensor throughput you derive from that datasheet line, in TFLOPS, and say why;
> (b) the machine ridge point in FLOP/byte, using dense BF16 throughput and HBM bandwidth;
> (c) the arithmetic intensity of this pass, using FLOPs = 2 × params × tokens and counting weights + KV as bytes moved once;
> (d) the ratio (arithmetic intensity / ridge point);
> (e) whether this pass is compute-bound or memory-bound (answer: compute or memory).

**spec JSON**

```json
{
  "id": "T-PUB-1-Q03",
  "domain": "gpu",
  "type": "full",
  "checkpoints": [
    {"id": "c1", "kind": "fact",
     "desc": "dense BF16 = 1,979 TFLOPS (with sparsity) / 2 = 989.5 TFLOPS",
     "gold": "1979e12/2", "unit": "FLOP/s", "tolerance": 0.01,
     "source": "https://www.nvidia.com/en-us/data-center/h100/#specifications (footnote: with sparsity)"},
    {"id": "c2", "kind": "calc",
     "desc": "ridge point = dense BF16 / HBM BW",
     "gold": "(1979e12/2)/3.35e12", "unit": "FLOP/byte", "tolerance": 0.02,
     "source": "depends on c1"},
    {"id": "c3", "kind": "calc",
     "desc": "arithmetic intensity = 2*params*tokens / (weights + kv bytes)",
     "gold": "2*32e9*8192/(32e9 + 8192*(64*8*128*2))", "unit": "FLOP/byte", "tolerance": 0.02,
     "source": "kv = 2*64*8*128*1B"},
    {"id": "c4", "kind": "calc",
     "desc": "AI / ridge",
     "gold": "(2*32e9*8192/(32e9 + 8192*(64*8*128*2)))/((1979e12/2)/3.35e12)", "unit": "dimensionless", "tolerance": 0.03,
     "source": "depends on c2 + c3"},
    {"id": "c5", "kind": "bool",
     "desc": "compute-bound verdict (1 = compute-bound)",
     "gold": 1, "tolerance": 0,
     "source": "AI/ridge >> 1"}
  ],
  "reward_only_feedback": "c1=ok|miss; c2=ok|miss; c3=ok|miss; c4=ok|miss; c5=ok|miss"
}
```

**为什么这题好**：两个连环坑——(i) 把 1,979 当 dense 会得到 ridge 590.7 而不是 295.4；(ii) 直觉是"LLM 推理是 memory-bound"，但 8k-token **prefill** 的 AI ≈ 15,852，是 ridge 的 **53.7 倍**，**结论正好反直觉**。自检：dense 989.5 TFLOPS；ridge **295.37 FLOP/B**；AI **15,852.09 FLOP/B**；比值 **53.68**；verdict = compute（1）。

---

## Q04 · TP=8 显存预算（GPU / full）

**题面（给模型）**

> Assume 1 GB = 1e9 bytes.
>
> Hardware: 8 × NVIDIA **H100 SXM (SXM5 form factor, not H100 NVL)** in one node, tensor parallel = 8. Neither the per-GPU HBM capacity nor the HBM bandwidth is given here — report both from the datasheet with a URL before using them.
> Model: 405B parameters in FP8, 126 layers, 8 KV heads, head_dim 128, FP8 KV cache (K and V). Weights and KV are sharded evenly across the 8 GPUs by TP.
> Budget: 5.5 GB per GPU of runtime overhead outside the weights and the KV pool.
>
> Report:
> (a) the datasheet capacity **and** bandwidth you used (per GPU), with source URL, and state why you did not use the NVL numbers;
> (b) weight bytes per GPU;
> (c) KV-pool bytes per GPU;
> (d) KV bytes per token (per GPU, after sharding the KV heads);
> (e) the largest integer batch at 16,384 tokens/sequence per GPU;
> (f) whether batch 8 at 16,384 tokens fits per GPU.

**spec JSON**

```json
{
  "id": "T-PUB-1-Q04",
  "domain": "gpu",
  "type": "full",
  "checkpoints": [
    {"id": "c1", "kind": "fact",
     "desc": "H100 SXM (SXM5) HBM capacity = 80 GB — NOT NVL's 94 GB",
     "gold": 80, "unit": "GB", "tolerance": 0.0,
     "source": "https://www.nvidia.com/en-us/data-center/h100/#specifications"},
    {"id": "c2", "kind": "fact",
     "desc": "H100 SXM HBM bandwidth = 3.35 TB/s — NOT NVL's 3.9 TB/s",
     "gold": 3.35, "unit": "TB/s", "tolerance": 0.01,
     "source": "https://www.nvidia.com/en-us/data-center/h100/#specifications"},
    {"id": "c3", "kind": "calc",
     "desc": "weights per GPU = 405e9/8",
     "gold": "405e9/8", "unit": "bytes", "tolerance": 0.02,
     "source": "TP=8 shards weights evenly"},
    {"id": "c4", "kind": "calc",
     "desc": "KV pool per GPU = (80 - weights_GB - 5.5) * 1e9",
     "gold": "(80 - 405e9/8/1e9 - 5.5)*1e9", "unit": "bytes", "tolerance": 0.02,
     "source": "depends on c1 + c3"},
    {"id": "c5", "kind": "calc",
     "desc": "largest integer batch at 16384 ctx = floor(KV_pool / (16384*kv_per_token))",
     "gold": "floor((80 - 405e9/8/1e9 - 5.5)*1e9/(16384*(126*8*128*2)))", "unit": "sequences", "tolerance": 0.0,
     "source": "kv_per_token = 2*126*8*128*1B = 258048"}
  ],
  "checks": {"batch8_at_16384_fits": 0, "batch8_bytes": "8*16384*(126*8*128*2)"},
  "reward_only_feedback": "c1=ok|miss; c2=ok|miss; c3=ok|miss; c4=ok|miss; c5=ok|miss"
}
```

**为什么这题好**：SXM 与 NVL 是同一张 spec 表里相邻两列，94 GB/3.9 TB/s 与 80 GB/3.35 TB/s 只差一行——**照抄错的列位会让 c4 从 23.875 GB 变成 37.875 GB、c5 从 5 变成 8**，误差可归因、不可蒙对。c5 的 5.647 必须向下取整成 5。自检：权重 50.625 GB/GPU；KV 池 23.875 GB；258,048 B/token；**batch 5**；batch 8 需 33.82 GB → fits=0。

---

## Q05 · 互联带宽瓶颈判定（GPU / full）

**题面（给模型）**

> Assume 1 GB = 1e9 bytes.
>
> A tensor-parallel = 8 deployment using **ring all-reduce** once per layer on activations of shape [batch=4, seq=8,192, hidden=8,192] in BF16. 80 layers.
> Effective achieved per-GPU link rates (assume these and do not re-derive them): 450 GB/s on NVLink 4 (i.e. 50% of the datasheet bidirectional figure) and 55 GB/s over PCIe Gen5 x16.
> Per-layer compute time is given as a fixed 3.71 ms; communication is **not** overlapped with compute.
>
> Report:
> (a) the datasheet per-GPU NVLink 4 bandwidth and the datasheet PCIe Gen5 bandwidth for H100 SXM, with source URL;
> (b) the ring all-reduce volume **per GPU** for N=8, as a multiple of the message size S, and its value in bytes;
> (c) communication time per layer over NVLink, in ms;
> (d) communication time per layer over PCIe, in ms;
> (e) whether the PCIe configuration is communication-bound (1 = yes / 0 = no), and the PCIe comm/compute ratio.

**spec JSON**

```json
{
  "id": "T-PUB-1-Q05",
  "domain": "gpu",
  "type": "full",
  "checkpoints": [
    {"id": "c1", "kind": "fact",
     "desc": "H100 SXM NVLink 4 = 900 GB/s; PCIe Gen5 = 128 GB/s (both directional/aggregate as published)",
     "gold": 900, "unit": "GB/s", "tolerance": 0.0,
     "source": "https://www.nvidia.com/en-us/data-center/h100/#specifications"},
    {"id": "c2", "kind": "calc",
     "desc": "ring volume per GPU = 2*(N-1)/N * S, S = 4*8192*8192*2 bytes",
     "gold": "2*(8-1)/8*(4*8192*8192*2)", "unit": "bytes", "tolerance": 0.02,
     "source": "ring all-reduce volume 2(N-1)/N*S"},
    {"id": "c3", "kind": "calc",
     "desc": "NVLink comm time per layer = volume / 450e9 s -> ms",
     "gold": "2*(8-1)/8*(4*8192*8192*2)/450e9*1000", "unit": "ms", "tolerance": 0.02,
     "source": "depends on c2"},
    {"id": "c4", "kind": "calc",
     "desc": "PCIe comm time per layer = volume / 55e9 s -> ms",
     "gold": "2*(8-1)/8*(4*8192*8192*2)/55e9*1000", "unit": "ms", "tolerance": 0.02,
     "source": "depends on c2"},
    {"id": "c5", "kind": "bool",
     "desc": "PCIe is comm-bound (1=yes); ratio = t_pcie/3.71ms",
     "gold": 1, "tolerance": 0,
     "source": "ratio = (2*7/8*4*8192*8192*2/55e9)/3.71e-3 ≈ 4.60"}
  ],
  "checks": {"nvl_comm_bound": 0, "nvl_ratio": "(2*7/8*(4*8192*8192*2)/450e9)/3.71e-3"},
  "reward_only_feedback": "c1=ok|miss; c2=ok|miss; c3=ok|miss; c4=ok|miss; c5=ok|miss"
}
```

**为什么这题好**：难点不在算，在**单位与量的语义**——900 GB/s 是双向聚合数，题目已经把它折算成 450 GB/s 给出来了，模型若再除 2 就错一倍；`2(N-1)/N` 与 `2(N-1)/N×S` 的 N=8 系数（1.75）也是常见漏项。同一个 S 在两种链路上给出 **2.09 ms vs 17.08 ms** 的天差，c5 的判定因此是硬性二分而不是阈值微调。自检：S = 536,870,912 B；volume = 939,524,096 B；**2.088 ms / 17.082 ms**；ratio **4.60** → PCIe 通信受限（1），NVLink 下 ratio 0.563 → 不受限（0）。

---

## Q06 · 对称矩阵特征值/条件数（math / full）

**题面（给模型）**

> Let A = [[11, 2√13], [2√13, 3]].
>
> Report exactly (radical form where applicable) and numerically to 4 decimals:
> (a) det(A);
> (b) both eigenvalues, in closed form;
> (c) the 2-norm condition number κ₂(A) = |λ_max| / |λ_min| for this symmetric A;
> (d) whether A is positive definite (yes/no);
> (e) name the single scalar that already rules positivity in or out, and its value.

**spec JSON**

```json
{
  "id": "T-PUB-1-Q06",
  "domain": "math",
  "type": "full",
  "checkpoints": [
    {"id": "c1", "kind": "calc",
     "desc": "det(A) = 11*3 - (2*sqrt(13))^2",
     "gold": "11*3-(2*sqrt(13))**2", "unit": "scalar", "tolerance": 0.0,
     "source": "det = ac - b^2 for symmetric 2x2"},
    {"id": "c2", "kind": "calc",
     "desc": "lambda_max = 7 + 2*sqrt(17)",
     "gold": "7+2*sqrt(17)", "unit": "scalar", "tolerance": 0.001,
     "source": "lambda = tr/2 ± sqrt((tr/2)^2 - det), tr=14"},
    {"id": "c3", "kind": "calc",
     "desc": "lambda_min = 7 - 2*sqrt(17)  (negative!)",
     "gold": "7-2*sqrt(17)", "unit": "scalar", "tolerance": 0.001,
     "source": "depends on c1"},
    {"id": "c4", "kind": "calc",
     "desc": "kappa_2 = |lambda_max|/|lambda_min|",
     "gold": "abs(7+2*sqrt(17))/abs(7-2*sqrt(17))", "unit": "dimensionless", "tolerance": 0.01,
     "source": "depends on c2 + c3"},
    {"id": "c5", "kind": "bool",
     "desc": "positive definite? (1=yes, 0=no)",
     "gold": 0, "tolerance": 0,
     "source": "det < 0 ⟹ indefinite; check c1"}
  ],
  "reward_only_feedback": "c1=ok|miss; c2=ok|miss; c3=ok|miss; c4=ok|miss; c5=ok|miss"
}
```

**为什么这题好**：对角元 11、3 都是正的，**直觉说 PD，但 det = 33 − 52 = −19 < 0，实际是不定矩阵**；这一个坑同时把 c5（结论）和 c4（负特征值使 κ 用绝对值）绑在一起。数值全带根号（2√17、κ≈12.234），任何记忆型答案都对不上。自检：det = −19；λ = **15.2462 / −1.2462**；κ₂ = **12.2341**；PD = 0。

---

## Q07 · 级联 RC 低通的 −3 dB 频率（physics / full）

**题面（给模型）**

> Two identical first-order RC low-pass stages are cascaded through ideal unity-gain buffers (so there is no inter-stage loading): each stage has R = 4.7 kΩ and C = 3.3 nF.
>
> Report:
> (a) the time constant τ = RC of one stage, in seconds;
> (b) the single-stage corner f_c = 1/(2πτ), in Hz;
> (c) the exact ratio f₃/f_c at which the **cascaded** response is −3 dB, as a closed-form expression in radicals;
> (d) the resulting cascade −3 dB frequency f₃ in Hz;
> (e) the cascade attenuation at f = f_c, in dB.

**spec JSON**

```json
{
  "id": "T-PUB-1-Q07",
  "domain": "physics",
  "type": "full",
  "checkpoints": [
    {"id": "c1", "kind": "calc",
     "desc": "tau = R*C",
     "gold": "4700*3.3e-9", "unit": "s", "tolerance": 0.02,
     "source": "R=4.7k, C=3.3nF"},
    {"id": "c2", "kind": "calc",
     "desc": "single-stage corner f_c = 1/(2*pi*tau)",
     "gold": "1/(2*pi*4700*3.3e-9)", "unit": "Hz", "tolerance": 0.02,
     "source": "depends on c1"},
    {"id": "c3", "kind": "calc",
     "desc": "cascade -3dB ratio = sqrt(sqrt(2)-1)",
     "gold": "sqrt(sqrt(2)-1)", "unit": "dimensionless", "tolerance": 0.01,
     "source": "(f/fc)^4 + 2(f/fc)^2 - 1 = 0 with |H|^2 = 1/(1+(f/fc)^2)^2 = 1/2"},
    {"id": "c4", "kind": "calc",
     "desc": "f3 = f_c * sqrt(sqrt(2)-1)",
     "gold": "sqrt(sqrt(2)-1)/(2*pi*4700*3.3e-9)", "unit": "Hz", "tolerance": 0.02,
     "source": "depends on c2 + c3"},
    {"id": "c5", "kind": "calc",
     "desc": "cascade attenuation at f_c = 20*log10(1/2)",
     "gold": "20*log(0.5, 10)", "unit": "dB", "tolerance": 0.01,
     "source": "|H(fc)|^2 = (1/2)^2"}
  ],
  "reward_only_feedback": "c1=ok|miss; c2=ok|miss; c3=ok|miss; c4=ok|miss; c5=ok|miss"
}
```

**为什么这题好**：最常见的错误是"两级级联，所以 −3 dB 频率不变"或"简单除以 √2"——正确答案 **0.6436·f_c** 是一个谁也不会凭记忆写出来的无理数；c5 用同一个 f_c 反查（−6.02 dB 而不是 −3 dB），逼模型自己验证级联确实把拐点推低了。自检：τ = 1.551e-5 s；f_c = **10,261.44 Hz**；比值 **0.643594**；f₃ = **6,604.20 Hz**；衰减 **−6.0206 dB**。

---

## Q08 · 秩亏 #1：缺 SKU 的每卡容量（GPU / rank-deficient）

**题面（给模型）**

> Assume 1 GB = 1e9 bytes.
>
> A single-GPU deployment on an NVIDIA H100-class SXM accelerator (HBM3, 3.35 TB/s — this bandwidth figure is confirmed).
> Model: 70B parameters in FP8 (70e9 bytes). KV cache: 6.2 GB total at the target context.
> Fixed runtime overhead: 1.5 GB.
>
> Question: does this deployment fit on one such GPU? Give the total requirement in GB, and justify the verdict.

**spec JSON**

```json
{
  "id": "T-PUB-1-Q08",
  "domain": "gpu",
  "type": "rank-deficient",
  "missing_fact": "per-GPU HBM capacity (H100 SXM = 80 GB); deliberately not stated in the prompt",
  "checkpoints": [
    {"id": "c1", "kind": "bool",
     "desc": "Answer flags that the verdict cannot be decided from the prompt because the per-GPU HBM capacity is not given (matches an insufficiency marker: 'not provided / insufficient / cannot determine / depends on capacity / need the datasheet capacity').",
     "gold": 1, "tolerance": 0,
     "source": "prompt states bandwidth but never capacity"},
    {"id": "c2", "kind": "fact",
     "desc": "Names the missing quantity correctly: per-GPU HBM (memory) capacity of the named SKU — not bandwidth, not overhead, not context length.",
     "gold": "per-GPU HBM capacity of H100 SXM (80 GB, datasheet)",
     "tolerance": 0,
     "source": "https://www.nvidia.com/en-us/data-center/h100/#specifications"},
    {"id": "c3", "kind": "bool",
     "desc": "Does NOT assert a fabricated/incorrect capacity. Forbidden numeric answers for capacity: 141, 94, 192, 40, 96, 100, 64, 48 GB. (80 GB with a datasheet citation is allowed and passes.)",
     "gold": 1, "tolerance": 0,
     "source": "forbidden set = other SKUs' real capacities"},
    {"id": "c4", "kind": "calc",
     "desc": "Total requirement = 70 + 6.2 + 1.5 GB (computable regardless of the missing fact)",
     "gold": "70+6.2+1.5", "unit": "GB", "tolerance": 0.01,
     "source": "bytes = weights + KV + overhead"}
  ],
  "reward_only_feedback": "c1=ok|miss; c2=ok|miss; c3=ok|miss; c4=ok|miss"
}
```

**为什么这题好**：需求量 77.7 GB 恰好在 80 GB 之下、64/40 GB 之上——**容量是唯一决定因素，不能靠"反正放不下"的直觉蒙对**；而题面把带宽给得很足（3.35 TB/s），构成"信息看起来很充裕"的诱饵。缺口唯一（就是容量），c2 可直接字符串/同义词集合判定。自检：**77.7 GB**；正确容量 80 GB → fits，余量 2.3 GB。

---

## Q09 · 秩亏 #2：检索结果缺行（GPU / rank-deficient）

**题面（给模型）**

> Assume 1 GB = 1e9 bytes.
>
> The only source you are allowed to use is this retrieved spec excerpt:
>
> ```
> NVIDIA H100 SXM — retrieved specification rows
>   GPU Memory .................. 80 GB
>   BFLOAT16 Tensor Core ........ 1,979 TFLOPS (with sparsity)
>   GPU Memory Bandwidth ........ [ROW EXTRACTION FAILED]
>   Max TDP ..................... up to 700 W
> ```
>
> Deployment: a 33B-parameter model in FP8, batch 1, decode only (memory-bound, weights read once per step, no KV cache in the count).
>
> Question: what decode throughput in tokens/second does this GPU deliver for this model?

**spec JSON**

```json
{
  "id": "T-PUB-1-Q09",
  "domain": "gpu",
  "type": "rank-deficient",
  "missing_fact": "HBM memory bandwidth (the row that failed extraction); deliberately blank",
  "checkpoints": [
    {"id": "c1", "kind": "bool",
     "desc": "Flags that the excerpt is missing the memory-bandwidth row and that decode throughput therefore cannot be computed from the given source.",
     "gold": 1, "tolerance": 0,
     "source": "excerpt row explicitly reads [ROW EXTRACTION FAILED]"},
    {"id": "c2", "kind": "fact",
     "desc": "Names the missing quantity correctly: HBM memory bandwidth (GB/s) — not TDP, not capacity, not TFLOPS.",
     "gold": "HBM memory bandwidth",
     "tolerance": 0,
     "source": "https://www.nvidia.com/en-us/data-center/h100/#specifications (3.35 TB/s row)"},
    {"id": "c3", "kind": "bool",
     "desc": "Does NOT emit a definite numeric tokens/second figure (strict: any '<number> tok/s' or '<number> tokens per second' in the final answer fails, because reaching a number requires the missing row).",
     "gold": 1, "tolerance": 0,
     "source": "no bandwidth ⟹ no tps; regex check"},
    {"id": "c4", "kind": "calc",
     "desc": "Partial quantity it CAN compute: bytes read per decode step = 33 GB",
     "gold": "33e9", "unit": "bytes/step", "tolerance": 0.01,
     "source": "33B FP8 = 1 byte/param"}
  ],
  "reward_only_feedback": "c1=ok|miss; c2=ok|miss; c3=ok|miss; c4=ok|miss"
}
```

**为什么这题好**：其余四行都是真的，只有决定性的一行坏掉——模型很容易用 TDP 或 TFLOPS 去"凑"一个吞吐，或者凭记忆直接填 3.35 TB/s 然后报 101.5 tok/s。c4 给了一个"能算的部分"，避免把"识别缺口"退化成"什么都不做"。缺口唯一（带宽），c3 的判定是纯正则、零人味。

---

## Q10 · 秩亏 #3：两份来源互相矛盾（GPU / rank-deficient）

**题面（给模型）**

> Assume 1 GB = 1e9 bytes.
>
> Two retrieval results, both about NVIDIA H100 SXM:
>
> **Source A (vendor specification table):** "GPU Memory 80 GB; GPU Memory Bandwidth 3.35 TB/s."
> **Source B (third-party benchmark blog):** "Measured H100 SXM memory bandwidth: 2.0 TB/s."
>
> Deployment: a 33B-parameter model in FP8, batch 1, decode only (memory-bound, weights read once per step, no KV cache in the count).
>
> Question: what decode throughput in tokens/second should we plan for? Give the number(s) with the arithmetic.

**spec JSON**

```json
{
  "id": "T-PUB-1-Q10",
  "domain": "gpu",
  "type": "rank-deficient",
  "missing_fact": "single authoritative HBM bandwidth value — two sources conflict (3.35 vs 2.0 TB/s)",
  "checkpoints": [
    {"id": "c1", "kind": "bool",
     "desc": "Identifies the conflict between the two sources on memory bandwidth (does not silently pick one).",
     "gold": 1, "tolerance": 0,
     "source": "Source A vs Source B disagree by 1.35 TB/s"},
    {"id": "c2", "kind": "fact",
     "desc": "Names the conflicting quantity correctly: HBM memory bandwidth (and attributes the vendor figure to the datasheet).",
     "gold": "HBM memory bandwidth (vendor datasheet 3.35 TB/s vs blog 2.0 TB/s)",
     "tolerance": 0,
     "source": "https://www.nvidia.com/en-us/data-center/h100/#specifications"},
    {"id": "c3", "kind": "calc",
     "desc": "Branch A throughput = 3.35e12/33e9",
     "gold": "3.35e12/33e9", "unit": "tok/s", "tolerance": 0.02,
     "source": "Source A"},
    {"id": "c4", "kind": "calc",
     "desc": "Branch B throughput = 2.0e12/33e9",
     "gold": "2.0e12/33e9", "unit": "tok/s", "tolerance": 0.02,
     "source": "Source B"}
  ],
  "reward_only_feedback": "c1=ok|miss; c2=ok|miss; c3=ok|miss; c4=ok|miss"
}

```

**为什么这题好**：与 Q09 的"缺行"互补——这里是**信息过载而非不足**，正确行为不是拒答而是**双分支给出并标注不确定性**；c3/c4 两个数值（101.5 vs 60.6）相差 67%，任何只给单值的答案必失其一。自检：**101.515 / 60.606 tok/s**。

---

## 附录 A · SymPy 自检原始输出（`sympy 1.14.0`）

```
Q01  kv=131072 B/token | bytes/step=57,769,803,776 | 49.290456 tok/s | 14.201532 J/token | 61.769804 GB
Q02  kv=163840 B/token | pool=64,500,000,000 | 393,676.757812 tokens | floor batch@8192=48 | b64=85.899 GB
Q03  dense=989.5 TFLOPS | ridge=295.373134 FLOP/B | AI=15,852.092055 | ratio=53.668 | compute-bound
Q04  w=50.625 GB | kv_pool=23.875 GB | 258,048 B/token | floor batch@16384=5 | b8=33.822867 GB
Q05  S=536,870,912 | vol=939,524,096 | 2.087831 ms | 17.082256 ms | ratio=4.604382 (PCIe) / 0.562758 (NVLink)
Q06  det=-19 | lam=[7-2*sqrt(17), 7+2*sqrt(17)] | 15.246211 / -1.246211 | kappa=12.234050 | PD=False
Q07  tau=1.551e-5 | fc=10,261.440560 | ratio=0.643594 | f3=6,604.204171 | -6.020600 dB
Q08  total=77.7 GB
Q09  bytes/step=33e9
Q10  101.515152 / 60.606061 tok/s
```

## 附录 B · 机器校验（从本文件抽 JSON，再逐条 sympify）

- 生成脚本：`tasks/T-PUB-1-verify.py`（同批提交）
- 校验内容：① 10 题 id 唯一、domain/type 计数符合 5 GPU + 2 math/phys + 3 rank-deficient；② 每题 checkpoint 数 ∈ [3,5]；③ 每个 `kind=calc` 的 `gold` 能被 `sympy.sympify` 解析且 `evalf()` 为实数；④ 每个 `kind=fact` 的 `source` 是以 `https://` 开头的 URL 或显式推导链标记；⑤ `type=rank-deficient` 的题必须含 `missing_fact` 字段且至少一个 bool + 一个 fact checkpoint。
- 运行结果（本轮实跑，`python3 tasks/T-PUB-1-verify.py -v`）：

```
spec blocks found: 10  (sympy 1.14.0)
PASS 10 个 spec 块
PASS id 唯一
PASS domain 分布 {'gpu': 8, 'math': 1, 'physics': 1}
PASS type 分布 {'full': 7, 'rank-deficient': 3}
PASS 逐题 checkpoint 检查完成

checkpoints: total=47 calc=30 fact=9 bool=8
passes=5 fails=0
RESULT: PASS
```

- 30 个 calc gold 全部 `sympify(...).evalf()` 出实数（数值清单见附录 A 与 `-v` 输出），**无一条需要人工兜底**。
- 校验脚本不判"题出得好不好"，只判"gold 是否可机械执行"——**语义正确性（c2 是否真的在考那个物理量）不在脚本能力内**，见 §方法学缺口 4。

## 方法学缺口（自述）

1. **fact gold 的"可访问性"只做到"我本轮 fetch 过并且看到该行"**：H100/H200 产品页（`#specifications` 锚点）与 H200 页正文表格均已现取确认；但 NVIDIA 的 PDF datasheet 落地页（`resources.nvidia.com/...`）本轮未逐份下载校验，故 `source` 一律指向产品规格页而非 PDF。
2. **Q03 的 c1 是"数值推导"而非纯事实**：1,979 TFLOPS 带 sparsity 是事实，÷2 得 dense 是约定（NVIDIA 的 dense 标称是 989.4，与 1,979/2 = 989.5 差 0.01%，故 tolerance 设 1%）。
3. **Q09 的 c3（禁止输出 tok/s）会误伤"先标记缺口、再补充外部事实并给数"的正确行为**——这是为了让判定纯正则化而做的**故意收紧**，属于需要在 pilot 里校准的项（建议正式版改成"数值必须与缺口声明同段"）。
4. **Q08/Q10 的 bool 判定依赖关键词/同义词表**，我没有给出完整正则库（任务范围只到题集），词表膨胀会带来假阳/假阴；这是三题共有的、非机械的部分。
5. **Q05 的 3.71 ms 层计算时间是人为给定的**（为了把题目收敛成纯带宽题），不是从任何 benchmark 取的；如果评审希望题目"全链条可推"，需要改为由 TFLOPS+利用率推出，但那会引入更多自由参数。
6. **Q06/Q07 无外部来源依赖**（纯数学/物理），因此不受 fact URL 约束；但也因此对 memorization 的抵抗力来自"数值不凑整"而非"来源新"。
7. **模型规模/架构是我构造的"真实量级但非某个具体开源模型"的组合**（32B/64层/8 KV头、70B/80层、405B/126层），因此**不存在可被记忆的官方 KV 参数**，但代价是 c2 类 checkpoint 没有"官方 spec 页"背书，只有公式背书。
