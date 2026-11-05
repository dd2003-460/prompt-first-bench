# 阶段 04：执行验证日志 — RV3G3-threshold-crossdomain-reverify

> 日期：2026-10-30 · 分支 `ralph/rv3g3-threshold-crossdomain-reverify`
> 交付物：`bench/rubric-v3/ablation/scripts/assert-goldrank-crossdomain.py`（schema 预注册骨架，~285 行）

## A1 · 骨架落盘 ✓

脚本结构（与 03 行动表一致）：
- docstring 内嵌 schema 预注册：三输入文件最小字段集（hit-matrix-batch2.json / prior-estimates-batch2.json / judge-blindtest-batch2.json）+ 七方案合成式 + D1-D5 判定语义 + exit code 约定（0/1/2）——byte-stable，后续改协议须走新文件 + APPROVALS
- 三分支主流程：`batch2/` 目录不存在 → SIGNAL blocked-on-external + exit 0；数据齐备 → (a)(b) verdict；schema 违例 → ERROR + exit 2
- 常量锚点：`GOLD_DOMAIN1`、`S1 = {W3-orig, W4-orig, W3-new}`、`T_PASS = 4`（均溯源 goldrank-threshold-proof.md L55/L57/L83）

**当前 ablation 面实跑**（无 batch2 数据，常态）：
```
[SIGNAL] blocked-on-external: batch2 data absent (等 batch2 数据落盘 bench/rubric-v3/ablation/batch2/ 后零改动接入)
[INFO] 预注册锚点: S1=['W3-new', 'W3-orig', 'W4-orig'], T_PASS=4, GOLD_DOMAIN1=['N-2.1', 'N-3.2.2', 'N-2', 'N-4', 'N-1.3']
exit=0
```
✓ 验收标准第 1 条达成。

## A2 · DP 可达计数枚举器 ✓（含两处现场修复）

`reachable_top10_gold_counts(ws, gold)`：跨 cut 组识别 + 席位预算 DP。**本阶段发现并修复两个 bug**（均为 M0 fuzz / 回归锚点暴露，非一次写对——如实登记）：

- **Bug #1（累计名次）**：初版用组序 `enumerate` idx 当名次起点，前组大小 >1 时跨 cut 分类错位。修复：running `pos` 累加器（`lo_pos, hi_pos = pos, pos+len(members)-1`）。
- **Bug #2（精确席位预算）**：M0 fuzz 50 seeds 中 2 个 diff（seed=9: DP=[2,3,4] vs BF=[3,4]；seed=30: DP=[3,4,5] vs BF=[4,5]）。根因：不同权重组间不可交错，故所有跨 cut 组的席位占用之和被钉死为 `Σk_j == 10 − above_members`（above_members = 整组在 cut 上方的组成员总数）；DP 转移枚举 k 从 0 起后终态未过滤，used < budget 的幻影状态泄漏出偏低计数值。修复：终态只保留 `u == 10 − above_members` 的状态。docstring「实现注记」段已同步改写（旧版「k 下限兜底靠暴力互验」表述作废）。

## A3 · 第一域回归锚点 ✓（18/18 PASS）

| 检查 | 结果 |
|------|------|
| 7 方案 top-10 gold 计数 == {W1:3, W2-orig:3, W3-orig:4, W4-orig:4, W2-new:2, W3-new:4, W4-new:3}（assert-goldrank-threshold.py expected_counts） | 7/7 PASS |
| Fraction 排序键 vs float 排序键 top-10 成员序列逐方案一致（X1 待实证项闭环） | 7/7 PASS |
| tie 可达集合：W3-orig/W4-orig/W3-new = [4]、W2-new = [2,3]（proof L57 锚点），且 DP == 暴力全枚举 | 4/4 PASS |

X1 结论：**Fraction 键与 float 键在本数据面上完全等价**（权重均为 limit_denominator(10**6) 产物，float 表示无边界翻转）；骨架维持更严格的 Fraction 键。

## M0 · DP vs 暴力互验 ✓

50 个随机种子（n∈[12,16] 节点、gold 5 节点、权重池 ≤8 种 Fraction 值制造大量并列）：修复前 2/50 DIFF → **修复后 50/50 ALL MATCH**。

## A4 · 变异测试 ✓（4 场景，全部实测输出核对）

临时 fixture 写入 `bench/rubric-v3/ablation/batch2/`，测毕即删（A5 确认目录已不存在）：

- **M1 稳定镜像**（batch2 = 第一域数据原样复制）→ `[PASS] (a) S2==S1∩域` + `[PASS] (b)` 三过线方案全 tie-robust，exit 0 ✓
- **M2 tie-sensitive 构造**（11 节点：8 个 distinct 高位 + 3 节点同权跨 cut 组含 2 gold + 3 低位；gold_nodes 显式声明）→ 基准序计数 4 过线，可达集合 [3,4]（DP==BF）→ `[FAIL] (b) tie-sensitive 过线方案: ['W1','W2-orig','W3-orig','W4-orig']`，exit 1 ✓（注：该构造同时触发 (a) FAIL——四方案全过线与 S1∩域={W3-orig,W4-orig} 不一致，属预期，两 FAIL 路径同轮实证）
- **M3 schema 违例 fail-loud**：M3a 必需文件缺失 → `[ERROR] hit-matrix-batch2.json missing` exit 2 ✓；M3b 换题面声明 ghost gold_nodes 而 hit-matrix 无对应节点 → `[ERROR] hit-matrix run1: gold node GHOST-1 absent` exit 2 ✓
- **M4 缺 new 侧 JSON**（prior+hit-matrix 镜像、blindtest 删除）→ `[SIGNAL] D5 降级` + orig 侧对照 `[PASS] (a)`（S2={W3-orig,W4-orig}==S1∩域），exit 0 ✓

## A5 · 冻结面零修改 ✓

`git status --porcelain` 仅一行：`?? bench/rubric-v3/ablation/scripts/assert-goldrank-crossdomain.py`（新增文件）。逐一核验 UNTOUCHED：hit-matrix.json / prior-estimates.json / gold-tree.md / judge-blindtest-r1.json；runs-C0-run*.md 与 stats-*.json 无 diff。`__pycache__/` 测试副产物已清理。

## 负面结果 / 边界登记

- **N3（承接 03 不做清单）**：gmr 方向一致性检查未实现——L4.2 条件 (c) 附属证据义务，属 DRAFT 改写范畴，非 (a)(b) 机判对象。
- **N4（本阶段新增）**：(b) 审计只对**过线方案**做可达性检查（设计如此：tie-sensitivity 的威胁是「过线资格翻转」）。若未来需要「未过线方案能否 tie 到 ≥4」（假阳性方向），需扩展 s2 遍历范围——当前 docstring 未承诺该方向，不视为缺口，仅登记防误读。
- **N5（本阶段新增）**：M2 构造中 W2-orig 可达集合出现 [0..5] 全区间（p_tilde=null → w2_exact=F(1) 全并列），说明 DP 在全并列退化情形下仍正确（与 BF 一致），但实际第二域数据若出现大规模 p_tilde=null，(b) 会大面积 FAIL——这是**正确的 fail-loud 行为**（数据质量信号），非算法缺陷。

## 结论

验收标准 5 条中 4 条本阶段闭环（queue 更新在收口步骤）。进 04.5 反方复核。