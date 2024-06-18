import gradio as gr
from boneFractureClassification.pipeline.prediction import PredictionPipeline
from boneFractureClassification.utils.common import decodeImage


def prediction(img):
    #decodeImage(img, "inputImage.jpg")
    classifier = PredictionPipeline("inputImage.jpg")
    result = classifier.predict()[0]["image"]
    print(result)
    return result
    
if __name__ == "__main__":
    app = gr.Interface(prediction,
                       gr.inputs.Image(type="pil"),
                       outputs=gr.outputs.Label(num_top_classes=2),
                       capture_session=True,
                       server_name="0.0.0.0")
    app.launch(share=True)