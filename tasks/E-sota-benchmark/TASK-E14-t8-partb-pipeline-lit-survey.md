# T8-Part-B: 文献调研——multi-stage agent pipeline prompt 贡献度

**任务类型**: 文献调研（arena 代干）
**执行通道**: arena agent mode @ decomp-bench
**产出路径**: `experiments/T8-lit/lit-survey-pipeline-prompts.md`
**门禁**: ≥2 独立来源 + 每条结论标 conf (0-1)

## 背景

T8 是 prompt-first 消融研究：测 pfb pipeline 的 7 段 prompt 各自对输出质量（M8 核验真实性率）的贡献。L1 组件级消融已完成（decomp bench），现在需要文献支撑来回答：

1. 我们的 L1 结论（单组件删除效应）能否合理映射到 multi-stage pipeline 阶段级？
2. 文献中有没有类似"删掉 pipeline 某阶段的 prompt → 输出质量变化多少"的系统性研究？
3. critic/reviewer prompt 什么条件下真提升、什么是表演？

## 调研问题（4 个，逐个回答）

### Q1: multi-stage agent pipeline 各阶段 prompt 贡献度

搜索方向：
- "LLM agent pipeline ablation" / "multi-step LLM workflow component importance"
- AutoGen / CrewAI / LangGraph 等框架的 ablation study
- 学术论文：ICLR/NeurIPS/ACL 2024-2025 中关于 agent pipeline 设计的 empirical study
- 重点找：有没有人系统性地测过"删掉 pipeline 第 N 步的 system prompt → 最终输出质量变化"

### Q2: critic/reviewer prompt 设计——真提升 vs 表演

搜索方向：
- Self-Refine (Madaan et al 2023), CRITIC (Gou et al 2024), LLM-as-judge 偏差
- "Does self-criticism actually improve LLM output?" 类实证研究
- 重点找：critic prompt 在什么条件下有效（任务复杂度？错误类型？）vs 什么时候只是增加 token 消耗不改善质量
- 已知偏差：position bias, verbosity bias, self-preference bias

### Q3: staged revision vs one-shot 效果对比

搜索方向：
- "iterative refinement LLM" vs "single-pass generation"
- Chain-of-Thought 的多轮 vs 单轮
- ReAct / Reflexion 类框架的 ablation（去掉 reflection step 后性能下降多少）
- 重点找：staged revision 的边际收益曲线（第 1 轮 revision 提升 X%，第 2 轮只提升 Y%）

### Q4: L1 组件级结论 → pipeline 阶段级的映射合理性

这是理论问题，不需要搜文献，但需要引用 Q1-Q3 的发现来论证：
- 如果文献表明 pipeline 各阶段贡献度高度不均（如 planning 阶段贡献 60%，execution 阶段贡献 10%），那我们的 L1 单组件消融结论外推到 pipeline 级时需要注意什么？
- 如果文献表明 critic 步骤在简单任务上无效但在复杂任务上有效，那我们的 decomp（最简任务类型）L1 结论对 pfb（复杂 pipeline）的预测力如何？

## 产出格式

```markdown
# T8 Part B: Pipeline Prompt 文献调研

> origin: ai · arena agent mode · 日期
> 来源数: N (≥2 独立)
> 覆盖: arXiv / GitHub / 学术会议

## Q1: Multi-stage pipeline 各阶段贡献度
[发现 + 来源 URL + conf]

## Q2: Critic/Reviewer prompt 有效性边界
[发现 + 来源 URL + conf]

## Q3: Staged revision vs one-shot
[发现 + 来源 URL + conf]

## Q4: L1→pipeline 映射合理性论证
[基于 Q1-Q3 的推理 + 局限声明]

## 对 T8 Part C 实验设计的启示
[哪些假设被文献支持/反驳，C3 paired runs 设计需要调整什么]

## 来源清单
| # | 标题 | 类型 | URL | 关键发现一句话 |
```

## 验收标准

1. 4 个问题全部有回答（找不到文献的明确说"未找到直接证据"，不编造）
2. ≥2 个独立来源（不同作者/机构）
3. 每条结论标 conf（0-1）
4. 来源 URL 可访问（非 paywall 优先；paywall 的标注）
5. 产出落盘 `experiments/T8-lit/lit-survey-pipeline-prompts.md` + commit+push

## 铁律

- 本任务域 = 文献调研，不涉及代码执行
- 只读网络（arXiv/GitHub/ACM/IEEE/Semantic Scholar），不读仓库其他文件
- 找不到就说找不到，不编造引用
- 产出必须可复现：列出搜索关键词 + 筛选标准
## 回执要求（Lead 验收门禁）

完成后必须 commit + push 到当前工作分支，并输出回执 JSON：
```json
{
  "repo": "https://github.com/dd2003-460/decomp-bench.git",
  "branch": "<你实际 push 的分支名>",
  "commit_sha": "<完整 sha>",
  "artifact": "experiments/T8-lit/lit-survey-pipeline-prompts.md",
  "sources_count": N,
  "observed_at": "<ISO 带时区>"
}
```
文件不存在 = 任务未完成。
