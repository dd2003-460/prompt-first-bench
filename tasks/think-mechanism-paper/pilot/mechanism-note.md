# T4b Pilot 机制解读（subagent 分析，供 Lead 验收参考）

> origin: ai · 2026-11-26 00:52 · 非任务书交付物（任务书 3 文件之外），不改动 runs.json/results.md。
> 目的：回答"Δ(B−A) 由什么决定"，给论文写作（TMLR 审稿人必问）提前备好防御性解读。

## 观察

B−A 差异集中在 P1(+1)、P5(+1)，P2/P3/P4 持平（baseline 也满分）。

## 机制解读（两层）

1. **Δ 由 prompt 对目标结构的诱导程度决定，不由模板质量决定。**
   P2/P3/P4 的 prompt 原文本身就点名了目标结构（"Is there a single formula…"、"Turn this into a testable quantitative prediction"、"Audit … dimension by dimension"）→ baseline 自然满足 rubric，模板无增量。
   P1/P5 的 prompt 没点名关键结构项（"验证原解=特例"、"哪一步缺 ground truth"）→ 只有模板注入补齐。
   即：机械 rubric 测的是**模板短语复述率**，增量只出现在 prompt 未诱导的维度上。

2. **截断/长度混淆（重要 caveat）。**
   B 条件 system prompt 更长（5 条纪律）→ 输出更长 → 9/10 撞 1500 上限。B 的满分部分得益于模板短语出现在截断窗口内（模型倾向先回应 system 指令）；
   P1-A 被截断，无法排除其"special case"句本会出现在 1500 token 之后。P5-A 未截断仍 0 分，说明截断非唯一因素，但 B−A 差值中有"窗口位置"成分。

## 可检验预言（本轮未执行，超出任务书 10 次调用范围）

- **预言1**：把 P1/P5 的 prompt 改写为显式点名结构项（"verify binary search is a special case of the unified form" / "state which step lacks cheap ground truth"），baseline 应升至 1 分，B−A 坍缩至 0。
  成立条件：机制1 正确。失效条件：baseline 0 分源于能力而非诱导缺失（则改写 prompt 也救不回）。
- **预言2**：max_tokens 提到 4000（消除截断）后重跑，B−A 差值应收窄（长度混淆移除）。
  成立条件：机制2 正确。失效条件：差值不变 → 模板效应是真实的结构效应而非窗口效应。

两条预言都便宜（各 4-10 次本地调用），若 T4a 论文写作需要更强证据，优先跑预言2（直接回应"分数受截断污染"质疑）。

## 域核对

本解读所在域 = prompt 诱导 × 输出预算 × 关键词复述，与机械 rubric 实验同域；
"reward hacking"类比（模型优化关键词命中而非纪律执行）仅在局限性声明层面成立，不升级为主结论。
