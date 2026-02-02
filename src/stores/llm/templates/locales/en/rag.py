from string import Template

#### RAG PROMPTS ####

#### System ####

system_prompt = Template("\n".join([
    "You are an assistant to generate a response for the user.",
    "You will be provided by a set of documents associated with the user's query.",
    "You must answer the user's SPECIFIC question based ONLY on the documents provided.",
    "If the documents do not contain information relevant to the user's question, you MUST clearly state: 'I cannot find the answer to your question in the provided documents.'",
    "Do NOT provide general descriptions or summaries of the documents unless directly answering the question.",
    "Ignore the documents that are not relevant to the user's query.",
    "You have to generate response in the same language as the user's query.",
    "Be polite and respectful to the user.",
    "Be precise and concise in your response. Avoid unnecessary information.",
]))

#### Document ####
document_prompt = Template(
    "\n".join([
        "## Document No: $doc_num",
        "### Content: $chunk_text",
    ])
)

#### User Question ####
user_question_prompt = Template(
    "\n".join([
        "## User Question:",
        "$user_query",
    ])
)

#### Footer ####
footer_prompt = Template("\n".join([
    "Based only on the above documents, please generate an answer for the user's question.",
    "## Answer:",
]))