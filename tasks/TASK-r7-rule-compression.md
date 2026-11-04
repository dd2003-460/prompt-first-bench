# origin: ai — R7 任务书：规则压缩（P1）

> 派发目标：LMArena agent（pfb 仓库，复用既有会话）
> 本任务只涉及 prompt-first-bench/main，忽略历史中其他仓库的消息。
> 背景：R6 P0（阶段门控加载）完成，Model A M1=78.2（达标），Model B M1=62.0（差 8 分）。
> 本任务实施 P1（规则压缩），目标 Model B M1 ≥ 70。

## 【强制段】
你是 LMArena agent，工作仓库 = dd2003-460/prompt-first-bench，分支 main。先 `git pull` 到最新（commit 1a79bc2）。
严格按本任务书步骤执行，产出落盘路径见【交付物】。任何通道故障报告 Lead，不得静默跳过、不得伪造数据。
完成后回执必须含 repo URL + branch + commit_sha + 自报模型身份（如可知）。

## 【目标】
压缩 loop 规则文件 + SOP，使单会话累计规则负载从 11,011 → < 7,500 o200k tok，
从而使 Model B 的 R 分量从 0.479 → ≥ 0.65，M1 从 62.0 → ≥ 70。

## 【背景】≤10行
- R6 发现：单会话走完 6 阶段后，末态规则负载 11,011 tok（仅比 baseline 12,086 省 8.9%）
- Model B M1=62.0，缺口 8 分，主要瓶颈是 R 分量（0.479 vs Model A 的 0.833）
- 当前文件实测（o200k）：
  - 核心 7 文件合计 ~6,342 tok
  - examples 7 文件合计 ~4,211 tok
  - INDEX.md 458 tok
  - SOP (arena-loop-pipeline.md) ~2,541 tok（R6 计量）
  - 总计 ~13,552 tok（全量注入时）
- 压缩目标：保持 hard constraints 完整，删除冗余解释/重复示例/过时内容
- 验收：压缩后跑 check-route-coverage.py 必须 exit 0（无漏载）

## 【执行分解】

### Step 1: 审计可压缩空间（~30 min）
对每个文件做逐段审计，标注：
- **KEEP**：hard constraint / 门禁条件 / 不可省略的操作指令
- **COMPRESS**：可缩短的解释/背景（保留核心，删冗余）
- **CUT**：纯示例/重复/过时内容（可整段删除或移到 references/）
- **MERGE**：跨文件重复段落（合并到一处，另一处引用）

输出：`bench/self-opt-tester/runs/r7/compression-audit.md`

### Step 2: 执行压缩（~60 min）
按审计结果修改文件：
- 优先压缩最大文件：SOP (2,541) > 01-goal-decomposition (1,755) > 02-information-research (1,237)
- examples 层：每个文件保留 top-1 最典型示例，其余移到 `loop/prompt-first/examples/archive/`
- 目标：核心文件总量 ≤ 4,000 tok，examples 总量 ≤ 2,000 tok
- **纪律**：每改一个文件，跑 `python3 bench/self-opt-tester/runs/r6/check-route-coverage.py` 确认 exit 0

### Step 3: 验证（~20 min）
- 跑 `node bench/self-opt-tester/runs/r6/count-rule-tokens.js --json` 测量压缩后总量
- 跑 `python3 bench/self-opt-tester/runs/r6/check-route-coverage.py` 确认无漏载
- 计算新的 Model B M1（用 run6-m1-score.json 的公式，替换 R 分量的 x 值）
- 如果 M1 < 70 → 继续压缩直到达标或确认天花板

### Step 4: 写报告（~15 min）
`bench/self-opt-tester/runs/r7/r7-compression-report.md`：
- 压缩前后对比表（逐文件）
- Model B M1 新分数
- 是否达到验收标准（M1 ≥ 70）
- 遗留问题（如有）

## 【交付物】（均在 pfb 仓库内）
- 压缩后的 `loop/prompt-first/*.md`（git diff 可见变化）
- 压缩后的 `sop/arena-loop-pipeline.md`
- `loop/prompt-first/examples/archive/`（被移出的示例）
- `bench/self-opt-tester/runs/r7/compression-audit.md`
- `bench/self-opt-tester/runs/r7/r7-compression-report.md`
- 回执：repo URL + branch(main) + 最终 commit_sha + 自报模型身份

## 【失败降级】
- 如果压缩后 check-route-coverage.py FAIL → 回滚该文件，记录原因
- 如果 M1 仍 < 70 → 如实报告，给出"还需压缩多少 tok"的估算
- 不要为了凑数而删除 hard constraints

## 【给 Lead 的备注】
- 边界：本任务只做 P1（压缩），不改 harness 行为
- 压缩原则：宁可少压不可错压——hard constraint 丢了比 token 多更严重
- 下一步归属：Lead 收到 r7 数据后更新 bench 权重校准（n=7）+ 判断是否需要 P2
