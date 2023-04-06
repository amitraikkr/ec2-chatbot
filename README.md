# ec2-chatbot


## Installation
1. Clone the repository

2. Folder structure will be

```
ec2-chatbot/
│
├── extension/
│   ├── manifest.json
│   ├── index.html
│   ├── script.js
│   ├── styles.css
│   └── icon.png
│   └── jquery-3.6.4.min
│
├── lambda/
│   ├── lambda_function.py
│   └── parameters.json
```

3. Install Python Dependencies, package them in a layer to upload on AWS

   ```pip install boto3 openai ```

4. Create a OpenAI API key and store it in a parameters.json file


5. Deploy the AWS Lambda function using the AWS CLI or the AWS Console.

6. Load the extension in Chrome by going to chrome://extensions and clicking on "Load unpacked" to select the extension directory.


Usage
-
1. Click on the extension icon in the toolbar to open the chatbot window.
2. Type in a message and press enter to send it to the chatbot.
3. The chatbot will respond with the appropriate message based on the user's input.

