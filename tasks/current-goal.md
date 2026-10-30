# Goal: R5.2assert-suite-docsync — docstring 文档-实现同步（核销轮）

> 创建：2026-10-30 · ralph loop runner（`tasks/goal-queue.md` 候选「R5.2assert-suite-docsync」）
> 依据：r132 04.5 导出；工作量极小

## 【目标】
assert-c4-timing.py docstring 判定口径段补 r132 fail-loud/WS 拦截行为说明（文档-实现同步）。

**范围发现（阶段 A 实证）**：该 goal 已由 **r133 (c55848f)** 完成——docstring L13-15 已含「r132 健壮性行为：WS_RUN2 目录缺失 → 显式 FAIL + exit 1…epoch() 先剥离时区段再按主体位数分派…fail-loud ValueError」，与 r132 实现逐条对应。但 `goal-queue.md` 中本候选**未被划掉**（r133 收口漏更新 queue——对比 r132b/r134b/r135b/r136b 均有独立收口 commit，r133 没有）。→ 本 goal 收口为**核销+队列卫生修复**：(a) 验证 r133 改动与实现的对应关系；(b) 脚本实跑确认行为与 docstring 一致；(c) 划掉 queue 条目并注记 r133 已完成 + 本次核销增量。

## 【阶段】
零代码改动的核销轮（若验证发现 docstring 与实现有真实偏差则例外修复）。

## 【SOP 索引】
- `loop/prompt-first/01..04.5`；对象 `bench/self-opt-tester/r5/assert-c4-timing.py`（只读验证）

## 【验收标准】
- [ ] docstring r132 行为段三条声明（WS 缺失 FAIL+exit1 / epoch 时区剥离+位数分派 / 未知格式 fail-loud）与代码实现逐条对照表
- [ ] 脚本实跑 exit 0 + SIGNAL not-reconstructable（与 r130 基线语义一致，无行为漂移）
- [ ] WS 缺失场景复验（/tmp 假路径沙盒）→ 显式 FAIL + exit 1 非 traceback（docstring 声明的行为实证）
- [ ] queue 条目划掉 + 结果注记（含「r133 已完成、r133 漏更新 queue、本轮 = 核销+队列卫生」事实链）

## 【失败降级】
- 对照发现 docstring 与实现真实偏差 → 修复 docstring 或代码（以实现为准，除非实现本身违反 r132 预注册口径）
- web-llm 不可用 → unverified 降级（纯文档核销边际贡献 ≈ 0，同族判据）