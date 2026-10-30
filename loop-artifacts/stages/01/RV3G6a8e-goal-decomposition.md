# 阶段 01：目标分解 — RV3G6-audit8-erratum

> goal: AUDIT-report §8 参考值表绝对值勘误 · 分支 ralph/rv3g6-audit8-erratum · 2026-10-30
> 上游：tasks/current-goal.md（五字段）+ gmr-criterion-freeze.md §4.1/§5 + AUDIT-report.md L108/L109/L172/L252/L261-271

## F1 · 交付物结构分解

| # | 交付物 | 内容 | 关键判读点 |
|---|--------|------|-----------|
| D1 | AUDIT-report.md erratum（就地修订） | 全部引用错误绝对值的位置修正为 freeze doc §5 复算值 + L109 结论句改写 + 文末新增「Erratum」节（勘误声明：错在哪、以谁为准、何时发现） | 每处修正必须可追溯到 freeze doc §5 或 assert-gmr-recompute.py expected 表；定性结论（排序方向/tie-robust 判定/span 宽度）零改动 |
| D2 | gmr-criterion-freeze.md §4 同步 | byte-exact 块重抄录为 erratum 后 AUDIT §8 原文 + 标注「erratum 后版本（rXXX）」+ §4.1 处置段补一句「erratum 已发，双源消除」 | byte-exact 声明重新成立（机判 diff 验证）；freeze doc §5 权威表本身不动 |
| D3 | assert-audit8-erratum.py | ① AUDIT 内 gmr 数值 token 与 freeze doc §5 表一致；② L109 不再含「可优于 W3-orig」语义且含正确表述；③ freeze doc §4 byte-exact 块 == AUDIT §8 实际文本（diff 空） | exit 0；变异测试确认检查实义生效（仿 o3cl W5 教训：先注入错误值确认 FAIL 再还原） |
| D4 | loop-artifacts 六阶段工件 | 本文件 + 02/02.5/03/04/04.5 | 文件名前缀 RV3G6a8e 防撞车 |

**判读**：D1 是核心（~5 处数值 + 1 句结论）；D2 是连锁义务（byte-exact 条款的单一事实源维护）；D3 防未来漂移。三者合起来才真正「消除双源困惑」——只改 AUDIT 不改 freeze doc §4 会制造新的不一致（byte-exact 块指向已不存在的原文）。

## F2 · 输入完备性盘点

| 输入 | 状态 | evidence |
|------|------|----------|
| freeze doc §5 权威参考值表（W1 [8.60,12.40] id=10.20 / W2-orig [8.20,8.40] id=8.20 / W3-W4-orig 5.40 / W2-new [8.80,10.20] id=9.80 / W3-W4-new [7.40,7.60] id=7.60） | ✅ 在仓 | gmr-criterion-freeze.md L160-168 |
| freeze doc §4.1 偏差定位（tie 组结构一致 / span 一致 / 绝对值系统性偏移 / 定性结论不受影响） | ✅ 在仓 | gmr-criterion-freeze.md L133-150 |
| assert-gmr-recompute.py（expected 表与 §5 同源，exit 0 基线） | ✅ 在仓 | scripts/assert-gmr-recompute.py L62-70 |
| AUDIT 错误位置清单（L108 范围句 / L109 落盘顺序值+结论句 / L172 finding #11 / L252 引用模板 / L263-269 参考值表） | ✅ 本 goal grep 盘点 | 见 F3-J2 全量盘点 |
| tie 组结构列（{5.0: N-2,N-4} {2.0: N-2.1,N-1.3} {3.396: N-3.2.2} 等） | ✅ 两源一致 | freeze doc §4.1 L146「tie 组结构完全一致」 |
| 外部文献交叉验证 | ❌ 不需要 | 纯仓库内数值一致性工作，无外部依赖 |

**空缺**：无阻塞性空缺。一个非阻塞观察登记为 F4-R3（AUDIT L109 的 new judge 侧落盘顺序值 W2=7.6 与 freeze doc §5 的 W2-new id-order 9.80 不一致——queue 描述未覆盖此点，属 erratum 完整性扩展项）。

## F3 · 判断点识别

