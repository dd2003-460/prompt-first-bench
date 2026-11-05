# 阶段 04：执行与验证日志 — RV3G6-gmr-caliber-u3

> 分支 ralph/rv3g6-gmr-caliber-u3 · 2026-10-30 · 依据 03 行动表 A1-A7

## §1 · 行动执行记录

| # | 行动 | 实跑结果 | evidence |
|---|------|----------|----------|
| A1 | L103 口径注记 | ✅ 已落地：「gold 平均排名 6.4→8.6（G3 F3b 口径，1-based rank；冻结 0-based gmr 等价 5.40→7.60，连续移动，方案间排序不变）」——数值保留、定性句原样 | AUDIT-report.md L103（git diff） |
| A2 | L166 口径注记 | ✅ 已落地：「gold 平均排名 6.4→8.6，G3 口径 1-based rank；冻结 0-based gmr 等价 5.40→7.60」——「与 W3 同幅恶化」保留 | AUDIT-report.md L166 |
| A3 | U3 段转已裁定 | ✅ L362「未并入项（U3，导出 queue）」→「已裁定项（U3，RV3G6-gmr-caliber-u3 · 2026-10-30）」+ 裁定结论 + evidence 指针；旧表述以引号历史引用形式保留于段内 | AUDIT-report.md L362 |
| A4 | assert 扩展 | ✅ 新增检查组⑤（8 条断言：行定位 / 1-based 注记×2 / 等价值×2 / 无裸写歧义×2 / 定性句保留×2 / U3 段状态×2）；首跑发现 ⑤g token 含日期后缀失配 → 修正 token 后全绿 | assert-audit8-erratum.py ⑤a-⑤h |
| A5 | 冻结数据零修改 | ✅ `git diff --stat` 对 prior-estimates.json / judge-blindtest-r1.json / hit-matrix.json / stats-* = 0 行 | 本日志 §1 A5 命令输出 |
| A6 | 六阶段工件 | ✅ 01/02/02.5/03 已落盘 + 本文件 + 04.5 待写 + web-llm 回执（prompt-first/） | loop-artifacts/stages/ |
| A7 | queue 导出 | ⏳ 收口时执行（u3 标 [x] + 追加 RV3B1-webllm-tool-fix 候选） | — |

## §2 · 机判输出（原样摘录）

**assert-audit8-erratum.py（扩展后）**：
```
=== 32 PASS / 0 FAIL ===   exit 0
```
（r122 基线 21 条全部维持 PASS + 新增 ⑤a-⑤h 共 11 条中 10 条独立检查项全 PASS；注：⑤a 为前置定位检查）

**变异测试**（防「检查空转」，仿 o3cl W5 教训）：
- 注入：L103 注记还原为旧裸写「gmr 6.4→8.6（连续移动…）」→ **exit 1，3 FAIL**（⑤b/⑤c/⑤d L103 三条精确命中被改行）
- 还原：恢复修订文本 → **exit 0，32 PASS / 0 FAIL**
- 结论：检查组⑤实义生效，非恒真检查。

**独立复算**（02 §2 表，协议 = assert-gmr-recompute.py 原样复用，冻结 JSON 只读）：
```
scheme     exact-gmr   g3-recorded   diff
W1            10.20        11.2     +1.0
W2-orig       8.20         9.2      +1.0
W3-orig       5.40         6.4      +1.0
W4-orig       5.40         6.4      +1.0
W2-new        9.80        10.8      +1.0
W3-new        7.60         8.6      +1.0
W4-new        7.60         8.6      +1.0
```
7/7 列均匀 +1.0 → 1-based rank 记法判定成立（02.5 A1/A2 攻击均失败）。

## §3 · 诚实声明（负结果与不确定性）

1. **web-llm 未实际执行**（工具故障：`ralph-loop.md` 缺失，`ralph prompt-first web-llm` 无法启动）——本 goal 证据链仓库内闭合，降级不阻塞，但「外部在线复核」一项对本 goal 是 **unverified** 而非 pass。详见 `loop-artifacts/prompt-first/02-web-llm-cross-check-RV3G6u3.md`。
2. **G3 当时使用的 gold 集归属是数值反推**（7/7 全列 +1.0 排除 3 节点窄集假设），非 G3 协议文档直证——G3 无落盘计算脚本（stats-w3w4.json 只存 top-5 计数，不存 rank 均值）。此推断强度足以支撑裁定（数值指纹即身份），但如实标注。
3. **G3/G4 过程记录未改动**（L31/L48/L69/L86 保持原口径名）——历史工件留痕原则；其内部「gold 平均排名」字样在 G3 语境下本就正确，无需也不应改写。

## §4 · 验收标准对照（current-goal【验收标准】）

- [x] 口径判定有 evidence：02 §1（逐字溯源表）+ §2（7/7 复算表）+ 02.5（5 攻击）
- [x] 按判定落地二选一不并存：走加注路径（L103/L166 注记 + U3 段转已裁定），未发 E7 勘误行——判定依据见 02 §4「为何不走二次勘误」
- [x] assert 脚本 exit 0：32 PASS / 0 FAIL + 变异测试确认实义
- [x] 冻结数据零修改：git diff 0 行
- [x] 定性结论零改动：④ 组关键词全 PASS + ⑤e/⑤f 定性句定点保留；grep 复核「连续移动，方案间排序不变」「与 W3 同幅恶化」原样在位