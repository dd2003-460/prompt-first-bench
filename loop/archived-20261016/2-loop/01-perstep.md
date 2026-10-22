# 2-loop — Per-Step 执行规范

> 每个子任务严格按此流程执行：backup → execute → review → 交叉验证 → commit

## 执行流程

对 plan.md 中的每个子任务，按依赖拓扑序依次执行：

### 1. 前置检查

- 依赖子任务已完成？依赖 → 继续；未完成 → 跳过或等待
- 输入文件存在？不存在 → 标记 BLOCKED，记录原因
- 通过 → 继续

### 2. Git Backup

```bash
git add -A
git commit -m "[2-loop] backup: <task-id> pre-execution"
```

### 3. Execute

按 plan.md 中定义执行子任务，产出到定义的文件路径。

### 4. Review/Verify

根据任务类型选择验证方式：

**code** → 运行测试套件（pytest/单元测试/功能验证）
**paper/writing** → 全文传给网页 LLM 评审（逻辑连贯性、论据充分性、结构合理性、语言表达）
**data_prediction** → 用实际数据/已知基准验证预测结果
**research** → 外部信息交叉验证 + LLM 逻辑完整性检查
**other** → 按 plan.md 定义的方式验证

### 5. 交叉验证（网页 LLM）

**所有 Review 后必须执行交叉验证**（code 测试是例外，但推荐也做 LLM 逻辑 review）。

消息模板：
```
任务类型：{task_type}
Review 结果：{review_summary}
产出摘要：{output_summary}
关键疑点：{issues}

请评估：Review 结果是否可靠？有无遗漏问题？方法论/逻辑是否合理？
返回：PASS / FAIL / UNCERTAIN
```

## 判定与处置

**PASS** → git commit + 标记 COMPLETED + 允许后续任务启动

**FAIL** → 
1. 写入 fix-plan.md（修复意图、方案、修复子任务分解）
2. 修复子任务必须遵守**多层分解规则**（与 1-loop 相同）：
   - 任务可以继续细分，不设置固定的计划修订次数或最大深度
   - 同一并行层级必须正交，跨层必须声明输入、输出和条件
3. 每个修复子任务使用稳定任务 ID，并记录 revision 和 lineage
4. 每个修复子任务走完整 per-step 循环
5. 修复结果使用新 revision，失败中间态保存在事件日志和 artifact
6. 原任务重新走完整 per-step 循环

**UNCERTAIN** → 标记 `blocked_human` + 记录风险描述 + 跳过当前子任务；没有 ready 任务时进入 `exploration`

## 约束

1. 禁止原地重试 — Review 不通过必须先分解修复
2. 所有修复子任务也必须走完整 per-step 循环
3. 禁止跨子任务直接耦合 — 仅通过文件接口通信
4. Git commit 必须有明确标记
5. Backup 失败不阻塞执行，但记录到日志
