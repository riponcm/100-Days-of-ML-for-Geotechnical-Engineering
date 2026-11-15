# Day 083: Model Deployment (ONNX, TorchScript)

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Exporting PyTorch models to ONNX format
- TorchScript: tracing and scripting for deployment
- Model optimization: quantization and pruning
- Serving models with Flask/FastAPI REST APIs
- Edge deployment considerations for field applications

## Key Takeaways

1. ONNX provides a framework-agnostic format for deploying models across different platforms and runtimes.
2. TorchScript converts dynamic PyTorch models into a static graph that can run without Python.
3. Model deployment enables geotechnical engineers to use trained models in the field via web APIs or mobile applications.

## Code Summary

- Exported a trained model to ONNX and TorchScript, built a simple REST API for predictions, and benchmarked inference speed

## Geotechnical Application

- Deploying trained geotechnical ML models for field use, enabling real-time predictions during site investigations or construction monitoring

## Resources

- [PyTorch Deployment Tutorial](https://pytorch.org/tutorials/beginner/onnx/export_simple_model_to_onnx_tutorial.html)
- [ONNX Runtime](https://onnxruntime.ai/)

---

> *Day 083 of 100 — 100 Days of ML for Geotechnical Engineering*
