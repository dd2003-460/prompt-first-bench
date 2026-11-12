# T40 / Q2 · 执行日志与完整定量分解树

**执行/证据观察日**：2026-11-06 UTC。**执行仓库/分支**：`dd2003-460/prompt-first-bench` / `arena/2d62d48c-prompt-first-bench`。任务书取自 `main@e7dc6ee` 的 `tasks/T40-gold-replication-arena.md`，在当前分支工作树恢复；原任务书误指不存在的 `experiments/stage-ablation/questions/Q2.txt`，本次按实际题面 [`Q2-model-selection.md`](../../../experiments/stage-ablation/questions/Q2-model-selection.md) 执行。先读 SOP + loop 00..04.5，再实际使用 `functions.web_search` 搜官方报告、第三方评估、报价、许可证、硬件；来源/观察时间及矛盾明细见 `../02/T40-evidence.md`、`../02.5/T40-cross-check.md`。**未使用仓库旧 gold 中的 benchmark 分数当作网页证据。**

**执行口径**：题面有六个原始候选，身份不成立者保留在树上并通过硬门槛阻断，绝不悄悄替换。`[GAP]` 是未测变量，**不是数字叶子或零值**；`[估计, conf 0.X]` 只用于明确的演算情景，不代表真实流量。本执行者不能取得独立 Reviewer 回执：本文件是可核验的条件化分析，**不声称流程已获独立审阅或生产选型已批准**。

## 一、根节点：可排序标量与公式

**目标**：`C_m = ¢/1k_acc`，对允许的候选模型 `m` 和服务路由 `r`，每 **1,000 个合格回答**的总成本（越小越好）；**合格**定义为在实际业务分布中，单次回答同时通过代码测试**且**满足指令约束。若任务只要一般指令而不需代码，则须先按实际 Python/JS/一般任务构成分别定义验收，再做加权；现有题面没有权重。[题面](../../../experiments/stage-ablation/questions/Q2-model-selection.md)

```text
准入 G(m,r) = G_身份 × G_许可证 × G_运行容量 × G_数据政策；0 = 不参与排序，未知 = 暂缓生产排序。
C_m,r [¢/1k_acc] = 100 [¢/$] × { (1,000 / q_m,r) × c_attempt(m,r,W) [$/尝试]
                                    + (1,000 / N_acc) × F_m,r [$] } ；q_m,r ∈ (0,1]，N_acc > 0。
q_m,r = P(代码测试通过 ∧ 指令达标 | 同一实际任务分布、部署版本/量化、prompt、解码模式)。
API：c_attempt = (i × p_in + o × p_out) / 1,000,000 + c_test + c_review + c_network。
自托管：c_attempt = (n_GPU × h_GPU + h_storage + h_ops) / H_effective
                 + c_test + c_review + c_network；H_effective = 每付费墙钟小时实际完成的尝试数。
```

`i,o` 为**实际计费**输入/输出 tokens（Qwen3 thinking 的思维 token 若计费须计入 `o`）；`p_in,p_out` 单位 USD/百万 token；`c_test,c_review,c_network` 是按每尝试摊的测试/人工/传输费；`F` 是该路由在研究期内的一次性接入/开发费用（不含已列入 `h_ops` 的按小时运维），`N_acc` 是同期真实合格数。自托管 `h_GPU` 可取租卡价**或**自有机器按研究期折旧/分摊后的每卡小时资本成本，不能把采购价同时计入 `F` 再计入折旧；`h_ops` 另纳电力、散热、CPU/RAM、维护，`h_storage` 纳磁盘/备份。若采用现金流口径一次性硬件采购计入 `F`，则对应 `h_GPU` 不再含该购置摊销；各种口径、寿命、利用率均待用户提供。API 与自托管是**互斥**服务分支，不能把两者加起来。单位换算 `100 ¢/$`、归一化 `1,000` 不是 benchmark。[题面](../../../experiments/stage-ablation/questions/Q2-model-selection.md) 此期望值需要足够稳定的业务/重试流程；失败后的追加尝试可能更长、更难、相关性更强，届时直接用每轮条件成本与条件成功率或实际总账本重估，不能生搬几何重试假设。

## 二、正交维度（四个一级维度，每个数值输入只归属一处）

| 一级节点 | 独占的原始变量/子层 | 如何进入根节点 / 不重计规则 |
|---|---|---|
| **W · 业务工作量** | 合格回答的归一化目标、实际 `i/o` 与 Python/JS/通用指令任务构成；情景 token 长度 | 决定 API 花费、KV/吞吐及 `q` 的任务加权；不是某候选“性能加分”。 |
| **Q · 单次联合合格率** | 代码测试/指令合格证据、相关性与基准→真实工作流迁移、模式/量化后表现 | 真正分母**只能是同题联合实测 `q`**；公开 HumanEval、LCB、SWE、IFEval 是不同口径的代理叶子，不能直接相乘或排序。 |
| **S · 单次服务可变成本** | API 指定 SKU 的输入/输出单价；**或**自托管每卡小时费与有效尝试数；额外审查/测试 | 经 W 决定每尝试美元金额。所有价格只作已声明路由的本轮挂牌情景，未公开近 7 天有效期者需复核。 |
| **E · 准入与固定投入** | 精确型号身份、权重许可、可运行性、共享 `params`、权重文件尺寸、`F/N_acc` | 不合规/不存在 ⇒ 一票否决；固定美元另摊，不把重量、参数或“生态”加到 API token 单价。 |

`params` 是**共享参数**：模型总参数量同时影响 Q（同族能力假说）、S（推理吞吐/成本）和 E（权重/显存），树中只在 E 一处记录，通过 `↗Q,S,E` 交叉引用而非在三个分支复制/相加。参数量不是通过率，也不足以预测性能；代码助手的模板、FIM 支持、工具链生态会改变迁移率、接入 `F` 和 `H_effective`，尚需在实际路由验证。此处“严格开源门槛”只**条件性**检查权重授权是否为 Apache/MIT 一类标准许可，不能据此声称整个模型/训练数据满足 OSI 的完整开放定义，也不是正式法律意见。深度按根→维度→子因素→数值叶子计 **3–4 边**；下树实际数得 **52 个具单位的数值叶子、77 个总节点**。每条 `Lxx` 的可点击来源和敏感性见紧随的叶子卡片；树不把不同 benchmark 当成可加项。

