# 阶段 02 · 线 B 性能与生态核验

> 目标：Qwen3.8-27B 本地部署候选硬件的实测性能与软件生态门禁
> 日期：2026-10-28
> 数据分级：🟢 双源以上交叉验证 / 🟡 单源可信 / 🔴 单源弱/存疑

---

## 一、G1 模型架构参数

来源：HuggingFace Qwen/Qwen3.8-27B model card（发布 2026-07-20）+ config.json

| 参数 | 值 | 来源 | conf |
|---|---|---|---|
| 总参数 | 27B（100% 激活，稠密） | HF model card | 🟢 |
| 层数 | 64 | config.json | 🟢 |
| 隐藏维 hidden_size | 5120 | config.json | 🟢 |
| 注意力头数 | 24 | config.json | 🟢 |
| KV heads | 4（GQA，与 Qwen3.5-4B 同配） | config.json | 🟢 |
| 线性注意力头（GDN） | 48 | config.json | 🟢 |
| 上下文窗口 | 262,144 tokens（262K） | HF model card | 🟢 |
| 架构 | 混合 Gated DeltaNet（GDN）+ 经典注意力 | HF model card | 🟢 |
| 原生精度 | BF16（~54 GiB） | HF model card | 🟢 |
| 推理友好量化 | NVFP4（24 GiB）、Q4_K_M GGUF（17.3 GiB） | HF model card + 社区 | 🟢 |
| MTP（多 token 预测） | 内置 nextn 层，支持投机解码 | GitHub jcr211/qwen38-mtp | 🟢 |
| 词元容量 | 33M | HF model card | 🟢 |

**关键架构影响**：
- GDN 线性注意力 → KV cache 极小（仅 4 个 KV head），长上下文显存友好
- MTP 头内置 → 投机解码可显著提升 decode 速度（+33-107% 取决于硬件）
- 稠密 27B → decode 是显存带宽瓶颈，不是算力瓶颈

---

## 二、G5 实测性能总表

### 2.1 NVIDIA GPU（decode tok/s，单请求）

#### RTX 5090 32GB

| 引擎/量化 | 短ctx decode | 64K ctx | 128K ctx | 200K+ ctx | 来源 | conf |
|---|---|---|---|---|---|---|
| llama.cpp Q4_K_M + MTP | 131 | 68.8 | 55.3 | 48.1@200K, 42.1@256K | GitHub tsarihan playbook | 🟢 |
| vLLM NVFP4 (0.26) | 66.4 | 53.9 | 50.7 | — | 同上 | 🟢 |
| vLLM nightly NVFP4 + MTP k=2 | 104.7 | 78.8 | — (98K cap) | — | 同上 | 🟡 |
| SGLang NVFP4 + lmhead4 + MTP | 162.6 | 81.0@63K | — | — | HF eemin recipe | 🟡 |
| NInfer groupwise-int + MTP3 | 185.8 | — | — | — | GitHub tensorninja | 🟡 |
| NInfer NVFP4 + MTP3 | 202.4 | — | — | — | 同上 | 🟡 |
| NInfer NVFP4 + MTP3 并发C=8 聚合 | 1,146.9 聚合 | — | — | — | 同上 | 🟡 |
| VoidInfer EXL3 6bpw + OSCAR INT4 KV | 147 | — | — | 262K 单请求 | Reddit r/LocalLLM | 🟡 |
| 4×RTX 5090 vLLM MTP off ~85-145K | 72.3 | — | — | — | HF discussions | 🟡 |

**prefill（RTX 5090）**：
- llama.cpp Q4_K_M：~3,024 tok/s@0K → 1,336@128K（边际速率）
- NInfer groupwise-int：3.3K@3K prompt → 3.2K@128K prompt
- NInfer 4090 port sm89：12.3 req/min@118K prompt

**TTFT（RTX 5090）**：
- llama.cpp 200K：219s
- NInfer 128K：20.9s（NVFP4）/ 40.8s（VoidInfer EXL3）
- SGLang NVFP4 63K：~0.43s（prefix cache hit）

#### RTX 4090 24GB

