from langchain.memory import ConversationBufferMemory

def criar_memoria():
    return ConversationBufferMemory(
        return_messages=True,
        memory_key="historico",
        input_key="user_input",
        output_key="assistant_response"
    )
