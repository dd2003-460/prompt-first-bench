# origin: ai — Ralph Loop 自主工作协议（goal-template 驱动）

> 本协议让执行 agent 在 pfb 仓库内**持续自主工作**：每个 goal 走完整 1-loop，收口后找下一个，直到被显式停止。

## 循环协议（每轮必走）

### 阶段 A：取 goal
0. **先 `git checkout main`**（防分支漂移），确认在 main 上再动作
   **runner 外包规则（2026-11-01 v3 · arena agent mode 执行层，替代本地 claude CLI）**：
   背景：claude CLI 背后也是本地 27b（经 ~/.claude-vllm-proxy → ninfer），跟 subagent 卡死同根——能力天花板不在壳。按 AGENTS.md 红线 1「外包核验与调研」+ skill `arena-outsource`，执行层一律走 LMArena agent mode（免费、多模型对战、可代干活）。
   - 从 `tasks/goal-queue.md` 取队首未完成 goal → 写 `tasks/current-goal.md`
   - **任务书先 push**：goal 任务书 commit+push 到本仓 `tasks/<T-id>.md`，派发 prompt 只写「读 tasks/<T-id>.md 按其中步骤执行」（不贴内容、不贴 clone 命令）
   - **ego-browser 提交 arena**（唯一通道，SOP 见 `.claude/skills/arena-outsource/SKILL.md`）：taskSpace 命名 `pfb-ralph-<goal短名>`，goto https://arena.ai/agent，填任务卡（自包含：目标一句话+约束+交付格式模板+长度≤50行+落盘硬约束「文件不存在=任务未完成」），waitForFunction 等回复落页（三档超时 30s/1min/3min，超 3min 进降级阶梯）
   - **大 goal 拆分优先**（m00656）：子领域正交拆 3-7 个，每个 ≤30min，并行 ≤3；arena 失败率高，调研类每子领域拆 2 个（主调研+交叉验证）
   - **汇报通道不变**：arena 产出由我（Lead）读取 snapshot 后写入 `tasks/BRIDGE-REPORT.md`（goal 短名+交付物路径+验收自检+一句话结论）——claude 时代它是工人自己写，现在是我收到 arena 结果后代写。我对账方式相同：cat 报告 + 查 ego-browser taskSpace 状态
   - **交叉验证门禁**（02.5/04.5）：同一 claim ≥2 独立回答（arena 内不同对战轮次各答一遍），回执 JSON 满足最低字段；矛盾点记录+核实
   - **降级阶梯**（逐级降，记录原因）：arena agent mode → arena Battle → ego-browser 直抓 → 本地自答（conf −0.2，标「arena 不可用 <日期> <原因>」）
   - 收口：我验证产出（跑断言/grep 关键数字）→ merge ralph/<goal短名> → push → 更新 queue → 同一回合取下一个 goal
1. 读 `tasks/goal-queue.md` → 取队首未完成的 goal；若队列空则自找：
   - 扫 `bench/self-opt-tester/bench.md` 已知缺陷清单 → 选产投比最高的未解决项
   - 扫 `tasks/*.md` 未完成的任务书回执
   - 扫 `git log --oneline -20` 找 "建议" / "下一步" / "待办" 类导出项
2. 按五字段格式写当前 goal（【目标】【阶段】【SOP 索引】【验收标准】【失败降级】），落盘 `tasks/current-goal.md`
3. **大 goal 拆解规则**：若 goal 带任务书且任务书内有「执行分解」（G1/G2/... 子 goal 列表），则把每个子 goal 当作独立 goal 逐个处理——子 goal 各自走完整 1-loop、各自 commit+push+merge、各自更新 queue（划掉当前子 goal、标注断点位置）。主 goal 在所有子 goal 完成后才标记完成。

### 阶段 B：执行 1-loop（六阶段一个不少）
4. 读 `loop/prompt-first/01..04.5` + `sop/arena-loop-pipeline.md`
5. 每阶段产出落盘 `loop-artifacts/stages/<N>/`（文件名带 goal 短名前缀防撞车）
6. 阶段判定 pass 才进下一阶段；04.5 反方复核必须做
7. **研究级质量线**（对标 goal-template 选题标准）：
   - 结论必须带 evidence（文件路径+行号 或 JSON path），不接受"我认为"
   - 负面结果明确声明（证伪的假设写出来，不藏着不美化）
   - 对照业界坐标系（gap-analysis 28 bench / ResearcherBench / RACE）定位自己的产出
   - 不做 trivial 修补凑数：每步要么推进核心问题，要么登记为 SKIP+理由

### 阶段 C：收口 + 找下一个
8. commit + push 到**你的新分支**（`ralph/<goal短名>`），ls-remote 验证落点
9. `git checkout main && git merge ralph/<goal短名> --no-edit && git push origin main`
10. 更新 `tasks/goal-queue.md`：划掉完成的 `[x]` + 日期 + 一句话结果，追加新导出的候选（≥1 个）
11. **同一回合内立即回到阶段 A 取下一个 goal**——无 goal = 停摆是违规
12. 重复 A→B→C，直到收到显式停止指令或 max-turns 耗尽

## 硬规则
- **始终在 main 上读 queue、开新分支干活、干完 merge 回 main**
- 一次一个 goal（大 goal 的子 goal 也是串行，一次一个）
- 每步产出可验证（文件/hash/分数），未达标不收口
- 冻结数据只读（hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-*）；要改必须开新文件 + APPROVALS.md 登记
- 不可逆操作（删数据/外发/花钱）→ 写 `APPROVALS.md` 跳过继续干别的，不阻塞
- 网络调研受限（无 ego-browser）→ 用仓库内已有材料（gap-analysis survey 28 条等）+ 标注 unverified，不虚构
- 每 3 个 goal 回读一次 bench.md 指标定义防漂移
- **工具调用纪律**：只用 Read/Write/Edit/Bash/Glob/Grep 基础工具；禁止使用任何需要特殊 content block 的工具（如 Task/subagent 派生）；所有子任务在当前会话内顺序完成
- **稳定性优先于速度**：宁可少做一个 goal 做扎实，不要赶进度留半成品。max-turns 快耗尽时优先收口当前 goal 而不是开新的
