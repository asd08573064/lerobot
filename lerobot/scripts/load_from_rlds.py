from lerobot.common.datasets.push_dataset_to_hub.openx_rlds_format import load_from_raw
from pathlib import Path

videos_dir = Path("./video")
dataset = load_from_raw(
    raw_dir="gs://gresearch/robotics/ucsd_pick_and_place_dataset_converted_externally_to_rlds/0.1.0",
    videos_dir=videos_dir,
    fps=3,   
    video=False,
    openx_dataset_name='ucsd_pick_and_place_dataset_converted_externally_to_rlds',
    split='train',
    topk=5
)


print(dataset['language_instruction'])