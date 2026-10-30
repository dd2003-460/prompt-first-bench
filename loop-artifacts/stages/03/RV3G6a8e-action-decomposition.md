# 阶段 03：行动分解 — RV3G6-audit8-erratum

> goal: AUDIT-report §8 参考值表绝对值勘误 · 分支 ralph/rv3g6-audit8-erratum · 2026-10-30
> owner 标注：agent = runner 可自主执行 / user = 需成璐决策（写 APPROVALS 不阻塞）
> 输入边界：只使用 02/02.5 已核验证据；U3（L103/L166 G3 口径数值）经 02.5 A3a 裁决**不并入**本 erratum，导出 queue

## 行动表

| # | 行动 | owner | 依赖 | 验收 |
|---|------|-------|------|------|
| A1 | AUDIT L108 范围句修正：W1 [2.60, 6.40]→[8.60, 12.40] / W2-orig [7.80, 8.00]→[8.20, 8.40] / W2-new [5.20, 6.60]→[8.80, 10.20] / W3-new/W4-new [6.80, 7.00]→[7.40, 7.60]（tie 组结构列与 5.40 不动） | agent | 02 §1 E1 | grep 旧区间串零命中；新值与 freeze doc §5 逐字一致 |
| A2 | AUDIT L109 修正：落盘顺序值 orig 侧 W1=9.8→10.2、new 侧 W1=9.8→10.2 / W2=7.6→9.8（W2-orig=8.2 与 W3=W4=7.6 保留）+ E3 结论句改写「可优于」→「仍劣于」（2.60→8.60）+ 02.5 M-1 衔接半句（预注册 tie-break 强制价值表述更新） | agent | 02 §1 E2/E3 + 02.5 A4a | grep「可优于 W3-orig」零命中；grep「仍劣于 W3-orig」命中 1；定性尾句（禁止各方案取各自最优）原文保留 |
| A3 | AUDIT L172 finding #11 区间 [2.60, 6.40]→[8.60, 12.40]（G5 原引作废声明句不动） | agent | 02 §1 E4 | grep 复核 |
| A4 | AUDIT L252 §8 规则 1 引用模板「9.8…[2.60, 6.40]」→「10.2…[8.60, 12.40]」 | agent | 02 §1 E5 | grep 复核 |
| A5 | AUDIT L263-269 §8 参考值表四行区间列修正（同 A1 值），表头下加一行注记「绝对值 2026-10-30 erratum 修正（见文末 Erratum 节）」 | agent | 02 §1 E6 | 表格渲染完整；span 跨度标注（3.8/0.2/1.4/0.2）与 tie 组列不动 |
| A6 | AUDIT 文末新增「## Erratum（2026-10-30）」节：勘误范围（E1-E6 清单）/ 错误定位（§8 表绝对值算术错误，tie 结构与 span 正确——引 freeze doc §4.1 判定）/ 权威源声明（以 gmr-criterion-freeze.md §5 + assert-gmr-recompute.py computed 列为准）/ 定性结论不变声明 / U3 登记（L103/L166 的 6.4→8.6 属 G3 F2 过程记录口径，未并入本次勘误，导出 queue 单独裁定） | agent | A1-A5 | 节内每处修正带行号 evidence；U3 表述与 02.5 A3a 一致 |
| A7 | freeze doc §4 byte-exact 块重抄录为 erratum 后 AUDIT §8 全文（脚本提取，不手敲——R2 缓解）+ 块前标注「erratum 后版本（rXXX, 2026-10-30）」+ §4.1 处置段末补一句「erratum 已发（见 AUDIT-report.md 文末 Erratum 节），双源消除」 | agent | A1-A6 | 机判 diff：freeze doc §4 块内容 == AUDIT §8 实际文本（assert 检查③） |
| A8 | 新增 `bench/rubric-v3/ablation/scripts/assert-audit8-erratum.py`：① AUDIT 内 8 个修正值定点断言（L108/L109/L172/L252/L265-269 正则锚定）；② 旧错误 token 黑名单全文扫描（[2.60, 6.40] / [7.80, 8.00] / [5.20, 6.60] / [6.80, 7.00] / 「可优于 W3-orig」）零命中；③ freeze doc §4 byte-exact 块 == AUDIT §8 文本 diff 空；④ 定性关键词仍在（tie-robust 单值 / 对 tie-break 规则敏感 / 禁止各方案取各自最优 / 跨方案比较必须在预注册 tie-break 下进行） | agent | A1-A7 | exit 0；变异测试：临时注入一个旧错误 token → exit 1 且报出位置 → 还原 → exit 0 |
| A9 | 冻结数据零修改验证（git status：prior-estimates.json / judge-blindtest-r1.json / hit-matrix.json / stats-* / gold-tree.md / runs-C0-* 无 diff）+ web-llm 回执状态核对（原路径文件零 diff + per-goal 新文件存在） | agent | A1-A8 | git status 输出仅含本 goal 预期文件 |
| A10 | 阶段 04.5 反方复核（≥3 攻击：erratum 是否引入新不一致 / byte-exact 声明是否真成立 / 定性结论是否被误伤 / U3 切割是否干净）+ verdict | agent | A9 | verdict pass 方可收口 |
| A11 | 收口：commit + push `ralph/rv3g6-audit8-erratum` + ls-remote 验证 → merge main + push → goal-queue 标记 [x] + 结果注记 + 追加 ≥1 新候选（RV3G6-g3-gmr-caliber-adjudicate：L103/L166「gmr 6.4→8.6」G3 F2 口径归属裁定——若属 global gmr 则需二次勘误，若属 per-run/历史口径则在 AUDIT 加注区分） | agent | A10 | main 上可见 merge commit；queue 队首变为下一 goal |

## 关键路径

A1→A2→A3→A4→A5→A6→A7→A8→A9→A10→A11（全串行——同一文件多处编辑必须顺序防 Edit 冲突；A7 依赖 A1-A6 全部完成后的最终文本）

## 不做的事（边界）

- 不改 L103/L166 的「6.4→8.6」（U3，02.5 A3a 裁决导出 queue，不在本 erratum 强行裁定）
- 不改 freeze doc §5 权威表 / §1-§3 / §6-§7（只动 §4 抄录块 + §4.1 末句）
- 不改 DRAFT v2（其 gmr 引用指向 AUDIT §3.2/§8 机制性引用，不含具体数值——02 §3 已核）
- 不改任何冻结 JSON / stats / run 文件
- 不代裁 U3 口径归属（需对照 G3 原始计算工件逐行定位，超出本 goal 最小范围）