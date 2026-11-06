# T41 · 02 信息调研（Q1 + Q3）

> 观察时间：2026-11-06 约 07:55–08:07 UTC；基线 `main@18375e2`。`web_search` 的搜索摘录可能是索引快照，不等于下单时的实时报价；网页的发表日期和摘录刷新日期也不能混为一谈。引用按搜索结果原编号与 URL 标识。下列仅是调查事实/假设，决策与计算在 04。

## 通道和输入回执

- `ego-browser --help` 实际返回 `/bin/bash: ego-browser: command not found`、退出码 127；`test -r .claude/skills/ego-verify/SKILL.md` 退出码 1。未获得网页 LLM 回答，不把它冒充来源。没有可调用的独立 Reviewer，不能伪造阶段 pass。
- T41 两个题面引用在 main 中均不存在：`git cat-file -e HEAD:<path>` 均退出 128；实际目录的 Q1/Q3 分别是 H100 变体题和固定服务器框架题。样例和原任务的边界见 01。
- 按 SOP 先尝试网页 LLM，失败后使用 `web_search`。围绕 H100 SXM/PCIe datasheet、Runpod GPU price、Llama 3.1 roofline、三家 `gpt-oss-120b` price/cache/rate limits、独立价格表等检索。精确搜索 `site:huggingface.co/meta-llama/Llama-3.1-8B-Instruct "8.03B" "BF16"` 无结果，换词后找到 Meta 卡片、Hugging Face 内存估算和其他资料；无结果不是证据。
- 按抓取限额，只对一个具体 URL 调用一次 `fetch_page`：Runpod 官方价格页可读，显示页面更新时间 2026-11-04 和 SKU；成功获得一手页面后停止抓取。其他资料仅为 `web_search` 返回的标题/摘录。

## Q1：查到的数值

