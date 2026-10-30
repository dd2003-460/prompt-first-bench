# 阶段 03：行动分解 — RV3G6-gmr-caliber-u3

> 依据：02 §4 裁定（加注路径）+ 02.5 verdict pass · 分支 ralph/rv3g6-gmr-caliber-u3

## 行动表

| # | 行动 | 对象 | 具体改动 | 验证方式 |
|---|------|------|----------|----------|
| A1 | L103 口径注记 | AUDIT-report.md L103 | 「gmr 6.4→8.6」→「gold 平均排名 6.4→8.6（G3 F3b 口径，1-based rank；冻结 0-based gmr 等价 5.40→7.60）」——保留数值与「连续移动，方案间排序不变」定性句 | grep 定点行 + assert 新断言 |
| A2 | L166 口径注记 | AUDIT-report.md L166 | 「gmr 6.4→8.6」→「gold 平均排名 6.4→8.6（G3 口径，1-based；冻结 0-based gmr 5.40→7.60）」——保留「与 W3 同幅恶化」定性句 | 同上 |
| A3 | U3 段状态更新 | AUDIT-report.md L362（Erratum 节内） | 「未并入项（U3，导出 queue）」→「已裁定项（U3，RV3G6-gmr-caliber-u3）」+ 裁定结论一句话 + 指向 02 工件的 evidence 指针；旧表述以引号历史引用形式保留 | grep + assert |
| A4 | assert 扩展 | ablation/scripts/assert-audit8-erratum.py | 新增检查组⑤：(a) L103/L166 含「1-based」注记 token；(b) L103/L166 不再裸写「gmr 6.4→8.6」（正则锚定该两行）；(c) U3 段含「已裁定」且不含「未并入项（U3」。现有①–④不动 | 脚本 exit 0 + 变异测试（去注记→FAIL→还原→PASS） |
| A5 | 冻结数据零修改核验 | prior-estimates.json / judge-blindtest-r1.json / hit-matrix.json / stats-* | 只读使用 | `git status` 无 diff |
| A6 | 六阶段工件落盘 | loop-artifacts/stages/{01,02,02.5,03,04,04.5}/ + prompt-first/ | 本文件 + 04 执行日志 + 04.5 反方复核（≥3 攻击） | 文件存在性 |
| A7 | queue 导出 | tasks/goal-queue.md（收口时） | u3 标记 [x] + 结果注记；追加候选 `RV3B1-webllm-tool-fix`（ralph-loop.md 缺失致 web-llm 不可用，优先级高于 receipt-per-goal） | 收口 commit 后 ls-remote |

## 明确不做（防范围蔓延）

- 不改 G3/G4 过程记录（L31/L48/L69/L86 保持原口径名——历史工件留痕原则，r122 先例）
- 不改 freeze doc（§5 本来就是 0-based 权威值，§4 byte-exact 块不涉及 L103/L166）
- 不引入 +40.7% 等新百分比进修订句（R3 缓解：只引用可机判绝对值 5.40/7.60）
- 不裁定 O1 判据最终选择（那是 G6 定稿范畴，G3 F3b 已声明「最终选择权交 G6」）

## 顺序依赖

A1/A2 → A3（U3 段引述修订后的定位）→ A4（assert 锚定最终文本）→ A5（全程）→ A6（04 汇总 A1-A5 实跑输出）→ 收口 A7。