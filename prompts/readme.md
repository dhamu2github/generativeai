<!-- GETTING STARTED -->
### Quick Start

To quickly build a chatbot, you will need some pretrained models from providers like OpenAI, Groq, etc.
For this project, we will use the Groq API, which is currently free. You will need to obtain an API key from Groq to use their models.


### Installation

1. Get a free API Key at [https://console.groq.com/keys](https://console.groq.com/keys)
2. Clone the repo
   ```sh
   git clone https://github.com/dhamu2github/generativeai.git
   ```
3. Install GROQ Packages
   ```sh
   pip install groq
   ```
4. Install Chainlit Packages
   ```sh
   pip install chainlit
   ```
5. Configure the API keys into your local environment
   ```sh
   export GROQ_API_KEY=<your-api-key-here>
   ```
6. Start your server by running the code
   ```sh
   chainlit run chatbot.py -w
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To interact with your chatbot, open your browser and go to:

http://localhost:8000  (or) http://localhost:<check_the_port_number_you_started>

or check the correct port number in the terminal if it's different.

For more information and documentation, refer to the following links:

1. [Groq Documentation](https://console.groq.com/docs/quickstart)
2. [Chainlit Documentation](https://docs.chainlit.io/get-started/pure-python)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
