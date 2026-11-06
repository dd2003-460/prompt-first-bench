# 阶段 01：Q3 Pricing-Enhanced 目标分解

## 任务目标

重做 Q3（推理框架/服务选型），增加价格时效性强制段，验证 pricing-enhanced prompt 能否将 M1 从 0.53 提升到 ≥0.60。

**原始 Q3 题面（仅 question 字段）**：
> 已有 27B 模型权重 + 固定 GPU（RTX 3090×4，96GB 总显存），选一个推理服务框架，使**每千输出 token 的服务成本最低**，且满足在线 SLO（TTFT p99 < 2s，TPOT p99 < 60ms，并发 ≥ 8）。
> 候选：vLLM · TGI（Text Generation Inference）· 原生 transformers（`generate()`/`pipeline`）· （对照：SGLang，作为国内/长上下文备选）。

**Pricing-Enhanced 扩展**：将候选集扩展至 API 服务商（Groq, Together.ai, Fireworks.ai 等），引入真实价格数据，按 [as of YYYY-MM-DD] 标注、双源交叉验证、差异 >20% 标 [CONTRADICTION]、无法确认标 [UNVERIFIED]。

---

## 顶层影响因素分解（L1）

目标：最小化 `c_serve = c_hour / (λ_out × u)`，受约束于 SLO（TTFT p99 < 2s, TPOT p99 < 60ms, 并发 ≥ 8）。

| 因素编号 | 因素名称 | 正交性说明 | 优先级 |
|---------|---------|-----------|--------|
| F1 | **硬件持有成本 `c_hour`** | 仅影响分子，与框架/服务商无关；自托管场景为常数，API 场景隐含在 token 定价中 | 高 |
| F2 | **输出吞吐 `λ_out`** | 分母核心变量，框架/服务商间差异 1.3–2.5×（原 gold B1 黑盒） | 高 |
| F3 | **延迟可行性 `latency_ok`** | 硬约束：不达 SLO 直接淘汰，无论成本 | 高 |
| F4 | **显存/并发容量 `mem_eff`** | 决定最大并发 n = min(n_mem, n_slo)，间接影响 λ_out | 中 |
| F5 | **运维成本 `ops_cost`** | 次级 tie-breaker，吞吐差 <10% 时生效 | 低 |
| F6 | **功能完备 `feature`** | 量化/投机解码/长上下文，特定场景门槛 | 低 |
| F7 | **可行域 `feasible`** | 硬件/模型支持的一票否决项 | 高（约束） |
| F8 | **API Token 单价 `price_token`** | **新增**：API 服务商按 token 计费时的直接成本分子 | 高（新增） |
| F9 | **API 吞吐/SLA 保障 `api_slo`** | **新增**：API 服务商的实际延迟表现与承诺 SLA | 高（新增） |

**正交性检验**：
- F1 (硬件成本) 与 F8 (API token 价) 互斥：自托管用 F1，API 用 F8
- F2 (吞吐) 与 F3 (延迟) 正交：吞吐看平均，延迟看 p99
- F4 (显存/并发) 与 F2 耦合：通过 SHARED 参数 `n = min(n_mem, n_slo)` 关联（原 gold 已标注）

---

## 已知条件（人类提供/项目可推导）

| 条件 | 来源 | 确定性 |
|------|------|--------|
| 目标模型：27B 权重（假设为 Llama-2-27B 或同规模） | 题面给定 | 确定 |
| 目标硬件：RTX 3090 × 4，96GB 总显存 | 题面给定 | 确定 |
| 负载画像：in≈1500 / out≈500 token，并发 8–32 | Gold Q3 口径声明 | 确定 |
| SLO：TTFT p99 < 2s，TPOT p99 < 60ms，并发 ≥ 8 | 题面给定 | 确定 |
| 成本口径：只算框架带来的增量成本差异；`c_hour` 常数项在排名中抵消，但绝对值仍要报 | Gold Q3 | 确定 |

---

## 空缺条件（需阶段 02 研究）

### F1 硬件持有成本 `c_hour` 相关

| 空缺项 | 子问题 | 阻塞判断 | 研究路径 |
|--------|--------|----------|----------|
| [待研究] RTX 3090 24GB 当前市场价/租赁价 | 1) 单卡购买价（二手/翻新） 2) 云端租赁价（$/h） 3) 电力/托管成本 | 决定自托管 `c_hour` 分子 | 京东/淘宝/闲鱼二手价；AWS/GCP/Azure/RunPod/lambda.ai 云 GPU 定价页；电价按工业/居民价估算 |
| [待研究] 服务器其余组件成本（CPU、内存、主板、机箱、电源） | 单次采购成本摊销到小时 | 影响 `c_hour` 绝对值 | 参考 DIY 服务器 BOM 或云实例溢价反推 |

### F2/F3/F4 框架工程属性（原 gold 黑盒 B1/B2/B3）

| 空缺项 | 子问题 | 阻塞判断 | 研究路径 |
|--------|--------|----------|----------|
| [待研究] vLLM 在 27B/4×3090 下的实测吞吐/延迟 | sched_eff, kv_mgmt, batch_eff, kernel_eff, TTFT p99, TPOT p99, n_mem, n_slo | 核心排序依据 | vLLM 官方 benchmarks、社区压测报告、GitHub issues、自测脚本 |
| [待研究] TGI 在 27B/4×3090 下的实测吞吐/延迟 | 同上 | 核心排序依据 | TGI 官方文档、HuggingFace 基准、社区对比 |
| [待研究] 原生 transformers 在 27B/4×3090 下的实测吞吐/延迟 | 同上 | 基线对比 | HF 文档、社区实测 |
| [待研究] SGLang 在 27B/4×3090 下的实测吞吐/延迟 | 同上 | 备选对比 | SGLang 官方 benchmarks、论文数据 |

