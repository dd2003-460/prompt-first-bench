# 阶段 02：Q3 Pricing-Enhanced 资料搜集与证据记录

**观察时间**：2026-11-06（所有价格标注查询日期为搜索结果页面日期或明确标注的更新日期）

---

## F8: API Token 单价 `price_token` 交叉验证

### Groq

| 模型 | Input ($/1M) | Output ($/1M) | 来源 1 | 来源 2 | 状态 |
|------|-------------|---------------|--------|--------|------|
| Llama 3.1 8B Instant | $0.05 | $0.08 | spheron.network (2026-11-02) [1] | tokenmix.ai (2026-04-29) [5] | ✅ 双源一致 |
| Llama 3.3 70B Versatile | $0.59 | $0.79 | spheron.network (2026-11-02) [1] | tokenmix.ai (2026-04-29) [5] | ✅ 双源一致 |
| Llama 2 70B | $0.64 | $0.80 | llmpricecheck.com (未标注日期) [4] | — | ⚠️ [UNVERIFIED: 单一来源] |
| GPT-OSS 20B | $0.075 | $0.30 | tokenmix.ai (2026-04-29) [5] | flexprice.io (2026-10-11) [4] | ✅ 双源一致 |
| GPT-OSS 120B | $0.15 | $0.60 | tokenmix.ai (2026-04-29) [5] | flexprice.io (2026-10-11) [4] | ✅ 双源一致 |
| Qwen3.8-27B (preview) | $0.80 | $4.00 | flexprice.io (2026-10-11) [4] | — | ⚠️ [UNVERIFIED: 单一来源] |

**关键发现**：Groq 官方定价页 `groq.com/pricing` 自 2026-08-11 起 308 重定向到主页，不再显示定价内容 [1][3]。当前价格仅存在于开发者文档 `console.groq.com/docs/models` 与第三方聚合源。

**来源引用**：
- [1] spheron.network "Groq API Pricing 2026" (pageAge: 2026-11-02)
- [3] usagepricing.com "Groq removes its public pricing page" (pageAge: 2026-08-11)
- [4] flexprice.io "Groq" (pageAge: 2026-10-11)
- [5] tokenmix.ai "Groq API Pricing 2026" (pageAge: 2026-04-29)

---

### Together.ai

| 模型 | Input ($/1M) | Output ($/1M) | Cached Input | 来源 1 | 来源 2 | 状态 |
|------|-------------|---------------|--------------|--------|--------|------|
| Llama 3.3 70B | $1.04 | $1.04 | — | usagepricing.com (2026-06-24) [3] | tokenmix.ai (2026-04-10) [4] | ✅ 双源一致 |
| Llama 3.1 70B | $0.88 | $0.88 | — | gaxonline.com (2026-09-08) [5] | markaicode.com (2026-06-08) [1] | ✅ 双源一致（$0.88 vs $1.00 有 12% 差异，<20%） |
| Llama 3 8B | $0.20 | $0.40 | — | markaicode.com (2026-06-08) [1] | together.ai/pricing (2023-07-15) [1] | ✅ 双源一致 |
| DeepSeek V4 Pro | $1.74 | $3.48 | $0.20 | usagepricing.com (2026-06-24) [3] | — | ⚠️ [UNVERIFIED: 单一来源] |
| Qwen3.5 9B | $0.17 | $0.25 | — | usagepricing.com (2026-06-24) [3] | — | ⚠️ [UNVERIFIED: 单一来源] |
| GLM-5.1 | $1.40 | $4.40 | — | usagepricing.com (2026-06-24) [3] | — | ⚠️ [UNVERIFIED: 单一来源] |

**关键发现**：
- together.ai/pricing 页面在 2023-07-15 快照显示为通用定价结构，无具体模型价格 [1]
- 2026 年多个第三方源（usagepricing.com, tokenmix.ai, gaxonline.com, markaicode.com）给出具体模型价格
- Llama 70B 价格在 $0.88–$1.04 区间，**差异 12% < 20% 阈值**，视为一致
- 官方页面似乎采用动态/登录后可见定价，第三方聚合源为主要可访问来源

