import os


ZERO_SHOT = "zero-shot"
FEW_SHOT = "few-shot"
LORA_FINE_TUNE = "lora-fine-tune"

TRAIN_FOLDERS = [
    "83",
    "84",
    "85",
    "86",
    "87",
    "88",
    "89",
    "90",
    "91",
    "91_bu",
    "92",
    "92_bu",
    "93",
    "94",
    "95",
    "96",
    "97",
    "98",
    "99",
    "100",
    "101",
    "102",
    "103",
    "104",
    "105",
    "106",
    "107",
    "108",
    "109",
]

VALID_FOLDERS = [
    "110",
    "111",
    "112",
]

CHECKPOINT_DIR = "checkpoint"
os.makedirs(CHECKPOINT_DIR, exist_ok=True)
