'''
The configuration system.

If we have any setting that require affect whole ep system or the config
require eq to restart, those configs should place here.

This module will export a singleton of ``Config`` -- ``config``.
'''


__all__ = (config,)


class Config:
    '''
    Main configuration here.

    If a property consider as *readonly*, we will use ``property`` decorator
    for it.
    '''
    ...


config = Config()