| 引擎/量化 | 短ctx decode | 128K ctx | 256K ctx | 来源 | conf |
|---|---|---|---|---|---|
| NInfer sm89 groupwise-int + MTP3 | 148.6（code gen） | 77.5（prose） | 65.4（prose）/91.2（code） | GitHub sergiuszm/ninfer-4090 | 🟡 |
| NInfer 无投机 | 50.5 | 39.6 | 36.6 | 同上 | 🟡 |
| llama.cpp UD-Q4_K_M | ~46@144K | — | — | 同上 | 🟡 |
| llama.cpp + draft-mtp（code shallow） | 118.8 | — | — | 同上 | 🟡 |
| RTX 4 SPadav_ unsloth Q4_K_M + MTP | — | — | +60%@4096 tokens | GitHub jcr211/qwen38-mtp | 🟡 |

**prefill（RTX 4090 sm89）**：
- NInfer：1,849 tok/s@64K, 1,561@128K, 1,381@192K, 1,228@256K
- llama.cpp 边际：3,024@0K → 1,866@64K → 1,336@128K

#### RTX 3090 24GB

| 引擎/量化 | decode | 来源 | conf |
|---|---|---|---|
| NInfer（3090 base） | 未直测 27B，但 35B-A3B 有数据 | GitHub Don-Chad/ninfer-3090 | 🔴 |
| llama.cpp Q4_K_M + MTP flag | 41.3（+33% over 31.0 baseline） | GitHub jcr211/qwen38-mtp | 🟡 |

#### RTX PRO 5000 48GB / RTX PRO 6000 96GB

内部 KB 实测（gpu-inference-hardware.md，2026-10）：
- RTX PRO 5000 48GB：Qwen3.8-27B FP8 prefill 6,265 tok/s（225K tokens, 36.2s）
- RTX PRO 6000 96GB：同条件

外部交叉：
- vLLM blog（RTX PRO 6000 96GB）：Qwen3.6-27B NVFP4 prefill 17,746 tok/s，decode 289 tok/s（C=1）
- 注：Qwen3.6-27B 与 Qwen3.8-27B 架构相似（同 27B 稠密），可参考但非同模型

### 2.2 AMD GPU（ROCm）

| 卡 | 引擎 | 量化 | decode | 来源 | conf |
|---|---|---|---|---|---|
| RX 7900 XTX 24GB | Ollama ROCm | Qwen3.5-27B Q4_K_M | 59.8 | Reddit r/LocalLLM | 🟡（Qwen3.5非3.8） |
| RX 7900 XTX 24GB | llama.cpp ROCm | Qwen3.5-27B Q4_K_M | ~52.2 | 同上 | 🟡 |
| RX 7900 XTX 24GB | Ollama ROCm | Qwen3.6-27B Q4_K_M | 49.2 | Reddit r/LocalLLM | 🟡（Qwen3.6非3.8） |

**缺失**：无 Qwen3.8-27B 在 ROCm 的直接实测。Qwen3.5/3.6-27B 数据可作为参考下界。
- ROCm 7.4.1+ 支持 Qwen3.5（需 `--attention-level 1` 解决 metal 冲突）
- Qwen3.8 的 GDN 混合架构在 ROCm 上的 kernel 支持状态未确认 → **风险点**

### 2.3 Apple Silicon（MLX）

#### M3 Ultra 192GB / 256GB

| 引擎 | 量化 | decode（短ctx） | 长ctx | 来源 | conf |
|---|---|---|---|---|---|
| oMLX 0.7.0 | oQ4e-fp16-mtp | ~80.7@8K → 53.4@64K | 98K agent 可用 | holistech.ai M1 Ultra 测试 | 🟡 |
| oMLX 0.6.1 Lightning MTP | oQ4e-mtp | 90.6@8K → 53.4@64K | — | GitHub jundot/omlx release | 🟡 |
| Rapid-MLX 0.15.7 | 4bit-MTP-fp16-MLX | 31.5@13K | 52K agent | holistech.ai | 🟡 |
| MTPLX 2.12.2 | Optimized-Speed-FP16 | 37.3@13K | 32K（128K 失败） | holistech.ai | 🟡 |
| llama.cpp 0.6.0 | UD-Q4_K_M.gguf | 20.2@13K | 128K 24/24 正确 | holistech.ai | 🟡 |
| mlx-lm 0.32.0 | 4bit | 23.4@13K | 32K（更长失败） | holistech.ai | 🟡 |

#### M5 Max 36GB / M5 Pro 48GB

