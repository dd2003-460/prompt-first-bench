# 阶段 02.5：交叉核对 — RV3G3-threshold-crossdomain-reverify

## 核对方法
仓库内交叉（无外部通道；web-llm 三 provider 登录态失效为已知状态，本 goal 无外部事实主张，不触发 web-llm 义务——登记于此防误判缺口）。三个独立核对视角：

## X1 · 协议一致性核对（骨架 vs 第一域权威脚本）
逐要素对照 R1 表与 `assert-goldrank-threshold.py` L38-42/L90-104 原文：
- w2_exact 公式 ✓（含 EPS=0.01、limit_denominator(10**6)、+1 三细节）
- 七方案合成式 ✓（orig 侧 4 式 + new 侧 3 式，new 侧 W4=w1+w2 非 w3 变体——与 g3-w3w4-completion.md L13「W4=w1+w2」一致）
- top-10 排序键 `(-float(w), nid)` ✓（注意 float() 转换——Fraction 直接比较亦可但须与权威脚本同型，防 limit_denominator 近似值在 float/Fraction 比较下出现边界翻转；实测两实现等价，因权重值均为 limit_denominator(10**6) 产物，float 表示精确到该分母无需舍入歧义——⚠️ 此论断需 04 变异测试加一格实证：构造两个 limit_denominator 后 float 相等但 Fraction 不同的权重，确认排序结果一致或显式改用 Fraction 比较。**处置**：骨架直接用 Fraction 比较（key=(-w, nid)，w 为 Fraction），比 float 更严格，且对第一域数据复算结果必须与权威脚本完全一致（回归锚点），若不一致则说明 float 路径有隐藏行为，如实登记。）

## X2 · DP 枚举器正确性核对（R2 引理 vs 暴力枚举）
小样例上双实现互验：构造 ≤3 个跨 cut 组、组大小 ≤3 的合成权重表（总置换 ≤ 6³=216 可暴力全枚举），DP 可达计数集合 == 暴力枚举集合。此验证作为 04 阶段变异测试 M0（自测锚点），不在本阶段执行。
另核对闭式退化：单跨 cut 组情形 DP 输出 == R2 闭式区间端点。

## X3 · 判定语义核对（D3/D5 vs L4.2 原文）
- (a)「过线集合跨域稳定」→ S₂==S₁ PASS 是否过严？L4.2 原文只说「稳定」未定义量化 → D3 三分支是预注册解释，**非原文强约束**——已在 01 标注为设计决策，04.5 复核时列为「成璐可推翻项」。✓ 无伪装
- (b)「过线集合在全部合法 tie-break 下不变」→ 骨架实现 = 「每个过线方案计数恒 ≥4」（即过线资格不变），与原文「过线集合不变」等价吗？不等价于「集合成员排名不变」——原文指**哪些方案过线**（集合层面），不是方案间相对顺序。骨架语义 = 每方案过线资格 robust → 集合不变 ✓ 对齐。
- D5 同方案名对照：S₁ 中 new 侧方案在第二域缺数据时不参与对照——这是「对照集 = 两域交集」的自然读法，非新增假设。✓

## X4 · 常态出口语义核对（D4: SIGNAL exit 0 vs FAIL exit 1）
r136 kappa-receipt 选 FAIL exit 1 的理由：回执缺失 = 门禁违规（评分无效）。本 goal 数据缺失 = 外部等待（非违规）→ SIGNAL exit 0 更贴切。反方视角：exit 0 会让 CI/轮询误判「已验证通过」？**缓解**：SIGNAL 行显式打印 `blocked-on-external: batch2 data absent`，且 queue 条目保持未划掉状态——双重标记防误读。维持 D4，04.5 再攻一次。

## 结论
X1 一处待实证（float vs Fraction 排序键）→ 转 04 行动 A3；X2/X3/X4 无阻塞。阶段判定 **pass**，进 03。