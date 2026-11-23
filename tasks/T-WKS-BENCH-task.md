# T-WKS-BENCH: 顶会 workshop 论文对标调研（agent 评测方向）

> origin: ai · 2026-11-24 · 仓库 prompt-first-bench · 分支 arena/f65a5a27-prompt-first-bench
> 本任务只涉及 prompt-first-bench 仓库，忽略历史中其他仓库的消息。

## [任务]

回答一个问题：**NeurIPS / ICLR / ICML / AAAI / ACL 2025-2026 的 workshop track（不是主会）里，
有没有论文与下面这篇草稿的 3 个卖点重叠？重叠度多高？撞车风险排序是什么？**

草稿 3 卖点（我们的 workshop 草稿，metacognition 方向的 LLM 研究 agent 评测）：
1. **过程测量框架**：不只看最终答案对不对，把 agent 内部拆开量——gap 标记、检索、
   验证、返工每个环节单独有指标（83 runs / 21,945 节点 / 3 个域）
2. **负结果 + 裸臂对照**：核心发现是"预算买不到收敛"（0/21 次命中 gold 配置，
   每个预算档都一样）+ 监控好但修复差（93.5% gap 诊断正确，返工只修好 3.1%）；
   关掉状态机的裸臂重跑，失败照样复现
3. **机械 judge**：coverage 和 conclusion 层纯机械打分（无 LLM 参与，同输入同输出），
   规避 LLM 自评偏差

## [背景]

- 草稿位置：本仓 `experiments/stage-ablation/workshop-draft-metacog-20261122.md`
  （可只读 §1-§3 了解草稿全貌，不必全文）
- 目标 venue：NeurIPS/ICLR/ICML/AAAI/ACL 2025-2026 的 **workshop track**
  （ICLR/NeurIPS workshop 在 OpenReview，ACL 在 anthology，AAAI 在 ojs.aaai.org）
- 关注方向关键词：LLM agent evaluation / deep research benchmark / metacognition /
  LLM-as-judge / process-level evaluation / self-monitoring / citation grounding
- 已知撞车候选（草稿 related work 已引，不用重复调研）：DREAM (ACL 2026 long.448)、
  DR-Bench、BrowseComp、DynaBench、AgentBench、WebArena

## [约束]

- 中文回答；每条论文条目标 conf(0-1)；给来源 URL（OpenReview/arXiv/anthology 直链）
- 不确定的标"未验证"，不编造论文标题
- 只收 workshop track 论文；主会论文单独列一小节（标"主会非 workshop"）

## [交付]

markdown 文件，写到本仓 `experiments/stage-ablation/workshop-benchmark-survey-20261124.md`，
格式：

```
# Workshop 对标调研（agent 评测方向）
> origin: ai · <日期> · conf 标注

## 1. 论文清单
| # | 标题 | venue+workshop名 | 一句话方法 | 与卖点1重叠 | 与卖点2重叠 | 与卖点3重叠 | conf | URL |
（重叠度填：无 / 部分 / 高）

## 2. 撞车风险排序
（按风险从高到低，每条一句话理由）

## 3. 主会论文（非 workshop，单独列）
（同上表格，简版）

## 4. 结论
（≤5 行：我们的 3 卖点在 workshop 层面是否独有；最强威胁是谁；claim 措辞建议）
```

## [长度]

核心 ≤50 行；论文清单表格不限行数（这是交付主体）。

## [落盘约束]

文件不存在 = 任务未完成，Lead 不验收。
