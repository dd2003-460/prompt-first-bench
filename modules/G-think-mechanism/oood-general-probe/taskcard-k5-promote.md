# K5 任务卡: 剥离版转正 — 5 处域中性替换应用到生产核

> 判决依据: oood-column-status.md K4b 判决（格 1 负资产, 域味该删, 2026-11-27）+ kernel-config-split.md §2（5 处替换规格, 单变量）。
> 被测 S1 配置 = 生产文件 + 恰好这 5 处替换。转正必须复现该配置, 多一处少一处都破坏单变量。

## 目标文件（唯一可改）
`/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/s5_state_machine.py`

## 步骤
1. 读 `/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/G-think-mechanism/oood-general-probe/kernel-config-split.md` §2（5 处替换规格, ~25 行, 含每处的目标替换串）。
2. 定位: 对每处 spec 原文, 先 `grep -n` 精确匹配; 匹配不到用短子串锚点（"TCO 公式"/"head_dim"/"温度采样"/"最优选择"/"容量、比率"/"硬件参数"）定位行号, 再 read 该行 ±15 行确认语义位置。已知漂移（Lead 预核）:
   - TCO 公式清单（spec 处 1）当前在 ~L1621 和 ~L1641 出现 **2 处**, 第二处多"、临界阈值"——两处都替换（同一语义位置, 用 spec 目标串）。
   - head_dim 例（spec 处 1b）当前 ~L1624/~L1644 2 处, 都替换。
   - spec 处 3/4/5（"最优选择"/"容量、比率、价格、复杂度、带宽"/"具体硬件参数"）精确串可能已漂移——用锚点找当前等价位置。
3. 逐处 patch（只动这 5 处, 其余一字不改）。替换文本 = spec §2 的目标串; 若当前串与 spec 原文略有出入, 保持 spec 替换意图, 适配当前上下文, 适配处记入映射表。
4. 验证（全过才算完成）:
   - `python3 -m py_compile s5_state_machine.py`
   - `git diff --stat` 只该文件, 行数 ≤15
   - grep 确认: 新串在位 + 旧域味串清零（"TCO 公式"、"roofline 公式"、"KV Cache"、"head_dim"、"温度采样"、"量化噪声"、"batch 组成" 在 prompt 字符串内 0 命中; 注释里的 roofline 说明文字不算 prompt, 不动）
   - **不要碰**: EDGE_TYPE_PROMPT/PREDICT cartesian 段的 GPU 例（~L233/L253）——不在 spec 5 处内, 被测 S1 也没动它, 多改破坏单变量。
5. commit（pfb repo, main）: `OOD K5: 剥离版转正 — 生产核应用 kernel-config-split §2 五处域中性替换 (K4b 格1负资产判决, 单变量复现被测 S1)`
6. 汇报 JSON: `{"mapping": [5 行: spec处号|spec原文|当前行号|当前串摘录|是否适配], "diff_stat": "...", "commit": "...", "verify": {"py_compile":"ok", "grep_old_zero": true, "gpu_example_untouched": true}, "anomalies": [spec 串无当前对应的位置, 若有]}`

## 边界
- 只改 5 处; 不动超参（ObjectiveConfig 默认值保留——超参层"核默认+域覆盖"机制是 spec §1 明确保留项, 不是本次范围）
- 不动 s1/ 副本、不动 prompts.py（若存在）、不动其他文件
- spec 串真无对应（非漂移, 是已被别的改动移除）: 不自作主张找替代位置, 标 anomalies 跳过该处并汇报
- 不 push（Lead 推）
- 无在跑 run 依赖此文件（Lead 已核: 95936 死, 无其他进程 import 它）
