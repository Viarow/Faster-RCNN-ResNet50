class Config:
    model_weights = "./checkpoints/resnet50_fpn"
    image_path = "../COCODevKit/test2017/000000250101.jpg"
    gpu_id = '0'
    num_classes = 80 + 1
    data_root_dir = "../COCODevKit/"
    fig_path = "./imgs/test.png"


test_cfg = Config()
