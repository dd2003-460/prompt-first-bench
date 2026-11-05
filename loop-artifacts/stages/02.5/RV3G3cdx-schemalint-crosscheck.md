# 02.5 — RV3G3cdx-batch2-schema-lint · 交叉核对（独立重读源码复核 02 提取）

> goal: batch2 schema lint 独立化 · 分支 ralph/rv3g3cdx-batch2-schema-lint · 2026-10-30
> 方法：不读 02 结论列，从文件重新 grep/计数，逐格比对。

## X1 — 检查链完整性复核

`grep -c 'return False'` = **8 处**：L189（目录缺）/ L203（不可读，经 errs 汇总）/ L209（nodes 非 dict）/ L214（gold_nodes 类型）/ L218（w1 缺）/ L220（p_tilde 键缺）/ L225（hit-matrix gold 缺席）/ L230（blindtest entry 缺字段）。→ 失败出口总数 = **8**，与 02 S2 的 7 步描述一致（S2 把「加载」计为步骤 2 内含 errs 汇总，口径差异已核，无遗漏检查点）。✓

## X2 — docstring schema 字段覆盖复核

docstring L15-35 声明的字段 vs load_batch2 实际消费：
- prior.nodes.{parent_id, p_tilde, w1, w2, parent_share} → 代码只查 **w1 + p_tilde**；parent_id/w2/parent_share **无存在性检查**（w2 在 build_schemes 中仅 orig 侧用 w2_exact(p_tilde) 合成、new 侧来自 blindtest——prior 的 w2 字段实际不被任何路径消费）。02 S1 表未显式标注此三点 → **补记**：属 M 类 mismatch 同族（docstring 声明 > 代码检查），并入 M1 处置口径（登记不扩规则）。
- prompt_version → 零消费（M2 ✓ 与 02 一致）。
- blindtest.judge 字段 → 零消费（同上族，补记）。

## X3 — 调用面独立复核

`grep -rn 'crossdomain' bench/ --include='*.py' -l` = 仅 assert-o3-claim-rejudge.py（docstring 文字提及，L7）+ 自身。`grep -rn 'import.*crossdomain\|subprocess.*crossdomain' bench/` = **0 命中**。✓ 与 02 S3 一致：改签名零外溢。

## X4 — 基线捕获复核

`/tmp/cd-before.txt` 独立重跑比对：exit 0 + 两行输出（SIGNAL blocked-on-external / INFO 预注册锚点）与 r146 A1 表记录逐字一致。✓

## X5 — 边界声明

- 本 02.5 只复核 02 的**提取正确性**（检查点枚举、字段覆盖、调用面），方案选型（A/B）由 03 决策、04.5 攻击。
- 样例矩阵设计细节（正/负样例具体内容）属 04 执行产物，不在本阶段范围。