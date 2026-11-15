# origin: ai — R6 任务书：Arena 通道 Token 重发优化（阶段门控加载）

> 派发目标：LMArena agent（pfb 仓库，复用既有会话）
> 本任务只涉及 prompt-first-bench/main，忽略历史中其他仓库的消息。
> 背景：R5.5 bench 发现 run2 (arena) M1=25，根因 = 每轮全量重发 12,086 o200k tokens 规则负载。
> 本任务实施 P0 方案（阶段门控加载），目标 M1 ≥ 70。

## 【强制段】
你是 LMArena agent，工作仓库 = dd2003-460/prompt-first-bench，分支 main。先 `git pull` 到最新。
严格按本任务书步骤执行，产出落盘路径见【交付物】。任何通道故障报告 Lead，不得静默跳过、不得伪造数据。
完成后回执必须含 repo URL + branch + commit_sha + 自报模型身份（如可知）。

## 【目标】
实施"阶段门控加载"优化：修改 arena 任务书模板，让 agent 按当前阶段只加载需要的 loop 文件（而非全量 7 个），
降低单 turn 规则负载从 12,086 → ~3,700 o200k（降低 69%），然后跑 1 个完整 9 步 run 验证效果。

## 【背景】≤10行
- 问题：run2 每轮重发全部 7 个 loop 文件 + SOP = 12,086 o200k tokens
- T=30 turns 时总规则重发 ≈ 362,580 tokens（仅规则部分）
- M1 量化公式：M1 = 100 × (0.4×S + 0.35×R + 0.25×G)
  - S (切分完整率): 有 per-request 日志且可切分到 run 窗口 → 1.0
  - R (规则重发惩罚): 每轮 ≤ 首次 10% → 1.0; 全量重发 → 0.0
  - G (膨胀比): last/first ≤ 1.5x → 1.0; ≥ 5x → 0.0
- run2 当前：S=0.0, R=0.0, G=0.57 → M1=14.3（量化值）/ 25（人工评分）
- 目标：通过阶段门控让 R ≥ 0.7，S ≥ 0.5，G ≤ 2.5x → M1 ≥ 70

## 【执行分解】

### Step 1: 创建路由文件（~30 min）
在 `loop/prompt-first/` 下创建 `INDEX.md`（~500 bytes），内容：
```markdown
# Loop 阶段路由表

| 当前阶段 | 需要读取的文件 |
|---------|--------------|
| 01-goal-decomposition | 00-common-review.md, 01-goal-decomposition.md, 02-information-research.md |
| 02-information-research | 00-common-review.md, 02-information-research.md, 02.5-cross-check.md |
| 02.5-cross-check | 00-common-review.md, 02.5-cross-check.md, 03-action-decomposition.md |
| 03-action-decomposition | 00-common-review.md, 03-action-decomposition.md, 04-execution-verification.md |
| 04-execution-verification | 00-common-review.md, 04-execution-verification.md, 04.5-final-review.md |
| 04.5-final-review | 00-common-review.md, 04.5-final-review.md |

**纪律**：每次进入新阶段前，先读 INDEX.md 确定需要哪些文件，只读那些文件。不要一次性读全部 7 个。
```

### Step 2: 修改任务书模板（~30 min）
找到 arena 任务书模板（可能在 `tasks/` 或 `bench/` 下），修改规则注入部分：
- **旧**：贴全量 7 个 loop 文件 + SOP
- **新**：只贴 INDEX.md + 当前阶段的 2-3 个文件
- 添加指令："进入下一阶段前，重新读 INDEX.md 确定需要哪些文件"

### Step 3: 跑对照 run（~60 min）
用修改后的任务书模板跑 1 个完整的 9 步 run（与 run2 相同的任务类型），记录：
- 每个 turn 的 input token 数（如果 arena 暴露的话）
- 或者：从本地日志提取 per-request 序列
- 计算 S/R/G 三个分量
- 用 M1 量化公式算出 M1 分数

### Step 4: 对比分析（~15 min）
写一份简短报告：
- run2 (baseline): M1=25, S=0.0, R=0.0, G=0.57
- run6 (optimized): M1=?, S=?, R=?, G=?
- 改善幅度：ΔM1 = ?
- 是否达到验收标准（M1 ≥ 70）？

## 【交付物】（均在 pfb 仓库内）
- `loop/prompt-first/INDEX.md`（路由文件）
- 修改后的任务书模板（commit diff）
- `bench/self-opt-tester/runs/r6/run6-token-analysis.md`（token 消耗分析）
- `bench/self-opt-tester/runs/r6/run6-m1-score.json`（M1 量化打分）
- 回执：repo URL + branch(main) + 最终 commit_sha + 自报模型身份

## 【失败降级】
- 如果 arena 不暴露 per-request token 数据 → 用字节数估算（o200k tokenizer），标注 conf=0.5
- 如果 run 中途失败 → 停在当前步骤，回执注明完成到哪一步
- 如果 M1 < 70 → 如实报告，不要凑数

## 【给 Lead 的备注】
- 边界：本任务只做 P0（阶段门控），不做 P1（规则压缩）——如果 P0 效果不够，Lead 再决定
- 下一步归属：Lead 收到 run6 数据后更新 R5.5 bench 的权重校准（n=6）+ 判断是否需要 P1
