import hydra
from omegaconf import DictConfig

@hydra.main(config_path=".", config_name="config", version_base=None)
def main(cfg: DictConfig):
    print(f"learning rate: {cfg.learning_rate}")
    print(f"batch size: {cfg.batch_size}")

if __name__ == "__main__":
    main()