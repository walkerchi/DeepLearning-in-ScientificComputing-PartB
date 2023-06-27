from .ffn import MLP,FFN
from .deeponet import DeepONet
from .fno import FNO2d
from .cno import CNO2d, UNet2d
from .kno import KNO2d


# it's only for mesh neural operator trainer
ModelLookUp = { 
        "fno":FNO2d,
        "cno":CNO2d,
        "unet":UNet2d,
        "kno":KNO2d
}