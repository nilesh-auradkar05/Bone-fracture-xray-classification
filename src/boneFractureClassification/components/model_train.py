import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

from pathlib import Path
from PIL import ImageFile

from boneFractureClassification.config.configuration import ModelTrainingConfig
import datetime


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        ImageFile.LOAD_TRUNCATED_IMAGES = True

        self.config = config
        self.__current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.model_filename = f"custom_model_train_{str(self.__current_datetime)}"
        self.checkpoint = ModelCheckpoint(
            filepath=f"artifacts/training/{self.model_filename}.h5",
            monitor="val_loss",
            mode="auto",
            save_best_only=True,
        )
        self.early_stopping = EarlyStopping(verbose=1, patience=3)

    def load_base_model(self):
        self.model = tf.keras.models.load_model(self.config.custom_trained_model_path)

    def train_val_data_generator(self):
        datagenerator_kwargs = dict(rescale=1.0 / 255, validation_split=0.20)

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear",
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.validation_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs,
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs,
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs,
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def train_model(self):
        self.steps_per_epoch = (
            self.train_generator.samples // self.train_generator.batch_size
        )
        self.validation_steps = (
            self.valid_generator.samples // self.valid_generator.batch_size
        )

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=[self.checkpoint, self.early_stopping],
        )

        # self.save_model(path=self.config.trained_model_path, model=self.model)