| # | 判断 | 选项空间 | 预注册倾向 |
|---|------|----------|-----------|
| J1 | erratum 形式：A 就地修订 + 文末 Erratum 节 / B 单独 erratum 文件不动 AUDIT 正文 | A（queue 描述原文「同步修正」「发 erratum 消除双源困惑」——B 会让 AUDIT 正文继续携带错误值，双源困惑只减一半；A 的留痕由 git diff + Erratum 节承担） |
| J2 | 修正范围：A 只改 queue 描述的「两处数值+一行措辞」（§8 表 + L109）/ B 全量盘点同文件所有引用同一错误绝对值的位置一并修正 | B（grep 盘点结果：L108 范围句、L109 落盘顺序值、L172 finding #11 区间、L252 §8 规则 1 模板值、L263-269 表——只改 §8 表会在同一文件内留下 L108/L172/L252 三处旧值，等于把双源从跨文件挪到文件内。current-goal 失败降级条款授权此扩展，每处带 evidence） |
| J3 | L109 落盘顺序值（W1=9.8/W2=8.2/new 侧 W1=9.8/W2=7.6/W3=W4=7.6）是否一并修正 | 修（freeze doc §5 id-order 值 = W1 10.20 / W2-orig 8.20 / W2-new 9.80 / W3-new 7.60——注意 orig 侧 W1 与 new 侧 W1 在 freeze doc 中同为 10.20（E3.2：W1-new 与 W1-orig gmr 范围完全相同），AUDIT L109 写 W1=9.8 两侧重复且都错；new 侧 W2=7.6 应为 9.80，W3=W4=7.6 正确保留） |
| J4 | freeze doc §4 byte-exact 块处置：A 重抄录 erratum 后文本 / B 保留旧抄录 + 标注「已被 erratum 取代」 | A（B 让冻结件内部同时存在新旧两版 §8 文本，违反冻结件「唯一定义源」定位 §7；A 保持单一事实源，git 历史留旧版） |
| J5 | 新 assert 脚本的检查粒度：A 全文数值 token 扫描 / B 定点行断言（已知 5 处位置的正则锚定） | B + 兜底 A 的轻量版（定点断言防回归 + 全文 grep 错误 token 黑名单如「[2.60, 6.40]」确保无遗漏位置） |

## F4 · 风险登记

| # | 风险 | 严重度 | 缓解 |
|----|------|--------|------|
| R1 | 修数值时误伤定性结论（如把「W1 最差且 tie-sensitive」也改掉） | 高 | 每处 Edit 前后 grep 复核定性句不变；assert 脚本加一条「定性关键词仍在」检查（tie-robust / tie-break 敏感 / 跨方案排序方向） |
| R2 | freeze doc §4 重抄录时手抖引入新差异，byte-exact 声明变成假声明 | 高 | 用脚本提取 AUDIT §8 实际文本写入 freeze doc §4 块（不手敲）；assert 检查③ diff 验证 |
| R3 | AUDIT L109 new 侧 W2=7.6 与 freeze doc §5 W2-new id-order 9.80 的偏差未被 queue 描述覆盖——若 freeze doc §5 此处也有错，erratum 会把错误固化 | 中 | 执行前用 assert-gmr-recompute.py 独立复算 W2-new id-order 值确认 9.80（该脚本 expected 表即 freeze doc §5，exit 0 基线已在 r118 建立）；若复算不符则回退 02 重新定位 |
| R4 | 「落盘顺序值」与「id 字典序值」概念混淆（两者按 freeze doc §1.1 等价，但 AUDIT 混用两种叫法） | 低 | erratum 统一沿用 AUDIT 原有用语「落盘顺序值」，不引入新术语；freeze doc §1.1 已声明两者等价 |
| R5 | 修改 AUDIT-report.md 触发其他下游文档的 byte-exact 引用失效 | 中 | grep 全仓「BYTE-EXACT」标记找所有抄录 AUDIT 的位置（已知仅 freeze doc §4 一处）；revision-log 登记 |

## 阶段 02 研究入口

- 第一批行动：grep 全仓 AUDIT-report.md 的 byte-exact 抄录点（R5 核查）+ 全量盘点 AUDIT 内 gmr 数值出现位置（J2 清单定稿）
- 第二批行动：跑 assert-gmr-recompute.py 确认 exit 0 基线 + 独立打印 W2-new id-order 值（R3 核查）
- 第三批行动：web-llm 强制步骤（per-goal 分文件回执，避免覆写既有回执——RV3B1-webllm-receipt-per-goal 前置执行）
- 失败备用路径：若 web-llm 快速失败（登录过期延续）→ 记录完整失败原因后继续，本 goal 无外部依赖不阻塞