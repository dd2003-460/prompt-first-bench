# T30: Tool-Access Experiment (decomposition)

## 分解树

- A. Research Hook 修复（基础设施）
  - A1. KNOWN_SITES 修正：Q2→HF Leaderboard/Artificial Analysis；Q4→Lost in the Middle/Anthropic eval
  - A2. arXiv 多查询策略：每个 Q 用 2-3 个精准 query 取并集，而非单一宽泛 query
  - A3. 验证：5 个 Q 各跑一次 research_hook，人工检查相关性 ≥3/5
- B. S7+tools 实验设计
  - B1. 新臂定义：S7T = S7 hybrid prompt + research_hook sources 注入（同 S2-S5 的 inject_sources_into_prompt）
  - B2. 参数：n=5Q × 3reps, temp=0.1+seed（同 S7）, max_tokens=8000
  - B3. 评分：M1-M6 (27B judge) + M7 (rule-based)，同现有 pipeline
- C. 对比分析
  - C1. S7 vs S7T per-dim delta（重点 M1 事实覆盖、M4 缺口识别、M6 引用可验证性）
  - C2. 按题型分组：data-intensive (Q1/Q2) vs conceptual (Q5) vs contradiction (Q4)
  - C3. 结论：tool access 的边际贡献是否因题型而异？是否兑现 §5.1 "tool-access hypothesis"？
- D. 论文更新
  - D1. 新增 §4.6 "Tool-Access Ablation" 小节
  - D2. 更新 §5.1 discussion（从假设变为实证）
  - D3. 更新 limitations（M6 不再 structurally zero for S7T）

正交性自检：A(基础设施) / B(实验执行) / C(分析) / D(写作) — 顺序依赖 A→B→C→D，内部无交叉 ✓
完备性：回答成璐问题"优化应用+实测"= 修复检索质量(A) + 量化 tool access 效果(B/C) + 论文落地(D) ✓

## 缺口清单

| 子项 | 缺什么 | 来源 | 状态 |
|------|--------|------|------|
| A1 | Q2/Q4 的正确直访站点 URL 可达性 | ego-browser _fetch_page 测试 | [待核验] HF Leaderboard SPA 可能返回空内容 |
| A2 | arXiv 多查询的 query 措辞影响结果质量 | 实测对比 | [待核验] "Qwen2.5-Coder HumanEval" 能命中 tech report，但 GLM/Mistral 无对应 arXiv paper |
| B1 | S7T prompt 中 sources 注入位置是否干扰 hybrid 结构 | dry-run 检查 | [待核验] inject_sources 插在"工具说明"后，S7 无此 marker → fallback 追加末尾 |
| B2 | 运行时间估算 | S7 单次 ~15s × 15 runs + research ~30s/run | 预计 ~15 min |
| C1 | S7 baseline 分数已有（T28-fix 后） | /tmp/score-s6s7-rerun.json | ✓ 已有 |
| C3 | tool access 对 M7 的影响（预期无影响，需验证） | 实验 | [待核验] |
| D1 | 论文新增小节的长度控制（不超 1 页） | 写作时判断 | — |

## 任务表

| # | 动作 | 验收 |
|---|------|------|
| 1 | 修 KNOWN_SITES + 多查询策略 | 5Q 各 ≥3/5 relevant sources |
| 2 | harness 加 S7T arm（build_prompt + run_arm 支持） | dry-run 通过，prompt 含 sources block |
| 3 | 跑 15 runs (S7T-Q1..Q5-r1..r3) | 15/15 JSON 落盘，无 error |
| 4 | 打分 M1-M7 | score JSON 生成 |
| 5 | 对比分析 + 论文 §4.6 写入 | per-dim delta 表 + 结论段 |
| 6 | commit + push | git log 确认 |