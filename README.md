
# End-to-End AI Cold Email Generation Tool

![Image](https://github.com/user-attachments/assets/7ec6fb3c-61fc-45f8-b6f6-7c058b6472f2)

An AI-powered tool designed to streamline the process of generating cold emails for businesses seeking contract-based clients. Companies such as HCL, Microsoft, and Google often provide contract-based employees to clients like Nike or Adidas. Instead of hiring full-time software developers, these companies can use this tool to automatically send personalized cold emails to potential clients, saving time and reducing the hassle of manual email crafting.

### Key Features
- **AI-Powered**: Uses the latest version of the Llama model for generating natural, personalized cold emails.
- **End-to-End Solution**: The tool requires only a link to the target client’s profile, and it generates a tailored email.
- **Time Efficiency**: Automates email generation to help companies focus on their core business without worrying about crafting emails.
- **Ideal for Contract-Based Clients**: Perfect for companies offering contract-based employees to large organizations.

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Llama API
- Required libraries: `requests`, `llama`, `openai` (or any other dependencies mentioned in the code)

### Usage

1. Open the Jupyter Notebook and run the cells sequentially for better understanding of groq api, chromadb, email generation.
2. The tool will ask for a link to the potential client's profile (e.g., Nike, Adidas).
3. Upon submission, the AI will generate a cold email tailored for the client.

### Example Flow

1. Provide the URL to the client profile (e.g., a LinkedIn profile or company page).
2. The tool uses the latest Llama version to generate a personalized cold email.
3. The email is ready to be sent to potential clients, without the need for manual drafting.

### Project Workflow

1. **Data Extraction**: The client’s profile is used to extract relevant information.
2. **Email Generation**: Llama model is utilized to generate a personalized email based on the extracted information.
3. **Email Customization**: The generated email is formatted and customized based on the target client's industry and needs.

### Example:

- **Input**: "Nike"
- **Generated Email**:
  ```text
  Subject: Transform Your Workforce with Top-Notch Developers

  Hi Nike Team,

  I hope this message finds you well! My name is [Your Name], and I represent [Your Company]. We specialize in providing highly skilled contract-based software developers who can seamlessly integrate with your existing team.

  Given Nike's innovative spirit and commitment to excellence, we believe our developers can contribute significantly to your next big project. Whether it’s scaling your tech team or meeting tight deadlines, we’re here to support you.

  Would you be open to a conversation about how we can assist Nike with your upcoming initiatives?

  Best regards,
  [Your Name]
  ```

### Deployment 

Deployed Link : https://coldmail-pro-production-b581.up.railway.app/ 

It can be deployed on strealit, as an alternative can deploy on railway. 

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