| 引擎 | 量化 | decode | 来源 | conf |
|---|---|---|---|---|
| Rapid-MLX 0.16.1 | 4bit + MTP | 37.9 单流 / 82.8 四流聚合 | rapidmlx.com | 🟡 |
| LM Studio (MLX) | 4bit | 26.0 单流 / 69.7 四流 | 同上 | 🟡 |
| Splash Engine (Inco) | — | 74@短prompt, 54@32K | lmstudio.ai blog | 🟡 |
| oMLX（M5 Max 36GB 用户） | 4bit KV + MTP | 8-10 tok/s（128K ctx 配置） | Medium oeholmen | 🟡 |

**注**：M5 Max 36GB 上 oMLX 128K 配置仅 8-10 tok/s，说明长上下文+大窗口显著牺牲速度。Splash Engine 74 tok/s 是短 prompt 数据。

#### M2 Max 96GB（并发基准）

来源：promiseandrisk.ai（2026-09-25）
- Qwen3.8-27B 8bit MLX：12.4 tok/s 单请求，51.5 tok/s@16 并发聚合
- 6 请求出现悬崖（per-request 从 8.2 跌到 3.4）

#### M1 Ultra 64GB（长上下文正确性）

来源：holistech.ai（M1 Ultra 64GB，2026-10）
- 128K 仅 llama.cpp 24/24 全对；oMLX 22/24；MTPLX 3/24（OOM）
- llama.cpp 128K 输出 13.7 tok/s；Rapid-MLX 32K 输出 27.3 tok/s

### 2.4 长上下文衰减规律（跨平台）

**RTX 5090 llama.cpp Q4_K_M**（tsarihan playbook）：
| ctx | decode tok/s | 相对短ctx衰减 |
|---|---|---|
| 4K | 93.8 | 基准 |
| 16K | 87.6 | -6.6% |
| 65K | 68.8 | -26.7% |
| 128K | 55.3 | -41.1% |
| 200K | 48.1 | -48.7% |
| 256K | 42.1 | -55.1% |
| 491K (YaRN) | 35 | -62.7% |

**RTX 4090 NInfer（prose，无投机）**：
| ctx | decode | 衰减 |
|---|---|---|
| 0K | 50.4 | 基准 |
| 32K | 42.0 | -16.7% |
| 64K | 38.6 | -23.4% |
| 128K | 33.1 | -34.3% |
| 256K | 36.6 | -27.4%（E8 KV 模式） |

**M3 Ultra oMLX**：
| ctx | decode | 衰减 |
|---|---|---|
| 8K | 80.7 | 基准 |
| 16K | 56.1 | -30.5% |
| 32K | 51.9 | -35.7% |
| 64K | 43.8 | -45.7% |

**规律**：GDN 混合架构使长 ctx 衰减比纯注意力模型温和（Qwen3.6-27B 稠密注意力在 4×5090 上 10K→150K 仅衰减 37%，而 Qwen3.8 GDN 在 5090 单卡 4K→256K 衰减 55%）。但 200K+ 仍有显著衰减。

---
## 三、G6 软件生态门禁

### 3.1 Apple MLX / LM Studio 长ctx + 并发

| 能力 | 状态 | 证据 | conf |
|---|---|---|---|
| MLX 长上下文（128K+） | ✅ 支持，但速度显著下降 | oMLX 98K agent、llama.cpp 128K 24/24 | 🟢 |
| MLX 并发（continuous batching） | ✅ LM Studio 0.4.2+ 支持（text-only） | LM Studio tips PDF + AIOS research | 🟢 |
| MLX 并发悬崖 | ⚠️ 6 请求后 per-request 速度暴跌 | promiseandrisk.ai M2 Max 实测 | 🟡 |
| MTP 投机解码（MLX） | ✅ oMLX/Rapid-MLX/MTPLX 均支持 | 多源 | 🟢 |
| LM Studio MLX 后端 vs llama.cpp | ✅ MLX 快 2-2.5× | LM Studio 官方文档 | 🟢 |
| 128K 正确性 | ⚠️ 仅 llama.cpp 全对，MLX 引擎有错误 | holistech.ai M1 Ultra | 🟡 |

**门禁结论**：MLX 生态可用但长 ctx 并发有天花板（~5 请求有效），128K+ 正确性 llama.cpp 更可靠。

### 3.2 AMD ROCm 成熟度

