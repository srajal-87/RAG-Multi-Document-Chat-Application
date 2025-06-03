# 📚 RAG Multi-Document Chat Application

A powerful **Retrieval-Augmented Generation (RAG)** application built with Streamlit that allows users to upload multiple documents and engage in intelligent conversations with their content. Ask questions about your documents and get accurate, context-aware responses powered by OpenAI's GPT models.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)

## 🌟 Features

- **Multi-format Support**: Upload and process PDF, DOCX, and TXT files
- **Intelligent Chat Interface**: Ask questions about your documents using natural language
- **Real-time Processing**: View file processing status and document information
- **Context-Aware Responses**: Get answers based solely on your uploaded documents
- **Memory Management**: Maintains conversation history for contextual discussions
- **Clean UI**: Professional Streamlit interface with intuitive design
- **Error Handling**: Robust error handling with user-friendly messages

## 🚀 Demo

### Key Capabilities:
- Upload multiple documents simultaneously
- Process various file formats (PDF, DOCX, TXT)
- Ask complex questions about document content
- Get accurate responses with source attribution
- Maintain conversation context across queries

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **LLM**: OpenAI GPT-4o-mini
- **Embeddings**: OpenAI Embeddings
- **Vector Store**: FAISS (Facebook AI Similarity Search)
- **Document Processing**: PyPDF2, python-docx
- **Framework**: LangChain
- **Memory**: ConversationBufferMemory

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Git (for cloning the repository)

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/rag-document-chat.git
cd rag-document-chat
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the Application
```bash
streamlit run RAG-app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📦 Installation

### Using requirements.txt

Create a `requirements.txt` file:
```txt
streamlit>=1.28.0
PyPDF2>=3.0.1
python-docx>=0.8.11
langchain>=0.0.350
langchain-community>=0.0.10
langchain-openai>=0.0.5
faiss-cpu>=1.7.4
python-dotenv>=1.0.0
```

Then install:
```bash
pip install -r requirements.txt
```

## 🎯 Usage

### 1. **Upload Documents**
   - Click "Browse files" in the sidebar
   - Select multiple PDF, DOCX, or TXT files
   - Review the uploaded files list

### 2. **Process Documents**
   - Click "🔄 Process Documents" button
   - Wait for processing completion
   - Check processing status for each file

### 3. **Start Chatting**
   - Type your question in the input field
   - Press Enter to get AI-generated responses
   - Continue the conversation with follow-up questions

### 4. **Reset Chat**
   - Use "Reset Chat" button to clear conversation history
   - Upload new documents as needed

## 🏗️ Project Structure

```
rag-document-chat/
│
├── RAG-app.py              # Main application file
├── htmlTemplates.py        # HTML templates for chat interface
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for providing the GPT models
- [LangChain](https://python.langchain.com/) for the RAG framework
- [Streamlit](https://streamlit.io/) for the web application framework
- [FAISS](https://github.com/facebookresearch/faiss) for vector similarity search

---

⭐ **Star this repository if you find it helpful!**

*Built with ❤️ using Python and Streamlit*