## 三、ASCII 定量树

```text
R  C(m,r) = ¢/1k_acc；min C，仅 G=1 且真实 q、费用可得时完整排序
├─ W 业务工作量〔候选无关〕
│  ├─ W1 归一化目标
│  │  └─ L01 = 1,000 次合格/标准批（题面）
│  └─ W2 单次计费形状〔仅情景，非内部日志〕
│     ├─ L02 = 2,000 token 输入/尝试 [估计, conf 0.2]
│     └─ L03 = 500 token 输出/尝试 [估计, conf 0.2]
├─ Q 真正的联合 q=[GAP]；下列是互斥协议的质量证据，不可相乘
│  ├─ Q1 代码能力（版本/评测集隔离）
│  │  ├─ Q1a 厂商 benchmark：
│  │  │  ├─ L04 = 65.7% Qwen3 thinking LCB v5
│  │  │  ├─ L05 = 31.3% Qwen3 non-thinking LCB v5
│  │  │  ├─ L06 = 92.7% Qwen2.5-Coder-Instruct HumanEval Python
│  │  │  ├─ L07 = 85.7% Qwen2.5-Coder-Instruct MultiPL-E JS
│  │  │  ├─ L08 = 84.8% Mistral-2501 HumanEval instruct
│  │  │  ├─ L09 = 85.4% Llama 3.3 HumanEval（Mistral 同 pipeline）
│  │  │  └─ L10 = 33.8% GLM SWE-Verified（Moatless agent，非补全）
│  │  └─ Q1b 独立动态 Code2Bench-2505（同队列、另任务）
│  │     ├─ L17 = 35.2% Qwen3 Python
│  │     ├─ L18 = 28.0% Qwen3 JS
│  │     ├─ L19 = 36.2% Qwen2.5-Coder-Instruct Python
│  │     └─ L20 = 34.2% Qwen2.5-Coder-Instruct JS
│  ├─ Q2 指令跟随代理（严格看来源/harness）
│  │  ├─ L11 = 85.0% Qwen3 thinking IFEval strict-prompt
│  │  ├─ L12 = 83.2% Qwen3 non-thinking IFEval strict-prompt
│  │  ├─ L13 = 79.9% Qwen2.5-Coder-Instruct IFEval
│  │  ├─ L14 = 82.9% Mistral-2501 IFEval
│  │  ├─ L15 = 87.6% GLM-4-32B-0414 IFEval
│  │  └─ L16 = 88.35% Llama 3.3 IFEval（Mistral 同 pipeline）
│  └─ Q3 联合失败相关/benchmark→实际 Python+JS 迁移/量化差=[GAP]
├─ S 服务成本：S1 API 或 S2 本地，二选一，不相加
│  ├─ S1 API 输入价与输出价（USD/百万实际计费 token）
│  │  ├─ Mistral-2501 路由
│  │  │  ├─ L21 = $0.05/M 输入
│  │  │  └─ L22 = $0.08/M 输出
│  │  ├─ Z.AI GLM-4-32B-0414-128K
│  │  │  ├─ L23 = $0.10/M 输入
│  │  │  └─ L24 = $0.10/M 输出
│  │  ├─ Qwen3-32B 路由
│  │  │  ├─ L25 = $0.08/M 输入
│  │  │  └─ L26 = $0.28/M 输出
│  │  ├─ Llama-3.3-70B-Instruct 路由（严格许可时不准入）
│  │  │  ├─ L27 = $0.10/M 输入
│  │  │  └─ L28 = $0.32/M 输出
│  │  └─ Qwen2.5-Coder-32B-Instruct 路由
│  │     ├─ L29 = $0.66/M 输入
│  │     └─ L30 = $1.00/M 输出
│  └─ S2 自托管卡价：互斥租卡 SKU，非额外 API 费；有效吞吐=[GAP]
│     ├─ L31 = $0.89/GPU·h Secure 4090
│     └─ L32 = $0.34/GPU·h Community 4090
└─ E 准入门槛 × 共享规格 + 固定投入 F/N_acc=[GAP]
   ├─ E1 题面资源上限及示例 4090 规格
   │  ├─ L33 = 2 GPU/单台（题面上限）
   │  └─ L34 = 24 GB/GPU（4090 示例）
   ├─ E2 Q4_K_M 原权重文件体积（不是峰值显存）
   │  ├─ L35 = 19.8 GB Qwen3
   │  ├─ L36 = 19.9 GB Qwen2.5-Coder-Instruct
   │  ├─ L37 = 14.3 GB Mistral-2501
   │  ├─ L38 = 19.7 GB GLM-0414
   │  └─ L39 = 42.5 GB Llama-3.3-70B
   ├─ E3 精确型号身份：不得把同族原代、Lite、Base 混成题面候选
   │  ├─ L40 = 0 布尔：DeepSeek-Coder-V2-33B 官方身份不成立
   │  ├─ L41 = 16B 参数：实际 V2-Lite（非替代候选）
   │  └─ L42 = 236B 参数：实际 V2（非替代候选）
   ├─ E4 SHARED 总参数（只存一份，↗Q 质量/↗S 吞吐/↗E 显存）
   │  ├─ L43 = 32B 参数 Qwen3-32B（名义规模）
   │  ├─ L44 = 32.5B 参数 Qwen2.5-Coder-Instruct
   │  ├─ L45 = 24B 参数 Mistral-2501
   │  ├─ L46 = 32B 参数 GLM-0414（名义规模）
   │  └─ L47 = 70B 参数 Llama-3.3（名义规模）
   ├─ E5 许可证门槛：若用户“开源”=Apache/MIT 类严格许可
   │  ├─ L48 = 1 布尔 Qwen3 Apache-2.0
   │  ├─ L49 = 1 布尔 Qwen2.5-Coder-Instruct Apache-2.0
   │  ├─ L50 = 1 布尔 Mistral-2501 Apache-2.0
   │  ├─ L51 = 1 布尔 GLM 权重 MIT
   │  └─ L52 = 0 布尔 Llama 3.3 自定义 Community License（非 OSI）
   └─ E6 FIM/模板/推理引擎适配、数据政策与接入 F=[GAP；待实测，非数值叶]
```