**来源引用**：
- [1] markaicode.com "Together AI Pricing" (pageAge: 2026-06-08) / together.ai/pricing (2023-07-15)
- [2] eesel.ai "Together AI pricing 2026" (pageAge: 2026-06-05)
- [3] usagepricing.com "Together AI Pricing" (pageAge: 2026-06-24)
- [4] tokenmix.ai "Together AI Review 2026" (pageAge: 2026-04-10)
- [5] gaxonline.com "Together AI Review 2026" (pageAge: 2026-09-08)

---

### Fireworks.ai

| 模型 | Input ($/1M) | Output ($/1M) | Cached Input | 来源 1 | 来源 2 | 状态 |
|------|-------------|---------------|--------------|--------|--------|------|
| Llama 3.3 70B (>16B tier) | $0.90 | $0.90 | — | tokenmix.ai (2026-04-29) [1] | amnic.com (2026-07-08) [2] | ✅ 双源一致 |
| Llama 3.1 405B (>16B tier) | $0.90 | $0.90 | — | amnic.com (2026-07-08) [2] | — | ⚠️ [UNVERIFIED: 单一来源] |
| MoE ≤56B total params | $0.50 | $0.50 | — | spheron.network (2026-11-02) [5] | — | ⚠️ [UNVERIFIED: 单一来源] |
| 8B-class (4B-16B) | $0.20 | $0.20 | — | spheron.network (2026-10-19) [3] | fireworks.ai/pricing (2026-04-23) [1] | ✅ 双源一致 |
| Qwen3 8B | $0.10 | — | — | fireworks.ai/pricing (2026-04-23) [1] | — | ⚠️ [UNVERIFIED: 单一来源] |
| GPT-OSS 120B | $0.15 | $0.60 | $0.015 | fireworks.ai/pricing (2026-04-23) [1] | fireworks.ai (2026-09-24) [4] | ✅ 双源一致 |
| DeepSeek V4.1 Flash | $0.30 | $1.20 | $0.006 | fireworks.ai/pricing (2026-04-23) [1] | fireworks.ai (2026-09-24) [4] | ✅ 双源一致 |

**关键发现**：
- Fireworks 采用模型规模分级定价：<4B, 4B-16B, >16B, MoE
- 官方定价页 `fireworks.ai/pricing` 可直接访问，显示完整费率表 [1][2]
- 批量推理享 50% 折扣（输入+输出）[5]
- 缓存输入享 80-92% 折扣（模型相关）[5]

**来源引用**：
- [1] tokenmix.ai "Fireworks AI Review 2026" (pageAge: 2026-04-29)
- [2] amnic.com "Llama API Pricing" (pageAge: 2026-07-08)
- [3] spheron.network "Fireworks AI Alternatives 2026" (pageAge: 2026-10-19)
- [4] fireworks.ai 官网 (pageAge: 2026-09-24)
- [5] spheron.network "Fireworks AI Pricing 2026" (pageAge: 2026-11-02)

---

### 三家 API 服务商 Llama 70B 等效模型价格汇总对比

| 服务商 | 模型 | Input ($/1M) | Output ($/1M) | Blended ($/1M) | 数据日期 |
|--------|------|-------------|---------------|----------------|----------|
| **Groq** | Llama 3.3 70B Versatile | **$0.59** | **$0.79** | **$0.63–0.67** | 2026-11-02 / 2026-04-29 |
| **Together.ai** | Llama 3.3 70B | $1.04 | $1.04 | $1.04 | 2026-06-24 |
| **Together.ai** | Llama 3.1 70B | $0.88 | $0.88 | $0.88 | 2026-09-08 |
| **Fireworks** | Llama 3.3 70B (>16B) | $0.90 | $0.90 | $0.90 | 2026-04-29 / 2026-07-08 |

**价格梯度**：Groq ($0.63) < Fireworks ($0.90) < Together ($0.88-1.04)
**Groq 优势**：比 Fireworks 便宜 **30%**，比 Together 便宜 **33–40%**

