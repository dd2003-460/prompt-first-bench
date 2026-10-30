# 01 — RV3G6-o3-claim-rejudge-scaffold · goal 分解

> goal: claim 级独立重判的仓库内闭环骨架（schema + assert + 采样清单）
> 分支: ralph/rv3g6-o3-claim-rejudge-scaffold · 2026-10-30

## 1. 问题定义与范围切割

**上游状态**：`o3-claim-list.md` §4.4/§5.2 U1 登记「claim 级独立重判 unverified（工具纪律禁 subagent → arena 通道）」；DRAFT v2 L70 `[batch2: R-13]` 行标注剩余部分导出 queue `RV3G6-o3-claim-rejudge`。原 goal 定义 = fresh-context judge 盲读 run 原文对 31×8=248 cell 逐格判 h_claim，落盘后按 §3 口径报 M1/M2 实际读数。

**阻塞源判定**：执行主体（judge 盲判 248 cell）需外部通道——同族 subagent 被工具纪律禁止（o3-claim-list §4.1 独立性定义要求上下文独立盲读，且 S2 限定语要求家族独立更佳），arena 会话通道当前不可用（web-llm 三 provider 登录态失效，r126 登记）。→ **执行体 blocked-on-external**。

**可先行切片判定**（先例对齐）：
| 先例 | 模式 | 本 goal 对应 |
|------|------|-------------|
| r136 kappa-receipt-assert | 回执缺失常态 FAIL/SIGNAL，不伪造转绿；schema 预注册先行 | rejudge 结果缺失常态 SIGNAL exit 0 |
| r140 crossdomain-reverify | batch2 数据未落盘 → assert 骨架 + schema 预注册 + 变异测试先行 | rejudge JSON 未落盘 → assert + protocol + sample-plan 先行 |

本 goal = 上述模式的第三个实例：**消费侧机判件全部落盘，生产侧（judge 执行）零改动接入**。

## 2. 交付物分解（三件，全新文件）

| # | 交付物 | 内容边界 | 验收锚点 |
|---|--------|----------|----------|
| D1 | `rejudge/judge-protocol-batch1.md` | blind-packet 结构 + I/O schema + 聚合/κ 引用 + S2 叠加声明 | 字段集 byte-stable；引用 o3-claim-list §2/§3/§4/§5.1 不另行定义 |
| D2 | `rejudge/sample-plan.json` | 248 cell 全量枚举 + P0/P1 分层 + gold strict 标记 | 与 hit-matrix 机算比对零 mismatch（150/98/40） |
| D3 | `scripts/assert-o3-claim-rejudge.py` | 三分支消费断言 + M1/M2 复算 + 防泄漏检查 | 实跑 SIGNAL exit 0；变异 ≥3 场景 |

**不做的事**（范围红线）：
- 不产生任何新的 h 值（o3-claim-list §4.4 硬条款）
- 不修改 o3-claim-list.md / hit-matrix.json / gold-tree.md / DRAFT v2（冻结面）
- 不发明 κ 计算公式（§4.3 只引用顺序关系；具体公式若冻结件未定义 → UNRESOLVED 登记）
- 不替代 judge 做语义判断（协议只规定输入边界与输出格式）

## 3. 阶段计划

01（本文）→ 02 精读 o3-claim-list §2-§5 + assert-o3-claim-list.py 黑名单机制 + assert-kappa-receipt.py 三分支写法 → 02.5 hit-matrix 分布 vs §3.2 注记交叉核对 → 03 行动分解 → 04 三件落盘 + 实跑 + 变异 → 04.5 反方复核（重点攻击：是否变相产生 h 值 / 防泄漏检查是否空转 / 偏离量计算口径是否与 §3 一致 / 冻结面是否真零修改）