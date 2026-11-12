# T40 / Q2 · 阶段 02.5：对抗核验、来源矛盾、可用边界

核验日 2026-11-06 UTC；输入：`stages/01/T40-decomposition.md`、`stages/02/T40-evidence.md` 及其中带 URL 的一手/独立资料。无 ego-browser/独立 Reviewer 可用，**以下是本执行者的对抗性自查，不冒充第三方审阅或正式 pass**。

## 1. 高影响值逐项双源检验（“有两份网页”≠“同协议复测”）

| 高影响主张 | 来源 A | 来源 B、反例 | 核验结果及能否用于根标量 |
|---|---|---|---|
| Qwen2.5-Coder-Instruct Python/JS 编码能力 | 官方报告 v3 [1](https://arxiv.org/html/2409.12186v3)：HumanEval/Python **92.7%**、MultiPL-E JS **85.7%** | BigCode 社区提交 [1](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard/discussions/87)：HumanEval **83.2%**、MultiPL-E JS **76.05%**；同一源码表中的任务分布、prompt/执行差异未完全追明 | 实际查到了两来源，数值矛盾 **9.5pp / 9.65pp**；不能择高值当内部 `q`。v3 专属 32B；v1 和 Base FIM 均不能替代 Instruct。 |
| Qwen3-32B thinking/non-thinking | 官方 PDF Table 13/14 [1](https://arxiv.org/pdf/2505.09388) 经逐列提取，LCB v5 **65.7/31.3%**；IFEval **85.0/83.2%** | 独立 Code2Bench-2505 [1](https://arxiv.org/html/2508.07180v1) Python **35.2%**、JS **28.0%**，未确认该表 Qwen3 模式；独立 IFEval strict-prompt **86.1%**（non-thinking）[3](https://arxiv.org/pdf/2608.23830) | 同名但不同任务/模式/提示；PDF 对列解决了搜索摘要错位，独立评测证明迁移不可靠，**不**构成 65.7 的同协议复现。Thinking 用非 thinking 的低 token 假设会低估钱。 |
| Mistral 2501 代码和指令分数 | 官方模型卡 [1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)：HumanEval **84.8%**、IFEval **82.9%** | Red Hat 评估**原始权重**的 OpenLLM v2 IFEval **73.27%** [3](https://huggingface.co/RedHatAI/Mistral-Small-24B-Instruct-2501-FP8-dynamic) | 同名 IFEval 相差 **9.63pp**，不同聚合协议；没有第二份相同 HumanEval 设置的独立复测。官方卡**同一内部 pipeline**的 Llama 数字可同 pipeline 比，仍不可算联合率。 |
| Llama 3.3 代码/指令 | Meta 模型卡 [1](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)：HumanEval **88.4%**、IFEval **92.1%** | Mistral 同流程测得 Llama **85.4%/88.35%** [1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)，Red Hat 原始模型 **83.20%/90.89%** [4](https://huggingface.co/RedHatAI/Llama-3.3-70B-Instruct-quantized.w8a8) | 三组口径不同；不能将 Meta 高值与 Mistral pipeline 的 Mistral 做排序。即便代码较好，严格 OSI 许可一票否决。 |
| GLM 工程/指令指标 | 官方 GitHub/HF [1](https://github.com/zai-org/GLM-4) [1](https://huggingface.co/zai-org/GLM-4-32B-0414)：IFEval **87.6%**，SWE-Verified Moatless/Agentless/OpenHands **33.8/30.7/27.2%** | 没找到同协议独立 GLM Python/JS 函数补全或 IFEval 复测；不同 agent 框架内部已有 **6.6pp** 波动 | **[GAP]** 不满足同口径双源交叉验证；SWE-Verified 是 agent 修复 repo issue，不可当函数补全合格概率。 |
| 2501 Mistral API 价格 | OpenRouter 精确路由 **$0.05/$0.08 每百万输入/输出 token** [1](https://openrouter.ai/mistralai/mistral-small-24b-instruct-2501) | DeepInfra 同名 2501 产品目录同价 [5](https://deepinfra.com/mistral) | 两供应方报价一致（但 OpenRouter 可能就是代理 DeepInfra）；只限本轮报价，更新日未公开。 |
| Qwen3 32B API 价格 | OpenRouter **$0.08/$0.28** [1](https://openrouter.ai/qwen/qwen3-32b) | DeepInfra **$0.08/$0.28** [2](https://deepinfra.com/pricing?amp=&amp=)；另一第三方页面仍有 **$0.08/$0.24** [2](https://www.llmreference.com/provider/openrouter/qwen3-32b) | 以本轮供应商公开报价 $0.28 计算，保留 0.24 的**时点/来源冲突**；OpenRouter 与 DeepInfra 并非独立计费数据。 |
| Qwen2.5-Coder API 价格 | OpenRouter **$0.66/$1.00** [1](https://openrouter.ai/qwen/qwen-2.5-coder-32b-instruct) | Cloudflare 同名 SKU **$0.66/$1.00** [1](https://developers.cloudflare.com/workers-ai/models/qwen2.5-coder-32b-instruct/) | 报价吻合；OpenRouter 路由指向 Cloudflare 时存在同供应方依赖，不能称为两家独立成交价。 |
| GLM / Llama API 价格 | Z.AI **精确 0414-128K** $0.10/$0.10 [1](https://docs.z.ai/guides/overview/pricing)；OpenRouter **精确 Llama 3.3 70B** $0.10/$0.32 [1](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct) | OpenRouter GLM `z-ai/glm-4-32b` $0.10/$0.10 [3](https://openrouter.ai/z-ai/glm-4-32b-0414)；DeepInfra Llama 同价 [1](https://deepinfra.com/llama) | GLM 网页路径与实际 API ID 不一致，**不证明**与 Z.AI 0414 完全同版；Llama OpenRouter 和 DeepInfra 同后端，独立性有限。所有价格在部署前再次核对。 |
| 2×24 GB 与量化占用 | NVIDIA 4090 **24 GB/卡** [1](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)，Runpod **24 GB/卡** [1](https://www.runpod.io/gpu-models/rtx-4090) | Llama Q4_K_M **42.5 GB 权重文件** [1](https://huggingface.co/second-state/Llama-3.3-70B-Instruct-GGUF/blob/abac21c4be7dca642bd7de0221aeb2149eba5c8f/Llama-3.3-70B-Instruct-Q4_K_M.gguf)；Runpod 明言双 4090 无 NVLink [1](https://www.runpod.io/gpu-models/rtx-4090) | 42.5 GB > 单卡 24 GB 是确定的；两卡 **不是统一显存**，需要显式模型并行/卸载，KV 和临时显存未测，不能断言双卡可用或不可用。 |
| DeepSeek 精确身份 | 官方 V2 列表只有 Lite **16B**、完整版 **236B**，原代 Coder **33B** [1](https://github.com/deepseek-ai/deepSeek-Coder-V2) | 原论文列 V2 **16B/236B** [4](https://arxiv.org/pdf/2406.11931) | **双源吻合**：`DeepSeek-Coder-V2-33B` 不存在，身份门槛不通过；不得将 V1 33B 改称 V2。 |
| 权重许可 | Qwen3 LICENSE Apache-2.0 [1](https://huggingface.co/Qwen/Qwen3-32B/blob/main/LICENSE)，GLM 权重 MIT [1](https://huggingface.co/zai-org/GLM-4-32B-0414/blob/main/README.md) | Meta 原始模型卡嵌入独立的 Llama 3.3 Community License [1](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)；Mistral Apache-2.0 [1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)；Qwen Coder Apache-2.0 [2](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct/blob/main/README.md) | 严格 Apache/MIT 准入时 Llama=**0**；开放权重解释另需内部法务核准，不借第三方营销文案判合法性。 |

## 2. 主动攻击本研究结论（多轮反例 → 修正）

1. **攻击“benchmark 两个高分相乘≈真实合格率”**：HumanEval、IFEval 来自不同样本空间，失败事件可能相关；公司 Python/JS 函数补全含内部项目约定、仓库上下文及量化/模式差异。乘积、`min(p1,p2)` 乃至弗雷歇下界都不适用于不同题集的联合事件。修正：以 `q_m = P(代码测试通过 ∧ 指令达标 | 本公司任务、部署路由、模式)` 作为**待测输入**；原值只做代理和选测试用例的线索。第三方 Code2Bench 同 cohort 中 Qwen2.5 Coder JS **34.2%** vs Qwen3 JS **28.0%** [1](https://arxiv.org/html/2508.07180v1)，是足以推翻“官方 LCB 更高 ⇒ Qwen3 必胜”的反例，但两者均非内部 q。
2. **反攻“至少找到第二个网页=高影响分数复现”**：BigCode vs 厂商 Qwen Coder 差 9.5pp；Mistral 82.9 vs Red Hat 73.27；不同 protocol/样本/含量不等价。修正：02 的高影响质量分标**矛盾未消解**；GLM 无独立同协议结果，留 [GAP]，不伪装“交叉验证通过”。
3. **反攻“同报价每请求就同成本”**：输出 token 在 Qwen3 thinking 模式可能包含思维内容，API 路由上下文、量化、税费和账期也不同；GLM OpenRouter 名称不保证同权重。修正：仅建立**相同 2,000 输入+500 实际计费输出 token**、不计固定/评审费用的 API 情景，并把模式/版本差异列为单独阻断项。可用的事实是每 token 价格，**不是**实际每请求成本。
4. **反攻“20GB GGUF <24GB 所以能跑 128K”**：权重文件不包括 KV cache、引擎、长上下文峰值；多卡无 NVLink 不合并池。修正：只能说单卡 24 GB 静态存储门槛上 Mistral/Qwen3/Qwen2/GLM 的所列权重文件 <24 GB，Llama >24 GB；本地服务准入仍 [GAP]。部分第三方把 GLM Q4 文件标 **18.3 GB** [4](https://gpufit.tech/models/glm-4-32b-0414/)，与 HF 的 **19.7 GB** [2](https://huggingface.co/unsloth/GLM-4-32B-0414-GGUF/tree/main) 可能是十进制 GB / 二进制 GiB（19.7/1.0737≈18.35），但未验证同一哈希/单位，不将推测当矛盾已解。
5. **反攻“题面每个都是开源可用型号”**：官方 DeepSeek 无 V2-33B；Llama 自定义许可不满足严格 OSI。修正：保持**原六项**，DeepSeek 原字符串身份=0（不排名）；Llama 仅在“开放权重 + 法务同意”敏感性分支出现。
6. **反攻“选择 OpenRouter 价格最低=最划算”**：若 Mistral 对真实内部任务通过率极低，其他模型即使报价高也可能有更低的 ¢/1k_acc；人类修复/安全/隐私及集成也未计。修正：阶段 04 只给充分条件、临界阈值和**有明确排除项的情景排序**，不宣称真实总成本最优。

停止点：要进一步给真正 `q_m` 必须收集/标注内部代码片段、员工请求、测试结果及失败原因，可能涉及员工个人信息和公司机密；目前未获该资料/授权，公开网页无法解开这一**个人信息搜集与授权瓶颈**。下游可先用经批准的脱敏仓库+匿名提示做盲测；在此之前不声称 Reviewer pass 或确定性最优。

## 3. 给阶段 03 的证据边界

- 可以**据公开价格、题面所给归一化单位及明确 [估计] token 情景**，复算每尝试 API 花费和 `q` 临界值；不能把情景值称为总成本。
- 公开 benchmark 可作为**数值叶子但必须保留来源、协议、模式和敏感性**；不同数据集/内部目标不可直接相乘。
- 许可、型号身份是硬门槛；本地容量只给重量级的必要条件，不给充分条件。
- 时间敏感报价仅是 2026-11-06 搜索观察：供应商未公布一致的近 7 天生效日，正式采购前重查；没有 Reviewer 回执，下一阶段为**未获独立审阅的降级续作**。
