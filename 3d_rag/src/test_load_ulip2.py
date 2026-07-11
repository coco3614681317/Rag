import torch
from easydict import EasyDict

from models.ULIP_models import ULIP2_PointBERT_Colored


args = EasyDict({
    "model": "ULIP2_PointBERT_Colored",
    "npoints": 8192,
    "evaluate_3d_ulip2": True,
    "evaluate_3d": False,
})


print("Creating model...")

model = ULIP2_PointBERT_Colored(args)

print("Model created")


ckpt_path = r"D:\3D\3d_rag\models\ULIP\checkpoints\ULIP-2-PointBERT-8k-xyz-pc-slip_vit_b-objaverse-pretrained.pt"


checkpoint = torch.load(
    ckpt_path,
    map_location="cpu",
    weights_only=False
)


msg = model.load_state_dict(
    checkpoint["state_dict"],
    strict=False
)


print("Checkpoint loaded")
print(msg)

print("OK")