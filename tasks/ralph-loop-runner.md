# origin: ai — Ralph Loop 自主工作协议（goal-template 驱动）

> 本协议让执行 agent 在 pfb 仓库内**持续自主工作**：每个 goal 走完整 1-loop，收口后按 find-goal SOP 找下一个，直到被显式停止。

## 循环协议（每轮必走）

### 阶段 A：取 goal
1. 读 `tasks/goal-queue.md`（若存在且非空）→ 取队首 goal；否则按 find-goal SOP 自找：
   - 扫 `bench/self-opt-tester/bench.md` 已知缺陷清单 → 选产投比最高的未解决项
   - 扫 `tasks/*.md` 未完成的任务书回执
   - 扫 `git log --oneline -20` 找 "R5.2 建议" / "下一步" / "待办" 类导出项
2. 按 `sop/goal-template.md` §1 五字段格式写当前 goal（【目标】【阶段】【SOP 索引】【验收标准】【失败降级】），落盘 `tasks/current-goal.md`

### 阶段 B：执行 1-loop（六阶段一个不少）
3. 读 `loop/prompt-first/01..04.5` + `sop/arena-loop-pipeline.md`
4. 每阶段产出落盘 `loop-artifacts/stages/<N>/`（文件名带 goal 短名前缀防撞车）
5. 阶段判定 pass 才进下一阶段；04.5 反方复核必须做

### 阶段 C：收口 + 找下一个
6. commit + push 到你的分支，ls-remote 验证落点
7. 更新 `tasks/goal-queue.md`：划掉完成的，追加新导出的候选（≥1 个）
8. **同一回合内立即回到阶段 A 取下一个 goal**——无 goal = 停摆是违规
9. 重复 A→B→C，直到收到显式停止指令或 max-turns 耗尽

## 硬规则
- 一次一个 goal，干完再找下一个（goal-template §3）
- 每步产出可验证（文件/hash/分数），未达标不收口
- 不可逆操作（删数据/外发/花钱）→ 写 `APPROVALS.md` 跳过继续干别的，不阻塞
- 网络调研受限（无 ego-browser）→ 用仓库内已有材料 + 标注 unverified，不虚构
- 每 3 个 goal 回读一次 bench.md 指标定义防漂移