| 主张 | 来源和观察 | 时效/不确定性 |
|---|---|---|
| H100 SXM 80 GB、HBM 3.35 TB/s、700 W、NVLink 900 GB/s | NVIDIA 官方规格页 [1](https://www.nvidia.com/en-us/data-center/h100/)；厂商 [7](https://lenovopress.lenovo.com/lp1732-thinksystem-nvidia-h100-pcie-gen5-gpu) | 稳定硬件规格；配置 TDP 不是实测功率。NVIDIA 当前页面对比对象是 **NVL**，不能把 NVL 一列读成 PCIe 80GB。 |
| H100 PCIe 80GB HBM2e、2 TB/s、350 W、桥接 NVLink 600 GB/s | NVIDIA PCIe 产品说明表格 [2](https://www.nvidia.com/content/dam/en-zz/Solutions/gtcs22/data-center/h100/PB-11133-001_v01.pdf)，Lenovo [7](https://lenovopress.lenovo.com/lp1732-thinksystem-nvidia-h100-pcie-gen5-gpu) | NVIDIA PDF 摘录正文亦出现 900 GB/s，而同文 NVLink 表 6 为 600 GB/s；与 Lenovo/PNY 的 600 一致，实际卡、桥和拓扑需实查，不能假设所有 PCIe 租赁实例装桥。 |
| BF16 Tensor 稀疏峰值 SXM 1,979、PCIe 1,513 TFLOP/s；dense 按半值 | Lenovo [7](https://lenovopress.lenovo.com/lp1732-thinksystem-nvidia-h100-pcie-gen5-gpu)，图宾根大学 [3](https://portal.mlcloud.uni-tuebingen.de/user-guide/_specs/gpu/h100/) 明确 `*` 为 sparsity，非稀疏为一半；Flopper [3](https://flopper.io/compare?s=nvidia-h100-pcie-80gb,nvidia-h100-sxm5-80gb) 直接列 BF16 dense | Dense 算术峰值分别 989.5/756.5 TFLOP/s；不是实际 prefill 性能。 |
| PCIe Gen5 x16 总双向峰值 128 GB/s；PCIe 的 600 GB/s 是可选桥 | NVIDIA [2](https://www.nvidia.com/content/dam/en-zz/Solutions/gtcs22/data-center/h100/PB-11133-001_v01.pdf)，Lenovo [7](https://lenovopress.lenovo.com/lp1732-thinksystem-nvidia-h100-pcie-gen5-gpu) | 所有数值为标称峰值，单向和双向不能混用，也不是 GPU 利用率。 |
| 单卡 Secure Cloud Pod：PCIe $2.89、SXM $3.99/GPU·h | 2026-11-04 更新的 Runpod [1](https://www.runpod.io/pricing)，独立对照 2026-10-31 的 Activepieces [3](https://www.activepieces.com/blog/runpod-pricing-2026-for-pods-serverless-and-storage) | 前者于本轮成功直接抓取；不同 CPU/RAM、地区、库存和额外存储费用可改变比较。厂商较旧文章 SXM $3.49 [4](https://www.runpod.io/articles/guides/h100-clusters-on-runpod-for-distributed-ai-training) 与现价冲突，不取旧值。 |
| Llama 3.1 8B 示例：约 8B 参数、16-bit 约 16 GB 权重 | Meta [1](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md)，Hugging Face [1](https://huggingface.co/blog/llama31) | 仅模型权重，KV/工作区另计；原题模型未知。 |
| 理想 single-stream decode: SXM 约 4.78 ms、PCIe 约 8 ms/token | 独立 roofline 例子 [3](https://dev.to/sachin_krrajput/the-roofline-model-for-llm-inference-4cne)；VMware [2](https://blogs.vmware.com/cloud-foundation/2024/09/25/llm-inference-sizing-and-performance-guidance/) | 算术估计不是实测。Runpod 对 1024-in/1024-out、batch=1 的 H100 PCIe 报 88 output tok/s [4](https://www.runpod.io/gpu-compare/b300-vs-h100-pcie)，精度/框架口径待确认，不能直接当作两卡受控比较。 |
| 不同场景的配对实测约 SXM 吞吐 +30% | Dell 对 H100 的 Llama 2 7B BF16 测试 [3](https://infohub.delltechnologies.com/fr-fr/p/comparing-nvidia-h100-pcie-on-r760xa-vs-nvidia-h100-sxm-on-xe9680/) | 主机、模型及负载口径与本示例不同；该测试说明 1.675× 带宽比不保证同等吞吐比，不能替代本题实测。 |
| 理论 100% 带宽效率/满负荷示例 | 理论峰值带宽例子 [2](https://www.jslet.com/llm-inference-latency)；DigitalOcean 用 100% 利用率计算单 token 成本 [1](https://www.digitalocean.com/community/tutorials/llm-inference-cost) | 均是公开算例的边界条件，非本题观测；DigitalOcean 利用率为吞吐占峰值，04 的 `u` 为付费时间中活跃占比，口径不同。 |
| 模型 KV 开销约 128 KiB/token/序列（BF16） | 公开公式与配置的 HF 论坛 [5](https://discuss.huggingface.co/t/llama-3-1-8b-instruct-memory-usage-more-than-reported/140711)；VMware 表 0.000122 GiB/token [2](https://blogs.vmware.com/cloud-foundation/2024/09/25/llm-inference-sizing-and-performance-guidance/) | 还需额外 runtime/激活/碎片；1 KiB=1024 字节、1 GB=10^9 字节。 |

## Q3：候选与数值

- **研究中显式更换示例模型（2026-11-06）：** 01 的三家供应商候选不变，原拟三方同款 Llama 3.3 70B 的公开按量比较失效：Groq 的原路径被列入 2026-08-16 弃用记录 [8](https://console.groq.com/docs/deprecations)，现目录给出 Enterprise/Contact Sales [1](https://console.groq.com/docs/models)；Together 对该模型页面显示不在 Serverless [4](https://www.together.ai/models/llama-3-3-70b)；Fireworks 同一页面的 FAQ 宣称 Serverless，但元数据又显示 Not supported [1](https://fireworks.ai/models/fireworks/llama-v3p3-70b-instruct)。不将旧 $0.59/$0.79、$0.88 或 $0.90 价格当成当前可购买报价。
- 同候选集合改为 `gpt-oss-120b`：Groq [1](https://console.groq.com/docs/model/openai/gpt-oss-120b)、Together [6](https://docs.together.ai/docs/serverless/models)、Fireworks [1](https://fireworks.ai/models/fireworks/gpt-oss-120b) 搜索摘录均列出 serverless/production，非原题已指定模型。
- 按量标准未缓存输入/输出价格均为 **$0.15/$0.60 每百万 token**，三家的官方页分别为上述三个来源；独立报价对照 [2](https://www.braintrust.dev/articles/best-ai-apis-2026) 和 [6](https://techiehub.blog/cheapest-ai-api/) 一致。后者写的价格核对日为 2026-10-28，已超过七天；不能充当近期独立复核。Groq 价格另有 2026-11-04 的第三方 [8](https://www.aipricing.guru/groq-pricing/)。
- 缓存输入价格 Groq $0.075/M [1](https://console.groq.com/docs/model/openai/gpt-oss-120b)，Fireworks $0.015/M [1](https://docs.fireworks.ai/serverless/pricing)；Together 对此模型的 Cached input 列为 `-` [6](https://docs.together.ai/docs/serverless/models)，官方规则规定无缓存报价模型全部按普通输入费率 [1](https://docs.together.ai/docs/inference/chat/prompt-caching)；第三方对照 [1](https://omidsaffari.com/blog/groq-pricing)（2026-10-28）。各来源没有证明相同真实命中率，故 50% 只可用作例子。
- 上下文 131,072 tokens：Groq [1](https://console.groq.com/docs/model/openai/gpt-oss-120b)、Together [6](https://docs.together.ai/docs/serverless/models)、Fireworks 目录 [4](https://fireworks.ai/models?providers=OpenAI)。Groq 开发者公开目录另列 250K TPM / 1K RPM [2](https://console.groq.com/docs/models)；Fireworks 的有卡账户 6,000 RPM 是**账户上限而非保底** [2](https://docs.fireworks.ai/guides/quotas_usage/rate-limits)。
- 一个公开的说明性工作量是 100M 输入、20M 输出，另举 50% 缓存示例 [1](https://omidsaffari.com/blog/groq-pricing)。来源未明确将该工作量限定为每月，后续仅为算例方便自行设为一月；这不是用户的真实流量或承诺命中率。
- 第三方 AA 的高 reasoning 路径摘要列 Groq 472.4 tok/s、Together 147 tok/s [1](https://artificialanalysis.ai/models/gpt-oss-120b/providers)；Groq 自报约 500 tok/s [1](https://console.groq.com/docs/model/openai/gpt-oss-120b)。实验的环境、时间与样本细节未完全取得；不是用户业务的 p99 或 SLA，Fireworks 不可据此与之比较。

## 主要缺口与后续

缺少原题、业务 SLO、规模/预算、区域与合规、受控基准、实时库存及实际缓存命中；高影响动态价格虽有一手索引与部分独立对照，但 Together/Fireworks 的近七天独立快照、实际账户与订单尚缺。后续 02.5 比较来源口径、识别矛盾并限定计算适用条件；04 给出可复算条件化树。
