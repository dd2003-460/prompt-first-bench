# origin: ai — Ralph Loop 自主工作协议（goal-template 驱动）

> 本协议让执行 agent 在 pfb 仓库内**持续自主工作**：每个 goal 走完整 1-loop，收口后找下一个，直到被显式停止。

## 循环协议（每轮必走）

### 阶段 A：取 goal
0. **先 `git checkout main`**（防分支漂移），确认在 main 上再动作
   **runner 桥接规则（Hermes stop-hook 驱动模式）**：当本会话由 Hermes stop-hook 唤醒且消息含「ralph loop runner」或指向本协议时，执行者 = Hermes agent 本人（不是 claude CLI）：
   - 从 `tasks/goal-queue.md` 取队首未完成 goal → 写 `tasks/current-goal.md`
   - 用 terminal 工具派发 claude 执行该 goal：
     `claude -p "git checkout main。读 tasks/ralph-loop-runner.md 和 <goal任务书路径>，执行 <goal短名>，走完整 1-loop 六阶段，commit+push 到你的新分支 ralph/<goal短名>。" --dangerously-skip-permissions --max-turns 200`
     （background=true, notify=true；prompt 保持单段、无角色前缀、≤3 个文件引用——复杂多段 prompt 会触发 API 400 tool_reference）
   - 轮询验证（每 5-8 min 一次）：`git log --oneline main..HEAD` + `find loop-artifacts/stages/ -name "*<goal前缀>*"` + `ps aux | grep "[c]laude -p" | wc -l`
   - claude 收口后（进程退出或 max-turns 耗尽）：我验证产出（跑断言脚本/grep 关键数字）→ merge 回 main → push → 更新 queue（划掉+结果注记+追加新候选）
   - **同一回合内立即取下一个 goal 重复上述流程**——stop-hook 会在每次我想停时把我拽回来，所以「回合结束」不是终点
   - 若 claude 进程死亡（API error/卡死）：检查 /tmp/ralph-loop-r*.log 定位原因，简化 prompt 重试一次；仍失败则登记边界后跳过该 goal 取下一个
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
