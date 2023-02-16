import kfp
from kfp.components import func_to_container_op


def train():
    print("Trainig model....")

train_op = func_to_container_op(train)

@kfp.dsl.pipeline(
    name="Train Model",
    description="Trains a simple model"
)

def train_pipeline():
    train_task = train_op

if __name__ == "__main__":
    kfp.compiler.Compiler().compile(train_pipeline, "train_pipeline.yaml")