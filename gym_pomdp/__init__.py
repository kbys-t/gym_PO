import logging
from gym.envs.registration import registry, register, make, spec

logger = logging.getLogger(__name__)

register(
    id='AcrobotPO-v0',
    entry_point='gym_pomdp.envs:AcrobotIsEnv',
)

register(
    id='AcrobotPO-v1',
    entry_point='gym_pomdp.envs:AcrobotEmaEnv',
)

register(
    id='BallArmPO-v0',
    entry_point='gym_pomdp.envs:BallArmIsEnv',
)

register(
    id='BallArmPO-v1',
    entry_point='gym_pomdp.envs:BallArmEmaEnv',
)
