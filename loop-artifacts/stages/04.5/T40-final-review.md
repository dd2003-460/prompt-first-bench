# T40 / Q2 · 阶段 04.5：最终反方复核与交接

2026-11-06 UTC，审阅者为**本执行 agent 自检**，**不是**独立 Reviewer。没有 `ego-browser` 可执行命令/ego-verify skill，也没有独立 Reviewer 回执或 `latest-review.md`；遵守任务书通道故障降级：记录能力边界、不编造审批。在本页编写时 commit/push 尚待执行，最终终端/会话回执为准。

## 原任务→证据→行动→结果链

| 验收项 | 输入与事实证据 | 真正执行/可见结果 | 未完成/结论边界 |
|---|---|---|---|
| 仅目标仓库、原任务书及实际题面 | `main@e7dc6ee` 的 `tasks/T40-gold-replication-arena.md` 与 [Q2 实际题面](../../../experiments/stage-ablation/questions/Q2-model-selection.md)；任务书误指不存在的 Q2.txt | 工作分支未切换；恢复任务书到当前分支并创建阶段 01/02/02.5/03/04/04.5 文件 | 原问题路径错误已记录，不凭空创建改写题面。 |
| 实际查具体 benchmark、不是旧 gold/记忆 | 官方 Qwen2.5-Coder v3 [1](https://arxiv.org/html/2409.12186v3)、Qwen3 原 PDF [1](https://arxiv.org/pdf/2505.09388)、Mistral 卡 [1](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)、Meta 卡 [1](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)、GLM 卡 [1](https://huggingface.co/zai-org/GLM-4-32B-0414)、独立 BigCode [1](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard/discussions/87)、Code2Bench [1](https://arxiv.org/html/2508.07180v1) | 阶段 02 记来源/观察日，02.5 记矛盾；04 每一个数值叶子有来源及敏感性；Qwen3 PDF 的两模式/表头用 `pypdf` 独立于搜索摘要逐列核实。 | 不同 benchmark/harness 未强制统一。GLM 代码/IFEval 独立同协议结果仍 [GAP]；没有实跑候选。 |
| 根可排序标量、正交 3–5 维、树≥3 深/≥15 节点 | `stages/01/T40-decomposition.md` 的 W/Q/S/E 边界；`stages/04/execution-log.md` 根公式及 ASCII 树 | `python loop-artifacts/stages/04/T40-verify.py` 以 `Decimal` 验五路 API 钱及 q 临界；结果 **77 节点、最小 3 / 最大 4 边深、52 个唯一数值叶子**，卡片与树逐一对应；四维互斥路由。 | 根的真正 `q`、固定 `F`、本地 `H_effective` 未给，所以**不能**以公开分数无条件排序真实 TCO。 |
| 高影响数字双源 / 矛盾解释 | 02/02.5 的官方价/第三方价和官方/独立评测；DeepSeek 官方列表与论文 [1](https://github.com/deepseek-ai/deepSeek-Coder-V2) [4](https://arxiv.org/pdf/2406.11931) | 04 §六双源表明确 92.7 vs 83.2、82.9 vs 73.27、Qwen3 65.7 vs 31.3 **不同模式**、OpenRouter GLM ID 差异；保留独立性不足。 | “两个网页”不等于同协议独立复测/近 7 日合同报价；未解决者标 GAP，不以自查覆盖。 |
| 完整输出在指定文件、数值可复核 | `loop-artifacts/stages/04/execution-log.md`，附 `T40-verify.py` | 文件中顺序为公式→正交表→ASCII 树→52 叶卡→情景计算→双源表→缺口→结论。新增文件已显式 `git add -- ...`，`git diff --cached --check` exit 0；本工件完成后须再检查包括本文件的最终 index。 | 复核脚本只核算情景及源 URL 文本，不联网验证全部链接，更不是独立审稿。 |
| 提交及推送 | 用户要求 commit + push；固定分支为 `arena/2d62d48c-prompt-first-bench` | 由随后 `git commit`、`git push origin arena/2d62d48c-prompt-first-bench` 实际退出码证明 | **此刻未执行，不能在本工件预报成功。** 若鉴权失败，在 Arena 请用户重连 GitHub，不收集凭证。 |

## 反方检查：怎么推翻当前推荐？

1. **若企业任务 Mistral 真正联合通过率低于竞争者的价格比门槛**，GLM 甚至可能在更高挂牌单价下更省：04 的反事实 `q_M=.40, q_G=.80` 为 35¢ vs 31.25¢。这个反例说明 **Mistral 不是已证明的总成本赢家**。已在 04 结论处将其限制成经合规批准后的低单价盲测试点，未把公开 HumanEval/IFEval 乘为 q。
2. **若 Qwen3 thinking 额外生成大量计费 token**，它的 `o=500 [估计]` 行尤其乐观，不能把 65.7% thinking 的 LCB 质量与 31.3% non-thinking 的短输出钱混成一个模型方案。[1](https://arxiv.org/pdf/2505.09388) 必须按实际模式每次拿 token 账本。
3. **若真正“开源”=带条件的开放权重也可以**，Llama 进入 API 备选而非严格许可一票否决；Meta 自有社区协议需法务看。[1](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) 但它的 42.5 GB GGUF 静态文件 >单卡 24 GB，双卡 VRAM 不会无条件合并。[1](https://huggingface.co/second-state/Llama-3.3-70B-Instruct-GGUF/blob/abac21c4be7dca642bd7de0221aeb2149eba5c8f/Llama-3.3-70B-Instruct-Q4_K_M.gguf) [1](https://www.runpod.io/gpu-models/rtx-4090)
4. **若采购可以谈判更低价或用自托管**，OpenRouter/Qwen2.5 的 13× 差价不再代表所有供应路线；本地吞吐、质量损失及固定投入未测。GLM 的 Z.AI `0414-128K` 与 OpenRouter `z-ai/glm-4-32b` 未证完全同权重，04 只按精确官方 SKU 算。[1](https://docs.z.ai/guides/overview/pricing) [3](https://openrouter.ai/z-ai/glm-4-32b-0414)
5. **若审批要求“候选都必须有效”**，DeepSeek 原字符串无法评价，不能把 V1 33B 或 V2 Lite 16B 偷渡到六项结果中；这并不阻止为余下五个可辨模型交付条件化结构。[1](https://github.com/deepseek-ai/deepSeek-Coder-V2)

## 未完成项、回退和下一位执行者的第一步

- **需要用户同步确认（阶段 03 A7）**：“开源”许可解释；是否允许对匿名的内部代码/员工请求进行测评；数据驻留及是否允许把脱敏代码提交给 API；接受的正确率/延迟阈值。未授权时**不要**采集内部日志或调用外部 API。
- **需要实测（阶段 03 A8）**：固定匿名 Python/JS/通用指令任务比例，逐项测同一道题的代码单测 **AND** 格式约束、按路由/模式记实际 token、人工评审费用、并行吞吐及 KV/峰值，再带置信区间算真实 ¢/1k_acc。无此结果不得生产中标。
- **证据需要回退阶段 02/02.5**：GLM 同协议独立函数补全、API 正式报价生效日和 GLM SKU 映射、模型量化后 pass@1、隐私/许可证批准；如拿不到，标明缺口，不准用本文件 q 情景当事实。**若**发现公式或静态计算错误，回退阶段 04 修复并重新运行脚本。
- **通道风险**：本轮未通过 SOP 指定的独立 Reviewer（不可用）。阶段 Markdown 均不写 Review 路由块或 `verdict: pass/revise`，不可给下游呈现为已审批选型。

**交接定位**：完整交付只需打开 `loop-artifacts/stages/04/execution-log.md`；需要追查来源争议读 02/02.5；复算运行 `python loop-artifacts/stages/04/T40-verify.py`。终稿结论为“有条件的 API 低价试点和量化 break-even，真实最划算者 [GAP]”，不是声称所有六个候选均已上线验证。
