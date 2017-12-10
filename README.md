# gym_pomdp

# Dependency

[OpenAI Gym](https://github.com/openai/gym)

# Installation

```bash
git clone https://github.com/kbys-t/gym_PO.git
cd gym_PO
pip install -e .
```

# How to use
1. First of all,
`import gym_pomdp`

1. Select environment from ``["AcrobotPO-v0", "AcrobotPO-v1", "BallArmPO-v0", "BallArmPO-v1"]`
```python
ENV_NAME = "AcrobotPO-v0"
env = gym.make(ENV_NAME)
```

1. Give degree of POMDP `env.POMDP_PARAM` within `[0.0, 1.0]`

1. Send action and get observation and reward
```python
observation, reward,, done, info = env.step(action)
```