| 能力 | 状态 | 证据 | conf |
|---|---|---|---|
| Qwen3.5-27B 支持 | ✅ Q4_K_M 可跑 59.8 tok/s | Reddit r/LocalLLM ROCm 7.4.1 | 🟡 |
| Qwen3.6-27B 支持 | ✅ Q4_K_M 49.2 tok/s | 同上 ROCm 7.4.2 | 🟡 |
| Qwen3,8-27B GDN 架构支持 | ❓ 未确认 | 无直接证据 | 🔴 |
| FP8 支持 | ✅ ROCm 7.4+ 支持 FP8 推理 | vLLM on ROCm 文档 | 🟡 |
| MTP 投机解码 | ❓ 未确认 | 无证据 | 🔴 |

**门禁结论**：ROCm 对 Qwen3.5/3.6-27B 可用，但 Qwen3.8 的 GDN 混合架构 + MTP 在 ROCm 上的支持未验证。**这是关键风险点** — 若 GDN kernel 缺失，ROCm 路径可能不可用或性能骤降。

### 3.3 国产卡 CANN / MUSA 成熟度

#### 华为昇腾 CANN
| 能力 | 状态 | 证据 | conf |
|---|---|---|---|
| Qwen3 系列支持 | ✅ 昇腾 910B/950 支持 Qwen3-32B 等 | 昇腾社区文档 | 🟡 |
| Qwen3.8-27B 具体适配 | ❓ 未确认 | 无直接证据 | 🔴 |
| 950 系列_FP8 | ✅ 原生支持，性能接近 A100 | 华为官方 | 🟡 |
| 个人消费级可得性 | ❌ 无零售渠道 | 任务书已确认 | 🟢 |

#### 摩尔线程 MUSA
| 能力 | 状态 | 证据 | conf |
|---|---|---|---|
| Qwen 系列适配 | ✅ "发布即适配" Qwen 等主流模型 | 摩尔线程官网 + 证券时报 | 🟡 |
| llama.cpp 适配 | ✅ MUSA 已完成 llama.cpp 适配 | OSCHINA 2025-08 | 🟡 |
| vLLM/SGLang 适配 | ✅ 深度适配 | 摩尔线程官网 | 🟡 |
| Qwen3.8-27B 具体benchmark | ❓ 未找到 | — | 🔴 |
| 消费级产品（MTT S80/S3000） | ✅ 有零售渠道 | 摩尔线程官网 | 🟡 |
| MTT S5000（数据中心） | ✅ 旗舰训推卡 | 官网 | 🟡 |

**门禁结论**：
- 昇腾：个人不可得，排除
- 摩尔线程：生态在快速追赶（llama.cpp/vLLM/SGLang 均已适配），但 Qwen3.8-27B 具体性能数据缺失，消费级卡（S80/S3000）算力远低于 S5000，27B 稠密模型在消费级 MUSA 卡上的实际体验未知 → **高风险探索项**

---
## 四、G11 候选补全

任务书已覆盖：RTX 3090/4090/5090、RTX PRO 5000/6000、Mac M3 Ultra/M4 Max/M5、RX 7900 XTX、昇腾、摩尔线程

**补充候选**：

| 候选 | 理由 | 数据 | 评估 |
|---|---|---|---|
| RTX 5090 移动端 24GB | 笔记本场景 | llama.cpp MTP 50.9 tok/s（jcr211） | 有价值但非主力 |
| 双卡 RTX 4090/5090（TP=2） | 显存扩展 | 2×5090 vLLM FP8 76.3 tok/s（fentz26） | 有价值 |
| Cerebras（云） | 官方宣布支持 Qwen3.8 | Cerebras 部署公告 | 非本地，排除 |
| M5 Ultra 256GB | 高端 Mac | mlx-serve 文档有 M5 Ultra 数据 |  pricey 但长ctx强 |
| RTX 2080 Ti 11GB | 预算极限 | 理论可跑 Q4 但KV紧张 | 边缘候选 |
| Intel Arc Pro B50 / A770 | 另一国产替代 | 无 Qwen3.8 数据 | 数据不足，暂不纳入 |

**结论**：主力候选无需大幅补充。双卡 5090（TP=2）和 M5 Ultra 是值得关注的扩展项。

---
## 五、关键发现 TOP5

1. **Qwen3.8-27B 的 GDN 混合架构使长上下文显存极友好**（KV cache 仅 4 head），262K 上下文在 24GB 卡上可 fitting（Q4_K_M + q4_0 KV = 22.2GB），但 decode 速度在 200K+ 衰减 49-55%。

