1. This is a sample repo in the specified format as mentioned in the Skyserve Model Submission Guideline
2. main.py is the main script containing pre-processing/inference/post-processing logic and gives out the final output
3. SampleData folder contains the sample Image and its corresponding expected output.
4. To run this model, follow the following steps:
    a. Create a virtual environment:        python -m venv mnist-model-repo
    b. Activate the virtual environment:    mnist-model-repo\Scripts\activate
    c. Install the requirements:            pip install -r requirements.txt
    d. Run the main script:                 python main.py
    e. Remove the virtual env once done:    rm -r model-env