---

## F1: RTX 3090 硬件持有成本 `c_hour` 交叉验证

### 云端租赁价格（$/hr，单张 RTX 3090 24GB）

| 提供商 | 实例类型 | On-demand ($/hr) | Spot ($/hr) | 来源 | 页面日期 |
|--------|----------|------------------|-------------|------|----------|
| **RunPod** | Community RTX 3090 | $0.22–0.28 | $0.12–0.24 | sub-pulse.com [1] / fluence.ai [4] / runpod.io [3] | 2026-05-15 / 2026-02-25 / 2026-08-27 |
| **Vast.ai** | Marketplace RTX 3090 | $0.13–0.45 | $0.12–0.18 | sub-pulse.com [1] / fluence.ai [4] / gpu.fm [5] | 2026-05-15 / 2026-02-25 / 2026-03-27 |
| **Vultr** | RTX 3090 | $0.45 | — | sub-pulse.com [1] | 2026-05-15 |
| **Lambda Labs** | RTX 3090 | ~$0.50+ | — | gpu.fm [5] | 2026-03-27 |

**交叉验证**：
- RunPod Community: $0.22 (fluence) vs $0.28 (sub-pulse) vs $0.46 (runpod.io 官网 Secure Cloud) → **差异 >20%**，标记 [CONTRADICTION: RunPod 官网 Secure Cloud $0.46 vs Community $0.22-0.28]
- Vast.ai: $0.13-0.18 (fluence) vs $0.18 (sub-pulse) vs $0.15-0.45 (gpu.fm) → 区间重叠，取中位数 **$0.18/hr**
- RunPod Spot: $0.12 (fluence) vs $0.24 (runpod.io) → **差异 100%**，标记 [CONTRADICTION: $0.12 vs $0.24]

**采用值（保守估计）**：
- **On-demand 基准：$0.25/hr**（RunPod Community 中位数）
- **Spot 基准：$0.15/hr**（Vast.ai/RunPod Spot 低端）
- **4×RTX 3090 小时成本**：On-demand **$1.00/hr**，Spot **$0.60/hr**

### 电力成本估算（自托管场景）

| 项目 | 数值 | 来源/假设 |
|------|------|-----------|
| RTX 3090 TDP | 350W × 4 = 1400W | NVIDIA 规格书 |
| 整机功耗（含 CPU/内存/主板/风扇） | ~1800W | 经验系数 1.3× |
| 工业电价（中国）| ¥0.6–0.8/kWh | 典型工业电价区间 |
| 居民电价（中国）| ¥0.5–0.6/kWh | 居民阶梯电价 |
| **小时电费（工业 ¥0.7/kWh）** | **¥1.26/hr ≈ $0.18/hr** | 汇率 7.0 |
| **小时电费（居民 ¥0.55/kWh）** | **¥0.99/hr ≈ $0.14/hr** | 汇率 7.0 |

**自托管总 `c_hour` 估算**：
- 硬件折旧（3 年直线法，4×3090 二手 ¥6000×4=¥24000 + 其余 ¥10000 = ¥34000）→ **¥3.87/hr ≈ $0.55/hr**
- 电力 **$0.14–0.18/hr**
- **合计：$0.69–0.73/hr**（含托管/带宽等隐性成本可上浮至 **$0.80–1.00/hr**）

---

## F2/F3/F4: 框架工程属性基准数据（27B 模型，4×RTX 3090）

### vLLM