## 四、叶子卡片（52/52：每叶数值＋单位＋来源＋敏感性）

**卡片读法**：来源是可点击原始 URL/题面路径；公开分数只支持“代理证据”，不许把表中 `p` 直接作为 `q_m`。`高/中/门槛` 是对根标量的敏感性及使用限制，不是额外分数。源的**观察时间均为 2026-11-06 UTC**；页面发行/更新年月及报价时效见阶段 02。

| ID | 数值 / 严格定义 | 来源 | 对根的敏感性、证据局限 |
|---|---|---|---|
| L01 | **1,000 次合格/标准批** | [题面](../../../experiments/stage-ablation/questions/Q2-model-selection.md) | 归一化常数；改批量使 C 线性变但不改变相对顺序。 |
| L02 | **2,000 token 输入/尝试 [估计, conf 0.2]** | 题面无流量计数；仅借公开示范 [1](https://llmprice.com/models/openrouter-qwen-qwen3-32b/) 的 `2,000 input + 500 output` 作**演算情景**，非模型性能事实。 | 高：API 输入钱正比 `i`；实际仓库上下文更长则需重算。 |
| L03 | **500 token 实际计费输出/尝试 [估计, conf 0.2]** | 仅作演算示范 [1](https://llmprice.com/models/openrouter-qwen-qwen3-32b/)；非 Qwen3 thinking 实测输出量。 | 高：API 输出钱正比 `o`；思维 token/补全长度改变排序。 |
| L04 | **65.7% Qwen3-32B thinking，LiveCodeBench v5** | 官方 PDF Table 13 第 16 页 [1](https://arxiv.org/pdf/2505.09388)；本次从 GitHub 官方 PDF 逐列提取。 | 高质量代理，不是 Python/JS FIM 联合率；思维模式额外计费待测。 |
| L05 | **31.3% Qwen3-32B non-thinking，LiveCodeBench v5** | 同报告 Table 14 第 16 页 [1](https://arxiv.org/pdf/2505.09388)。 | 高：与 L04 同测试集差 34.4pp；**不能**用 thinking 分数搭配 non-thinking token。 |
| L06 | **92.7% Qwen2.5-Coder-32B-Instruct，HumanEval Python pass@1** | 官方报告 **v3** 的 32B-Instruct 行 [1](https://arxiv.org/html/2409.12186v3)。 | 高但强协议敏感；独立 BigCode 83.2%，函数生成不等于内部补全。 |
| L07 | **85.7% Qwen2.5-Coder-32B-Instruct，MultiPL-E JavaScript pass@1** | 官方 v3 表格 JS 列 [1](https://arxiv.org/html/2409.12186v3)。 | 高：直接覆盖 JS，但第三方为 76.05%；不能拿 Base FIM 分替代。 |
| L08 | **84.8% Mistral-Small-24B-Instruct-2501，HumanEval instruct pass@1** | 官方卡同一内部 pipeline [1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)。 | 高：仅 Python 风格代码代理；与 L09 **同 pipeline** 可比，不代表 JS。 |
| L09 | **85.4% Llama-3.3-70B，同 pipeline HumanEval instruct pass@1** | Mistral 官方对照表（**非 Meta 的 88.4**）[1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)。 | 高：能和 L08 同协议比较；许可严格门槛=0。 |
| L10 | **33.8% GLM-4-32B-0414，SWE-bench Verified + Moatless** | Z.AI 官方工程评测表 [1](https://github.com/zai-org/GLM-4)。 | 高证据缺口：agent 修 repo issue，不能作函数级 Python/JS pass@1。 |
| L11 | **85.0% Qwen3 thinking IFEval strict-prompt** | 官方 PDF Table 13 [1](https://arxiv.org/pdf/2505.09388)。 | 高但同题联合率/思维成本未测。 |
| L12 | **83.2% Qwen3 non-thinking IFEval strict-prompt** | 官方 PDF Table 14 [1](https://arxiv.org/pdf/2505.09388)。 | 高：独立非思维 strict-prompt 86.1%，协议仍不同。 |
| L13 | **79.9% Qwen2.5-Coder-Instruct IFEval** | 官方 v3 模型表 [1](https://arxiv.org/html/2409.12186v3)。 | 高：第三方 OpenLLM v2 可低至 72.7%；不和 L06 相乘。 |
| L14 | **82.9% Mistral 2501 IFEval（厂商 pipeline）** | 官方模型卡 [1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)。 | 高：Red Hat 原模型 73.27%（口径不同）；不和 L08 相乘。 |
| L15 | **87.6% GLM-4-32B-0414 IFEval** | 官方 GLM 模型卡 [1](https://huggingface.co/zai-org/GLM-4-32B-0414)。 | 高、独立同协议核验缺失；不可与别家 IFEval 直接排序。 |
| L16 | **88.35% Llama 3.3 IFEval（Mistral 同 pipeline）** | Mistral 官方对照表 [1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)。 | 高：仅与 L14 同流程比较；Meta 自测为 92.1%。 |
| L17 | **35.2% Qwen3-32B，Code2Bench Python** | 第三方动态代码评测 [1](https://arxiv.org/html/2508.07180v1)。 | 高迁移警示：与官方 LCB 不同任务，Qwen3 模式尚未核对。 |
| L18 | **28.0% Qwen3-32B，Code2Bench JS** | 同一第三方表 [1](https://arxiv.org/html/2508.07180v1)。 | 高：同队列低于 Qwen2.5-Coder JS 的 34.2%，但不等于内部补全。 |
| L19 | **36.2% Qwen2.5-Coder-Instruct，Code2Bench Python** | 同一第三方表 [1](https://arxiv.org/html/2508.07180v1)。 | 高：仅能在该评测队列里与 L17 对照；不混厂商 HE。 |
| L20 | **34.2% Qwen2.5-Coder-Instruct，Code2Bench JS** | 同一第三方表 [1](https://arxiv.org/html/2508.07180v1)。 | 高：相对 L18 +6.2pp，不是实际业务 `q` 的差。 |
| L21 | **$0.05/百万输入 token，OpenRouter Mistral 2501** | 精确型号挂牌 [1](https://openrouter.ai/mistralai/mistral-small-24b-instruct-2501)；DeepInfra 同价 [5](https://deepinfra.com/mistral)。 | 高：`∂C/∂p_in=0.1i/q` 美分/每千合格每加 $1/M；情景下 `200/q`。 |
| L22 | **$0.08/百万输出 token，OpenRouter Mistral 2501** | 同上 [1](https://openrouter.ai/mistralai/mistral-small-24b-instruct-2501) [5](https://deepinfra.com/mistral)。 | 高：`∂C/∂p_out=0.1o/q`；情景下 `50/q`；要复核实际结算。 |
| L23 | **$0.10/百万输入 token，Z.AI GLM-4-32B-0414-128K** | 精确 SKU 官方价 [1](https://docs.z.ai/guides/overview/pricing)。 | 高：仅对 `0414-128K` 直接 API；OpenRouter 泛 GLM API ID 未证同版。 |
| L24 | **$0.10/百万输出 token，Z.AI GLM-4-32B-0414-128K** | 同官方价表 [1](https://docs.z.ai/guides/overview/pricing)。 | 高：真实输出量和价格生效日待复核。 |
| L25 | **$0.08/百万输入 token，OpenRouter Qwen3-32B** | 精确路由 [1](https://openrouter.ai/qwen/qwen3-32b)；DeepInfra [2](https://deepinfra.com/pricing?amp=&amp=)。 | 高：两页可能同一后端；不是两次独立计费实测。 |
| L26 | **$0.28/百万输出 token，OpenRouter Qwen3-32B** | 本轮供应商报价 [1](https://openrouter.ai/qwen/qwen3-32b) [2](https://deepinfra.com/pricing?amp=&amp=)。 | **极高**：另第三方仍列 $0.24/M；thinking 输出量会放大此项，实际支付重核。 |
| L27 | **$0.10/百万输入 token，OpenRouter Llama 3.3 70B** | 挂牌 [1](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct)；DeepInfra [1](https://deepinfra.com/llama)。 | 高但严格 OSI 不准入；若放宽许可须单独审查。 |
| L28 | **$0.32/百万输出 token，OpenRouter Llama 3.3 70B** | 同供应商页面 [1](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct) [1](https://deepinfra.com/llama)。 | 高：API 路由可能与 DeepInfra 同后端。 |
| L29 | **$0.66/百万输入 token，OpenRouter Qwen2.5-Coder-32B-Instruct** | 挂牌 [1](https://openrouter.ai/qwen/qwen-2.5-coder-32b-instruct)；Cloudflare 文档 [1](https://developers.cloudflare.com/workers-ai/models/qwen2.5-coder-32b-instruct/)。 | 高：情景下输入成本占主导；该 SKU 贵不否认其代码优势。 |
| L30 | **$1.00/百万输出 token，OpenRouter Qwen2.5-Coder-32B-Instruct** | 同 [1](https://openrouter.ai/qwen/qwen-2.5-coder-32b-instruct) [1](https://developers.cloudflare.com/workers-ai/models/qwen2.5-coder-32b-instruct/)。 | 高：不同供应商/企业折扣可能改变，不能外推全市场。 |
| L31 | **$0.89/GPU·小时，Runpod Secure Cloud RTX 4090** | 供应商产品价 [1](https://www.runpod.io/gpu-models/rtx-4090)；总价页 [1](https://www.runpod.io/pricing)。 | 高：双卡每小时 $1.78，需吞吐/利用率；不是显卡买断价。 |
| L32 | **$0.34/GPU·小时，Runpod Community Cloud RTX 4090** | 同一供应商两页 [1](https://www.runpod.io/gpu-models/rtx-4090) [1](https://www.runpod.io/pricing)。 | 高、与 Secure 互斥；可用性、安全/SLA/地域不一定等价。 |
| L33 | **2 GPU/单台，预算上限（题面）** | [题面](../../../experiments/stage-ablation/questions/Q2-model-selection.md)。 | 门槛：是硬件上限非“必需占用 2 卡”，单卡方案亦可；两卡不共享 VRAM。 |
| L34 | **24 GB/卡，RTX 4090 示例** | NVIDIA 规格 [1](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)；Runpod 产品页 [1](https://www.runpod.io/gpu-models/rtx-4090)。 | 门槛：只做静态文件与单卡容量的必要比较；题面不指定必须买 4090。 |
| L35 | **19.8 GB，Qwen3-32B Q4_K_M GGUF 文件** | Qwen 官方上传 [3](https://huggingface.co/Qwen/Qwen3-32B-GGUF/blob/main/Qwen3-32B-Q4_K_M.gguf)。 | 高：<24 GB 仅静态必要条件，不保证 128K KV/峰值/吞吐。 |
| L36 | **19.9 GB，Qwen2.5-Coder-Instruct Q4_K_M 文件** | bartowski GGUF 具体文件 [1](https://huggingface.co/bartowski/Qwen2.5-Coder-32B-Instruct-GGUF/blob/main/Qwen2.5-Coder-32B-Instruct-Q4_K_M.gguf)。 | 高：第三方量化，不等于厂商 BF16 benchmark 或部署可用。 |
| L37 | **14.3 GB，Mistral 2501 Q4_K_M 文件** | LM Studio community 具体文件 [3](https://huggingface.co/lmstudio-community/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q4_K_M.gguf)。 | 高：权重空间较宽裕，仅可推出静态必要条件。 |
| L38 | **19.7 GB，GLM-4-32B-0414 Q4_K_M 文件** | Unsloth 具体清单 [2](https://huggingface.co/unsloth/GLM-4-32B-0414-GGUF/tree/main)。 | 高：不同制品/GB vs GiB 可能不同；不能推断真实 VRAM。 |
| L39 | **42.5 GB，Llama-3.3-70B Q4_K_M 文件** | second-state 文件指针 [1](https://huggingface.co/second-state/Llama-3.3-70B-Instruct-GGUF/blob/abac21c4be7dca642bd7de0221aeb2149eba5c8f/Llama-3.3-70B-Instruct-Q4_K_M.gguf)。 | **门槛**：单张 24 GB 不可能完全容纳权重；双卡并行+缓存能否运行未证。 |
| L40 | **0 布尔，原字符串 `DeepSeek-Coder-V2-33B` 身份无效** | 官方 V2 模型列表、原代 33B 行 [1](https://github.com/deepseek-ai/deepSeek-Coder-V2)；V2 论文 [4](https://arxiv.org/pdf/2406.11931)。 | 一票否决：不能为不存在的 checkpoint 编 33B V2 质量、API 价格或许可。 |
| L41 | **16B 参数，实际 DeepSeek-Coder-V2-Lite（非原候选）** | 同 [1](https://github.com/deepseek-ai/deepSeek-Coder-V2) [4](https://arxiv.org/pdf/2406.11931)。 | 门槛线索：不得偷换 Lite 为题面 33B。 |
| L42 | **236B 参数，实际 DeepSeek-Coder-V2 完整版（非原候选）** | 同 [1](https://github.com/deepseek-ai/deepSeek-Coder-V2) [4](https://arxiv.org/pdf/2406.11931)。 | 门槛：理想纯 4-bit 权重下界 `236B×4/8=118 GB`，已 >2×24 GB；激活 21B 不等于仅存 21B 权重。 |
| L43 | **32B 参数，Qwen3-32B 名义总规模** | 官方技术报告规格表 [1](https://arxiv.org/pdf/2505.09388)。 | 共享 `params`，影响能力/吞吐/容量三路，不当作成功率。 |
| L44 | **32.5B 参数，Qwen2.5-Coder-32B-Instruct 总量** | 官方模型卡 [2](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct/blob/main/README.md)。 | 共享 `params`，不等于 32.5B 激活成本之外的“质量加分”。 |
| L45 | **24B 参数，Mistral Small 2501 名义规模** | 官方模型卡 [1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)。 | 共享；无法仅据规模推断吞吐。 |
| L46 | **32B 参数，GLM-4-32B-0414 名义规模** | 官方模型卡 [1](https://huggingface.co/zai-org/GLM-4-32B-0414)。 | 共享；真实重量/性能仍按对应实现测。 |
| L47 | **70B 参数，Llama 3.3 名义规模** | Meta 官方模型卡 [1](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)。 | 共享；强烈影响本地容量，但不证明质量优势。 |
| L48 | **1 布尔，Qwen3 许可证满足严格 Apache/MIT 过滤** | Qwen3 官方 LICENSE 为 Apache-2.0 [1](https://huggingface.co/Qwen/Qwen3-32B/blob/main/LICENSE)。 | 一票否决门槛；此处 1 是**许可分类**，不是商用合同/数据合规批准。 |
| L49 | **1 布尔，Qwen2.5-Coder-Instruct 严格许可过滤** | 官方模型卡 `license: apache-2.0` [2](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct/blob/main/README.md)。 | 同上；第三方量化模型附加条件需另核。 |
| L50 | **1 布尔，Mistral 2501 严格许可过滤** | 官方模型卡 Apache-2.0 [1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)。 | 同上；API 服务协议另计。 |
| L51 | **1 布尔，GLM-4-32B-0414 权重严格许可过滤** | 官方权重卡 `license: mit` [1](https://huggingface.co/zai-org/GLM-4-32B-0414/blob/main/README.md)。 | 一票否决门槛；代码仓库 Apache-2.0 是另一授权对象，并非权重矛盾。 |
| L52 | **0 布尔，Llama 3.3 不满足严格 Apache/MIT/OSI 过滤** | Meta 官方自定义 Community License [1](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)。 | **条件性一票否决**：若用户允许开放权重并批准条款，可进入 API 备选；不是“禁止一切商用”。 |

## 五、计算与敏感性（**情景**，不是实测总成本）

### A. 5 个精确挂牌路由；仅模型 API token 费用

假设 **相同的** `i=2,000` 输入、`o=500` **实际计费**输出 token/尝试，两数均 **[估计, conf 0.2]**，只借公开计算器的演算例子 [1](https://llmprice.com/models/openrouter-qwen-qwen3-32b/) 做可复核比较；不表示内部请求长度。固定费 `F`、测试/审查/网络、税、吞吐与失败后不同长度**一概未计**（未计≠实际为 0）；`q_m` 不拿 benchmark 代填。输入/输出价格源见 L21–L30。公式例：Mistral `(2,000×$0.05 + 500×$0.08)/1,000,000=$0.00014/尝试`；`100×1,000×$0.00014/q = 14/q ¢/1k_acc`。

| 原候选、路线 | 输入 / 输出挂牌价 ($/百万) | token 费 ($/尝试) | 仅 API token 费 `C_API(q)` (¢/1k_acc) | 若**假设**所有可准入模型 `q=0.50`：¢/1k_acc；条件顺序 |
|---|---:|---:|---:|---:|
| Mistral-Small-24B-Instruct-2501 / OpenRouter [1](https://openrouter.ai/mistralai/mistral-small-24b-instruct-2501) | 0.05 / 0.08 | **0.00014** | **14/q_M** | **28；1** |
| GLM-4-32B-0414 / **Z.AI 0414-128K** [1](https://docs.z.ai/guides/overview/pricing) | 0.10 / 0.10 | **0.00025** | **25/q_G** | **50；2** |
| Qwen3-32B / OpenRouter [1](https://openrouter.ai/qwen/qwen3-32b) | 0.08 / 0.28 | **0.00030** | **30/q_Q3** | **60；3**（只在假设 500 token 已含 thinking 输出时） |
| Llama-3.3-70B-Instruct / OpenRouter [1](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct) | 0.10 / 0.32 | **0.00036** | **36/q_L** | **72；严格许可门槛不准入**；放宽开放权重时临时次序 4 |
| Qwen2.5-Coder-32B-Instruct / OpenRouter [1](https://openrouter.ai/qwen/qwen-2.5-coder-32b-instruct) | 0.66 / 1.00 | **0.00182** | **182/q_Q2** | **364；严格许可准入的次序 4** |
| `DeepSeek-Coder-V2-33B` [1](https://github.com/deepseek-ai/deepSeek-Coder-V2) | **[GAP] 无该型号** | **不定义** | **身份门槛=0，+∞/不参与** | **不排名** |

**`q=0.50` 是纯敏感性假设 [估计, conf 0.1]，不是某模型通过率。**若真正质量不同则不能按上表最后一列排名。令 `c_j` 为 challenger 每尝试 API token 费，`c_M=$0.00014`；在完全相同的 token 工作量、无固定/附加费、可用同样路由的条件下，`j` 比 Mistral 更省的充要条件是 `q_j/q_M > c_j/c_M`；仅由 `q_j≤1` 可得 **Mistral 必比 j 便宜的充分条件** `q_M > c_M/c_j`（等号可能同价）。

| j 与 Mistral 比 | 挑战者所需 `q_j / q_M` **大于** | 若 `q_M` **大于**该值，则该 j 即使 q=1 也无法更便宜 | 含义 |
|---|---:|---:|---|
| GLM 精确 Z.AI SKU [1](https://docs.z.ai/guides/overview/pricing) | 1.785714 | **0.560000** | 最大的非 Mistral 竞争威胁阈值；GLM 代码/联合率未测。 |
| Qwen3 [1](https://openrouter.ai/qwen/qwen3-32b) | 2.142857 | **0.466667** | thinking 的真实输出若 >500 token，挑战门槛还会更高。 |
| Llama（仅放宽许可）[1](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct) | 2.571429 | **0.388889** | 严格许可时本来不参与。 |
| Qwen2.5-Coder [1](https://openrouter.ai/qwen/qwen-2.5-coder-32b-instruct) | 13.000000 | **0.076923** | 在**该特定 API 挂牌价**和 token 形状下；自托管/其他供应方另算。 |

**反例**：若内部实测 `q_M=0.40`、`q_G=0.80`（均 **[估计, conf 0.1] 的反事实举例**），则 `14/0.40=35¢` vs `25/0.80=31.25¢`，GLM 反超；因此不能把“原始单价最低”冒充真实总成本最优。若 `q_M>0.56`，在上述**仅 API token 费用**的前提下，它对其余四个可辨型号均有无需知道对方 q 的充分条件优势；**并不**推断真实 `q_M>0.56`。若 Qwen3 输出报价用另一网页的 $0.24/M [2](https://www.llmreference.com/provider/openrouter/qwen3-32b) 而不是本轮供应商 $0.28/M [1](https://openrouter.ai/qwen/qwen3-32b)，则情景 `c=$0.00028`、`C_API=28/q_Q3 ¢`，仍须核对真实账单；不是擅自择便宜来源。

### B. 自托管可行性只到**必要条件**，不伪造有效吞吐

若以 Runpod Secure 4090 **$0.89/GPU·h** [1](https://www.runpod.io/gpu-models/rtx-4090) 为**示例租卡价**，且**同一模型**自托管质量恰等于 API、无任何自托管固定/存储/运维成本且拥有完全相同请求形状（实际通常不成立）**[估计, conf 0.1]**，单卡自托管仅 GPU 钱低于同模型 API 钱的**必要**吞吐门槛 `H_effective > 0.89/c_API`：Mistral **6,357.14** 尝试/h；Qwen3 **2,966.67**；GLM **3,560.00**；Qwen2.5-Coder **489.01**。Llama 42.5GB 权重**不能装在单张 24GB 卡** [1](https://huggingface.co/second-state/Llama-3.3-70B-Instruct-GGUF/blob/abac21c4be7dca642bd7de0221aeb2149eba5c8f/Llama-3.3-70B-Instruct-Q4_K_M.gguf) [1](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)；**若**双卡 4090 真正能通过模型并行运行，其 **$1.78/h** 示例下门槛 `1.78/0.00036=4,944.44` 尝试/h。GPU 指标是每付费小时完成的**尝试**数，不是生成 tokens/s、并发用户数或合格回答数；租卡价变更、闲置、量化后 q 变化都使阈值重算。

静态文件由 L35–L39 验证：Mistral 14.3、GLM 19.7、Qwen3 19.8、Qwen2.5 19.9 GB **<24 GB 文件大小基线**，并**不证明**单卡能承载所需上下文；Llama 42.5 GB **>单卡 24 GB**。两张 4090 **无 NVLink、不是统一 48 GB 池** [1](https://www.runpod.io/gpu-models/rtx-4090)；是否可跨卡加载 Llama 及运行峰值，须实际试验。官方 V2 完整版 **236B 参数** [1](https://github.com/deepseek-ai/deepSeek-Coder-V2) 的*理想全权重 4-bit* 下界 `236×4/8=118 GB`（尚未加元数据/KV），**大于**双卡 2×24GB 总名义容量；其实际版本不是原题的 33B。没有本地 `H_effective`、`q_local`、缓存容量和折旧 `F`，就**没有**可信的本地 `¢/1k_acc` 排名。

## 六、双源交叉验证与冲突（高影响值不择高、也不伪造“复现”）

| 关键数字/门槛 | 来源一 | 来源二 / 实际观察 | 判定及排序影响 |
|---|---|---|---|
| Qwen2.5-Coder 代码 | 官方 v3 Python/JS **92.7/85.7%** [1](https://arxiv.org/html/2409.12186v3) | BigCode 同名提交 **83.2/76.05%** [1](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard/discussions/87) | Python −9.5pp、JS −9.65pp；harness 不同，不把高值当 q；报告 v1 不适用 32B。 |
| Qwen3 thinking 质量/模式 | 官方 PDF Table 13/14 同一 LCB v5 **65.7/31.3%** [1](https://arxiv.org/pdf/2505.09388) | 独立 Code2Bench Qwen3 Python/JS **35.2/28.0%** [1](https://arxiv.org/html/2508.07180v1) | 另任务非 LCB 复测；也不知道独立表所用思维模式，说明任务迁移不可忽略。 |
| Qwen3 IFEval | 官报 non-thinking **83.2%** [1](https://arxiv.org/pdf/2505.09388) | 独立严格 prompt **86.1%** [3](https://arxiv.org/pdf/2608.23830) | 模式接近但采样/温度等设置不同，不能用两数拟合真实联合 q。 |
| Mistral IFEval | 官方卡 **82.9%** [1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) | Red Hat 原模型 OpenLLM v2 **73.27%** [3](https://huggingface.co/RedHatAI/Mistral-Small-24B-Instruct-2501-FP8-dynamic) | −9.63pp；不能强行解释成量化影响（73.27 是未量化原版）。 |
| Llama HumanEval/IFEval | Meta **88.4/92.1%** [1](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | Mistral 同流程 **85.4/88.35%** [1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)；Red Hat 原模型 **83.20/90.89%** [4](https://huggingface.co/RedHatAI/Llama-3.3-70B-Instruct-quantized.w8a8) | 三套 harness 不同；L09/L16 仅用**Mistral 同流程**与 Mistral 比；严格许可证仍 0。 |
| GLM 代码/指令 | 官方 **33.8% SWE+Moatless / 87.6% IFEval** [1](https://github.com/zai-org/GLM-4) | 同厂但改 Agentless **30.7%** / OpenHands **27.2%** [1](https://huggingface.co/zai-org/GLM-4-32B-0414)；**独立同协议来源 [GAP]** | 不把多 agent 分数当独立代码补全；真实 q 未知。 |
| Mistral 精确 API 价 | OpenRouter **$0.05/$0.08** [1](https://openrouter.ai/mistralai/mistral-small-24b-instruct-2501) | DeepInfra 同名 2501 **$0.05/$0.08** [5](https://deepinfra.com/mistral) | 两供应端公开价相同，可能同一后端；真实结算及更新日待确认。 |
| Qwen3 精确 API 价 | OpenRouter **$0.08/$0.28** [1](https://openrouter.ai/qwen/qwen3-32b) | DeepInfra 同价 [2](https://deepinfra.com/pricing?amp=&amp=)，第三方旧页 **$0.08/$0.24** [2](https://www.llmreference.com/provider/openrouter/qwen3-32b) | 按本轮供应商价 $0.28 算，冲突保留，不能称两家独立签单。 |
| Qwen2.5-Coder 精确价 | OpenRouter **$0.66/$1.00** [1](https://openrouter.ai/qwen/qwen-2.5-coder-32b-instruct) | Cloudflare SKU 同价 [1](https://developers.cloudflare.com/workers-ai/models/qwen2.5-coder-32b-instruct/) | 同价，但 OpenRouter 可能代理 Cloudflare；仅挂盘价。 |
| GLM / Llama 精确价 | Z.AI **0414-128K $0.10/$0.10** [1](https://docs.z.ai/guides/overview/pricing)；OpenRouter Llama **$0.10/$0.32** [1](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct) | OpenRouter GLM 页面显示 API ID `z-ai/glm-4-32b` 同价 [3](https://openrouter.ai/z-ai/glm-4-32b-0414)；DeepInfra Llama 同价 [1](https://deepinfra.com/llama) | **GLM SKU 对齐 [GAP]**（故只用 Z.AI 精确 SKU）；Llama 两页可能同后端。 |
| 硬件与量化 | NVIDIA **24 GB/4090** [1](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/) | Runpod **24 GB/4090、无 NVLink** [1](https://www.runpod.io/gpu-models/rtx-4090)；Llama 文件 **42.5 GB** [1](https://huggingface.co/second-state/Llama-3.3-70B-Instruct-GGUF/blob/abac21c4be7dca642bd7de0221aeb2149eba5c8f/Llama-3.3-70B-Instruct-Q4_K_M.gguf) | 单卡 Llama 静态必不合；多卡上下文、并行和真实吞吐 [GAP]。 |
| DeepSeek 候选准确性 | V2 官方只有 **16B Lite /236B full**，旧 33B 为原代 [1](https://github.com/deepseek-ai/deepSeek-Coder-V2) | V2 论文再次列 **16B/236B** [4](https://arxiv.org/pdf/2406.11931) | `V2-33B` 身份=0；禁止混合 V1 性能与 V2 成本。 |
| 许可证一票否决 | 官方 Qwen3 Apache [1](https://huggingface.co/Qwen/Qwen3-32B/blob/main/LICENSE)、GLM 权重 MIT [1](https://huggingface.co/zai-org/GLM-4-32B-0414/blob/main/README.md) | Meta 官方自定义 Llama 3.3 协议 [1](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)、Qwen2.5 Apache [2](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct/blob/main/README.md)、Mistral Apache [1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) | 若“开源”是严格 Apache/MIT，Llama=0；若开放权重够用，需法务批准且重新考虑服务路线。 |

**反方复核已经实际进行**，不是给自己 `pass`：官方与社区评分差异、思维模式 token 漏算、OpenRouter GLM SKU 错映射、文件大小不等于运行显存、低单价不等于低合格成本，均在阶段 02.5 逐项反证。高影响模型质量和近期正式价格仍无同协议/独立成交双源，不能据此给“真实 q/TCO 已验证”的结论。

## 七、缺口清单（哪些值阻断无条件最优、怎样补）

1. **[GAP，决定排序]** 内部真实 `q_m = P(Python/JS 函数补全测试通过 ∧ 指令达标)`、各任务/语言比例、失败相关、重复生成策略。**动作**：获授权后建匿名、含隐藏单测的同队列盲测，给所有可准入型号相同提示/温度/版本/模式及置信区间；未测前禁用公开 benchmark 乘积。
2. **[GAP，高]** 内部 `i/o` 分布、超长上下文与 Qwen3 thinking 的**全部计费输出**。**动作**：获得脱敏日志或跑匿名样本后按路由收集 API 实际计费字段；目前 2,000/500 是 [估计, conf 0.2]。
3. **[GAP，高]** 测试运行、人工复查/修复、隐私/网络/数据驻留成本 `c_test,c_review,c_network` 与固定 `F`、总量 `N_acc`；自购硬件的购置/折旧、电力散热、CPU/RAM/备份、维修与使用年限。**动作**：财务/工程提供同一核算期成本并避免采购价与折旧双计；此文件不能称全量 TCO 价格。
4. **[GAP，高]** W4 / Q4_K_M 的质量损失、单卡/双卡最大 KV 与长上下文峰值、吞吐/闲置、服务时延 SLA、量化推理引擎与 FIM/chat 模板及 IDE 工具链适配。**动作**：同硬件、提示格式和上下文真实加载及压测；不得由 19.xGB 文件断言能跑 128K；生态集成的时间与钱记入适当的 `F` 或小时/尝试费用，本地成本未排名。
5. **[GAP，硬门槛]** “开源”是否仅限 OSI 类许可证还是接受带条款开放权重、Llama 许可证及数据政策审查。**动作**：用户/法务确认；严格解释先剔除 Llama，API 使用也须审服务协议。
6. **[GAP，候选身份]** 原题的 `DeepSeek-Coder-V2-33B` 在官方发布中不存在。**动作**：向用户确认是否要将未来任务的候选改为 V2-Lite 16B 或原代 Coder 33B；**本轮不得替代**。
7. **[GAP，报价时效/映射]** GLM OpenRouter 页面 ID 与 Z.AI 精确 `0414-128K` 未证明同权重；各报价页缺可核近 7 日生效日期、具体地域/费用。**动作**：生产采购前校验精确 API ID、计费账单/供应商协议与缓存政策；本轮价格仅搜索日挂牌情景。
8. **[GAP，评测交叉验证]** GLM 的 Python/JS 函数级独立结果缺；Mistral、Qwen3、Qwen2、Llama 有多来源但不全为同 harness 复测。**动作**：同队列、相同部署方式的内部独立复测。触及公司代码和员工请求日志可能含个人信息；目前未获授权，停在个人信息搜集/授权边界，不自取日志。
9. **[流程未完]** repo SOP 指定的 ego-browser 和独立 Reviewer 通道均不可用，本环境 `command -v ego-browser` 无结果，`.claude/skills/ego-verify/SKILL.md` 缺失；`functions.web_search` 已真实执行，**不**伪造网页 LLM/Reviewer 回执，阶段文档为降级续作而非流程审核通过。

## 八、结论（条件化判断，不超出数据）

**当前有条件的下一步：在确认可向所选 API 服务发送脱敏代码、地区和许可证合规后，将 Mistral-Small-24B-Instruct-2501 作为“只计固定请求形状下公开 API token 费”的低成本盲测试点；GLM-4-32B-0414（核对 Z.AI 精确 SKU）是价格相近而联合质量待测的对照组，Qwen3-32B 需分别实测 thinking/non-thinking 的合格率和计费输出；代码优先时也盲测 Qwen2.5-Coder-Instruct，但在所列 OpenRouter 价下其每尝试 token 费为 Mistral 的 13 倍。**严格 Apache/MIT 门槛下 Llama 不参加；题面的 DeepSeek-Coder-V2-33B 不存在，不参加。[1](https://openrouter.ai/mistralai/mistral-small-24b-instruct-2501) [1](https://docs.z.ai/guides/overview/pricing) [1](https://openrouter.ai/qwen/qwen3-32b) [1](https://openrouter.ai/qwen/qwen-2.5-coder-32b-instruct) [1](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) [1](https://github.com/deepseek-ai/deepSeek-Coder-V2)

在上述等 token / 无附加费 API **情景**中，若各候选联合通过率恰相同，Mistral `28¢/1k_acc`（假设 `q=0.50`）最便宜；若实际 `q_M>0.56`，则即使其他可辨候选 `q=1` 也不能以这些挂牌价格击败它（未计固定费用）。但**真实 `q_M`、任务长度、测试人工费及本地吞吐全部未测**，所以现在**无法严谨地判断哪个模型的真实“每千次合格回答总成本”最低**；不把这个条件结果写成无条件中标。反例 `q_M=0.40、q_G=0.80` 下 GLM 的 token 钱反而更省，说明下一步最有价值的是经授权的同任务联合盲测，而非继续堆叠不可比的厂商分数。

**本次实际执行/核对**：已在固定分支完成阶段 01、02、02.5、03 工件和本文件；`functions.web_search` 检索具体 benchmark/供应商价；官方 Qwen3 PDF 表头经 `pypdf` 核对，`pdftotext` 缺失（exit 127）后更换方法。运行 `python loop-artifacts/stages/04/T40-verify.py`（exit 0）：`Decimal` 验证五种价格的 `C(q)` 系数 `14/25/30/36/182`、比值和自托管临界值；静态扫描显示 **77 节点、3–4 边深、52 个唯一数值叶子**，树与 52 张来源/单位/敏感性卡片编号完全匹配，题面相对路径存在。已用明确文件列表 `git add -- ...` 使新增文件纳入检查，`git diff --cached --check`（exit 0）；请注意脚本只核算给定输入及检查 URL/路径**存在于文本**，不是 HTTP 可达性测试、同协议 benchmark 复现或独立 Reviewer。未进行真实 API 调用、GPU 推理、外部 Reviewer 审批或内部隐私数据采集；不能将这些写成已完成。
