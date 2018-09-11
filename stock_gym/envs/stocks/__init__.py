"""Initialize the env.stocks module"""

from gym.envs.registration import registry, register, make, spec

# Public classes
from stock_gym.envs.stocks.basic import LinMarketEnv, NegLinMarketEnv,\
                                        SinMarketEnv, OHLCVMarketEnv

from stock_gym.envs.stocks.imarket import IMarketEnv


register(
    id='SinMarketEnv-v0',
    entry_point='stock_gym.envs.stocks:SinMarketEnv',
    )

register(
    id='LinMarketEnv-v0',
    entry_point='stock_gym.envs.stocks:LinMarketEnv',
    )

register(
    id='NegLinMarketEnv-v0',
    entry_point='stock_gym.envs.stocks:NegLinMarketEnv',
    )

register(
    id='FakeMarketEnv-v0',
    entry_point='stock_gym.envs.stocks:FakeMarketEnv',
    )

register(
    id='OHLCVMarketEnv-v0',
    entry_point='stock_gym.envs.stocks:OHLCVMarketEnv',
    )