### F8 API Token 单价 `price_token` 相关（新增强制段）

| 空缺项 | 子问题 | 阻塞判断 | 研究路径 |
|--------|--------|----------|----------|
| [待研究] Groq 27B 等效模型定价 | 1) $/1M input tokens 2) $/1M output tokens 3) 是否支持 27B 规模 | API 成本分子 | **官方定价页 groq.com/pricing** 优先；第三方聚合源（OpenRouter, Artificial Analysis）为备用 |
| [待研究] Together.ai 27B 等效模型定价 | 同上 | API 成本分子 | **官方定价页 together.ai/pricing** 优先 |
| [待研究] Fireworks.ai 27B 等效模型定价 | 同上 | API 成本分子 | **官方定价页 fireworks.ai/pricing** 优先 |
| [待研究] 其他 API 服务商（OpenRouter 聚合、Anyscale、Replicate 等） | 同上 | 补充对比 | 聚合平台定价页 |

### F9 API 吞吐/SLA 保障 `api_slo` 相关

| 空缺项 | 子问题 | 阻塞判断 | 研究路径 |
|--------|--------|----------|----------|
| [待研究] 各 API 服务商的实际 TTFT/TPOT p99 | 独立实测或第三方基准（Artificial Analysis 等） | 判断是否满足 SLO | Artificial Analysis、社区实测、服务商 SLA 文档 |
| [待研究] 并发限制/速率限制 | max concurrent requests, rate limits | 判断并发 ≥ 8 可行性 | 服务商文档、开发者论坛 |

### F5/F6/F7 次级因素

| 空缺项 | 子问题 | 阻塞判断 | 研究路径 |
|--------|--------|----------|----------|
| [待研究] 各框架部署复杂度 setup（人时） | 从零到首个可用服务 | Tie-breaker | 官方快速开始、社区教程、GitHub issues |
| [待研究] 量化/投机解码/长上下文支持矩阵 | 功能完备度 | 特定场景门槛 | 官方文档、模型卡 |
| [待研究] 硬件兼容性（CUDA 版本、消费级卡支持） | 一票否决 | 可行域过滤 | 官方 CI 支持矩阵、GitHub issues |

---

## 候选集冻结（防漂移）

| 类别 | 候选 | 状态 | 备注 |
|------|------|------|------|
| 自托管框架 | vLLM | 待验证 | 主流选择，PagedAttention + continuous batching |
| 自托管框架 | TGI | 待验证 | HF 官方，Docker Compose 部署 |
| 自托管框架 | 原生 transformers | 待验证 | 基线，无调度开销 |
| 自托管框架 | SGLang | 待验证 | 备选，长上下文/前缀缓存优势 |
| API 服务商 | Groq | 待验证 | LPU 推理，极低延迟宣称 |
| API 服务商 | Together.ai | 待验证 | 多模型托管，有 27B 等效 |
| API 服务商 | Fireworks.ai | 待验证 | 类 Together，Fireworks 优化 |
| API 服务商 | OpenRouter (聚合) | 待验证 | 聚合定价参考 |
| API 服务商 | Anyscale (Ray) | 待验证 | Ray Serve + vLLM 托管 |

**排除理由记录**：若阶段 02 发现某候选不支持 27B 模型、或硬件不兼容、或无法满足 SLO，在阶段 02 显式记录"排除 — 理由 C"。

---

## 阶段 02 研究入口汇总

| 优先级 | 研究动作 | 目标来源 | 搜索关键词 | 备用来源 |
|--------|----------|----------|------------|----------|
| P0 | Groq/Together/Fireworks 官方定价页抓取 | groq.com/pricing, together.ai/pricing, fireworks.ai/pricing | "Groq pricing 27B", "Together.ai pricing Llama 27B", "Fireworks pricing" | OpenRouter 定价页、Artificial Analysis 价格对比表 |
| P0 | RTX 3090 云租赁价格 | RunPod, lambda.ai, vast.ai, AWS p4d/g5 | "RTX 3090 rental price per hour 2024", "RunPod 3090 pricing" | 闲鱼/淘宝二手购买价折算 |
| P0 | vLLM/TGI/SGLang 27B 4×3090 实测数据 | 官方 benchmarks、GitHub、社区博客 | "vLLM 27B 4x3090 benchmark", "TGI 27B throughput", "SGLang 27B performance" | 自测脚本（若环境允许） |
| P1 | API 服务商实际延迟/吞吐基准 | Artificial Analysis、独立评测 | "Artificial Analysis Groq latency", "Together.ai TPOT benchmark" | 社区实测帖子 |
| P1 | 部署复杂度/运维成本定性对比 | 官方文档、技术博客 | "vLLM deployment time", "TGI setup guide", "transformers generate production" | GitHub issues 统计 |

---

## 判定：分解完成

- ✅ 目标交付物明确：`loop-artifacts/stages/04/Q3-execution-log-r2.md`，含定价强制段合规的对比结论
- ✅ 主要因素覆盖完整（F1–F9），正交性检验通过
- ✅ 已知/可推导/空缺三分法清晰，无伪装事实
- ✅ 空缺条件逐项给出子问题、阻塞判断、研究路径
- ✅ 候选集冻结（9 个候选），防漂移机制就位
- ✅ 阶段 02 研究入口具体可执行（优先级、目标来源、搜索词、备用）

**阶段 01 产出完成，可进入阶段 02。**