# Goal: RV3G3cdx-batch2-schema-lint — batch2 三输入文件 schema lint 独立化（r147）

> 创建：2026-10-30 · ralph loop runner（queue 消费——r145 核销轮导出项，纯仓库内脚本工作）
> 依据：assert-goldrank-crossdomain.py docstring L11-35 已预注册 batch2 三文件字段级 schema；当前 lint 逻辑嵌在 `load_batch2()` 内且**只在数据目录存在时可达**——数据提供方写入 `bench/rubric-v3/ablation/batch2/` 前无法自验，schema 违例要到 closure 轮才暴露（RV3G3-batch2-arrival-closure 执行往返成本）。本 goal = 把 lint 从「断言前置检查」拆为「可独立调用的自验入口」。
> 范围上限：只动 `assert-goldrank-crossdomain.py`（加 `--lint-only` 入口 + 参数化路径）+ 新测试样例目录；不动判定协议（S1/S2/(a)/(b)）、不动其他脚本、不动冻结面。

## 【目标】
给 assert-goldrank-crossdomain.py 增加 `--lint-only [--dir <path>]` 入口：对指定目录（默认 `bench/rubric-v3/ablation/batch2/`）的三输入文件做**纯 schema 校验**（不跑 (a)/(b) 判定），输出逐文件 PASS/FAIL + exit code（0 = 全通过 / 2 = schema 违例或不可读 / 缺 blindtest = D5 降级提示但非错误）。规则零新增设计——全部复用 `load_batch2()` 既有检查 + docstring 预注册 schema。

## 【阶段】
01（本文件）→ 02 现状扫描（docstring schema 逐条提取 + load_batch2 检查逻辑盘点 + 现有调用面核查）→ 02.5 交叉核对（独立重读源码复核 02 提取完整性）→ 03 动作分解 → 04 执行验证（实现 + 正/负样例矩阵实跑 + 回归基线 spot check）→ 04.5 反方复核 → 收口（queue 更新 + merge main）

## 【SOP 索引】
- `tasks/ralph-loop-runner.md` 阶段 B/C
- 被改对象：`bench/rubric-v3/ablation/scripts/assert-goldrank-crossdomain.py`（282 行，结构见 02）
- schema 权威源：同文件 docstring L11-35（字段级预注册）+ `load_batch2()` L186-232（机判实现）
- 参照先例：assert-kappa-receipt.py（r136 schema 骨架模式）；assert-goldrank-threshold.py（check() 汇总模式）

## 【验收标准】
- [ ] `python3 assert-goldrank-crossdomain.py --lint-only` 在 batch2/ 不存在时输出明确信号（非 crash、非误报 schema 违例）且 exit 0
- [ ] 正样例（合规三文件，含 blindtest 缺失变体）→ exit 0 + 逐文件 PASS
- [ ] 负样例矩阵（≥4 类违例：缺 prior / nodes 缺 w1 / p_tilde 键缺失 / hit-matrix gold 节点缺席 / blindtest 条目缺字段）→ 各自 exit 2 + 指名道姓的错误信息
- [ ] 无参调用行为与改动前 byte-exact 一致（回归基线：exit 0 + SIGNAL blocked-on-external 两行逐字不变）
- [ ] 七脚本回归基线 spot check 与 r146 A1 表零漂移（exit=[0,0,0,1,0,0,0]）
- [ ] 冻结面零修改（hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-*）；改动面 ⊆ {crossdomain 脚本, stages/*, current-goal.md, goal-queue.md}
- [ ] 04.5 verdict pass；queue 更新（本 goal `[x]` + 结果注记 + 新候选 ≥1）

## 【失败降级】
- 若 `load_batch2()` 重构引入无参调用行为变化 → 回滚脚本改动，改为独立新脚本 `assert-batch2-lint.py`（import 共享逻辑或复制），本 goal 仍按原验收标准收口
- 若负样例暴露 docstring schema 与代码实现不一致（如某字段 docstring 声明必需但代码未查）→ 以代码为准登记 mismatch 并导出候选，不擅自扩 lint 规则（防超范围）