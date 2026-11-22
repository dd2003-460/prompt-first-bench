# Judge v1.0 coverage 层 MAGNET 伪影（2026-11-23）

## 问题

B-r1（idea2, 401 节点）judge cov = 0.0，A-r1（316 节点）cov = 0.222。
401 节点只可能比 316 节点覆盖更多 gold，cov 却从 0.22 掉到 0——方向反了。
这是测量伪影，不是真实覆盖。

## 根因：MAGNET_LIMIT=3 是二元开关，不是上限

`judge_v1.py layer_coverage`：一个 gold unit 被 ≥3 个节点命中 → 该 unit
**整个从 confirmed 剔除**（不是"只数 3 次"，是清零）。

```python
magnets = {g for g, c in absorb.items() if c >= MAGNET_LIMIT}  # c>=3
confirmed = {top1[i] for i in range(len(nodes))
             if matched[i] and top1[i] not in magnets}          # magnet 全剔
score = len(confirmed) / len(gold_units)
```

高节点 run（300+）里，热门 gold unit 天然被 3+ 节点命中（同一概念多个
节点从不同角度表述），于是被清零。节点越多 → 越容易触发 magnet →
cov 反而越低。**coverage 轴对高节点 run 是反相关的测量伪影。**

## 验证（source ①，2026-11-23 bge-m3 重算）

| run | n_nodes | matched(≥0.70) | 去重 cov (unit命中≥1算1) | magnet 排除 cov |
|---|---|---|---|---|
| A-r1 | 316 | 50 | **0.3889** (14 units) | 0.2222 |
| B-r1 | 401 | 42 | **0.2222** (8 units) | 0.0000 |

- A-r1：50 个节点命中，去重后 14 个 gold unit；6 个 unit 被 magnet 吞 → 剩 8
- B-r1：42 个节点命中，去重后 8 个 gold unit；8 个 unit 全被 magnet 吞 → 剩 0
- B-r1 的 8 个命中 unit 全部 ≥3 次命中（共享 122 节点 ckpt 前缀反复命中同一批 unit）

## 正确的 coverage 定义

coverage 应该测"模型覆盖了多少 gold unit"= **去重计数**（每个 unit 命中≥1次
算 1 次，封顶 1）。magnet 规则的本意是防"一个 unit 被冗余节点刷分"，
正确实现是去重（数一次），不是清零（剔整个 unit）。

## 对 workshop 的影响（待 K7 15-run 重算确认）

若"峰在 150"部分是 cov 被 magnet 伪影压出来的（150 节点中等、magnet 触发少，
719 节点多、magnet 触发多 → cov 被压低 → 150 相对显高），则 finding 3 的
budget–quality 曲线形状是 judge 伪影，不是实验发现。

**K7 15-run 去重 cov 重算**：后台跑（bge-m3 编码 15 run），结果出来后
复算权重消融，看峰还在不在 150。若去重口径下峰消失或移位 → finding 3 需重写，
breadth-vs-depth 结论（基于实际节点数）可能仍是稳健部分。

## 修复方向（未实施，等 D 确认）

1. **最小修复**：layer_coverage 的 confirmed 改用去重计数（unit 命中≥1 算 1），
   删掉 magnet 清零逻辑。MAGNET_LIMIT 常量保留但不再用于剔除。
2. **影响范围**：所有用 cov 的下游（judge total、K7 曲线、idea2 对比、
   metacog 轴的 cov 分量）需重算。
3. **不可逆性**：judge v1.0 是 FROZEN 的，改 cov 层 = 解冻重校准。
   但伪影是硬 bug（方向反了），不改 = 发表一个测量错误的轴，更糟。

## 文件

- judge: `modules/B-pipeline-ablation/judge_v1.py` (layer_coverage, MAGNET_LIMIT=3)
- 本记录: `modules/B-pipeline-ablation/research/judge-v1-magnet-artifact-20261123.md`
- K7 重算: 后台 proc_bc55409e9fa1, 输出 /tmp/k7-dedup-cov.json
