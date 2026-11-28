# 任务卡 K1 — 生成 S1 剥离版 prompt（域中性副本，生产零改动）
> 你是纯执行 sub。本卡是唯一指令来源。零改动生产文件（只复制+改副本）。git commit 由你做（见 S4）。
> 设计依据: `tasks/oood-general-probe/kernel-config-split.md` §2（不要读其他文件做判断）。

## S0 步骤
### S1 建副本
```bash
mkdir -p /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/s1
cp /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/s5_state_machine.py /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/s1/s5_state_machine.py
cp /Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/D-decomp-state-machine/scripts/prompts.py /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/s1/prompts.py
```

### S2 应用 11 处替换（old→new 逐字，用 patch 工具；⑪ 用 replace_all）
**文件 A: `oood-probe/s1/s5_state_machine.py`（6 处）**

A1. old:
```
f"【关键】上面列出的每一个公式（如 TCO 公式、roofline 公式、KV Cache 计算、"
             f"故障损耗项、利用率分解等），必须在你的回答中完整保留并代入具体数值，"
```
new:
```
f"【关键】上面列出的每一个公式（如本题域内的关键公式与数值链），"
             f"必须在你的回答中完整保留并代入具体数值，"
```

A2. old: `如果不同事实之间存在矛盾（如不同 head_dim 取值），取多数一致的值并注明分歧。`
new: `如果不同事实之间存在矛盾（如同一参数在不同节点的取值），取多数一致的值并注明分歧。`

A3. old:
```
f"【关键】上面各层摘要中出现的每一个公式、数值、参数（如 TCO 公式、roofline 公式、"
               f"KV Cache 计算、故障损耗项、利用率分解、临界阈值等），必须在最终答案中显式保留并代入具体数值，"
```
new:
```
f"【关键】上面各层摘要中出现的每一个公式、数值、参数（如本题域内的关键公式、数值与参数），"
               f"必须在最终答案中显式保留并代入具体数值，"
```

A4. old: `如果各层之间存在矛盾（如不同 head_dim 取值），取多数一致的值并注明分歧。`
new: `如果各层之间存在矛盾（如同一参数在不同节点的取值），取多数一致的值并注明分歧。`

A5. old: `（如频率表老化、热度漂移、容量覆盖不足），不能只讲优势不讲上限；`
new: `（如本题域内的主要限制因素），不能只讲优势不讲上限；`

A6. old: `f"如果事实中有隐含的推导步骤（如「年 OpEx = 4×450W×8760h×电价」），也要显式写出来。"`
new: `f"如果事实中有隐含的推导步骤，也要显式写出来。"`
（注: A6 在 `_FULL` 块内，默认路径不激活；一并剥是为了 S1 文件级纯净。若 old 串与文件不符（±标点），以文件实际文本为准做最小等价替换并在汇报注明。）

**文件 B: `oood-probe/s1/prompts.py`（5 处，⑪ 计 5 个位置）**

B1. old: `（如温度采样、量化噪声、batch 组成波动）`
new: `（如传感器噪声、队列波动、环境扰动）`

B2. old: `例：推理稳定性 ← temp 采样 → 输出一致性；量化质量 ← 同一 temp 流 → 精度损失。`
new: `例：系统稳定性 ← 同一噪声源 → 输出一致性；估计精度 ← 同一噪声源 → 误差传播。`

B3. old: `（如「推理稳定性」← temp 采样 → 一致性+精度）`
new: `（如「系统稳定性」← 噪声源 → 一致性+精度）`

B4. old: `即对题目所问的决策/结论，给出在不同时间跨度与口径下（与该决策相关的、题目隐含或显式要求的时间维度）的最优选择及其量化依据。`
new: `即对题目所问的结论/答案（决策/解释/点估计/规划皆可），给出其量化依据与必要的限定条件。`

B5. old: `（容量、比率、价格、复杂度、带宽）`
new: `（数值、比率、参数、约束量）`

B6(replace_all). old: `不要输出具体硬件参数、具体公式推导、具体数值`
new: `不要输出具体参数、具体公式推导、具体数值`
（预期 5 处命中；若命中数≠5，汇报实际数，不强行凑。）

### S3 验证（全部通过才算 done）
1. 残留域味 grep（对两个 S1 文件，排除 `#` 注释行）:
```bash
grep -n "TCO\|roofline\|Roofline\|KV Cache\|head_dim\|故障损耗\|温度采样\|temp 采样\|量化噪声\|硬件参数\|频率表老化\|热度漂移\|最优选择\|OpEx" oood-probe/s1/s5_state_machine.py oood-probe/s1/prompts.py | grep -v "^\s*#"
```
预期: 0 命中（注释行允许残留，汇报列出即可）。
2. 语法编译: `python3 -m py_compile oood-probe/s1/s5_state_machine.py oood-probe/s1/prompts.py`
3. 导入冒烟（不跑 LLM）:
```bash
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation && python3 -c "
import sys
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/s1')
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation')
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/D-decomp-state-machine/scripts')
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/A-eval-infra/scripts')
import prompts, s5_state_machine
assert prompts.__file__.endswith('oood-probe/s1/prompts.py'), prompts.__file__
assert s5_state_machine.__file__.endswith('oood-probe/s1/s5_state_machine.py'), s5_state_machine.__file__
print('IMPORT-OK', prompts.__file__)
"
```
预期: IMPORT-OK 且路径指向 s1/。

### S4 commit
```bash
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech && git add experiments/stage-ablation/oood-probe/s1/ && git commit -m "exp: S1 剥离版核 (11 处域味→域中性, 生产零改动, 导入冒烟过)"
```

## 汇报（≤5 行）
1. 11 处替换各命中几次（B6 实际命中数）
2. 残留 grep 结果（0 或列出注释行）
3. py_compile + IMPORT-OK 是否过
4. commit hash
5. 任何与任务卡不符的偏差（old 串不匹配等）

## 边界
- 生产文件 `experiments/stage-ablation/s5_state_machine.py` 和 `modules/D-decomp-state-machine/scripts/prompts.py` 一个字都不许动
- 不碰 run_q9_gated.py / checkpoints/ / 8787（本任务零 LLM 调用）
- 不做任何实验运行