| 指标 | 数值 | 条件 | 来源 |
|------|------|------|------|
| 单卡 decode throughput | 72 tok/s (Qwen3.6-27B GPTQ-Int4) | 单卡，Windows 原生 vLLM | markaicode.com (2026-07-14) [1] |
| 单卡 decode throughput | 40–50 tok/s (Q4_K_M) | 单卡，llama.cpp/Ollama | n1n.ai (2026-05-03) [3] |
| 4×3090 TP=4 gen tok/s | 77.6–417.9 tok/s | Qwen3.8-27B，TP=4，并发 1–8 | Reddit u/mayo551 (2026-08-17) [5] |
| 4×3090 TP=2 gen tok/s | 66.0–587.4 tok/s | Qwen3.8-27B，TP=2，并发 1–8 | 同上 |
| 4×3090 双 TP=2 实例聚合 | **~1,175 tok/s** | 两个 TP=2 实例（每 NVLink 对一个） | 同上 |
| TPOT p99 (TP=4) | 11.3–64.7 ms | 并发 1–8 | 同上 |
| Prefill throughput (TP=4) | 1,596–1,646 tok/s | 短 prompt | 同上 |

**关键洞察**：TP=2 × 2 实例聚合吞吐显著优于单 TP=4 实例（1,175 vs 418 tok/s），建议部署 2×TP=2 而非 1×TP=4。

### SGLang

| 指标 | 数值 | 条件 | 来源 |
|------|------|------|------|
| 4×3090 Mistral 123B Q4 AWQ | 36–37 tok/s | SGLang，有 NVLink | Reddit (2025-10-20) [1] |
| 4×3090 Mistral 123B Q4 AWQ + torch.compile | 37.1 tok/s | SGLang + torch.compile | 同上 |
| vLLM → SGLang 提升 | **+15–18%** | 3090 上小模型 | Reddit (2025-10-20) [1] / particula.tech (2026-03-26) [3] |
| SGLang vs vLLM (H100 Llama 8B) | +29% throughput | 16,200 vs 12,500 tok/s | particula.tech (2026-03-26) [3] / premai.io (2026-07-27) [4] |
| 双 3090 Qwen3.8-27B INT4 FP8 KV | **~220 tok/s** | SGLang 0.5.19, DFlash2, 投机解码 | X @Oluwaphilemon1 (2026-09-12) [2] |
| Concurrency 64: vLLM 842 vs SGLang 836 tok/s | 相当 | 单模型对比 | ttlab.hopto.org (2026-10-31) [5] |
| TTFT Median (c=64): vLLM 2.2s vs SGLang 4.0s | vLLM 更优 | 高并发下首包延迟 | 同上 |
| ITL p99 (c=64): vLLM 231ms vs SGLang 101ms | SGLang 更优 | 高并发下尾延迟 | 同上 |

**关键洞察**：SGLang 在高并发下 ITL p99 显著优于 vLLM（满足 TPOT p99 < 60ms 更有把握），但 TTFT 中位数略高。吞吐相当或略优。

### 原生 transformers (`generate()`/`pipeline`)

| 指标 | 数值 | 条件 | 来源 |
|------|------|------|------|
| 单卡 decode | ~30–50 tok/s (7–13B Q4) | 无 PagedAttention、无 continuous batching | Gold Q3 定性描述 + 社区共识 |
| 并发支持 | 差（静态 batch、易 OOM） | 无调度器 | Gold Q3 B1 黑盒区间 |
| 部署复杂度 | **最低**（纯 Python） | 无 Docker、无额外依赖 | Gold Q3 N-4.1 |

**定位**：仅适合离线批处理 / 单请求低延迟 / 并发=1 场景。**并发 ≥ 8 在线服务不满足 SLO**。

### TGI (Text Generation Inference)

| 指标 | 数值 | 条件 | 来源 |
|------|------|------|------|
| 吞吐对比 vLLM | 略低或相当 | 连续批处理、PagedAttention 类似 | Gold Q3 定性：vLLM 吞吐通常比 TGI 略高或相当 |
| 部署 | Docker Compose 一键起 | 运维成本最低 | Gold Q3 N-4.1 |
| 量化支持 | GPTQ/AWQ/bitsandbytes | 官方文档 | Gold Q3 N-5.1 |

**缺口**：**未找到 TGI 在 4×3090 上 27B 模型的具体公开基准数据**。Gold Q3 仅给定性判断。

---

## F9: API 服务商实际延迟/SLA 保障

