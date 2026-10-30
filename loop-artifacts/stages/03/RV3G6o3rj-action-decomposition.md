# 03 — RV3G6-o3-claim-rejudge-scaffold · 行动分解

> goal: claim 级独立重判的仓库内闭环骨架 · 分支 ralph/rv3g6-o3-claim-rejudge-scaffold · 2026-10-30

## 行动表

| # | 行动 | 输入 | 输出 | 依赖 | 验证方式 |
|---|------|------|------|------|----------|
| A1 | sample-plan.json 生成（机算脚本现场执行，非手写）：248 cell 全量枚举 + P0/P1 分层 + gold strict 标记 + 元数据（生成源 commit / 分布计数） | hit-matrix.json（只读） | `rejudge/sample-plan.json` | — | 独立 python 复核：cell 数 248 / P0=150 / P1=98 / gold=40 / 无重复无遗漏（set 比对 hit-matrix 全 cell 集） |
| A2 | judge-protocol-batch1.md 落盘：blind-packet 白名单结构 + I/O schema（byte-stable）+ §4.2/§4.3 引用 + S2 §5.1 byte-exact 引用 + U-K1 UNRESOLVED 登记 | o3-claim-list §2/§3/§4/§5.1（只读） | `rejudge/judge-protocol-batch1.md` | A1（schema 中引用 sample-plan 路径） | grep：S2 限定语段落与 o3-claim-list §5.1 逐字 diff = 空；schema 字段清单与 assert docstring 一致 |
| A3 | assert-o3-claim-rejudge.py 落盘：docstring 预注册 schema + 三分支主流程 + M1/M2 复算 + evidence 子串检查 + flip 偏离表 | protocol D1 schema + hit-matrix + runs-C0-*（只读） | `scripts/assert-o3-claim-rejudge.py` | A2 | 实跑当前面 = SIGNAL blocked-on-external exit 0 |
| A4 | 变异测试 ≥3 场景（临时 fixture 写入 rejudge/，测毕即删）：M1 伪造完整 rejudge 结果（构造已知 flip 集合）→ M1/M2 偏离量逐格正确 + exit 0；M2 部分翻转含 h=0→1 → flip 方向切片报告正确；M3 schema 违例（evidence 非 run 子串 / h_claim=1 缺 evidence / 未知 node）→ ERROR exit 2；M4 缺文件常态 → SIGNAL exit 0 | A3 + runs-C0-* 原文 | 04 日志各场景实测输出 | A3 | 各场景 exit code + stdout 关键行核对 |
| A5 | 冻结面零修改验证 + 既有断言回归（assert-o3-claim-list.py / assert-goldrank-threshold.py / assert-gmr-recompute.py 重跑基线维持） | git status + 三脚本 | 04 日志记录 | A1-A4 | git status 冻结文件零 diff；回归脚本 exit 0 且计数与基线一致 |
| A6 | queue 更新 + 新候选导出：RV3G6-o3-claim-rejudge 标注「仓库内骨架完成（r141），剩余 = judge 实际执行 blocked-on-external」；追加候选 U-K1 κ 公式裁定 + （若 04.5 暴露）其他项 | goal-queue.md | queue diff | A1-A5 | queue 条目格式合规（五要素） |

## 预注册规则（04.5 攻击面预先声明）

1. **零 h 值红线**：本 goal 任何交付物不得包含 judge 对 (run, node) 的实质内容判定。sample-plan 的 P0/P1 标签来自冻结 h_id（非新判定）；protocol 的示例 cell 必须用占位符（`<yes/no>`）不得填真实判断。
2. **不发明口径**：M1/M2 公式照抄 o3-claim-list §3.1 定义式；κ 不计算（U-K1）；聚合规则只引用 §4.2 不改写。
3. **fixture 不留痕**：变异测试临时文件测毕删除，git status 验证 rejudge/ 目录最终只含 A1/A2 两件正式交付物 + assert 在 scripts/。
4. **exit code 约定不变**：0 = 无 FAIL（含 SIGNAL）/ 1 = verdict FAIL（数据齐备但偏离超界或 schema 外错误）/ 2 = schema 违例 fail-loud。注意：数据齐备时 M1/M2 偏离本身**不是** FAIL 条件——偏离是预期产出（FM-2 检验目标就是找 flip），verdict FAIL 仅限「结果不可信」类错误（evidence 编造 / cell 覆盖不全）。此语义在 docstring 显式预注册，防 04.5 攻击「为何偏离不 FAIL」。