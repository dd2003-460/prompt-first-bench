# 修复①：L1 objective factors 注入逐层 decompose prompt（治 nat b 型维度盲区）

> origin: ai · 2026-11-26 · 依据 `experiments/stage-ablation/nat-failure-mode-20261126.md` §6 修复优先级①

## 背景（sub 不需再查）

- nat 278 节点树失败模式判定 = b（维度盲区）主导：LFU 频率表老化机制 0 节点承载，根因 = L1 解析出的 objective **从未进任何后续 prompt**（grep 18 处实证，:510-511 注释"不进后续 prompt"）
- 加强证据：sm-nat checkpoint 的 objective.factors[3] 明确点名"1%/天更新率"约束——模型 L1 知道该维度，后续层看不到
- **设计约束（Decision 19 原意）**：objective 当初故意不进 prompt，角色是"机器侧对照基准（G9 gold 维度集的免费替代初稿），不是刷分目标"。注入必须保持这个性质 → 措辞框架 = **维度覆盖检查清单**，不是"朝这些因素优化"

## 代码位置（pfb/experiments/stage-ablation/s5_state_machine.py）

| 位置 | 内容 |
|------|------|
| :461 | `self.objective: Optional[dict] = None` 声明 |
| :514 | L1 轮赋值 `self.objective = objective`（dict: composition/factors/rationale） |
| :543-600 | `_decompose_layer(parents)`：prompt 构造。三个注入槽先例：`confirmed_block`(:547)、`contradiction_block`(:575-584)、`edge_block`(:556-569)；:586 `prompt = self._safe_prompt(P1H_INDEX, question=..., confirmed_block=..., parents_block=..., start=...)` |
| :1009 | objective 已随 checkpoint 落盘（resume 自动恢复，无需新字段） |
| 文件尾 | argparse（grep `add_argument` 定位） |

## 改动设计

1. **argparse 加 `--obj-inject`**（store_true，默认 OFF）→ `self.obj_inject = args.obj_inject`
2. **`_decompose_layer` 内构造 `objective_block`**（仿 contradiction_block 模式）：
   - 条件：`self.obj_inject and self.objective` 且 `self.objective.get("factors")` 非空
   - 内容：composition 一行 + factors 列表（≤4 条，每条截 60 字）
   - 措辞框架（必须体现"覆盖清单非刷分目标"）：
     ```
     【维度覆盖检查清单（L1 层自估的终点目标维度，仅用于检查覆盖、不是刷分目标）】
     组合：<composition>
     - <factor1>
     - <factor2>
     ...
     展开父节点前检查：该父节点的子维度是否覆盖了上述维度中尚未在树内出现的项？
     未覆盖的维度优先展开；已覆盖的不要重复拆。
     ```
   - 注入位置：追加到 `confirmed_block`（与 contradiction_block 同款拼法），不动 P1H_INDEX 模板
3. **不改** `s5_pipeline.py` 的 P1H_INDEX 模板；不加 checkpoint 新字段；OFF 时行为与现状逐字节一致

## 验收（全过才算完成）

- [x] 2026-11-26 17:51 完成（sub deleg_769faae1，报 failed 但磁盘核验全过，死在汇报 repetition loop）：commit `edce50b28`（23 行改动，仅 s5_state_machine.py）；测试 `scratch/test_obj_inject.py` 三断言全 PASS（ON 注入/OFF 不注入/objective=None 不注入），Lead 17:58 复跑确认 EXIT=0；resume 路径核验：objective 随 checkpoint 落盘（:1027）→ resume 恢复（:1763），fresh/resumed 均生效

1. **离线 monkeypatch 测试**（不碰 8787）：python 片段构造/加载 SM 实例（可从 `checkpoints/sm-nat-r1/` resume 或直接构造对象设 `self.objective`），monkeypatch `call_llm` 捕获 prompt：
   - flag ON：assert factors 文本出现在 prompt
   - flag OFF：assert 不出现
   - 测试脚本放 `/Users/a1-6/.hermes/cache/scratch/`，不留仓内
2. `git add experiments/stage-ablation/s5_state_machine.py && git commit -m 'fix(s5-sm): --obj-inject L1 objective factors 注入逐层 decompose(维度覆盖清单框架, 默认OFF, 治nat b型盲区)'`，**不 push**
3. summary ≤6 行：改动行数 + 两条断言结果 + commit hash

## 边界

- 只改 `s5_state_machine.py` 一个文件；不跑完整 nat run（不占 8787）；不 stash/checkout/切分支；不碰其他 runs/checkpoint

## 任务表

| 任务 | 依赖 | 读(行) | 写(行) | commits | 载体 |
|------|------|--------|--------|---------|------|
| 改 argparse + _decompose_layer 注入 | - | ~80 | ~40 | 1 | sub-27b |
| 离线 monkeypatch 双断言测试 | 上 | ~30 | 0(脚本在 scratch) | 0 | sub-27b(同卡) |
