# T40 / Q2 · 阶段 02：资料搜集与证据边界

观察日：**2026-11-06 UTC**；研究对象固定为阶段 01 / Q2 题面中的六个候选字符串。本工件仅是资料账本，**不是选型结论、不是 Reviewer 回执**。全部 benchmark、报价、容量数值均来自本轮实际 `functions.web_search`；另对 Qwen3 官方 PDF 通过 GitHub API 取得原件并用 Python `pypdf` 提取表格，以免网页搜索摘要错列。完整计算和树在阶段 04。

## 0. 通道/方法回执

- SOP 要求的 ego-browser 网页 LLM 交叉询问：本环境执行 `command -v ego-browser` 无路径，`.claude/skills/ego-verify/SKILL.md` 和仓库 `AGENTS.md` 均不存在；**不可执行**，没有网页 LLM 回执，也不假造。按 SOP 的快速失败规则改为实际 `functions.web_search` 搜公开网页；网页摘要仅用于定位，原始供应商/报告与独立测评分别记录。
- `functions.fetch_page` 已对四个已知 URL 各读取一次 chunk 0：Qwen3 论文 HTML `arxiv.org/html/2505.09388v1`、Qwen2.5-Coder **v1**、Mistral 官方模型卡、Meta 官方模型卡。前两者篇幅很长；Qwen2.5 的 32B **不在 v1**，故另用 web_search 检索 **v3**。之后没有对任一 URL 重试 fetch。
- `gh api repos/QwenLM/Qwen3/contents/Qwen3_Technical_Report.pdf --jq .content | base64 -d` 成功取得官方 PDF（674,714 字节，35 页）；系统缺 `pdftotext`（exit 127）；`pypdf` 安装在仓库外 `/home/user/.cache/T40/python` 并提取第 16 页：Table 13 最后一列 Qwen3-32B **thinking** 的 IFEval strict prompt 85.0%、LiveCodeBench v5 65.7%；Table 14 最后一列 **non-thinking** 83.2%、31.3%。原件：[1](https://arxiv.org/pdf/2505.09388)；官方仓库文件 `https://github.com/QwenLM/Qwen3/blob/main/Qwen3_Technical_Report.pdf`。这一提取不代表独立复现模型 benchmark。
- 研究日期是**本次实际查看时间**，不等于网页发布日期；价格页面没有可核的近 7 日发布/生效日期时标为时效未结，不能将抓取时间伪装成报价有效期。

## 1. 事实账本：模型身份、质量指标及协议

以下每行的「发布/更新」是来源自己能核实的版本/日期；无则记「未标」。所有行为 Q2 提供线索，**不同 benchmark 行不能横向合算**。

| 主张 / 来源类型 | 数值和测量口径 | 发布/更新；观察 | 状态与限制 |
|---|---|---|---|
| Qwen2.5-Coder 研究报告 **v3**，一手论文 [1](https://arxiv.org/html/2409.12186v3)；修订历史 [2](https://arxiv.org/abs/2409.12186) | 32B-Instruct：HumanEval Python pass@1 **92.7%**；MultiPL-E Python **92.7%**、JS **85.7%**、TS **86.8%**；LiveCodeBench **31.4%**；IFEval **79.9%**。MultiPL-E 表头 Python/Java/C++/C#/TS/JS/PHP/Bash，**85.7 为 JS 列**。 | v3：2024-11-12；2026-11-06 | 模型限定 **Instruct**；v1 只有 1.5/7B，报告第 6 节的 FIM 是 **Base**，不许赋给 Instruct。LCB 与 Qwen3 的 v5 不是同协议。 |
| BigCode 社区提交，独立评测 [1](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard/discussions/87) | 同名 Qwen2.5-Coder-32B-Instruct：HumanEval **83.2%**；MultiPL-E JS **76.05%**。 | 2024-11-11；2026-11-06 | ≠厂商 92.7/85.7；模型名一致但提示、采样、测试及 harness 不一致；没有证据证明同协议。 |
| Qwen3 官方报告 Table 13/14，一手论文 PDF [1](https://arxiv.org/pdf/2505.09388) | **Thinking**：LiveCodeBench v5 **65.7%**、IFEval strict-prompt **85.0%**；**non-thinking**：LCB v5 **31.3%**、IFEval **83.2%**。两模式代码分差 **34.4pp**（本轮由两表相减）。 | 2025-05；2026-11-06 | 官方 PDF 经逐列核验。Thinking 可能计费额外输出 token，不能沿用 non-thinking 的 500 输出 token 成本。 |
| 第三方动态真实代码生成评测 Code2Bench-2505 [1](https://arxiv.org/html/2508.07180v1) | Qwen3-32b：Python **35.2%**、JS **28.0%**；Qwen2.5-Coder-32b-Instruct：Python **36.2%**、JS **34.2%**，同一论文/任务族。 | 2025-08-10；2026-11-06 | 论文研究由近期仓库构建动态任务；**Qwen3 模式未从该表确认**；不是 LCB/HumanEval 的同题复测，更不是内部助手的合格率。不同公开基准会改变相对顺序。 |
| 第三方 instruction-following 论文 [3](https://arxiv.org/pdf/2608.23830) | Qwen3-32B **non-thinking**：IFEval **strict-prompt 86.1%**。 | 2026-08；2026-11-06 | 原论文区分 IFEval strict 和其他口径；与厂商 non-thinking 83.2% 的定义较近但温度/提示不同，不能称一致复现。 |
| Mistral 官方模型卡 [1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) | Mistral 2501 HumanEval instruct pass@1 **84.8%**、IFEval **82.9%**；**同一内部评估流程**中的 Llama 3.3 70B 为 **85.4%/88.35%**；32k 上下文、Apache 2.0。 | 2025-01-30；2026-11-06 | 可在这个供应商的同一套流程中比较两者对应指标；不能和 Meta 自测按同一口径比较，更不能把两指标乘成实测联合率。 |
| 独立量化评测 Red Hat [3](https://huggingface.co/RedHatAI/Mistral-Small-24B-Instruct-2501-FP8-dynamic) | **原始未量化** Mistral 2501 OpenLLM v2 IFEval 0-shot **73.27%**；FP8 版本 **73.53%**。 | 页面未标清发布日；2026-11-06 | 官方模型卡的 IFEval 82.9% vs 此处 73.27% 为不同 harness 和聚合方式；不是量化后必然增益。 |
| Meta 官方模型卡 [1](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | Llama 3.3 70B HumanEval 0-shot pass@1 **88.4%**，IFEval **92.1%**；自有 Llama 3.3 Community License，非 Apache/MIT。 | 2024-12-06；2026-11-06 | 可能以开放权重条款使用，但**严格 OSI 开源准入=0**；是否接受附加条款须用户/法务确定。 |
| Red Hat 独立量化评测 [4](https://huggingface.co/RedHatAI/Llama-3.3-70B-Instruct-quantized.w8a8) | **原始未量化** Llama 3.3 70B HumanEval **83.20%**、OpenLLM v2 IFEval **90.89%**。 | 页面未标清发布日；2026-11-06 | 与 Meta 88.4/92.1 不同 harness；不是同协议复现。 |
| Z.AI 官方 GLM 模型卡及代码仓库 [1](https://huggingface.co/zai-org/GLM-4-32B-0414) [1](https://github.com/zai-org/GLM-4) | **GLM-4-32B-0414** IFEval **87.6%**；SWE-bench Verified 使用 Moatless **33.8%**，Agentless **30.7%**，OpenHands **27.2%**。权重卡 `license: mit` [1](https://huggingface.co/zai-org/GLM-4-32B-0414/blob/main/README.md)。 | 2025-04-14 系列发布；2026-11-06 | SWE-bench 是代理+仓库 issue 修复指标，**不是函数级 Python/JS 补全**；未搜得同协议的独立 GLM 代码/IFEval 复现。仓库代码 Apache-2.0 与权重 MIT 分属不同对象，不冲突。 |
| DeepSeek 官方 Coder-V2 发布 [1](https://github.com/deepseek-ai/deepSeek-Coder-V2) | V2-Lite **16B 总/2.4B 激活**；V2 **236B 总/21B 激活**；表中 **33B** 行名为 *DeepSeek-Coder-Instruct*（原代），不是 V2。 | 2024-06；2026-11-06 | 题面 `DeepSeek-Coder-V2-33B` **身份不成立 (0)**，不可将 33B 原代基准与 V2 费用混算，也不可静默替换成 Lite。 |

## 2. 事实账本：API、租卡、权重与许可

**API 单价均为 USD / 1,000,000 实际计费 input/output tokens**；只是指定路由/精确 SKU 的公开挂牌价，不含税、平台额外费用、重试、cache、服务等级。观察日均 2026-11-06。第一、第二来源有时引用同一后端，并非完全独立的账单复现。

| 精确产品 / 主来源及第二来源 | 输入 / 输出；更新信息；独立性 | 未解决影响 |
|---|---|---|
| OpenRouter `mistralai/mistral-small-24b-instruct-2501` [1](https://openrouter.ai/mistralai/mistral-small-24b-instruct-2501)；DeepInfra 的 2501 产品列表 [5](https://deepinfra.com/mistral) | **$0.05 / $0.08**；两个不同供应方报价，同值；网页更新日未标。 | 可作为本轮 API 情景，需结算前复核价格及服务区域。 |
| OpenRouter `qwen/qwen3-32b` [1](https://openrouter.ai/qwen/qwen3-32b)；DeepInfra 报价 [2](https://deepinfra.com/pricing?amp=&amp=) | **$0.08 / $0.28**；OpenRouter 页面路由 DeepInfra；第二来源可能同一计费后端。页面发布日 ≠ 现价生效日。 | Thinking 的输出量、实际下单路由及上下文配额待查。另一第三方页面仍列 **$0.24** 输出 [2](https://www.llmreference.com/provider/openrouter/qwen3-32b)，这是时效/供应商异议，按主来源本轮价计算并留敏感性。 |
| OpenRouter `qwen/qwen-2.5-coder-32b-instruct` [1](https://openrouter.ai/qwen/qwen-2.5-coder-32b-instruct)；Cloudflare 直接产品文档 [1](https://developers.cloudflare.com/workers-ai/models/qwen2.5-coder-32b-instruct/) | **$0.66 / $1.00**；两家报价同值，文档更新日未标。 | OpenRouter 页面可路由 Cloudflare，不能当真正独立的吞吐/可用性复测。 |
| Z.AI `GLM-4-32B-0414-128K` 官方 [1](https://docs.z.ai/guides/overview/pricing)；另一个产品的 OpenRouter `z-ai/glm-4-32b` [3](https://openrouter.ai/z-ai/glm-4-32b-0414) | 各列 **$0.10 / $0.10**；官方页面未标可核验的近 7 日修订；二者**不是已经证明同一个 SKU**（OpenRouter URL 路径含 0414，而展示 API ID 不含）。 | 只用 Z.AI **精确 SKU**算 GLM，另一页只核对数量级，不拿它证明同一权重。 |
| OpenRouter `meta-llama/llama-3.3-70b-instruct` [1](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct)；DeepInfra 列表 [1](https://deepinfra.com/llama) | **$0.10 / $0.32**；OpenRouter 页面路由 DeepInfra，两页面可能同供应商。更新日未标。 | 权重许可仍须另行核验；API 的条款与自托管许可不可混为一谈。 |
| Runpod RTX 4090 产品 [1](https://www.runpod.io/gpu-models/rtx-4090)；Runpod 价格总页 [1](https://www.runpod.io/pricing) | **24 GB/卡**；Community Cloud **$0.34/GPU·h**，Secure Cloud **$0.89/GPU·h**。产品页标记 2026-08-27，总价页搜索索引 2026-11-04；两页同供应商。NVIDIA 官方规格也记 **24 GB/卡** [1](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)。 | 2 张卡 2×24 GB 并**非统一的 48 GB 显存池**，4090 不支持 NVLink（Runpod 产品页）。租卡价格随地域/库存变，使用 Secure 情景非采购事实。 |

Q4_K_M 文件体积（**仅静态权重文件，不含 KV cache、推理时临时张量及服务器进程**）：Qwen3 官方 GGUF **19.8 GB** [3](https://huggingface.co/Qwen/Qwen3-32B-GGUF/blob/main/Qwen3-32B-Q4_K_M.gguf)；Qwen2.5-Coder-Instruct 社区 GGUF **19.9 GB** [1](https://huggingface.co/bartowski/Qwen2.5-Coder-32B-Instruct-GGUF/blob/main/Qwen2.5-Coder-32B-Instruct-Q4_K_M.gguf)；Mistral Small 2501 **14.3 GB** [3](https://huggingface.co/lmstudio-community/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q4_K_M.gguf)；GLM-4-32B-0414 **19.7 GB** [2](https://huggingface.co/unsloth/GLM-4-32B-0414-GGUF/tree/main)；Llama 3.3 70B **42.5 GB** [1](https://huggingface.co/second-state/Llama-3.3-70B-Instruct-GGUF/blob/abac21c4be7dca642bd7de0221aeb2149eba5c8f/Llama-3.3-70B-Instruct-Q4_K_M.gguf)。Q4_K_M 的实际有效位宽并非恰好 4 bits/param。Llama 单卡 24 GB 装不下 42.5 GB 权重；双卡并行能否在 KV+峰值开销下可用仍未实测。

许可一手出处：Qwen3 Apache-2.0 [1](https://huggingface.co/Qwen/Qwen3-32B/blob/main/LICENSE)；Qwen2.5-Coder-Instruct Apache-2.0 [2](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct/blob/main/README.md)；Mistral 2501 Apache-2.0 [1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)；GLM 权重 MIT [1](https://huggingface.co/zai-org/GLM-4-32B-0414/blob/main/README.md)；Llama 自定义 Community License [1](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)。若「开源」要求 Apache/MIT 一类许可，Llama 不符合；DeepSeek **候选型号不存在**，无需假定其许可。

## 3. 阶段 01 的空缺逐项清算及不应当计算的值

| 空缺 | 本轮找到的公开值 | 阻断根标量的未给值 / 下一步 |
|---|---|---|
| A：真实代码+指令的**联合合格率**和 benchmark→内部任务迁移 | 厂商 Python/JS/IFEval、第三方同队列 Code2Bench，有代码基准差异 | **[GAP]** 各候选在相同内部 Python/JS 函数补全且满足指令格式的 `q_m`、失败关联性、prompt/采样设置、量化后降幅、Qwen3 模式；不能拿两个数据集分数相乘冒充观测联合率。 |
| B：可购买 API 价格 | 五个可辨认型号的相应挂牌价，DeepSeek 原字符串不能报价 | **[GAP]** 同日正式报价/税费/路由结算/服务 SLA；GLM OpenRouter 映射未核准。价格没有可核近 7 日生效时间，仅本轮检索观察。 |
| C：本地预算 | 24 GB/卡、单/双卡租价及静态 GGUF 文件体积 | **[GAP]** 完整上下文 KV/峰值与吞吐、利用率、加速/多卡并行方式、量化损失、模型服务压测；不能由文件大小推出 24 GB 卡上 128K 可用。 |
| D：身份与授权 | 5 个候选确有模型/对应权重；「V2-33B」不在官方列表；许可 4 Apache/MIT、Llama 自有许可 | **[GAP]** 用户对「开源」是否严格 OSI/开放权重、Llama 法务批准、是否允许用 DeepSeek Lite 或原 33B 替换原字符串。候选集不暗改。 |
| E：总成本/工作量 | 题面只给 1,000 个合格单位与 2×24 GB 级资源 | **[GAP]** 真实输入/输出 token、长期合格量、审查/测试/修复及开发运维费用、失败重试相关性；可给标记为**情景**的币值与 break-even，但不填实际 TCO。 |

至此能交给 02.5 的是**公开证据+未解决条件**，不是模型排行。未收到独立 Reviewer 回执，不给本阶段贴 `pass`。