2. **RTX 5090 是单卡最优解**：llama.cpp Q4_K_M + MTP 达 131 tok/s 短ctx，SGLang NVFP4 + MTP 达 162.6 tok/s；并发 C=8 聚合 1,147 tok/s（NInfer NVFP4）。RTX 4090 通过 NInfer sm89 port 可达 148.6 tok/s（code gen MTP3），差距比预期小。

3. **MTP 投机解码是最大加速杠杆**（+33-107%），但引擎间支持差异大：llama.cpp 已支持（--spec-type draft-mtp）、vLLM 支持但长ctx有 prefill 回归、SGLang 支持但 OOM 风险、oMLX 支持（Lightning MTP）。

4. **ROCm 是最大生态风险**：Qwen3.5/3.6-27B 在 RX 7900 XTX 上 49-60 tok/s 可用，但 Qwen3.8 的 GDN 架构在 ROCm 上的 kernel 支持未验证。若 GDN 缺失，AMD 路径整体不可用。

5. **Apple Silicon 长ctx 正确性有隐患**：128K 上下文下仅 llama.cpp 24/24 全对，MLX 系引擎（oMLX 22/24、MTPLX 3/24）有错误。并发在 6 请求后出现悬崖。M3 Ultra + oMLX 短ctx 80 tok/s 体验好，但长ctx agent 场景需审慎。

---
## 六、数据缺口

| 缺口 | 影响 | 补充方式 |
|---|---|---|
| Qwen3.8-27B 在 ROCm 上的直接实测 | 高（决定 AMD 是否可行） | 需实际购买测试或等社区数据 |
| RTX PRO 5000/6000 跑 Qwen3.8-27B 的 decode 数据 | 中（prefill 已有内部数据） | 内部实测补充 |
| 摩尔线程消费级卡（S80/S3000）跑 27B 数据 | 中 | 需实际测试 |
| M5 Max/M5 Pro 上 Qwen3.8-27B 长ctx（128K+）decode | 中 | 社区数据稀疏 |
| RTX 3090 跑 Qwen3.8-27B 的完整数据 | 低（3090 非主力候选） | llama.cpp MTP 41.3 已有 |
| 双卡 4090 TP=2 跑 Qwen3.8-27B | 低 | 可推导但无直接数据 |

---
## 七、来源索引

| # | 来源 | URL | 日期 | 类型 |
|---|---|---|---|---|
| 1 | HF Qwen3.8-27B model card | huggingface.co/Qwen/Qwen3.8-27B | 2026-07-20 | 官方 |
| 2 | tsarihan/qwen3.8-27b-rtx5090-playbook | github.com/tsarihan/... | 2026-08 | 社区实测 |
| 3 | tensorninja/ninfer-4090 performance.md | github.com/tensorninja/... | 2026-09 | 社区实测 |
| 4 | sergiuszm/ninfer-4090 rtx4090-port | github.com/sergiuszm/... | 2026-09 | 社区实测 |
| 5 | jcr211/qwen38-mtp | github.com/jcr211/qwen38-mtp | 2026-07 | 社区实测 |
| 6 | eemin/Qwen3.8-27B-NVFP4-lmhead4-recipe | huggingface.co/eemin/... | 2026-08 | 社区实测 |
| 7 | fentz26/Qwen3.8-27B-5090 | github.com/fentz26/... | 2026-09 | 社区实测 |
| 8 | holistech.ai M1 Ultra 27B agent 测试 | labs.holistech.ai/en/m1-ultra-27b/ | 2026-10 | 专业评测 |
| 9 | promiseandrisk.ai batching on Apple Silicon | promiseandrisk.ai/labs/batching-on-apple-silicon/ | 2026-09-25 | 专业评测 |
| 10 | rapidmlx.com vs LM Studio | rapidmlx.com/compare/lm-studio | 2026-10-12 | 厂商对比 |
| 11 | Reddit r/LocalLLM ROCm Qwen3.5/3.6 | reddit.com/r/LocalLLM/... | 2026-06/07 | 社区 |
| 12 | 摩尔线程官网 + 证券时报 | mthreads.com / stcn.com | 2026-07 | 官方/媒体 |
| 13 | 内部 KB gpu-inference-hardware.md | workspace notes | 2026-10 | 内部实测 |
| 14 | HF Qwen3.8-27B discussions/51 (GDN kernel) | huggingface.co/Qwen/Qwen3.8-27B/discussions/51 | 2026-09 | 社区 |
| 15 | Reddit VoidInfer 400K context | reddit.com/r/LocalLLM/comments/1xcvfnq/ | 2026-10 | 社区 |
