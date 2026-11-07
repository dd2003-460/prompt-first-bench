# 中期目标规划：PFB-APPLY（可应用 + 真实泛化 + 打赢开源）

> origin: ai · 2026-11-07 早 · 成璐指令「和subagent用人话商量一个中期目标」
> 状态：decomp 落盘，待 subagent 讨论轮 + arena 派发

## 0. 用户原话（意图锚点）

「我希望到时候看到的是最终可以应用而且真实泛化也能打赢开源的pfb!（当然别忘了隔离下先跑出类似gold的效果喔）」

拆成四个验收面：**A 可应用**（能当工具用）、**B 真实泛化**（没见过的题也行）、**C 打赢开源**（对 GPT Researcher 有统计显著优势）、**D 先隔离跑出 gold 级效果**（前置条件）。

## 1. 现状盘点（全部来自本轮工具输出）

| 资产 | 状态 | 证据 |
|------|------|------|
| S5 (六阶段流水线+记忆hook) | n=30/arm, mean 0.7907 [0.764,0.816] | scoring.md @673760a |
| S0/S1 baseline | 0.5558 / 0.5746，S1 无显著增益 p=0.856 | stats-n30.json |
| D1 = GPT Researcher pipeline | **今天刚补分**：mean 0.602 (n=5, 1rep/Q) | runs/d1-score-draft.md |
| Gold trees Q1-Q5 | 已建（bench/rubric-v3/ablation/gold-tree.md 31节点 + gold/Q*.md） | T40/T41/T42/T48 任务卡 |
| S10 组合臂 (人话reviewer/讲原因/soothe) | 90 runs 跑完，FAIL计数修正 v2，未异族打分 | s10-runs/ @d20d4b0 |
| HBM hook fix | committed 未验证 | 9b2f25d |
| T30 (emotion/motivation) | arena 侧运行中，分支无新 commit | origin/arena/071ab5cb-* |

**关键发现（今天）**：D1 终于有了分数。S5 (0.7907) vs D1 (0.602) Δ+0.189——方向对了，但 D1 只有 1rep/Q 且 duckduckgo 无 key 检索是下限配置，这个差值还不能宣称。这是 C 面的真正起点，不是终点。

## 2. 分解树（正交子项）

```
PFB-APPLY
├── D. Gold 复现门禁（前置，隔离环境）
│   ├── D1. 选 2 道新题（Q6/Q7，训练集外，防泄漏）
│   ├── D2. pfb 全流程（六阶段+hook）盲跑新题，产出分解树
│   ├── D3. 人工/异族 judge 对照 gold 标准打分：达到 gold 级阈值？
│   └── 缺口：新题的 gold tree 需要独立构建（T48 双gold 路径复用）
├── B. 泛化测试（2026-11-07 修订：范围限定 AI/ML 域内）
│   ├── B1. 子领域扩展：AI/ML 域内加 3-5 道新题（不同子领域：如 LLM 评估方法、多模态架构、RLHF 流程），验证 pfb 在域内的泛化性
│   ├── B2. ~~模型泛化~~ [砍掉，报告声明"结论限定 27b 家族"]
│   ├── B3. 评分器泛化：rubric-v3 在新题上 κ≥0.6（双judge）
│   └── 缺口：新题 gold 构建成本 ~每题半天；D-face 跨域 FAIL 已定性为模型天花板，不再作为 B 面阻塞项
├── C. 打赢开源（统计硬化）
│   ├── C1. D1 扩 rep：5 题 × 3rep = 15 runs（消除 1rep 方差盲区）
│   ├── C2. 检索对齐：D1 换 Tavily/SerpAPI key 或同等质量检索器（现在 duckduckgo 是下限）
│   ├── C3. 配对检验：S5 vs D1 per-question paired sign test + bootstrap CI
│   ├── C4. 分项归因：M1-M6 哪一维拉开差距（预期 M4 缺口识别 + M5/M6 核验维度）
│   └── 缺口：检索 API key 预算 [待核验: 免费额度是否够 15 runs]
├── A. 可应用（产品化最小闭环 · 范围限定 AI/ML 域）
│   ├── A1. CLI 入口：`pfb ask "问题"` → 六阶段流水线 → markdown 报告+来源表（适用域：AI/ML）
│   ├── A2. 三道闸内置：矛盾检测/citation check/缺口标注默认开
│   ├── A3. 回执落盘：每次 run 自动写 receipt（可审计）
│   ├── A4. 文档：README 从实验仓库变成工具仓库的样子，明确声明适用域
│   └── 缺口：CLI 与 ablation_harness 解耦设计（harness 是实验脚手架，不能直接当产品入口）
└── Q. 质量门（贯穿所有子项）
    ├── Q1. 异族 judge：battle 通道 ≥3 家族，κ≥0.6 才出结论
    ├── Q2. fabrication 抽查：URL/数字 spot-check，不看语气
    ├── Q3. 全轮次文本保留（R1-R4），可复现
    └── Q4. 自评只做相对参考，conf cap 0.7，不对外宣称
```

## 3. 缺口标注汇总

| 缺口 | 阻塞谁 | 怎么补 |
|------|--------|--------|
| 新题 gold tree（Q6/Q7+） | D, B | T48 双gold 路径，arena 外包建树 |
| 第二模型家族 endpoint | B2 | 查 LM Studio 本地可用模型；没有就降级为单模型+声明 |
| 检索 API key/免费额度 | C2 | 先算 15 runs 的调用量，再决定白嫖还是小额付费（写 APPROVALS） |
| CLI 与 harness 解耦 | A1 | 设计评审：哪些函数复用、哪些重写 |
| S10 异族打分 | Q（S10 结论冻结前） | battle 通道，材料已齐（90 runs） |

## 4. 执行顺序（产投比排序 · v2 修订，吸收 subagent 意见）

1. **Q1 异族 judge 校准**（battle 通道对现有 S5/D1 35 runs 复评）— 评分器是单点风险，κ≥0.6 过了才信后续所有分数。不达标先修 rubric。[subagent Q4: 从第3位提到第1位]
2. **C2 检索对齐可行性判断**（duckduckgo→Tavily/SerpAPI 免费额度够不够 15 runs）— 决策点前置，避免 C1 白跑。[subagent Q2: 从最后提到第2位]
3. **C1+C3**（D1 扩 rep + 配对检验）— 在 C2 决策后开跑，~2h 本地
4. **D1-D3**（新题 gold 复现门禁）— arena 外包建树+本地盲跑，与 C1 并行
5. **B1+B3**（题目域扩展 + 评分器泛化）— ~~B2 模型泛化~~ [subagent Q1/Q5: 砍掉，报告声明"结论限定 27b 家族"]
6. **A1-A4**（CLI 产品化）— 最后做，前面都是它的弹药

### D3 验收标准量化 [subagent Q3 修正]
- pfb 盲跑输出 vs gold tree：节点级 Jaccard 覆盖率 ≥ 0.70（从已有 gold 对比数据取分位数）
- M4/M5/M6 三维度各自 ≥ 0.65
- 双 judge 分差 ≤ 0.10，超了走仲裁

## 5. 给 subagent 的讨论任务（用人话）

见 tasks/PFB-APPLY-subagent-discussion.md —— 让它挑毛病：哪个子项是伪需求、哪个顺序错了、哪个验收标准不可机器检查。
