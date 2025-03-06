from bokeh.io import output_file
import yaml


def create_config(username,is_training,model,root_path,data,target,pre_len):
    # 定义配置信息
    config = {
        "task_name": "long_term_forecast",
        "is_training": is_training,
        "model_id": "test",
        "model": model,  # 替换为实际模型名称

        "data": data,  # 替换为实际数据文件名
        "root_path": root_path + username,  # 替换为实际路径
        "data_path": data + ".csv",  # 替换为实际路径
        "features": "M",
        "target": target,  # 替换为实际目标变量
        "freq": "h",
        "checkpoints": "./checkpoints",

        "seq_len": 96,
        "label_len": 0,
        "pred_len": pre_len,

        "mask_rate": 0.25,

        "anomaly_ratio": 0.25,

        "top_k": 5,
        "num_kernels": 6,
        "enc_in": 2,
        "dec_in": 2,
        "c_out": 2,
        "d_model": 16,
        "n_heads": 8,
        "e_layers": 2,
        "d_layers": 1,
        "d_ff": 32,
        "moving_avg": 25,
        "factor": 3,
        "distil": True,
        "dropout": 0.1,
        "embed": "timeF",
        "activation": "gelu",
        "output_attention": True,
        'channel_independence': 1,
        'decomp_method': 'moving_avg',
        'use_norm': 1,
        'down_sampling_layers': 3,
        'down_sampling_window': 2,
        'down_sampling_method': 'avg',
        'use_future_temporal_feature': 0,
        'mask_rate': 0.25,
        '--anomaly_ratio': 0.25,

        "num_workers": 10,
        "itr": 1,
        "train_epochs": 5,
        "batch_size": 16,
        "patience": 10,
        "learning_rate": 0.01,
        "des": "test",
        "loss": "MSE",
        "lradj": "type1",
        "use_amp": False,

        "use_gpu": True,
        "gpu": 0,
        "use_multi_gpu": False,
        "devices": [0, 1],

        "p_hidden_dims": [128, 128],
        "p_hidden_layers": 2
    }

    #保存YAML文件
    output_file = root_path + "\\" + username + "\\" + "cfg" + "\\config.yaml"
    with open(output_file, 'w') as f:
        yaml.dump(config, f,sort_keys=False)

    print(f"配置文件已经保存为{output_file}")