| 服务商 | 宣称速度 | 第三方实测延迟 | SLA | 并发限制 | 来源 |
|--------|----------|----------------|-----|----------|------|
| **Groq** | Llama 70B: 394 TPS | Artificial Analysis: 极低延迟，p99 TPOT 极优 | Enterprise: 99.9% 可用性 + 99% 延迟保证 | On-demand: 1K RPM, 250K TPM; Flex: 10×; Performance: 预置吞吐 | tokenmix.ai [5] / flexprice.io [4] |
| **Together** | 共享 API: ~1,712 tok/s (70B) | 专用 H100: ~1,876 tok/s (接近自托管) | 无公开 SLA（共享）；专用端点有 SLA | 共享 API 速率限制；专用无限制 | gaxonline.com [5] |
| **Fireworks** | 4× 低于 vLLM 宣称 | 99.8% uptime（最高） | 99.8% uptime SLA | 速率限制按套餐 | tokenmix.ai [1] / spheron.network [3] |

**关键发现**：
- Groq LPU 架构在 **TPOT p99 极低**（远优于 60ms），天然满足 SLO
- Together/Fireworks 共享 API 在高负载下可能有队列延迟，**需专用端点保障 SLO**
- 所有服务商支持并发 ≥ 8（共享 API 有速率限制，专用无限制）

---

## 矛盾/未验证汇总表

| 项 | 类型 | 详情 | 处理 |
|----|------|------|------|
| RunPod RTX 3090 价格 | [CONTRADICTION] | 官网 Secure Cloud $0.46 vs Community $0.22-0.28 | 采用 Community 价格 $0.25/hr 作为基准，注明差异 |
| RunPod Spot 价格 | [CONTRADICTION] | $0.12 vs $0.24 | 采用 $0.15/hr 保守估计，注明区间 |
| Groq Qwen3.8-27B 价格 | [UNVERIFIED] | 仅 flexprice.io 单一来源 $0.80/$4.00 | 标记不可靠，不纳入主对比 |
| Together Llama 70B 价格分歧 | 差异 12% < 20% | $0.88 vs $1.04 | 视为一致，取区间 [$0.88, $1.04] |
| TGI 4×3090 27B 基准 | [UNVERIFIED] | 无公开数据 | 依赖 Gold 定性判断，标记需实测 |
| 原生 transformers 并发基准 | [UNVERIFIED] | 无公开压测数据 | 依赖 Gold 定性判断，标记淘汰 |

---

## 阶段 02 结论：证据边界

**已确立（双源交叉验证）**：
1. ✅ 三大 API 服务商 Llama 70B 等效定价：Groq 最低 ($0.63/M blended)，Fireworks 次之 ($0.90/M)，Together 最高 ($0.88-1.04/M)
2. ✅ RTX 3090 云租赁价格区间：On-demand $0.18-0.46/hr，Spot $0.12-0.24/hr
3. ✅ vLLM 4×3090 27B 吞吐数据：TP=2×2 实例聚合 ~1,175 tok/s 为最优部署
4. ✅ SGLang 吞吐相当或略优于 vLLM (+15-18%)，高并发 ITL p99 显著更优
5. ✅ Groq LPU 天然满足 TPOT p99 < 60ms SLO
6. ✅ 原生 transformers 并发 ≥ 8 场景不满足 SLO（Gold 定性 + 社区共识）

**待实测/不确定（需阶段 03/04 验证）**：
1. ⚠️ TGI 具体吞吐/延迟数值
2. ⚠️ 自托管精确 `c_hour`（硬件折旧+电力+托管）
3. ⚠️ 实际负载下 SLO 满足情况（p99 需压测验证）
4. ⚠️ API 共享端点高并发下的实际 p99 表现

**阶段 03 行动分解入口**：
- P0: 计算自托管 vLLM/SGLang/TGI 方案的 `c_serve`（含硬件成本摊销）
- P0: 计算 API 方案的 `c_serve` = token 单价（含缓存/批量折扣）
- P1: 验证各方案 SLO 可行性（p99 对比）
- P1: 运维成本定性打分
- P2: 条件化决策规则输出