This project creates a Research Assistant Agent using the Groq API and Streamlit. It leverages the Llama model to answer user queries, offering quick solutions and explaining technical concepts. The application is easily deployable with `requirements.txt` managing dependencies and a Cloudflared local tunnel for public access.

## Features

*   Integration with Groq API for powerful language models.
*   Interactive user interface built with Streamlit.
*   Leverages Llama model for research assistance.
*   Real-time explanations of technical concepts.
*   Easy deployment using `requirements.txt` and Cloudflared for tunneling.

## Functionality of the Application
You can check the functionality of this model by clicking the drive's link below:
https://drive.google.com/file/d/1w8SXvmVBcHom4NIX7Vo6ekxl0DwIcRAw/view?usp=drive_link 

Link to the Web Application:
https://researchaiassistant.streamlit.app/

## Technologies Used
*   Python
*   Groq API
*   Streamlit
*   Cloudflared

## Setup / Installation
To get this project up and running on your local machine, follow these steps:
**1. Clone the repository:**
```bash
git clone https://github.com/FamerTech/Research-Assistant-Agent.git
cd /Research-Assistant-Agent
```
**2. Install dependencies:**
Make sure you have `pip` installed. Then, install the required Python packages:
```bash
pip install -r requirements.txt
```

**3. Set up Groq API Key:**

You will need a Groq API key. You can obtain one from the https://console.groq.com. Once you have your key, set it as an environment variable or create a `.env` file in the root of your project:

**Option A: Environment Variable**

```bash
export GROQ_API_KEY="YOUR_GROQ_API_KEY"
```

**Option B: `.env` file**

Create a file named `.env` in the project root with the following content:

```
GROQ_API_KEY="YOUR_GROQ_API_KEY"
```

Replace `YOUR_GROQ_API_KEY` with your actual Groq API key.

**4. Run the Streamlit application:**

```bash
streamlit run app.py
```

This will start the Streamlit application, usually accessible at `http://localhost:8501`.

**5. (Optional) For local tunnel with Cloudflared:**

If you want to expose your local Streamlit application to the internet, you can use Cloudflared. First, install Cloudflared if you haven't already:

```bash
npm install -g cloudflared # Or use your preferred method for your OS
```

Then, run the tunnel command:

```bash
cloudflared tunnel --url http://localhost:8501
```

Cloudflared will provide you with a public URL to access your Streamlit application.

## Usage

*   Once the Streamlit app is running (either locally or via Cloudflared tunnel), open your web browser and navigate to the provided address.
*   You will see an input field where you can type your research questions.
*   Enter your query, and the AI assistant, powered by the Llama model via the Groq API, will provide answers and explanations.
