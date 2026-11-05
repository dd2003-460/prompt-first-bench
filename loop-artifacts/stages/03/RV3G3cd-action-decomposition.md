# 阶段 03：行动分解 — RV3G3-threshold-crossdomain-reverify

| # | 行动 | 产出 | 验证方式 |
|---|------|------|---------|
| A1 | 写 `assert-goldrank-crossdomain.py` 骨架：docstring 内嵌 schema 预注册（输入文件最小字段集 + D1-D5 判定语义）+ 三分支主流程（无第二域数据 → SIGNAL blocked-on-external exit 0 / 有数据 → (a)(b) verdict / schema 违例或换题面无声明 → ERROR exit 2） | 脚本落盘 | python3 实跑当前 ablation 面 = SIGNAL + exit 0 |
| A2 | 实现 R2 DP 可达计数枚举器 `reachable_top10_gold_counts(ws, gold)`（跨 cut 组识别 + 席位预算 DP），含单组闭式退化 | 同上（函数级） | M0 双实现互验（暴力 ≤216 置换 vs DP，合成样例） |
| A3 | 第一域回归锚点：骨架复算函数对第一域 7 方案 top-10 计数 == {W1:3, W2-orig:3, W3-orig:4, W4-orig:4, W2-new:2, W3-new:4, W4-new:3}（assert-goldrank-threshold.py L100-101 expected_counts），且 Fraction 排序键与 float 权威路径结果一致（X1 处置实证）；tie 枚举器对第一域输出：W3-orig/W4-orig/W3-new 可达集合 {4}、W2-new 可达 [2,3]（proof L57 锚点） | 同上 | 实跑全 PASS |
| A4 | 变异测试 ≥3 场景：M1 伪造 batch2 数据（稳定过线集）→ (a) PASS + (b) verdict 路径可达；M2 tie-sensitive 构造（过线方案含跨 cut gold 组）→ (b) FAIL；M3 换题面无 gold_nodes 声明 → ERROR fail-loud exit 2；M4 缺 new 侧 JSON → D5 降级对照 + SIGNAL 登记 | 测试记录 | 各场景实测输出逐条核对 |
| A5 | 冻结面零修改验证 + queue 更新材料准备 | git status 输出 | hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / stats-*.json / judge-blindtest-r1.json 全部未触碰 |

**执行顺序**：A1+A2 同文件一次写完 → A3 实跑 → A4 变异 → A5 收口。预估 ~8-10 turns。

**不做清单**（防范围蔓延）：不实现 gmr 方向一致性检查的独立分支（queue 条目提及「gmr 排序方向一致性」——经 02 R4 核对，(a)(b) 两条件本身不含 gmr；gmr 方向一致性是 L4.2 条件 (c) 的附属证据义务，属 DRAFT 改写范畴，非本 assert 对象。此切割登记为 N3，入 04 工件）。