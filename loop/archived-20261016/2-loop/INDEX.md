# 2-loop — 执行与 Review（精简版）

> 取消 6 阶段划分。每个子任务执行一个固定循环：
> **backup → execute → review/verify → commit**

## 不再存在的阶段

- ~~01-pre-check~~ → 并入 per-step 开头
- ~~02-backup~~ → 保留为 per-step 第一步
- ~~03-execute~~ → 保留为 per-step 第二步
- ~~04-verify~~ → 拆分为 Review + 交叉验证
- ~~05-confidence~~ → 砍掉。Review 通过=成功，不通过=失败，不评分
- ~~06-decision~~ → 砍掉。结果只分通过/不通过，不通过则分解修复

## Per-Step 固定流程

每个子任务独立执行以下循环，**每一步完成后必须等待验证通过才能进入下一步**：

```
Step 0: 前置检查（前置子任务产出存在、输入数据可用）
Step 1: git backup（commit 执行前状态，带子任务ID标记）
Step 2: execute（按 plan.md 执行子任务）
Step 3: review/verify（根据任务类型调用不同验证手段）
Step 4: 交叉验证（所有 review 必须经网页 LLM 交叉确认）
Step 5: 判定
  - 通过 → commit + 标记完成，允许依赖本任务的后续任务启动
  - 不通过 → 分解修复任务 + 重新规划修复方案
```

## Review/验证矩阵

| 任务类型 | Review 方式 | 交叉验证方式 | 通过标准 |
|----------|-------------|--------------|----------|
| **code** | 直接运行测试/单元测试/功能验证 | 网页 LLM review 代码逻辑、边界条件 | 测试通过 + LLM 确认逻辑正确 |
| **paper/writing** | 传文件给网页 LLM 评审 | 人工审阅关键论点 | LLM 评审无异议 + 关键论点人工确认 |
| **data_prediction** | 用实际数据/已知结果验证预测 | 网页 LLM 评估方法论合理性 | 误差在预期范围内 + LLM 确认方法合理 |
| **research** | 结论与外部信息交叉验证 | 网页 LLM 评估逻辑完整性 | 无矛盾发现 + LLM 确认论证链完整 |
| **other** | 按任务性质定义验证方式 | 网页 LLM 交叉确认 | 达到任务定义的成功标准 |

## 交叉验证规则

1. **所有 Review 必须包含网页 LLM 交叉验证**（纯代码测试是例外，但推荐也做 LLM 逻辑 review）
2. 交叉验证方式：将任务产出 + Review 结果 + 关键疑点发送给网页大模型
3. 网页 LLM 的结论：
   - `PASS`: 确认 Review 结果可信 → 执行 commit
   - `FAIL`: 发现 Review 遗漏的问题 → 进入修复分解
   - `UNCERTAIN`: 信息不足无法判定 → 标记 `blocked_human`，跳过当前任务并继续队列

### 网页 LLM 交叉验证技能

**`gpu-web-cross-verify`** — 专为 GPU 调研项目设计的多源核验流程（web_fetch/browser 多源交叉验证）

- **触发**：硬件规格、价格、兼容性等关键事实验证
- **方法**：≥2 个独立来源一致才标记 verified，记录来源 URL/日期/置信度/核验状态
- **位置**：`~/.hermes/skills/gpu-web-cross-verify/SKILL.md`
- **集成**：在 2-loop Step 4 (交叉验证) 中调用，替代手动网页搜索
- **报告输出**：`loop-artifacts/verification-reports/YYYY-MM-DD-{fact-slug}.json`

### 人类确认门（UNCERTAIN 时）

当交叉验证返回 UNCERTAIN 时，当前子任务进入 `blocked_human`，但 Commander **不得等待并阻塞整个循环**：

```
[人工确认 — 不确定状态]
───────────────────
任务 ID: {task-id}
任务类型: {task-type}
Review 结果: {review-result}
交叉验证结果: UNCERTAIN
关键疑点: {issues}

请在人类方便时决定：
- APPROVE → 视为 PASS，继续执行
- REJECT → 视为 FAIL，进入修复分解
- COMMENT → 给出指导意见，代理根据意见重新执行
───────────────────
```

**注意**：
- 当前子任务等待确认，其他 ready 任务继续执行
- 如果没有 ready 任务，进入 exploration 并生成 candidate tasks
- 其余情况（PASS/FAIL）全部自主处理，不等待人类

## 失败修复流程

```
Review 不通过 → 分解修复任务 → 重新规划 → 回到 per-step 循环
```

具体规则：
1. **不允许原地重试同一方案** — 必须先分解修复任务
2. 修复分解为子子任务（T1.1, T1.2...），每个子子任务也走完整 per-step 循环
3. 修复方案写入 `<project>/fix-plan.md`（包含修复意图、方案、Review 策略）
4. 修复后的产出使用新 revision 关联原产出；失败中间态保存在 `loop-events.md` 和 artifact
5. **修复也需交叉验证** — 修复方案本身也通过网页 LLM 确认合理性
6. **修复任务遵守多层分解规则**：
   - 不设置固定的计划修订次数或 DAG 深度上限
   - 每一层必须声明输入、输出、条件和依赖
   - 同一并行层级必须正交且无写入冲突
   - 如果无法继续分解，标记原因并转入 `blocked_human` 或 `exploration`

## Git 备份规则

- 每次 execute 前必须 `git commit -m "[2-loop] backup: <task-id> pre-execution"`
- 每次 commit 前必须 `git commit -m "[2-loop] commit: <task-id> completed"`
- 修复任务的 backup 标记为 `[2-loop] backup: <task-id> fix`
- backup 失败不影响执行，但记录到日志

## 输出

每个子任务完成后，更新 `<project>/plan.md` 中的任务状态：

```markdown
## 6. 子任务 DAG（执行后更新）

- **T1**: [COMPLETED] → 产出: output.md
  - Review: PASS (LLM cross-validate: PASS)
  - 执行时间: 2026-07-13T20:30:00
  - 失败次数: 0

- **T2**: [IN_PROGRESS] → 产出: draft.md
  - Review: FAIL → 已分解修复 [T2.1, T2.2]
  - 修复方案: fix-plan.md
  - 失败次数: 1
```
