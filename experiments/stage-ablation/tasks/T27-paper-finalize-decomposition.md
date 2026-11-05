# T27 论文定稿 — 分解树 + 缺口清单

> origin: ai · 2026-11-05 · goal T27-paper-finalize stage 00

## 分解树

```
T27 paper-draft.md 定稿（167行初稿 → 可投稿完整版）
├── A. 实验设计更新（§3）
│   ├── A1. 臂定义表：S0-S5 → S0,S1,S5,S6(fuzzy),S7(hybrid)
│   │     现状：只写了 S0-S5 cumulative；缺 S6/S7 独立臂
│   │     数据源：ablation_harness.py prompt 定义 + T17 report §S6/§S7
│   ├── A2. 评分维度表：M1-M6 → M1-M7（+M7 矛盾推理，weight 0.15）
│   │     现状：只有 M1-M6；缺 M7 定义和权重分配
│   │     数据源：scoring-v4-m7.md + T17 report §M7
│   └── A3. 执行参数：judge 描述更新（同族 27B + 异源 Arena GPT-5.5）
│         现状：写"heterogeneous cross-judge in progress"
│         数据源：T26 receipt + hetero-judge-s6s7-results.json
├── B. 结果更新（§4）
│   ├── B1. 主曲线表：加 S6/S7 列（per-question + mean）
│   │     数据源：/tmp/score-s6.json, /tmp/score-s7.json, T17 report 表格
│   ├── B2. 新增 §4.X "Fuzzy vs Mechanical"（S6/S7 核心发现）
│   │     - S6 > S0 (+0.065)：模糊触发训练过的推理模式
│   │     - S7 ≈ S5 total 但赢 Q1/Q2：hybrid 捕获覆盖+深度
│   │     - M7 反直觉：机械 prompt 降低矛盾推理（S1=0.256 < S0=0.306）
│   │     - 结论：最优 prompt 风格是 question-type-dependent
│   ├── B3. 新增 §4.Y "Hetero-Judge Validation"（T26 结果）
│   │     - Arena M1/M4 vs 本地 27B：排序一致，arena 偏高 ~0.15
│   │     - self-bias 方向 = 压分（不改变相对排序）
│   │     - r1/r2/r3 逐字相同限制（非独立样本）
│   └── B4. M7 维度分解表（per-arm per-question）
│         数据源：scoring-v4-m7.md 全量表
├── C. 讨论更新（§5）
│   ├── C1. §5.1 Tool Access Hypothesis → 保留，补充 S6/S7 视角
│   │     （fuzzy prompt 激活已有知识 vs tool access 获取新知识——正交互补）
│   ├── C2. §5.2 Implications → 加第 5 条："prompt style should be adaptive"
│   │     （data+depth→S7, pure concept→S6, pure retrieval→S5）
│   ├── C3. §5.3 Limitations → 更新：
│   │     - 异源 judge 已完成（不再是 in progress）
│   │     - 新局限：r1/r2/r3 输出相同（harness 未加 temperature 扰动）
│   │     - 新局限：arena 未暴露模型名（unverified）
│   └── C4. Related Work → 加 ScientistTwo 对比段（定位差异：选手 vs 裁判）
├── D. 摘要+结论重写（Abstract + §6）
│   ├── D1. Abstract：加 S6/S7 发现 + 异源验证 + M7
│   └── D2. Conclusion：从"tool access is king"扩展为
│         "tool access + adaptive prompt style + honest self-assessment (M7)"
└── E. 格式收口
      ├── E1. References 补全（ScientistTwo arXiv:2609.19644, DREAM ACL 2026 等）
      ├── E2. 全文数字交叉核验（report vs draft 一致性）
      └── E3. commit + push pfb main
```

## 缺口清单

| 子项 | 缺什么 | 来源 | 状态 |
|------|--------|------|------|
| A1 | S6/S7 prompt 原文（~300c / ~2.6k） | ablation_harness.py | ✅ 已有 |
| A2 | M7 权重分配理由 | scoring-v4-m7.md | ✅ 已有 |
| A3 | Arena 模型名 | T26 receipt | ⚠️ unverified（标注即可） |
| B1 | S6/S7 per-dim 分数 | /tmp/score-s6.json, score-s7.json | ✅ 已有 |
| B2 | S6/S7 关键发现 | T17 report §S6/§S7 | ✅ 已有 |
| B3 | T26 异源分数 | hetero-judge-s6s7-results.json | ✅ 已有 |
| B4 | M7 per-arm 表 | scoring-v4-m7.md | ✅ 已有 |
| C4 | ScientistTwo 对比 | scientisttwo-comparison.md | ✅ 已有 |
| D1-D2 | 无外部依赖 | — | 纯写作 |
| E1 | 引用列表完整性 [待核验] | 需逐条核对 arXiv/ACL 编号 | 执行时核 |
| E2 | 数字一致性 [待核验] | draft vs report 逐表对 | 执行时核 |

## 正交性自检

- A/B/C/D/E 之间：A=设计(输入)、B=结果(数据)、C=讨论(解释)、D=摘要(浓缩)、E=格式(收尾) → 正交 ✓
- B1/B2/B3/B4：主曲线/新发现/异源验证/M7分解 → 四个不同证据面 → 正交 ✓
- 完备性：paper-draft.md 的每个 section（Abstract/Intro/RelatedWork/Design/Results/Discussion/Conclusion/Refs）都有对应子项 → 完备 ✓

## 任务表（执行顺序）

| # | 任务 | 产出 | 估时 |
|---|------|------|------|
| 1 | A+B+C+D 一次性重写 paper-draft.md | 完整草稿 v2 | 主要工作量 |
| 2 | E1 引用核验 | references 完整 | 10min |
| 3 | E2 数字交叉核验 | 一致性确认 | 10min |
| 4 | E3 commit+push | pfb main 新 commit | 2min |