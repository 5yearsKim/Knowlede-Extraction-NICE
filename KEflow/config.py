# CLSTYPE in ["BASICCNN", "LENET5", "RESNET", "VGG", "WRN"]
TYPE_CLS = "WRN"
# TYPE in ["GLOW", "NICE", "REALNVP"]
TYPE_FLOW = "NICE"
# TYPE in ["DIGIT", "FASHION", "SVHN", "CIFAR"]
TYPE_DATA = "CIFAR"

'''classifier config'''
CLS_CONFIG = {
    # train_config
    "BATCH_SIZE":128,
    "LR": 1e-3,
    "WD": 1e-3,
    "EPOCHS": 20,
    "PRINT_FREQ":1000,
    "VAL_FREQ": 1,
    # model config
    "NC":3,
    "N_CLASS":10,
    "IM_SIZE":32,
}

""" NICE Extractor config """
FLOW_CONFIG = {
    # Dataset
    "NUM_SAMPLE" : 10000,
    # Extractor config
    "SPREAD_S":0.05,
    "GRAVITY_S": 0., 
    "BN_S": 5.,
    # train config
    "LR":2e-5,
    "WD":1e-2,
    "SMOOTHE":0.,
    "BATCH_SIZE":128,
    "EPOCHS":100,
    "PRINT_FREQ":100,
    "VAL_FREQ":1,
}



