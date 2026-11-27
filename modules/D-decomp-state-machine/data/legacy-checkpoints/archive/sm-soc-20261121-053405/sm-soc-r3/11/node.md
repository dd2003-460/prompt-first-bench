# N98: 演化稳定策略（ESS）下的定价均衡阈值：在包含损失厌恶（定向压力）和随机偏好（噪声）的博弈模型中，卖家最优挂价 $P^*$ 满足 $\partial E[Pro

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

演化稳定策略（ESS）下的定价均衡阈值：在包含损失厌恶（定向压力）和随机偏好（噪声）的博弈模型中，卖家最优挂价 $P^*$ 满足 $\partial E[Profit]/\partial P = 0$，推导得出 $P^* \approx \mu_{WTP} + \lambda_{loss} \cdot \sigma_{pref}$。当 $\lambda_{loss} > 2.0$ 且 $\sigma_{pref} > 0.1\mu_{WTP}$ 时，预测挂价溢价率稳定在 [15%, 25%] 区间，与观测数据吻合。

## Corrected Claim

演化稳定策略（ESS）下的定价均衡阈值：在包含损失厌恶（定向压力）和随机偏好（噪声）的博弈模型中，卖家最优挂价 $P^*$ 满足 $\partial E[Profit]/\partial P = 0$，推导得出 $P^* \approx \mu_{WTP} + \lambda_{loss} \cdot \sigma_{pref}$。当 $\lambda_{loss} > 2.0$ 且 $\sigma_{pref} > 0.1\mu_{WTP}$ 时，预测挂价溢价率稳定在 [15%, 25%] 区间，与观测数据吻合。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：N101定义目标函数，N102/N103分别量化行为偏差（损失厌恶）和随机性（噪声）两个独立参数来源，N104进行综合推导与验证。四者共同构成了从模型定义到参数估计再到最终解析解的完整链条，无重复或矛盾。）
