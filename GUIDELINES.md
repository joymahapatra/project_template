# Guidelines
* [saved](saved/) contains log files, model outputs, checkpoints, etc.
* [utils.py](utils.py) conatains logger, command-line-arguments, etc.
* Always train from checkpoint.
* Checkpoints in `dict`
    ```python
    {
        "name": architecture_name,
        "time": time,
        "epoch": epoch,
        "model_state_dict": model_state_dict,
        "optimizer_state_dict": optimizer_state_dict,
        "best": path_or_epoch_or_bool,
        "configuration": config_json_to_dict,
    }
    ```