# Copyright (c) SenseTime Research. All rights reserved.

attr_dict = dict(
    interface_gan={ # strength
        'upper_length': [1],
        'bottom_length': [1]
    },
    stylespace={ # layer, strength, threshold
        'upper_length': [5, 5, 0.0028], 
        'bottom_length': [3, 5, 0.003] 
    },
    sefa={ # layer, strength
        'upper_length': [[4, 5, 6, 7], -5],
        'bottom_length': [[4, 5, 6, 7], 5]
    }
)